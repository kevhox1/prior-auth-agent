# Agent spec (as built)

This describes the agent as it exists in the repo. The original build brief is `SPEC.md`, and every place the build departed from it is logged in `DECISIONS.md`. Terms are defined in `GLOSSARY.md`.

## 1. Job

Given a prior authorization request, the patient's chart and the payer's coverage policy, the agent produces one of three results for a human reviewer:
- **READY_FOR_REVIEW:** every criterion is proven with a quote. The agent drafts the PA form and the letter of medical necessity, every claim cited, and independently checks them.
- **GAPS_TO_CLOSE:** something is missing. Each missing item comes with who can most likely supply it, a drafted message, and what the policy would accept.
- **NEEDS_PHYSICIAN:** a criterion fails or the chart contradicts itself. A doctor decides.

Nothing leaves without human sign-off. Submission is mocked.

## 2. Boundaries

| Rule | Where it is enforced |
|---|---|
| Never submit to a payer, change the order, or suggest a different drug (D2) | No such tool or output field exists. Submission is a separate function gated by `agent/submit.py` |
| Never mark MET without a quote (D2) | Schema validator on every assessment (`agent/schemas.py`) |
| Missing evidence is INSUFFICIENT_EVIDENCE with the exact item named, never inferred (D4) | Schema validator, plus `assess@v3` rules |
| Code can take a MET away, never grant one (B22) | `agent/checks.py`, with a test for every status |
| Chart text is data, never instructions | Chart is wrapped and labeled as data. The model flags injected text, and a regex scan backs it up (B23) |
| Drafted packets use only verified facts (B36) | The drafter never sees the raw chart, only quotes that passed step 6 |
| A physician signs any letter, and any NOT_MET or CONFLICTING case (D1) | `required_role()` and `blockers()` in `agent/submit.py`. The UI cannot bypass them |
| Release gate: zero false MET on the eval set (D3) | `evals/metrics.py`, reported first in every eval report |

## 3. Inputs

- **Request** (`data/cases/<id>/request.yaml`): drug, exact product, dose, ICD-10 code, payer, plan type, ordering provider, urgency (with the reason if expedited), request date, requested start, and optionally the benefit channel staff entered.
- **Chart** (`data/charts/<patient>/*.md`): one file per document. The header gives the id, type, date and author. The document types are specialty-neutral: demographics, problem list, medication history, progress note, procedure report, labs, outside records, other.
- **Policy** (`data/policies/<policy_id>/policy.md`): prose, the way a payer publishes it. A gold checklist sits beside it for evaluation only.
- **Reference tables** (`data/reference/`), maintained by staff and versioned with the policy:
  - `pa_lookup.yaml`: whether PA is required, which policy and version governs, benefit channel per phase of therapy, decision clock.
  - `policy_rules.yaml`: numbers code enforces regardless of extraction: minimum age, lookback months per section, weight recency.
  - `label_dosing.yaml`: labeled dose tables for drugs that have a code dose check (ustekinumab only today).

## 4. Pipeline

| Step | What it does | Done by | Output |
|---|---|---|---|
| 1 Intake | Validates the request, the chart's patient and dates, and that the policy version matches the lookup table. Attaches the decision clock | Code | `IntakeResult`, or a stop |
| 2 Routing | Is PA required? Which benefit pays for each phase? Is the channel staff entered right? | Code plus lookup table | `RoutingDecision` |
| 3 Policy extraction | Prose policy to a structured checklist, with ALL/ANY logic and sub-criteria. Once per policy version, approved by a person (B39) | Model (`policy_extract@v1`) plus sanity checks | `PolicyChecklist` |
| 4 Retrieval | Finds verbatim passages for every criterion in one call. Non-verbatim passages are dropped. Injected instructions are flagged | Model (`retrieve@v1`) plus code filter | `RetrievalResult` per criterion |
| 5 Assessment | One status per leaf criterion, with reasoning, quotes, confidence and missing items. Sees the passages and a document inventory, not the full chart | Model (`assess@v3`; v2 for the archived M2-M4 runs) | `CriterionAssessment` drafts |
| 6 Code checks | Quote is verbatim, date and patient match, lookback window, no stale result copied into a recent note, age from DOB, dose against the label tier and weight recency. Any failure downgrades MET to NOT_MET (proven failure) or INSUFFICIENT_EVIDENCE (missing proof) | Code | Final leaf statuses. Parents roll up in code: ALL is N > C > I; ANY is MET if any child is MET |
| 7 Gap plan | For every non-MET: missing item, who can supply it, a drafted message, and what would satisfy the policy, with the date computed (B35). NOT_MET and CONFLICTING always go to the ordering provider | Model (`gaps@v2`) plus code defaults | `GapItem` list |
| 8 Draft | PA form fields (derived from the checklist) and the letter, one cited sentence per fact. READY cases only. Citations are re-checked by code | Model (`draft@v2`) plus code | `PacketDraft` |
| 9 Verify | A separate call sees only the request, the packet and the chart, and checks each claim against its source. A missing check counts as unsupported | Model (`verify@v1`) plus code | `VerificationResult` |
| 10 Review | Per-criterion approve, edit (with a reason code) or reject. Sign-off by the required role | Human, in the Streamlit UI | `review.jsonl`, `SignOff` |
| 11 Submit | One file per benefit, the letter, and a receipt | Code, mocked | `submission/` |

