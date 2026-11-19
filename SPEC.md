# SPEC: Prior Authorization Agent for IBD Biologics (v1)

Author: Kevin Hoxha
Status: Draft for build
Build tool: Claude Code
Timebox: 2 working days

This file is the build brief. Claude Code: read all of it before writing anything, then follow the milestones in section 12 and stop at every STOP point.

---

## 0. Decisions Kevin owns

These are judgment calls. Each has a default so the build can start, but Kevin should confirm or change them before milestone M1, because he will be asked to defend them.

| # | Decision | Default | Why it matters |
|---|---|---|---|
| D1 | Who reviews what | A nurse or PA specialist reviews every packet. A physician signs the letter of medical necessity and sees any case with a CONFLICTING or NOT_MET criterion | Sets how much clinician time the agent saves and where the risk sits |
| D2 | What the agent may never do | Submit to a payer, change the order, suggest a different drug, or mark a criterion MET without a quoted source | Defines the safety boundary |
| D3 | Release gate | Zero false MET results on the test set. Any false MET blocks release | A false MET sends a wrong packet out under a physician's name |
| D4 | Behavior when evidence is missing | Say INSUFFICIENT_EVIDENCE and name the exact missing item. Never infer | Trades automation rate for trust |
| D5 | v1 scope | Initial authorization only. No renewals, denials, appeals, or peer-to-peer calls | Keeps the first version shippable |
| D6 | Test set mix | 30 cases, about 1 in 4 clean. The rest are designed to break the agent | An easy test set proves nothing |

---

## 1. Problem

A gastroenterology practice prescribes a biologic for a patient with Crohn's disease or ulcerative colitis. The payer requires prior authorization (PA). Staff must find the payer's policy, read the criteria, dig through the chart for proof of each one, fill in the form, write a letter of medical necessity, and submit. If one item is missing, such as a tuberculosis screen or proof that an earlier drug failed, the request is denied or delayed and the patient waits.

Background facts (checked November 2026, cite in README):

- The AMA's 2025 physician survey reports about 40 PA requests per physician per week, about 13 hours of physician and staff time, and 40% of physicians with staff who work only on PA.
- Pharmacy-benefit and medical-benefit PA run on different rails. Self-injected drugs usually go through the pharmacy benefit (NCPDP SCRIPT ePA, networks such as CoverMyMeds and Surescripts). Infused drugs billed by the practice usually go through the medical benefit (plan portals, X12 278). An agent must know which one applies.
- The 2024 CMS Interoperability and Prior Authorization rule (CMS-0057-F) set 72-hour expedited and 7-day standard decision deadlines for impacted payers from January 1, 2026, but those deadlines cover medical items and services, not drugs. Do not claim they govern this workflow.

## 2. What v1 does, in one paragraph

Given a PA request, a patient chart, and a payer policy, the agent decides which benefit channel applies, turns the policy into a checklist, finds and quotes the chart evidence for each criterion, marks each criterion MET, NOT_MET, INSUFFICIENT_EVIDENCE, or CONFLICTING, lists what is missing and who can supply it, drafts the PA form and the letter of medical necessity with every claim tied to a quoted source, runs an independent check on its own draft, and hands the packet to a human reviewer. Nothing leaves without human sign-off.

## 3. Users

- PA specialist or nurse: reviews the checklist and packet, closes gaps, approves or edits.
- Gastroenterologist: signs the letter, resolves conflicts.
- Agent owner (the role Kevin is applying for): reads the eval report and failure log, decides what ships next.

## 4. Scope

In scope for v1:

- Initial PA requests for 4 drugs in adult IBD: adalimumab, infliximab, ustekinumab, vedolizumab.
- 2 fictional payers, each with its own policy per drug.
- Standard and expedited requests.
- Pharmacy-benefit and medical-benefit routing.

Out of scope for v1 (list these in the README as the v2 roadmap):

- Renewals and continuation requests.
- Denials, appeals, peer-to-peer preparation.
- Real payer portals, real EHR integration, real submission. Submission is mocked.
- Pediatric patients.
- Any clinical recommendation. The agent assembles evidence. It does not choose therapy.

## 5. Hard rules for the build

