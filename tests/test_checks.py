"""Step 6 unit tests. The property that matters: code can only take a MET away."""

from datetime import date

import pytest

from agent import intake as I
from agent.checks import age_on, check, dates_in, iv_tier_mg, months_before, scan_injection
from agent.schemas import CriterionAssessmentDraft, Evidence, Status

POLICY = "northfield-ustekinumab-ibd"


@pytest.fixture(scope="module")
def pa2():
    req = I.load_request("PA-0002")
    chart = I.load_chart(req.patient_id)
    cl = I.load_gold_checklist(POLICY)
    return req, chart, cl


def draft(cid, status, evidence, missing=()):
    return CriterionAssessmentDraft(criterion_id=cid, status=status, confidence=0.9, evidence=evidence,
                                    reasoning="test", missing_items=list(missing))


def ev(doc_id, quote, d):
    return Evidence(doc_id=doc_id, quote=quote, doc_date=d)


# --- helpers -----------------------------------------------------------------

def test_months_before_handles_month_ends():
    assert months_before(date(2026, 11, 18), 12) == date(2025, 11, 18)
    assert months_before(date(2026, 3, 31), 1) == date(2026, 2, 28)
    assert months_before(date(2028, 3, 31), 1) == date(2028, 2, 29)


def test_age_on_birthday_boundary():
    assert age_on(date(2008, 11, 18), date(2026, 11, 18)) == 18
    assert age_on(date(2008, 11, 19), date(2026, 11, 18)) == 17


@pytest.mark.parametrize("kg,mg", [(40, 260), (55, 260), (55.1, 390), (85, 390), (85.1, 520), (130, 520)])
def test_iv_tiers_inclusive_upper_bounds(kg, mg):
    assert iv_tier_mg("ustekinumab", kg) == mg


def test_dates_in_reads_iso_and_us():
    assert dates_in("drawn 2024-08-21, repeated 03/05/2026") == [date(2024, 8, 21), date(2026, 3, 5)]


# --- citations ---------------------------------------------------------------

def test_true_met_passes(pa2):
    req, chart, cl = pa2
    d = draft("C6", Status.MET, [ev("PT-0002/labs-2026-10-06", "QuantiFERON-TB Gold Plus              NEGATIVE",
                                    date(2026, 10, 6))])
    a = check(d, cl.find("C6"), chart, req, POLICY)
    assert a.status == Status.MET and a.status_before_checks is None
    assert a.deterministic_checks.passed()


def test_whitespace_differences_are_forgiven(pa2):
    req, chart, cl = pa2
    d = draft("C6", Status.MET, [ev("PT-0002/labs-2026-10-06", "QuantiFERON-TB Gold Plus NEGATIVE", date(2026, 10, 6))])
    assert check(d, cl.find("C6"), chart, req, POLICY).status == Status.MET


def test_fabricated_quote_downgrades_met(pa2):
    req, chart, cl = pa2
    d = draft("C7", Status.MET, [ev("PT-0002/labs-2026-10-06", "Hepatitis B core antibody, total: Nonreactive",
                                    date(2026, 10, 6))])
    a = check(d, cl.find("C7"), chart, req, POLICY)
    assert a.status == Status.INSUFFICIENT_EVIDENCE and a.status_before_checks == Status.MET
    assert a.deterministic_checks.quote_found is False and a.missing_items


def test_paraphrase_is_not_verbatim(pa2):
    req, chart, cl = pa2
    d = draft("C6", Status.MET, [ev("PT-0002/labs-2026-10-06", "QuantiFERON-TB Gold Plus: negative", date(2026, 10, 6))])
    assert check(d, cl.find("C6"), chart, req, POLICY).status == Status.INSUFFICIENT_EVIDENCE


