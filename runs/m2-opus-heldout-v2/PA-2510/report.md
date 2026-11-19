# PA-2510: ustekinumab-aekn for PT-2510

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 85.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI prescriber's 2026-11-02 note states the diagnosis is moderately to severely active ileocolonic Crohn's disease. A Harvey-Bradshaw Index of 14 supports this. (confidence 0.96)

- `PT-2510/gi-note-2026-11-02` (2026-11-02): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2510/gi-note-2026-11-02` (2026-11-02): "Harvey-Bradshaw Index today: 14."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A colonoscopy on 2026-08-31 falls within 12 months of the 2026-11-18 request. It found ulcers in the terminal ileum with erythema and edema, and an SES-CD of 11, which shows active mucosal inflammation. This rests on the colonoscopy, not on the lab markers. (confidence 0.95)

- `PT-2510/colonoscopy-2026-08-31` (2026-08-31): "PROCEDURE: Colonoscopy with biopsies"
- `PT-2510/colonoscopy-2026-08-31` (2026-08-31): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-2510/colonoscopy-2026-08-31` (2026-08-31): "SES-CD: 11"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. M. Chen, Gastroenterology. The ustekinumab order appears in the GI follow-up note of 2026-11-02. (confidence 0.93)

- `PT-2510/gi-note-2026-11-02` (2026-11-02): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 1973-11-02, the member is 53 on the 2026-11-18 request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-2510/demographics-2026-09-03` (2026-09-03): "Date of birth: 1973-11-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-11-02

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Budesonide was used 2020-05 to 2020-08 and stopped for inadequate response. Methotrexate was used 2020-09 to 2021-03 and stopped for intolerance. Both are conventional agents with dates and a qualifying reason. (confidence 0.93)

- `PT-2510/medication-history-2026-10-31` (2026-10-31): "Budesonide 9 mg daily, 2020-05 to 2020-08. Reason stopped: inadequate response after 10 weeks."
- `PT-2510/medication-history-2026-10-31` (2026-10-31): "Methotrexate 25 mg subcutaneously weekly, 2020-09 to 2021-03. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The medication history says infliximab was given from 2023-07 and stopped for loss of response, based on patient report. The 2023-12 outside records say the patient declined infliximab in 2023-07 and was biologic-naive. The requested outside records that might settle this are not in the chart. C5 can still be satisfied through C5a. (confidence 0.80)

- `PT-2510/medication-history-2026-10-31` (2026-10-31): "Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-05. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-2510/outside-records-2023-12-18` (2023-12-18): "- Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

A QuantiFERON-TB Gold Plus collected 2026-09-16 was negative, which is within 6 months of the request. The 2023 screen mentioned in the GI note is older, but it is not needed. (confidence 0.95)

- `PT-2510/labs-2026-09-16` (2026-09-16): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

HBsAg and total hepatitis B core antibody both resulted nonreactive on 2026-09-16. Because neither is reactive, no prophylaxis plan is required. (confidence 0.96)

- `PT-2510/labs-2026-09-16` (2026-09-16): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-2510/labs-2026-09-16` (2026-09-16): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current medication history states there is no biologic or small-molecule advanced therapy at present. The listed current medications, prednisone and omeprazole, are not in an excluded class. Whether infliximab was ever given (see C5b) does not change this, because no such agent is current. (confidence 0.88)

- `PT-2510/medication-history-2026-10-31` (2026-10-31): "- No biologic or small-molecule advanced therapy at present."
- `PT-2510/medication-history-2026-10-31` (2026-10-31): "- Prednisone 20 mg daily, taper planned after induction"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 85.0 kg on 2026-11-02 is within 90 days of the request and falls in the >55 to ≤85 kg band, which calls for 390 mg IV. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the label. The patient sits exactly at the band boundary; the older 86.4 kg weight from 2026-04-12 is outside the 90-day window. (confidence 0.90)

- `PT-2510/gi-note-2026-11-02` (2026-11-02): "Weight 85.0 kg."
- `PT-2510/gi-note-2026-11-02` (2026-11-02): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 85.0 kg (2026-11-02) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C5b**: Provider review of conflicting infliximab history (prior use and loss of response vs. declined/biologic-naive) (who: ordering_provider)
  > Dr. Chen, for PT-2510's ustekinumab PA (criterion C5b, prior biologic failure), the chart has two conflicting accounts of infliximab. The medication history dated 2026-10-31 lists infliximab 5 mg/kg IV every 8 weeks from 2023-07 to 2026-05, stopped for loss of response per patient report. The outside records dated 2023-12-18 say infliximab was recommended in 2023-07, the patient declined, and the patient was biologic-naive. The outside records requested to settle this are not in the chart yet, so please review and document which history is accurate.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: conflicting.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
