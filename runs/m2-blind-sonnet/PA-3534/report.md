# PA-3534: ustekinumab-aekn for PT-3534

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: URGENT review. Decision within 24 hours of receiving all required information (policy section E). Prescriber attestation of urgency is required. Work this case first.
- Ordered dose: 390 mg IV once (weight 66.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-11-09 states moderately to severely active Crohn's disease. Nothing in the chart contradicts it. (confidence 0.96)

- `PT-3534/gi-note-2026-11-09` (2026-11-09): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy on file is the colonoscopy of 2025-04-18, which is more than 12 months before the 2026-11-18 request. The recent CRP is a lab marker and does not satisfy the direct visualization requirement. (confidence 0.85)

- `PT-3534/colonoscopy-2025-04-18` (2025-04-18): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3534/labs-2026-10-21` (2026-10-21): "C-reactive protein                    22.0 mg/L     <5.0"

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No retrieved chart passage states the prescriber's specialty or documents a gastroenterology consultation. The specialty appears only in the request form, not in a quoted chart document. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (gastroenterology) or of a consultation with a gastroenterologist

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Born 03/19/1992, the member is 34 on the request date of 2026-11-18, so is over 18. (confidence 0.97)

- `PT-3534/demographics-2026-04-29` (2026-04-29): "Date of birth: 03/19/1992"
- Code checks: age 34 on 2026-11-18 from DOB 1992-03-19

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Infliximab was used 07/2023 to 07/2026 and stopped for secondary loss of response. Budesonide was also stopped for inadequate response. Either one satisfies the criterion. (confidence 0.96)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."
- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Budesonide 9 mg daily, 05/2019 to 08/2019. Reason stopped: inadequate response after 10 weeks."

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON dated 2026-10-21 is within 6 months of the request date. (confidence 0.95)

- `PT-3534/labs-2026-10-21` (2026-10-21): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are on file and nonreactive, so no prophylaxis plan is required. (confidence 0.96)

- `PT-3534/labs-2026-10-21` (2026-10-21): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3534/labs-2026-10-21` (2026-10-21): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The current medication list shows no biologic, JAK inhibitor or S1P modulator. The prior infliximab ended 07/2026, so there is no combination. (confidence 0.92)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 66.2 kg recorded 2026-11-09 is within 90 days of the request and falls in the 390 mg tier. The maintenance regimen of 90 mg SC every 8 weeks matches the label. (confidence 0.95)

- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Weight 66.2 kg."
- Code checks: weight 66.2 kg (2026-11-09) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy within 12 months showing active inflammation (who: ordering_provider)
  > PA-3534 (PT-3534), criterion C2 (policy B.2): the only endoscopy on file is the colonoscopy of 2025-04-18, which is over 12 months before the 2026-11-18 request. The CRP of 22.0 mg/L (2026-10-21) is a lab marker and does not meet the direct visualization requirement. Please review and advise whether a more recent ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report exists or how you wish to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers (CRP, ESR, fecal calprotectin) and cross-sectional imaging do not satisfy it.
- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consult (who: practice_staff)
  > PA-3534 (PT-3534), criterion C3 (policy B.3): the prescriber's specialty appears only on the request form, not in any chart document. Could you locate a chart note, letterhead or signature block showing Dr. S. Adeyemi's gastroenterology specialty, or a note documenting a consultation with a gastroenterologist about this treatment, and attach it?
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment.

## Run cost

3 model calls, 17,182 input and 4,991 output tokens, 31.9 s of model time, $0.098 at list price (0 served from cache).

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
