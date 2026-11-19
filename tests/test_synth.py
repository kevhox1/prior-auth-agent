"""The synthetic generator: integrity of every committed case, and determinism."""

import filecmp
from collections import Counter
from pathlib import Path

import pytest

from agent import intake
from agent.schemas import Status
from synth.build import build
from tests.integrity import check_case

BATCHES = sorted((intake.DATA / "synth").glob("batch-*")) if (intake.DATA / "synth").exists() else []
CASES = [(b, c) for b in BATCHES for c in intake.list_cases(b / "cases")]


@pytest.mark.parametrize("batch,case_id", CASES, ids=[c for _, c in CASES])
def test_committed_synthetic_case_is_consistent(batch, case_id):
    check_case(case_id, batch / "cases", batch / "charts")


def test_generator_is_deterministic_and_mixed(tmp_path):
    a = build(batch=9, n=40, seed=123, out_root=tmp_path / "a")
    b = build(batch=9, n=40, seed=123, out_root=tmp_path / "b")
    cmp = filecmp.dircmp(a, b)
    assert not cmp.diff_files and not cmp.left_only and not cmp.right_only

    outcomes = Counter()
    for case_id in intake.list_cases(a / "cases"):
        check_case(case_id, a / "cases", a / "charts")
        outcomes[intake.load_gold(case_id, a / "cases").packet_outcome] += 1
    assert len(outcomes) == 3, f"expected all three packet outcomes, got {outcomes}"


def test_no_met_alternate_and_every_state_reachable():
    from synth.blueprint import STATES
    from synth.label import STATUS
    for cid, menu in STATES.items():
        assert set(menu) == set(STATUS[cid]), cid
    for cid, table in STATUS.items():
        for status, alts in table.values():
            assert not (status != Status.MET and Status.MET in alts)


def test_latent_tb_treatment_starts_after_positive_screen_and_xray():
    """QA agent finding (M2): treatment must not predate the test that prompted it."""
    import re
    from agent.checks import parse_date
    for batch, case_id in CASES:
        gold = intake.load_gold(case_id, batch / "cases")
        if gold.criteria["C6"].note != "synthetic state: positive_with_plan":
            continue
        chart = intake.load_chart(case_id.replace("PA", "PT"), batch / "charts")
        xray = next(d for d in chart.documents if "chest-xray" in d.doc_id)
        labs = max(d.date for d in chart.documents if d.doc_type.value == "labs" and "POSITIVE" in d.text.upper()
                   and "QUANTIFERON" in d.text.upper())
        starts = [parse_date(m) for d in chart.documents
                  for m in re.findall(r"rifampin daily for 4 months, started ([\d/-]+)\.", d.text)]
        assert starts, case_id
        for st in starts:
            assert labs <= xray.date <= st, (case_id, labs, xray.date, st)
