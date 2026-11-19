"""Gold labels from blueprint states. Code only; no model is involved.

Blueprint states describe the chart (for example "C6=met_borderline" means the
only TB screen is about 11.8 months old). What that chart means depends on the
payer's policy: under Northfield (12-month TB window) it is MET, under Calder
(6-month window) it is NOT_MET. STATUS is the Northfield table; CALDER_STATUS
overrides only the states whose meaning changes.
"""

from __future__ import annotations

from agent.schemas import CaseGold, Citation, GoldCriterion, GoldRouting, PolicyChecklist, Status, outcome_for
from synth.blueprint import Blueprint
from synth.render import Rendered

M, N, I, C = Status.MET, Status.NOT_MET, Status.INSUFFICIENT_EVIDENCE, Status.CONFLICTING

# state -> (gold status, acceptable alternates). Northfield policy NHP-CCP-RX-0412.
STATUS: dict[str, dict[str, tuple[Status, list[Status]]]] = {
    "C1": {"met_clean": (M, []), "not_met_mild": (N, [])},
    "C2": {"met_scope": (M, []), "met_fcp": (M, []), "met_buried": (M, []), "met_borderline": (M, []),
           # Stale evidence of the right kind is NOT_MET, the same rule as a stale TB screen (spec 7.1).
           # Evidence of the wrong kind (CRP only) is INSUFFICIENT: the required item is absent (B32).
           "crp_only": (I, [N]), "stale_scope": (N, [I])},
    "C3": {"met_clean": (M, [])},
    "C4": {"met_clean": (M, [])},
    "C5a": {"met_clean": (M, []), "met_buried": (M, []), "missing": (I, [N])},
    "C5b": {"met_clean": (M, []), "met_buried": (M, []), "contraindication": (M, []),
            "conflicting": (C, [N]), "not_met_naive": (N, []), "insurance_stop": (N, [I])},
    "C6": {"met_clean": (M, []), "met_borderline": (M, []), "positive_with_plan": (M, []),
           # Indeterminate IGRA: practice is to repeat the test, so it is a gap, not a failure (B25).
           "stale": (N, [I]), "indeterminate": (I, []), "missing": (I, []), "ordered_not_resulted": (I, [])},
    "C7": {"met_clean": (M, []), "core_positive_with_plan": (M, []),
           "partial": (I, []), "decoy": (I, []), "missing": (I, [])},
    "C8": {"met_clean": (M, []), "switch_with_stop": (M, []), "not_met_combo": (N, [])},
    "C9": {"met_clean": (M, []), "met_borderline": (M, []), "wrong_tier": (N, []), "stale_weight": (I, [])},
    "C10": {"met_clean": (M, []), "not_met_reference": (N, [])},
}

# Calder Mutual policy CM-RX-217. Only states whose meaning differs are listed.
CALDER_STATUS: dict[str, dict[str, tuple[Status, list[Status]]]] = {
    # B.2: endoscopy only. Calprotectin-only charts are missing the required procedure.
    "C2": {"met_fcp": (I, [N]), "met_buried": (I, [N]), "met_borderline": (I, [N]), "stale_scope": (N, [I])},
    # B.5(b): any advanced-therapy failure, or a TNF-blocker contraindication. Naive is still not met.
    "C5b": {"not_met_naive": (N, [I])},
    # B.6: 6-month window. An 11.8-month-old negative screen is stale here.
    "C6": {"met_borderline": (N, [I])},
    # B.9: weight within 90 days. A 45-80 day old weight is current enough.
    "C9": {"stale_weight": (M, [])},
}
CALDER_MISSING = {
    "C2": "Ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report from the past 12 months showing active "
          "inflammation (calprotectin and CRP do not count under this policy).",
    "C6": "TB screening (IGRA or TST) with a negative result dated within 6 months of the request.",
}
KEEP_RENDERED_MISSING = {("C6", "indeterminate"), ("C6", "ordered_not_resulted")}

