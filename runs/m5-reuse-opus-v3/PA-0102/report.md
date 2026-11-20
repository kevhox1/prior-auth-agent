# PA-0102: evolocumab for PT-0102

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-evolocumab-lipids version 2026-09
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: decision within 72 hours of receiving all required information (policy section E).
- Ordered dose: 140 mg subcutaneously every 2 weeks
- Benefit routing: sc_injection -> pharmacy

## Checklist

### C1 (policy B.1): **INSUFFICIENT**
_The prescriber documents in the clinical record that the member has one of two conditions. The first is clinical ASCVD, meaning a prior myocardial infarction or acute coronary syndrome, coronary or other arterial revascularization, stable or unstable angina with documented coronary artery disease, ischemic stroke or TIA of atherosclerotic origin, or symptomatic peripheral artery disease. The second is heterozygous familial hypercholesterolemia (HeFH) confirmed by genetic testing or by a Dutch Lipid Clinic Network score of 6 or higher._

No ASCVD is documented, and no genetic testing was done, so HeFH rests on the DLCN score of 8. Of those 8 points, 4 are for arcus before age 45, but the only arcus finding in the chart is from the 11/05/2026 exam, when the patient was 54. Without those points the score is 4, which is below 6, and the untreated LDL behind the LDL points has no source document in the chart. (confidence 0.60)

- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Dutch Lipid Clinic Network score 8: LDL-C 190-249 (3), premature CAD in a first-degree relative (1), corneal arcus before age 45 (4). Probable FH. Genetic testing not done."
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Bilateral corneal arcus. No tendon xanthomas."
- `PT-0102/demographics-2026-11-05` (2026-11-05): "Date of birth: 03/19/1972"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Untreated LDL-C 236 mg/dL (2019, outside records not on file)."
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Heterozygous familial hypercholesterolemia without known ASCVD."
- Missing: Documentation that corneal arcus was present before age 45 (arcus is recorded only at the 11/05/2026 exam, age 54), or a genetic test result confirming FH
- Missing: Source record for the 2019 untreated LDL-C of 236 mg/dL used for the DLCN LDL points

### C2 (policy B.2): MET
_An LDL-C result drawn in the 3 months before the request, while the member was on the lipid-lowering therapy described in B.3 and B.4, is at or above the member's threshold. The threshold is 70 mg/dL for a member with clinical ASCVD, or 100 mg/dL for a member with HeFH and no clinical ASCVD. An LDL-C drawn before the current lipid-lowering regimen was started does not meet this requirement._

LDL-C was 188 mg/dL, drawn 10/21/2026, which is within 3 months of the 11/18/2026 request. That is above both the 100 (HeFH) and 70 (ASCVD) thresholds. It was drawn on the current regimen, ezetimibe since 03/2022; the lack of a statin is judged separately under C3. (confidence 0.72)

- `PT-0102/labs-2026-10-21` (2026-10-21): "LDL cholesterol, calculated         188 mg/dL     <100"
- `PT-0102/labs-2026-10-21` (2026-10-21): "COLLECTED: 10/21/2026 08:32      ORDERING: Dr. J. Varga"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "LDL-C 188 mg/dL on 10/21/2026 on ezetimibe 10 mg daily (since 03/2022). TSH normal."

### C3 (policy B.3): **NOT MET**
_The member is on maximally tolerated statin therapy, shown by either (a) or (b). One is enough. For any claimed intolerance, the record must describe each statin's drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement._

**C3a (policy B.3(a)): **NOT MET****: The member takes a high-intensity statin (atorvastatin 40 to 80 mg daily or rosuvastatin 20 to 40 mg daily), or the highest statin dose the member tolerates when a higher dose caused a documented adverse effect. The member has taken it for at least 8 weeks before the B.2 LDL-C and will continue it with evolocumab. Any intolerance of a higher dose must be described with the drug, dose, symptom or adverse effect, and improvement after stopping or reducing it. A bare "statin intolerant" statement does not count.

The patient takes no statin now. The only statin, simvastatin 20 mg, was stopped in 2021. The plan does not include a statin to continue alongside evolocumab. (confidence 0.92)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "| Simvastatin | 20 mg nightly | 2021-04 | 2021-06 | Stopped: muscle aches in both thighs |"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "LDL-C far above goal on ezetimibe alone."
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "2. Continue ezetimibe 10 mg daily."

**C3b (policy B.3(b)): **NOT MET****: The member cannot take a statin for one of two reasons. (i) Intolerance of at least two different statins, at least one of them at the lowest approved starting dose. (ii) A contraindication, meaning a history of statin-associated rhabdomyolysis or active liver disease. For each statin, the intolerance must be described with the drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement.

The reconciled medication history shows only one statin trial, simvastatin 20 mg, and does not record improvement after stopping it. The policy requires at least two statins. The 'statin intolerance' entries are bare statements, and no rhabdomyolysis or active liver disease is documented. (confidence 0.82)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "| Simvastatin | 20 mg nightly | 2021-04 | 2021-06 | Stopped: muscle aches in both thighs |"
- `PT-0102/medication-history-2026-11-05` (2026-11-05): "LIPID-LOWERING MEDICATION HISTORY - reconciled against pharmacy fill history 11/05/2026 (fill history available from 2021 onward)"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Statin intolerant (myalgias on simvastatin)."
- `PT-0102/problem-list-2026-11-05` (2026-11-05): "2. Statin intolerance."

