"""Step 1: intake. Loads the request, chart and policy from disk.

Loaders, plus request validation and the decision clock (urgency).
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from agent.schemas import CaseGold, Chart, ChartDocument, IntakeResult, PARequest, PolicyChecklist

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def _split_front_matter(raw: str, path: Path) -> tuple[dict, str]:
    if not raw.startswith("---\n"):
        raise ValueError(f"{path}: missing front matter header")
    _, header, body = raw.split("---\n", 2)
    return yaml.safe_load(header), body.strip("\n")


def load_document(path: Path) -> ChartDocument:
    header, body = _split_front_matter(path.read_text(encoding="utf-8"), path)
    expected_id = f"{path.parent.name}/{path.stem}"
    if header.get("doc_id") != expected_id:
        raise ValueError(f"{path}: doc_id {header.get('doc_id')!r} does not match path {expected_id!r}")
    return ChartDocument(patient_id=path.parent.name, text=body, **header)


def load_chart(patient_id: str, charts_dir: Path = DATA / "charts") -> Chart:
    folder = charts_dir / patient_id
    docs = [load_document(p) for p in sorted(folder.glob("*.md"))]
    if not docs:
        raise FileNotFoundError(f"no chart documents in {folder}")
    docs.sort(key=lambda d: (d.date, d.doc_id))
    return Chart(patient_id=patient_id, documents=docs)


def load_request(request_id: str, cases_dir: Path = DATA / "cases") -> PARequest:
    return PARequest(**yaml.safe_load((cases_dir / request_id / "request.yaml").read_text()))


def load_gold(request_id: str, cases_dir: Path = DATA / "cases") -> CaseGold:
    return CaseGold(**yaml.safe_load((cases_dir / request_id / "gold.yaml").read_text()))


def policy_dir(policy_id: str, policies_dir: Path = DATA / "policies") -> Path:
    return policies_dir / policy_id


def load_policy_prose(policy_id: str, policies_dir: Path = DATA / "policies") -> str:
    return (policy_dir(policy_id, policies_dir) / "policy.md").read_text(encoding="utf-8")


def load_gold_checklist(policy_id: str, policies_dir: Path = DATA / "policies") -> PolicyChecklist:
    """Evaluation only. The agent builds its own checklist from the prose."""
    raw = (policy_dir(policy_id, policies_dir) / "gold_checklist.yaml").read_text()
    return PolicyChecklist(**yaml.safe_load(raw))


def list_cases(cases_dir: Path = DATA / "cases") -> list[str]:
    return sorted(p.name for p in cases_dir.iterdir() if (p / "request.yaml").exists())


# --------------------------------------------------------------------------
# Step 1: request validation (M1)
# --------------------------------------------------------------------------

class IntakeError(ValueError):
    """The request cannot be processed. Nothing downstream runs."""


_VERSION_RE = re.compile(r"\|\s*Version\s*\|\s*([\w.-]+)\s*\|")


def policy_prose_version(prose: str) -> str | None:
    m = _VERSION_RE.search(prose)
    return m.group(1) if m else None


def intake(req: PARequest, chart: Chart, policy_id: str, expected_version: str, prose: str,
           decision_clock: dict[str, str]) -> IntakeResult:
    """Validate that request, chart and policy belong together. Raises IntakeError."""

    notes: list[str] = []
    if chart.patient_id != req.patient_id:
        raise IntakeError(f"chart {chart.patient_id} does not match request patient {req.patient_id}")
    wrong = [d.doc_id for d in chart.documents if d.patient_id != req.patient_id]
    if wrong:
        raise IntakeError(f"documents from another patient in chart: {wrong}")
    future = [d.doc_id for d in chart.documents if d.date > req.request_date]
    if future:
        raise IntakeError(f"documents dated after the request date: {future}")
    if req.requested_start < req.request_date:
        notes.append("Requested start date is before the request date.")
    found = policy_prose_version(prose)
    if found != expected_version:
        # Stale-policy guard (spec 9.4): the lookup table and the policy on file must agree.
        raise IntakeError(f"policy {policy_id} on file is version {found}; lookup expects {expected_version}")
    return IntakeResult(
        request=req, policy_id=policy_id, policy_version=found, n_documents=len(chart.documents),
        decision_clock=decision_clock[req.urgency.value], notes=notes,
    )