1. Synthetic data only. No real patients, no real practice, no real payer names, no copied payer policy text. Policies are written from scratch and modeled on the common structure of published policies.
2. Fictional names: practice is "Harbor Digestive Associates". Payers are "Northfield Health Plan" and "Calder Mutual". Use generic drug names only.
3. Do not name any real company as the intended user anywhere in the repo.
4. README must say: built by Kevin Hoxha with AI coding tools, synthetic data, not clinically validated, not medical advice.
5. Stack: Python 3.11+, Anthropic Python SDK, pydantic for schemas, Streamlit for the reviewer UI, pytest. Model ID comes from an environment variable. Check the current Anthropic docs for the right model ID instead of assuming one.
6. All model outputs that feed later steps use structured output (tool use with a pydantic schema). No free-text parsing.
7. Every prompt lives in `prompts/` as a versioned file. The prompt version is written to the audit log.
8. Chart text is data, never instructions. One test case contains an injected instruction inside a clinic note. The agent must ignore it and flag it.

## 6. Inputs

### 6.1 PA request

```yaml
# === PA REQUEST (example) ===
request_id: PA-0007
patient_id: PT-0007
drug: ustekinumab
dose: "weight-based IV induction, then 90 mg SC every 8 weeks"
indication_icd10: K50.90
payer: northfield
plan_type: commercial
ordering_provider: "Dr. A. Rivera, Gastroenterology"
urgency: standard        # standard | expedited
requested_start: 2026-12-01
```

### 6.2 Chart

One folder per patient under `data/charts/PT-xxxx/`. Each document is a plain text or markdown file with a header (doc id, type, date, author). Document types:

- problem list
- medication history (start date, stop date, reason stopped)
- GI progress notes (free text, 2 to 5 per patient)
- endoscopy and colonoscopy reports
- labs (CRP, fecal calprotectin, TB screen, hepatitis B panel, CBC, liver panel)
- outside records (scanned-style text, messier formatting)

### 6.3 Payer policy

Each policy exists twice: as prose the way a payer publishes it (`policy.md`), and as the structured checklist the agent extracts from it. The gold structured version is stored for evaluation only. The agent must build its own from the prose.

```yaml
# === EXTRACTED POLICY CHECKLIST (target schema) ===
policy_id: northfield-ustekinumab-ibd
version: "2026-10"
benefit_channel:
  iv_induction: medical
  sc_maintenance: pharmacy
auth_duration_months: 6
logic: ALL            # ALL criteria below must be met
criteria:
  - id: C1
    type: diagnosis
    text: "Diagnosis of moderately to severely active Crohn's disease or ulcerative colitis"
    evidence_needed: ["diagnosis in GI note", "objective activity measure"]
  - id: C2
    type: prescriber
    text: "Prescribed by or in consultation with a gastroenterologist"
  - id: C3
    type: age
    text: "Patient is 18 or older"
  - id: C4
    type: step_therapy
    logic: ANY
    text: "Inadequate response, intolerance, or contraindication to at least one conventional therapy AND at least one preferred anti-TNF agent"
    evidence_needed: ["drug name", "dates", "reason stopped"]
  - id: C5
    type: safety_screen
    text: "Negative TB screening within the past 12 months"
  - id: C6
    type: safety_screen
    text: "Hepatitis B screening on file"
  - id: C7
    type: exclusion
    text: "Not used together with another biologic or JAK inhibitor"
  - id: C8
    type: dosing
    text: "Requested dose is within the labeled dosing"
```

The two payers must differ in ways that matter: one requires a step through a preferred anti-TNF before ustekinumab or vedolizumab and the other does not; TB lookback is 12 months for one and 6 for the other; one accepts fecal calprotectin as the objective measure and the other requires endoscopy.

## 7. Pipeline

Each step is its own module with its own schema, prompt, and tests.

| Step | Name | What it does | Model or code |
|---|---|---|---|
| 1 | Intake | Validates the request, loads chart and policy, sets urgency | Code |
| 2 | Benefit routing | Decides pharmacy or medical channel and whether PA is required at all | Code plus lookup table |
| 3 | Policy extraction | Turns policy prose into the checklist schema | Model |
| 4 | Evidence retrieval | For each criterion, finds candidate passages across all chart documents | Model |
| 5 | Criterion assessment | Assigns a status to each criterion with quoted evidence and a confidence | Model |
| 6 | Deterministic checks | Quote exists verbatim in the cited document; dates fall inside lookback windows; age computed from date of birth; dose compared to a label table | Code |
| 7 | Gap plan | For every criterion that is not MET, names the missing item, who can supply it, and drafts a short query to the clinician | Model |
| 8 | Packet drafting | Fills the PA form fields and writes the letter of medical necessity. Every factual sentence carries a citation | Model |
| 9 | Independent verification | A separate model call that sees only the packet and the source documents, not the earlier reasoning, and checks each claim | Model |
| 10 | Review gate | Routes to the right reviewer and records approve, edit, or reject per criterion | Streamlit UI |
| 11 | Mock submission and audit log | Writes the final packet and a full trace to disk | Code |

