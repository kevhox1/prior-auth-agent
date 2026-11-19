"""Audit log: one JSON line per pipeline step, with prompt version, model and usage."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from agent.llm import CallRecord
from agent.schemas import AuditEvent


class AuditLog:
    def __init__(self, request_id: str):
        self.request_id = request_id
        self.events: list[AuditEvent] = []

    def log(self, step: str, rec: CallRecord | None = None, **payload) -> None:
        ev = AuditEvent(timestamp=datetime.now(timezone.utc), request_id=self.request_id, step=step,
                        payload=payload)
        if rec is not None:
            pid, _, ver = rec.prompt_id.partition("@")
            ev = ev.model_copy(update=dict(
                prompt_id=pid, prompt_version=ver or None, model=rec.model,
                input_tokens=rec.input_tokens + rec.cached_input_tokens, output_tokens=rec.output_tokens,
                latency_s=rec.latency_s,
                payload={**payload, "backend": rec.backend, "effort": rec.effort, "cache_hit": rec.cache_hit,
                         "attempts": rec.attempts, "cost_usd_list": rec.cost_usd_list,
                         "request_hash": rec.request_hash},
            ))
        self.events.append(ev)

    def write(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as f:
            for ev in self.events:
                f.write(json.dumps(ev.model_dump(mode="json"), default=str) + "\n")

    def totals(self) -> dict:
        calls = [e for e in self.events if e.model]
        return {
            "model_calls": len(calls),
            "input_tokens": sum(e.input_tokens or 0 for e in calls),
            "output_tokens": sum(e.output_tokens or 0 for e in calls),
            "latency_s": round(sum(e.latency_s or 0 for e in calls), 1),
            "cost_usd_list": round(sum(e.payload.get("cost_usd_list", 0) for e in calls), 4),
            "cache_hits": sum(1 for e in calls if e.payload.get("cache_hit")),
        }
