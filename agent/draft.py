"""Step 8: packet drafting. Form fields plus a letter of medical necessity, every fact cited.

Runs only when every criterion is MET (spec 7.2). The model sees the request,
the checklist and the quotes that already passed step 6, never the raw chart,
so it cannot pick up a fact that nobody verified. Code then checks every
citation again: verbatim in the cited document (or in the request), same patient.
"""

from __future__ import annotations

import json

from agent.checks import quote_in_text
from agent.llm import CallRecord, LLMConfig, structured_call
from agent.prompts import load_prompt
from agent.render import request_block
from agent.schemas import (
    Chart,
    CriterionAssessment,
    DocType,
    PacketDraft,
    PARequest,
    PolicyChecklist,
    Status,
)

PROMPT = "draft@v2"
REQUEST_DOC = "request"
IDENTITY_FIELDS = ["Member name", "Member date of birth", "Member ID"]
REQUEST_FIELDS = ["Requested product", "Requested regimen", "Diagnosis code (ICD-10)", "Ordering provider",
                  "Requested start date", "Review type"]


def form_field_names(checklist: PolicyChecklist, met_ids: set[str] | None = None) -> list[str]:
    """Identity, request, then one field per MET policy criterion. Derived from the checklist, so a new
    policy (or a new specialty) gets the right form without code changes. Under ANY logic a READY request
    can have an unmet branch (Calder B.5: conventional OR advanced therapy); that branch gets no field."""
    return IDENTITY_FIELDS + REQUEST_FIELDS + [
        f"{leaf.id} (policy {leaf.policy_ref})" for leaf in checklist.leaves() if met_ids is None or leaf.id in met_ids]


def field_key(name: str) -> str:
    """'C6 (policy 3.6): Negative TB screen' and 'C6 (policy 3.6)' are the same field."""
    return name.split(":")[0].strip()


def _describe(key: str, checklist: PolicyChecklist) -> str:
    leaf = next((c for c in checklist.leaves() if key.startswith(f"{c.id} (")), None)
    return leaf.text.split(". ")[0] if leaf else "from the request or the member's registration"


def _evidence_block(chart: Chart, assessments: list[CriterionAssessment]) -> str:
    ev = {a.criterion_id: [e.model_dump(mode="json") for e in a.evidence] for a in assessments}
    demo = next((d for d in chart.documents if d.doc_type == DocType.DEMOGRAPHICS), None)
    if demo:
        ev["member_identity"] = [{"doc_id": demo.doc_id, "doc_date": str(demo.date), "quote": ln.strip()}
                                 for ln in demo.text.splitlines() if ":" in ln and ln.strip()]
    return "<verified_evidence>\n" + json.dumps(ev, indent=1) + "\n</verified_evidence>"


def citation_issues(packet: PacketDraft, chart: Chart, req: PARequest) -> list[str]:
    req_text = json.dumps(req.model_dump(mode="json"))
    issues = []
    cites = [(f"form:{f.name}", c) for f in packet.form_fields for c in f.citations]
    cites += [(f"letter:{i}", c) for i, s in enumerate(packet.letter) for c in s.citations]
    for ref, c in cites:
        if c.doc_id == REQUEST_DOC:
            if not quote_in_text(c.quote, req_text):
                issues.append(f"{ref}: request quote not found: {c.quote[:60]!r}")
            continue
        if not c.doc_id.startswith(f"{req.patient_id}/"):
            issues.append(f"{ref}: cites another patient's document {c.doc_id}")
            continue
        doc = chart.get(c.doc_id)
        if doc is None or not quote_in_text(c.quote, doc.text):
            issues.append(f"{ref}: quote not verbatim in {c.doc_id}: {c.quote[:60]!r}")
    return issues


def draft(req: PARequest, chart: Chart, checklist: PolicyChecklist, assessments: list[CriterionAssessment],
          routing_notes: list[str], cfg: LLMConfig | None = None) -> tuple[PacketDraft, CallRecord, list[str]]:
    p = load_prompt(PROMPT)
    assessments = [a for a in assessments if a.status == Status.MET]  # only verified facts reach the drafter
    fields = form_field_names(checklist, {a.criterion_id for a in assessments})
    user = "\n\n".join([
        request_block(req),
        "<form_fields>\n" + "\n".join(f"- {f}: {_describe(f, checklist)}" for f in fields) + "\n</form_fields>",
        "<benefit_routing>\n" + "\n".join(routing_notes) + "\n</benefit_routing>",
        _evidence_block(chart, assessments),
    ])
    packet, rec = structured_call(step="draft", prompt_id=p.ref, system=p.text, user=user, schema=PacketDraft, cfg=cfg)
    issues = citation_issues(packet, chart, req)
    got = {field_key(f.name) for f in packet.form_fields}
    issues += [f"form field missing: {f}" for f in fields if f not in got]
    return packet, rec, issues
