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

The cardiologist documents clinical ASCVD and names the event: an ischemic stroke from large-artery atherosclerosis, followed by carotid endarterectomy. The outside discharge summary confirms the stroke was atherosclerotic, which qualifies under B.1. (confidence 0.96)

- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Clinical ASCVD: ischemic stroke from large-artery atherosclerosis, status post carotid endarterectomy, with diabetes. Very high risk."
- `PT-0103/outside-records-2025-04-09` (2025-04-09): "Acute ischemic stroke, left middle cerebral artery territory, due to large-artery atherosclerosis (70% stenosis of the left internal carotid artery)."

### C2 (policy B.2): **NOT MET**
_An LDL-C result drawn in the 3 months before the request, while the member was on the lipid-lowering therapy described in B.3 and B.4, is at or above the member's threshold. The threshold is 70 mg/dL for a member with clinical ASCVD, or 100 mg/dL for a member with HeFH and no clinical ASCVD. An LDL-C drawn before the current lipid-lowering regimen was started does not meet this requirement._

The only LDL-C in the 3-month window (drawn 10/15/2026 on rosuvastatin and ezetimibe) is 64 mg/dL, which is below the 70 mg/dL threshold for ASCVD. The 152 mg/dL value was drawn off therapy in 04/2025, so it does not count. The prescriber's own 55 mg/dL target is not the policy threshold. (confidence 0.93)

- `PT-0103/labs-2026-10-15` (2026-10-15): "LDL cholesterol, calculated         64 mg/dL      <100"
- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Lipid panel 10/15/2026: LDL-C 64 mg/dL on rosuvastatin 40 mg and ezetimibe 10 mg. LDL-C at the stroke admission was 152 mg/dL off therapy."
- `PT-0103/outside-records-2025-04-09` (2025-04-09): "LDL cholesterol 152 mg/dL (on no lipid-lowering therapy). Hemoglobin A1c 7.4%."

### C3 (policy B.3): MET
_The member is on maximally tolerated statin therapy, shown by either (a) or (b). One is enough. For any claimed intolerance, the record must describe each statin's drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement._

**C3a (policy B.3(a)): MET**: The member takes a high-intensity statin (atorvastatin 40 to 80 mg daily or rosuvastatin 20 to 40 mg daily), or the highest statin dose the member tolerates when a higher dose caused a documented adverse effect. The member has taken it for at least 8 weeks before the B.2 LDL-C and will continue it with evolocumab. Any intolerance of a higher dose must be described with the drug, dose, symptom or adverse effect, and improvement after stopping or reducing it. A bare "statin intolerant" statement does not count.

The member has taken rosuvastatin 40 mg daily, a high-intensity dose, since 04/09/2025. That is well over 8 weeks before the 10/15/2026 LDL-C draw. The plan says rosuvastatin will continue with evolocumab. (confidence 0.93)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "| Rosuvastatin | 40 mg daily | 2025-04-09 | ongoing | Started at stroke discharge. Fills on time. No side effects reported. |"
- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "1. Add evolocumab 140 mg subcutaneously every 2 weeks to reach LDL-C below 55 mg/dL. Continue rosuvastatin 40 mg and ezetimibe 10 mg."

**C3b (policy B.3(b)): **NOT MET****: The member cannot take a statin for one of two reasons. (i) Intolerance of at least two different statins, at least one of them at the lowest approved starting dose. (ii) A contraindication, meaning a history of statin-associated rhabdomyolysis or active liver disease. For each statin, the intolerance must be described with the drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement.

The member tolerates rosuvastatin 40 mg with no side effects reported. The chart documents no intolerance to two statins, no rhabdomyolysis and no active liver disease, and ALT is normal. This path does not apply; C3 may still be satisfied through C3a. (confidence 0.85)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "| Rosuvastatin | 40 mg daily | 2025-04-09 | ongoing | Started at stroke discharge. Fills on time. No side effects reported. |"
- `PT-0103/labs-2026-10-15` (2026-10-15): "ALT                                   24 U/L        7-56"

### C4 (policy B.4): **NOT MET**
_The member has taken ezetimibe 10 mg daily for at least 4 weeks, now or in the past, and LDL-C stayed at or above the B.2 threshold. Alternatively, the record documents intolerance of or a contraindication to ezetimibe._

