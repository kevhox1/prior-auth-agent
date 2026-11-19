# QA report: m2-opus-heldout

This report comes from the QA agent in `evals/qa.py` (prompt `qa_review@v1`). It reviewed every disagreement between the agent and gold. It sees the gold label and the full chart, which the agent never does. It decides whether the agent or the gold label is wrong, then names a root cause and where the fix belongs. Its verdicts are a model's judgment: a human reads them before acting on them.

**4 disagreements.** Verdicts: gold_error 4.

Root causes: none 4.

Where fixes belong: generator 4.

## Findings

### PA-2054 (northfield) C6 (policy 3.6): agent CONFLICTING, gold MET

- Verdict: **gold_error**. Root cause: none. Fix target: generator.
- Planted state: `positive_with_plan`. Retrieval surfaced the gold evidence: yes.
- The generator planted 'positive_with_plan', but the GI note (2026-11-09) dates the LTBI rifampin start to 2026-09-12. That is before the positive QuantiFERON (2026-10-04) and before the chest X-ray (2026-10-07), whose indication is 'Positive interferon-gamma release assay'. No earlier positive TB test exists in the chart, so the chart has an impossible sequence (treatment before diagnosis and before active TB was excluded). The agent's flag is reasonable, and gold MET only holds if that inconsistency is ignored.
- Suggested fix: In the generator's positive_with_plan template, add a validation step: LTBI treatment start date >= max(IGRA collection date, chest imaging date) and <= the note date. Regenerate the chart if the check fails. Regenerate PA-2054 with a start date such as 2026-10-12.

### PA-2070 (northfield) C6 (policy 3.6): agent CONFLICTING, gold MET

- Verdict: **gold_error**. Root cause: none. Fix target: generator.
- Planted state: `positive_with_plan`. Retrieval surfaced the gold evidence: yes.
- The generator meant to plant a clean 'positive_with_plan' state. Instead, the GI note dates the rifampin start to 2026-09-10, which is before the positive QuantiFERON (collected 2026-10-04) and before the chest x-ray done for that result (2026-10-07), and the chart has no earlier TB test. Policy 3.6 does not literally require any order, so MET holds on the wording. But a treatment start that comes before its diagnosis is an unintended inconsistency the agent reasonably flagged, even though CONFLICTING (two documents disagreeing) is not quite the right label.
- Suggested fix: In the positive_with_plan template, set the latent TB treatment start date to a date after both the IGRA collection date and the chest imaging date (for example, imaging date + 3 to 14 days). Add a generator check that rejects any chart where a treatment start date comes before the diagnostic test it depends on.

### PA-2554 (calder) C6 (policy B.6): agent INSUFFICIENT_EVIDENCE, gold MET

- Verdict: **gold_error**. Root cause: none. Fix target: generator.
- Planted state: `positive_with_plan`. Retrieval surfaced the gold evidence: yes.
- The generator meant to create a positive_with_plan scenario, but it wrote the rifampin start date (2026-09-12) before both the positive QuantiFERON (2026-10-04) and the chest X-ray that ruled out active TB (2026-10-07). That order is clinically implausible, and nothing else in the chart explains it. The agent flagged this real contradiction correctly rather than misreading anything, so the case is defective test data, not a valid measure of the agent.
- Suggested fix: In the generator's positive_with_plan template, set the LTBI treatment start date after both the IGRA collection date and the chest X-ray date (e.g., 3-14 days after the X-ray and on or before the request date). Add a generator validation check that rejects charts where treatment starts before the screening test or the X-ray.

### PA-2570 (calder) C6 (policy B.6): agent INSUFFICIENT_EVIDENCE, gold MET

- Verdict: **gold_error**. Root cause: none. Fix target: generator.
- Planted state: `positive_with_plan`. Retrieval surfaced the gold evidence: yes.
- The GI note dated 2026-11-04 says 'rifampin daily for 4 months, started 2026-09-10.' That is before the positive QuantiFERON (2026-10-04) and the chest X-ray (2026-10-07), and the X-ray's stated indication is that positive test. The chart has no earlier TB screen, so the generator wrote an LTBI start date that contradicts its own 'positive_with_plan' timeline. The agent correctly flagged the gap and named a specific missing item, so its INSUFFICIENT_EVIDENCE call is defensible and the planted MET label is not a clean test.
- Suggested fix: In the positive_with_plan generator template, set the LTBI treatment start date to after both the IGRA collection date and the chest X-ray date, and on or before the note date. Add a generator check that rejects any chart whose treatment start date is earlier than the screening date or the X-ray date.

