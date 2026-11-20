# Prior Authorization Agent (v1)

> **Built by Kevin Hoxha with AI coding tools. All data is synthetic. Not clinically validated. Not medical advice.**
>
> Every patient, practice, payer and policy in this repo is fictional. The policies were written from scratch to follow the common structure of published coverage policies; no payer text is copied.

## What it is

Given a PA request, a patient chart, and a payer policy, the agent:
1. decides which benefit channel applies;
2. turns the policy into a checklist;
3. finds and quotes the chart evidence for each criterion;
4. marks each criterion MET, NOT_MET, INSUFFICIENT_EVIDENCE, or CONFLICTING;
5. lists what is missing and who can supply it;
6. drafts the PA form and the letter of medical necessity, with every claim tied to a quoted source;
7. runs an independent check on its own draft;
8. hands the packet to a human reviewer.

Nothing leaves without human sign-off.

The main example is a fictional gastroenterology practice requesting ustekinumab, a biologic for Crohn's disease and ulcerative colitis, from two fictional payers with different rules. A cardiology drug (evolocumab, a PCSK9 inhibitor) was added afterwards to test whether a new specialty is configuration or engineering.

**Why this problem.** Prior authorization is slow, manual and high-stakes:
- **The workload.** The AMA's 2025 prior authorization physician survey reports about 40 PA requests per physician per week and about 13 hours of physician and staff time. 40% of physicians have staff who work only on PA.
- **Two rails.** Pharmacy-benefit and medical-benefit PA run on different systems (NCPDP SCRIPT ePA vs payer portals and X12 278). One drug can need both, as ustekinumab does.
- **CMS deadlines don't apply to drugs.** The CMS Interoperability and Prior Authorization rule (CMS-0057-F) set decision deadlines for impacted payers from January 1, 2026. Those deadlines cover medical items and services, not drugs, so this repo does not claim they govern drug PA.

New to the terms? Start with [`docs/GLOSSARY.md`](docs/GLOSSARY.md), then [`docs/WALKTHROUGH.md`](docs/WALKTHROUGH.md).

## Headline results

All on synthetic cases, with Opus unless noted. Full reports are in `docs/`.

| Evaluation | Cases | False MET (gate: 0) | Quotes verbatim | Outcome exact | Report |
|---|---|---|---|---|---|
| Held-out set (no prompt tuned on it) | 30 | **0** | 509 / 509 | 29 / 30 | [`EVAL_REPORT.md`](docs/EVAL_REPORT.md) |
| Blind set, Opus | 30 | **0** | 100% | 25 / 30 | [`MODEL_COMPARISON.md`](docs/MODEL_COMPARISON.md) |
| Blind set, Sonnet | 30 | **0** | 100% | 23 / 30 | same |
| Blind set, Haiku | 30 | **0** | 100% | 20 / 30 | same |
| Reuse test: cardiology drug, new policy | 3 | **0** | 100% | 2 / 3, 0 wrong after the B43 fix | [`DECISIONS.md` B41, B43](docs/DECISIONS.md) |
| Spot check after the B43 prompt fix (IBD + reuse) | 12 | **0** | 100% | 10 / 12, 0 wrong | [`DECISIONS.md` B43](docs/DECISIONS.md) |
| Verifier vs planted errors in real packets | 10 errors | | | 10 / 10 caught, 0 false alarms | [`VERIFIER_REPORT.md`](docs/VERIFIER_REPORT.md) |

Each held-out and blind set is 15 Northfield cases plus their Calder Mutual twins, which have the same chart and a different payer. About 1 in 4 cases is clean; the rest are built to break the agent.

What the numbers mean:
- **Safety holds on every model tested.** Zero false METs means the agent never claimed a criterion was met when it wasn't. The models differ in how often they escalate a case that was actually fine. That costs reviewer time but sends nothing wrong.
- **Opus's 5 blind misses are not clear agent errors.** Four are on a stale-evidence boundary the answer key accepts either way. The fifth is a contradiction my generator put in the chart, which Opus correctly flagged.
- **Opus is the offline pick.** List price per case was about $0.29 on Opus, $0.11 on Sonnet and $0.01 on Haiku. Opus is the cheapest model that passes every gate and comes within 5 points of the best outcome accuracy (`COST_EFFECTIVENESS_SPEC.md`).
- **The reuse test was mostly configuration.** It needed two small code fixes, and its runs exposed two errors in my own answer key (B41). Its one real miss, a criterion failed because a different criterion failed, was then fixed with a prompt rule (B43).
- **These are small synthetic samples.** They show the design holds; they do not measure production accuracy.

