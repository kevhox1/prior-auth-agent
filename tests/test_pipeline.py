"""End-to-end plumbing test with an oracle in place of the model.

The oracle answers every model step with the gold labels. If the pipeline is
wired correctly, the outcome must match gold on every case, and step 6 must not
downgrade a single true MET. The second property is a false-alarm test for the
code checks across all 200 synthetic cases.
"""

from pathlib import Path

import pytest

from agent import assess, draft, gaps, intake as I, policy_extract, retrieve, verify
from agent.audit import AuditLog
from agent.llm import CallRecord, LLMConfig
from agent.pipeline import CaseSource, run_case
from agent.routing import lookup
from agent.schemas import (
    CandidatePassage,
    CaseAssessmentDraft,
    CaseRetrievalDraft,
    CitedSentence,
    Citation,
    ClaimCheck,
    FormField,
    PacketDraft,
    VerificationDraft,
    ChannelEntry,
    CriterionAssessmentDraft,
    Evidence,
    ExtractedCriterion,
    ExtractedSubCriterion,
    GapPlanDraft,
    PolicyExtractionDraft,
    RetrievalDraft,
    Status,
)
from evals.score import score

SYNTH_BATCHES = sorted((I.DATA / "synth").glob("batch-*"))


def extraction_from_gold(cl) -> PolicyExtractionDraft:
    def sub(c):
        return ExtractedSubCriterion(id=c.id, policy_ref=c.policy_ref, type=c.type, text=c.text,
                                     evidence_needed=c.evidence_needed, lookback_months=c.lookback_months)
    return PolicyExtractionDraft(
        version=cl.version, effective_date=cl.effective_date, indications=cl.indications,
        benefit_channels=[ChannelEntry(phase=k, channel=v) for k, v in cl.benefit_channel.items()],
        auth_duration_months=cl.auth_duration_months, logic=cl.logic,
        criteria=[ExtractedCriterion(id=c.id, policy_ref=c.policy_ref, type=c.type, text=c.text,
                                     evidence_needed=c.evidence_needed, lookback_months=c.lookback_months,
                                     logic=c.logic, sub_criteria=[sub(s) for s in c.sub_criteria])
                  for c in cl.criteria],
    )


def install_oracle(monkeypatch, gold, chart, gold_cl):
    def ev(e):
        return Evidence(doc_id=e.doc_id, quote=e.quote, doc_date=chart.get(e.doc_id).date)

    def fake(*, step, prompt_id, system, user, schema, cfg=None):
        rec = CallRecord(step=step, prompt_id=prompt_id, model="oracle", backend="test", effort=None)
        if schema is PolicyExtractionDraft:
            return extraction_from_gold(gold_cl), rec
        if schema is CaseRetrievalDraft:
            return CaseRetrievalDraft(criteria=[
                RetrievalDraft(criterion_id=cid, passages=[
                    CandidatePassage(**ev(e).model_dump(), why_relevant="gold") for e in g.evidence])
                for cid, g in gold.criteria.items()]), rec
        if schema is CaseAssessmentDraft:
            return CaseAssessmentDraft(assessments=[
                CriterionAssessmentDraft(
                    criterion_id=cid, status=g.status, confidence=1.0, evidence=[ev(e) for e in g.evidence],
                    reasoning="oracle", missing_items=[g.missing_item or "item"] if g.status != Status.MET else [])
                for cid, g in gold.criteria.items()]), rec
        if schema is GapPlanDraft:
            return GapPlanDraft(gaps=[]), rec  # exercises the default-gap fallback
        if schema is PacketDraft:
            return oracle_packet(gold, gold_cl, req_for_oracle[0]), rec
        if schema is VerificationDraft:
            pk = oracle_packet(gold, gold_cl, req_for_oracle[0])
            return VerificationDraft(checks=[ClaimCheck(claim_ref=r, supported=True) for r in verify.claim_refs(pk)],
                                     overall_pass=True), rec
        raise AssertionError(schema)

    req_for_oracle = [None]
    for mod in (policy_extract, retrieve, assess, gaps, draft, verify):
        monkeypatch.setattr(mod, "structured_call", fake)
    return req_for_oracle


