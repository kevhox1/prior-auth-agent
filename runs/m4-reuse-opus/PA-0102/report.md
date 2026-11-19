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

No clinical ASCVD is documented, so the claim rests on HeFH, and genetic testing was not done. The DLCN score of 8 counts 4 points for corneal arcus before age 45, but the arcus was found on today's exam at age 54 and no earlier record is on file. Without those points the score is 4, below 6. The LDL-C points also rest on outside records that are not on file. (confidence 0.70)

- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Dutch Lipid Clinic Network score 8: LDL-C 190-249 (3), premature CAD in a first-degree relative (1), corneal arcus before age 45 (4). Probable FH. Genetic testing not done."
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Bilateral corneal arcus. No tendon xanthomas."
- `PT-0102/demographics-2026-11-05` (2026-11-05): "Date of birth: 03/19/1972"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Untreated LDL-C 236 mg/dL (2019, outside records not on file)."
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Heterozygous familial hypercholesterolemia without known ASCVD."
- Missing: Genetic test result confirming HeFH
- Missing: OR documentation of corneal arcus before age 45 (arcus was first recorded at the 11/05/2026 exam, at age 54)
- Missing: Source record for the 2019 untreated LDL-C of 236 mg/dL used in the DLCN score

### C2 (policy B.2): **NOT MET**
_An LDL-C result drawn in the 3 months before the request, while the member was on the lipid-lowering therapy described in B.3 and B.4, is at or above the member's threshold. The threshold is 70 mg/dL for a member with clinical ASCVD, or 100 mg/dL for a member with HeFH and no clinical ASCVD. An LDL-C drawn before the current lipid-lowering regimen was started does not meet this requirement._

The LDL-C of 188 mg/dL from 10/21/2026 is within 3 months and above either threshold. However, it was drawn on ezetimibe alone, with no statin. The B.3 statin requirement is not satisfied by a qualifying statin or a qualifying documented intolerance, so the draw was not on the B.3/B.4 regimen the policy requires. (confidence 0.60)

- `PT-0102/labs-2026-10-21` (2026-10-21): "LDL cholesterol, calculated         188 mg/dL     <100"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "LDL-C 188 mg/dL on 10/21/2026 on ezetimibe 10 mg daily (since 03/2022). TSH normal."
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "LDL-C far above goal on ezetimibe alone."

### C3 (policy B.3): **NOT MET**
_The member is on maximally tolerated statin therapy, shown by either (a) or (b). One is enough. For any claimed intolerance, the record must describe each statin's drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement._

**C3a (policy B.3(a)): **NOT MET****: The member takes a high-intensity statin (atorvastatin 40 to 80 mg daily or rosuvastatin 20 to 40 mg daily), or the highest statin dose the member tolerates when a higher dose caused a documented adverse effect. The member has taken it for at least 8 weeks before the B.2 LDL-C and will continue it with evolocumab. Any intolerance of a higher dose must be described with the drug, dose, symptom or adverse effect, and improvement after stopping or reducing it. A bare "statin intolerant" statement does not count.

The member is not on any statin now. The only statin, simvastatin 20 mg, was stopped in 2021, and the plan does not continue a statin with evolocumab. (confidence 0.92)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "| Simvastatin | 20 mg nightly | 2021-04 | 2021-06 | Stopped: muscle aches in both thighs |"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "LDL-C far above goal on ezetimibe alone."
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "2. Continue ezetimibe 10 mg daily."

**C3b (policy B.3(b)): **NOT MET****: The member cannot take a statin for one of two reasons. (i) Intolerance of at least two different statins, at least one of them at the lowest approved starting dose. (ii) A contraindication, meaning a history of statin-associated rhabdomyolysis or active liver disease. For each statin, the intolerance must be described with the drug, dose, symptom or adverse effect, and improvement after the statin was stopped or reduced. A statement such as "statin intolerant" without these details does not meet this requirement.

The reconciled history shows only one statin trial (simvastatin 20 mg, thigh aches), and it does not record improvement after stopping. The policy requires at least two statins. The other entries are bare "statin intolerance" statements, which do not count, and no rhabdomyolysis or active liver disease is documented. (confidence 0.85)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "| Simvastatin | 20 mg nightly | 2021-04 | 2021-06 | Stopped: muscle aches in both thighs |"
- `PT-0102/medication-history-2026-11-05` (2026-11-05): "LIPID-LOWERING MEDICATION HISTORY - reconciled against pharmacy fill history 11/05/2026 (fill history available from 2021 onward)"
- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Statin intolerant (myalgias on simvastatin)."
- `PT-0102/problem-list-2026-11-05` (2026-11-05): "2. Statin intolerance."

### C4 (policy B.4): MET
_The member has taken ezetimibe 10 mg daily for at least 4 weeks, now or in the past, and LDL-C stayed at or above the B.2 threshold. Alternatively, the record documents intolerance of or a contraindication to ezetimibe._

The member has taken ezetimibe 10 mg daily since 03/2022 with on-time fills, far more than 4 weeks. LDL-C on 10/21/2026 was 188 mg/dL, above both the 70 and 100 mg/dL thresholds. (confidence 0.88)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "| Ezetimibe | 10 mg daily | 2022-03 | ongoing | Fills on time |"
- `PT-0102/labs-2026-10-21` (2026-10-21): "LDL cholesterol, calculated         188 mg/dL     <100"

