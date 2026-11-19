"""Step 6: deterministic checks. Code, not model.

The model proposes a status in step 5; this module checks it. The rule is
one-directional: code can downgrade a MET (to INSUFFICIENT_EVIDENCE or NOT_MET)
but never upgrades anything. Every downgrade is recorded with the reason, and
the model's original status is kept in `status_before_checks`.

Checks:
- quote_found       every quote appears verbatim (whitespace forgiven) in the cited document
- doc_date_matches  the cited date is the document's date
- patient_matches   the cited document belongs to this patient
- date_in_window    for criteria with a lookback, a cited result is dated inside it, and
                    no date written inside the quote itself falls outside it (copy-forward trap)
- age_ok            age from the date of birth in the chart, computed at the request date
- dose_in_label     requested IV dose matches the label tier for the cited weight; weight is recent
"""

from __future__ import annotations

import re
from datetime import date, timedelta
from functools import cache
from pathlib import Path

import yaml

from agent.schemas import (
    Chart,
    Criterion,
    CriterionAssessment,
    CriterionAssessmentDraft,
    CriterionType,
    DeterministicChecks,
    InjectionFlag,
    PARequest,
    Status,
)

REF_DIR = Path(__file__).resolve().parent.parent / "data" / "reference"
_WS = re.compile(r"\s+")


def normalize_ws(s: str) -> str:
    """Collapse whitespace runs to one space.

    Only whitespace is forgiven: scanned outside records wrap lines and pad
    columns unpredictably. Characters, case and punctuation must match exactly.
    """
    return _WS.sub(" ", s).strip()


def quote_in_text(quote: str, text: str) -> bool:
    q = normalize_ws(quote)
    return bool(q) and q in normalize_ws(text)


# --------------------------------------------------------------------------
# Reference tables
# --------------------------------------------------------------------------


@cache
def policy_rules(policy_id: str) -> dict:
    return yaml.safe_load((REF_DIR / "policy_rules.yaml").read_text())[policy_id]


@cache
def label_table() -> dict:
    return yaml.safe_load((REF_DIR / "label_dosing.yaml").read_text())


# --------------------------------------------------------------------------
# Small parsers
# --------------------------------------------------------------------------