MISSING_DEFAULTS = {
    "C5a": "Documentation of a trial of at least one conventional therapy (corticosteroid, thiopurine, "
           "methotrexate, or for UC an aminosalicylate) with dates and reason stopped.",
}


def status_for(payer: str, cid: str, state: str) -> tuple[Status, list[Status]]:
    if payer == "calder" and state in CALDER_STATUS.get(cid, {}):
        return CALDER_STATUS[cid][state]
    return STATUS[cid][state]


def _has_out_of_window_endoscopy(r: Rendered) -> bool:
    """Any endoscopy in the chart: a procedure report, or a note that reports an old scope (crp_only)."""
    if any(d.doc_type == "procedure_report" and ("colonoscopy" in d.stem or "sigmoidoscopy" in d.stem) for d in r.docs):
        return True
    return any("showed active disease" in ln and ln.startswith("Last ") for d in r.docs for ln in d.lines)


def _apply_stale_rule(cid: str, status: Status, alts: list[Status], r: Rendered) -> tuple[Status, list[Status]]:
    """B32, applied to what the chart contains rather than the state name: when C2 is not met and the
    chart holds an endoscopy that is out of the window, the right kind of evidence is stale -> NOT_MET."""
    if cid == "C2" and status == I and _has_out_of_window_endoscopy(r):
        return N, [I]
    return status, alts


def case_type(bp: Blueprint, statuses: dict[str, Status]) -> str:
    problems = [s for s in statuses.values() if s != M]
    if len(problems) >= 2:
        return "multi_issue"
    if len(problems) == 1:
        return {I: "missing_item", N: "not_met", C: "conflicting"}[problems[0]]
    if any(v in ("met_buried",) for v in bp.states.values()):
        return "buried_evidence"
    if any(v in ("met_borderline", "positive_with_plan", "core_positive_with_plan", "switch_with_stop",
                 "contraindication", "stale_weight") for v in bp.states.values()):
        return "borderline"
    return "clean"


def _evidence(bp: Blueprint, r: Rendered, cid: str) -> list[Citation]:
    ev = r.evidence.get(cid, [])
    if bp.payer == "calder" and cid == "C2":
        # Only a procedure report can prove B.2; a calprotectin line is not evidence for it.
        ev = [e for e in ev if any(k in e.doc_id for k in ("colonoscopy", "sigmoidoscopy"))]
    return ev


def _missing(bp: Blueprint, r: Rendered, cid: str, state: str, status: Status) -> str | None:
    if status == M:
        return None
    if bp.payer == "calder" and cid in CALDER_MISSING and (cid, state) not in KEEP_RENDERED_MISSING:
        return CALDER_MISSING[cid]
    return r.missing_item.get(cid) or (MISSING_DEFAULTS.get(cid) if status in (I, C) else None)


def label(bp: Blueprint, r: Rendered, checklist: PolicyChecklist) -> CaseGold:
    crit: dict[str, GoldCriterion] = {}
    statuses: dict[str, Status] = {}
    for leaf in checklist.leaves():
        cid = leaf.id
        state = bp.states[cid]
        status, alts = _apply_stale_rule(cid, *status_for(bp.payer, cid, state), r)
        statuses[cid] = status
        crit[cid] = GoldCriterion(
            status=status,
            acceptable_alternates=alts,
            evidence=_evidence(bp, r, cid),
            missing_item=_missing(bp, r, cid, state, status),
            note=f"synthetic state: {state}",
        )
    return CaseGold(
        request_id=bp.request_id,
        case_type=case_type(bp, statuses),
        policy_id=checklist.policy_id,
        description=f"Synthetic case (seed {bp.seed}, payer {bp.payer}). States: "
                    + ", ".join(f"{k}={v}" for k, v in bp.states.items() if v != "met_clean"),
        routing=GoldRouting(
            pa_required=True,
            channels=dict(checklist.benefit_channel),
            requested_channel_ok=False if bp.knobs.requested_channel_wrong else None,
        ),
        criteria=crit,
        packet_outcome=outcome_for(checklist, statuses),
        expect_injection_flag=bp.knobs.injection,
    )
