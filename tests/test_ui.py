"""Smoke test the reviewer UI with Streamlit's AppTest on a saved result (no model calls)."""

import shutil

import pytest
from streamlit.testing.v1 import AppTest

from agent.pipeline import RUNS
from tests.test_packet import _result

UI_RUN = "_ui-test"


@pytest.fixture()
def saved_case():
    res = _result()
    d = RUNS / UI_RUN / res.request.request_id
    d.mkdir(parents=True, exist_ok=True)
    (d / "result.json").write_text(res.model_dump_json())
    (d / "audit.jsonl").write_text("")
    yield d
    shutil.rmtree(RUNS / UI_RUN)


def test_ui_renders_and_gates_signoff(saved_case):
    at = AppTest.from_file("../ui/app.py", default_timeout=30)
    at.run()
    assert not at.exception
    at.sidebar.selectbox[0].select(UI_RUN).run()
    assert not at.exception
    assert any("PA-0001" in t.value for t in at.title)
    button = next(b for b in at.button if b.label == "Sign off")
    assert button.disabled  # no criterion decided yet
    for radio in at.radio:
        if radio.label == "Decision" and "approve" in radio.options:
            radio.set_value("approve")
    next(s for s in at.sidebar.selectbox if s.label == "Role").select("physician")
    at.run()
    assert not at.exception
    button = next(b for b in at.button if b.label == "Sign off")
    assert not button.disabled
    button.click().run()
    assert (saved_case / "submission" / "receipt.json").exists()
    assert "10_signoff" in (saved_case / "audit.jsonl").read_text()
