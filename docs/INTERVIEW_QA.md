# Interview Q&A

Fifteen questions a product leader at a clinical AI company would likely ask about this build, with direct answers drawn from the repo. Numbers come from the eval reports in `docs/`. All data is synthetic.

---

**1. What does it do, in one breath?**
It takes a prior authorization request, the patient's chart and the payer's policy. It turns the policy into a checklist and proves or disproves each criterion with verbatim quotes from the chart. Then it either drafts a cited packet, lists exactly what is missing and who can supply it, or sends the case to a physician. A human signs before anything leaves. It never submits, never changes the order and never suggests a drug.

**2. Why is the review line where it is? Nurse for every packet, physician only for letters and failed criteria (D1).**
- **The work is mostly evidence assembly.** Nurses and PA specialists already do it in most practices. A physician reviewing every routine packet would spend scarce time confirming quotes a nurse can confirm.
- **Two things need a physician:** the letter goes out under their name, and a failed or conflicting criterion is a clinical decision (wait, appeal, or choose another path).
- **The rules are code, not convention.** The sign-off button cannot be enabled any other way (`agent/submit.py`, B37).
- **What would move the line:** a practice where nurses sign routine letters under a standing protocol. The role check is configurable for that. I'd want a clinician to confirm the split; it is open question 1 in the README.

**3. Why is the release gate zero false METs rather than a tolerance?**
A false MET means the agent claims the patient meets a rule they don't, in a packet signed by a doctor. That is the one error that turns the agent from "slow" into "wrong in the payer's eyes". Every other error costs time: a human catches an over-escalation in seconds. So the system is built to fail in one direction:
- the model may not say MET without a quote;
- code can downgrade a MET but never grant one;
- the drafter only sees verified quotes;
- an independent verifier checks the draft.

Across every Opus run (75 eval cases, 3 reuse cases and the 12-case B43 spot check) and the Sonnet and Haiku blind runs, false METs are 0.

**4. How do you know it works? What did you actually measure?**
- **Held-out set** (30 cases, no prompt tuned on them): 0 false METs, 509 of 509 quotes verbatim, 315 of 315 criteria defensible, 29 of 30 outcomes exact.
- **Then I spoiled that set.** Reading its disagreements exposed gold-label and generator errors, so I generated a fresh blind batch. On it, Opus had 25 of 30 exact outcomes. Four of the five misses sit on a boundary the gold labels allow either way. The fifth is a contradiction my generator introduced, and Opus correctly flagged it.
- **Verifier:** it caught 10 of 10 planted errors in real packets, with no false alarms.
- **Limits:** these are small samples on synthetic data. They show the design holds; they don't measure production accuracy. That needs the shadow period in `PRODUCTION_PLAN.md`.

**5. Synthetic data is easy to game. Why should I trust these numbers?**
Partly, you shouldn't, and I tried to make that visible.
- **How the labels are made:** code decides each case's gold labels from a blueprint, and models only write the prose (B14), so a model can't leak the answer into the chart.
- **The cases are built to break it:** about one in four is clean (D6). The rest have buried evidence, stale results, copied-forward values, OCR-style faxes, wrong-channel requests and planted prompt injections.
- **Payer twins:** the same chart under two payers tests whether the agent reads the policy, not the chart's tone.
- **A QA agent can blame the answer key:** it reviews every disagreement and found four of my generator bugs (B33).
- **What it can't fix:** synthetic charts are realistic in what they include and probably unrealistic in what they omit. That's open question 6, and why the next step is real de-identified cases.

**6. What breaks first at scale?**
1. **Policy drift.** A payer updates its policy and the checklist is stale. Every packet is then confidently correct against old rules. The version is pinned in three places and intake refuses a mismatch, but someone has to notice the change. Production needs a policy-page watcher and a review step (`PRODUCTION_PLAN.md` section 4).
2. **Long, messy charts.** Retrieval is one call per case, fine for 7 to 12 documents. A real chart with 40 documents and bad fax OCR needs chunked retrieval and will produce more "missed evidence" edits.
3. **The medical-benefit submission rail.** Portals differ by payer and break often. I would keep a human submitting from the packet there until volume justifies automation.

