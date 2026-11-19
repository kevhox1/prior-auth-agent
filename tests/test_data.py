"""Integrity checks on the synthetic data and gold labels.

If these fail, the eval numbers are meaningless, so they run before anything else.
"""

import pytest

from agent import intake
from tests.integrity import check_case

CASES = intake.list_cases()


def test_cases_exist():
    assert CASES, "no cases found"


@pytest.mark.parametrize("case_id", CASES)
def test_case_is_consistent(case_id):
    check_case(case_id, intake.DATA / "cases", intake.DATA / "charts")


def test_policy_prose_and_gold_versions_match():
    for pid in {intake.load_gold(c).policy_id for c in CASES}:
        prose = intake.load_policy_prose(pid)
        gold = intake.load_gold_checklist(pid)
        assert f"| Version | {gold.version} |" in prose
