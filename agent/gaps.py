"""Step 7: gap plan. For each criterion not MET: what is missing, who can supply it,
and a short message staff can send."""

from __future__ import annotations

import json

from agent.llm import CallRecord, LLMConfig, structured_call
from agent.prompts import load_prompt
from agent.render import request_block
from agent.schemas import (
    Criterion, CriterionAssessment, GapItem, GapPlanDraft, PARequest, PolicyChecklist, Status, Supplier, roll_up,
)

PROMPT = "gaps@v2"


def settled_leaves(checklist: PolicyChecklist, assessments: list[CriterionAssessment]) -> set[str]:
    """Leaves under a parent that is already MET, such as the unused branch of an either/or (ANY)
    requirement. They need no to-do item: nothing about them can change the outcome (B41)."""
    status = roll_up(checklist, {a.criterion_id: a.status for a in assessments})
    out: set[str] = set()

    def walk(c: Criterion, covered: bool) -> None:
        covered = covered or (bool(c.sub_criteria) and status.get(c.id) == Status.MET)
        if not c.sub_criteria and covered:
            out.add(c.id)
        for s in c.sub_criteria:
            walk(s, covered)

    for c in checklist.criteria:
        walk(c, False)
    return out


def plan_gaps(req: PARequest, checklist: PolicyChecklist, assessments: list[CriterionAssessment],
              cfg: LLMConfig | None = None) -> tuple[list[GapItem], CallRecord | None, list[str]]:
    settled = settled_leaves(checklist, assessments)
    open_ = [a for a in assessments if a.status != Status.MET and a.criterion_id not in settled]
    if not open_:
        return [], None, []
    items = []
    for a in open_:
        crit = checklist.find(a.criterion_id)
        items.append({
            "criterion_id": a.criterion_id,
            "policy_ref": crit.policy_ref if crit else None,
            "requirement": crit.text if crit else None,
            "status": a.status.value,
            "reasoning": a.reasoning,
            "missing_items": a.missing_items,
            "evidence": [e.model_dump(mode="json") for e in a.evidence],
            "code_check_notes": a.deterministic_checks.notes,
        })
    p = load_prompt(PROMPT)
    user = request_block(req) + "\n\n<open_criteria>\n" + json.dumps(items, indent=1) + "\n</open_criteria>"
    draft, rec = structured_call(step="gaps", prompt_id=p.ref, system=p.text, user=user,
                                 schema=GapPlanDraft, cfg=cfg)
    notes: list[str] = []
    by_id: dict[str, GapItem] = {}
    for g in draft.gaps:
        by_id.setdefault(g.criterion_id, g)
    gaps = []
    for a in open_:
        g = by_id.get(a.criterion_id)
        if g is None:
            notes.append(f"gap plan skipped {a.criterion_id}; added a default item")
            g = GapItem(criterion_id=a.criterion_id,
                        missing_item="; ".join(a.missing_items) or f"Physician review ({a.status.value})",
                        who_can_supply=Supplier.ORDERING_PROVIDER,
                        clinician_query=f"Please review criterion {a.criterion_id}: {a.reasoning}")
        elif a.status in (Status.NOT_MET, Status.CONFLICTING) and g.who_can_supply != Supplier.ORDERING_PROVIDER:
            # D1: these go to the physician, whatever the model suggested.
            notes.append(f"{a.criterion_id}: {a.status.value} routed to ordering_provider (model said {g.who_can_supply.value})")
            g = g.model_copy(update={"who_can_supply": Supplier.ORDERING_PROVIDER})
        gaps.append(g)
    return gaps, rec, notes