### C4 (policy B.4): MET
_The member has taken ezetimibe 10 mg daily for at least 4 weeks, now or in the past, and LDL-C stayed at or above the B.2 threshold. Alternatively, the record documents intolerance of or a contraindication to ezetimibe._

The patient has filled ezetimibe 10 mg daily on time since 03/2022, which is well over 4 weeks. LDL-C on ezetimibe was 188 mg/dL on 10/21/2026, above the threshold. (confidence 0.90)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "| Ezetimibe | 10 mg daily | 2022-03 | ongoing | Fills on time |"
- `PT-0102/labs-2026-10-21` (2026-10-21): "LDL cholesterol, calculated         188 mg/dL     <100"

### C5 (policy B.5): MET
_The prescriber is a cardiologist, an endocrinologist, or a lipid specialist, or the prescriber has consulted with one about this treatment._

The prescriber, Dr. J. Varga, is a cardiologist in the lipid clinic. (confidence 0.97)

- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Electronically signed by Dr. J. Varga, MD, Cardiology (Lipid Clinic), 11/05/2026"

### C6 (policy B.6): MET
_The member is at least 18 years old on the date of the request._

With a date of birth of 03/19/1972, the member is 54 on the 11/18/2026 request date. (confidence 0.98)

- `PT-0102/demographics-2026-11-05` (2026-11-05): "Date of birth: 03/19/1972"
- Code checks: age 54 on 2026-11-18 from DOB 1972-03-19

### C7 (policy B.7): MET
_Evolocumab will not be combined with another PCSK9-directed therapy (alirocumab or inclisiran). When the member is switching from one of these, the record shows the earlier agent is stopping._

The reconciled medication history shows no current or prior alirocumab or inclisiran, so there is no combined PCSK9 therapy and nothing to switch from. (confidence 0.93)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "No current or prior PCSK9 inhibitor (alirocumab, evolocumab) or inclisiran."

### C8 (policy B.8): MET
_The requested regimen is a labeled adult regimen: 140 mg under the skin every 2 weeks, or 420 mg under the skin once a month._

The requested regimen, 140 mg subcutaneously every 2 weeks, is a labeled adult regimen and matches the clinic plan. (confidence 0.97)

- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "1. Start evolocumab 140 mg subcutaneously every 2 weeks."

## To-do list (gap plan)

- **C1**: Records showing corneal arcus before age 45, or a genetic test confirming FH; plus the source record for the 2019 untreated LDL-C of 236 mg/dL (who: outside_provider)
  > For PT-0102's evolocumab request (criterion B.1, HeFH), the 11/05/2026 lipid clinic note gives a DLCN score of 8, with 4 points for 'corneal arcus before age 45'. The only arcus finding in the chart is from the 11/05/2026 exam, when the patient was 54 (DOB 03/19/1972). Without those 4 points the score is 4. Can you send any earlier exam or outside record that documents arcus before age 45, or any genetic test result for FH? Please also send the 2019 outside lab report showing the untreated LDL-C of 236 mg/dL, which the note lists as 'outside records not on file'.
  - Would satisfy the policy: Policy B.1 accepts HeFH confirmed by a genetic test, or by a DLCN score of 6 or higher in which each scored item has a source record (for example, a dated exam showing corneal arcus before age 45 and the source lab report for the untreated LDL-C). It also accepts documented clinical ASCVD. The policy sets no date window for these records.
- **C3a**: A current high-intensity or maximally tolerated statin that will continue with evolocumab (who: ordering_provider)
  > For PT-0102's evolocumab request (criterion B.3(a)), the medication history reconciled on 11/05/2026 shows no current statin. The only statin listed is simvastatin 20 mg, taken 2021-04 to 2021-06 and stopped for thigh aches. The 11/05/2026 plan continues ezetimibe 10 mg alone. Dr. Varga, please review and confirm whether this reflects the current regimen.
- **C3b**: Documented intolerance to a second, different statin (with dose, symptom and improvement after stopping), or a documented statin contraindication (who: ordering_provider)
  > For PT-0102's evolocumab request (criterion B.3(b)), the chart shows one statin trial: simvastatin 20 mg nightly, 2021-04 to 2021-06, stopped for 'muscle aches in both thighs'. The chart does not record whether the symptoms improved after stopping. The pharmacy fill history only goes back to 2021, and 'statin intolerance' appears in the problem list without details. Dr. Varga, please review: were there any other statin trials, including before 2021? Did the myalgias improve after simvastatin was stopped? Is there any history of statin-associated rhabdomyolysis or active liver disease?
  - Would satisfy the policy: Policy B.3(b) accepts documented intolerance to at least two different statins, at least one of them at the lowest approved starting dose. For each statin, the record must give the drug, the dose, the symptom or adverse effect, and improvement after the statin was stopped or reduced. Alternatively, the policy accepts a documented contraindication: a history of statin-associated rhabdomyolysis or active liver disease. The policy sets no date window for these records.

## Run cost

3 model calls, 4,826 input and 2,061 output tokens, 20.7 s of model time, $0.067 at list price (2 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent NEEDS_PHYSICIAN. Case type: reuse.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3a | B.3(a) | NOT_MET | NOT_MET | NOT_MET | ok |
| C3b | B.3(b) | INSUFFICIENT_EVIDENCE | NOT_MET | NOT_MET | ok (alternate) |
| C4 | B.4 | MET | MET | MET | ok |
| C5 | B.5 | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
