# PA-0103: evolocumab for PT-0103

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-evolocumab-lipids version 2026-09
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: decision within 72 hours of receiving all required information (policy section E).
- Ordered dose: 140 mg subcutaneously every 2 weeks
- Benefit routing: sc_injection -> pharmacy

## Checklist

### C1 (policy B.1): MET
_The prescriber documents in the clinical record that the member has one of two conditions. The first is clinical ASCVD, meaning a prior myocardial infarction or acute coronary syndrome, coronary or other arterial revascularization, stable or unstable angina with documented coronary artery disease, ischemic stroke or TIA of atherosclerotic origin, or symptomatic peripheral artery disease. The second is heterozygous familial hypercholesterolemia (HeFH) confirmed by genetic testing or by a Dutch Lipid Clinic Network score of 6 or higher._

The cardiologist documents clinical ASCVD: an ischemic stroke caused by large-artery atherosclerosis, followed by carotid endarterectomy. The outside discharge summary confirms the stroke was of atherosclerotic origin. Either one is a qualifying ASCVD condition under B.1. (confidence 0.96)

- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Clinical ASCVD: ischemic stroke from large-artery atherosclerosis, status post carotid endarterectomy, with diabetes. Very high risk."
- `PT-0103/outside-records-2025-04-09` (2025-04-09): "Acute ischemic stroke, left middle cerebral artery territory, due to large-artery atherosclerosis (70% stenosis of the left internal carotid artery)."

### C2 (policy B.2): **NOT MET**
_An LDL-C result drawn in the 3 months before the request, while the member was on the lipid-lowering therapy described in B.3 and B.4, is at or above the member's threshold. The threshold is 70 mg/dL for a member with clinical ASCVD, or 100 mg/dL for a member with HeFH and no clinical ASCVD. An LDL-C drawn before the current lipid-lowering regimen was started does not meet this requirement._

The only LDL-C drawn on therapy inside the 3-month window is 64 mg/dL (10/15/2026). That is below the 70 mg/dL threshold for ASCVD. The 152 mg/dL value was drawn before therapy started and is outside the window, so it does not count, and the prescriber's own target of below 55 mg/dL is not the policy threshold. (confidence 0.93)

- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Lipid panel 10/15/2026: LDL-C 64 mg/dL on rosuvastatin 40 mg and ezetimibe 10 mg. LDL-C at the stroke admission was 152 mg/dL off therapy."
- `PT-0103/labs-2026-10-15` (2026-10-15): "COLLECTED: 10/15/2026 07:48      ORDERING: Dr. M. Osei"

### C3 (policy B.3): MET
_The member is on maximally tolerated statin therapy, shown by either (a) or (b). One is enough. For any claimed intolerance, the record must describe each statin's drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement._

**C3a (policy B.3(a)): MET**: The member takes a high-intensity statin (atorvastatin 40 to 80 mg daily or rosuvastatin 20 to 40 mg daily), or the highest statin dose the member tolerates when a higher dose caused a documented adverse effect. The member has taken it for at least 8 weeks before the B.2 LDL-C and will continue it with evolocumab. Any intolerance of a higher dose must be described with the drug, dose, symptom or adverse effect, and improvement after stopping or reducing it. A bare "statin intolerant" statement does not count.

Rosuvastatin 40 mg daily is a high-intensity statin. It was started 04/09/2025, well over 8 weeks before the 10/15/2026 LDL-C draw. The plan says to continue it alongside evolocumab. (confidence 0.93)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "| Rosuvastatin | 40 mg daily | 2025-04-09 | ongoing | Started at stroke discharge. Fills on time. No side effects reported. |"
- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Continue rosuvastatin 40 mg and ezetimibe 10 mg."

**C3b (policy B.3(b)): **NOT MET****: The member cannot take a statin for one of two reasons. (i) Intolerance of at least two different statins, at least one of them at the lowest approved starting dose. (ii) A contraindication, meaning a history of statin-associated rhabdomyolysis or active liver disease. For each statin, the intolerance must be described with the drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement.

The member tolerates high-intensity rosuvastatin with no side effects, and no statin intolerance or rhabdomyolysis is recorded. ALT is normal, so there is no evidence of active liver disease. This part does not apply, but C3 is satisfied through C3a. (confidence 0.85)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "| Rosuvastatin | 40 mg daily | 2025-04-09 | ongoing | Started at stroke discharge. Fills on time. No side effects reported. |"
- `PT-0103/labs-2026-10-15` (2026-10-15): "ALT                                   24 U/L        7-56"

