from datetime import datetime

import pytest
from pydantic import ValidationError

from agent.schemas import (
    CitedSentence,
    CriterionAssessmentDraft,
    Logic,
    PacketOutcome,
    ReviewDecision,
    Status,
    combine,
    packet_outcome,
)

M, N, I, C = Status.MET, Status.NOT_MET, Status.INSUFFICIENT_EVIDENCE, Status.CONFLICTING


@pytest.mark.parametrize(
    "statuses,expected",
    [([M, M], M), ([M, I], I), ([M, C, I], C), ([I, N, C], N)],
)
def test_combine_all(statuses, expected):
    assert combine(Logic.ALL, statuses) == expected


@pytest.mark.parametrize(
    "statuses,expected",
    [([N, M], M), ([N, N], N), ([N, I], I), ([I, C], C)],
)
def test_combine_any(statuses, expected):
    assert combine(Logic.ANY, statuses) == expected


@pytest.mark.parametrize(
    "statuses,expected",
    [
        ([M, M], PacketOutcome.READY_FOR_REVIEW),
        ([M, I], PacketOutcome.GAPS_TO_CLOSE),
        ([I, C], PacketOutcome.NEEDS_PHYSICIAN),
        ([M, N], PacketOutcome.NEEDS_PHYSICIAN),
    ],
)
def test_packet_outcome(statuses, expected):
    assert packet_outcome(statuses) == expected


def _draft(**kw):
    base = dict(criterion_id="C6", status=M, confidence=0.9, evidence=[], reasoning="x")
    return CriterionAssessmentDraft(**{**base, **kw})


def test_met_requires_quote():
    with pytest.raises(ValidationError, match="MET requires"):
        _draft()


def test_insufficient_requires_missing_item():
    with pytest.raises(ValidationError, match="name the missing item"):
        _draft(status=I)


def test_conflicting_requires_two_documents():
    ev = [{"doc_id": "PT-0001/a", "quote": "q", "doc_date": "2026-01-01"}]
    with pytest.raises(ValidationError, match="at least two"):
        _draft(status=C, evidence=ev)


def test_edit_requires_reason():
    with pytest.raises(ValidationError, match="reason code"):
        ReviewDecision(
            criterion_id="C1", action="edit", reviewer="r", reviewer_role="nurse",
            timestamp=datetime(2026, 11, 18),
        )


def test_factual_sentence_requires_citation():
    with pytest.raises(ValidationError, match="without a citation"):
        CitedSentence(text="TB screen was negative.", citations=[])


def test_met_cannot_be_alternate_for_non_met_gold():
    from agent.schemas import GoldCriterion
    with pytest.raises(ValidationError, match="MET cannot be an acceptable alternate"):
        GoldCriterion(status=C, acceptable_alternates=[M])


def test_score_merged_any_parent_is_not_a_false_met():
    """An agent that kept Calder B.5 as one criterion is scored at the parent, not charged a false MET."""
    from agent import intake as I
    from agent.schemas import Criterion, Logic, Status
    from evals.score import score
    from tests.test_packet import _result

    res = _result()
    gold = I.load_gold("PA-0001")
    gcl = I.load_gold_checklist(gold.policy_id)
    # Merge C5 into one leaf in the agent's checklist, and make gold C5a fail while C5 still holds under ANY.
    merged = [c if c.id != "C5" else Criterion(id="C5", policy_ref="3.5", type=c.type, text=c.text) for c in res.checklist.criteria]
    cl = res.checklist.model_copy(update={"criteria": merged})
    rolled = {**{k: v for k, v in res.rolled_up.items() if k not in ("C5a", "C5b")}, "C5": Status.MET}
    res = res.model_copy(update={"checklist": cl, "rolled_up": rolled,
                                 "assessments": [a for a in res.assessments if a.criterion_id not in ("C5a", "C5b")]})
    gcl_any = gcl.model_copy(update={"criteria": [c.model_copy(update={"logic": Logic.ANY}) if c.id == "C5" else c
                                                  for c in gcl.criteria]})
    g = gold.model_copy(update={"criteria": {**gold.criteria, "C5a": gold.criteria["C5a"].model_copy(
        update={"status": Status.INSUFFICIENT_EVIDENCE, "evidence": []})}})
    sc = {s.gold_id: s for s in score(res, g, gcl_any)}
    assert sc["C5a"].aligned_via == "parent" and not sc["C5a"].false_met and sc["C5a"].correct
