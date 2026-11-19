"""Code checks that a rendered (or model-rewritten) chart says what the blueprint says.

The template renderer should always pass. These checks matter most after the
optional model rewrite pass, which can drop a planted fact or leak a new one.
"""

from __future__ import annotations

import re

from agent.checks import quote_in_text
from agent.schemas import CaseGold, ChartDocument
from synth.blueprint import Blueprint

RESULT = r"[^\n]*\b(nonreactive|non-reactive|reactive|negative|positive|indeterminate|detected)\b"
LEXICON = {
    "tb": re.compile(r"(quantiferon|igra|t-spot|tuberculin|ppd)" + RESULT, re.I),
    "hbc": re.compile(r"(core antibody|anti-?hbc|hep b core|hbcab)" + RESULT, re.I),
    "hbsag": re.compile(r"(surface antigen|hbsag|surface ag|surf ag)" + RESULT, re.I),
    "fcp": re.compile(r"calprotectin[^\n]*\d", re.I),
}
# (criterion, state) -> lexicon entries that must NOT appear anywhere in the chart.
FORBIDDEN = {
    ("C6", "missing"): ["tb"],
    ("C6", "ordered_not_resulted"): ["tb"],
    ("C7", "missing"): ["hbc", "hbsag"],
    ("C7", "decoy"): ["hbc", "hbsag"],
    ("C7", "partial"): ["hbc"],
    ("C2", "crp_only"): ["fcp"],
    ("C2", "stale_scope"): ["fcp"],
}
REAL_PAYERS = re.compile(
    r"\b(aetna|cigna|unitedhealth\w*|humana|anthem|elevance|kaiser|blue cross|blue shield|bcbs|centene|"
    r"molina|caremark|express scripts|optum\w*|highmark|wellcare)\b", re.I)


def validate(bp: Blueprint, docs: list[ChartDocument], gold: CaseGold) -> list[str]:
    errors: list[str] = []
    by_id = {d.doc_id: d for d in docs}
    full = "\n".join(d.text for d in docs)

    for cid, g in gold.criteria.items():
        for ev in g.evidence:
            doc = by_id.get(ev.doc_id)
            if doc is None:
                errors.append(f"{cid}: evidence cites unknown doc {ev.doc_id}")
            elif not quote_in_text(ev.quote, doc.text):
                errors.append(f"{cid}: planted quote missing from {ev.doc_id}: {ev.quote[:60]!r}")

    for (cid, state), keys in FORBIDDEN.items():
        if bp.states.get(cid) == state:
            for key in keys:
                if m := LEXICON[key].search(full):
                    errors.append(f"{cid}={state}: forbidden fact present: {m.group(0)[:60]!r}")

    if m := REAL_PAYERS.search(full):
        errors.append(f"real payer name present: {m.group(0)!r}")
    for d in docs:
        if d.date > bp.request_date:
            errors.append(f"{d.doc_id}: dated after the request")
    if bp.last_name.lower() not in full.lower():
        errors.append("patient name missing from chart")
    return errors