### C4 (policy B.4): **NOT MET**
_The member has taken ezetimibe 10 mg daily for at least 4 weeks, now or in the past, and LDL-C stayed at or above the B.2 threshold. Alternatively, the record documents intolerance of or a contraindication to ezetimibe._

Ezetimibe 10 mg daily has been taken since 09/15/2025, which is more than 4 weeks. However, LDL-C on ezetimibe is 64 mg/dL, below the 70 mg/dL B.2 threshold, so the requirement that LDL-C stayed at or above the threshold fails. No ezetimibe intolerance or contraindication is documented. (confidence 0.85)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "| Ezetimibe | 10 mg daily | 2025-09-15 | ongoing | Fills on time. |"
- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Lipid panel 10/15/2026: LDL-C 64 mg/dL on rosuvastatin 40 mg and ezetimibe 10 mg."

### C5 (policy B.5): MET
_The prescriber is a cardiologist, an endocrinologist, or a lipid specialist, or the prescriber has consulted with one about this treatment._

The prescribing physician, Dr. M. Osei, signs the note as Cardiology. Cardiology is a qualifying specialty. (confidence 0.97)

- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Electronically signed by Dr. M. Osei, MD, Cardiology, 11/12/2026"

### C6 (policy B.6): MET
_The member is at least 18 years old on the date of the request._

The member was born 01/08/1959, which makes them 67 on the 2026-11-18 request date. That is at least 18. (confidence 0.98)

- `PT-0103/demographics-2026-11-12` (2026-11-12): "Date of birth: 01/08/1959"
- Code checks: age 67 on 2026-11-18 from DOB 1959-01-08

### C7 (policy B.7): MET
_Evolocumab will not be combined with another PCSK9-directed therapy (alirocumab or inclisiran). When the member is switching from one of these, the record shows the earlier agent is stopping._

The reconciled medication history states there is no current or prior alirocumab, evolocumab, or inclisiran. No combination with another PCSK9 agent and no switch are involved. (confidence 0.93)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "No current or prior PCSK9 inhibitor (alirocumab, evolocumab) or inclisiran."

### C8 (policy B.8): MET
_The requested regimen is a labeled adult regimen: 140 mg under the skin every 2 weeks, or 420 mg under the skin once a month._

The ordered and requested regimen is 140 mg subcutaneously every 2 weeks. That is a labeled adult regimen. (confidence 0.97)

- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Add evolocumab 140 mg subcutaneously every 2 weeks"

## To-do list (gap plan)

- **C2**: On-therapy LDL-C at or above 70 mg/dL within the 3 months before the request (who: ordering_provider)
  > Dr. Osei, for PT-0103's evolocumab request (PA-0103), criterion B.2 is not met. The only on-therapy LDL-C in the window is 64 mg/dL (labs collected 10/15/2026, on rosuvastatin 40 mg and ezetimibe 10 mg), which is below the policy's 70 mg/dL ASCVD threshold. The 152 mg/dL value from the stroke admission was drawn off therapy, so it does not count, and the policy uses 70 mg/dL rather than the <55 mg/dL target in your 11/12/2026 note. Please review and tell us whether there is any other on-therapy LDL-C result from this period, or how you would like to proceed.
  - Would satisfy the policy: Policy B.2 accepts an LDL-C of 70 mg/dL or higher (clinical ASCVD threshold), collected between 2026-08-18 and 2026-11-18 while the member was on the current statin and ezetimibe regimen.
- **C4**: LDL-C at or above 70 mg/dL after at least 4 weeks of ezetimibe, or documented ezetimibe intolerance/contraindication (who: ordering_provider)
  > Dr. Osei, for PT-0103's evolocumab request (PA-0103), criterion B.4 is not met. The medication history (11/12/2026) shows ezetimibe 10 mg daily since 09/15/2025, but the on-ezetimibe LDL-C of 64 mg/dL (10/15/2026) is below the 70 mg/dL threshold, and the chart does not document any ezetimibe intolerance or contraindication. Please review and tell us whether any other documentation applies.
  - Would satisfy the policy: Policy B.4 accepts either an LDL-C of 70 mg/dL or higher drawn after at least 4 weeks of ezetimibe 10 mg daily (on or after 2025-10-13 for the current course), or documentation of intolerance of or a contraindication to ezetimibe.

## Run cost

3 model calls, 3,589 input and 1,348 output tokens, 20.1 s of model time, $0.043 at list price (2 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: reuse.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3a | B.3(a) | MET | MET | MET | ok |
| C3b | B.3(b) | NOT_MET | NOT_MET | NOT_MET | ok |
| C4 | B.4 | NOT_MET | NOT_MET | NOT_MET | ok |
| C5 | B.5 | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
