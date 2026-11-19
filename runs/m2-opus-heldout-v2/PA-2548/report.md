# PA-2548: ustekinumab-ttwe for PT-2548

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 111.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The prescriber's GI note of 2026-11-10 says the Crohn's disease is moderately to severely active. The problem list records the Crohn's diagnosis (K50.80). (confidence 0.95)

- `PT-2548/gi-note-2026-11-10` (2026-11-10): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2548/problem-list-2026-11-10` (2026-11-10): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2020."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy on file is the colonoscopy of 2025-04-18. That is about 19 months before the 2026-11-18 request, outside the 12-month window. The CRP from 2026-09-21 is a lab marker, and the policy says lab markers do not meet this requirement on their own. (confidence 0.75)

- `PT-2548/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-2548/labs-2026-09-21` (2026-09-21): "CRP | 26.3 mg/L | H | <5.0"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. M. Chen, Gastroenterology. The ustekinumab order is written in a GI follow-up note. The quoted chart text does not itself state the prescriber's specialty, so the reviewer may want to confirm it. (confidence 0.85)

- `PT-2548/gi-note-2026-11-10` (2026-11-10): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 111.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The date of birth is 1964-01-08, so the member is 62 on the 2026-11-18 request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-2548/demographics-2026-01-01` (2026-01-01): "Date of birth: 1964-01-08"
- Code checks: age 62 on 2026-11-18 from DOB 1964-01-08

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate was used from 2020-05 to 2020-09 and stopped for intolerance (nausea and raised ALT). The blank treatment history in the 2020 outside records is an omission, not a conflict. (confidence 0.90)

- `PT-2548/medication-history-2026-11-10` (2026-11-10): "| Methotrexate | 25 mg subcutaneously weekly | 2020-05 | 2020-09 | Intolerance (nausea and ALT above 3 times the upper limit of normal) |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab was used from 2023-07 to 2026-07. It was stopped for secondary loss of response with a low trough level and antibodies, which counts as inadequate response. (confidence 0.93)

- `PT-2548/medication-history-2026-11-10` (2026-11-10): "| Infliximab | 5 mg/kg IV every 8 weeks | 2023-07 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 60 U/mL (reference <10) |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The IGRA of 2026-09-21 is positive and within 6 months, so the positive-screen pathway applies. The chest radiograph of 2026-09-24 shows no active TB, and rifampin for latent TB was started on 2026-10-01. Both required conditions are documented. (confidence 0.90)

- `PT-2548/labs-2026-09-21` (2026-09-21): "QuantiFERON-TB Gold Plus | POSITIVE | A | Negative"
- `PT-2548/chest-xray-2026-09-24` (2026-09-24): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2548/gi-note-2026-11-10` (2026-11-10): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-09-21. No plan for prophylaxis or monitoring is needed. (confidence 0.96)

- `PT-2548/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-2548/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current medication history says there is no biologic or small-molecule advanced therapy at present. The earlier infliximab was stopped in 2026-07. The only concurrent IBD drug is budesonide, which is not a biologic. (confidence 0.90)

- `PT-2548/medication-history-2026-11-10` (2026-11-10): "- No biologic or small-molecule advanced therapy at present."
- `PT-2548/medication-history-2026-11-10` (2026-11-10): "| Infliximab | 5 mg/kg IV every 8 weeks | 2023-07 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 60 U/mL (reference <10) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 111.6 kg on 2026-11-10 is within 90 days of the request and falls in the above-85 kg band, which calls for 520 mg IV. The order is 520 mg IV once, then 90 mg SC every 8 weeks starting 8 weeks after the infusion, which matches the labeled regimen. (confidence 0.95)

- `PT-2548/gi-note-2026-11-10` (2026-11-10): "Weight 111.6 kg."
- `PT-2548/gi-note-2026-11-10` (2026-11-10): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 111.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 111.6 kg (2026-11-10) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: An endoscopy report from 2025-11-18 or later showing active mucosal inflammation (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy), or a provider decision on how to proceed (who: ordering_provider)
  > Dr. Chen, for PA-2548 (PT-2548, ustekinumab-ttwe), Calder policy criterion B.2 needs an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from the past 12 months that shows active mucosal inflammation. The only endoscopy on file is the colonoscopy dated 2025-04-18, which is about 19 months before the 2026-11-18 request. The CRP of 26.3 mg/L from 2026-09-21 does not count on its own under this policy. Please review and tell us whether a more recent endoscopy exists, here or at another facility, or how you would like to proceed.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
