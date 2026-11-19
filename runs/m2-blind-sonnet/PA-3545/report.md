# PA-3545: ustekinumab-aekn for PT-3545

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-11-06 states moderately to severely active ileocolonic Crohn's disease. This is a prescriber statement in the clinical record. (confidence 0.96)

- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy on file is dated 2025-04-18, about 19 months before the request, so it is outside the 12-month window. The 2026 CRP is a lab marker and does not satisfy the direct-visualization requirement. (confidence 0.80)

- `PT-3545/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3545/labs-2026-10-03` (2026-10-03): "C-reactive protein                    31.2 mg/L     <5.0"

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No passage provided states the prescriber's specialty or documents a gastroenterology consultation. The request lists Gastroenterology, but no chart passage confirms it. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (gastroenterologist) or a gastroenterology consultation note

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Born 02/21/1966, the member is 60 on the request date of 2026-11-18, which is over 18. (confidence 0.98)

- `PT-3545/demographics-2026-04-15` (2026-04-15): "Date of birth: 02/21/1966"
- Code checks: age 60 on 2026-11-18 from DOB 1966-02-21

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Adalimumab was used 12/2023 to 05/2026 and stopped for intolerance. This gives the drug, the dates and the reason, which satisfies the biologic pathway. Mercaptopurine was also stopped for inadequate response. (confidence 0.96)

- `PT-3545/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON was resulted 2026-10-03, within 6 months of the request. The 2023 QuantiFERON mentioned in a note is older and not relied on. (confidence 0.95)

- `PT-3545/labs-2026-10-03` (2026-10-03): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented as nonreactive. No reactive result, so no prophylaxis plan is needed. (confidence 0.96)

- `PT-3545/labs-2026-10-03` (2026-10-03): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3545/labs-2026-10-03` (2026-10-03): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The medication history lists no current biologic, JAK inhibitor or S1P modulator. The prior adalimumab ended 05/2026, so there is no overlap. (confidence 0.93)

- `PT-3545/medication-history-2026-11-04` (2026-11-04): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3545/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg was recorded 2026-11-06, within 90 days of the request. The 260 mg IV dose matches the tier for up to and including 55 kg, and the maintenance regimen is 90 mg SC every 8 weeks starting 8 weeks after the infusion. (confidence 0.95)

- `PT-3545/gi-note-2026-11-06` (2026-11-06): "1. Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Weight 55.0 kg."
- Code checks: weight 55.0 kg (2026-11-06) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C2**: Direct visualization of active inflammation within 12 months (who: ordering_provider)
  > PA-3545 (PT-3545), criterion C2 (policy B.2): the only endoscopy on file is the colonoscopy dated 2025-04-18, which is about 19 months before the request date and outside the 12-month window. The CRP of 31.2 mg/L (2026-10-03) is a lab marker and cannot satisfy this criterion alone. Please review and advise whether a more recent ileocolonoscopy, colonoscopy or flexible sigmoidoscopy exists or how you wish to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers (CRP, ESR, fecal calprotectin) and cross-sectional imaging do not satisfy it.
- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consult note (who: practice_staff)
  > PA-3545 (PT-3545), criterion C3 (policy B.3): the request lists Dr. S. Adeyemi as Gastroenterology, but no chart document confirms the specialty. Could you locate and attach documentation of the prescriber's gastroenterology specialty (e.g., a signed clinic note with credentials) or a gastroenterology consultation note for this treatment?
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment.

## Run cost

3 model calls, 17,372 input and 5,334 output tokens, 34.4 s of model time, $0.102 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
