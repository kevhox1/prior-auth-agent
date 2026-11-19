"""Optional realism pass: a model rewrites each templated document.

Runs through agent.llm (default backend: `claude -p` on the user's Claude Code
login). The model never sees the gold labels. After rewriting, the validator
re-checks the planted quotes and forbidden facts; any document that fails keeps
its template text, so the gold labels stay correct either way.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel

from agent.llm import LLMConfig, structured_call

PROMPT = Path(__file__).resolve().parent.parent / "prompts" / "synth_rewrite@v1.md"
NEVER_MENTION = {
    ("C6", "missing"): "any tuberculosis test result",
    ("C6", "ordered_not_resulted"): "any tuberculosis test result",
    ("C7", "missing"): "any hepatitis B test result",
    ("C7", "decoy"): "hepatitis B surface antigen or core antibody results",
    ("C7", "partial"): "hepatitis B core antibody results",
    ("C2", "crp_only"): "fecal calprotectin",
    ("C2", "stale_scope"): "fecal calprotectin",
}


class RewriteOut(BaseModel):
    text: str


def _system() -> str:
    raw = PROMPT.read_text()
    return raw.split("---", 2)[2].strip()


def rewrite_doc(text: str, keep: list[str], never: list[str], cfg: LLMConfig) -> tuple[str, object]:
    user = (
        "<keep_verbatim>\n" + "\n".join(keep or ["(none)"]) + "\n</keep_verbatim>\n"
        "<never_mention>\n" + "\n".join(never or ["(none)"]) + "\n</never_mention>\n"
        f"<document>\n{text}\n</document>"
    )
    out, rec = structured_call(step="synth_rewrite", prompt_id="synth_rewrite@v1",
                               system=_system(), user=user, schema=RewriteOut, cfg=cfg)
    return out.text, rec


def never_list(states: dict[str, str]) -> list[str]:
    return [v for (cid, st), v in NEVER_MENTION.items() if states.get(cid) == st]
