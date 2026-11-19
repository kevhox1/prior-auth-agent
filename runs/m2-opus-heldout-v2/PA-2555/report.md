# PA-2555: ustekinumab-ttwe for PT-2555

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 75.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-11-05 states the patient has moderately to severely active ileocolonic Crohn's disease. The problem list records the Crohn's diagnosis (K50.80), which matches the request. (confidence 0.95)

- `PT-2555/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2555/problem-list-2026-11-05` (2026-11-05): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2021."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy mentioned is a colonoscopy from 07/2021, which is outside the 12-month window, and no findings report is on file. Raised calprotectin, raised CRP and the HBI score do not count on their own under the policy. (confidence 0.88)

- `PT-2555/outside-records-2021-12-18` (2021-12-18): "Dx: Crohn's discase, diagnosed 07/2021 by co1onoscopy."
- `PT-2555/labs-2026-09-12` (2026-09-12): "Calprotectin, fecal | 107 ug/g | H | <50"
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ustekinumab order appears in a GI follow-up note, and the request lists the ordering provider as Dr. M. Chen, Gastroenterology. The quoted passage itself does not state the author's specialty, so the reviewer may want to confirm Dr. Chen's credentials. (confidence 0.80)

- `PT-2555/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 75.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

Two documents give the same date of birth, 08/18/1960. That makes the member 66 years old on the request date of 2026-11-18. (confidence 0.98)

- `PT-2555/demographics-2025-12-06` (2025-12-06): "Date of birth: 08/18/1960"
- `PT-2555/outside-records-2021-12-18` (2021-12-18): "PT: ZIELINSKI,  ANDRE     DOB 08/18/1960"
- Code checks: age 66 on 2026-11-18 from DOB 1960-08-18

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Azathioprine (08/2021 to 10/2021) was stopped for intolerance (acute pancreatitis). Budesonide (11/2021 to 02/2022) was stopped for inadequate response. The outside record's treatment history section is blank, but a blank section is not a conflict. (confidence 0.93)

- `PT-2555/medication-history-2026-11-04` (2026-11-04): "| Azathioprine | 2.5 mg/kg daily | 08/2021 | 10/2021 | Intolerance (acute pancreatitis) |"
- `PT-2555/medication-history-2026-11-04` (2026-11-04): "| Budesonide | 9 mg daily | 11/2021 | 02/2022 | Inadequate response after 10 weeks |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab was used from 07/2023 to 06/2026 and stopped for intolerance (drug-induced lupus). The record gives the drug, the dates and the reason for stopping. (confidence 0.93)

- `PT-2555/medication-history-2026-11-04` (2026-11-04): "| Infliximab | 5 mg/kg IV every 8 weeks | 07/2023 | 06/2026 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The IGRA from 2026-09-12, within 6 months, was positive. The 2026-09-15 chest radiograph shows no active TB, and latent TB treatment with rifampin started 09/21/2026, which meets the policy's exception for a positive screen. (confidence 0.90)

- `PT-2555/labs-2026-09-12` (2026-09-12): "QuantiFERON-TB Gold Plus | POSITIVE | A | Negative"
- `PT-2555/chest-xray-2026-09-15` (2026-09-15): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2555/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 09/21/2026."

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

HBsAg resulted nonreactive and total anti-HBc resulted reactive. Because anti-HBc is reactive, a plan is required, and the GI note documents HBV DNA and liver test monitoring every 3 months. (confidence 0.93)

- `PT-2555/labs-2026-09-12` (2026-09-12): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-2555/labs-2026-09-12` (2026-09-12): "Anti-HBc (total) | Reactive | A | Nonreactive"
- `PT-2555/gi-note-2026-11-05` (2026-11-05): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The only current biologic, vedolizumab, is documented as being stopped when ustekinumab starts. The other current medications listed (prednisone, ferrous sulfate) are not biologics, JAK inhibitors or S1P modulators. (confidence 0.90)

- `PT-2555/medication-history-2026-11-04` (2026-11-04): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/24/2026); to be discontinued when ustekinumab starts."
- `PT-2555/gi-note-2026-11-05` (2026-11-05): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 75.6 kg was recorded on 2026-11-05, within 90 days of the request, and falls in the >55 to 85 kg band, so 390 mg IV is the correct induction dose. Maintenance at 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the labeled regimen. (confidence 0.95)

- `PT-2555/gi-note-2026-11-05` (2026-11-05): "Weight 75.6 kg."
- `PT-2555/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 75.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 75.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy) dated on or after 2025-11-18 that documents active mucosal inflammation (who: ordering_provider)
  > Dr. Chen, the ustekinumab-ttwe prior auth for PT-2555 (PA-2555) needs an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from the past 12 months (on or after 2025-11-18) that documents active mucosal inflammation (Calder policy B.2). The only endoscopy on file is the 07/2021 diagnostic colonoscopy, mentioned in outside records dated 2021-12-18, and we have no findings report for it. Under the policy, the 2026-09-12 fecal calprotectin (107 ug/g), CRP and HBI score don't meet this requirement on their own. Has a qualifying endoscopy been done in that window? If so, please send us the report or tell us where it was performed so we can request it.

## Run cost

3 model calls, 20,437 input and 7,862 output tokens, 61.6 s of model time, $0.281 at list price (0 served from cache).

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
