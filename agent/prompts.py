"""Versioned prompt files.

Each prompt is `prompts/<prompt_id>@<version>.md` with a YAML header. Modules
pin the exact version they use, so a prompt change is a visible code change and
the version lands in the audit log.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from pathlib import Path

import yaml

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


@dataclass(frozen=True)
class Prompt:
    prompt_id: str
    version: str
    text: str

    @property
    def ref(self) -> str:
        return f"{self.prompt_id}@{self.version}"


@cache
def load_prompt(ref: str) -> Prompt:
    """Load 'assess@v1' from prompts/assess@v1.md and check its header agrees."""
    raw = (PROMPTS_DIR / f"{ref}.md").read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"{ref}: missing header")
    _, header, body = raw.split("---\n", 2)
    meta = yaml.safe_load(header)
    pid, ver = ref.split("@")
    if meta.get("prompt_id") != pid or meta.get("version") != ver:
        raise ValueError(f"{ref}: header says {meta.get('prompt_id')}@{meta.get('version')}")
    return Prompt(prompt_id=pid, version=ver, text=body.strip())
