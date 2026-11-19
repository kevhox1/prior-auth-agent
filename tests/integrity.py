"""Shared integrity checks for hand-built and synthetic cases."""

from pathlib import Path

from agent import intake
from agent.checks import quote_in_text
from agent.schemas import Status, outcome_for


def check_case(case_id: str, cases_dir: Path, charts_dir: Path) -> None:
    req = intake.load_request(case_id, cases_dir)
    gold = intake.load_gold(case_id, cases_dir)
    chart = intake.load_chart(req.patient_id, charts_dir)
    checklist = intake.load_gold_checklist(gold.policy_id)

    assert gold.request_id == req.request_id
    assert checklist.payer == req.payer and checklist.drug == req.drug
    assert all(d.patient_id == req.patient_id for d in chart.documents)
    assert all(d.date <= req.request_date for d in chart.documents), "document dated after request"
    assert set(gold.criteria) == {c.id for c in checklist.leaves()}
    leaf_status = {cid: g.status for cid, g in gold.criteria.items()}
    assert outcome_for(checklist, leaf_status) == gold.packet_outcome
    assert gold.routing.channels == checklist.benefit_channel
    for cid, g in gold.criteria.items():
        for ev in g.evidence:
            doc = chart.get(ev.doc_id)
            assert doc is not None, f"{case_id} {cid}: unknown doc {ev.doc_id}"
            assert quote_in_text(ev.quote, doc.text), f"{case_id} {cid}: quote not in {ev.doc_id}: {ev.quote!r}"
        if g.status == Status.MET:
            assert g.evidence, f"{case_id} {cid}: MET gold with no evidence"
        if g.status in (Status.INSUFFICIENT_EVIDENCE, Status.CONFLICTING):
            assert g.missing_item, f"{case_id} {cid}: non-MET gold must say what would resolve it"
        if g.status == Status.CONFLICTING:
            assert len({e.doc_id for e in g.evidence}) >= 2, f"{case_id} {cid}: conflict needs two documents"
