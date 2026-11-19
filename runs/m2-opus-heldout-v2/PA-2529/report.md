# PA-2529: ustekinumab-ttwe for PT-2529

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 110.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The 2026-11-03 GI note says the patient has Crohn's disease and that it is moderately to severely active. The problem list also shows Crohn's disease (K50.80). (confidence 0.95)

- `PT-2529/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The colonoscopy on 2026-08-13 is about 3 months before the request, so it is inside the 12-month window. It found ulcers with erythema and edema in the terminal ileum, which is active mucosal inflammation. The pathology also shows chronic active inflammation. (confidence 0.95)

- `PT-2529/colonoscopy-2026-08-13` (2026-08-13): "PROCEDURE: Colonoscopy with biopsies"
- `PT-2529/colonoscopy-2026-08-13` (2026-08-13): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request names the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab plan is in a GI follow-up note. The quoted line itself does not name the author or specialty, so the reviewer should check the note's signature. (confidence 0.80)

- `PT-2529/gi-note-2026-11-03` (2026-11-03): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 110.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The date of birth is 1993-06-19, so the member is 33 on the request date of 2026-11-18. That meets the 18-or-older requirement. (confidence 0.97)

- `PT-2529/demographics-2025-10-24` (2025-10-24): "Date of birth: 1993-06-19"
- Code checks: age 33 on 2026-11-18 from DOB 1993-06-19

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Azathioprine was used from 2021-03 to 2021-05 and stopped because of intolerance (acute pancreatitis). Prednisone was used from 2021-06 to 2021-12, and the patient flared each time the dose went below 15 mg, which shows an inadequate response. (confidence 0.93)

- `PT-2529/medication-history-2026-11-03` (2026-11-03): "| Azathioprine | 2.5 mg/kg daily | 2021-03 | 2021-05 | Intolerance (acute pancreatitis) |"
- `PT-2529/medication-history-2026-11-03` (2026-11-03): "| Prednisone | 40 mg daily, tapered | 2021-06 | 2021-12 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab was used from 2023-07 to 2026-07. It was stopped because of intolerance (drug-induced lupus). (confidence 0.93)

- `PT-2529/medication-history-2026-11-03` (2026-11-03): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON (IGRA) on 2026-10-10 was negative. That date is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-2529/labs-2026-10-10` (2026-10-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

There are resulted tests for both hepatitis B surface antigen and total core antibody, and both are nonreactive. Because neither is reactive, no prophylaxis or monitoring plan is needed. (confidence 0.96)

- `PT-2529/labs-2026-10-10` (2026-10-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2529/labs-2026-10-10` (2026-10-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The medication history says the patient is on no biologic or small-molecule advanced therapy now. The earlier biologic, adalimumab, was stopped in 2026-07. Budesonide is a conventional agent, not an excluded therapy. (confidence 0.90)

- `PT-2529/medication-history-2026-11-03` (2026-11-03): "- No biologic or small-molecule advanced therapy at present."
- `PT-2529/medication-history-2026-11-03` (2026-11-03): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 110.7 kg was recorded on 2026-11-03, within 90 days of the request. Above 85 kg the labeled IV dose is 520 mg, which matches the request. The 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the labeled maintenance schedule. (confidence 0.95)

- `PT-2529/gi-note-2026-11-03` (2026-11-03): "Weight 110.7 kg."
- `PT-2529/gi-note-2026-11-03` (2026-11-03): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 110.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 110.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

## Run cost

2 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (2 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: clean.

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
