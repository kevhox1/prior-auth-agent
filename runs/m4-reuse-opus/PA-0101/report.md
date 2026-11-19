# PA-0101: evolocumab for PT-0101

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-evolocumab-lipids version 2026-09
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: decision within 72 hours of receiving all required information (policy section E).
- Ordered dose: 140 mg subcutaneously every 2 weeks
- Benefit routing: sc_injection -> pharmacy

## Checklist

### C1 (policy B.1): MET
_The prescriber documents in the clinical record that the member has one of two conditions. The first is clinical ASCVD, meaning a prior myocardial infarction or acute coronary syndrome, coronary or other arterial revascularization, stable or unstable angina with documented coronary artery disease, ischemic stroke or TIA of atherosclerotic origin, or symptomatic peripheral artery disease. The second is heterozygous familial hypercholesterolemia (HeFH) confirmed by genetic testing or by a Dutch Lipid Clinic Network score of 6 or higher._

The cardiologist documents clinical ASCVD and names the event: NSTEMI in 03/2025 with a stent to the proximal LAD. The outside discharge summary confirms the PCI with a drug-eluting stent. Both MI and revascularization count under this criterion. (confidence 0.97)

- `PT-0101/cardiology-note-2026-11-10` (2026-11-10): "Clinical ASCVD: NSTEMI 03/2025 with drug-eluting stent to the proximal LAD."
- `PT-0101/outside-records-2025-03-18` (2025-03-18): "Percutaneous coronary intervention with one drug-eluting stent."

### C2 (policy B.2): MET
_An LDL-C result drawn in the 3 months before the request, while the member was on the lipid-lowering therapy described in B.3 and B.4, is at or above the member's threshold. The threshold is 70 mg/dL for a member with clinical ASCVD, or 100 mg/dL for a member with HeFH and no clinical ASCVD. An LDL-C drawn before the current lipid-lowering regimen was started does not meet this requirement._

LDL-C was 98 mg/dL on 10/27/2026, which is within 3 months of the 11/18/2026 request. That is above the 70 mg/dL threshold for ASCVD. It was drawn while the patient was on atorvastatin 80 mg plus ezetimibe, which was started 06/02/2026. (confidence 0.95)

- `PT-0101/labs-2026-10-27` (2026-10-27): "LDL cholesterol, calculated         98 mg/dL      <100"
- `PT-0101/cardiology-note-2026-11-10` (2026-11-10): "Lipid panel 10/27/2026: LDL-C 98 mg/dL on atorvastatin 80 mg and ezetimibe 10 mg (ezetimibe since 06/02/2026)."

### C3 (policy B.3): MET
_The member is on maximally tolerated statin therapy, shown by either (a) or (b). One is enough. For any claimed intolerance, the record must describe each statin's drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement._

**C3a (policy B.3(a)): MET**: The member takes a high-intensity statin (atorvastatin 40 to 80 mg daily or rosuvastatin 20 to 40 mg daily), or the highest statin dose the member tolerates when a higher dose caused a documented adverse effect. The member has taken it for at least 8 weeks before the B.2 LDL-C and will continue it with evolocumab. Any intolerance of a higher dose must be described with the drug, dose, symptom or adverse effect, and improvement after stopping or reducing it. A bare "statin intolerant" statement does not count.

The patient has taken atorvastatin 80 mg, a high-intensity dose, since 2025-03-18 and fills it on time. That is well over 8 weeks before the 10/27/2026 LDL-C. The plan says atorvastatin will continue alongside evolocumab. (confidence 0.95)

- `PT-0101/medication-history-2026-11-10` (2026-11-10): "| Atorvastatin | 80 mg nightly | 2025-03-18 | ongoing | Started at hospital discharge after NSTEMI. Fills on time every 90 days. No side effects reported. |"
- `PT-0101/cardiology-note-2026-11-10` (2026-11-10): "1. Start evolocumab 140 mg subcutaneously every 2 weeks. Continue atorvastatin 80 mg and ezetimibe 10 mg."

**C3b (policy B.3(b)): **NOT MET****: The member cannot take a statin for one of two reasons. (i) Intolerance of at least two different statins, at least one of them at the lowest approved starting dose. (ii) A contraindication, meaning a history of statin-associated rhabdomyolysis or active liver disease. For each statin, the intolerance must be described with the drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement.

