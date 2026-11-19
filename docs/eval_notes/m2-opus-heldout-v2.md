**Headline.** On 30 cases that no prompt was tuned on (15 Northfield cases and their 15 Calder twins), Opus made no false MET and quoted 509 of 509 passages word for word. 315 of 315 criterion judgments were defensible, and 29 of 30 packet outcomes were exact. Every spec gate passes. The remaining outcome difference (PA-2063) sits on a boundary the gold labels allow either way: the only endoscopy is years old, so it is stale under the B32 rule. The agent called that a gap to close rather than a failure.

**What the second payer showed.** Calder Mutual needed no agent code, only data (B28). Extraction found all 10 of its criteria, including the ANY logic on prior therapy that Northfield lacks. The one extraction difference is harmless: the model gave Calder's 90-day weight rule a 3-month lookback, and the code checks use the reviewed rules table either way. The agent judged the same chart differently for each payer, and saw correctly whether the two answers should differ in 14 of 15 pairs.

**How the numbers moved, and why that needs care.** The first pass on this set scored 21 of 30 exact outcomes. The fixes were all to synthetic data or gold labels, never to the agent's prompts:
1. The QA agent found that the generator dated latent-TB treatment before its own positive test. This was 4 criterion "failures" where the agent was right (B33).
2. Gold labeled stale endoscopies as INSUFFICIENT but stale TB screens as NOT_MET. The spec rule makes both NOT_MET (B32).
3. Gold applied that rule to the planted state name, not to what the chart contained. Two charts had an old endoscopy the state name did not mention (B34).

Each fix follows a rule written before the run. They were found by reading disagreements, though, so this set is no longer fully blind. **The next run should be a fresh batch that nobody has looked at.** That is the true held-out number.

**Since this run.** The blind confirmation run on a fresh batch, on Opus, Sonnet and Haiku, is in `MODEL_COMPARISON.md`. Every model kept zero false METs; Opus had 25 of 30 exact outcomes, with no clear agent error. M3 added drafting, the verifier (10 of 10 seeded errors caught) and the reviewer UI. M4, the cardiology reuse test, is in `DECISIONS.md` B41.

**Next three things to fix or build.**
1. **Data fixes, then re-run the cheaper models on the approved checklist.** Apply B38: a signature line that states the prescriber's specialty, and remove the random weight sentence. Re-run Sonnet and Haiku with Opus's human-approved checklist (B39). That isolates the per-case model choice, which decides most of the cost.
2. **Coupled criteria and computed thresholds.**
   - Let assessment mark a criterion as depending on another, instead of failing it. This was the one real miss in the reuse test (B41).
   - Move numeric lab thresholds (LDL-C, calprotectin against the reference range) into code checks driven by the rules table, as age and dose already are.
3. **Longer and messier charts.** Retrieval is one call per case, which works for 7 to 12 documents. Add chunked retrieval and test it on 40+ document charts with real-world OCR noise. Add the coverage gaps found earlier: repeated indeterminate TB results, and contradictory dates of birth.