def test_wrong_document_date_downgrades(pa2):
    req, chart, cl = pa2
    d = draft("C6", Status.MET, [ev("PT-0002/labs-2026-10-06", "QuantiFERON-TB Gold Plus              NEGATIVE",
                                    date(2026, 10, 7))])
    a = check(d, cl.find("C6"), chart, req, POLICY)
    assert a.status == Status.INSUFFICIENT_EVIDENCE and a.deterministic_checks.doc_date_matches is False


def test_other_patients_document_downgrades(pa2):
    req, chart, cl = pa2
    d = draft("C3", Status.MET, [ev("PT-0001/gi-note-2026-11-03", "Start ustekinumab", date(2026, 11, 3))])
    a = check(d, cl.find("C3"), chart, req, POLICY)
    assert a.status == Status.INSUFFICIENT_EVIDENCE and a.deterministic_checks.patient_matches is False


# --- lookback ------------------------------------------------------------------

def test_stale_tb_screen_downgrades(pa2):
    req, chart, cl = pa2
    doc = chart.get("PT-0002/outside-records-2024-08-21")
    line = next(ln for ln in doc.text.splitlines() if "QUANTIFERON" in ln.upper())
    d = draft("C6", Status.MET, [ev(doc.doc_id, line, doc.date)])
    a = check(d, cl.find("C6"), chart, req, POLICY)
    assert a.status == Status.INSUFFICIENT_EVIDENCE and a.deterministic_checks.date_in_window is False


def test_lookback_comes_from_rules_even_if_extraction_missed_it(pa2):
    req, chart, cl = pa2
    crit = cl.find("C6").model_copy(update={"lookback_months": None})
    doc = chart.get("PT-0002/outside-records-2024-08-21")
    line = next(ln for ln in doc.text.splitlines() if "QUANTIFERON" in ln.upper())
    a = check(draft("C6", Status.MET, [ev(doc.doc_id, line, doc.date)]), crit, chart, req, POLICY)
    assert a.status == Status.INSUFFICIENT_EVIDENCE


def test_copied_forward_date_inside_quote_downgrades(pa2):
    """A recent note repeating an old result: document date in window, result date not."""
    from agent.schemas import Chart, ChartDocument, DocType

    req, chart, cl = pa2
    note = ChartDocument(doc_id="PT-0002/gi-note-2026-11-10", patient_id="PT-0002", doc_type=DocType.PROGRESS_NOTE,
                         date=date(2026, 11, 10), author="t", text="TB: QuantiFERON negative 2024-08-21.")
    ch = Chart(patient_id="PT-0002", documents=[*chart.documents, note])
    d = draft("C6", Status.MET, [ev(note.doc_id, "TB: QuantiFERON negative 2024-08-21.", note.date)])
    a = check(d, cl.find("C6"), ch, req, POLICY)
    assert a.status == Status.INSUFFICIENT_EVIDENCE and a.deterministic_checks.date_in_window is False


def test_old_context_date_passes_when_a_clean_result_is_also_cited():
    """B41, found by the PCSK9 reuse test: a note gives the drug's old start date as context, next to a
    current lab. The current lab carries the criterion; the older date is not a copied-forward result."""
    pol = "calder-evolocumab-lipids"
    req = I.load_request("PA-0101")
    chart = I.load_chart(req.patient_id)
    crit = I.load_gold_checklist(pol).find("C2")
    note = ev("PT-0101/cardiology-note-2026-11-10", "Lipid panel 10/27/2026: LDL-C 98 mg/dL on atorvastatin 80 mg and "
              "ezetimibe 10 mg (ezetimibe since 06/02/2026).", date(2026, 11, 10))
    lab = ev("PT-0101/labs-2026-10-27", "LDL cholesterol, calculated         98 mg/dL      <100", date(2026, 10, 27))
    assert check(draft("C2", Status.MET, [lab, note]), crit, chart, req, pol).status == Status.MET
    # The note alone is still treated as possibly copied forward.
    alone = check(draft("C2", Status.MET, [note]), crit, chart, req, pol)
    assert alone.status == Status.INSUFFICIENT_EVIDENCE


# --- age and dose ------------------------------------------------------------------

