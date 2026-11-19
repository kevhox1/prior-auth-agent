"""Metrics over a finished run directory (runs/<run>/). Pure code, no model calls."""

from __future__ import annotations

import csv
import json
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from agent import intake as I
from agent.checks import quote_in_text
from agent.policy_extract import norm_phase
from agent.schemas import CaseGold, Chart, PARequest, PipelineResult, Status
from evals.score import CriterionScore, score

STATUSES = [Status.MET, Status.NOT_MET, Status.INSUFFICIENT_EVIDENCE, Status.CONFLICTING]


@dataclass
class CaseEval:
    request_id: str
    payer: str
    cases_dir: Path
    charts_dir: Path
    req: PARequest
    result: PipelineResult
    gold: CaseGold
    scores: list[CriterionScore]
    usage: dict
    knobs: dict = field(default_factory=dict)
    pair: str = ""

    @property
    def outcome_grade(self) -> str:
        if self.result.outcome == self.gold.packet_outcome:
            return "exact"
        return "alternate" if all(s.correct for s in self.scores) else "wrong"

    def chart(self) -> Chart:
        return I.load_chart(self.req.patient_id, self.charts_dir)


def find_case(request_id: str) -> tuple[Path, Path]:
    for cases_dir in [I.DATA / "cases", *sorted((I.DATA / "synth").glob("batch-*/cases"))]:
        if (cases_dir / request_id / "request.yaml").exists():
            return cases_dir, cases_dir.parent / "charts"
    raise FileNotFoundError(request_id)


def _manifest_row(cases_dir: Path, request_id: str) -> dict:
    m = cases_dir.parent / "manifest.csv"
    if not m.exists():
        return {}
    for r in csv.DictReader(m.open()):
        if r["request_id"] == request_id:
            return r
    return {}


def load_run(run_dir: Path) -> list[CaseEval]:
    usage = {r["id"]: r for r in json.loads((run_dir / "rows.json").read_text()) if "error" not in r}
    out = []
    for res_path in sorted(run_dir.glob("PA-*/result.json")):
        rid = res_path.parent.name
        cases_dir, charts_dir = find_case(rid)
        res = PipelineResult.model_validate_json(res_path.read_text())
        gold = I.load_gold(rid, cases_dir)
        row = _manifest_row(cases_dir, rid)
        out.append(CaseEval(
            request_id=rid, payer=res.request.payer, cases_dir=cases_dir, charts_dir=charts_dir, req=res.request,
            result=res, gold=gold, scores=score(res, gold, I.load_gold_checklist(gold.policy_id)),
            usage=usage.get(rid, {}), knobs={k[5:]: v for k, v in row.items() if k.startswith("knob_")},
            pair=row.get("pair", ""),
        ))
    return out


def _pct(a: int, b: int) -> str:
    return f"{a}/{b} ({100 * a / b:.0f}%)" if b else "n/a"


def failure_category(s: CriterionScore) -> str:
    if s.false_met:
        return "FALSE_MET"
    if s.gold == Status.MET:
        return "over_escalation (gold MET)"
    if s.agent == Status.INSUFFICIENT_EVIDENCE:
        return "under_escalation (said INSUFFICIENT, gold " + s.gold.value + ")"
    if s.agent is None:
        return "criterion missing from extracted checklist"
    return f"wrong problem type ({s.agent.value} vs {s.gold.value})"


def retrieval_had_gold(ce: CaseEval, s: CriterionScore) -> str:
    """Did step 4 surface any gold evidence quote (for any criterion)? Attributes the miss."""
    gold_quotes = ce.gold.criteria[s.gold_id].evidence
    if not gold_quotes:
        return "-"
    passages = [p for r in ce.result.retrieval for p in r.passages]
    for g in gold_quotes:
        for p in passages:
            if p.doc_id == g.doc_id and (quote_in_text(g.quote, p.quote) or quote_in_text(p.quote, g.quote)):
                return "yes"
    return "no"


