**Bottom line.** On 30 blind cases, none of the three models produced a false MET, a non-verbatim quote, or a routing error. The safety design holds even on the smallest model. The models differ in how often they escalate cases that were actually fine: Opus 1 of 282 MET criteria, Sonnet 34, Haiku 41. Escalation is safe but costs reviewer time. Per case, Haiku costs about 4% of Opus at list price, and Sonnet about 40%.

**Opus made no clear agent errors on the blind set.** Of its 5 non-exact outcomes, 4 sit on the stale-endoscopy boundary, where gold accepts either answer (B32). The fifth (PA-3091) is a generator contradiction: a note says "weight down 3 kg" while the recorded weight went up 2.1 kg, right at the 85 kg dosing cutoff. Opus flagged it as CONFLICTING instead of guessing, which is the behavior we want. That one goes on the generator fix list (B38).

**Where the smaller models lose accuracy, and why:**
1. **Prescriber specialty (C3), most of Sonnet's and Haiku's misses.** In the synthetic notes, "Gastroenterology" appears only in the document header (`author`), never in quotable text. Sonnet and Haiku refused MET without a quote showing the specialty. That is arguably the more correct reading of D2. Opus accepted the request's "Dr. A. Rivera, Gastroenterology". This is a data realism gap, since real notes carry a signature block. Fix the data, not the models (B38).
2. **Policy extraction.** Haiku split Northfield 3.10 into (a) and (b) with ANY and lost the "requested product is preferred" branch, so every Northfield case looked like a non-preferred request. Sonnet kept Calder B.5 as one criterion. That is harmless after a scoring fix: an unsplit parent is now scored at the parent, which removed 3 false METs the scorer had invented. **Extraction runs once per policy version, so in production it should use the strongest model and be approved by a human before any case runs** (B39). Per-case steps are where model cost matters.
3. **Retrieval robustness.** On one Sonnet case (PA-3006), retrieval returned garbled quotes. Code dropped them, and every criterion became INSUFFICIENT. That is the safe failure mode, by design.

**What to run next, in order:**
1. Fix the two data gaps (signature lines, the weight sentence) and regenerate.
2. Re-run Sonnet and Haiku with the Opus-extracted, human-approved checklist. That isolates per-case quality, which is the actual production choice.
3. If Haiku or Sonnet then matches Opus within 5 points on outcomes, it becomes the candidate for the blinded reviewer study. If not, Opus stays, and its cost (about $0.29 per case at list price) is weighed against reviewer minutes saved.

The sample has no injection case; batch 3 drew none in the stratified set. The M1 and M2 runs covered injection, with 3 of 3 flagged.