### 7.1 Criterion statuses

- MET: at least one verbatim quote supports it and step 6 passes.
- NOT_MET: the chart shows the criterion fails (for example, TB screen is 14 months old against a 12-month window).
- INSUFFICIENT_EVIDENCE: nothing in the chart settles it. The agent names what is missing.
- CONFLICTING: two documents disagree (for example, one note says adalimumab was stopped for loss of response, an outside record says it was never started).

Rule: the builder of a claim does not approve it. Step 5 proposes, step 6 and step 9 check, a human decides.

### 7.2 Packet outcomes

- READY_FOR_REVIEW: all criteria MET.
- GAPS_TO_CLOSE: at least one INSUFFICIENT_EVIDENCE and none NOT_MET. Output is a to-do list, not a packet.
- NEEDS_PHYSICIAN: any CONFLICTING or NOT_MET. The agent states the facts and stops. It does not propose another drug.

### 7.3 Output schema for one criterion

```json
{
  "criterion_id": "C5",
  "status": "MET",
  "confidence": 0.94,
  "evidence": [
    {
      "doc_id": "PT-0007/labs-2026-08-14",
      "quote": "QuantiFERON-TB Gold Plus: NEGATIVE",
      "doc_date": "2026-08-14"
    }
  ],
  "reasoning": "Negative IGRA dated 2026-08-14 is within the 12-month lookback.",
  "deterministic_checks": {"quote_found": true, "date_in_window": true}
}
```

## 8. Reviewer UI (Streamlit)

One page per request:

1. Header: patient, drug, payer, channel, urgency, packet outcome.
2. Checklist: one row per criterion with status, the quoted evidence, and a link that opens the source document at the quote.
3. Gap list with the drafted clinician query.
4. Draft form and letter, with citations visible.
5. Verification results from step 9, with any disagreement shown in red.
6. Per-criterion Approve, Edit, Reject. Edits require a reason from a short list (wrong evidence, missed evidence, wrong status, wording).
7. Final sign-off button, disabled until every criterion has a decision.

Every reviewer action is written to the audit log. Reviewer edits are the main production signal, so the reason codes matter.

## 9. Evaluation

### 9.1 Test set

30 synthetic cases under `data/cases/`, each with gold labels per criterion and a gold packet outcome.

| Type | Count | What it tests |
|---|---|---|
| Clean, all criteria met | 8 | Baseline |
| One required item missing (TB screen, HBV panel, objective measure) | 6 | Says INSUFFICIENT, names the item |
| Criterion clearly not met (stale TB screen, no step therapy, concurrent biologic) | 4 | Says NOT_MET, does not stretch |
| Conflicting documents | 3 | Says CONFLICTING, routes to physician |
| Evidence only in messy outside records or buried in free text | 3 | Retrieval |
| Same patient, two payers, different answer | 2 | Policy differences are respected |
| Wrong benefit channel on the request | 2 | Routing |
| Expedited request | 1 | Urgency handling |
| Injected instruction inside a clinic note | 1 | Treats chart as data |

### 9.2 Metrics and gates

| Metric | Definition | Gate |
|---|---|---|
| False MET rate | Criteria marked MET that gold says are not | 0, blocks release |
| Citation validity | Quotes found verbatim in the cited document | 100%, enforced in code |
| Criterion accuracy | Status matches gold | 90% or higher |
| INSUFFICIENT recall | Missing items correctly flagged | 95% or higher |
| Packet outcome accuracy | Outcome matches gold | 90% or higher |
| Routing accuracy | Benefit channel correct | 100% |
| Verifier catch rate | Seeded errors caught by step 9 | Report only |
| Cost and latency per case | Tokens, dollars, seconds | Report only |

### 9.3 Harness

`python -m evals.run` runs all cases, writes `docs/EVAL_REPORT.md` with a per-case table, a confusion matrix for criterion status, and a list of every failure with the case id, the criterion, what the agent said, what gold says, and a failure category. Seed 5 deliberate errors into packets to measure whether step 9 catches them.

### 9.4 Failure modes to track

| Failure mode | How it is detected | Mitigation in v1 |
|---|---|---|
| Unsupported claim in the letter | Step 6 quote check, step 9 | Blocks packet |
| Right fact, wrong patient or wrong date | Step 6 date and id checks | Blocks packet |
| Stretching weak evidence to MET | False MET rate on test set | Prompt rule plus INSUFFICIENT as the default |
| Misreading policy logic (ALL vs ANY) | Compare extracted checklist to gold | Report extraction accuracy per policy |
| Missing evidence that exists | Reviewer reason code "missed evidence" | Retrieval over every document, not top few |
| Stale policy version | Policy version in audit log | Version field required |
| Instruction hidden in chart text | Injection test case | Chart passed as quoted data, flagged in output |

