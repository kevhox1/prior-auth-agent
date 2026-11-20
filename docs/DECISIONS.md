# Decisions

Every judgment call in the build, with the choice made, the main alternative, and the reason.

## Owner decisions (D1 to D6)

Status: **defaults accepted by Kevin for the build.** They are the parts a clinician reviewer should challenge first (see the open questions in the README).

| # | Decision | Choice (default) | Alternative considered | Reason |
|---|---|---|---|---|
| D1 | Who reviews what | A nurse or PA specialist reviews every packet. A physician signs the letter of medical necessity and sees every case with a CONFLICTING or NOT_MET criterion | Physician reviews every packet | Nurses already do this work in most practices. Physician time goes to the cases that need judgment |
| D2 | What the agent may never do | Submit to a payer, change the order, suggest a different drug, or mark a criterion MET without a quoted source | Let the agent suggest an alternative drug when a criterion fails | Choosing therapy is a clinical decision. The agent assembles evidence only |
| D3 | Release gate | Zero false MET results on the test set | A tolerance, such as under 2% | A false MET sends a wrong packet out under a physician's name |
| D4 | Missing evidence | Say INSUFFICIENT_EVIDENCE and name the exact missing item. Never infer | Infer from indirect evidence (for example, "patient was on infliximab, so they must have had a TB screen") | Gives up some automation to earn trust |
| D5 | v1 scope | Initial authorization only | Include renewals | Renewals need response-to-therapy evidence, which is a different problem |
| D6 | Test set mix | 30 cases, about 1 in 4 clean | Mostly clean cases | An easy test set proves nothing |

## Build decisions

### B1. Diagnosis and objective disease activity are separate criteria (M0, confirmed by Kevin)
The spec example puts both under C1. They are split into C1 (diagnosis and severity) and C2 (objective measure). **Why:** "objective measure missing" is one of the spec's missing-item test types. As its own criterion it gets its own status and gap item. Otherwise it would be hidden inside a partly met diagnosis criterion. **Cost:** criterion ids differ from the spec example.

### B2. Nested criteria: the model assesses leaves, code combines them (M0, confirmed by Kevin)
Step therapy is a parent criterion (C5, logic ALL) with two leaves: C5a conventional therapy and C5b anti-TNF. The model assesses only leaf criteria. `schemas.roll_up()` computes parent statuses in code. **Why:** misreading ALL against ANY is a listed failure mode. Doing that logic in code removes the failure mode from the model's job. Extraction accuracy on the `logic` field is still scored in step 3.

Combination rules (`schemas.combine`):
- ALL: NOT_MET outranks CONFLICTING, which outranks INSUFFICIENT_EVIDENCE. Any of them fails the parent.
- ANY: one MET satisfies the parent. Otherwise CONFLICTING outranks INSUFFICIENT_EVIDENCE, which outranks NOT_MET, because an unresolved branch might still turn out MET.

### B3. The packet outcome uses rolled-up top-level statuses (M0)
A NOT_MET leaf inside an ANY group that is otherwise MET does not send the case to a physician. Only top-level criteria decide the outcome (spec 7.2).

### B4. Specialty-neutral document types (M0)
`progress_note` and `procedure_report` replace "GI progress note" and "endoscopy report". A `demographics` type was added, because the spec's list has nowhere to hold date of birth, and the age check needs one. **Why:** the reuse test (section 10) should need no new document types for a cardiology chart.

### B5. A `request_date` field on the request (M0)
Lookback windows (TB within 12 months, and so on) are measured back from `request_date`, not from today's date or `requested_start`. **Why:** evals must give the same answer on any day they are run. In production this would be the submission date.

### B6. An optional `requested_channel` on the request (M0)
**Why:** the wrong-channel test cases need an office-entered channel for routing to check and correct. Routing never trusts this field. It computes the channel from the lookup table and flags any mismatch.