def test_age_computed_from_chart(pa2):
    req, chart, cl = pa2
    d = draft("C4", Status.MET, [ev("PT-0002/demographics-2026-10-30", "Date of birth: 11/02/1984", date(2026, 10, 30))])
    a = check(d, cl.find("C4"), chart, req, POLICY)
    assert a.status == Status.MET and a.deterministic_checks.age_ok is True
    assert any("age 42" in n for n in a.deterministic_checks.notes)


def test_minor_is_not_met(pa2):
    req, chart, cl = pa2
    req = req.model_copy(update={"request_date": date(2002, 10, 1)})
    d = draft("C4", Status.MET, [ev("PT-0002/demographics-2026-10-30", "Date of birth: 11/02/1984", date(2026, 10, 30))])
    a = check(d, cl.find("C4"), chart, req, POLICY)
    assert a.status == Status.NOT_MET


def test_correct_dose_passes(pa2):
    req, chart, cl = pa2
    d = draft("C9", Status.MET, [ev("PT-0002/gi-note-2026-10-30", "Weight 58.2 kg.", date(2026, 10, 30))])
    a = check(d, cl.find("C9"), chart, req, POLICY)
    assert a.status == Status.MET and a.deterministic_checks.dose_in_label is True


def test_wrong_tier_is_not_met(pa2):
    req, chart, cl = pa2
    req = req.model_copy(update={"dose": "520 mg IV once, then 90 mg SC every 8 weeks"})
    d = draft("C9", Status.MET, [ev("PT-0002/gi-note-2026-10-30", "Weight 58.2 kg.", date(2026, 10, 30))])
    a = check(d, cl.find("C9"), chart, req, POLICY)
    assert a.status == Status.NOT_MET and a.deterministic_checks.dose_in_label is False


def test_short_maintenance_interval_is_not_met(pa2):
    req, chart, cl = pa2
    req = req.model_copy(update={"dose": "390 mg IV once, then 90 mg SC every 4 weeks"})
    d = draft("C9", Status.MET, [ev("PT-0002/gi-note-2026-10-30", "Weight 58.2 kg.", date(2026, 10, 30))])
    assert check(d, cl.find("C9"), chart, req, POLICY).status == Status.NOT_MET


def test_stale_weight_is_insufficient(pa2):
    req, chart, cl = pa2
    req = req.model_copy(update={"request_date": date(2027, 1, 15)})
    d = draft("C9", Status.MET, [ev("PT-0002/gi-note-2026-10-30", "Weight 58.2 kg.", date(2026, 10, 30))])
    assert check(d, cl.find("C9"), chart, req, POLICY).status == Status.INSUFFICIENT_EVIDENCE


# --- code never upgrades ----------------------------------------------------------

@pytest.mark.parametrize("status", [Status.NOT_MET, Status.INSUFFICIENT_EVIDENCE])
def test_code_never_upgrades(pa2, status):
    req, chart, cl = pa2
    d = draft("C6", status, [ev("PT-0002/labs-2026-10-06", "QuantiFERON-TB Gold Plus              NEGATIVE",
                                date(2026, 10, 6))], missing=["x"])
    a = check(d, cl.find("C6"), chart, req, POLICY)
    assert a.status == status and a.status_before_checks is None


# --- injection backstop -------------------------------------------------------------

def test_injection_scan_finds_planted_instruction():
    from pathlib import Path
    import csv

    base = Path(I.DATA / "synth" / "batch-001")
    rows = list(csv.DictReader((base / "manifest.csv").open()))
    inj = [r["request_id"] for r in rows if r["knob_injection"] == "True"]
    clean = [r["request_id"] for r in rows if r["knob_injection"] == "False"]
    for rid in inj:
        chart = I.load_chart(rid.replace("PA", "PT"), base / "charts")
        assert scan_injection(chart), rid
    for rid in clean:
        chart = I.load_chart(rid.replace("PA", "PT"), base / "charts")
        assert not scan_injection(chart), rid
