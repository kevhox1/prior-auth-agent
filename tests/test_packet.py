"""Steps 8 to 11 without a model: citation checks, verifier bookkeeping, and the sign-off gate."""

from datetime import datetime, timezone

import pytest

from agent import intake as I
from agent.draft import citation_issues
from agent.schemas import (
    Citation, CitedSentence, ClaimCheck, FormField, PacketDraft, PacketOutcome, PipelineResult,
    ReviewAction, ReviewDecision, SignOff, Status, VerificationDraft,
)
from agent.submit import SignOffBlocked, blockers, final_statuses, mock_submit, required_role


@pytest.fixture()
def pa1():
    req = I.load_request("PA-0001")
    return req, I.load_chart(req.patient_id)


def packet(quote, doc_id):
    return PacketDraft(form_fields=[FormField(name="TB", value="negative", citations=[Citation(doc_id=doc_id, quote=quote)])],
                       letter=[CitedSentence(text="TB screen negative.", citations=[Citation(doc_id=doc_id, quote=quote)])])


def test_citation_check_passes_verbatim_and_request_quotes(pa1):
    req, chart = pa1
    doc = next(d for d in chart.documents if d.doc_type.value == "demographics")
    line = next(ln for ln in doc.text.splitlines() if "Date of birth" in ln)
    pk = packet(line, doc.doc_id)
    pk.form_fields.append(FormField(name="Product", value=req.product, citations=[Citation(doc_id="request", quote=req.product)]))
    assert citation_issues(pk, chart, req) == []


def test_citation_check_catches_fabrication_and_wrong_patient(pa1):
    req, chart = pa1
    assert citation_issues(packet("QuantiFERON NEGATIVE 2026-01-01", chart.documents[0].doc_id), chart, req)
    assert any("another patient" in i for i in citation_issues(packet("x", "PT-0002/labs-2026-10-06"), chart, req))


def test_letter_sentence_needs_citation():
    with pytest.raises(ValueError):
        CitedSentence(text="The patient failed infliximab.", citations=[])


def _result(outcome=PacketOutcome.READY_FOR_REVIEW, verified=True, issues=()):
    """A minimal READY result built from the oracle path's pieces."""
    from tests.test_pipeline import oracle_packet
    gold = I.load_gold("PA-0001")
    cl = I.load_gold_checklist(gold.policy_id)
    req = I.load_request("PA-0001")
    from agent.routing import route
    from agent.schemas import CriterionAssessment, DeterministicChecks, Evidence, IntakeResult, roll_up
    chart = I.load_chart(req.patient_id)
    assessments = [CriterionAssessment(criterion_id=cid, status=g.status, confidence=1, reasoning="r",
                                       evidence=[Evidence(doc_id=e.doc_id, quote=e.quote, doc_date=chart.get(e.doc_id).date)
                                                 for e in g.evidence],
                                       deterministic_checks=DeterministicChecks()) for cid, g in gold.criteria.items()]
    pk = oracle_packet(gold, cl, req)
    return PipelineResult(
        request=req, intake=IntakeResult(request=req, policy_id=gold.policy_id, policy_version=cl.version,
                                         n_documents=len(chart.documents), decision_clock="x"),
        policy_id=gold.policy_id, policy_version=cl.version, routing=route(req), checklist=cl,
        assessments=assessments, rolled_up=roll_up(cl, {a.criterion_id: a.status for a in assessments}),
        outcome=outcome, packet=pk, packet_code_issues=list(issues),
        verification=VerificationDraft(checks=[ClaimCheck(claim_ref="letter:1", supported=verified,
                                                          issue=None if verified else "wrong date")],
                                       overall_pass=verified))


def decide(res, action=ReviewAction.APPROVE, **kw):
    return [ReviewDecision(criterion_id=a.criterion_id, action=action, reviewer="R. Patel", reviewer_role="nurse",
                           timestamp=datetime.now(timezone.utc), **kw) for a in res.assessments]


def sign(role="physician", decision="submit", note=None):
    return SignOff(reviewer="Dr. A. Rivera", reviewer_role=role, decision=decision, note=note,
                   timestamp=datetime.now(timezone.utc))


def test_clean_packet_submits_to_both_rails(tmp_path):
    res = _result()
    sub = mock_submit(res, decide(res), sign(), tmp_path)
    names = sorted(p.name for p in sub.iterdir())
    assert "iv_induction-medical-portal-request.json" in names and "sc_maintenance-pharmacy-epa-request.json" in names
    assert "letter_of_medical_necessity.md" in names


def test_letter_needs_a_physician():
    res = _result()
    assert required_role(res) == "physician"
    assert any("physician" in b for b in blockers(res, decide(res), sign(role="nurse")))


def test_every_criterion_needs_a_decision():
    res = _result()
    assert any("no decision" in b for b in blockers(res, decide(res)[:-1], sign()))


def test_reviewer_edit_to_not_met_blocks_submission(tmp_path):
    res = _result()
    ds = decide(res)
    ds[0] = ds[0].model_copy(update={"action": ReviewAction.EDIT, "reason_code": "wrong_status",
                                     "new_status": Status.NOT_MET})
    assert final_statuses(res, ds)[ds[0].criterion_id] == Status.NOT_MET
    with pytest.raises(SignOffBlocked):
        mock_submit(res, ds, sign(), tmp_path)


def test_verifier_flag_blocks_unless_overridden():
    res = _result(verified=False)
    assert any("verifier" in b for b in blockers(res, decide(res), sign()))
    assert not blockers(res, decide(res), sign(note="Override: checked the 2026-08 lab report myself."))


def test_code_citation_issue_always_blocks():
    res = _result(issues=["letter:2: quote not verbatim"])
    assert any("citation" in b for b in blockers(res, decide(res), sign(note="override")))
