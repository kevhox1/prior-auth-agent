"""Case blueprints and a seeded sampler.

A blueprint is the full truth of a synthetic case: who the patient is, what the
request says, the state of every criterion, and how the chart is styled. Gold
labels are computed from it in code (synth/label.py). Documents are rendered
from it (synth/render.py). No model decides anything here.
"""

from __future__ import annotations

import random
from datetime import date

from pydantic import BaseModel, ConfigDict, Field

REQUEST_DATE = date(2026, 11, 18)

# Criterion state menu for the Northfield ustekinumab policy.
# Each criterion: state -> (weight when sampled as a "problem", is_problem)
STATES: dict[str, dict[str, bool]] = {
    "C1": {"met_clean": False, "not_met_mild": True},
    "C2": {"met_scope": False, "met_fcp": False, "met_buried": False, "met_borderline": False,
           "crp_only": True, "stale_scope": True},
    "C5a": {"met_clean": False, "met_buried": False, "missing": True},
    "C5b": {"met_clean": False, "met_buried": False, "contraindication": False,
            "conflicting": True, "not_met_naive": True, "insurance_stop": True},
    "C6": {"met_clean": False, "met_borderline": False, "positive_with_plan": False,
           "stale": True, "indeterminate": True, "missing": True, "ordered_not_resulted": True},
    "C7": {"met_clean": False, "core_positive_with_plan": False,
           "partial": True, "decoy": True, "missing": True},
    "C8": {"met_clean": False, "switch_with_stop": False, "not_met_combo": True},
    "C9": {"met_clean": False, "met_borderline": False, "wrong_tier": True, "stale_weight": True},
    "C10": {"met_clean": False, "not_met_reference": True},
}
# C3 (prescriber) and C4 (age) are always met in v1 synthetic cases: every
# request comes from a Harbor gastroenterologist for an adult.
ALWAYS_MET = ("C3", "C4")

# Relative chance a criterion is chosen when a case needs a problem.
PROBLEM_WEIGHTS = {"C1": 1, "C2": 4, "C5a": 2, "C5b": 5, "C6": 6, "C7": 5, "C8": 2, "C9": 3, "C10": 2}
# Chance a non-problem criterion uses a harder-but-still-MET variant.
HARD_MET_RATE = 0.25


class StyleKnobs(BaseModel):
    model_config = ConfigDict(extra="forbid")
    note_template: int = Field(ge=0, le=2, description="0 SOAP, 1 HPI/Impression, 2 problem-oriented")
    provider: int = Field(ge=0, le=2)
    medhx_format: str = Field(pattern="^(table|narrative|scattered)$")
    lab_vendor: int = Field(ge=0, le=2)
    outside_quality: str = Field(pattern="^(clean|fax|ocr)$")
    outside_practice: int = Field(ge=0, le=3)
    distractors: int = Field(ge=0, le=2)
    date_style: str = Field(pattern="^(iso|us)$")
    copy_forward: bool
    requested_channel_wrong: bool
    expedited: bool
    injection: bool


class Blueprint(BaseModel):
    model_config = ConfigDict(extra="forbid")
    seed: int
    request_id: str
    patient_id: str
    request_date: date = REQUEST_DATE
    payer: str = Field(default="northfield", pattern="^(northfield|calder)$")
    first_name: str
    last_name: str
    sex: str
    dob: date
    disease: str = Field(pattern="^(cd|uc)$")
    weight_kg: float
    states: dict[str, str]
    knobs: StyleKnobs


_FIRST = {
    "F": ["Ana", "Priya", "Grace", "Lena", "Marisol", "Hannah", "Yuki", "Fatima", "Claire", "Noor",
          "Beatriz", "Ingrid", "Tamsin", "Dana", "Rosa", "Mei", "Olivia", "Sana", "Teresa", "Leah"],
    "M": ["Omar", "Lucas", "Dev", "Samuel", "Tomas", "Kwame", "Eli", "Rafael", "Henry", "Arjun",
          "Felix", "Jonah", "Mateo", "Victor", "Kenji", "Isaac", "Malik", "Peter", "Andre", "Leo"],
}
_LAST = ["Abara", "Bellweather", "Castellano", "Dunmore", "Ekwueme", "Fairbanks", "Galloway",
         "Halvorsen", "Ibarra", "Jansen", "Kowalczyk", "Lindahl", "Marchetti", "Nakashima",
         "Oyelaran", "Petrakis", "Quintero", "Rasmussen", "Sorensen", "Thibodeaux", "Umarov",
         "Vasquez", "Whitcombe", "Yilmaz", "Zielinski", "Ashworth", "Brennagh", "Delacroix"]


def _pick_weighted(rng: random.Random, options: dict[str, int]) -> str:
    keys = list(options)
    return rng.choices(keys, weights=[options[k] for k in keys])[0]


def sample_blueprint(seed: int, request_num: int) -> Blueprint:
    rng = random.Random(seed)
    sex = rng.choice("FM")
    age = rng.randint(19, 74)
    dob = date(REQUEST_DATE.year - age, rng.randint(1, 12), rng.randint(1, 28))
    disease = rng.choice(["cd", "cd", "uc"])

    # How many problems: about 1 in 4 clean (D6), the rest 1 or 2.
    n_problems = rng.choices([0, 1, 2], weights=[25, 45, 30])[0]
    problem_cids: set[str] = set()
    weights = dict(PROBLEM_WEIGHTS)
    for _ in range(n_problems):
        cid = _pick_weighted(rng, weights)
        problem_cids.add(cid)
        weights.pop(cid)

    states: dict[str, str] = {}
    for cid, menu in STATES.items():
        problems = [s for s, is_p in menu.items() if is_p]
        mets = [s for s, is_p in menu.items() if not is_p]
        if cid in problem_cids:
            states[cid] = rng.choice(problems)
        elif len(mets) > 1 and rng.random() < HARD_MET_RATE:
            states[cid] = rng.choice(mets[1:])
        else:
            states[cid] = mets[0]
    for cid in ALWAYS_MET:
        states[cid] = "met_clean"

    # Weight follows the dosing state.
    if states["C9"] == "met_borderline":
        weight = rng.choice([55.0, 85.0])
    else:
        weight = round(rng.uniform(47, 112), 1)
        if weight in (55.0, 85.0):
            weight += 0.4

    knobs = StyleKnobs(
        note_template=rng.randint(0, 2),
        provider=rng.randint(0, 2),
        medhx_format=rng.choice(["table", "narrative", "scattered"]),
        lab_vendor=rng.randint(0, 2),
        outside_quality=rng.choice(["clean", "fax", "ocr"]),
        outside_practice=rng.randint(0, 3),
        distractors=rng.choices([0, 1, 2], weights=[40, 40, 20])[0],
        date_style=rng.choice(["iso", "us"]),
        copy_forward=rng.random() < 0.25,
        requested_channel_wrong=rng.random() < 0.08,
        expedited=rng.random() < 0.06,
        injection=rng.random() < 0.04,
    )
    return Blueprint(
        seed=seed,
        request_id=f"PA-{request_num:04d}",
        patient_id=f"PT-{request_num:04d}",
        first_name=rng.choice(_FIRST[sex]),
        last_name=rng.choice(_LAST),
        sex=sex,
        dob=dob,
        disease=disease,
        weight_kg=weight,
        states=states,
        knobs=knobs,
    )