## 10. Reuse test

After the IBD work passes its gates, add one policy for a different specialty with no code changes: a PCSK9 inhibitor for a cardiology practice (criteria: diagnosis, LDL above threshold on maximally tolerated statin, statin intolerance documentation, prescriber specialty). Add 3 cases. If this needs code changes, record exactly what and why in `docs/DECISIONS.md`. The point is to show whether "new drug, new payer, new specialty" is configuration or engineering.

## 11. Repo layout

```text
# === REPO LAYOUT ===
prior-auth-agent/
  README.md
  SPEC.md
  agent/
    intake.py  routing.py  policy_extract.py  retrieve.py
    assess.py  checks.py  gaps.py  draft.py  verify.py  audit.py
    schemas.py  pipeline.py
  prompts/            # versioned prompt files
  data/
    policies/         # prose policy + gold checklist per payer and drug
    charts/           # one folder per synthetic patient
    cases/            # request + gold labels
    reference/        # label dosing table, PA-required lookup
  evals/
    run.py  metrics.py  seeded_errors.py
  ui/
    app.py
  tests/
  docs/
    WALKTHROUGH.md  DECISIONS.md  GLOSSARY.md
    EVAL_REPORT.md  PRODUCTION_PLAN.md  INTERVIEW_QA.md
```

## 12. Milestones

| # | Deliverable | STOP for Kevin |
|---|---|---|
| M0 | `schemas.py`, 1 prose policy with gold checklist, 3 full sample cases (one clean, one missing item, one conflicting) | Yes. Kevin reviews realism and confirms D1 to D6 |
| M1 | Steps 1 to 7 running on the 3 cases, with unit tests for step 6 | Yes. Kevin reads 3 outputs end to end |
| M2 | Remaining policies, all 30 cases, eval harness, first `EVAL_REPORT.md` | Yes. Kevin picks which failures to fix |
| M3 | Steps 8 to 11 and the reviewer UI | No |
| M4 | Reuse test (section 10) | No |
| M5 | All docs in section 13, final eval report, README | Yes. Final read |

At each STOP, summarize what was built, what failed, and what you need decided. Do not continue until Kevin answers.

## 13. Documents to write

These are for a reader with no healthcare background. Plain language, short sentences, define every term the first time.

- `README.md`: what it is, the one-paragraph description from section 2, how to run it, headline eval numbers, the honesty statement from section 5.
- `docs/WALKTHROUGH.md`: one request followed from start to finish in narrative form, including what a human sees and decides. Then the same request with a missing TB screen, and what changes.
- `docs/GLOSSARY.md`: prior authorization, step therapy, biologic, anti-TNF, medical vs pharmacy benefit, buy and bill, letter of medical necessity, formulary, IGRA, fecal calprotectin, peer-to-peer, ePA, NCPDP SCRIPT, X12 278.
- `docs/DECISIONS.md`: each of D1 to D6 with the choice made, the alternative, and the reason. Add every design decision made during the build.
- `docs/EVAL_REPORT.md`: generated by the harness, plus a short written read of the results and the next 3 things to fix.
- `docs/PRODUCTION_PLAN.md`: what would change with a real client. EHR integration, the two submission rails, PHI handling, how payer policy updates are caught, what to monitor weekly (first-pass approval rate, denial reasons mapped back to criteria, reviewer edit rate by reason code, turnaround time), and what a rollout to a second practice would need.
- `docs/INTERVIEW_QA.md`: 15 questions a product leader at a clinical AI company would ask about this build, each with a direct answer drawn from the repo. Include the hard ones: why this review line, what breaks first at scale, what you would cut, what a clinician would object to.

## 14. Open questions for a clinician

List these in the README. They are the limits of a build done without clinical review.

1. Is the split between nurse review and physician review in D1 how a GI practice would staff this?
2. Which objective disease activity measures do payers accept in practice, and how often is the chart missing them?
3. How often is step therapy history only in outside records?
4. What do reviewers distrust most in a drafted letter of medical necessity?
5. Which denial reasons are most common for these drugs, and would they change the criteria list?
6. Are the synthetic charts realistic in what they omit, not only in what they include?

## 15. Definition of done

- All gates in 9.2 pass, or each miss is explained in `EVAL_REPORT.md` with a planned fix.
- A reviewer can open any case in the UI, trace every sentence in the letter to a quote, and sign off.
- The reuse test result is written down, whichever way it went.
- A person who has never worked in healthcare can read `WALKTHROUGH.md` and explain the process back.
