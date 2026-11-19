"""Step 2: benefit routing. Code plus a lookup table, no model.

Answers two questions before any model call: does this payer require PA for
this drug at all, and which benefit (medical or pharmacy) pays for each phase
of therapy. The channel the office typed on the request is checked, not trusted.
"""

from __future__ import annotations

from functools import cache
from pathlib import Path

import yaml

from agent.schemas import BenefitChannel, PARequest, RoutingDecision

REF = Path(__file__).resolve().parent.parent / "data" / "reference" / "pa_lookup.yaml"


class RoutingError(LookupError):
    pass


@cache
def _table() -> tuple[dict, ...]:
    return tuple(yaml.safe_load(REF.read_text()))


def lookup(payer: str, drug: str, plan_type: str) -> dict:
    for row in _table():
        if row["payer"] == payer and row["drug"] == drug and plan_type in row["plan_types"]:
            return row
    raise RoutingError(f"no PA lookup entry for payer={payer} drug={drug} plan_type={plan_type}")


def route(req: PARequest) -> RoutingDecision:
    row = lookup(req.payer, req.drug, req.plan_type.value)
    channels = {k: BenefitChannel(v) for k, v in row["channels"].items()}
    notes: list[str] = []
    ok: bool | None = None
    if req.requested_channel is not None:
        # A request names one channel; the drug may need two (IV induction is
        # medical, SC maintenance is pharmacy). One channel for everything is wrong
        # whenever the phases split.
        ok = len(set(channels.values())) == 1 and req.requested_channel in channels.values()
        if not ok:
            split = ", ".join(f"{k} -> {v.value}" for k, v in channels.items())
            notes.append(
                f"Request lists the {req.requested_channel.value} benefit for the whole order, "
                f"but this payer splits the phases ({split}). Submit each phase on its own benefit."
            )
    if len(set(channels.values())) > 1:
        notes.append("Two submissions: " + "; ".join(
            f"{phase.replace('_', ' ')} via the {ch.value} benefit" for phase, ch in channels.items()))
    return RoutingDecision(pa_required=row["pa_required"], channels=channels,
                           requested_channel_ok=ok, notes=notes)
