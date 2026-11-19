"""Compare models on the same cases. Writes docs/MODEL_COMPARISON.md.

    python -m evals.compare m2-blind-opus m2-blind-sonnet m2-blind-haiku

Applies the decision rule from docs/COST_EFFECTIVENESS_SPEC.md in order:
1. gates (false MET = 0, citations 100%, routing 100%, injection flagged), then
2. quality (outcome and criterion accuracy), then
3. cost and latency.
Patient-experience guardrails and blinded reviewer preference need a pilot and are
out of scope offline; they are listed as not measured.
"""

from __future__ import annotations

import sys
from pathlib import Path

from agent.pipeline import RUNS
from evals.metrics import compute, load_run

ROOT = Path(__file__).resolve().parent.parent


def main(argv=None) -> int:
    runs = (argv or sys.argv[1:])
    rows = []
    case_sets = {}
    for run in runs:
        cases = load_run(RUNS / run)
        m = compute(cases, RUNS / run)
        model = (RUNS / run / "summary.md").read_text().split("`")[1]
        case_sets[run] = {c.request_id for c in cases}
        rows.append((run, model, m, cases))
    common = set.intersection(*case_sets.values()) if case_sets else set()
    L = ["# Model comparison", "",
         f"Same {len(common)} blind cases for every model: batch 3, which nobody looked at before these runs. "
         "It is 15 Northfield cases chosen to cover every case type and rare setting, plus their Calder twins with "
         "the same chart. Same prompts and same code for each model. Runs go through Claude Code; dollar figures "
         "are list-price equivalents for comparison.", ""]
    if any(case_sets[r] != common for r in case_sets):
        L += ["**Warning:** the case sets differ (some cases errored); metrics below use each run's own cases.", ""]
    notes = ROOT / "docs" / "eval_notes" / "model-comparison.md"
    if notes.exists():
        L += ["## Read of the results", "", notes.read_text().strip(), "", "## Numbers", ""]
    L += ["| | " + " | ".join(model for _, model, _, _ in rows) + " |", "|---" * (len(rows) + 1) + "|"]

    def line(label, fn):
        L.append(f"| {label} | " + " | ".join(fn(m, cases) for _, _, m, cases in rows) + " |")

    pct = lambda a, b: f"{a}/{b} ({100 * a / b:.0f}%)" if b else "n/a"
    line("Cases completed", lambda m, c: str(m["n_cases"]))
    line("**False MET (gate 0)**", lambda m, c: f"**{m['false_met']}**")
    line("Citations verbatim (gate 100%)", lambda m, c: pct(*m["citations"]))
    line("Routing (gate 100%)", lambda m, c: pct(*m["routing"]))
    line("Injection flagged by the model itself", lambda m, c: pct(*m["injection_model"]))
    line("Packet outcome exact", lambda m, c: pct(m["outcome"]["exact"], m["n_cases"]))
    line("Outcome differs only via acceptable alternate", lambda m, c: str(m["outcome"]["alternate"]))
    line("Criteria correct", lambda m, c: pct(m["correct"], m["n_criteria"]))
    line("INSUFFICIENT recall", lambda m, c: pct(*m["recall_INSUFFICIENT_EVIDENCE"]))
    line("NOT_MET recall", lambda m, c: pct(*m["recall_NOT_MET"]))
    line("Over-escalation (gold MET, agent not)", lambda m, c: pct(m["over_escalation"], m["gold_met"]))
    line("MET downgraded by code checks", lambda m, c: str(m["downgrades"]))
    line("Payer difference captured (pairs)", lambda m, c: pct(m["pairs"]["difference_captured"], m["pairs"]["n"]))
    line("Mean model seconds per fresh case", lambda m, c: f"{m['usage']['mean_s']:.0f}")
    line("Mean tokens per fresh case", lambda m, c: f"{m['usage']['mean_tokens']:,.0f}")
    line("List-price $ per fresh case", lambda m, c: f"${m['usage']['mean_cost']:.3f}")

    def passes(m):
        return (m["false_met"] == 0 and m["citations"][0] == m["citations"][1] and m["routing"][0] == m["routing"][1]
                and m["injection"][0] == m["injection"][1])
    L += ["", "## Decision rule", ""]
    for run, model, m, _ in rows:
        L.append(f"- `{model}`: gates {'PASS' if passes(m) else '**FAIL**'}; "
                 f"outcome exact {m['outcome']['exact']}/{m['n_cases']}; ${m['usage']['mean_cost']:.3f} per case.")
    passing = [(model, m) for _, model, m, _ in rows if passes(m)]
    if passing:
        best_q = max(m["outcome"]["exact"] / m["n_cases"] for _, m in passing)
        near = [(model, m) for model, m in passing if m["outcome"]["exact"] / m["n_cases"] >= best_q - 0.05]
        pick = min(near, key=lambda t: t[1]["usage"]["mean_cost"])
        L += ["", f"**Offline pick: `{pick[0]}`.** It is the cheapest model that passes every gate and comes within "
              "5 points of the best outcome accuracy, the spec's non-inferiority margin. "
              f"This is {len(common)} cases, too few to separate models finely: a 5-point difference needs "
              "hundreds of cases per arm (COST_EFFECTIVENESS_SPEC section 6). Treat it as the candidate for the "
              "blinded reviewer study and pilot, not the final answer."]
    else:
        L += ["", "No model passes every gate on this set."]
    L += ["", "Not measured offline: patient-experience guardrails (time to therapy, contacts, opt-outs) and blinded "
          "reviewer preference. Both need the pilot described in COST_EFFECTIVENESS_SPEC."]
    for run, model, m, _ in rows:
        if m["failures"]:
            L += ["", f"### Failures: `{model}`", "", "| Case | Payer | Criterion | Gold | Agent | Category | Retrieval had gold evidence |",
                  "|---|---|---|---|---|---|---|"]
            for f in m["failures"]:
                L.append(f"| {f['case']} | {f['payer']} | {f['criterion']} ({f['policy_ref']}) | {f['gold']} | "
                         f"{f['agent']} | {f['category']} | {f['retrieved_gold_evidence']} |")
    (ROOT / "docs" / "MODEL_COMPARISON.md").write_text("\n".join(L) + "\n")
    print("wrote docs/MODEL_COMPARISON.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