Each step uses one model call per case, not one per criterion (B19). All model output is structured (a JSON schema from pydantic). Nothing is parsed from free text.

## 5. Statuses and outcome

- **MET:** proven, with at least one verbatim quote.
- **NOT_MET:** the chart affirmatively shows the requirement fails. Examples: an LDL-C below the threshold, a concurrent biologic that will continue, or stale evidence of the right kind when it is the only evidence (B32).
- **INSUFFICIENT_EVIDENCE:** not shown either way. This includes an indeterminate or unresulted test, or evidence of the wrong kind.
- **CONFLICTING:** the chart makes incompatible statements. Silence on a point is not a conflict (B27).

Outcome: any NOT_MET or CONFLICTING at the top level gives NEEDS_PHYSICIAN. Otherwise any INSUFFICIENT_EVIDENCE gives GAPS_TO_CLOSE. Otherwise the outcome is READY_FOR_REVIEW.

## 6. Prompts, models and audit

- **Prompts.** Every prompt is a versioned file in `prompts/` (`name@vN.md`) with a header the loader checks. The version is written to the audit log on every call. Old versions stay in the repo so earlier runs can be reproduced.
- **Model calls.** All calls go through `agent/llm.py`. Backends:
  - `claude_code` (the default): `claude -p` with a JSON schema, no tools, an empty working directory.
  - `anthropic_api`.
  - `replay`, for tests.

  Choose with `PA_AGENT_BACKEND` and `PA_AGENT_MODEL` (default `claude-opus-5-5`). Responses are cached by a hash of the model, prompt and input.
- **Audit.** Each case writes `audit.jsonl`: every step, with its inputs summary, output, prompt version, model, tokens, seconds and list-price cost.

## 7. Adding a policy, drug or payer

All of this is data, with no code (B28, B41):
1. Write `data/policies/<policy_id>/policy.md`, and a `gold_checklist.yaml` if you want it scored.
2. Add a row to `pa_lookup.yaml` (channels and decision clock) and to `policy_rules.yaml` (age, lookbacks).
3. Run extraction, review the checklist, and add cases.

What still needs code today:
- **A code dose check for a new drug.** The weight-tier check is specific to ustekinumab. Other drugs rely on the model alone for dosing.
- **A new kind of computed check**, for example a lab value against a numeric threshold. LDL-C against 70 mg/dL is judged by the model today, not by code.

## 8. Evaluation

- **Synthetic charts.** Code decides each case's gold labels from a blueprint, and models only write prose (B14). Payer twins share one chart (B29).
- **Gates:** zero false MET, 100% verbatim citations, 100% routing, and every injection flagged.
- **Quality:** packet outcome (exact, or different only through an acceptable alternate), per-criterion accuracy, recall per status, and over-escalation.
- **Disagreement review.** A QA agent reviews every disagreement and may blame the gold label (B31).
- **Seeded errors.** Planted errors in real packets test the verifier (B40).
- **Model comparison.** Gates first, then quality within 5 points, then cost (`COST_EFFECTIVENESS_SPEC.md`).

## 9. Known limits

- **Narrow test coverage.** One IBD drug (ustekinumab) across two payers, plus one cardiology drug as a reuse test. The brief's four IBD drugs were cut to keep the demo small (B42).
- **Synthetic data has its own blind spots.** In the archived batches the prescriber's specialty appears only in note metadata, and one generator sentence can contradict the recorded weight (B38). The generator is fixed (B43); batches 1 to 3 were left as they were so the archived runs stay reproducible.
- **The retrieval step is not built for long charts.** One call works for charts of 7 to 12 documents. Long real charts would need chunked retrieval.
- **No clinical validation.** The open questions for a clinician are listed in the README.
