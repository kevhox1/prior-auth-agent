"""Step 9: independent verification.

A separate model call that sees only the request, the packet and the chart. It
does not see the checklist reasoning, the retrieval passages or the drafting
prompt, so it cannot inherit the drafter's mistakes. Code makes sure every
claim got a check; an unchecked claim counts as unsupported.
"""

from __future__ import annotations

import json

from agent.llm import CallRecord, LLMConfig, structured_call
from agent.prompts import load_prompt
from agent.render import chart_block, request_block
from agent.schemas import Chart, ClaimCheck, PacketDraft, PARequest, VerificationDraft

PROMPT = "verify@v1"


def claim_refs(packet: PacketDraft) -> list[str]:
    return ([f"form:{f.name}" for f in packet.form_fields]
            + [f"letter:{i}" for i, s in enumerate(packet.letter) if s.is_factual])


def verify(req: PARequest, chart: Chart, packet: PacketDraft, cfg: LLMConfig | None = None
           ) -> tuple[VerificationDraft, CallRecord, list[str]]:
    p = load_prompt(PROMPT)
    numbered = {
        "form_fields": [f.model_dump() for f in packet.form_fields],
        "letter": [{"index": i, **s.model_dump()} for i, s in enumerate(packet.letter)],
    }
    user = "\n\n".join([request_block(req), "<packet>\n" + json.dumps(numbered, indent=1) + "\n</packet>",
                        chart_block(chart)])
    v, rec = structured_call(step="verify", prompt_id=p.ref, system=p.text, user=user,
                             schema=VerificationDraft, cfg=cfg)
    notes: list[str] = []
    seen = {c.claim_ref for c in v.checks}
    missing = [r for r in claim_refs(packet) if r not in seen]
    checks = list(v.checks)
    for r in missing:
        notes.append(f"verifier did not check {r}; counted as unsupported")
        checks.append(ClaimCheck(claim_ref=r, supported=False, issue="not checked by the verifier"))
    overall = v.overall_pass and not missing and all(c.supported for c in checks)
    if overall != v.overall_pass:
        notes.append("overall_pass recomputed from the individual checks")
    return VerificationDraft(checks=checks, overall_pass=overall), rec, notes
