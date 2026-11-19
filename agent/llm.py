"""One interface for every model call, with swappable backends.

Backends:
- claude_code (default): shells out to `claude -p` with --json-schema. Runs on
  the user's Claude Code login, so no API key or API budget is needed.
- anthropic_api: the Anthropic Python SDK with structured outputs
  (`client.messages.parse`). Needs ANTHROPIC_API_KEY. The production path.
- replay: returns cached responses only. Re-scoring a past run costs nothing.

Every backend returns a pydantic object validated against the step's schema.
Business-rule validators (for example "MET needs a quote") run on top of the
JSON schema; a violation is fed back to the model for one retry.

Every call is cached by hash(backend-independent request) under runs/cache/, so
a repeated run with unchanged prompts and inputs is free and deterministic.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel, ValidationError

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "runs" / "cache"

T = TypeVar("T", bound=BaseModel)


class LLMError(RuntimeError):
    pass


@dataclass
class CallRecord:
    """Usage for one model call. Written to the audit log and usage.jsonl."""

    step: str
    prompt_id: str
    model: str
    backend: str
    effort: str | None
    input_tokens: int = 0
    cached_input_tokens: int = 0
    output_tokens: int = 0
    cost_usd_list: float = 0.0  # list-price equivalent, even on a subscription
    latency_s: float = 0.0
    cache_hit: bool = False
    attempts: int = 1
    request_hash: str = ""


@dataclass
class LLMConfig:
    backend: str = field(default_factory=lambda: os.environ.get("PA_AGENT_BACKEND", "claude_code"))
    model: str = field(default_factory=lambda: os.environ.get("PA_AGENT_MODEL", "claude-opus-5-5"))
    effort: str | None = None
    timeout_s: int = 600
    use_cache: bool = True


def _request_hash(model: str, effort: str | None, system: str, user: str, schema: dict) -> str:
    blob = json.dumps(
        {"model": model, "effort": effort, "system": system, "user": user, "schema": schema},
        sort_keys=True,
    )
    return hashlib.sha256(blob.encode()).hexdigest()[:24]


def _cache_get(h: str) -> dict | None:
    p = CACHE_DIR / f"{h}.json"
    return json.loads(p.read_text()) if p.exists() else None


def _cache_put(h: str, data: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / f"{h}.json").write_text(json.dumps(data, indent=2, default=str))


# --------------------------------------------------------------------------
# Backends. Each returns (raw_json_dict, usage_dict).
# --------------------------------------------------------------------------


def _call_claude_code(cfg: LLMConfig, system: str, user: str, schema: dict) -> tuple[dict, dict]:
    cmd = [
        "claude", "-p",
        "--model", cfg.model,
        "--output-format", "json",
        "--json-schema", json.dumps(schema),
        "--system-prompt", system,
        "--tools", "",                 # no tools: the model sees only what we pass it
        "--no-session-persistence",
        "--strict-mcp-config",         # no MCP servers
        "--setting-sources", "",       # ignore user/project settings and CLAUDE.md
    ]
    if cfg.effort:
        cmd += ["--effort", cfg.effort]
    # Run from an empty temp dir so no project files or CLAUDE.md leak into context.
    with tempfile.TemporaryDirectory() as cwd:
        proc = subprocess.run(
            cmd, input=user, capture_output=True, text=True, timeout=cfg.timeout_s, cwd=cwd
        )
    if proc.returncode != 0:
        raise LLMError(f"claude -p failed ({proc.returncode}): {proc.stderr.strip()[:500]}")
    out = json.loads(proc.stdout)
    if out.get("is_error") or out.get("subtype") != "success":
        raise LLMError(f"claude -p error: {out.get('subtype')} {out.get('result', '')[:300]}")
    if out.get("structured_output") is None:
        raise LLMError("claude -p returned no structured_output")
    u = out.get("usage", {})
    usage = {
        "input_tokens": u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0),
        "cached_input_tokens": u.get("cache_read_input_tokens", 0),
        "output_tokens": u.get("output_tokens", 0),
        "cost_usd_list": out.get("total_cost_usd", 0.0),
    }
    return out["structured_output"], usage


def _call_anthropic_api(cfg: LLMConfig, system: str, user: str, schema_cls: type[BaseModel]) -> tuple[dict, dict]:
    import anthropic  # imported lazily so the default backend needs no API key

    client = anthropic.Anthropic()
    kwargs = {}
    if cfg.effort:
        kwargs["output_config"] = {"effort": cfg.effort}
    resp = client.messages.parse(
        model=cfg.model,
        max_tokens=16000,
        system=system,
        messages=[{"role": "user", "content": user}],
        output_format=schema_cls,
        **kwargs,
    )
    if resp.stop_reason == "refusal":
        raise LLMError(f"refusal: {getattr(resp, 'stop_details', None)}")
    u = resp.usage
    usage = {
        "input_tokens": (u.input_tokens or 0) + (u.cache_creation_input_tokens or 0),
        "cached_input_tokens": u.cache_read_input_tokens or 0,
        "output_tokens": u.output_tokens or 0,
        "cost_usd_list": 0.0,  # filled from evals/prices.yaml by the harness
    }
    return resp.parsed_output.model_dump(mode="json"), usage


def _with_backoff(fn, waits=(20, 60)):
    """Retry a backend call on process-level failures (rate limit, overload, timeout)."""
    for wait in (*waits, None):
        try:
            return fn()
        except (LLMError, subprocess.TimeoutExpired):
            if wait is None:
                raise
            time.sleep(wait)


# --------------------------------------------------------------------------
# Public entry point
# --------------------------------------------------------------------------


def structured_call(
    *,
    step: str,
    prompt_id: str,
    system: str,
    user: str,
    schema: type[T],
    cfg: LLMConfig | None = None,
) -> tuple[T, CallRecord]:
    """Run one model call and return a validated `schema` instance plus usage."""
    cfg = cfg or LLMConfig()
    json_schema = schema.model_json_schema()
    h = _request_hash(cfg.model, cfg.effort, system, user, json_schema)
    rec = CallRecord(step=step, prompt_id=prompt_id, model=cfg.model, backend=cfg.backend,
                     effort=cfg.effort, request_hash=h)

    if cfg.use_cache and (cached := _cache_get(h)) is not None:
        rec.cache_hit = True
        return schema.model_validate(cached["output"]), rec
    if cfg.backend == "replay":
        raise LLMError(f"replay backend: no cached response for {step}/{prompt_id} ({h})")

    attempt_user = user
    last_err: Exception | None = None
    t0 = time.monotonic()
    for attempt in (1, 2):
        rec.attempts = attempt
        if cfg.backend == "claude_code":
            raw, usage = _with_backoff(lambda: _call_claude_code(cfg, system, attempt_user, json_schema))
        elif cfg.backend == "anthropic_api":
            raw, usage = _call_anthropic_api(cfg, system, attempt_user, schema)
        else:
            raise LLMError(f"unknown backend {cfg.backend!r}")
        for k, v in usage.items():
            setattr(rec, k, getattr(rec, k) + v)
        try:
            obj = schema.model_validate(raw)
        except ValidationError as e:
            last_err = e
            attempt_user = (
                f"{user}\n\n<validation_error>\nYour previous output was rejected:\n{e}\n"
                "Return a corrected output that satisfies every rule.\n</validation_error>"
            )
            continue
        rec.latency_s = round(time.monotonic() - t0, 2)
        if cfg.use_cache:
            _cache_put(h, {"step": step, "prompt_id": prompt_id, "model": cfg.model, "output": raw})
        return obj, rec

    rec.latency_s = round(time.monotonic() - t0, 2)
    raise LLMError(f"{step}: output failed validation twice: {last_err}")
