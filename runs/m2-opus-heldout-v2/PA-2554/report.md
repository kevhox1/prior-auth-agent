# PA-2554: ustekinumab-aekn for PT-2554

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The gastroenterologist's 2026-11-09 note says the UC is moderately to severely active. The problem list records the UC diagnosis, K51.00. (confidence 0.96)

- `PT-2554/gi-note-2026-11-09` (2026-11-09): "Moderately to severely active ulcerative pancolitis."
- `PT-2554/problem-list-2026-11-09` (2026-11-09): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2019."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A flexible sigmoidoscopy on 2026-08-19, about 3 months before the request, shows active mucosal inflammation (Mayo endoscopic subscore 3). The lab markers were not used to meet this criterion. (confidence 0.95)

- `PT-2554/flexible-sigmoidoscopy-2026-08-19` (2026-08-19): "- Rectum to 27 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-2554/flexible-sigmoidoscopy-2026-08-19` (2026-08-19): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab plan appears in the GI follow-up note. (confidence 0.90)

- `PT-2554/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a birth date of 1974-08-12, the member is 52 on the request date of 2026-11-18. (confidence 0.98)

- `PT-2554/demographics-2025-12-01` (2025-12-01): "Date of birth: 1974-08-12"
- Code checks: age 52 on 2026-11-18 from DOB 1974-08-12

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Budesonide was used from 2019-06 to 2019-09 and stopped for inadequate response. Prednisone was used from 2019-10 to 2020-02 and stopped because of steroid dependence. (confidence 0.95)

- `PT-2554/medication-history-2026-11-09` (2026-11-09): "Budesonide 9 mg daily, 2019-06 to 2019-09. Reason stopped: inadequate response after 10 weeks."
- `PT-2554/medication-history-2026-11-09` (2026-11-09): "Prednisone 40 mg daily, tapered, 2019-10 to 2020-02. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab was used from 2023-07 to 2026-06. It was stopped for intolerance (drug-induced lupus). (confidence 0.95)

- `PT-2554/medication-history-2026-11-09` (2026-11-09): "Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-06. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The IGRA on 2026-10-04, within 6 months, was positive, so the positive-screen pathway applies. The 2026-10-07 chest radiograph shows no active TB. Rifampin for latent TB started on 2026-10-12. (confidence 0.92)

- `PT-2554/labs-2026-10-04` (2026-10-04): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-2554/chest-xray-2026-10-07` (2026-10-07): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2554/gi-note-2026-11-09` (2026-11-09): "Latent TB infection: rifampin daily for 4 months, started 2026-10-12."

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

None of the retrieved passages contain an HBsAg or total anti-HBc result. Both results are required. (confidence 0.93)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The medication history says the member is on no current biologic, JAK inhibitor or S1P receptor modulator. The earlier agent, infliximab, was stopped in 2026-06. (confidence 0.93)

- `PT-2554/medication-history-2026-11-09` (2026-11-09): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-2554/medication-history-2026-11-09` (2026-11-09): "Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-06. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 55.0 kg was recorded on 2026-11-09, within 90 days of the request, and falls in the 260 mg band (up to and including 55 kg). The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the label. The older 58.0 kg weight from 2026-03 is outside the 90-day window and does not decide this criterion. (confidence 0.90)

- `PT-2554/gi-note-2026-11-09` (2026-11-09): "Weight 55.0 kg."
- `PT-2554/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-09) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C7**: Hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results (who: practice_staff)
  > For PA-2554 (patient PT-2554, ustekinumab-aekn), Calder policy B.7 requires documented results for both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc). We could not find either result in the records we retrieved. Results of any age are accepted, but surface antibody results, vaccination records and pending orders do not count. Please locate and file both results, and if either is reactive, include the documented plan for antiviral prophylaxis or monitoring.

## Run cost

3 model calls, 18,447 input and 6,118 output tokens, 49.9 s of model time, $0.231 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