**7. What would a clinician object to?**
- **"It doesn't know what payers actually accept."** Policies say "objective evidence of disease activity". Payer reviewers have habits the document doesn't state. Only denial data teaches that.
- **"Indeterminate TB isn't a paperwork gap."** I settled that one on practice: an indeterminate test is repeated, so it is INSUFFICIENT and names the repeat. A clinician should confirm it.
- **"The letter is a checklist, not an argument."** It is deliberately one cited fact per sentence, which reviewers can verify but which reads mechanically. Physicians may want a short clinical summary up top. Open question 4 asks what reviewers distrust in drafted letters.
- **"Who's liable?"** The physician who signs. That's why the drafter can only use verified facts and the verifier shows its flags in red.

**8. What would you cut if you had half the time?**
- **The Streamlit polish.** The sign-off rules matter; the layout doesn't.
- **The second payer's full policy,** keeping only the twin mechanism.
- **The QA agent.**

I would not cut the code checks, the verifier, or the blind run. Those are what make the numbers mean anything.

**9. What would you build next?**
In order:
1. **Re-run the cheaper models on the fixed data and the approved checklist.** The data fixes are in (B43); the re-run is about 1.5M tokens. This isolates the real per-case model choice, which decides most of the cost.
2. **Numeric lab thresholds checked in code.** Coupled criteria, the one real miss in the reuse test, are already fixed (B43).
3. **Chunked retrieval for long charts.**

After those, renewals (v2 scope) are the obvious product expansion. They are the same machinery with response-to-therapy evidence.

**10. Opus, Sonnet or Haiku?**
All three passed the safety gates on the blind set. They differ in how often they flag fine criteria anyway: 1, 34 and 41 of 282. List price per case was about $0.29, $0.11 and $0.01. The decision rule (`COST_EFFECTIVENESS_SPEC.md`) is: gates first, then quality within 5 points of the best, then cost. That picks Opus offline today. But most of the cheaper models' misses came from my data (the prescriber's specialty appeared only in note metadata) and from their policy extraction. So the production design is:
- the strongest model extracts each policy once per version;
- a person approves the extracted checklist;
- the per-case model is chosen separately, by blinded reviewer grading and then a pilot.

Thirty cases can't separate models finely.

**11. How do you handle prompt injection in chart text?**
The chart is wrapped and labeled as data in every prompt. The retrieval model is asked to flag any text addressed to an automated reviewer, and a regex scan backs it up (B23). The UI shows flagged text in a red box and asks the reviewer to check where it came from. Earlier runs caught 3 of 3 planted injections. The blind sample happened to contain none, which I report rather than hide.

**12. Is a new drug or specialty configuration or engineering?**
Mostly configuration. That was the point of the reuse test (B41). Adding a cardiology drug (evolocumab) under a new policy needed a policy file, one lookup row and one rules row, with no schema, prompt or UI change. It also needed two small code fixes:
- **A date check that encoded an IBD habit.** "A recent note quoting an old date" usually means a copied-forward TB result. In cardiology it was a drug start date.
- **A to-do item for an either/or branch that didn't matter.**

The one real miss, a criterion failed because a different criterion failed, was then fixed with a single prompt rule and spot-checked on 12 cases (B43). Dose checks and numeric lab thresholds are still drug-specific code. The honest answer is "configuration, with about a day of engineering per new specialty, mostly in code checks."

**13. How would you measure success in production?**
Weekly:
- first-pass approval rate by payer and drug;
- denial reasons mapped back to criteria (a denial on a criterion the agent called MET is an incident);
- reviewer edit rate by reason code;
- turnaround from order to submission;
- physician minutes per case.

Patient outcomes such as time to first dose are guardrails, not optimization targets (B16). Saving staff time by delaying a patient's therapy would be a failure.

**14. What did you get wrong along the way?**
Several things, all logged:
- **The first prompt treated silence as conflict** and over-escalated (B27).
- **My gold labels were inconsistent about stale evidence** (B32, B34).
- **My scorer invented three Sonnet false METs** by comparing a merged parent with a failed branch (B39).
- **The reuse test found two wrong gold labels of mine.** In both, the agent had read the policy more carefully than I did (B41).

The pattern: the most valuable debugging was reading disagreements with the possibility that the answer key was wrong.

**15. Where does a human stay in the loop, and why not automate them out?**
At three points:
- approving each policy checklist once per version;
- reviewing each criterion, with reason codes on edits;
- signing.

The reason codes are the learning signal: they tell you whether the agent misses evidence, picks the wrong evidence, or reaches the wrong status. Removing the human removes that signal and moves liability onto a system that can't hold it. The aim is to make the human's review fast: click a quote, see it highlighted in the source, approve. It is not to make the review disappear.
