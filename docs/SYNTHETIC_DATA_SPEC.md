# SPEC: Synthetic Case Pipeline (Data Agent → PA Agent → QA Agent)

Status: Generator built (template renderer + validator + optional model rewrite). Auditor and QA agent: next.
Scope note: this is an interview demo. Every model call runs through Claude Code (`claude -p`) on Kevin's login, not a paid API budget.
Extends: SPEC.md section 9.1 (test set), COST_EFFECTIVENESS_SPEC.md
Built in: M2

## 1. Why

The 30 hand-built cases are too few and too similar. They share one practice, one doctor, one nurse and one lab layout, and nothing sits near a cutoff. They catch obvious failures but cannot show *what kinds* of chart break the agent. This pipeline builds hundreds of varied cases. It runs the PA agent on them and has a QA agent grade the results and write a report.

## 2. The core rule: an LLM never decides the gold label

If a model writes the chart *and* decides the right answer, its mistakes become the answer key, and the eval cannot catch them. Here:

1. **Code** samples a structured case *blueprint*: the facts, dates and values, and the state of each criterion.
2. **Code** computes the gold label from the blueprint with a fixed rule table.
3. **The data agent** writes the documents. By default it is a **code template renderer** (`synth/render.py`): free, instant, reproducible from a seed, and it cannot leak facts. An optional **model rewrite pass** (`--rewrite --model <id>`, through Claude Code) makes the prose read more naturally. It must keep every planted fact verbatim and must not state forbidden facts; any rewritten document that fails validation keeps its template text.
4. **Code and an independent auditor** check that the documents say what the blueprint says. Any case where they don't is quarantined, never auto-fixed.

## 3. Tiers of data

| Tier | Size | Built by | Used for | Gate role |
|---|---|---|---|---|
| Tier 1: hand set | 30 | Drafted by the pipeline, then read in full and corrected by Kevin (ideally a clinician too) | Release gates (D3), dev and holdout splits | **The release gate** |
| Tier 2: synthetic | 300+ | Pipeline, with a 5% human spot check | Breadth, regression, finding failure patterns, the human grading pool | Gate metrics reported. A false MET here first goes to adjudication (it may be a label error), then counts |

Drafting the remaining 27 Tier 1 cases with the pipeline and reviewing each one by hand is faster than writing them from scratch. It also tests the pipeline itself.

## 4. Pipeline

```text
blueprint sampler (code) ──> gold labeler (code)
        │
        ▼
data agent (model) ──> validator (code) ──> auditor (model, blind) ──> human spot check
        │                                                     │
        │                                      quarantine <───┘ (mismatch)
        ▼
accepted case  ──>  PA agent (the product)  ──>  scorer (code)  ──>  QA agent (model)  ──>  QA_REPORT.md
```

### 4.1 Blueprint sampler (code, seeded, reproducible)

A blueprint is a JSON document with these parts:

- **Request**: patient, drug, product, payer and policy, urgency, plan type, requested channel.
- **Patient facts**: date of birth, sex, a weight trajectory, disease type and location, and dates of the severity scores.
- **Criterion states**: one per leaf criterion, drawn from the menu below.
- **Planted facts**: one entry per fact the chart must contain:
  - `fact_id` and `criterion_id`;
  - `doc_hint` (which document type it belongs in);
  - `anchor_text`, the exact string that must appear;
  - `date`.
- **Forbidden facts**: patterns that must not appear. Example: any anti-HBc *result* in a case where that result is missing.
- **Style knobs**: listed below.

**Criterion state menu** (each state maps to a gold status in code):

| State | Example | Gold status | Alternates |
|---|---|---|---|
| `met_clean` | Negative QuantiFERON 2 months ago in the lab table | MET | none |
| `met_buried` | Only evidence is in a faxed outside record or the middle of a narrative note | MET | none |
| `met_borderline` | TB test 11.8 months old; weight 85.0 kg exactly | MET | none |
| `missing` | No anti-HBc anywhere | INSUFFICIENT_EVIDENCE | none |
| `missing_with_decoy` | Vaccine record and anti-HBs only; test ordered but never drawn | INSUFFICIENT_EVIDENCE | none |
| `stale` | TB test 12.3 months old against a 12-month window | NOT_MET | INSUFFICIENT_EVIDENCE |
| `not_met` | Concurrent upadacitinib with no stop plan | NOT_MET | none |
| `conflicting` | Two records disagree on whether a drug was taken | CONFLICTING | NOT_MET |
| `indeterminate` | Indeterminate IGRA | INSUFFICIENT_EVIDENCE | NOT_MET |
| `positive_with_plan` | Positive IGRA, clear chest X-ray, latent TB treatment started | MET | none |

