"""Score one pipeline result against gold. Used by the M1 runner and, later, evals.run.

The agent's checklist may number criteria differently from gold, so criteria
are aligned by policy section (policy_ref). If the agent kept a gold sub-criterion
merged into its parent, the parent's status stands in for it.
"""

from __future__ import annotations

from dataclasses import dataclass

from agent.policy_extract import norm_ref
from agent.schemas import CaseGold, PipelineResult, PolicyChecklist, Status, roll_up


@dataclass
class CriterionScore:
    gold_id: str
    policy_ref: str
    gold: Status
    agent: Status | None
    model_said: Status | None
    correct: bool
    exact: bool
    false_met: bool
    aligned_via: str  # "leaf", "parent", or "missing"


def _agent_status_by_ref(result: PipelineResult) -> tuple[dict[str, Status], dict[str, Status | None]]:
    by_ref: dict[str, Status] = {}
    before: dict[str, Status | None] = {}
    a_by_id = {a.criterion_id: a for a in result.assessments}
    for c in result.checklist.criteria:
        by_ref[norm_ref(c.policy_ref)] = result.rolled_up[c.id]
        for s in c.sub_criteria:
            by_ref[norm_ref(s.policy_ref)] = result.rolled_up[s.id]
    for leaf in result.checklist.leaves():
        a = a_by_id.get(leaf.id)
        before[norm_ref(leaf.policy_ref)] = (a.status_before_checks or a.status) if a else None
    return by_ref, before


def score(result: PipelineResult, gold: CaseGold, gold_checklist: PolicyChecklist) -> list[CriterionScore]:
    by_ref, before = _agent_status_by_ref(result)
    gold_rolled = roll_up(gold_checklist, {cid: g.status for cid, g in gold.criteria.items()})
    parent_of = {s.id: c.id for c in gold_checklist.criteria for s in c.sub_criteria}
    out = []
    for leaf in gold_checklist.leaves():
        g = gold.criteria[leaf.id]
        ref = norm_ref(leaf.policy_ref)
        via = "leaf"
        agent = by_ref.get(ref)
        gold_status, alts = g.status, g.acceptable_alternates
        if agent is None and "(" in ref:
            # The agent kept this part merged into its parent (e.g. one criterion for "3.5"). It never judged
            # the part, so score its parent status against gold's parent status. Under ANY logic, comparing a
            # parent MET with a failed part would invent a false MET the agent never claimed.
            agent, via = by_ref.get(ref.split("(")[0]), "parent"
            gold_status, alts = gold_rolled[parent_of[leaf.id]], []
        if agent is None:
            via = "missing"
        exact = agent == gold_status
        correct = exact or (agent in alts)
        out.append(CriterionScore(
            gold_id=leaf.id, policy_ref=leaf.policy_ref + (" (scored at parent)" if via == "parent" else ""),
            gold=gold_status, agent=agent,
            model_said=before.get(ref) if via == "leaf" else agent, correct=correct, exact=exact,
            false_met=(agent == Status.MET and gold_status != Status.MET), aligned_via=via,
        ))
    return out
