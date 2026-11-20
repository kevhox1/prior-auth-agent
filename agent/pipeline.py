"""Steps 1 to 7, end to end, plus a small runner.

    python -m agent.pipeline PA-0001 PA-0002 PA-0003
    python -m agent.pipeline --synth batch-001 --sample 12 --seed 7
    PA_AGENT_MODEL=claude-sonnet-5-5 python -m agent.pipeline PA-0002 --run-name sonnet-pa2

Each case writes runs/<run>/<case>/{result.json, audit.jsonl, report.md}; the
run writes runs/<run>/summary.md. Model calls go through agent.llm (default
backend: `claude -p` on your Claude Code login) and are cached, so a re-run with
unchanged prompts and inputs makes no new calls.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from agent import intake as I
from agent.assess import assess
from agent.audit import AuditLog
from agent.checks import check, scan_injection
from agent.draft import draft
from agent.gaps import plan_gaps
from agent.llm import LLMConfig
from agent.policy_extract import compare_to_gold, extract
from agent.retrieve import retrieve
from agent.verify import verify
from agent.routing import lookup, route
from agent.schemas import (
    InjectionFlag,
    PacketOutcome,
    PipelineResult,
    PolicyChecklist,
    Status,
    outcome_for,
    packet_outcome,
    roll_up,
)

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"


@dataclass
class CaseSource:
    request_id: str
    cases_dir: Path
    charts_dir: Path


def run_case(src: CaseSource, checklist: PolicyChecklist, audit: AuditLog, cfg: LLMConfig,
             draft_packets: bool = True) -> PipelineResult:
    # Step 1: intake --------------------------------------------------------
    req = I.load_request(src.request_id, src.cases_dir)
    chart = I.load_chart(req.patient_id, src.charts_dir)
    row = lookup(req.payer, req.drug, req.plan_type.value)
    prose = I.load_policy_prose(row["policy_id"])
    intake = I.intake(req, chart, row["policy_id"], row["policy_version"], prose, row["decision_clock"])
    audit.log("1_intake", policy_id=intake.policy_id, policy_version=intake.policy_version,
              n_documents=intake.n_documents, urgency=req.urgency.value, notes=intake.notes)

    # Step 2: routing -------------------------------------------------------
    routing = route(req)
    audit.log("2_routing", **routing.model_dump(mode="json"))
    if not routing.pa_required:
        raise NotImplementedError("PA not required: v1 stops here (no case in the set exercises this)")

    # Step 3: policy checklist (extracted once per run, passed in) -----------
    audit.log("3_policy_checklist", policy_id=checklist.policy_id, version=checklist.version,
              leaves=[c.id for c in checklist.leaves()])

    # Step 4: retrieval -----------------------------------------------------
    retrieval, model_flags, rec, notes = retrieve(req, chart, checklist, cfg)
    code_flags = scan_injection(chart)
    audit.log("4_retrieve", rec, notes=notes,
              passages={r.criterion_id: len(r.passages) for r in retrieval},
              injection_flags_model=len(model_flags), injection_flags_code=len(code_flags))
    flags = _dedupe_flags(model_flags + code_flags)

    # Step 5: assessment ----------------------------------------------------
    drafts, rec, notes = assess(req, chart, checklist, retrieval, cfg)
    audit.log("5_assess", rec, notes=notes,
              proposed={cid: d.status.value for cid, d in drafts.items()})

    # Step 6: deterministic checks -------------------------------------------
    assessments = [check(drafts[leaf.id], leaf, chart, req, checklist.policy_id) for leaf in checklist.leaves()]
    downgrades = {a.criterion_id: f"{a.status_before_checks.value} -> {a.status.value}"
                  for a in assessments if a.status_before_checks}
    audit.log("6_checks", downgrades=downgrades,
              failed={a.criterion_id: a.deterministic_checks.notes for a in assessments
                      if not a.deterministic_checks.passed()})

    leaf_status = {a.criterion_id: a.status for a in assessments}
    rolled = roll_up(checklist, leaf_status)
    outcome = packet_outcome([rolled[c.id] for c in checklist.criteria])
    assert outcome == outcome_for(checklist, leaf_status)

    # Step 7: gap plan ------------------------------------------------------
    gaps, rec, notes = plan_gaps(req, checklist, assessments, cfg)
    if rec is not None:
        audit.log("7_gaps", rec, notes=notes, n_gaps=len(gaps))

    audit.log("outcome", outcome=outcome.value, rolled_up={k: v.value for k, v in rolled.items()},
              injection_flags=len(flags))

    # Steps 8 and 9: only a fully MET request gets a packet (spec 7.2). ------
    packet = verification = None
    packet_issues: list[str] = []
    if outcome == PacketOutcome.READY_FOR_REVIEW and draft_packets:
        packet, rec, packet_issues = draft(req, chart, checklist, assessments, routing.notes, cfg)
        audit.log("8_draft", rec, form_fields=len(packet.form_fields), letter_sentences=len(packet.letter),
                  code_issues=packet_issues)
        verification, rec, notes = verify(req, chart, packet, cfg)
        audit.log("9_verify", rec, notes=notes, overall_pass=verification.overall_pass,
                  unsupported=[c.claim_ref for c in verification.checks if not c.supported])
    return PipelineResult(
        request=req, intake=intake, policy_id=checklist.policy_id, policy_version=checklist.version,
        routing=routing, checklist=checklist, assessments=assessments, rolled_up=rolled,
        retrieval=retrieval, injection_flags=flags, gaps=gaps, outcome=outcome,
        packet=packet, packet_code_issues=packet_issues, verification=verification,
    )


def _dedupe_flags(flags: list[InjectionFlag]) -> list[InjectionFlag]:
    seen, out = set(), []
    for f in flags:
        key = (f.doc_id, f.quote.strip()[:40])
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


# --------------------------------------------------------------------------
# Reports
# --------------------------------------------------------------------------

_ICON = {Status.MET: "MET", Status.NOT_MET: "**NOT MET**", Status.INSUFFICIENT_EVIDENCE: "**INSUFFICIENT**",
         Status.CONFLICTING: "**CONFLICTING**"}


def case_report(res: PipelineResult, audit: AuditLog, scores=None, gold=None) -> str:
    r, a_by_id = res.request, {a.criterion_id: a for a in res.assessments}
    L = [f"# {r.request_id}: {r.product} for {r.patient_id}",
         "",
         f"**Outcome: {res.outcome.value}**",
         "",
         f"- Payer: {r.payer} ({r.plan_type.value}); policy {res.policy_id} version {res.policy_version}",
         f"- Request date {r.request_date}; requested start {r.requested_start}; urgency **{r.urgency.value}**",
         f"- Decision clock: {res.intake.decision_clock}",
         f"- Ordered dose: {r.dose}",
         f"- Benefit routing: " + ", ".join(f"{k} -> {v.value}" for k, v in res.routing.channels.items()),
         ]
    for n in res.routing.notes + res.intake.notes:
        L.append(f"  - {n}")
    if res.injection_flags:
        L += ["", "## Warning: instructions found inside the chart", "",
              "The agent ignored these and treated them as data. A human should look at where they came from.", ""]
        for f in res.injection_flags:
            L.append(f"- `{f.doc_id}`: \"{f.quote}\" ({f.note})")
    L += ["", "## Checklist", ""]
    for c in res.checklist.criteria:
        L.append(f"### {c.id} (policy {c.policy_ref}): {_ICON[res.rolled_up[c.id]]}")
        L.append(f"_{c.text}_")
        L.append("")
        for leaf in (c.sub_criteria or [c]):
            a = a_by_id[leaf.id]
            if c.sub_criteria:
                L.append(f"**{leaf.id} (policy {leaf.policy_ref}): {_ICON[a.status]}**: {leaf.text}")
                L.append("")
            if a.status_before_checks:
                L.append(f"> Code check changed this from {a.status_before_checks.value} to {a.status.value}.")
                L.append("")
            L.append(f"{a.reasoning} (confidence {a.confidence:.2f})")
            L.append("")
            for e in a.evidence:
                L.append(f"- `{e.doc_id}` ({e.doc_date}): \"{e.quote.strip()}\"")
            for m in a.missing_items:
                L.append(f"- Missing: {m}")
            if a.deterministic_checks.notes:
                L.append(f"- Code checks: " + "; ".join(a.deterministic_checks.notes))
            L.append("")
    if res.gaps:
        L += ["## To-do list (gap plan)", ""]
        for g in res.gaps:
            L += [f"- **{g.criterion_id}**: {g.missing_item} (who: {g.who_can_supply.value})",
                  f"  > {g.clinician_query}"]
            if g.would_satisfy:
                L.append(f"  - Would satisfy the policy: {g.would_satisfy}")
        L.append("")
    if res.packet:
        bad = {c.claim_ref: c.issue for c in res.verification.checks if not c.supported} if res.verification else {}
        L += ["## Draft PA form (step 8)", "", "| Field | Value | Source |", "|---|---|---|"]
        for f in res.packet.form_fields:
            src = "; ".join(f"`{c.doc_id}`" for c in f.citations) or "-"
            flag = f" **[verifier: {bad[f'form:{f.name}']}]**" if f"form:{f.name}" in bad else ""
            L.append(f"| {f.name} | {f.value}{flag} | {src} |")
        L += ["", "## Draft letter of medical necessity (step 8)", ""]
        for i, sent in enumerate(res.packet.letter):
            cite = " " + " ".join(f"[`{c.doc_id}`]" for c in sent.citations) if sent.citations else ""
            flag = f" **[verifier: {bad[f'letter:{i}']}]**" if f"letter:{i}" in bad else ""
            L.append(f"{sent.text}{cite}{flag}  ")
        L += ["", "## Independent verification (step 9)", ""]
        if res.verification:
            L.append(("All claims supported." if res.verification.overall_pass else
                      f"**{len(bad)} claim(s) flagged.** Fix or record an override before sign-off.")
                     + f" ({len(res.verification.checks)} claims checked.)")
        for i in res.packet_code_issues:
            L.append(f"- Code citation check: {i}")
        L.append("")
    t = audit.totals()
    L += ["## Run cost", "",
          f"{t['model_calls']} model calls, {t['input_tokens']:,} input and {t['output_tokens']:,} output tokens, "
          f"{t['latency_s']} s of model time, ${t['cost_usd_list']:.3f} at list price "
          f"({t['cache_hits']} served from cache).", ""]
    if scores is not None:
        L += ["## Compared with gold (evaluation only; a reviewer would not see this)", "",
              f"Gold outcome {gold.packet_outcome.value}; agent {res.outcome.value}. Case type: {gold.case_type}.", "",
              "| Gold id | Policy | Gold | Agent | Model before checks | Result |", "|---|---|---|---|---|---|"]
        for s in scores:
            res_txt = "FALSE MET" if s.false_met else ("ok" if s.exact else ("ok (alternate)" if s.correct else "wrong"))
            L.append(f"| {s.gold_id} | {s.policy_ref} | {s.gold.value} | {s.agent.value if s.agent else '-'} | "
                     f"{s.model_said.value if s.model_said else '-'} | {res_txt} |")
        if gold.expect_injection_flag:
            L.append(f"\nInjection expected: flagged = {bool(res.injection_flags)}")
        L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------
# Runner
# --------------------------------------------------------------------------


def _sources(args) -> list[CaseSource]:
    out = [CaseSource(rid, I.DATA / "cases", I.DATA / "charts") for rid in args.cases]
    if args.synth:
        base = I.DATA / "synth" / args.synth
        ids = I.list_cases(base / "cases")
        if args.only:
            ids = [i.strip() for i in args.only.split(",")]
        elif args.pairs:
            ids = paired_sample(base, args.pairs, args.seed)
        elif args.sample:
            ids = stratified_sample(base, args.sample, args.seed)
        out += [CaseSource(rid, base / "cases", base / "charts") for rid in ids]
    return out


def paired_sample(base: Path, n_pairs: int, seed: int) -> list[str]:
    """Stratified sample of Northfield cases plus each one's Calder twin (same chart)."""
    import csv

    rows = list(csv.DictReader((base / "manifest.csv").open()))
    north = stratified_sample(base, n_pairs, seed, payer="northfield")
    pair_of = {r["request_id"]: r["pair"] for r in rows}
    twins = {r["pair"]: r["request_id"] for r in rows if r["payer"] == "calder"}
    return sorted(north + [twins[pair_of[rid]] for rid in north if pair_of[rid] in twins])