`stale` lists INSUFFICIENT as an alternate because "the screen is out of date" and "a current screen is missing" are both defensible readings. Both route away from MET. MET is never an alternate for a non-MET state; this is enforced by schema.

**Style knobs** (recorded on every case, so failures can be broken down by knob):

| Knob | Values |
|---|---|
| Practice template | 5 fictional practices, each with its own note structure, authors and abbreviations |
| Medication history format | Reconciled table / narrative only / scattered across notes |
| Lab vendor format | 3 layouts, including one with values in a separate column order |
| Outside record quality | Clean / fax header noise / OCR errors (character swaps, broken lines) |
| Document count | 5–15, including unrelated distractor visits |
| Copy-forward | None / a stale fact copied into later notes |
| Date formats | ISO / US / mixed |

**Case-type mix**: the sampler hits target proportions that follow D6. About 25% of cases have all criteria `met_*`; the rest have at least one non-clean state. Of the non-clean cases, 30% have two or more problems at once.

### 4.2 Gold labeler (code)

`synth/label.py` maps each criterion state to its gold status and alternates, using the table above. Parent criteria and the packet outcome come from `schemas.roll_up` and `schemas.outcome_for`, the same functions the agent's results go through. Routing gold comes from the reference lookup table. **No model is involved in this step.**

### 4.3 Data agent (model)

- **Input**: the blueprint and a style guide for the chosen practice template.
- **Output**: a structured list of documents, each with type, date, author, title and text, validated against `ChartDocument`.
- **Prompt rules** (`prompts/synth_generate@v1`):
  - Include every `anchor_text` verbatim, in a document of its `doc_hint` type.
  - Never state anything matching a forbidden fact.
  - Don't add test results or treatment history that bear on a criterion beyond what the blueprint plants. Clinically consistent filler is fine: symptoms, plans, unrelated problems.
  - Use only fictional names.
- **Generator diversity**: half the cases are written by `claude-opus-5-5` and half by `claude-sonnet-5-5`. This limits the risk that the PA agent finds text easy because the same model wrote it. Results are reported by generator; if the PA agent scores much better on one generator's cases, that is a red flag.

### 4.4 Validator (code)

A case is rejected if any of these checks fails:
- Every anchor appears verbatim (whitespace-normalized) in a document of the right type and date.
- No forbidden pattern matches. There is one lexicon per criterion; for example, `core antibody|anti-?HBc|HBcAb` followed by a result word.
- Name, date of birth and member ID are consistent across all documents.
- No real payer names. A blocklist covers the major US insurers and PBMs.
- Document dates fall within the blueprint's timeline, and nothing is dated after `request_date`.
- The output passes the schema.

Rejected cases are regenerated once with the validator's errors fed back. A case that fails twice is dropped and counted. The rejection rate is reported, because a high rate means the generator prompt needs work.

### 4.5 Auditor (model, blind)

A separate model call reads only the chart and the policy prose. It sees neither the blueprint nor the gold. It lists the evidence it finds for each criterion, using the same `Evidence` schema as retrieval. Code then compares that evidence with the blueprint:
- The auditor found a fact that the blueprint marks as missing or forbidden → **quarantine** (the generator leaked evidence).
- The auditor cannot find a planted anchor that the validator says is present → fine; this is a retrieval-difficulty signal, not a label problem.

Quarantined cases go to Kevin's adjudication queue. The quarantine rate is reported per batch.

### 4.6 Human spot check

For each batch, Kevin reads a random 5% of accepted cases plus everything in quarantine. For each one he records: realism (1–5), whether the gold label is right (yes/no), and an optional note. **A batch is accepted only if gold-label agreement on the spot check is 95% or higher.** Otherwise, fix the generator or the label rules and regenerate. Later, the clinician questions in the README feed back into the realism rubric.

### 4.7 PA agent run

Accepted cases are saved in exactly the same layout as hand cases: `data/synth/<batch_id>/charts/…` and `data/synth/<batch_id>/cases/…`, plus `blueprint.json`. The harness from COST_EFFECTIVENESS_SPEC.md runs them unchanged, as split `synth:<batch_id>`.

### 4.8 QA agent (model) and report

The scorer is code, so statuses are never graded by a model. The QA agent works on the scorer's output:

