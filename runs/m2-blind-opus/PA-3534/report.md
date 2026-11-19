# PA-3534: ustekinumab-aekn for PT-3534

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: URGENT review. Decision within 24 hours of receiving all required information (policy section E). Prescriber attestation of urgency is required. Work this case first.
- Ordered dose: 390 mg IV once (weight 66.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-11-09 states a Crohn's disease diagnosis and calls it moderately to severely active. The problem list also records Crohn's disease (K50.80). (confidence 0.95)

- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy on file is a colonoscopy from 2025-04-18. That is about 19 months before the 2026-11-18 request, outside the 12-month window. The recent CRP is a lab marker, and the policy says lab markers do not count on their own. No endoscopy within the past 12 months was found. (confidence 0.70)

- `PT-3534/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3534/labs-2026-10-21` (2026-10-21): "C-reactive protein                    22.0 mg/L     <5.0"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ustekinumab order appears in a GI follow-up note. The request names the ordering provider as Dr. S. Adeyemi, Gastroenterology. The quoted passage itself does not state the author's specialty, so the reviewer may want to confirm the note's signature. (confidence 0.85)

- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 03/19/1992, the member is 34 years old on the request date of 2026-11-18. That meets the 18-or-older requirement. (confidence 0.97)

- `PT-3534/demographics-2026-04-29` (2026-04-29): "Date of birth: 03/19/1992"
- Code checks: age 34 on 2026-11-18 from DOB 1992-03-19

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Budesonide is a listed conventional agent. The medication history gives its dates of use (05/2019 to 08/2019) and says it was stopped for inadequate response. (confidence 0.93)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Budesonide 9 mg daily, 05/2019 to 08/2019. Reason stopped: inadequate response after 10 weeks."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab, a biologic, was used from 07/2023 to 07/2026. It was stopped for secondary loss of response, with a low trough level and antibodies documented. That counts as inadequate response. (confidence 0.93)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON-TB Gold Plus (an interferon-gamma release assay) was negative on 2026-10-21. That is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-3534/labs-2026-10-21` (2026-10-21): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both the hepatitis B surface antigen and the total hepatitis B core antibody have results on file, and both are nonreactive. Because neither is reactive, no antiviral prophylaxis or monitoring plan is needed. (confidence 0.96)

- `PT-3534/labs-2026-10-21` (2026-10-21): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3534/labs-2026-10-21` (2026-10-21): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The medication history says the member is on no current biologic, JAK inhibitor, or S1P receptor modulator. The earlier biologic, infliximab, was stopped in 07/2026. (confidence 0.92)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 66.2 kg was recorded on 2026-11-09, within 90 days of the request. That weight falls in the over-55 to 85 kg band, which calls for 390 mg IV. The order is 390 mg IV once, then 90 mg SC every 8 weeks starting 8 weeks after the infusion, which matches the labeled regimen. (confidence 0.95)

- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Weight 66.2 kg."
- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.2 kg (2026-11-09) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report from the past 12 months showing active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, PA-3534 (ustekinumab-aekn) does not meet criterion C2 (policy B.2). The only endoscopy on file is the colonoscopy dated 2025-04-18, about 19 months before the 2026-11-18 request, so it falls outside the 12-month window. The CRP of 22.0 mg/L from 2026-10-21 is a lab marker, and the policy does not accept lab markers on their own. Please review, and let us know if there is a more recent endoscopy report we have not filed, or how you want to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers alone (fecal calprotectin, CRP, ESR) and cross-sectional imaging do not meet it.

## Run cost

3 model calls, 18,751 input and 5,798 output tokens, 51.1 s of model time, $0.224 at list price (0 served from cache).

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
