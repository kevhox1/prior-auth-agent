# PA-3545: ustekinumab-aekn for PT-3545

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note of 2026-11-06 states moderately to severely active ileocolonic Crohn's disease. The problem list confirms the Crohn's diagnosis with code K50.80, which matches the request. (confidence 0.95)

- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3545/problem-list-2026-11-06` (2026-11-06): "Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy on file is the colonoscopy of 2025-04-18. It shows active inflammation but falls before the 12-month cutoff of 2025-11-18. The raised CRP from 2026-10-03 is a lab marker, which the policy says does not count on its own. (confidence 0.80)

- `PT-3545/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3545/labs-2026-10-03` (2026-10-03): "C-reactive protein                    31.2 mg/L     <5.0"
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request names the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab order appears in a GI follow-up note dated 2026-11-06. (confidence 0.85)

- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The date of birth is 02/21/1966, and the outside records give the same date. That makes the member 60 years old on the 2026-11-18 request date. (confidence 0.98)

- `PT-3545/demographics-2026-04-15` (2026-04-15): "Date of birth: 02/21/1966"
- Code checks: age 60 on 2026-11-18 from DOB 1966-02-21

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Mercaptopurine is a listed conventional agent. It was used from 04/2023 to 10/2023 and was stopped for inadequate response. (confidence 0.93)

- `PT-3545/outside-records-2023-11-18` (2023-11-18): "Mercaptopurine 1.5 mg/kg daily, 04/2023 to 10/2023. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab is a biologic. It was used from 12/2023 to 05/2026 and was stopped for intolerance (drug-induced lupus). (confidence 0.94)

- `PT-3545/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

A QuantiFERON (IGRA) test on 2026-10-03 was negative, which is within 6 months of the 2026-11-18 request. The GI note's mention of a 2023 negative test is an older, separate result and does not contradict this one. (confidence 0.92)

- `PT-3545/labs-2026-10-03` (2026-10-03): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

HBsAg and total hepatitis B core antibody were both resulted as nonreactive on 2026-10-03. Because neither is reactive, no prophylaxis or monitoring plan is needed. (confidence 0.96)

- `PT-3545/labs-2026-10-03` (2026-10-03): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3545/labs-2026-10-03` (2026-10-03): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The 2026-11-04 medication history lists no current biologic, JAK inhibitor, or S1P receptor modulator. The earlier biologic, adalimumab, was stopped in 05/2026. (confidence 0.92)

- `PT-3545/medication-history-2026-11-04` (2026-11-04): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3545/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 55.0 kg was recorded on 2026-11-06, within 90 days of the request. That weight falls in the 260 mg band (up to and including 55 kg). The order matches the labeled regimen: 260 mg IV once, then 90 mg SC every 8 weeks starting 8 weeks later. (confidence 0.93)

- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Weight 55.0 kg."
- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-06) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy) dated on or after 2025-11-18 showing active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, for PA-3545 (PT-3545, ustekinumab-aekn), criterion C2 (policy B.2) is not met. The only endoscopy on file is the colonoscopy dated 2025-04-18. It shows terminal ileal ulcers, but it is older than the policy's 12-month window. The CRP of 31.2 mg/L on 2026-10-03 is a lab marker and does not count on its own. Can you check whether a more recent endoscopy report exists, including one done at an outside facility, and tell us how you want to proceed?
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers alone and cross-sectional imaging do not meet this requirement.

## Run cost

3 model calls, 19,547 input and 6,816 output tokens, 59.6 s of model time, $0.251 at list price (0 served from cache).

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