1. **Failure review.** For each wrong criterion, the QA agent reads the chart, the blueprint, the gold label and the agent's output. It either confirms the failure category the code proposed (COST spec 6.5) or marks the case **"gold may be wrong"** with a reason. It cannot change gold labels or scores; "gold may be wrong" cases go to Kevin's adjudication queue.
2. **Pattern finding.** Code computes failure rates broken down by style knob, criterion state and generator. The QA agent turns the biggest effects into plain-language clusters with examples. For instance: "C6 retrieval misses rise from 2% to 19% when labs use vendor layout 3; the TB result is in a column the agent skips."
3. **Report** (`runs/<run_id>/QA_REPORT.md`):
   - gates (pass or fail, with the cases that failed them);
   - metrics overall, by case type, by criterion, and by style knob;
   - the top 5 failure clusters, with 2 example cases each;
   - the suspected gold errors awaiting adjudication;
   - the recommended next 3 fixes, each tied to a cluster and to an expected metric change;
   - pipeline health: rejection, quarantine and spot-check agreement rates;
   - cost of the run by stage.

The QA agent's model and prompt are pinned per experiment series, like the judge in COST spec 4.3. Its "gold may be wrong" calls are checked against Kevin's adjudications; if it is wrong more than 20% of the time, its flags are treated as noise until the prompt is fixed.

## 5. Repo additions

```text
synth/
  blueprint.py    # pydantic Blueprint, CriterionState, PlantedFact, StyleKnobs
  sampler.py      # seeded sampler with case-type targets
  label.py        # state -> gold (code only)
  generate.py     # data agent call
  validate.py     # code checks + lexicons
  audit.py        # blind auditor call
  build.py        # python -m synth.build --n 100 --seed 7 --budget-usd 60
qa/
  analyze.py      # knob/state/generator breakdowns (code)
  qa_agent.py     # failure review + clusters + report
prompts/
  synth_generate@v1.md  synth_audit@v1.md  qa_review@v1.md  qa_report@v1.md
data/synth/<batch_id>/  # accepted cases, same layout as data/cases + data/charts
```

## 6. Cost and how to run it

No API budget. Generation and every model step run through Claude Code:

```bash
# Free: template rendering only (what is committed in data/synth/batch-001)
python -m synth.build --batch 1 --n 200 --seed 1

# Optional realism pass on the first 10 cases, using your Claude Code login
python -m synth.build --batch 2 --n 50 --seed 2 --rewrite --model claude-sonnet-5-5 --limit-rewrite 10
```

- Each model call is `claude -p --model <id> --json-schema <schema> --tools ""`, run from an empty temp directory with no settings, MCP servers or project files loaded. The model sees only the prompt.
- Claude Code reports a list-price cost and token counts for every call. These go into `usage.jsonl`, so the cost-vs-effectiveness numbers still work even though nothing is billed per token.
- Every response is cached under `runs/cache/` by request hash. Re-running or re-scoring is free.
- The practical limit is subscription rate limits, not money. For the demo, run the PA agent on the 3 hand cases plus a 10–20 case synthetic sample, not all 200.

## 7. What this does not solve

- **Synthetic is not real.** Every case is only as realistic as the blueprint menu and the style guides. Real charts will have failure modes nobody thought to plant. Tier 1 stays the release gate, and the production plan keeps a review-edit feedback loop.
- **Shared blind spots.** If every model in the pipeline misreads something the same way, the auditor and the QA agent will miss it too. The human spot check and the clinician questions are the only defense.
- **Overfitting to the generator.** Prompts tuned on synthetic cases may learn the generator's writing style. Watch for a widening gap between Tier 2 and Tier 1 scores.

## 8. Milestone changes

| Milestone | Before | Now |
|---|---|---|
| M1 | Steps 1–7 on 3 cases | Unchanged |
| M2 | Remaining policies, 30 cases, harness | Plus: sampler, labeler and validator (code, testable with no API calls); data agent, auditor and QA agent; one 100-case pilot batch; Tier 1 cases drafted by the pipeline and hand-reviewed |
| M2 STOP | Kevin picks failures to fix | Kevin also reviews the spot-check sample, the adjudication queue and the first QA_REPORT |
| M3 | Steps 8–11 and UI | Plus: blind grading mode for the human experiment (COST spec section 12) |
| After M3 | none | Scale to 300+ synthetic cases; human grading experiment on finalists |

This adds about 1–1.5 days to the original 2-day timebox.

## 9. Open questions for Kevin

1. ~~Budget~~ Resolved: no API budget; all model calls run through Claude Code.
2. **Spot-check time.** About 15 cases per 300-case batch, plus quarantined cases: roughly 1–2 hours of reading per batch. Is that workable?
3. **A clinician.** Is there anyone who could do even a 1-hour realism read of 10 cases? It would be the strongest single check on Tier 1.
