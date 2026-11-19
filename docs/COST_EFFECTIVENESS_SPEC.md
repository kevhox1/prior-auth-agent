# SPEC: Cost vs Effectiveness Evaluation

Status: Draft for Kevin's review
Scope note: interview demo. Runs go through Claude Code (`agent/llm.py`, backend `claude_code`), so dollar figures are list-price equivalents that Claude Code reports, not money spent. The method is the same as for a paid API.
Extends: SPEC.md section 9 (Evaluation)
Built in: M1 (usage logging), M2 (harness, compare tool, first runs)

## 1. The question this answers

For each pipeline step, which model, effort level, and prompt version gives a packet we can trust, for the least total cost?

"Total cost" includes more than API spend. A prior authorization takes about 20 minutes of staff and physician time today (the AMA's 2025 survey: about 13 hours a week for about 40 requests). At a loaded nurse cost of about $40 an hour, that is roughly $13 of labor per request. The model will cost between a few cents and about $2 per case. **Reviewer minutes and errors dominate the economics, not tokens.** A cheaper model that adds one wrong criterion per case costs more than it saves. The harness has to measure both sides.

## 2. Terms

- **Config**: one complete pipeline setup. For each model step it sets the model, effort level, and prompt version. Stored as a YAML file and frozen into every run.
- **Run**: one config executed over one case split, with k repeats.
- **Repeat**: running the same case again with the same config. Model output varies from run to run, so one pass is not enough.
- **Gate**: a pass/fail requirement. A config that fails any gate cannot ship, however cheap it is.
- **Flip**: a case-criterion pair whose result changed between two runs, either fixed (wrong to right) or regressed (right to wrong).

## 3. Decision rule (in order)

1. **Gates.** All must hold on every repeat:

| Gate | Threshold | Source |
|---|---|---|
| False MET | 0 across all cases and all repeats. One false MET in any repeat fails the config | D3 |
| Citation validity | 100% of quotes found verbatim in the cited document | SPEC 9.2 |
| Routing accuracy | 100% | SPEC 9.2 |
| Injection handling | Injected instruction not followed in any repeat, and flagged | SPEC 5.8 |
| Schema failure rate | Under 2% of model calls after one retry | This spec |

2. **Patient guardrails.** These must not be worse than the manual baseline (section 11). In offline evals, this is the modeled patient delay per case. In a pilot, it is measured time to therapy, patient contacts, and patient-reported experience. Patient delay is never converted to dollars, so savings cannot offset it.
3. **Human preference.** When two configs both pass, blinded grading by the reviewers decides between them (section 12). That outranks NVC differences smaller than the noise band.
4. **Net value per case (NVC).** Section 5 defines it. Among configs that pass everything above, prefer higher NVC.
5. **Tie-break.** If two configs are within the noise band (section 7), pick the cheaper one. If cost is also within noise, pick the one with fewer distinct models: fewer moving parts and better cache reuse.

The quality score and dollars per case are always reported next to NVC. NVC rests on assumptions; the two raw numbers do not.

## 4. Metrics

### 4.1 Effectiveness, by step

Measuring each step separately shows where quality is lost. Otherwise a bad end-to-end number says nothing about where to look.

| Step | Metric | How it is measured |
|---|---|---|
| 3 Policy extraction | Criterion recall and precision vs gold; `logic` field accuracy; lookback-months accuracy; channel-table accuracy | Align extracted criteria to gold by `policy_ref` (see section 10 open question), then compare fields in code |
| 4 Retrieval | Gold-evidence recall: share of gold quotes covered by at least one candidate passage | Code, using whitespace-normalized overlap |
| 4 Retrieval | Documents searched = all documents | Code |
| 5 Assessment | Criterion status accuracy; confusion matrix; INSUFFICIENT recall; CONFLICTING recall | Code vs gold |
| 5 Assessment | Calibration: accuracy within each confidence bucket (0.5–0.7, 0.7–0.9, 0.9+) | Code. Decides whether confidence can steer reviewer attention |
| 6 Checks | Downgrade rate: how often code overruled the model's status | Code. A high rate means the prompt is losing to the rules |
| 7 Gap plan | Missing-item match against gold `missing_item` | Judge model (4.3) |
| 8 Draft | Uncited factual sentences (should be 0, enforced by schema); citation validity | Code |
| 9 Verification | Catch rate on the 5 seeded errors; false-alarm rate on clean packets | Code vs seeded-error manifest |
| End to end | Packet outcome accuracy | Code vs gold |

### 4.2 Cost and speed

These are logged on every model call to `usage.jsonl`:
- step;
- model and effort level;
- tokens: input, cached input read, cache write, and output (thinking included);
- latency in seconds;
- dollars, computed from a price table in `evals/prices.yaml`. Prices come from the Anthropic docs, are dated, and are never hard-coded in Python.

Reported per case and per step: mean dollars, p50 and p95 latency, and the cache hit ratio.

### 4.3 Judge model (used only where code cannot grade)

Two outputs are free text: step 7's missing items and the clarity of the letter. These are graded by a judge model with a fixed rubric and structured output: `match: bool`, `reason: str`.
- The judge model and prompt are pinned and do not change during an experiment series. Changing them resets the leaderboard.
- **The judge is calibrated before anyone trusts it.** Kevin hand-labels 30 judge decisions, and we report agreement. If agreement is under 90%, fix the rubric before using the scores.
- The judge never grades criterion statuses. Code does that against gold.

## 5. Net value per case (NVC)

```
NVC = (manual_minutes - reviewer_minutes) * staff_rate_per_min
      - model_cost_usd
      - sum(error_penalties)
```

All parameters live in `evals/value_model.yaml`. They are assumptions for clinicians to check (README open questions) and are editable without code changes. Starting values:

| Parameter | Default | Basis |
|---|---|---|
| `manual_minutes` | 20 | AMA 2025: about 13 hours a week across about 40 requests |
| `staff_rate_per_min` | $0.67 ($40/hr loaded RN or PA specialist) | Assumption |
| `physician_rate_per_min` | $2.50 ($150/hr) | Assumption |
| Reviewer base time, READY packet | 5 min | Assumption: read checklist, spot-check quotes, approve |
| Reviewer base time, GAPS packet | 3 min, plus the time to chase the gap | Assumption |
| Per wrong criterion the reviewer must fix | +4 min staff | Assumption |
| Unneeded physician escalation (said NEEDS_PHYSICIAN, gold says otherwise) | +5 min physician | Assumption |
| Over-flag (said INSUFFICIENT, gold says MET) | +6 min staff chasing an item that already exists | Assumption |
| Missed conflict (said MET, gold says CONFLICTING) | Counts as a false MET, so a gate failure | D3 |
| False MET | Gate failure; no dollar value is assigned | D3 |

False METs get no dollar penalty on purpose. Pricing them would invite a trade ("a false MET is worth $X of savings"). D3 says that trade is not ours to make.

**Report NVC with a sensitivity band**: rerun the formula with every assumption at half and at double its value. If the ranking of two configs flips inside that band, the assumptions decide the choice, not the data. Say so in the report.

## 6. Harness

### 6.1 Commands

```bash
# Run one config over a split. Prints an estimated cost and asks before spending.
python -m evals.run --config evals/configs/baseline.yaml --split dev --repeats 3 --budget-usd 25

# Re-score an old run after a metric change, at zero cost (replays cached model responses).
python -m evals.run --replay runs/2026-11-20T1030_baseline

# Compare two runs.
python -m evals.compare runs/<run_a> runs/<run_b>
```

### 6.2 Config file

```yaml
name: baseline-opus
notes: "All steps on the default model. Reference point for every later run."
steps:
  policy_extract: {model: claude-opus-5-5, effort: high,   prompt: policy_extract@v1}
  retrieve:       {model: claude-opus-5-5, effort: medium, prompt: retrieve@v1}
  assess:         {model: claude-opus-5-5, effort: high,   prompt: assess@v1}
  gaps:           {model: claude-opus-5-5, effort: medium, prompt: gaps@v1}
  draft:          {model: claude-opus-5-5, effort: medium, prompt: draft@v1}
  verify:         {model: claude-opus-5-5, effort: high,   prompt: verify@v1}
judge:            {model: claude-opus-5-5, effort: high,   prompt: judge@v1}
```

### 6.3 Run output (`runs/<timestamp>_<config name>/`)

| File | Contents |
|---|---|
| `config.yaml` | Frozen config, plus git commit, prompt file hashes, and the price table version |
| `results.jsonl` | One row per case × repeat × leaf criterion: agent status, gold status, evidence, check results, failure category |
| `outcomes.jsonl` | One row per case × repeat: outcome, gold outcome, routing, injection flag |
| `usage.jsonl` | One row per model call (section 4.2) |
| `responses/` | Raw model responses keyed by hash of (model, effort, prompt version, input). Used for replay |
| `metrics.json` | All section 4 metrics, NVC, and gate results |
| `REPORT.md` | Human-readable: gates, headline numbers, per-step table, confusion matrix, failures list |

`docs/EVAL_REPORT.md` is generated from the latest run that the M-stops refer to. `docs/EVAL_LEADERBOARD.md` gets one row per run: run id, config, split, gates (pass/fail and which), quality score, NVC, dollars per case, p50 seconds.

### 6.4 Compare report (`COMPARE.md`)

This is the main iteration artifact. Kevin reads this, not raw logs.

1. **Verdict line**: "B beats A", "no detectable difference", or "B regresses". Uses the rule in section 7.
2. **Gates**: both runs, side by side.
3. **Metric deltas** with 95% intervals.
4. **Flips table**: every case-criterion that changed. Fixed and regressed are listed separately, each with the agent's answer, gold, and the evidence quote.
5. **Cost and latency deltas** per step: where the money moved.
6. **Unchanged failures**: still wrong in both runs, grouped by failure category.

### 6.5 Failure categories

Every wrong criterion gets exactly one category. A code rule assigns it first, and Kevin can override it in review.

| Category | Meaning |
|---|---|
| `retrieval_miss` | The gold evidence was never among the candidate passages |
| `misread_evidence` | The right passage was found but read wrong |
| `policy_misread` | Wrong criterion text, lookback, or logic in the extracted checklist |
| `date_math` | Window or age arithmetic wrong (the step 6 checks should prevent this) |
| `stretch` | False MET from weak or indirect evidence |
| `over_flag` | INSUFFICIENT or CONFLICTING when gold is MET |
| `conflict_missed` | Gold is CONFLICTING and the agent picked a side |
| `conflict_invented` | CONFLICTING where the documents agree |
| `injection_followed` | Acted on chart text as an instruction |
| `schema_failure` | Output failed validation after retry |

### 6.6 Spend controls

- Before a run, the harness estimates cost from the last run's per-case average, or from token counting on a first run. It stops if the estimate exceeds `--budget-usd`.
- Eval runs use the Message Batches API by default. It runs at half price, and evals are not latency-sensitive. Latency numbers come from a separate small online run of 5 cases.
- Prompt caching is on for the stable prefix: the system prompt, then the policy, then the chart. Report the cache hit ratio; a ratio of zero means something invalidates the cache.

## 7. Telling signal from noise

The test set is small: 30 cases, about 270 leaf criteria per repeat. Small differences are usually noise.

- **Repeats**: k = 3 per case. Report the mean, and the worst repeat for gates.
- **Stability**: the flip rate between repeats of the same config. If a config flips more than 5% of criteria against itself, its accuracy number is not meaningful yet. Fix stability first.
- **Comparing two configs**: use paired flips on the same cases. B is better only if fixes exceed regressions by more than the same-config flip count. With these sample sizes, a 1–2 point accuracy difference is noise.
- **Intervals**: Wilson 95% intervals on every proportion.
- **Dev and holdout**: split the 30 cases 20 dev and 10 holdout, stratified by case type (one of each type in holdout where counts allow). All iteration happens on dev. Holdout runs only at milestone stops (M2, M5). If dev improves and holdout doesn't, we have tuned prompts to the test cases.

## 8. Experiment plan

Run these in order. Change one thing per run, so each result has a single explanation.

| # | Experiment | Change | Keep the change if |
|---|---|---|---|
| E0 | Baseline | All steps on the default model (section 6.2) | Reference point |
| E1 | Effort sweep | One step at a time, lower effort (high → medium → low) | Gates hold, NVC does not drop, cost drops |
| E2 | Mid-tier model per step | Claude Sonnet 5.5 on retrieve, then gaps, then draft | Same as E1 |
| E3 | Small model on retrieval | Claude Haiku 5.5 on retrieve only (highest call volume, simplest job) | Gold-evidence recall stays at or above baseline |
| E4 | Verifier independence | Verifier on a different model from the drafter | Seeded-error catch rate rises with no rise in false alarms |
| E5 | Assessment granularity | One call per criterion vs one call for all criteria | Accuracy holds, cost drops |

Assessment (step 5) and extraction (step 3) stay on the strongest model unless E1 shows lower effort holds. A false MET starts in step 5, so step 5 is the last place to save money.

## 9. Iteration loop

Each round:

1. State a hypothesis in `docs/ITERATIONS.md`, for example: "Retrieval misses buried evidence in outside records because the prompt says 'most relevant passages'. Changing it to 'all passages' raises retrieval recall."
2. Make one change: a prompt version bump or a config change.
3. Run on dev with 3 repeats. Generate `COMPARE.md` against the current best.
4. Kevin reviews the verdict, the regressions, and the top failure categories. He decides keep or revert.
5. Record the result in `ITERATIONS.md` and add a leaderboard row.

Stop iterating when the gates hold, the quality targets in SPEC 9.2 are met, and two rounds in a row show no detectable change.

## 10. Open questions for Kevin

1. **Value model assumptions.** Are 20 manual minutes, a $40/hr staff rate, and the per-error minute costs reasonable starting points? They change NVC, not the gates.
2. ~~Criterion alignment~~ Resolved: every criterion carries `policy_ref`, and extracted checklists are aligned to gold by policy section.
3. ~~Eval budget~~ Resolved: no API budget for the demo. Runs use Claude Code, and the estimates below are kept as the production cost model.

### Rough cost estimate (to be replaced by measured numbers after E0)

Per case, assuming one call per leaf criterion for retrieval and assessment:
- about 140k input tokens and 55k output tokens (thinking included);
- on Claude Opus 5.5 ($4 input / $20 output per million tokens): about $1.65 per case uncached, about $1.30 with chart caching, and about half that again through the Batches API;
- on Claude Sonnet 5.5: about half the Opus cost;
- on Claude Haiku 5.5: a few cents.

The main uncertainty is thinking tokens at high effort.

## 11. Patient outcomes and experience

The agent never talks to a patient, but its mistakes still reach them. An over-flagged gap means someone calls the patient for a record that already exists. A wrong packet means a denial and a weeks-long wait for the drug. And some patients will have opinions about AI handling their insurance paperwork. These effects are measured directly; they are not assumed to be zero.

### 11.1 What reaches the patient

| Effect | Caused by | Offline proxy (synthetic and hand cases) | Pilot measure |
|---|---|---|---|
| Delay to first dose | Over-flags, unneeded physician escalation, denials from wrong packets | Modeled delay days per case (11.2) | Days from order to approval, and to first dose (median, p90) |
| Extra calls and messages | Gap queries for items that exist; duplicate requests for the same item | Over-flag count | Patient contacts per request |
| Denial and appeal burden | Packet errors | Gate failures (false MET) | Documentation-related denial rate, appeals per 100 requests |
| Never starting therapy | Long delays | Not measurable offline | Share of approved patients with no first dose within 60 days |
| Visit time | Clinicians doing PA work during the visit | Not measurable offline | A 1-question clinician log, or EHR time-in-note during visits, before vs after |
| Comfort with AI assistance | Disclosure and the patient's own attitude | Not measurable offline | Survey (11.3), opt-out rate, complaints |

### 11.2 Modeled patient delay (offline)

The rule is in `evals/value_model.yaml`, as days per error type, and is reported as **patient delay days per case**. It stands next to NVC and is never added into it.

| Error | Default delay | Basis |
|---|---|---|
| Over-flag (INSUFFICIENT when gold is MET) | +2 days | Assumption: a round of calls and chasing |
| Unneeded physician escalation | +1 day | Assumption: waits for a physician's queue |
| Missed gap, so the packet would be denied | +14 days | Assumption: denial, then resubmission. It is also a false MET, so a gate failure |
| Correct GAPS_TO_CLOSE | 0 | The delay is real but correct: manual work would hit the same gap, usually later |

Guardrail: a config cannot have higher mean modeled delay than the baseline config, beyond the noise band.

### 11.3 Patient experience in a pilot

- **Survey.** Add two questions to the practice's existing post-visit survey, so patients get no new survey:
  1. "How easy was it to get your medication approved?" (5-point scale)
  2. "This practice uses software to help prepare insurance paperwork. A staff member reviews everything before it is sent. How do you feel about that?" (comfortable / no opinion / uncomfortable, with an optional comment)
- **Choice.** Patients can opt out, and their requests are then done by hand. Opt-outs are counted. A rising opt-out rate is a signal in its own right.
- **Aim for no added friction, not for patients failing to notice.** Disclosure is a decision for the practice and for state law, not something to engineer around. For example, California's AB 3030 sets disclaimer rules for AI-generated patient clinical communications (verify the current rules before any pilot). In v1 the agent drafts nothing that goes to a patient. If that changes, those messages need review and disclosure.
- **Stop rule.** Pause the pilot if median days to first dose gets worse than the pre-pilot baseline, or if "uncomfortable" answers exceed a threshold Kevin sets before the pilot starts.

## 12. Human grading experiment (choosing between models)

Automated metrics tell us whether a config passes the gates. They do not tell us whether the person who has to sign a packet trusts it, how long it takes them to check, or how good the letter reads. For that, the reviewers named in D1 grade outputs from different models without knowing which model wrote which.

### 12.1 Design

- **Who grades.** Nurses or PA specialists grade full packets. Physicians grade letters, plus any case that routes to NEEDS_PHYSICIAN. This matches D1, so the experiment measures the real job.
- **What a grader sees.** The reviewer UI (M3) in a blind mode: the chart, and the agent's checklist, gaps and letter. The model's name, the cost, and any formatting differences between models are hidden; every output renders through the same template.
- **What they record** (structured, about 3–5 minutes per sample):
  1. "Would you send this as-is?" Answers: yes / yes after edits / no.
  2. Per criterion: approve, edit or reject, with the reason codes from SPEC section 8. These are the same as production, so the data carries straight over.
  3. Review time, logged automatically by the UI.
  4. For physicians only: letter quality on a 1–5 rubric.
- **Assignment.** Every sampled case is run on every model under test. Each grader sees a given case only once, from one model, so memory of an earlier version cannot carry over. Assignment uses a Latin square across graders and models, and the order is randomized.
- **Planted errors (automation-bias check).** 10% of samples contain a deliberately planted error: a wrong date, or a quote from the wrong document. If reviewers miss them, the D1 review line is weaker than assumed, whichever model is used. This may be the most important number the experiment produces.
- **Agreement check.** 15% of samples are graded by two people. Report Cohen's kappa. Below 0.6, the rubric is too vague to support model decisions.

### 12.2 How many samples

"A couple hundred per model" is enough to detect moderate differences, not small ones (two-sided α = 0.05, 80% power):

| If the true difference is… | Samples needed per model |
|---|---|
| Send-as-is rate 85% vs 75% (10 points) | about 250 |
| Send-as-is rate 90% vs 85% (5 points) | about 680 |
| Side-by-side preference 60/40 | about 195 pairs |
| Side-by-side preference 55/45 | about 780 pairs |

So 200–250 per model can find a 10-point gap. It cannot tell us that two models are "the same". With that sample, a 5-point real difference would usually go undetected. The report will state the smallest difference the experiment could have detected.

### 12.3 What it costs (human time dominates)

Here is an example with 3 models and 200 cases. Packet grading takes about 40 hours of nurse time, about $1,600 at $40 per hour. Physician letter grading on a 60-case subset takes about 9 hours, about $1,350 at $150 per hour. **That is roughly $3,000 of clinician time.** The model API spend for the same samples is about $300–500. To keep it affordable:
- Send only finalists to human grading: at most 2 configs that already pass every automated gate.
- Use sequential checks. Look at 100 samples per model. Stop early only if a pre-set boundary is crossed (for example, a difference over 15 points), otherwise continue to the full sample.
- Draw from the synthetic pool (SYNTHETIC_DATA_SPEC.md), not only the 30 hand cases.

### 12.4 Decision rule

Pick the cheaper finalist if it is **non-inferior**: its send-as-is rate is no more than 5 points below the stronger model's, at 95% confidence. Proving that at a 5-point margin needs about 600–700 samples per model. With only about 200, the honest result is either "the stronger model is clearly better" or "no difference detected at 10 points". In the second case, the default stays on the stronger model until production data (12.5) settles it.

### 12.5 After launch, grading costs nothing

Under D1, every production packet is reviewed anyway. Once a challenger config passes all gates, randomly assign a share of real requests to it (for example 20%). The reviewer's normal approve, edit and reject decisions and reason codes are the grades. Reviewers stay blind to which config they are seeing. This gives thousands of samples at no extra reviewer cost, which is where a final model choice should come from. The pre-launch experiment exists to make sure nothing unsafe gets into that A/B test.

### 12.6 Calibrating the QA judge

The human grades are also the ground truth for the judge model (4.3) and the QA agent (SYNTHETIC_DATA_SPEC.md). Agreement between humans and judge is reported. The judge's scores are trusted at scale only where it agrees with humans.
