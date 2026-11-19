"""Backend plumbing without any model call: cache hits and the replay backend."""

import pytest
from pydantic import BaseModel

from agent import llm


class Out(BaseModel):
    answer: str


def test_replay_uses_cache_and_fails_closed(tmp_path, monkeypatch):
    monkeypatch.setattr(llm, "CACHE_DIR", tmp_path)
    cfg = llm.LLMConfig(backend="replay", model="claude-opus-5-5")
    kwargs = dict(step="t", prompt_id="t@v1", system="s", user="u", schema=Out, cfg=cfg)

    with pytest.raises(llm.LLMError, match="no cached response"):
        llm.structured_call(**kwargs)

    h = llm._request_hash(cfg.model, cfg.effort, "s", "u", Out.model_json_schema())
    llm._cache_put(h, {"output": {"answer": "42"}})
    obj, rec = llm.structured_call(**kwargs)
    assert obj.answer == "42" and rec.cache_hit


def test_cache_key_changes_with_model_and_prompt():
    s = Out.model_json_schema()
    base = llm._request_hash("claude-opus-5-5", None, "s", "u", s)
    assert base != llm._request_hash("claude-sonnet-5-5", None, "s", "u", s)
    assert base != llm._request_hash("claude-opus-5-5", None, "s2", "u", s)
    assert base != llm._request_hash("claude-opus-5-5", "high", "s", "u", s)
