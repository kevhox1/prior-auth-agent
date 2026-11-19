"""Step 3: policy extraction. Model turns policy prose into the checklist schema.

Runs once per policy version (the call is cached). Code then checks the result
against the policy header and the rules table, and `compare_to_gold` scores it
for the eval report. The gold checklist is never shown to the model.
"""

from __future__ import annotations

import re

from agent.llm import CallRecord, LLMConfig, structured_call
from agent.prompts import load_prompt
from agent.schemas import PolicyChecklist, PolicyExtractionDraft

PROMPT = "policy_extract@v1"


class ExtractionError(ValueError):
    pass


def extract(policy_id: str, payer: str, drug: str, prose: str, expected_version: str,
            cfg: LLMConfig | None = None) -> tuple[PolicyChecklist, CallRecord, list[str]]:
    p = load_prompt(PROMPT)
    draft, rec = structured_call(
        step="policy_extract", prompt_id=p.ref, system=p.text,
        user=f"<policy>\n{prose}\n</policy>", schema=PolicyExtractionDraft, cfg=cfg,
    )
    checklist = draft.to_checklist(policy_id, payer, drug)
    warnings = sanity_check(checklist, expected_version)
    return checklist, rec, warnings


def sanity_check(checklist: PolicyChecklist, expected_version: str) -> list[str]:
    """Hard failures raise; soft problems come back as warnings for the audit log."""
    if checklist.version != expected_version:
        raise ExtractionError(f"extracted version {checklist.version!r}, expected {expected_version!r}")
    ids = [c.id for c in checklist.leaves()] + [c.id for c in checklist.criteria if c.sub_criteria]
    if len(ids) != len(set(ids)):
        raise ExtractionError(f"duplicate criterion ids: {ids}")
    warnings = []
    refs = [c.policy_ref for c in checklist.leaves()]
    if len(refs) != len(set(refs)):
        warnings.append(f"two leaf criteria share a policy_ref: {refs}")
    return warnings


def norm_ref(ref: str) -> str:
    return re.sub(r"[^0-9a-z().]", "", ref.lower().replace("section", ""))


def norm_phase(phase: str) -> str:
    """'subcutaneous_maintenance' and 'sc_maintenance' name the same phase."""
    p = phase.lower().replace("intravenous", "iv").replace("subcutaneous", "sc")
    return "_".join(t for t in re.split(r"[^a-z]+", p) if t and t not in ("dose", "doses", "phase"))


def compare_to_gold(extracted: PolicyChecklist, gold: PolicyChecklist) -> dict:
    """Align by policy_ref. Reports missing, extra, logic and lookback mismatches."""
    def index(cl: PolicyChecklist) -> dict:
        out = {}
        for c in cl.criteria:
            out[norm_ref(c.policy_ref)] = c
            for s in c.sub_criteria:
                out[norm_ref(s.policy_ref)] = s
        return out

    e, g = index(extracted), index(gold)
    gold_leaves = {norm_ref(c.policy_ref) for c in gold.leaves()}
    found = {r for r in gold_leaves if r in e}
    issues = []
    for r in sorted(gold_leaves - found):
        issues.append(f"missing criterion for policy {r}")
    for r in sorted(set(e) - set(g)):
        issues.append(f"extra criterion for policy {r}")
    for r in sorted(set(e) & set(g)):
        if (e[r].logic or None) != (g[r].logic or None):
            issues.append(f"{r}: logic {e[r].logic} vs gold {g[r].logic}")
        if e[r].lookback_months != g[r].lookback_months:
            issues.append(f"{r}: lookback {e[r].lookback_months} vs gold {g[r].lookback_months}")
    ec = {norm_phase(k): v.value for k, v in extracted.benefit_channel.items()}
    gc = {norm_phase(k): v.value for k, v in gold.benefit_channel.items()}
    if ec != gc:
        issues.append(f"benefit channels {ec} vs gold {gc}")
    if extracted.auth_duration_months != gold.auth_duration_months:
        issues.append(f"auth duration {extracted.auth_duration_months} vs gold {gold.auth_duration_months}")
    return {"gold_leaves": len(gold_leaves), "found": len(found), "issues": issues}