_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_US = re.compile(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b")
_DOB = re.compile(r"(?:date of birth|\bDOB)\s*:?\s*(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})", re.I)
_WEIGHT = re.compile(r"(\d{2,3}(?:\.\d)?)\s*kg\b", re.I)
_IV_MG = re.compile(r"(\d{3})\s*mg\s+(?:IV|intravenous)", re.I)
_SC = re.compile(r"(\d{2,3})\s*mg\s+(?:SC|subcutaneous(?:ly)?)\s+every\s+(\d+)\s+weeks", re.I)


def parse_date(s: str) -> date | None:
    if m := _ISO.fullmatch(s.strip()):
        return date(int(m[1]), int(m[2]), int(m[3]))
    if m := _US.fullmatch(s.strip()):
        return date(int(m[3]), int(m[1]), int(m[2]))
    return None


def dates_in(text: str) -> list[date]:
    out = []
    for m in _ISO.finditer(text):
        try:
            out.append(date(int(m[1]), int(m[2]), int(m[3])))
        except ValueError:
            pass
    for m in _US.finditer(text):
        try:
            out.append(date(int(m[3]), int(m[1]), int(m[2])))
        except ValueError:
            pass
    return out


def months_before(d: date, months: int) -> date:
    y, m = divmod(d.month - 1 - months, 12)
    year, month = d.year + y, m + 1
    day = min(d.day, [31, 29 if year % 4 == 0 and (year % 100 or year % 400 == 0) else 28,
                      31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)


def age_on(dob: date, on: date) -> int:
    return on.year - dob.year - ((on.month, on.day) < (dob.month, dob.day))


def find_dobs(chart: Chart) -> set[date]:
    out = set()
    for d in chart.documents:
        for m in _DOB.finditer(d.text):
            if (p := parse_date(m.group(1))) is not None:
                out.add(p)
    return out


def iv_tier_mg(drug: str, weight_kg: float) -> int:
    for tier in label_table()[drug]["iv_induction"]["tiers"]:
        if tier["max_kg"] is None or weight_kg <= tier["max_kg"]:
            return tier["mg"]
    raise ValueError("label table has no open-ended top tier")


# --------------------------------------------------------------------------
# The check
# --------------------------------------------------------------------------


def _norm_ref(ref: str) -> str:
    return re.sub(r"[^0-9a-z().]", "", ref.lower().replace("section", ""))


def _rule_for(rules: dict, key: str, ref: str):
    table = {_norm_ref(k): v for k, v in (rules.get(key) or {}).items()}
    return table.get(_norm_ref(ref))


def check(
    draft: CriterionAssessmentDraft,
    crit: Criterion,
    chart: Chart,
    req: PARequest,
    policy_id: str,
) -> CriterionAssessment:
    rules = policy_rules(policy_id)
    dc = DeterministicChecks()
    fail_insufficient: list[str] = []   # reasons a MET becomes INSUFFICIENT_EVIDENCE
    fail_not_met: list[str] = []        # reasons a MET becomes NOT_MET

    # --- citations (every status) ------------------------------------------
    if draft.evidence:
        dc.quote_found = dc.doc_date_matches = dc.patient_matches = True
    for ev in draft.evidence:
        doc = chart.get(ev.doc_id)
        if not ev.doc_id.startswith(f"{req.patient_id}/"):
            dc.patient_matches = False
            fail_insufficient.append(f"cites a document from another patient: {ev.doc_id}")
        if doc is None:
            dc.quote_found = False
            fail_insufficient.append(f"cites a document that does not exist: {ev.doc_id}")
            continue
        if not quote_in_text(ev.quote, doc.text):
            dc.quote_found = False
            fail_insufficient.append(f"quote not found verbatim in {ev.doc_id}: {ev.quote[:70]!r}")
        if ev.doc_date != doc.date:
            dc.doc_date_matches = False
            fail_insufficient.append(f"cited date {ev.doc_date} but {ev.doc_id} is dated {doc.date}")

    # --- lookback window ---------------------------------------------------
    lookback = _rule_for(rules, "lookback_months", crit.policy_ref) or crit.lookback_months
    if lookback and draft.evidence:
        start = months_before(req.request_date, lookback)
        in_window = [e for e in draft.evidence if start <= e.doc_date <= req.request_date]
        # A recent note that quotes an old date may be a copied-forward result (an IBD failure mode).
        # It may also be context, such as when a drug was started (the PCSK9 reuse test, B41). So the
        # criterion passes when at least one cited passage is in the window and carries no older date.
        clean = [e for e in in_window if not any(d < start for d in dates_in(e.quote))]
        stale_in_quote = [] if clean else [d for e in in_window for d in dates_in(e.quote) if d < start]
        dc.date_in_window = bool(clean)
        if not in_window:
            fail_insufficient.append(f"no cited evidence dated on or after {start} ({lookback}-month lookback)")
        if stale_in_quote:
            fail_insufficient.append(
                f"quote carries a date before the {lookback}-month window ({min(stale_in_quote)}); "
                "likely copied forward from an older result")

    # --- age ---------------------------------------------------------------
    if crit.type == CriterionType.AGE:
        dobs = find_dobs(chart)
        if len(dobs) == 1:
            a = age_on(next(iter(dobs)), req.request_date)
            dc.age_ok = a >= rules["min_age"]
            dc.notes.append(f"age {a} on {req.request_date} from DOB {next(iter(dobs))}")
            if not dc.age_ok:
                fail_not_met.append(f"computed age {a} is under {rules['min_age']}")
        else:
            dc.age_ok = False
            fail_insufficient.append("no date of birth found" if not dobs
                                     else f"chart has conflicting dates of birth: {sorted(dobs)}")

    # --- dose --------------------------------------------------------------
    if crit.type == CriterionType.DOSING and req.drug in label_table():
        dose_ok = True
        iv = _IV_MG.search(req.dose)
        weights = [(float(w), e) for e in draft.evidence for w in _WEIGHT.findall(e.quote)]
        sc = _SC.search(req.dose)
        lab = label_table()[req.drug]["sc_maintenance"]
        if sc and (int(sc[1]) != lab["mg"] or int(sc[2]) < lab["interval_weeks"]):
            dose_ok = False
            fail_not_met.append(f"maintenance '{sc[0]}' is outside label ({lab['mg']} mg every {lab['interval_weeks']} weeks)")
        if iv is None:
            dose_ok = False
            fail_insufficient.append("requested IV induction dose not stated in mg")
        elif not weights:
            dose_ok = False
            fail_insufficient.append("no body weight cited")
        else:
            w, ev = max(weights, key=lambda t: t[1].doc_date)
            expected = iv_tier_mg(req.drug, w)
            dc.notes.append(f"weight {w} kg ({ev.doc_date}) -> label tier {expected} mg; requested {iv[1]} mg")
            if int(iv[1]) != expected:
                dose_ok = False
                fail_not_met.append(f"requested {iv[1]} mg IV but label tier for {w} kg is {expected} mg")
            recency = _rule_for(rules, "weight_recency_days", crit.policy_ref)
            if recency and ev.doc_date < req.request_date - timedelta(days=recency):
                dose_ok = False
                fail_insufficient.append(f"most recent cited weight is from {ev.doc_date}, older than {recency} days")
        dc.dose_in_label = dose_ok

    dc.notes.extend(fail_not_met + fail_insufficient)

    # --- downgrade a MET that failed anything --------------------------------
    status, before = draft.status, None
    missing = list(draft.missing_items)
    if draft.status == Status.MET and (fail_not_met or fail_insufficient):
        before = Status.MET
        if fail_not_met:
            status = Status.NOT_MET
        else:
            status = Status.INSUFFICIENT_EVIDENCE
            missing = missing or [f"Verifiable documentation for policy {crit.policy_ref}: {fail_insufficient[0]}"]

    data = draft.model_dump()
    data.update(status=status, missing_items=missing)
    return CriterionAssessment(**data, deterministic_checks=dc, status_before_checks=before)


# --------------------------------------------------------------------------
# Injection backstop (defense in depth; the model is asked to flag too)
# --------------------------------------------------------------------------

_INJECTION = re.compile(
    r"[^\n]*(?:automated (?:review|system)|AI (?:system|reviewer|assistant)|language model|"
    r"ignore (?:all |any |the )?(?:previous|prior|above)|mark (?:every|all) criteri\w*|"
    r"skip (?:the )?verification|disregard (?:the )?(?:policy|instructions))[^\n]*",
    re.I,
)


def scan_injection(chart: Chart) -> list[InjectionFlag]:
    return [
        InjectionFlag(doc_id=d.doc_id, quote=m.group(0).strip(), note="code scan: text addressed to an automated reviewer")
        for d in chart.documents
        for m in _INJECTION.finditer(d.text)
    ]