def stratified_sample(base: Path, n: int, seed: int, payer: str | None = None) -> list[str]:
    """One case per case type and per rare knob (injection, wrong channel, expedited), then random fill."""
    import csv

    rng = random.Random(seed)
    rows = [r for r in csv.DictReader((base / "manifest.csv").open()) if payer is None or r.get("payer") == payer]
    rng.shuffle(rows)
    picked: list[str] = []
    groups = [lambda r, t=t: r["case_type"] == t for t in sorted({r["case_type"] for r in rows})]
    groups += [lambda r, k=k: r[k] == "True" for k in
               ("knob_injection", "knob_requested_channel_wrong", "knob_expedited")]
    for g in groups:
        hit = next((r["request_id"] for r in rows if g(r) and r["request_id"] not in picked), None)
        if hit and len(picked) < n:
            picked.append(hit)
    picked += [r["request_id"] for r in rows if r["request_id"] not in picked][: n - len(picked)]
    return sorted(picked)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cases", nargs="*", help="hand-built case ids under data/cases")
    ap.add_argument("--synth", help="synthetic batch folder under data/synth, e.g. batch-001")
    ap.add_argument("--sample", type=int, help="random sample size from the synthetic batch")
    ap.add_argument("--only", help="comma-separated case ids from the --synth batch")
    ap.add_argument("--pairs", type=int, help="paired batches: sample N Northfield cases plus their Calder twins")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--model", help="overrides PA_AGENT_MODEL")
    ap.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--backend", choices=["claude_code", "anthropic_api", "replay"])
    ap.add_argument("--workers", type=int, default=3, help="cases run in parallel")
    ap.add_argument("--checklist", choices=["extract", "gold"], default="extract",
                    help="'gold' skips step 3 to isolate retrieval/assessment errors")
    ap.add_argument("--run-name")
    args = ap.parse_args(argv)

    cfg = LLMConfig()
    if args.model:
        cfg.model = args.model
    if args.backend:
        cfg.backend = args.backend
    cfg.effort = args.effort
    sources = _sources(args)
    if not sources:
        ap.error("no cases given")
    run_name = args.run_name or f"{datetime.now():%Y%m%d-%H%M%S}-{cfg.model}"
    run_dir = RUNS / run_name
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"run {run_name}: {len(sources)} cases, model {cfg.model}, backend {cfg.backend}", flush=True)

    # Step 3 once per policy.
    checklists: dict[str, PolicyChecklist] = {}
    extraction_report = {}
    for src in sources:
        req = I.load_request(src.request_id, src.cases_dir)
        row = lookup(req.payer, req.drug, req.plan_type.value)
        pid = row["policy_id"]
        if pid in checklists:
            continue
        if args.checklist == "gold":
            checklists[pid] = I.load_gold_checklist(pid)
            continue
        audit = AuditLog(f"policy:{pid}")
        cl, rec, warns = extract(pid, req.payer, req.drug, I.load_policy_prose(pid), row["policy_version"], cfg)
        cmp = compare_to_gold(cl, I.load_gold_checklist(pid))
        audit.log("3_policy_extract", rec, warnings=warns, vs_gold=cmp)
        audit.write(run_dir / f"policy-{pid}" / "audit.jsonl")
        (run_dir / f"policy-{pid}" / "checklist.json").write_text(cl.model_dump_json(indent=2))
        checklists[pid] = cl
        extraction_report[pid] = cmp
        print(f"step 3 {pid}: {cmp['found']}/{cmp['gold_leaves']} gold criteria found; "
              f"{len(cmp['issues'])} issues", flush=True)

    rows = []

    def one(src: CaseSource):
        audit = AuditLog(src.request_id)
        req = I.load_request(src.request_id, src.cases_dir)
        pid = lookup(req.payer, req.drug, req.plan_type.value)["policy_id"]
        res = run_case(src, checklists[pid], audit, cfg)
        out = run_dir / src.request_id
        out.mkdir(parents=True, exist_ok=True)
        gold = I.load_gold(src.request_id, src.cases_dir)
        from evals.score import score  # local import: agent code does not depend on evals
        sc = score(res, gold, I.load_gold_checklist(pid))
        (out / "result.json").write_text(res.model_dump_json(indent=2))
        audit.write(out / "audit.jsonl")
        (out / "report.md").write_text(case_report(res, audit, sc, gold))
        (out / "error.txt").unlink(missing_ok=True)  # a re-run that succeeds clears an earlier failure
        return src, res, gold, sc, audit.totals()

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(one, s): s for s in sources}
        for f in as_completed(futs):
            src = futs[f]
            try:
                src, res, gold, sc, tot = f.result()
            except Exception as e:  # keep going; report the failure
                print(f"  {src.request_id}: ERROR {e}", flush=True)
                (run_dir / src.request_id).mkdir(parents=True, exist_ok=True)
                # Paths relative to the repo, so a traceback never carries the local home directory.
                tb = traceback.format_exc().replace(str(ROOT), "<repo>")
                (run_dir / src.request_id / "error.txt").write_text(tb)
                rows.append({"id": src.request_id, "error": str(e)[:200]})
                continue
            fm = sum(s.false_met for s in sc)
            ok = sum(s.correct for s in sc)
            # "alternate": outcome differs from gold only because a criterion took an acceptable alternate.
            outcome_grade = ("exact" if res.outcome == gold.packet_outcome
                             else "alternate" if ok == len(sc) else "wrong")
            row = {"id": src.request_id, "case_type": gold.case_type, "gold": gold.packet_outcome.value,
                   "agent": res.outcome.value, "outcome_grade": outcome_grade, "criteria_ok": f"{ok}/{len(sc)}", "false_met": fm,
                   "downgrades": sum(1 for a in res.assessments if a.status_before_checks),
                   "inj_expected": gold.expect_injection_flag, "inj_flagged": bool(res.injection_flags), **tot}
            rows.append(row)
            print(f"  {src.request_id}: {res.outcome.value:16} gold {gold.packet_outcome.value:16} "
                  f"criteria {ok}/{len(sc)} false MET {fm}  ({tot['latency_s']} s, ${tot['cost_usd_list']:.3f})",
                  flush=True)

    rows.sort(key=lambda r: r["id"])
    (run_dir / "rows.json").write_text(json.dumps(rows, indent=1))
    (run_dir / "summary.md").write_text(summary_md(run_name, cfg, rows, extraction_report))
    print(f"wrote {run_dir / 'summary.md'}")
    return 0


