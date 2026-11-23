# Build log: how this was built

This is the story of the build in order: what each milestone produced, what went wrong, and what changed because of it. Every numbered decision (B1 to B43) is written up in full in `DECISIONS.md`. All data is synthetic.

## Who did what

- **Kevin Hoxha** set the build brief (`SPEC.md`) and owned the product decisions. The brief proposed defaults for D1 to D6, and Kevin accepted them for the build:
  - who signs what (D1);
  - what the agent may never do (D2);
  - the zero-false-MET release gate (D3);
  - "missing is missing, never inferred" (D4);
  - the test mix (D6).

  He reviewed the work at each stop point and settled calls the build could not settle alone. He asked that an indeterminate TB test be treated as a gap rather than a failure (B25), and that the to-do list state what the policy would accept (B35). He set the scope cuts: one IBD drug instead of four (B42), and no expensive re-runs when a cheaper check would answer the question.
- **AI coding tools (Claude Code)** wrote most of the code, the synthetic data generator, the prompts and the first drafts of the documents, working from the brief.
- **The evaluation harness** is how the work was checked. Nothing counted as done because it looked right. It counted when the eval said so, and every disagreement was read by hand or by the QA agent.

**Constraint that shaped the design:** no paid API budget. Every model call runs through Claude Code on a subscription (B17), and identical calls are cached. That is why the build counts tokens carefully, and why some re-runs were done as small spot checks.

## Milestones

| Milestone | Built | What went wrong, and the fix | Result |
|---|---|---|---|
| **M0** Foundations | Schemas, the Northfield ustekinumab policy with a gold checklist, 3 hand-built cases (clean, missing item, conflicting) | The design questions came first: nested criteria are judged at the leaves and combined in code (B2), schema validators enforce "no MET without a quote" (B8), gold labels may list acceptable alternates (B13) | A typed data model that makes the unsafe outputs impossible to represent |
| **M1** Steps 1 to 7 | Intake, routing, policy extraction, retrieval, assessment, code checks, gap plan. Unit tests for every code check | The first prompt treated "a document doesn't mention X" as a conflict and over-escalated (B27). The generator wrote medication histories that contradicted themselves (B26) | 15 cases: 12/15 exact outcomes at first, then 15/15 after `assess@v2`. 0 false METs throughout |
| **M2** Second payer and evaluation | Calder Mutual's policy, built to differ where it matters (B28). A synthetic case generator in which code decides every gold label and models only write prose (B14). Payer twins: one chart under both payers (B29). The eval harness and a QA agent that reviews every disagreement (B31) | The first held-out run had 3 wrong outcomes. Reading them showed that my **answer key** was inconsistent about stale evidence (B32, B34), and the QA agent found generator bugs (B33). Fixing the answer key after reading a test set spoils that set, so a fresh blind batch was generated | Held-out: 29/30 exact, 315/315 criteria. Blind, Opus: 25/30 exact. Sonnet and Haiku: 23/30 and 20/30. 0 false METs on every model |
| **M3** Packets and review | Drafting of the PA form and letter from verified quotes only (B36), an independent verifier, the Streamlit reviewer screen, sign-off rules in code (B37), mocked submission | The scorer invented 3 Sonnet false METs by comparing a merged parent criterion with a failed branch (B39). The blind run also found data gaps: the prescriber's specialty appeared only in document metadata (B38) | The verifier caught 10/10 planted errors with no false alarms (B40) |
| **M4** Reuse test | A cardiology drug (evolocumab) under a new policy, for a new fictional practice, with 3 cases | A date check written for IBD charts misfired on a drug start date. The to-do list asked about an unused either/or branch. The agent also found 2 errors in my answer key (B41) | Mostly configuration: a policy file, one lookup row, one rules row, and 2 small code fixes. 0 false METs |
| **M5** Docs and follow-ups | README, walkthrough, glossary, agent spec, production plan, interview Q&A. Then the coupled-criteria fix and the data fixes (B43). Last, the reviewer screen was redesigned in Claude Design and ported to Streamlit (`docs/design/`, `ui/styles.css`); the review logic and sign-off rules did not change | The reuse test's one real miss was a criterion failed because a *different* criterion failed. Fixed with one prompt rule (`assess@v3`) | 12-case spot check: 0 false METs, 123/123 criteria, 0 wrong outcomes |

## How each change was tested

1. **Code first, where code can decide.** Quotes, dates, lookback windows, age and the weight-tier dose are checked in `agent/checks.py`, with a unit test for each. Code can take a MET away but never grant one (B22).
2. **The offline test suite** (1,278 tests) runs with no model calls. It includes an "oracle" run of every committed case through steps 1 to 9 with the gold answers replayed, so the plumbing is tested separately from the model.
3. **Small live runs before big ones.** Every prompt change was run on a handful of cases chosen to stress it. For `assess@v3`, the six blind cases with the most NOT_MET criteria were the stress test, because a rule that softens NOT_MET would do harm there.
4. **Held-out, then blind.** A test set that has been read in order to fix things is no longer a fair test. When the held-out set was used up that way, a new blind batch was generated.
5. **Read every disagreement**, and allow for the answer key being wrong. Over the build, the gold labels were wrong about as often as the agent was.

## What I'd say I learned

- **Safety comes from structure, not from asking the model to be careful.** The model cannot say MET without a quote, code re-checks what it can compute, the drafter never sees the raw chart, and a separate verifier checks the draft. Each layer assumes the one before it can fail.
- **The answer key is a product too.** Most of the debugging time went into finding out whether the agent or the label was wrong.
- **A heuristic for one specialty encodes that specialty's assumptions.** The reuse test found this in under a day, which is the argument for running a reuse test before selling a second specialty.
- **Measure before spending.** The cheaper-model re-run (about 1.5M tokens) was deliberately left undone. The data fix that would make it fair is in place, and the decision rule for using it is written down (`COST_EFFECTIVENESS_SPEC.md`).

## Prompt versions

| Prompt | Current | Why it changed |
|---|---|---|
| `assess` | v3 | v2: a document that doesn't mention something is not a conflict (B27), and an indeterminate test needs repeating. v3: judge a coupled criterion on what it measures (B43) |
| `draft` | v2 | v2: no uncited transition sentences, after the verifier flagged one (B40) |
| `gaps` | v2 | v2: each item states what the policy would accept, with the date computed, and never tells the provider to order a test (B35) |
| `retrieve`, `policy_extract`, `verify` | v1 | Unchanged |

Old versions stay in `prompts/` so archived runs can be reproduced. Each run's audit log records which version made each call.
