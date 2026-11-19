# PA-3504: ustekinumab-aekn for PT-3504

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

In the 2026-10-31 GI note, the prescriber writes that the patient has moderately to severely active ileocolonic Crohn's disease. This covers both the diagnosis and the severity the policy asks for. (confidence 0.95)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A colonoscopy on 2026-08-16 falls within 12 months of the 2026-11-18 request. It found ulcers in the terminal ileum, and pathology showed chronic active inflammation, so active mucosal inflammation is documented by direct visualization. (confidence 0.95)

- `PT-3504/colonoscopy-2026-08-16` (2026-08-16): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3504/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. A. Rivera, Gastroenterology. The ustekinumab plan comes from the GI follow-up note, so the prescriber is a gastroenterologist. (confidence 0.90)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

Two records give the same date of birth, 2000-04-27. That makes the member 26 on the request date of 2026-11-18, which is over 18. (confidence 0.98)

- `PT-3504/demographics-2026-02-05` (2026-02-05): "Date of birth: 2000-04-27"
- `PT-3504/outside-records-2023-09-18` (2023-09-18): "PT: KOWALCZYK, ROSA      DOB 2000-04-27"
- Code checks: age 26 on 2026-11-18 from DOB 2000-04-27

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Prednisone, a conventional corticosteroid, was used from 2023-05 to 2024-01. It was stopped because of steroid dependence, with a flare each time the dose was tapered, which counts as inadequate response. The outside record's treatment history section is blank because the fax was incomplete; that is missing information, not a conflict. (confidence 0.90)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Prednisone | 40 mg daily, tapered | 2023-05 | 2024-01 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab, a biologic, was used from 2024-03 to 2026-09. It was stopped for intolerance (drug-induced lupus), and the record gives the drug, the dates and the reason. (confidence 0.92)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Infliximab | 5 mg/kg IV every 8 weeks | 2024-03 | 2026-09 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON-TB Gold Plus test (an interferon-gamma release assay) was negative on 2026-09-20. That is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-3504/labs-2026-09-20` (2026-09-20): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both the hepatitis B surface antigen and the total core antibody were resulted as nonreactive on 2026-09-20. Since neither is reactive, no prophylaxis or monitoring plan is required. (confidence 0.96)

- `PT-3504/labs-2026-09-20` (2026-09-20): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3504/labs-2026-09-20` (2026-09-20): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The medication history says the patient is on no current biologic, JAK inhibitor, or S1P receptor modulator. The earlier biologic, infliximab, was stopped in 2026-09. (confidence 0.90)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Infliximab | 5 mg/kg IV every 8 weeks | 2024-03 | 2026-09 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 55.0 kg was recorded on 2026-10-31, within 90 days of the request. That puts the patient in the band of up to and including 55 kg, so the IV dose is 260 mg. The request is for 260 mg IV, then 90 mg under the skin every 8 weeks starting 8 weeks after the infusion, which matches the labeled regimen. (confidence 0.93)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "- Weight 55.0 kg."
- `PT-3504/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-31) -> label tier 260 mg; requested 260 mg

## Draft PA form (step 8)

