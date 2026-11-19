"""Steps 10 and 11 in code: apply reviewer decisions, gate the sign-off, mock the submission.

Nothing here talks to a payer. "Submission" writes the payload each rail would
carry (a portal request for the medical benefit, an ePA request for the pharmacy
benefit) to disk, with the full audit trail beside it.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from agent.schemas import (
    BenefitChannel,
    PacketOutcome,
    PipelineResult,
    ReviewAction,
    ReviewDecision,
    SignOff,
    Status,
    packet_outcome,
    roll_up,
)


class SignOffBlocked(RuntimeError):
    pass


def final_statuses(res: PipelineResult, decisions: list[ReviewDecision]) -> dict[str, Status]:
    """Leaf statuses after human review. An edit can change a status; a reject makes it unresolved."""
    out = {a.criterion_id: a.status for a in res.assessments}
    for d in decisions:
        if d.action == ReviewAction.EDIT and d.new_status is not None:
            out[d.criterion_id] = d.new_status
        elif d.action == ReviewAction.REJECT:
            out[d.criterion_id] = Status.INSUFFICIENT_EVIDENCE
    return out


def required_role(res: PipelineResult) -> str:
    """D1: a nurse or PA specialist reviews every packet; a physician signs any letter and resolves
    any CONFLICTING or NOT_MET criterion."""
    if res.packet is not None or res.outcome == PacketOutcome.NEEDS_PHYSICIAN:
        return "physician"
    return "nurse_or_pa"


def blockers(res: PipelineResult, decisions: list[ReviewDecision], signoff: SignOff) -> list[str]:
    b = []
    latest = {d.criterion_id: d for d in decisions}
    undecided = [a.criterion_id for a in res.assessments if a.criterion_id not in latest]
    if undecided:
        b.append(f"no decision yet for {', '.join(undecided)}")
    if required_role(res) == "physician" and signoff.reviewer_role != "physician":
        b.append("a physician must sign off (letter of medical necessity, or a NOT_MET/CONFLICTING criterion)")
    if signoff.decision == "submit":
        statuses = final_statuses(res, list(latest.values()))
        rolled = roll_up(res.checklist, statuses)
        if packet_outcome([rolled[c.id] for c in res.checklist.criteria]) != PacketOutcome.READY_FOR_REVIEW:
            b.append("not every criterion is MET after review; nothing can be submitted")
        if res.packet is None:
            b.append("no drafted packet")
        if res.packet_code_issues:
            b.append("packet has citation problems found by code: " + "; ".join(res.packet_code_issues[:3]))
        if res.verification is None:
            b.append("packet was not verified")
        elif not res.verification.overall_pass and not (signoff.note and "override" in signoff.note.lower()):
            b.append("verifier flagged claims; fix them or record an override reason in the note")
    return b


def mock_submit(res: PipelineResult, decisions: list[ReviewDecision], signoff: SignOff, out_dir: Path) -> Path:
    b = blockers(res, decisions, signoff)
    if b:
        raise SignOffBlocked("; ".join(b))
    sub = out_dir / "submission"
    sub.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    base = {
        "request_id": res.request.request_id, "payer": res.request.payer, "policy_id": res.policy_id,
        "policy_version": res.policy_version, "product": res.request.product, "urgency": res.request.urgency.value,
        "signed_by": signoff.reviewer, "signed_at": signoff.timestamp.isoformat(), "mock": True,
        "form_fields": [f.model_dump() for f in res.packet.form_fields] if res.packet else [],
    }
    written = []
    rails = {BenefitChannel.MEDICAL: "medical-portal-request.json", BenefitChannel.PHARMACY: "pharmacy-epa-request.json"}
    for phase, ch in res.routing.channels.items():
        payload = {**base, "phase": phase, "benefit": ch.value,
                   "rail": "payer provider portal (X12 278-style)" if ch == BenefitChannel.MEDICAL
                   else "electronic prior authorization (NCPDP SCRIPT ePA-style)"}
        path = sub / f"{phase}-{rails[ch]}"
        path.write_text(json.dumps(payload, indent=2))
        written.append(path.name)
    if res.packet:
        letter = "\n".join(s.text for s in res.packet.letter)
        (sub / "letter_of_medical_necessity.md").write_text(letter + f"\n\nSigned: {signoff.reviewer} ({now})\n")
    (sub / "receipt.json").write_text(json.dumps({"submitted_at": now, "files": written, "mock": True}, indent=2))
    return sub


def save_review(out_dir: Path, decisions: list[ReviewDecision], signoff: SignOff | None = None) -> None:
    with (out_dir / "review.jsonl").open("a") as f:
        for d in decisions:
            f.write(json.dumps({"kind": "decision", **d.model_dump(mode="json")}) + "\n")
        if signoff:
            f.write(json.dumps({"kind": "signoff", **signoff.model_dump(mode="json")}) + "\n")