def compute(cases: list[CaseEval], run_dir: Path) -> dict:
    all_scores = [(ce, s) for ce in cases for s in ce.scores]
    m: dict = {"n_cases": len(cases), "n_criteria": len(all_scores)}
    m["exact"] = sum(s.exact for _, s in all_scores)
    m["correct"] = sum(s.correct for _, s in all_scores)
    m["false_met"] = sum(s.false_met for _, s in all_scores)
    m["gold_non_met"] = sum(s.gold != Status.MET for _, s in all_scores)
    for st in (Status.INSUFFICIENT_EVIDENCE, Status.NOT_MET, Status.CONFLICTING):
        g = [s for _, s in all_scores if s.gold == st]
        m[f"recall_{st.value}"] = (sum(s.correct for s in g), len(g))
    m["over_escalation"] = sum(1 for _, s in all_scores if s.gold == Status.MET and s.agent != Status.MET)
    m["gold_met"] = sum(1 for _, s in all_scores if s.gold == Status.MET)
    m["outcome"] = Counter(ce.outcome_grade for ce in cases)

    # Routing: channels and the requested-channel check.
    def routing_ok(ce: CaseEval) -> bool:
        a = {norm_phase(k): v for k, v in ce.result.routing.channels.items()}
        g = {norm_phase(k): v for k, v in ce.gold.routing.channels.items()}
        return a == g and ce.result.routing.requested_channel_ok == ce.gold.routing.requested_channel_ok
    m["routing"] = (sum(routing_ok(ce) for ce in cases), len(cases))

    # Citation validity of what the model proposed (before step 6 filtered anything).
    n_q = ok_q = 0
    for ce in cases:
        chart = ce.chart()
        for a in ce.result.assessments:
            for e in a.evidence:
                n_q += 1
                d = chart.get(e.doc_id)
                ok_q += bool(d and quote_in_text(e.quote, d.text) and d.date == e.doc_date)
    m["citations"] = (ok_q, n_q)
    m["downgrades"] = sum(1 for ce in cases for a in ce.result.assessments if a.status_before_checks)

    # Injection.
    inj = [ce for ce in cases if ce.gold.expect_injection_flag]
    clean = [ce for ce in cases if not ce.gold.expect_injection_flag]
    m["injection"] = (sum(bool(ce.result.injection_flags) for ce in inj), len(inj))
    m["injection_model"] = (sum(any(not f.note.startswith("code scan") for f in ce.result.injection_flags) for ce in inj), len(inj))
    m["injection_false"] = (sum(bool(ce.result.injection_flags) for ce in clean), len(clean))

    # Confusion matrix.
    conf = Counter((s.gold, s.agent) for _, s in all_scores)
    m["confusion"] = conf

    # Usage.
    # A case counts as fresh only if every model call ran (no cache hits), so averages are true per-case costs.
    fresh = [ce for ce in cases if ce.usage.get("model_calls") and not ce.usage.get("cache_hits")]
    secs = [ce.usage.get("latency_s", 0) for ce in fresh]
    cost = [ce.usage.get("cost_usd_list", 0) for ce in fresh]
    toks = [ce.usage.get("input_tokens", 0) + ce.usage.get("output_tokens", 0) for ce in fresh]
    m["usage"] = {
        "fresh_cases": len(secs),
        "mean_s": statistics.mean(secs) if secs else 0, "p90_s": sorted(secs)[int(0.9 * (len(secs) - 1))] if secs else 0,
        "mean_cost": statistics.mean(cost) if cost else 0, "total_cost": sum(cost),
        "mean_tokens": statistics.mean(toks) if toks else 0,
    }

    # Breakdowns.
    by_payer = defaultdict(lambda: [0, 0, 0, 0, 0])  # cases, outcome exact, criteria, correct, false met
    for ce in cases:
        b = by_payer[ce.payer]
        b[0] += 1; b[1] += ce.outcome_grade == "exact"
        b[2] += len(ce.scores); b[3] += sum(s.correct for s in ce.scores); b[4] += sum(s.false_met for s in ce.scores)
    m["by_payer"] = dict(by_payer)

    by_crit = defaultdict(lambda: [0, 0])
    for ce, s in all_scores:
        k = (ce.payer, s.gold_id, s.policy_ref)
        by_crit[k][0] += 1; by_crit[k][1] += not s.correct
    m["by_criterion"] = dict(by_crit)

    by_knob = defaultdict(lambda: [0, 0])  # cases, cases with any criterion error
    for ce in cases:
        bad = any(not s.correct for s in ce.scores)
        for k, v in ce.knobs.items():
            by_knob[(k, v)][0] += 1; by_knob[(k, v)][1] += bad
    m["by_knob"] = dict(by_knob)

    # Pairs: same chart, two payers.
    pairs = defaultdict(dict)
    for ce in cases:
        if ce.pair:
            pairs[ce.pair][ce.payer] = ce
    full = [p for p in pairs.values() if len(p) == 2]
    m["pairs"] = {
        "n": len(full),
        "gold_differ": sum(p["northfield"].gold.packet_outcome != p["calder"].gold.packet_outcome for p in full),
        "both_exact": sum(all(c.outcome_grade == "exact" for c in p.values()) for p in full),
        "difference_captured": sum(
            (p["northfield"].result.outcome != p["calder"].result.outcome)
            == (p["northfield"].gold.packet_outcome != p["calder"].gold.packet_outcome) for p in full),
    }

    # Extraction.
    m["extraction"] = {}
    for audit in sorted(run_dir.glob("policy-*/audit.jsonl")):
        ev = json.loads(audit.read_text().splitlines()[0])
        m["extraction"][audit.parent.name.removeprefix("policy-")] = ev["payload"].get("vs_gold", {})

    m["failures"] = [
        {"case": ce.request_id, "payer": ce.payer, "criterion": s.gold_id, "policy_ref": s.policy_ref,
         "gold": s.gold.value, "agent": s.agent.value if s.agent else None,
         "model_said": s.model_said.value if s.model_said else None, "category": failure_category(s),
         "retrieved_gold_evidence": retrieval_had_gold(ce, s),
         "state": (ce.gold.criteria[s.gold_id].note or "").removeprefix("synthetic state: ")}
        for ce, s in all_scores if not s.correct
    ]
    m["outcome_failures"] = [
        {"case": ce.request_id, "payer": ce.payer, "gold": ce.gold.packet_outcome.value, "agent": ce.result.outcome.value,
         "grade": ce.outcome_grade}
        for ce in cases if ce.outcome_grade != "exact"
    ]
    return m
