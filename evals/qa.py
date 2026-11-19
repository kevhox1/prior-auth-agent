"""QA agent: one model call per disagreement between the agent and gold.

It sees the gold label and the full chart (the pipeline never does), decides
whether the agent or the gold label is wrong, names a root cause and where the
fix belongs. Code aggregates the findings into docs/QA_REPORT.md.
"""

from __future__ import annotations

import json
from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from agent import intake as I
from agent.llm import LLMConfig, structured_call
from agent.prompts import load_prompt
from agent.render import chart_block
from evals.metrics import CaseEval

PROMPT = "qa_review@v1"


class Verdict(StrEnum):
    AGENT_ERROR = "agent_error"
    GOLD_ERROR = "gold_error"
    AMBIGUOUS = "ambiguous"


class RootCause(StrEnum):
    RETRIEVAL_MISS = "retrieval_miss"
    MISREAD_EVIDENCE = "misread_evidence"
    POLICY_MISREAD = "policy_misread"
    OVER_CAUTION = "over_caution"
    DATE_MATH = "date_math"
    OTHER = "other"
    NONE = "none"


class FixTarget(StrEnum):
    ASSESS_PROMPT = "assess_prompt"
    RETRIEVE_PROMPT = "retrieve_prompt"
    EXTRACT_PROMPT = "extract_prompt"
    CODE_CHECK = "code_check"
    GENERATOR = "generator"
    POLICY_TEXT = "policy_text"
    CLINICIAN_DECISION = "clinician_decision"
    NONE = "none"


class QAFinding(BaseModel):
    model_config = ConfigDict(extra="forbid")
    verdict: Verdict
    root_cause: RootCause
    fix_target: FixTarget
    explanation: str
    suggested_fix: str


def review(ce: CaseEval, gold_id: str, cfg: LLMConfig | None = None) -> tuple[QAFinding, object]:
    gold_cl = I.load_gold_checklist(ce.gold.policy_id)
    crit = gold_cl.find(gold_id)
    g = ce.gold.criteria[gold_id]
    s = next(x for x in ce.scores if x.gold_id == gold_id)
    # The agent's own criterion for this policy section (it may be numbered differently).
    from agent.policy_extract import norm_ref
    mine = [c for c in ce.result.checklist.leaves() if norm_ref(c.policy_ref) == norm_ref(crit.policy_ref)]
    a = next((x for x in ce.result.assessments if mine and x.criterion_id == mine[0].id), None)
    retrieved = next((r for r in ce.result.retrieval if mine and r.criterion_id == mine[0].id), None)
    payload = {
        "request": ce.req.model_dump(mode="json", exclude={"requested_channel"}),
        "policy_criterion": {"policy_ref": crit.policy_ref, "text": crit.text, "lookback_months": crit.lookback_months},
        "gold": {"status": g.status.value, "acceptable_alternates": [x.value for x in g.acceptable_alternates],
                 "key_evidence": [e.model_dump() for e in g.evidence], "missing_item": g.missing_item,
                 "generator_note": g.note},
        "agent": {"status": s.agent.value if s.agent else None,
                  "status_before_code_checks": s.model_said.value if s.model_said else None,
                  "reasoning": a.reasoning if a else None,
                  "evidence": [e.model_dump(mode="json") for e in a.evidence] if a else [],
                  "missing_items": a.missing_items if a else [],
                  "code_check_notes": a.deterministic_checks.notes if a else []},
        "retrieved_passages_for_this_criterion": [p.model_dump(mode="json") for p in retrieved.passages] if retrieved else [],
    }
    user = ("<disagreement>\n" + json.dumps(payload, indent=1) + "\n</disagreement>\n\n" + chart_block(ce.chart()))
    p = load_prompt(PROMPT)
    return structured_call(step="qa_review", prompt_id=p.ref, system=p.text, user=user, schema=QAFinding, cfg=cfg)