The chart shows the patient tolerates atorvastatin 80 mg with no side effects. No intolerance of two statins and no contraindication is documented. This alternative path does not apply, but C3 is already satisfied through C3a. (confidence 0.90)

- `PT-0101/medication-history-2026-11-10` (2026-11-10): "No side effects reported."
- `PT-0101/cardiology-note-2026-11-10` (2026-11-10): "Taking atorvastatin and ezetimibe every day, no muscle symptoms."

### C4 (policy B.4): MET
_The member has taken ezetimibe 10 mg daily for at least 4 weeks, now or in the past, and LDL-C stayed at or above the B.2 threshold. Alternatively, the record documents intolerance of or a contraindication to ezetimibe._

Ezetimibe 10 mg daily was started 2026-06-02, about 21 weeks before the 10/27/2026 LDL-C. That LDL-C of 98 mg/dL is still at or above the 70 mg/dL threshold. (confidence 0.95)

- `PT-0101/medication-history-2026-11-10` (2026-11-10): "| Ezetimibe | 10 mg daily | 2026-06-02 | ongoing | Added for LDL 131 on atorvastatin alone. Fills on time. |"
- `PT-0101/labs-2026-10-27` (2026-10-27): "LDL cholesterol, calculated         98 mg/dL      <100"

### C5 (policy B.5): MET
_The prescriber is a cardiologist, an endocrinologist, or a lipid specialist, or the prescriber has consulted with one about this treatment._

The prescriber, Dr. M. Osei, signs as Cardiology, so the prescriber is a cardiologist. (confidence 0.97)

- `PT-0101/cardiology-note-2026-11-10` (2026-11-10): "Electronically signed by Dr. M. Osei, MD, Cardiology, 11/10/2026"

### C6 (policy B.6): MET
_The member is at least 18 years old on the date of the request._

With a date of birth of 06/02/1965, the patient is 61 on the 2026-11-18 request date, which is over 18. (confidence 0.98)

- `PT-0101/demographics-2026-11-10` (2026-11-10): "Date of birth: 06/02/1965"
- Code checks: age 61 on 2026-11-18 from DOB 1965-06-02

### C7 (policy B.7): MET
_Evolocumab will not be combined with another PCSK9-directed therapy (alirocumab or inclisiran). When the member is switching from one of these, the record shows the earlier agent is stopping._

The reconciled medication history says the patient has never taken a PCSK9 inhibitor or inclisiran, now or before. There is no concurrent therapy and no switch to document. (confidence 0.95)

- `PT-0101/medication-history-2026-11-10` (2026-11-10): "No current or prior PCSK9 inhibitor (alirocumab, evolocumab) or inclisiran."

### C8 (policy B.8): MET
_The requested regimen is a labeled adult regimen: 140 mg under the skin every 2 weeks, or 420 mg under the skin once a month._

The ordered regimen is 140 mg subcutaneously every 2 weeks. This matches the request and is a labeled adult regimen. (confidence 0.98)

- `PT-0101/cardiology-note-2026-11-10` (2026-11-10): "1. Start evolocumab 140 mg subcutaneously every 2 weeks."

## Draft PA form (step 8)