## How it works

| Step | | Done by |
|---|---|---|
| 1 | Intake: validate the request, chart and policy version | code |
| 2 | Benefit routing: medical vs pharmacy, per phase of therapy | code + lookup table |
| 3 | Policy to checklist, once per policy version, approved by a person | model |
| 4 | Find verbatim evidence for each criterion; flag injected instructions | model + code filter |
| 5 | Judge each criterion | model |
| 6 | Re-check quotes, dates, lookbacks, age and dose. Can take a MET away, never grant one | code |
| 7 | To-do list: missing item, who can supply it, drafted message, what the policy accepts | model |
| 8 | Draft the PA form and letter from verified quotes only | model |
| 9 | Independent verification of every claim against the chart | model |
| 10 | Human review and sign-off, with the required role enforced in code | human |
| 11 | Submission, one file per benefit (mocked) | code |

The full design is in [`docs/AGENT_SPEC.md`](docs/AGENT_SPEC.md). Every judgment call is in [`docs/DECISIONS.md`](docs/DECISIONS.md).

The agent may never submit to a payer, change the order, suggest a different drug, or mark a criterion MET without a quoted source. Missing evidence is reported as missing, never inferred.

## Run it

Requires Python 3.11+ and, for live model calls, [Claude Code](https://claude.com/claude-code) logged in (the default backend) or an Anthropic API key.

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/python -m pytest            # about 1,280 offline tests; no model calls
```

**Open the reviewer screen** on the included runs. This needs no model calls:

```bash
.venv/bin/streamlit run ui/app.py
```

Pick a run and a case:
- **Checklist:** each criterion shows its status, with quotes that open the source document highlighted.
- **Decisions:** approve, edit (with a reason code) or reject each criterion.
- **Packet:** the to-do list, the draft form and letter, and the verifier's flags in red.
- **Sign-off:** stays disabled until every criterion has a decision and the right role is signing. Submission is mocked to `runs/<run>/<case>/submission/`.

**Run the agent.** This makes live model calls:

```bash
# hand-built cases: 3 IBD, 3 cardiology
.venv/bin/python -m agent.pipeline PA-0001 PA-0002 PA-0003
.venv/bin/python -m agent.pipeline PA-0101 PA-0102 PA-0103 --run-name reuse
# synthetic cases: a stratified sample, or payer twins
.venv/bin/python -m agent.pipeline --synth batch-001 --sample 12
.venv/bin/python -m agent.pipeline --synth batch-003 --pairs 15 --seed 3 --model claude-sonnet-5-5
```

Each run writes `runs/<run>/summary.md` and, per case:
- `report.md`: what a reviewer reads, then a comparison with the gold labels;
- `result.json`;
- `audit.jsonl`: every step with its prompt version, model, tokens, seconds and list-price cost.

On Opus a case takes about 1 to 1.5 minutes of model time and about 30k tokens.

**Choose the model and backend:**
- `PA_AGENT_MODEL` sets the model (default `claude-opus-5-5`).
- `PA_AGENT_BACKEND` sets how calls are made: `claude_code` (default), `anthropic_api` or `replay`.
- Identical calls are cached in `runs/cache/`.

**Evaluate:**

```bash
.venv/bin/python -m evals.run --qa --run-name heldout --synth batch-002 --pairs 15 --seed 11   # run + report + QA agent
.venv/bin/python -m evals.run --report-only m2-opus-heldout-v2                              # re-report, no model calls
.venv/bin/python -m evals.compare m2-blind-opus m2-blind-sonnet m2-blind-haiku              # model comparison
.venv/bin/python -m evals.seeded_errors --run m3-opus-packets                               # verifier vs planted errors
```

**Generate synthetic cases:**

```bash
.venv/bin/python -m synth.build --batch 4 --n 100 --seed 4 --paired   # each chart under both payers
```

Code decides every gold label from a blueprint; models only write prose (`docs/SYNTHETIC_DATA_SPEC.md`).

## Repo layout

```text
agent/      pipeline steps 1-11, schemas, model backend, audit log
prompts/    versioned prompt files (name@vN.md); the version goes in the audit log
data/
  policies/   prose policy + gold checklist (gold is for scoring only)
  charts/     hand-built patients (IBD PT-0001..3, cardiology PT-0101..3)
  cases/      requests + gold labels
  reference/  PA lookup, code-enforced policy rules, label dosing
  synth/      generated batches 1-3 (200 + 2 x 100 pairs) with manifests
synth/      synthetic case generator
evals/      metrics, scoring, eval runner, QA agent, seeded errors, model comparison
ui/         Streamlit reviewer screen
runs/       selected runs behind the reports (the response cache is not committed)
tests/      offline tests, including an oracle run of every case through steps 1-9
docs/       see below
```

## Documents

| Document | What it is |
|---|---|
| [`WALKTHROUGH.md`](docs/WALKTHROUGH.md) | One request from start to finish, then the same request with a missing TB screen |
| [`GLOSSARY.md`](docs/GLOSSARY.md) | Plain-language definitions |
| [`AGENT_SPEC.md`](docs/AGENT_SPEC.md) | The agent as built: boundaries, inputs, pipeline, statuses, how to add a policy |
| [`BUILD_LOG.md`](docs/BUILD_LOG.md) | How it was built: who did what, each milestone, what broke and what changed |
| [`DECISIONS.md`](docs/DECISIONS.md) | D1-D6 owner decisions and every build decision (B1-B43) |
| [`EVAL_REPORT.md`](docs/EVAL_REPORT.md) | Held-out evaluation, with the written read and the next three things to fix |
| [`MODEL_COMPARISON.md`](docs/MODEL_COMPARISON.md) | Opus vs Sonnet vs Haiku on the blind set |
| [`VERIFIER_REPORT.md`](docs/VERIFIER_REPORT.md) | Seeded-error test of the verifier |
| [`PRODUCTION_PLAN.md`](docs/PRODUCTION_PLAN.md) | EHR integration, the two submission rails, PHI, policy updates, weekly metrics, second-practice rollout |
| [`INTERVIEW_QA.md`](docs/INTERVIEW_QA.md) | 15 hard questions with answers from the repo |
| [`COST_EFFECTIVENESS_SPEC.md`](docs/COST_EFFECTIVENESS_SPEC.md) | How a cheaper model would earn its place |
| [`SYNTHETIC_DATA_SPEC.md`](docs/SYNTHETIC_DATA_SPEC.md) | How the synthetic cases are built and labeled |
| [`SPEC.md`](SPEC.md) | The original build brief |

## Scope and v2 roadmap

**v1 covers:**
- initial PA requests for adult patients;
- one IBD biologic (ustekinumab) under two fictional payers, and one cardiology drug (evolocumab) as a reuse test;
- standard and expedited requests;
- medical and pharmacy benefit routing.

The brief's other three IBD drugs are configuration work (B42).

**Out of scope, the v2 roadmap:**
- renewals and continuation requests;
- denials, appeals and peer-to-peer preparation;
- real payer portals, real EHR integration and real submission (submission is mocked);
- pediatric patients;
- any clinical recommendation. The agent assembles evidence; it does not choose therapy.

## Open questions for a clinician

These are the limits of a build done without clinical review.

1. Is the split between nurse review and physician review in D1 how a GI practice would staff this?
2. Which objective disease activity measures do payers accept in practice, and how often is the chart missing them?
3. How often is step therapy history only in outside records?
4. What do reviewers distrust most in a drafted letter of medical necessity?
5. Which denial reasons are most common for these drugs, and would they change the criteria list?
6. Are the synthetic charts realistic in what they omit, not only in what they include?

## License

MIT (see [`LICENSE`](LICENSE)). Anyone may reuse the code. The data is synthetic, and nothing here is fit for clinical use.