Ezetimibe 10 mg daily has been taken since 09/15/2025, which is more than 4 weeks. However, LDL-C on it is 64 mg/dL, below the 70 mg/dL threshold, so LDL-C did not stay at or above the threshold. No ezetimibe intolerance or contraindication is documented. (confidence 0.85)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "| Ezetimibe | 10 mg daily | 2025-09-15 | ongoing | Fills on time. |"
- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Lipid panel 10/15/2026: LDL-C 64 mg/dL on rosuvastatin 40 mg and ezetimibe 10 mg. LDL-C at the stroke admission was 152 mg/dL off therapy."

### C5 (policy B.5): MET
_The prescriber is a cardiologist, an endocrinologist, or a lipid specialist, or the prescriber has consulted with one about this treatment._

The prescriber, Dr. M. Osei, signs as Cardiology, which is a qualifying specialty. (confidence 0.97)

- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "Electronically signed by Dr. M. Osei, MD, Cardiology, 11/12/2026"

### C6 (policy B.6): MET
_The member is at least 18 years old on the date of the request._

Born 01/08/1959, the member is 67 years old on the 2026-11-18 request date, which is above 18. (confidence 0.98)

- `PT-0103/demographics-2026-11-12` (2026-11-12): "Date of birth: 01/08/1959"
- Code checks: age 67 on 2026-11-18 from DOB 1959-01-08

### C7 (policy B.7): MET
_Evolocumab will not be combined with another PCSK9-directed therapy (alirocumab or inclisiran). When the member is switching from one of these, the record shows the earlier agent is stopping._

The reconciled medication history states there is no current or prior alirocumab or inclisiran, so no PCSK9-directed therapy will be combined with evolocumab. (confidence 0.95)

- `PT-0103/medication-history-2026-11-12` (2026-11-12): "No current or prior PCSK9 inhibitor (alirocumab, evolocumab) or inclisiran."

### C8 (policy B.8): MET
_The requested regimen is a labeled adult regimen: 140 mg under the skin every 2 weeks, or 420 mg under the skin once a month._

The ordered regimen, 140 mg subcutaneously every 2 weeks, is a labeled adult regimen and matches the request. (confidence 0.97)

- `PT-0103/cardiology-note-2026-11-12` (2026-11-12): "1. Add evolocumab 140 mg subcutaneously every 2 weeks to reach LDL-C below 55 mg/dL. Continue rosuvastatin 40 mg and ezetimibe 10 mg."

## To-do list (gap plan)

- **C2**: LDL-C at or above 70 mg/dL on current therapy, drawn within 3 months before request (who: ordering_provider)
  > Dr. Osei, for PT-0103's evolocumab request (PA-0103), policy B.2 is not met. The only LDL-C in the 3-month window is 64 mg/dL (labs 2026-10-15, on rosuvastatin 40 mg and ezetimibe 10 mg). The ASCVD threshold is 70 mg/dL. The 152 mg/dL value from 2025-04-09 was drawn off therapy and does not count, and the 55 mg/dL target in your 2026-11-12 note is not the policy threshold. Please review and tell us how you want to proceed.
  - Would satisfy the policy: Policy B.2 accepts an LDL-C of 70 mg/dL or higher (clinical ASCVD threshold) drawn on the current lipid-lowering regimen within the 3 months before the request, i.e. dated 2026-08-18 through 2026-11-18 for this request date.
- **C4**: LDL-C at or above 70 mg/dL after 4 or more weeks of ezetimibe, or documented ezetimibe intolerance or contraindication (who: ordering_provider)
  > Dr. Osei, for PT-0103 (PA-0103), policy B.4 is not met. The medication history from 2026-11-12 shows ezetimibe 10 mg daily since 2025-09-15, but LDL-C on it was 64 mg/dL (2026-10-15), below the 70 mg/dL threshold. The chart documents no ezetimibe intolerance or contraindication. Please review this criterion.
  - Would satisfy the policy: Policy B.4 accepts either an LDL-C of 70 mg/dL or higher after at least 4 weeks of ezetimibe 10 mg daily, or chart documentation of ezetimibe intolerance or contraindication.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

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