### B7. Quote matching forgives whitespace only (M0)
`checks.quote_in_text` collapses runs of whitespace before matching. Case, punctuation and characters must match exactly. **Why:** scanned outside records wrap lines and pad columns, so a quote that crosses a line break has to match. Anything looser, such as case folding or fuzzy matching, would let a slightly wrong quote pass the 100% citation gate.

### B8. Schema validators enforce D2 and D4 (M0)
Pydantic validation rejects any model output that breaks these rules:
- MET with no quoted evidence;
- INSUFFICIENT_EVIDENCE that names no missing item;
- CONFLICTING that cites fewer than two documents;
- a factual letter sentence with no citation;
- a reviewer edit with no reason code.

**Why:** the rules hold even if a prompt changes. A rejected output is retried or logged as a failure. It is never silently accepted.

### B9. Gold labels say what would resolve every non-MET criterion (M0)
This applies to CONFLICTING as well as INSUFFICIENT_EVIDENCE. **Why:** the gap plan (step 7) is scored on whether it names the right missing item.

### B10. The Northfield policy states when patient-reported history counts (M0)
Section 3.5 accepts patient-reported treatment history only when "it is documented by the treating provider and does not conflict with other records on file." **Why:** this makes PA-0003's CONFLICTING label follow from the policy text, not from a judgment call. Real policies vary on this point. That is clinician question 3 in the README.

### B11. Baseline model, and how cheaper models get chosen (M0, confirmed by Kevin: start on Opus)
Every model step starts on `claude-opus-5-5` (checked against the Anthropic docs, cached 2026-11-03). The model ID comes from config or the environment, never from code. Moving a step to a cheaper model or a lower effort level is an experiment, not a default. It ships only if it passes the rule in `docs/COST_EFFECTIVENESS_SPEC.md`: gates hold on every repeat, and net value per case does not drop. **Why:** a false MET starts in assessment, and its cost is not measured in tokens. Model spend per case ($0.05–$1.65 estimated) is small next to the roughly $13 of staff time a manual prior authorization costs.

API notes for M1:
- On this model, thinking cannot be turned off. Effort is the control, and its default is `medium`, so set it explicitly in each step's config.
- Forced `tool_choice` is rejected on this model. Structured output uses `client.messages.parse()` with the pydantic schemas, which meets spec rule 6 ("no free-text parsing").

### B12. Policy changes after clinical review (M0)
A background agent reviewed the policy and charts against the FDA label, ACG/AGA guidelines, CDC hepatitis B guidance and published 2026 payer policies. Kevin approved these changes:
- **Section 3.5 rewording.** Prior therapy must now be supported by claims, prescription records or provider notes. Inconsistent records send the request to clinical review. The old clause accepting patient-reported history appears in no real policy the agent found, and it left PA-0003's label open to a NOT_MET reading.
- **New section 3.10, preferred products** (ustekinumab-aekn and ustekinumab-ttwe), and a `product` field on the request. Every 2026 policy the agent checked has a preferred-biosimilar rule. Billing (HCPCS) codes were left out on purpose, to avoid inventing wrong codes.
- **Adults only.** Pediatric requests point to a separate fictional policy, consistent with D5 and the spec's v1 scope. The 2026 label covers pediatric Crohn's, so calling it "not medically necessary" was wrong.
- **Chart fixes.** Timeline and dose inconsistencies were fixed. Labs now show realistic detail. The PT-0002 anti-HBc specimen was never collected (results normally return in 1–3 days, so a 19-day "pending" was not credible). A PT-0003 interim visit was added.

### B13. Gold labels can list acceptable alternates (M0)
`GoldCriterion.acceptable_alternates` lists other statuses a careful reviewer could defend. These are scored as correct but reported separately. The schema forbids MET as an alternate for any non-MET gold label, so D3 cannot be loosened through an alternate. First use: PA-0003 C5b (CONFLICTING, alternate NOT_MET).