| Field | Value | Source |
|---|---|---|
| Member name | Rosa Kowalczyk | `PT-3504/demographics-2026-02-05` |
| Member date of birth | 2000-04-27 | `PT-3504/demographics-2026-02-05` |
| Member ID | CMU-672-659-23 | `PT-3504/demographics-2026-02-05` |
| Requested product | ustekinumab-aekn | `request` |
| Requested regimen | 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose | `request` |
| Diagnosis code (ICD-10) | K50.80 | `request` |
| Ordering provider | Dr. A. Rivera, Gastroenterology | `request` |
| Requested start date | 2026-12-01 | `request` |
| Review type | Standard | `request` |
| C1 (policy B.1) | Met. The prescriber's GI note of 2026-10-31 documents moderately to severely active ileocolonic Crohn's disease. | `PT-3504/gi-note-2026-10-31` |
| C2 (policy B.2) | Met. Colonoscopy on 2026-08-16 (within 12 months of the 2026-11-18 request) showed multiple terminal ileal ulcers with erythema and edema; pathology showed chronic active inflammation. | `PT-3504/colonoscopy-2026-08-16`; `PT-3504/colonoscopy-2026-08-16`; `request` |
| C3 (policy B.3) | Met. The ordering prescriber is Dr. A. Rivera, Gastroenterology, who ordered the treatment in the GI note of 2026-10-31. | `request`; `PT-3504/gi-note-2026-10-31` |
| C4 (policy B.4) | Met. Date of birth 2000-04-27; the member is 26 years old on the request date of 2026-11-18. | `PT-3504/demographics-2026-02-05`; `request` |
| C5a (policy B.5(a)) | Met. Prednisone 40 mg daily, tapered (2023-05 to 2024-01), was stopped for inadequate response: the member was steroid dependent and flared each time the dose went below 15 mg. | `PT-3504/medication-history-2026-10-29` |
| C5b (policy B.5(b)) | Met. Infliximab 5 mg/kg IV every 8 weeks (2024-03 to 2026-09) was stopped for intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias). | `PT-3504/medication-history-2026-10-29` |
| C6 (policy B.6) | Met. QuantiFERON-TB Gold Plus negative on 2026-09-20 (within 6 months of the request). | `PT-3504/labs-2026-09-20` |
| C7 (policy B.7) | Met. On 2026-09-20, hepatitis B surface antigen was nonreactive and total hepatitis B core antibody was nonreactive. | `PT-3504/labs-2026-09-20`; `PT-3504/labs-2026-09-20` |
| C8 (policy B.8) | Met. Medication history documents no current biologic, JAK inhibitor, or S1P receptor modulator; prior infliximab ended 2026-09. | `PT-3504/medication-history-2026-10-29`; `PT-3504/medication-history-2026-10-29` |
| C9 (policy B.9) | Met. Weight 55.0 kg (up to and including 55 kg tier = 260 mg IV); regimen is 260 mg IV once, then 90 mg SC every 8 weeks starting 8 weeks after the IV dose. | `PT-3504/gi-note-2026-10-31`; `PT-3504/gi-note-2026-10-31`; `request` |

## Draft letter of medical necessity (step 8)

To the Calder Mutual Utilization Management / Prior Authorization Department:  
Re: Rosa Kowalczyk, date of birth 2000-04-27, Member ID CMU-672-659-23. [`PT-3504/demographics-2026-02-05`] [`PT-3504/demographics-2026-02-05`] [`PT-3504/demographics-2026-02-05`]  
I am requesting prior authorization of ustekinumab-aekn for my patient for diagnosis code K50.80. [`request`] [`request`]  
The requested regimen is 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose, with a requested start date of 2026-12-01. [`request`] [`request`]  
The record addresses each policy criterion in order below.  
B.1: My note of 2026-10-31 documents moderately to severely active ileocolonic Crohn's disease. [`PT-3504/gi-note-2026-10-31`]  
B.2: Colonoscopy on 2026-08-16 showed multiple ulcers of 0.5-2 cm in the terminal ileum with surrounding erythema and edema. [`PT-3504/colonoscopy-2026-08-16`]  
Pathology from that colonoscopy showed chronic active inflammation. [`PT-3504/colonoscopy-2026-08-16`]  
B.3: The ordering prescriber is Dr. A. Rivera, Gastroenterology. [`request`]  
B.4: The patient's date of birth is 2000-04-27, making her 26 years old on the request date of 2026-11-18. [`PT-3504/demographics-2026-02-05`] [`request`]  
B.5(a): Prednisone 40 mg daily, tapered, was used from 2023-05 to 2024-01, and the patient was steroid dependent, flaring each time the dose went below 15 mg. [`PT-3504/medication-history-2026-10-29`]  
B.5(b): Infliximab 5 mg/kg IV every 8 weeks was used from 2024-03 to 2026-09 and was stopped for intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias). [`PT-3504/medication-history-2026-10-29`]  
B.6: A QuantiFERON-TB Gold Plus test on 2026-09-20 was negative. [`PT-3504/labs-2026-09-20`]  
B.7: On 2026-09-20, hepatitis B surface antigen was nonreactive. [`PT-3504/labs-2026-09-20`]  
On the same date, total hepatitis B core antibody was nonreactive. [`PT-3504/labs-2026-09-20`]  
B.8: The medication history documents no current biologic, JAK inhibitor, or S1P receptor modulator. [`PT-3504/medication-history-2026-10-29`]  
B.9: The patient's documented weight is 55.0 kg. [`PT-3504/gi-note-2026-10-31`]  
The ordered regimen is 260 mg IV once, then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose. [`PT-3504/gi-note-2026-10-31`]  
Thank you for your review of this request.  
Sincerely,  
[Signature pending review by Dr. A. Rivera, Gastroenterology]  

## Independent verification (step 9)

All claims supported. (35 claims checked.)

## Run cost

4 model calls, 15,671 input and 6,528 output tokens, 51.7 s of model time, $0.235 at list price (2 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: borderline.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