def oracle_packet(gold, gold_cl, req) -> PacketDraft:
    """A correct packet built from gold evidence: every citation verbatim."""
    c4 = gold.criteria["C4"].evidence[0]
    fields = []
    met = {cid for cid, g in gold.criteria.items() if g.status.value == "MET"}
    for name in draft.form_field_names(gold_cl, met):
        if name in draft.IDENTITY_FIELDS:
            fields.append(FormField(name=name, value="x", citations=[Citation(doc_id=c4.doc_id, quote=c4.quote)]))
        elif name in draft.REQUEST_FIELDS:
            fields.append(FormField(name=name, value=req.product,
                                    citations=[Citation(doc_id="request", quote=req.product)]))
        else:
            cid = name.split(" ")[0]
            fields.append(FormField(name=name, value="met", citations=[
                Citation(doc_id=e.doc_id, quote=e.quote) for e in gold.criteria[cid].evidence]))
    letter = [CitedSentence(text="To the review team:", citations=[], is_factual=False)]
    letter += [CitedSentence(text=f"{cid} is documented.", citations=[Citation(doc_id=e.doc_id, quote=e.quote)
                                                                     for e in g.evidence])
               for cid, g in gold.criteria.items() if cid in met]
    return PacketDraft(form_fields=fields, letter=letter)


def _cases():
    hand = [CaseSource(r, I.DATA / "cases", I.DATA / "charts") for r in I.list_cases()]
    synth = [CaseSource(r, b / "cases", b / "charts") for b in SYNTH_BATCHES for r in I.list_cases(b / "cases")]
    return hand + synth


@pytest.mark.parametrize("src", _cases(), ids=lambda s: s.request_id)
def test_oracle_run_matches_gold(monkeypatch, src):
    req = I.load_request(src.request_id, src.cases_dir)
    gold = I.load_gold(src.request_id, src.cases_dir)
    chart = I.load_chart(req.patient_id, src.charts_dir)
    gold_cl = I.load_gold_checklist(gold.policy_id)
    install_oracle(monkeypatch, gold, chart, gold_cl)[0] = req

    row = lookup(req.payer, req.drug, req.plan_type.value)
    assert row["policy_id"] == gold.policy_id
    cl, _, warns = policy_extract.extract(gold.policy_id, req.payer, req.drug, I.load_policy_prose(gold.policy_id),
                                          row["policy_version"], LLMConfig(backend="replay"))
    assert policy_extract.compare_to_gold(cl, gold_cl)["issues"] == []

    res = run_case(src, cl, AuditLog(src.request_id), LLMConfig(backend="replay"))
    downgraded = {a.criterion_id: a.deterministic_checks.notes for a in res.assessments if a.status_before_checks}
    assert not downgraded, f"step 6 downgraded a gold MET: {downgraded}"
    assert res.outcome == gold.packet_outcome
    assert res.routing.channels == gold.routing.channels
    assert res.routing.requested_channel_ok == gold.routing.requested_channel_ok
    assert all(s.exact for s in score(res, gold, gold_cl))
    settled = gaps.settled_leaves(res.checklist, res.assessments)  # unused branch of a met either/or
    assert {g.criterion_id for g in res.gaps} == {a.criterion_id for a in res.assessments
                                                   if a.status != Status.MET and a.criterion_id not in settled}
    if gold.expect_injection_flag:
        assert res.injection_flags
    # Steps 8 and 9 run exactly when the outcome is READY, and a correct packet passes the code checks.
    assert (res.packet is not None) == (gold.packet_outcome.value == "READY_FOR_REVIEW")
    if res.packet is not None:
        assert res.packet_code_issues == [] and res.verification.overall_pass


def test_paired_cases_share_clinical_content():
    """Paired charts differ only in insurance lines, so gold differences come from policy alone."""
    import csv
    for b in SYNTH_BATCHES:
        rows = list(csv.DictReader((b / "manifest.csv").open()))
        if not rows or not rows[0].get("pair"):
            continue
        by_pair = {}
        for r in rows:
            by_pair.setdefault(r["pair"], {})[r["payer"]] = r["request_id"]
        for pair in by_pair.values():
            if len(pair) != 2:
                continue
            a = I.load_chart(pair["northfield"].replace("PA", "PT"), b / "charts")
            c = I.load_chart(pair["calder"].replace("PA", "PT"), b / "charts")
            assert [d.doc_id.split("/")[1] for d in a.documents] == [d.doc_id.split("/")[1] for d in c.documents]
            for da, dc in zip(a.documents, c.documents):
                diff = [(x, y) for x, y in zip(da.text.splitlines(), dc.text.splitlines()) if x != y]
                assert all(any(k in x for k in ("insurance", "Plan:", "Member ID", "Submit prior")) for x, _ in diff), diff