def summary_md(run_name: str, cfg: LLMConfig, rows: list[dict], extraction: dict) -> str:
    good = [r for r in rows if "error" not in r]
    L = [f"# Run {run_name}", "", f"Model `{cfg.model}`, backend `{cfg.backend}`, effort `{cfg.effort or 'default'}`.", ""]
    if good:
        n_crit = sum(int(r["criteria_ok"].split("/")[1]) for r in good)
        ok = sum(int(r["criteria_ok"].split("/")[0]) for r in good)
        L += [f"- Cases: {len(good)} ok, {len(rows) - len(good)} errored",
              f"- Packet outcome matches gold: {sum(r['outcome_grade'] == 'exact' for r in good)}/{len(good)} exact; "
              f"{sum(r['outcome_grade'] == 'alternate' for r in good)} more differ only via an acceptable alternate status; "
              f"{sum(r['outcome_grade'] == 'wrong' for r in good)} wrong",
              f"- Criteria correct (gold or acceptable alternate): {ok}/{n_crit}",
              f"- **False MET: {sum(r['false_met'] for r in good)}** (release gate: 0)",
              f"- MET claims downgraded by step 6 code checks: {sum(r['downgrades'] for r in good)}",
              f"- Injection cases flagged: {sum(r['inj_flagged'] for r in good if r['inj_expected'])}"
              f"/{sum(r['inj_expected'] for r in good)}",
              f"- Model time {sum(r['latency_s'] for r in good):.0f} s; list-price cost ${sum(r['cost_usd_list'] for r in good):.2f}",
              ""]
    for pid, cmp in extraction.items():
        L += [f"Step 3 extraction for {pid}: {cmp['found']}/{cmp['gold_leaves']} gold criteria found."]
        L += [f"- {i}" for i in cmp["issues"]] + [""]
    L += ["| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if "error" in r:
            L.append(f"| {r['id']} | ERROR: {r['error']} | | | | | | | |")
        else:
            mark = {"exact": "", "alternate": " (alt)", "wrong": " ✗"}[r["outcome_grade"]]
            L.append(f"| [{r['id']}]({r['id']}/report.md) | {r['case_type']} | {r['gold']} | {r['agent']}{mark} | "
                     f"{r['criteria_ok']} | {r['false_met']} | {r['downgrades']} | {r['latency_s']} | {r['cost_usd_list']:.3f} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    sys.exit(main())