### B14. Synthetic cases: code decides gold, models only write prose (M0 design, built in M2)
See `docs/SYNTHETIC_DATA_SPEC.md`. **Alternative:** have an LLM write each case and label it. **Rejected because** the generator's mistakes would become the answer key, and the eval could not catch them. The hand-reviewed 30 (Tier 1) stay the release gate; the synthetic set (Tier 2) is for breadth and for finding failure patterns.

### B15. Model choice is settled by blinded reviewer grading, then a production A/B (M0 design)
See COST_EFFECTIVENESS_SPEC.md section 12. Kevin's proposal: send reviewers outputs from several models and select on graded quality. The design is blinded and Latin-square assigned, with planted errors to measure automation bias and a double-graded subset for agreement. Two things are stated up front:
- About 200 samples per model detect roughly a 10-point difference, not 5.
- Clinician time (about $3,000) dwarfs the model spend.

The final choice comes from a randomized production A/B, where reviewers grade as part of normal review at no extra cost.

### B16. Patient outcomes are guardrails, not dollars (M0 design)
Kevin asked for patient outcomes and visit experience in the decision rule. Modeled delay days (offline) and measured time to therapy, patient contacts, survey answers and opt-outs (pilot) are guardrails that a config must not worsen. Like false METs, they are never converted to dollars. Patients can opt out to manual processing. Disclosure follows practice policy and state law; the aim is no added friction, not concealment.

### B17. Every model call goes through one backend interface; the default is Claude Code (M0)
`agent/llm.py` has three backends:
- `claude_code`, the default: `claude -p --json-schema`, with no tools, no settings, and an empty working directory;
- `anthropic_api`: `messages.parse` with the pydantic schema;
- `replay`: cache only.

**Why:** this is an interview demo, and Kevin chose not to fund an API budget. Claude Code's `--json-schema` returns schema-validated `structured_output`, so spec rule 6 (structured output, no free-text parsing) still holds. It also reports tokens and a list-price cost for every call, so the cost-vs-effectiveness method still works. Swapping to the API in production is a config change, not a code change.

### B18. Synthetic cases are rendered from code templates by default (M0)
**Alternative:** a model writes every document. **Chosen:** code templates with 3 note styles, 3 lab layouts, 3 medication-history formats, 4 outside practices (clean, faxed, or OCR-damaged), distractor documents, and copy-forward. **Why:**
- Generation is free and reproducible from a seed.
- The templates cannot leak a fact the blueprint says is missing.

The prose is less natural than a model's. The optional `--rewrite` pass adds realism through Claude Code, and validation keeps the gold labels correct. Batch 1 has 200 cases with 0 rejected, and all pass the same integrity tests as the hand cases.

### B19. One model call per step per case, not per criterion (M1)
**Alternative:** spec section 7 reads as one retrieval and one assessment call per criterion, which is about 22 calls per case. **Chosen:** retrieval, assessment, and the gap plan each make one call that covers every criterion, so a case costs 3 calls. Policy extraction is one more call per policy version, and it is cached. **Why:** runs go through Claude Code on a subscription, so call count is the real limit. Charts are small (about 10 to 30 KB), so one call can read all of them. Each step still has its own module, schema, prompt, and audit entry. Going back to per-criterion calls changes only the loop in `retrieve.py` and `assess.py`. It would be worth testing if long charts start to hurt recall.

### B20. Assessment sees the retrieved passages, not the full chart (M1)
**Why:** this makes every miss traceable to one step. If a passage never reached step 5, it is a retrieval miss. If it reached step 5 and was misread, it is an assessment error. Step 5 also gets the list of every document searched, so it can say "no anti-HBc result in any of 9 documents." Retrieval is told that recall matters more than precision. Code drops any retrieved passage that is not verbatim before step 5 sees it.

### B21. Code-checkable policy parameters live in a reviewed table, not only in the extraction (M1)
`data/reference/policy_rules.yaml` holds the lookback windows, the minimum age, and the weight-recency rule, keyed by policy section. Step 6 enforces them even when step 3 left them out. Intake stops the run if the policy version on file does not match the lookup table. **Why:** a missed lookback in extraction must never turn into a false MET. **Cost:** a human updates the table when a policy changes. That is the same review the policy-change process needs anyway.

