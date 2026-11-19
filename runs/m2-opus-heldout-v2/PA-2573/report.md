# PA-2573: ustekinumab (reference product) for PT-2573

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 61.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note of 2026-11-08 names the diagnosis as Crohn's disease and states it is moderately to severely active. A Harvey-Bradshaw Index of 13 supports this. (confidence 0.95)

- `PT-2573/gi-note-2026-11-08` (2026-11-08): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2573/gi-note-2026-11-08` (2026-11-08): "Harvey-Bradshaw Index today: 13."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy mentioned is the 2021 diagnostic colonoscopy, which is well outside the 12-month window. Calprotectin and CRP are raised, but the policy says lab markers do not count on their own. No recent endoscopy report is in the chart. (confidence 0.88)

- `PT-2573/outside-records-2022-12-18` (2022-12-18): "Dx: Crohn's disease, diagnosed 2021-12 by colonoscopy."
- `PT-2573/labs-2026-09-05` (2026-09-05): "Fecal calprotectin                    527 ug/g      <50"
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated 2025-11-18 or later documenting active mucosal inflammation

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the prescriber as Dr. M. Chen, Gastroenterology. The ustekinumab order appears in the GI follow-up note. (confidence 0.90)

- `PT-2573/gi-note-2026-11-08` (2026-11-08): "1. Start ustekinumab (reference product): 390 mg IV once (weight 61.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 1990-05-21, the member is 36 on the request date of 2026-11-18. The outside records show the same date of birth. (confidence 0.98)

- `PT-2573/demographics-2026-05-31` (2026-05-31): "Date of birth: 1990-05-21"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-21

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate was used from 2022-01 to 2022-07 and stopped for intolerance. Budesonide was used from 2022-08 to 2022-11 and stopped for inadequate response. Both are conventional agents. (confidence 0.95)

- `PT-2573/outside-records-2022-12-18` (2022-12-18): "- Methotrexate 25 mg subcutaneously weekly, 2022-01 to 2022-07. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-2573/outside-records-2022-12-18` (2022-12-18): "- Budesonide 9 mg daily, 2022-08 to 2022-11. Reason stopped: inadequate response after 10 weeks."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab was used from 2023-07 to 2023-11 and stopped for primary non-response, which counts as inadequate response. (confidence 0.95)

- `PT-2573/gi-note-2026-11-08` (2026-11-08): "Prior biologic: Adalimumab 40 mg every 2 weeks, 2023-07 to 2023-11. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON-TB Gold Plus result dated 2026-09-05 is negative. That date is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-2573/labs-2026-09-05` (2026-09-05): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both hepatitis B surface antigen and total core antibody have results, and both are nonreactive. Because neither is reactive, no prophylaxis plan is needed. (confidence 0.96)

- `PT-2573/labs-2026-09-05` (2026-09-05): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-2573/labs-2026-09-05` (2026-09-05): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current note says the member is on no biologic, JAK inhibitor, or S1P receptor modulator; budesonide, a conventional agent, is the only current therapy. Adalimumab was stopped in 2023. (confidence 0.92)

- `PT-2573/gi-note-2026-11-08` (2026-11-08): "Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-2573/gi-note-2026-11-08` (2026-11-08): "Budesonide 9 mg daily (bridge)"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 61.2 kg was recorded on 2026-10-03, within 90 days of the request. That weight falls in the over 55 to 85 kg band, which calls for 390 mg IV, and the maintenance dose of 90 mg SC every 8 weeks matches the label. The reported 3 kg weight loss would still leave the member in the same band. (confidence 0.88)

- `PT-2573/gi-note-2026-10-03` (2026-10-03): "Weight 61.2 kg."
- `PT-2573/gi-note-2026-11-08` (2026-11-08): "1. Start ustekinumab (reference product): 390 mg IV once (weight 61.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 61.2 kg (2026-11-08) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy) dated 2025-11-18 or later showing active mucosal inflammation (who: ordering_provider)
  > Dr. Chen: for PA-2573 (ustekinumab, PT-2573), the Calder policy requires an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from the past 12 months (on or after 2025-11-18) that documents active mucosal inflammation (criterion B.2). The only endoscopy in the chart is the 2021-12 diagnostic colonoscopy. Under this policy, the raised fecal calprotectin (527 ug/g on 2026-09-05) and CRP do not meet the criterion on their own. Has a qualifying endoscopy been done in that window, here or at another facility? If so, please send the report or tell us where it was done so we can request it.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
