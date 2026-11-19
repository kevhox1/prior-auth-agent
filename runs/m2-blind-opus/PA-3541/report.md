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

The GI note of 2026-11-08 states moderately to severely active ileocolonic Crohn's disease. The problem list confirms the Crohn's diagnosis (K50.80). (confidence 0.96)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3541/problem-list-2026-11-08` (2026-11-08): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2020."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The colonoscopy on 2026-08-17 is about 3 months before the request, so it falls inside the 12-month window. It shows ulcers in the terminal ileum with erythema and edema, and pathology shows chronic active inflammation. (confidence 0.95)

- `PT-3541/colonoscopy-2026-08-17` (2026-08-17): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3541/colonoscopy-2026-08-17` (2026-08-17): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3541/colonoscopy-2026-08-17` (2026-08-17): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request names the ordering provider as Dr. A. Rivera, Gastroenterology. The ustekinumab plan is written in a GI follow-up note. The quoted passage does not state the specialty itself, so a reviewer may want to confirm the provider's credentials. (confidence 0.85)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 07/12/2000, the member is 26 on the request date of 2026-11-18, which meets the 18-and-over requirement. (confidence 0.98)

- `PT-3541/demographics-2026-11-01` (2026-11-01): "Date of birth: 07/12/2000"
- Code checks: age 26 on 2026-11-18 from DOB 2000-07-12

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Prednisone, a conventional corticosteroid, was used from 05/2020 to 01/2021. It was stopped because of steroid dependence: the disease flared each time the dose went below 15 mg, which is an inadequate response. (confidence 0.92)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "| Prednisone | 40 mg daily, tapered | 05/2020 | 01/2021 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab was used from 07/2023 to 11/2023. It was stopped for primary non-response, which is an inadequate response. (confidence 0.95)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy B.6): **NOT MET**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The only TB screen in the chart is a negative QuantiFERON dated 2025-11-29. That is about 12 months before the 2026-11-18 request, outside the 6-month window. No newer IGRA or TST result was found. (confidence 0.88)

- `PT-3541/labs-2025-11-29` (2025-11-29): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg and total hepatitis B core antibody were resulted on 2026-09-19, and both are nonreactive. Because neither is reactive, no prophylaxis or monitoring plan is needed. (confidence 0.96)

- `PT-3541/labs-2026-09-19` (2026-09-19): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3541/labs-2026-09-19` (2026-09-19): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The medication history states the member is on no current biologic, JAK inhibitor, or S1P receptor modulator. The earlier adalimumab was stopped in 11/2023. (confidence 0.93)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3541/medication-history-2026-11-04` (2026-11-04): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 55.0 kg was recorded on 2026-11-08, within 90 days of the request. That falls in the up-to-and-including 55 kg band, so 260 mg IV is correct, and the maintenance dose of 90 mg SC every 8 weeks starting 8 weeks after the infusion matches the label. The older 58.0 kg weight from 2026-05-29 is outside the 90-day window and does not decide the dose. (confidence 0.90)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "- Weight 55.0 kg."
- `PT-3541/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-08) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C6**: Negative TB screen (IGRA or TST) from within the past 6 months (who: ordering_provider)
  > Dr. Rivera, for PA-3541 (ustekinumab-aekn, PT-3541), the TB screening criterion (policy B.6) is not met. The only TB screen in the chart is the negative QuantiFERON TB Gold Plus dated 2025-11-29 (labs-2025-11-29). That is about 12 months before the 2026-11-18 request date, and the policy requires a result from the past 6 months. Could you check whether there is a newer IGRA or TST result and tell us how you want to proceed?
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result does not count. If the screen is positive, the policy requires a chest radiograph showing no active disease and documentation that latent TB treatment has started.

## Run cost

3 model calls, 18,713 input and 5,932 output tokens, 53.0 s of model time, $0.226 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