### B22. Step 6 can take a MET away but can never grant one (M1)
- A failed check on a MET (quote not verbatim, wrong document date, another patient's document, out of window, a stale date written inside the quote, an age under 18, a dose off its label tier, a stale weight) downgrades it. Missing proof becomes INSUFFICIENT_EVIDENCE; proven failure becomes NOT_MET.
- The model's original status is kept and shown to the reviewer.
- Checks on non-MET statuses are recorded but never change the status.

**Why:** "the builder of a claim does not approve it" (spec 7.1), applied in the one direction that protects D3.

### B23. Injection defense has two layers (M1)
The retrieval prompt asks the model to flag any chart text that tries to instruct it. A code scanner, `checks.scan_injection`, also looks for text addressed to automated reviewers. The report lists both and keeps their counts separate in the audit log, so the eval can tell whether the model caught the injection itself. A test confirms the scanner fires on every synthetic injection case and on no other case.

### B24. NOT_MET and CONFLICTING gaps always go to the ordering provider (M1)
If the gap-plan model names someone else as the supplier, code overrides it and logs the override. If the model skips a criterion that is not MET, code adds a default gap item. **Why:** this is D1, the physician resolves conflicts and failures, enforced in code rather than in the prompt.

### B25. Outcome scoring separates "exact" from "differs only via an acceptable alternate" (M1)
In the first Opus run, two cases had an indeterminate TB test as the only screen. Gold says INSUFFICIENT_EVIDENCE, with NOT_MET as an acceptable alternate. The agent said NOT_MET both times, which turned "gaps to close" into "needs physician". Every criterion was defensible, but the outcome did not match. The summary now counts these separately from wrong outcomes. They err toward more escalation, not less. **Settled from clinical practice (Kevin asked for this):** an indeterminate IGRA is a gap, not a failure. Indeterminate results are common in IBD patients on steroids or thiopurines, and usually reflect a low mitogen response rather than TB. Practice is to repeat the IGRA or do a TST. Only a repeat that is also indeterminate becomes a physician or TB-expert judgment, using chest imaging and risk factors. Gold is now INSUFFICIENT_EVIDENCE with no alternate, and the missing item is the repeat test. The assessment prompt (assess@v2) gains a general rule: an indeterminate, invalid or unreadable result means the test needs repeating. It is not written for this one case; the same rule covers any lab. Not yet modeled: a case with two indeterminate results, which should go to the physician.

### B26. Synthetic medication histories must be internally consistent (M1 fix)
The first Opus run marked PA-1042's anti-TNF history CONFLICTING. The generator had written "primary non-response after induction and 8 weeks of maintenance" for an infliximab course that ran 2 years. The model was right and the data was wrong. Each stop reason now carries a duration range that fits it. The fix reuses the same random draws, so the case mix is unchanged. This is the QA loop working as intended: a model disagreement with gold is read before it is scored as an error.

### B27. assess@v2: omission is not conflict (M1 fix)
In the re-run, PA-1042's practice medication list left out infliximab, which the outside records documented, and the outside records left out methotrexate. The model called both step-therapy criteria CONFLICTING. Leaving something out is not a contradiction: real medication lists are routinely incomplete. CONFLICTING now requires two documents that make incompatible statements about the deciding fact. The prompt version moved v1 to v2, and both files stay in `prompts/`. Retrieval inputs did not change, so the re-run reused cached retrieval calls and only re-ran assessment and the gap plan.

### B28. The second payer is built to differ where it matters (M2)
Calder Mutual (CM-RX-217, version 2026-07) differs from Northfield on every axis the spec names, and on two more:

| | Northfield | Calder Mutual |
|---|---|---|
| Prior therapy | conventional AND anti-TNF (ALL) | conventional OR any advanced therapy (ANY) |
| TB lookback | 12 months | 6 months |
| Disease activity | endoscopy or fecal calprotectin | endoscopy only |
| Weight recency for dosing | 30 days | 90 days |
| Preferred product | ustekinumab-aekn or -ttwe required | no product rule |
| Section numbering | 3.1 to 3.10 | B.1 to B.9 |

The policy is also written in a different house style. That tests whether extraction depends on Northfield's layout, or on criterion ids lining up, which they don't: alignment is by policy section. **Adding the payer changed no code in `agent/` except removing two hard-coded Northfield strings.** Those were the decision clock in intake, which now lives in the lookup table, and policy-section matching in the code checks, which is now normalized. Everything else is data: the policy text, the gold checklist, one row in `pa_lookup.yaml`, and one block in `policy_rules.yaml`.

### B29. Same chart, two payers, generated as twins (M2)
`synth.build --paired` writes each blueprint twice: PA-2001 for Northfield and PA-2501 for Calder. The charts differ only in their insurance lines, which a test enforces. Gold for the Calder twin comes from a small override table: `CALDER_STATUS` in `synth/label.py` lists only the chart states whose meaning changes under Calder. Any difference between the twins' gold answers therefore comes from the policies alone. In batch 2, the payers give different answers in 29 of 100 pairs. This is the spec's "same patient, two payers, different answer" case type, at scale.

### B30. Held-out evaluation (M2)
The assessment prompt was revised (v2) after reading the M1 sample. M1 scores on those same 15 cases therefore show only that the fixes work, not how well the agent generalizes. The M2 evaluation runs on batch 2, which no prompt was tuned on: 15 Northfield cases chosen to cover every case type and the rare settings, plus their 15 Calder twins.

### B31. A QA agent reviews every disagreement, and may blame the gold label (M2)
`evals/qa.py` makes one model call per criterion where the agent and gold disagree. It sees what the pipeline never does: the gold label, the generator's note on what it planted, and the full chart. Its verdict is one of `agent_error`, `gold_error` or `ambiguous`, with a root cause and where the fix belongs. **Why it may blame gold:** in M1 the model was right twice when gold was wrong or arguable (B25, B26). A QA step that assumes gold is always right would have sent those to prompt tuning and taught the agent to agree with a bug. The QA agent's verdicts are themselves model output, so a human reads `QA_REPORT.md` before acting.

### B32. Stale evidence of the right kind is NOT_MET; evidence of the wrong kind is INSUFFICIENT (M2 gold fix)
The first held-out run showed 6 outcomes that differed from gold only through an acceptable alternate. Five of them were a stale endoscopy, where gold said INSUFFICIENT_EVIDENCE and the agent said NOT_MET. Gold was inconsistent with itself: a stale TB screen was already NOT_MET, following the spec's own example ("TB screen is 14 months old against a 12-month window"). The rule is now applied to every criterion:
- the only evidence of the required kind is outside the window: NOT_MET (alternate INSUFFICIENT);
- the required kind of evidence is absent, or only a kind the policy excludes is present (CRP only; calprotectin under Calder): INSUFFICIENT_EVIDENCE (alternate NOT_MET);
- an indeterminate result: INSUFFICIENT_EVIDENCE, because the test needs repeating (B25).

**Guard against grading to the answer:** the change brings gold in line with a rule written before the run (spec 7.1). It does not copy the agent's answers. In the one wrong-kind case (calprotectin only, Calder), the agent said NOT_MET, and gold still says INSUFFICIENT.

### B33. QA agent finding: latent-TB treatment dated before its own diagnosis (M2 generator fix)
The QA agent reviewed all 4 criterion-level disagreements in the first held-out run. It returned `gold_error` for every one, naming the same cause: in `positive_with_plan` charts, the generator wrote a rifampin start date about 3 weeks before the positive IGRA and the chest X-ray that followed it. Opus had refused MET on that impossible timeline, as CONFLICTING twice and INSUFFICIENT twice. The generator now dates treatment after the X-ray and on or before the note that reports it. A test enforces the ordering for every synthetic case. The first-pass reports are kept in `docs/sample_runs/` as the before picture.

### B34. Gold applies the stale-evidence rule to what the chart contains (M2 gold fix)
After B32, two cases still differed from gold through an alternate. Both charts held an endoscopy older than 12 months: a `crp_only` chart whose older note reports "Last colonoscopy 2023-02 showed active disease", and a Calder calprotectin-only chart with an old distractor colonoscopy. Gold followed the planted state name and said INSUFFICIENT. B32's rule, applied to the chart, says NOT_MET, which is what the agent said. `synth/label.py` now checks the rendered chart for an out-of-window endoscopy. This is the third gold change made after reading disagreements on the same cases, so the M2 set is no longer blind. See EVAL_REPORT, "Read of the results".

### B35. The to-do list says what would satisfy the policy, never what to do clinically (M3)
Kevin asked for the most logical next step on stale or missing evidence. Statuses stay as the spec defines them: stale evidence is NOT_MET and goes to the physician. Each gap item now also carries `would_satisfy`, which states what the policy accepts, with the date window computed. An example: "Policy 3.6 accepts a negative IGRA or TST dated on or after 2025-11-18." That is a fact about the policy, so it stays inside D2: the agent never recommends care. The physician decides whether to order the test. The prompt version moved gaps v1 to v2. It is null when no document could fix the criterion, for example mild disease.

### B36. The drafter sees only verified quotes; the verifier sees only the packet and the chart (M3)
- **Step 8 (draft)** gets the request, the checklist and the evidence that passed step 6. It does not get the raw chart, so it cannot cite a fact nobody checked. Under ANY logic, an unmet branch is left out entirely; a test caught this on Calder cases.
- Code re-checks every citation in the form and the letter: verbatim in the document, or in the request, and from the same patient.
- **Step 9 (verify)** is a separate call with a different prompt. It sees the request, the packet and the full chart, but not the drafter's prompt, the assessments or the retrieval passages, so it cannot inherit their mistakes. An unchecked claim counts as unsupported.
- Form fields come from the checklist: one per MET criterion, plus identity and request fields. A new policy or specialty therefore gets the right form with no code change.

### B37. Sign-off rules are code, not UI convention (M3)
`agent/submit.py` enforces these rules, and the Streamlit UI only displays them:
- every criterion needs a decision, and an edit needs a reason code;
- a physician signs whenever there is a letter, or any NOT_MET or CONFLICTING criterion (D1);
- submission requires every criterion MET after review, no code citation issue, and a verifier pass. A verifier flag can be overridden only with a written reason. A code citation issue can never be overridden.

Every decision and the sign-off go to `review.jsonl` and the case audit log. Mock submission writes one payload per benefit rail: a portal request for the medical benefit, an ePA request for the pharmacy benefit.

### B38. Data gaps found by the blind run, to fix before the next cycle (M3)
1. **Prescriber specialty is only in document metadata.** Synthetic and hand-built notes name "Gastroenterology" only in the header `author` field. Quotes must come from document text, so a strict model cannot prove C3. Real notes carry a signature block ("Electronically signed by A. Rivera, MD, Gastroenterology"). The generator and the hand cases should add one, and gold C3 should cite it.
2. **"Weight down 3 kg" is random filler.** It can contradict the two recorded weights (PA-3091), and Opus correctly called that CONFLICTING. It should be removed or tied to the actual weights.

These are recorded but not yet applied. Regenerating would change the charts under the archived blind runs, and the reports re-check every quote against the charts on disk. Apply them at the start of the next evaluation cycle, then re-run.

**Applied after M4 (B43):** the generator now writes a signature block into every GI note, and gold C3 cites it. The random weight sentence is gone. The three hand-built IBD charts gained signature lines, which only appended text, so every archived quote still checks. Batches 1 to 3 were not regenerated, so the archived runs stay reproducible; the next batch built gets the fix. The Sonnet and Haiku re-run on fixed data is still to do (about 1.5M tokens for 30 cases each).

### B39. Policy extraction is a once-per-version job for the strongest model, approved by a human (M3)
In the blind run, Haiku mis-split Northfield 3.10 and Sonnet left Calder B.5 unsplit. Extraction runs once per policy version, not once per case, so its cost is negligible, while an error in it touches every case under that policy. The production design: the strongest model extracts, a person compares the result to the policy (`compare_to_gold` already shows the differences), and approved checklists are pinned by version. The per-case model is chosen separately. The scorer now judges an unsplit parent at the parent level, so a coarser checklist is not charged with false METs it never claimed.

### B40. The verifier caught 10 of 10 seeded errors (M3)
Each seeded error kept a verbatim citation, so only the verifier could catch it. The five types were a changed dose, a shifted date, a flipped TB result, the wrong drug, and an invented vedolizumab trial. They were planted in two real Opus-drafted packets, and Opus as verifier flagged every one on the exact claim, with no false alarms on the clean packets. Earlier, on a real draft, it caught one genuine problem: a transition sentence marked factual, with an irrelevant citation attached. That led to drafter prompt v2. Ten seeds is a demo, not a measurement. The production version is a standing seeded-error set run on every prompt or model change.

### B41. Reuse test: a cardiology drug was mostly configuration, with two small code changes (M4)
Spec section 10 asked whether "new drug, new payer, new specialty" is configuration or engineering. The test added a PCSK9 inhibitor (evolocumab) under a new Calder Mutual policy, CM-RX-305, for a fictional cardiology practice, with three hand-built cases. The cases were one clean ASCVD case, one HeFH case with weak statin-intolerance documentation, and one stroke case whose on-therapy LDL-C is below the policy threshold.

**What was configuration only:**
- the policy prose and gold checklist;
- one row in `pa_lookup.yaml`. Evolocumab has a single pharmacy-benefit phase, not ustekinumab's two;
- one row in `policy_rules.yaml`: age 18 and a 3-month LDL-C lookback.

No schema, prompt, document type or UI change was needed. Extraction found 9 of 9 gold criteria, including the ANY logic on statin therapy. The only difference was the phase name, `self_administered_sc` instead of `sc_injection`, which routing ignores because it reads the lookup table.

**What needed code, and why:**
1. **The copy-forward date check misfired.** Step 6 flags a recent note that quotes an older date, because in IBD charts that usually means a TB result copied forward from an old note. In PA-0101 the quote "LDL-C 98 mg/dL on atorvastatin 80 mg and ezetimibe 10 mg (ezetimibe since 06/02/2026)" carries a therapy start date, not a result date. The check downgraded a true MET to INSUFFICIENT. This was a safe failure, but a wrong one. Fix: the criterion now passes when at least one cited passage is inside the window and carries no older date. A note that quotes only an old result is still flagged. A test covers both cases. This is the lesson of the reuse test: a heuristic written for one specialty's failure mode encoded that specialty's assumptions.
2. **Gap items for an unused either/or branch.** In PA-0103, statin therapy was met through branch (a), yet the to-do list still asked the doctor about branch (b). Leaves under a parent that is already MET no longer get gap items. This was latent in the Calder IBD policy too; the IBD cases never surfaced it.

**What still needs code for full parity:**
- **Dose.** The dose check is ustekinumab-specific. Evolocumab dosing (140 mg every 2 weeks or 420 mg monthly) is judged by the model alone.
- **Numeric lab thresholds.** LDL-C against 70 or 100 mg/dL is not checked by code. A generic "lab value against a threshold" check, driven by the rules table, would cover this and calprotectin alike.
- **Prompt wording.** `gaps@v2` still says "treating gastroenterologist". It did no harm here, but it should say "treating prescriber".

**Results** (Opus, after the two fixes; `docs/eval_runs/m4-reuse-opus/`): 0 false METs, 2 of 3 exact outcomes, and 26 of 27 criteria correct. PA-0101 reached READY, and the verifier confirmed all 32 claims in its packet.

**The run also found two errors in my own gold labels.** The agent was right both times:
- **PA-0103.** B.4 requires LDL-C to remain at or above the threshold on ezetimibe. 64 mg/dL is below 70, so B.4 is NOT_MET, not MET.
- **PA-0102.** The chart's Dutch Lipid Clinic score of 8 counts 4 points for corneal arcus "before age 45". The only arcus finding is from an exam at age 54, so the diagnosis is not supported as written.

Both gold labels were corrected with a note. The one remaining miss is real: in PA-0102 the agent called the LDL-C criterion NOT_MET because the patient is not on a statin. That makes B.2 depend on whether B.3 is resolved. The policy couples the two criteria, and the agent treated an unresolved dependency as a failure. It over-escalated to a physician, which is not a false MET. Fixed by assess@v3 (B43).

### B42. One IBD drug instead of four (M0 to M2)
The brief lists adalimumab, infliximab, ustekinumab and vedolizumab. The build covers ustekinumab only, across two payers, plus evolocumab for the reuse test. Kevin wanted a small example to talk through, not a full build. Ustekinumab was the best single choice, for three reasons:
- **Both benefit rails.** It exercises split routing: IV induction on the medical benefit, SC maintenance on the pharmacy benefit.
- **The hardest code check.** It has weight-tiered dosing.
- **Step-therapy and preferred-product rules.** Payers differ on these.

Adding the other three drugs is configuration work (B41), plus a dose table for each.

### B43. assess@v3: judge a coupled criterion on what it measures, plus the B38 data fixes (M5 follow-up)
**The problem.** Some policy criteria point at another criterion. Calder B.2 asks for an LDL-C "on the B.3 and B.4 therapy". In PA-0102 the patient is on ezetimibe with no statin, and Opus failed B.2 because B.3 (statin therapy) failed. That double-counts one problem: B.3 already carries it, and code combines the statuses.

**The fix.** assess@v3 adds one rule. A criterion that refers to another criterion's therapy is judged on what it measures, against the therapy the chart shows. It is never NOT_MET because the other criterion fails. If the dependency truly decides it and the chart doesn't settle it, it is INSUFFICIENT_EVIDENCE. This is a prompt rule, not a schema field. A "depends on" field in the checklist would be more explicit, but one rule fixed the miss without changing extraction.

**Results** (Opus, assess@v3, about 264k tokens in all):

| Run | Cases | False MET | Criteria | Outcome |
|---|---|---|---|---|
| Reuse test (`m5-reuse-opus-v3`) | 3 | 0 | 27/27 (was 26/27) | 2 exact, 1 acceptable alternate, 0 wrong (was 1 wrong) |
| Hand-built IBD (`m5-ibd-hand-v3`) | 3 | 0 | 33/33 | 3/3 exact. PA-0001's packet: 44 of 44 claims verified |
| Blind regression (`m5-blind-regress-v3`) | 6 | 0 | 63/63 | 5 exact, 1 acceptable alternate. Same as v2 on these cases |

- **PA-0102 now gets B.2 right.** Its outcome is still NEEDS_PHYSICIAN rather than gold GAPS_TO_CLOSE, because Opus calls the second-statin branch NOT_MET, an acceptable alternate. With only one statin documented, that is defensible either way.
- **The regression set was chosen to stress the change.** It is three payer pairs (PA-3006, PA-3018, PA-3045 and their Calder twins), the blind cases with the most NOT_MET criteria. That is where a rule softening NOT_MET would do harm. None changed.
- **The B38 signature block worked.** In PA-0001, C3 is now proven by the quote "Electronically signed by Dr. A. Rivera, Gastroenterology, 10/28/2026", not by the document header.
- **Caveat.** Twelve cases is a spot check, not a full re-run of the 30-case held-out set. The headline numbers in the README are from assess@v2.

**One reliability fix.** PA-0102 failed twice, in M4 and here, with "No such file or directory: 'claude'". The binary disappears briefly while Claude Code updates itself. The backend now retries that error with the same backoff as a rate limit.
