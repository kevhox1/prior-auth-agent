# Model comparison

Same 30 blind cases for every model: batch 3, which nobody looked at before these runs. It is 15 Northfield cases chosen to cover every case type and rare setting, plus their Calder twins with the same chart. Same prompts and same code for each model. Runs go through Claude Code; dollar figures are list-price equivalents for comparison.

## Read of the results

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

## Numbers

| | claude-opus-5-5 | claude-sonnet-5-5 | claude-haiku-5-5 |
|---|---|---|---|
| Cases completed | 30 | 30 | 30 |
| **False MET (gate 0)** | **0** | **0** | **0** |
| Citations verbatim (gate 100%) | 491/491 (100%) | 390/390 (100%) | 457/457 (100%) |
| Routing (gate 100%) | 30/30 (100%) | 30/30 (100%) | 30/30 (100%) |
| Injection flagged by the model itself | n/a | n/a | n/a |
| Packet outcome exact | 25/30 (83%) | 23/30 (77%) | 20/30 (67%) |
| Outcome differs only via acceptable alternate | 4 | 1 | 0 |
| Criteria correct | 314/315 (100%) | 280/315 (89%) | 274/315 (87%) |
| INSUFFICIENT recall | 18/18 (100%) | 15/15 (100%) | 18/18 (100%) |
| NOT_MET recall | 11/11 (100%) | 11/11 (100%) | 11/11 (100%) |
| Over-escalation (gold MET, agent not) | 1/282 (0%) | 34/285 (12%) | 41/282 (15%) |
| MET downgraded by code checks | 0 | 0 | 0 |
| Payer difference captured (pairs) | 10/15 (67%) | 9/15 (60%) | 11/15 (73%) |
| Mean model seconds per fresh case | 65 | 36 | 64 |
| Mean tokens per fresh case | 30,897 | 24,861 | 38,680 |
| List-price $ per fresh case | $0.285 | $0.114 | $0.011 |

## Decision rule

- `claude-opus-5-5`: gates PASS; outcome exact 25/30; $0.285 per case.
- `claude-sonnet-5-5`: gates PASS; outcome exact 23/30; $0.114 per case.
- `claude-haiku-5-5`: gates PASS; outcome exact 20/30; $0.011 per case.

**Offline pick: `claude-opus-5-5`.** It is the cheapest model that passes every gate and comes within 5 points of the best outcome accuracy, the spec's non-inferiority margin. This is 30 cases, too few to separate models finely: a 5-point difference needs hundreds of cases per arm (COST_EFFECTIVENESS_SPEC section 6). Treat it as the candidate for the blinded reviewer study and pilot, not the final answer.

Not measured offline: patient-experience guardrails (time to therapy, contacts, opt-outs) and blinded reviewer preference. Both need the pilot described in COST_EFFECTIVENESS_SPEC.

### Failures: `claude-opus-5-5`

| Case | Payer | Criterion | Gold | Agent | Category | Retrieval had gold evidence |
|---|---|---|---|---|---|---|
| PA-3091 | northfield | C9 (3.9) | MET | CONFLICTING | over_escalation (gold MET) | yes |

### Failures: `claude-sonnet-5-5`

| Case | Payer | Criterion | Gold | Agent | Category | Retrieval had gold evidence |
|---|---|---|---|---|---|---|
| PA-3004 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3006 | northfield | C1 (3.1) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C2 (3.2) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C4 (3.4) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C5a (3.5(a)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C5b (3.5(b)) | CONFLICTING | INSUFFICIENT_EVIDENCE | under_escalation (said INSUFFICIENT, gold CONFLICTING) | no |
| PA-3006 | northfield | C6 (3.6) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C7 (3.7) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C8 (3.8) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C9 (3.9) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3006 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | no |
| PA-3007 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3018 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3034 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3041 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3045 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3091 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3092 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3093 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3096 | northfield | C3 (3.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3506 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3507 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3518 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3534 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3540 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3541 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3545 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3550 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3580 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3590 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3591 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3592 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3593 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3596 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |

### Failures: `claude-haiku-5-5`

| Case | Payer | Criterion | Gold | Agent | Category | Retrieval had gold evidence |
|---|---|---|---|---|---|---|
| PA-3004 | northfield | C5a (3.5(a)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3004 | northfield | C5b (3.5(b)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3004 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3006 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3007 | northfield | C10 (3.10) | MET | NOT_MET | over_escalation (gold MET) | yes |
| PA-3018 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3034 | northfield | C5a (3.5(a)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3034 | northfield | C5b (3.5(b)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3034 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3040 | northfield | C5b (3.5(b)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3040 | northfield | C10 (3.10) | MET | NOT_MET | over_escalation (gold MET) | yes |
| PA-3041 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3045 | northfield | C5b (3.5(b)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3045 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3050 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3080 | northfield | C5b (3.5(b)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3080 | northfield | C8 (3.8) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3080 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3090 | northfield | C5a (3.5(a)) | MET | CONFLICTING | over_escalation (gold MET) | yes |
| PA-3090 | northfield | C5b (3.5(b)) | MET | CONFLICTING | over_escalation (gold MET) | yes |
| PA-3090 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3091 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3092 | northfield | C5a (3.5(a)) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3092 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3093 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3096 | northfield | C10 (3.10) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3504 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3506 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3507 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3518 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3534 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3540 | calder | C7 (B.7) | MET | CONFLICTING | over_escalation (gold MET) | yes |
| PA-3541 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3545 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3550 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3580 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3590 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3591 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3592 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3593 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
| PA-3596 | calder | C3 (B.3) | MET | INSUFFICIENT_EVIDENCE | over_escalation (gold MET) | yes |
