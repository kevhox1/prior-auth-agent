# PA-3541: ustekinumab-aekn for PT-3541

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

The 11/08/2026 GI follow-up note states the prescriber's assessment of moderately to severely active ileocolonic Crohn's disease. The Harvey-Bradshaw Index of 11 in the same note is consistent with that statement. (confidence 0.90)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3541/gi-note-2026-11-08` (2026-11-08): "Harvey-Bradshaw Index today: 11."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy with biopsies dated 08/17/2026 is within the past 12 months of the 11/18/2026 request. The report documents endoscopic ulcers, erythema and edema, which is active mucosal inflammation, and biopsies show chronic active inflammation. (confidence 0.88)

- `PT-3541/colonoscopy-2026-08-17` (2026-08-17): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3541/colonoscopy-2026-08-17` (2026-08-17): "Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The 11/08/2026 GI note contains the ustekinumab order, but the passages do not show the author's specialty in writing. No documented consultation with a gastroenterologist was found, so the specialty requirement cannot be confirmed from the chart passages. (confidence 0.60)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Missing: Written specialty of the ordering clinician (Dr. A. Rivera) or the signing provider on the 2026-11-08 GI note, showing gastroenterology

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth 07/12/2000 makes the member 26 years old on the 11/18/2026 request date, which meets the 18-or-older requirement. (confidence 0.97)

- `PT-3541/demographics-2026-11-01` (2026-11-01): "Date of birth: 07/12/2000"
- Code checks: age 26 on 2026-11-18 from DOB 2000-07-12

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history records oral prednisone used from 05/2020 to 01/2021. It was stopped because the member was steroid dependent and flared whenever the dose went below 15 mg, which is an insufficient response. (confidence 0.90)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "| Prednisone | 40 mg daily, tapered | 05/2020 | 01/2021 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The medication history records adalimumab, a TNF blocker, used from 07/2023 to 11/2023. It was stopped for primary non-response with no clinical improvement after induction and maintenance. (confidence 0.92)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy B.6): **NOT MET**
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The only TB screen in the passages is a negative QuantiFERON dated 11/29/2025, which is more than 6 months before the 11/18/2026 request. No TB screen dated within the past 6 months appears in the passages. (confidence 0.85)

- `PT-3541/labs-2025-11-29` (2025-11-29): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both required hepatitis B results are on the 09/19/2026 labs: HBsAg is nonreactive and total core antibody is nonreactive. Because neither result is reactive, no prophylaxis plan is required. (confidence 0.95)

- `PT-3541/labs-2026-09-19` (2026-09-19): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3541/labs-2026-09-19` (2026-09-19): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 11/04/2026 medication reconciliation states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The only prior biologic, adalimumab, was stopped in 11/2023, so this is not a switch from a current agent. (confidence 0.90)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg recorded 11/08/2026 is within 90 days of the request. The requested 260 mg IV induction matches the band for weights up to and including 55 kg, and the 90 mg SC every 8 weeks maintenance starts 8 weeks after induction. The earlier 58.0 kg weight from 05/29/2026 is outside the window and does not change the result. (confidence 0.88)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "Weight 55.0 kg."
- `PT-3541/gi-note-2026-11-08` (2026-11-08): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-08) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C3**: Written specialty of Dr. A. Rivera or the signing provider on the 2026-11-08 GI note, showing gastroenterology (or a documented gastroenterology consult about ustekinumab) (who: practice_staff)
  > PA-3541 (ustekinumab-aekn, patient PT-3541): criterion C3 needs written proof that the prescriber is a gastroenterologist. Please find the specialty listed for Dr. A. Rivera or the signing provider on the 2026-11-08 GI note and file it with the request. If no specialty appears on record, let Dr. Rivera know a documented gastroenterology consultation about this treatment would also satisfy C3.
  - Would satisfy the policy: Policy B.3 accepts documentation that the prescriber is a gastroenterologist (written specialty on the 2026-11-08 GI note or the provider record), or a documented consultation with a gastroenterologist about ustekinumab, dated on or before the request date of 2026-11-18.
- **C6**: Negative TB screen (interferon-gamma release assay or tuberculin skin test) dated within the past 6 months; the only screen on file is a negative QuantiFERON dated 2025-11-29 (who: ordering_provider)
  > PA-3541 (ustekinumab-aekn, patient PT-3541): criterion C6 is not met. The only TB screen in the records is a negative QuantiFERON-TB Gold Plus dated 2025-11-29, which is more than 6 months before the 2026-11-18 request date. Please review this criterion and document whether a current TB screen is available or planned.
  - Would satisfy the policy: Policy B.6 accepts a negative interferon-gamma release assay or tuberculin skin test dated on or after 2026-05-18. An indeterminate or borderline result does not count as negative. A positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun.

## Run cost

3 model calls, 19,142 input and 10,511 output tokens, 45.1 s of model time, $0.008 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