### C5 (policy B.5): MET
_The prescriber is a cardiologist, an endocrinologist, or a lipid specialist, or the prescriber has consulted with one about this treatment._

The prescriber, Dr. J. Varga, is a cardiologist in a lipid clinic. (confidence 0.97)

- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "Electronically signed by Dr. J. Varga, MD, Cardiology (Lipid Clinic), 11/05/2026"

### C6 (policy B.6): MET
_The member is at least 18 years old on the date of the request._

Born 03/19/1972, the member is 54 on the request date of 2026-11-18. (confidence 0.98)

- `PT-0102/demographics-2026-11-05` (2026-11-05): "Date of birth: 03/19/1972"
- Code checks: age 54 on 2026-11-18 from DOB 1972-03-19

### C7 (policy B.7): MET
_Evolocumab will not be combined with another PCSK9-directed therapy (alirocumab or inclisiran). When the member is switching from one of these, the record shows the earlier agent is stopping._

The reconciled medication history shows no current or prior alirocumab, evolocumab or inclisiran, so there is no combined use and no switch. (confidence 0.93)

- `PT-0102/medication-history-2026-11-05` (2026-11-05): "No current or prior PCSK9 inhibitor (alirocumab, evolocumab) or inclisiran."

### C8 (policy B.8): MET
_The requested regimen is a labeled adult regimen: 140 mg under the skin every 2 weeks, or 420 mg under the skin once a month._

The ordered regimen, 140 mg SC every 2 weeks, is a labeled adult regimen and matches the request. (confidence 0.97)

- `PT-0102/lipid-clinic-note-2026-11-05` (2026-11-05): "1. Start evolocumab 140 mg subcutaneously every 2 weeks."

## To-do list (gap plan)

- **C1**: Qualifying HeFH confirmation: a genetic test result, or a DLCN score of 6 or higher supported by source records (who: ordering_provider)
  > Dr. Varga, for PT-0102 (evolocumab, criterion B.1 HeFH): the 11/05/2026 lipid clinic note scores the DLCN at 8, including 4 points for corneal arcus before age 45. The only arcus finding on file is from the 11/05/2026 exam, when the patient was 54 (DOB 03/19/1972). Without those 4 points the score is 4. The 2019 untreated LDL-C of 236 mg/dL also comes from outside records that are not on file. Could you review the score and send any records that support it?
  - Would satisfy the policy: Policy B.1 accepts HeFH confirmed by a genetic test result, or a DLCN score of 6 or higher. Each scored item must be supported in the record, for example arcus documented before age 45 (before 2017-03-19) and the source lab report for the 2019 untreated LDL-C of 236 mg/dL.
- **C2**: LDL-C drawn while on a lipid-lowering regimen that meets B.3/B.4 (who: ordering_provider)
  > Dr. Varga, for PT-0102 (criterion B.2): the 10/21/2026 LDL-C of 188 mg/dL is recent enough and above the threshold. However, it was drawn on ezetimibe 10 mg alone, and the statin requirement in B.3 is not currently met. Please review whether this result was drawn on a regimen that meets the policy.
  - Would satisfy the policy: Policy B.2 accepts an LDL-C of 100 mg/dL or higher (HeFH without ASCVD) drawn on or after 2026-08-18, while the member was on therapy that meets B.3 and B.4. The 10/21/2026 result would count if B.3 is satisfied, for example through documented intolerance of two statins under B.3(b).
- **C3a**: Current high-intensity or maximally tolerated statin continued with evolocumab (who: ordering_provider)
  > Dr. Varga, for PT-0102 (criterion B.3(a)): the record shows no current statin. The only statin, simvastatin 20 mg nightly, was stopped in 06/2021, and the 11/05/2026 plan lists ezetimibe 10 mg daily with no statin. Please review and confirm this is accurate.
- **C3b**: Detailed record of intolerance to a second statin (and improvement after stopping simvastatin), or a documented contraindication (who: ordering_provider)
  > Dr. Varga, for PT-0102 (criterion B.3(b)): the reconciled medication history from 11/05/2026 shows one statin trial, simvastatin 20 mg nightly (04/2021–06/2021, thigh aches). It does not record whether symptoms improved after stopping. Fill history only goes back to 2021. The other entries are general 'statin intolerance' statements. Please review whether other statin trials, or a history of rhabdomyolysis or active liver disease, are documented anywhere.
  - Would satisfy the policy: Policy B.3(b) accepts documented intolerance of at least two different statins, at least one at the lowest approved starting dose. Each must be recorded with the drug, dose, symptom and improvement after stopping or reducing it. It also accepts a documented history of statin-associated rhabdomyolysis or active liver disease. A statement such as 'statin intolerant' alone is not accepted.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent NEEDS_PHYSICIAN. Case type: reuse.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C2 | B.2 | MET | NOT_MET | NOT_MET | wrong |
| C3a | B.3(a) | NOT_MET | NOT_MET | NOT_MET | ok |
| C3b | B.3(b) | INSUFFICIENT_EVIDENCE | NOT_MET | NOT_MET | ok (alternate) |
| C4 | B.4 | MET | MET | MET | ok |
| C5 | B.5 | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
