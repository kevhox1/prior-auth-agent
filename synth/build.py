"""Build a batch of synthetic cases.

    python -m synth.build --batch 1 --n 200 --seed 1
    python -m synth.build --batch 2 --n 100 --seed 2 --paired
    python -m synth.build --batch 3 --n 20 --seed 3 --rewrite --model claude-sonnet-5-5

--paired writes every case twice from the same blueprint: once for Northfield
(PA-<b>001...) and once for Calder Mutual (PA-<b>501...). The two charts are
clinically identical (only the insurance lines differ), so any difference in
the gold answer comes from the policies alone.

Output: data/synth/batch-NNN/{cases,charts}/... in the same layout as the hand
cases, plus blueprint.json per case and manifest.csv for the whole batch.
Template rendering costs nothing. --rewrite calls a model per document through
agent.llm (default: `claude -p` on your Claude Code login).
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter
from pathlib import Path

import yaml

from agent import intake
from agent.llm import LLMConfig
from agent.schemas import ChartDocument
from synth.blueprint import sample_blueprint
from synth.label import label
from synth.render import Doc, render
from synth.validate import validate

POLICY_BY_PAYER = {"northfield": "northfield-ustekinumab-ibd", "calder": "calder-ustekinumab-ibd"}
OUT_ROOT = intake.DATA / "synth"


def _to_chart_docs(pid: str, docs: list[Doc]) -> list[ChartDocument]:
    return [ChartDocument(doc_id=f"{pid}/{d.stem}", patient_id=pid, doc_type=d.doc_type, date=d.date,
                          author=d.author, title=d.title, text="\n".join(d.lines).rstrip()) for d in docs]


def _write_doc(folder: Path, d: ChartDocument) -> None:
    header = {"doc_id": d.doc_id, "doc_type": d.doc_type.value, "date": d.date, "author": d.author, "title": d.title}
    stem = d.doc_id.split("/", 1)[1]
    (folder / f"{stem}.md").write_text("---\n" + yaml.safe_dump(header, sort_keys=False) + "---\n" + d.text + "\n")


def build(batch: int, n: int, seed: int, rewrite: bool = False, model: str | None = None,
          limit_rewrite: int | None = None, out_root: Path = OUT_ROOT, paired: bool = False) -> Path:
    if not 1 <= batch <= 9 or n > (499 if paired else 999):
        raise SystemExit("batch must be 1-9 and n at most 999, or 499 with --paired (ids are PA-<batch><nnn>)")
    out = out_root / f"batch-{batch:03d}"
    if out.exists():
        shutil.rmtree(out)
    (out / "cases").mkdir(parents=True)
    (out / "charts").mkdir()
    checklists = {p: intake.load_gold_checklist(pid) for p, pid in POLICY_BY_PAYER.items()}
    cfg = LLMConfig(model=model) if model else LLMConfig()
    rows, failures = [], []
    outcome_by_pair: dict[int, dict[str, str]] = {}

    jobs = []
    for i in range(n):
        bp = sample_blueprint(seed * 100_000 + i, batch * 1000 + i + 1)
        jobs.append((i, bp))
        if paired:
            num = batch * 1000 + 500 + i + 1
            jobs.append((i, bp.model_copy(update={"payer": "calder", "request_id": f"PA-{num:04d}",
                                                  "patient_id": f"PT-{num:04d}"})))
    for i, bp in jobs:
        checklist = checklists[bp.payer]
        r = render(bp)
        docs = _to_chart_docs(bp.patient_id, r.docs)
        gold = label(bp, r, checklist)

        if rewrite and (limit_rewrite is None or i < limit_rewrite):
            from synth.rewrite import never_list, rewrite_doc
            never = never_list(bp.states)
            new_docs = []
            for d in docs:
                keep = [ev.quote for g in gold.criteria.values() for ev in g.evidence if ev.doc_id == d.doc_id]
                text, _ = rewrite_doc(d.text, keep, never, cfg)
                candidate = d.model_copy(update={"text": text})
                trial = [candidate if x.doc_id == d.doc_id else x for x in docs]
                new_docs.append(candidate if not validate(bp, trial, gold) else d)
            docs = new_docs

        errs = validate(bp, docs, gold)
        if errs:
            failures.append((bp.request_id, errs))
            continue

        chart_dir = out / "charts" / bp.patient_id
        chart_dir.mkdir()
        for d in docs:
            _write_doc(chart_dir, d)
        case_dir = out / "cases" / bp.request_id
        case_dir.mkdir()
        w = bp.weight_kg
        request = {
            "request_id": bp.request_id, "patient_id": bp.patient_id, "drug": "ustekinumab",
            "product": r.product,
            "dose": f"{r.requested_mg} mg IV once (weight {w:.1f} kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose",
            "indication_icd10": "K50.80" if bp.disease == "cd" else "K51.00",
            "payer": bp.payer, "plan_type": "commercial",
            "ordering_provider": next(d.author for d in docs if d.doc_type.value == "progress_note"),
            "urgency": "expedited" if bp.knobs.expedited else "standard",
            "request_date": bp.request_date, "requested_start": "2026-12-01",
        }
        if bp.knobs.expedited:
            request["expedited_reason"] = "Severe flare with weight loss on steroids; delay risks hospitalization."
        if bp.knobs.requested_channel_wrong:
            request["requested_channel"] = "pharmacy"
        (case_dir / "request.yaml").write_text(yaml.safe_dump(request, sort_keys=False))
        (case_dir / "gold.yaml").write_text("# GOLD - evaluation only. Generated from blueprint.json by synth/label.py.\n"
                                            + yaml.safe_dump(gold.model_dump(mode="json", exclude_defaults=True), sort_keys=False, width=110))
        (case_dir / "blueprint.json").write_text(bp.model_dump_json(indent=2))
        outcome_by_pair.setdefault(i, {})[bp.payer] = gold.packet_outcome.value
        rows.append({"request_id": bp.request_id, "payer": bp.payer, "pair": f"{batch}-{i + 1:03d}" if paired else "",
                     "case_type": gold.case_type, "outcome": gold.packet_outcome.value,
                     "problems": ";".join(f"{k}={v}" for k, v in bp.states.items() if v != "met_clean"),
                     **{f"knob_{k}": v for k, v in bp.knobs.model_dump().items()}, "n_docs": len(docs)})

    if paired:
        for row in rows:
            pair = outcome_by_pair[int(row["pair"].split("-")[1]) - 1]
            row["pair_outcomes_differ"] = len(set(pair.values())) > 1 if len(pair) == 2 else ""
    with (out / "manifest.csv").open("w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0]))
        wr.writeheader()
        wr.writerows(rows)
    print(f"wrote {len(rows)} cases to {out}  (rejected {len(failures)})")
    for rid, errs in failures[:10]:
        print(f"  rejected {rid}: {errs[:2]}")
    print("case types:", dict(Counter(r["case_type"] for r in rows)))
    print("outcomes:  ", dict(Counter((r["payer"], r["outcome"]) for r in rows)))
    if paired:
        print("pairs where the payers' answers differ:", sum(1 for r in rows if r["payer"] == "calder" and r["pair_outcomes_differ"]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--rewrite", action="store_true", help="model realism pass (uses agent.llm backend)")
    ap.add_argument("--model", default=None, help="model for --rewrite, e.g. claude-sonnet-5-5")
    ap.add_argument("--limit-rewrite", type=int, default=None, help="only rewrite the first N cases")
    ap.add_argument("--paired", action="store_true", help="write each case for both payers")
    a = ap.parse_args()
    build(a.batch, a.n, a.seed, a.rewrite, a.model, a.limit_rewrite, paired=a.paired)


if __name__ == "__main__":
    main()
