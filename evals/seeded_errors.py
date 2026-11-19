"""Seed deliberate errors into real drafted packets and measure whether step 9 catches them.

    python -m evals.seeded_errors --run m3-opus-packets

Each mutation changes one claim's text and keeps its citation verbatim and valid,
so the step 8 code check cannot catch it. Only the independent verifier can.
Results go to docs/VERIFIER_REPORT.md.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from agent import intake as I
from agent.llm import LLMConfig
from agent.pipeline import RUNS
from agent.schemas import CitedSentence, PacketDraft, PipelineResult
from agent.verify import verify

ROOT = Path(__file__).resolve().parent.parent

SWAPS = [("negative", "positive"), ("Negative", "Positive"), ("NEGATIVE", "POSITIVE"),
         ("nonreactive", "reactive"), ("Nonreactive", "Reactive"), ("non-reactive", "reactive"),
         ("infliximab", "adalimumab"), ("Infliximab", "Adalimumab"), ("adalimumab", "infliximab"),
         ("Adalimumab", "Infliximab"), ("azathioprine", "methotrexate"), ("Azathioprine", "Methotrexate")]


@dataclass
class Seeded:
    kind: str
    claim_ref: str
    before: str
    after: str
    packet: PacketDraft


def _letter_with(pk: PacketDraft, i: int, text: str) -> PacketDraft:
    letter = list(pk.letter)
    letter[i] = letter[i].model_copy(update={"text": text})
    return pk.model_copy(update={"letter": letter})


def _factual(pk: PacketDraft):
    return [(i, s) for i, s in enumerate(pk.letter) if s.is_factual]


def seed_all(pk: PacketDraft) -> list[Seeded]:
    out: list[Seeded] = []
    facts = _factual(pk)
    # 1. a number changed (lab value, dose or weight)
    for i, s in facts:
        m = re.search(r"\b(\d{2,4})(?:\.\d)?\s*(mg|kg|ug/g|mcg/g)\b", s.text)
        if m:
            new = s.text[:m.start(1)] + str(int(m.group(1)) + 37) + s.text[m.end(1):]
            out.append(Seeded("changed number", f"letter:{i}", s.text, new, _letter_with(pk, i, new)))
            break
    # 2. a date moved back two years (could push a result outside its window)
    for i, s in facts:
        m = re.search(r"\b(20\d\d)-(\d\d)-(\d\d)\b", s.text) or re.search(r"\b(\d\d)/(\d\d)/(20\d\d)\b", s.text)
        if m:
            yr = m.group(1) if m.group(1).startswith("20") else m.group(3)
            new = s.text.replace(yr, str(int(yr) - 2), 1)
            out.append(Seeded("shifted date", f"letter:{i}", s.text, new, _letter_with(pk, i, new)))
            break
    # 3. a result flipped (negative -> positive, nonreactive -> reactive)
    for i, s in facts:
        hit = next(((a, b) for a, b in SWAPS[:6] if re.search(rf"\b{a}\b", s.text)), None)
        if hit:
            new = re.sub(rf"\b{hit[0]}\b", hit[1], s.text, count=1)
            out.append(Seeded("flipped result", f"letter:{i}", s.text, new, _letter_with(pk, i, new)))
            break
    # 4. the wrong drug named
    for i, s in facts:
        hit = next(((a, b) for a, b in SWAPS[6:] if re.search(rf"\b{a}\b", s.text)), None)
        if hit:
            new = re.sub(rf"\b{hit[0]}\b", hit[1], s.text, count=1)
            out.append(Seeded("wrong drug", f"letter:{i}", s.text, new, _letter_with(pk, i, new)))
            break
    # 5. an unsupported claim with a real, verbatim citation borrowed from another sentence
    if facts:
        i, s = facts[0]
        extra = CitedSentence(text="The member also completed a 6-month trial of vedolizumab, stopped for loss of response.",
                              citations=s.citations)
        letter = list(pk.letter)
        letter.insert(i + 1, extra)
        out.append(Seeded("unsupported claim", f"letter:{i + 1}", "", extra.text,
                          pk.model_copy(update={"letter": letter})))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--model")
    ap.add_argument("--max-packets", type=int, default=2)
    a = ap.parse_args(argv)
    cfg = LLMConfig()
    if a.model:
        cfg.model = a.model
    results = []
    for path in sorted((RUNS / a.run).glob("PA-*/result.json")):
        res = PipelineResult.model_validate_json(path.read_text())
        if res.packet is not None:
            results.append(res)
    results = results[: a.max_packets]
    rows = []
    for res in results:
        from evals.metrics import find_case
        _, charts_dir = find_case(res.request.request_id)
        chart = I.load_chart(res.request.patient_id, charts_dir)
        clean_flags = [c.claim_ref for c in res.verification.checks if not c.supported] if res.verification else []
        for sd in seed_all(res.packet):
            v, rec, _ = verify(res.request, chart, sd.packet, cfg)
            flagged = {c.claim_ref: c.issue for c in v.checks if not c.supported}
            caught = sd.claim_ref in flagged
            rows.append((res.request.request_id, sd, caught, flagged.get(sd.claim_ref), not v.overall_pass,
                         sorted(set(flagged) - {sd.claim_ref}), clean_flags))
            print(f"  {res.request.request_id} {sd.kind:18} caught={caught}", flush=True)
    n = len(rows)
    caught = sum(r[2] for r in rows)
    L = ["# Verifier report (step 9 seeded errors)", "",
         f"Run `{a.run}`, verifier model `{cfg.model}`. Each seeded error changes one claim in a real drafted packet. "
         "Its citation stays valid and verbatim, so the step 8 code check cannot catch it; only the independent "
         "verifier can.", "",
         f"**Caught {caught} of {n} seeded errors** (the exact claim flagged). Packets blocked from sign-off: "
         f"{sum(r[4] for r in rows)} of {n}.", "",
         "| Case | Error | Claim | Seeded text | Caught | Verifier's reason | Other claims flagged |",
         "|---|---|---|---|---|---|---|"]
    for rid, sd, ok, why, blocked, others, clean in rows:
        L.append(f"| {rid} | {sd.kind} | {sd.claim_ref} | {sd.after[:110]} | {'yes' if ok else '**no**'} | "
                 f"{(why or '-')[:140]} | {', '.join(others) or '-'} |")
    L += ["", "Flags the verifier raised on the unmodified packets (false-alarm baseline): "
          + "; ".join(f"{r.request.request_id}: {', '.join(c.claim_ref for c in r.verification.checks if not c.supported) or 'none'}"
                      for r in results if r.verification) + "."]
    (ROOT / "docs" / "VERIFIER_REPORT.md").write_text("\n".join(L) + "\n")
    print(f"wrote docs/VERIFIER_REPORT.md: caught {caught}/{n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