| Field | Value | Source |
|---|---|---|
| Member name | Lindqvist, Marcus T. | `PT-0101/demographics-2026-11-10` |
| Member date of birth | 06/02/1965 | `PT-0101/demographics-2026-11-10` |
| Member ID | CMU-771-430-12 | `PT-0101/demographics-2026-11-10` |
| Requested product | evolocumab | `request` |
| Requested regimen | 140 mg subcutaneously every 2 weeks | `request` |
| Diagnosis code (ICD-10) | I25.10 | `request` |
| Ordering provider | Dr. M. Osei, Cardiology | `request` |
| Requested start date | 2026-12-01 | `request` |
| Review type | Standard | `request` |
| C1 (policy B.1) | Met: clinical ASCVD documented by the prescriber (NSTEMI 03/2025 with a drug-eluting stent to the proximal LAD). | `PT-0101/cardiology-note-2026-11-10`; `PT-0101/outside-records-2025-03-18` |
| C2 (policy B.2) | Met: LDL-C 98 mg/dL on 10/27/2026 while on atorvastatin 80 mg and ezetimibe 10 mg. | `PT-0101/labs-2026-10-27`; `PT-0101/cardiology-note-2026-11-10` |
| C3a (policy B.3(a)) | Met: atorvastatin 80 mg nightly since 2025-03-18, ongoing, to be continued. | `PT-0101/medication-history-2026-11-10`; `PT-0101/cardiology-note-2026-11-10` |
| C4 (policy B.4) | Met: ezetimibe 10 mg daily since 2026-06-02, ongoing; LDL-C 98 mg/dL on 10/27/2026 on ezetimibe. | `PT-0101/medication-history-2026-11-10`; `PT-0101/labs-2026-10-27` |
| C5 (policy B.5) | Met: prescriber is a cardiologist (Dr. M. Osei, MD, Cardiology). | `PT-0101/cardiology-note-2026-11-10` |
| C6 (policy B.6) | Met: date of birth 06/02/1965; age 61 on the request date of 2026-11-18. | `PT-0101/demographics-2026-11-10`; `request` |
| C7 (policy B.7) | Met: no current or prior PCSK9 inhibitor or inclisiran. | `PT-0101/medication-history-2026-11-10` |
| C8 (policy B.8) | Met: 140 mg subcutaneously every 2 weeks. | `PT-0101/cardiology-note-2026-11-10`; `request` |

## Draft letter of medical necessity (step 8)

To the Calder Mutual Pharmacy Prior Authorization Review Team:  
I am requesting prior authorization of evolocumab for my patient, Marcus T. Lindqvist (Member ID CMU-771-430-12). [`request`] [`PT-0101/demographics-2026-11-10`] [`PT-0101/demographics-2026-11-10`]  
The requested regimen is 140 mg subcutaneously every 2 weeks, with a requested start date of 2026-12-01. [`request`] [`request`]  
The diagnosis code for this request is I25.10. [`request`]  
The record shows how each policy criterion is met, as follows.  
B.1: My clinical note documents clinical ASCVD: NSTEMI in 03/2025 with a drug-eluting stent to the proximal LAD. [`PT-0101/cardiology-note-2026-11-10`]  
Outside records from 2025-03-18 confirm percutaneous coronary intervention with one drug-eluting stent. [`PT-0101/outside-records-2025-03-18`]  
B.2: A lipid panel drawn on 10/27/2026 showed a calculated LDL-C of 98 mg/dL. [`PT-0101/labs-2026-10-27`]  
This result was obtained while the patient was taking atorvastatin 80 mg and ezetimibe 10 mg. [`PT-0101/cardiology-note-2026-11-10`]  
B.3(a): The patient has taken atorvastatin 80 mg nightly since 2025-03-18, and that therapy is ongoing. [`PT-0101/medication-history-2026-11-10`]  
My plan is to continue atorvastatin 80 mg alongside evolocumab. [`PT-0101/cardiology-note-2026-11-10`]  
B.4: The patient has taken ezetimibe 10 mg daily since 2026-06-02, and that therapy is ongoing. [`PT-0101/medication-history-2026-11-10`]  
The LDL-C of 98 mg/dL on 10/27/2026 was measured while the patient was on ezetimibe. [`PT-0101/cardiology-note-2026-11-10`]  
B.5: I am the prescriber, and I am a cardiologist. [`PT-0101/cardiology-note-2026-11-10`]  
B.6: The patient's date of birth is 06/02/1965, so he was 61 years old on the request date of 2026-11-18. [`PT-0101/demographics-2026-11-10`] [`request`]  
B.7: The patient has no current or prior use of a PCSK9 inhibitor or inclisiran. [`PT-0101/medication-history-2026-11-10`]  
B.8: The ordered regimen is evolocumab 140 mg subcutaneously every 2 weeks. [`PT-0101/cardiology-note-2026-11-10`]  
Thank you for reviewing this request.  
Sincerely,  
[Signature pending review by Dr. M. Osei, Cardiology]  

## Independent verification (step 9)

All claims supported. (32 claims checked.)

## Run cost

4 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (4 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: reuse.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3a | B.3(a) | MET | MET | MET | ok |
| C3b | B.3(b) | NOT_MET | NOT_MET | NOT_MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5 | B.5 | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
