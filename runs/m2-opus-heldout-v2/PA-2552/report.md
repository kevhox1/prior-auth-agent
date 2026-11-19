# PA-2552: ustekinumab-ttwe for PT-2552

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The prescriber's GI note of 2026-10-31 says the patient has moderately to severely active ileocolonic Crohn's disease. That covers both the diagnosis and the severity. (confidence 0.96)

- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The chart has only lab markers: fecal calprotectin and CRP. The policy says these do not meet the requirement on their own. No colonoscopy, ileocolonoscopy or sigmoidoscopy report from the past 12 months was found. (confidence 0.90)

- `PT-2552/labs-2026-09-26` (2026-09-26): "Calprotectin, fecal | 76 ug/g | H | <50"
- `PT-2552/labs-2026-09-26` (2026-09-26): "CRP | 16.0 mg/L | H | <5.0"
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. M. Chen, Gastroenterology. The ustekinumab plan is written in a GI follow-up note. This supports a gastroenterology prescriber. (confidence 0.88)

- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth in 1957, the member is about 69 years old on the request date of 2026-11-18. That is well over 18. (confidence 0.98)

- `PT-2552/demographics-2026-08-05` (2026-08-05): "Date of birth: 04/03/1957"
- Code checks: age 69 on 2026-11-18 from DOB 1957-04-03

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate (01/2021 to 06/2021) was stopped for intolerance. Prednisone (05/2020 to 12/2020) was stopped for steroid dependence, which counts as inadequate response. Both entries give the drug, dates and reason. (confidence 0.95)

- `PT-2552/gi-note-2026-06-17` (2026-06-17): "- History: Methotrexate 25 mg subcutaneously weekly, 01/2021 to 06/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-2552/gi-note-2026-06-17` (2026-06-17): "- History: Prednisone 40 mg daily, tapered, 05/2020 to 12/2020. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab was used from 07/2023 to 08/2026. It was stopped for intolerance (drug-induced lupus). (confidence 0.95)

- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 08/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

A QuantiFERON test was ordered on 2026-10-31, but no result is in the chart. An order is not a result. (confidence 0.93)

- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- QuantiFERON-TB Gold Plus ordered today."
- Missing: Resulted IGRA (QuantiFERON-TB Gold Plus) or TST dated on or after 2026-05-18

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

No hepatitis B results were found in the passages. There is neither a surface antigen nor a total core antibody result. (confidence 0.92)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The 2026-10-31 note says the patient is on no current biologic, JAK inhibitor or S1P receptor modulator. Infliximab was stopped in 08/2026. (confidence 0.92)

- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 08/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 55.0 kg was recorded on 2026-10-31, within 90 days of the request. 55 kg falls in the 260 mg band (up to and including 55 kg). The 90 mg SC every 8 weeks maintenance, starting 8 weeks after the infusion, matches the label. (confidence 0.94)

- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- Weight 55.0 kg."
- `PT-2552/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-31) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy) dated 2025-11-18 or later showing active mucosal inflammation (who: practice_staff)
  > For the ustekinumab prior auth for PT-2552 (PA-2552), criterion C2 needs an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report dated 2025-11-18 or later that documents active mucosal inflammation. The chart has only the fecal calprotectin (76 ug/g) and CRP (16.0 mg/L) from 2026-09-26, and the policy says lab markers and imaging do not count on their own. Can you find and file a qualifying endoscopy report, including one done at an outside facility? If no such study exists, please let Dr. Chen know.
- **C6**: Resulted QuantiFERON-TB Gold Plus (or TST) dated 2026-05-18 or later (who: lab)
  > For PT-2552's ustekinumab prior auth (PA-2552), criterion C6 needs a resulted TB screen from within the past 6 months. Dr. Chen's GI note of 2026-10-31 shows a QuantiFERON-TB Gold Plus was ordered, but no result is in the chart. Please confirm whether the specimen was collected and send the final result. Indeterminate or borderline results do not count as negative.
- **C7**: Hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results (who: practice_staff)
  > For PT-2552's ustekinumab prior auth (PA-2552), criterion C7 needs results for both hepatitis B surface antigen and total hepatitis B core antibody. Results of any age are accepted, but surface antibody results, vaccination records and pending orders are not. No hepatitis B results were found in the chart. Please search past and outside records for both results and file them, or tell Dr. Chen if they have never been drawn.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | B.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
