# PA-2563: ustekinumab-aekn for PT-2563

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 85.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The prescriber's GI note of 2026-10-28 states the diagnosis is Crohn's disease. It also states the disease is moderately to severely active. (confidence 0.95)

- `PT-2563/gi-note-2026-10-28` (2026-10-28): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only colonoscopy documented after diagnosis is from 2023-02, well outside the 12-month window before 2026-11-18. The raised CRP is a lab marker, and the policy says lab markers do not count on their own. No endoscopy report from within the past 12 months is in the chart. (confidence 0.60)

- `PT-2563/gi-note-2026-04-08` (2026-04-08): "Last colonoscopy 2023-02 showed active disease."
- `PT-2563/labs-2026-09-26` (2026-09-26): "C REACTIVE PROTEIN ................ 14.6 mg/L  (<5.0)"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists Dr. A. Rivera, Gastroenterology, as the ordering provider. The ustekinumab order appears in a GI follow-up note. (confidence 0.93)

- `PT-2563/gi-note-2026-10-28` (2026-10-28): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 1963-04-22, the member is 63 on the request date of 2026-11-18. The outside records give the same date of birth. (confidence 0.98)

- `PT-2563/demographics-2026-06-06` (2026-06-06): "Date of birth: 1963-04-22"
- Code checks: age 63 on 2026-11-18 from DOB 1963-04-22

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Mercaptopurine was used from 2020-06 to 2021-01 and stopped for inadequate response. Methotrexate was used from 2021-02 to 2021-08 and stopped for intolerance. Both are listed conventional agents with dates and a reason for stopping. The blank treatment-history section in the outside records is an omission, not a conflict. (confidence 0.93)

- `PT-2563/gi-note-2026-04-08` (2026-04-08): "History: Mercaptopurine 1.5 mg/kg daily, 2020-06 to 2021-01. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."
- `PT-2563/gi-note-2026-04-08` (2026-04-08): "History: Methotrexate 25 mg subcutaneously weekly, 2021-02 to 2021-08. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab, a biologic, was used from 2023-07 to 2026-08. It was stopped for intolerance (drug-induced lupus). (confidence 0.92)

- `PT-2563/gi-note-2026-10-28` (2026-10-28): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-08. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON (IGRA) result was negative on 2026-09-26, about 2 months before the request. That is inside the 6-month window. (confidence 0.95)

- `PT-2563/labs-2026-09-26` (2026-09-26): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

HBsAg and total hepatitis B core antibody both have results on file, and both are nonreactive. Because neither is reactive, no prophylaxis or monitoring plan is required. (confidence 0.96)

- `PT-2563/labs-2026-09-26` (2026-09-26): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2563/labs-2026-09-26` (2026-09-26): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

Vedolizumab is the only current biologic, and the plan documents that it will be stopped when ustekinumab starts. The only other CD medication listed is budesonide, which is not a biologic, JAK inhibitor or S1P modulator. (confidence 0.88)

- `PT-2563/gi-note-2026-10-28` (2026-10-28): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-2563/gi-note-2026-10-28` (2026-10-28): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-12); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 85.0 kg was recorded 21 days before the request. It falls in the band above 55 kg up to and including 85 kg, which matches the 390 mg IV dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the infusion, as the label requires. (confidence 0.92)

- `PT-2563/gi-note-2026-10-28` (2026-10-28): "Weight 85.0 kg."
- `PT-2563/gi-note-2026-10-28` (2026-10-28): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 85.0 kg (2026-10-28) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy) dated 2025-11-18 or later showing active mucosal inflammation, or a provider decision on how to proceed (who: ordering_provider)
  > Dr. Rivera, PA-2563 (ustekinumab-aekn, PT-2563) does not meet Calder criterion C2 (policy B.2). The policy requires an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from the past 12 months (on or after 2025-11-18) that shows active mucosal inflammation. The only endoscopy in the chart is the 2023-02 colonoscopy mentioned in your 2026-04-08 GI note. The CRP of 14.6 mg/L on 2026-09-26 is a lab marker and does not count on its own under the policy. Can you check whether a more recent endoscopy report exists, possibly from an outside facility, and tell us how you want to proceed?

## Run cost

3 model calls, 19,167 input and 6,714 output tokens, 54.5 s of model time, $0.248 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent NEEDS_PHYSICIAN. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | NOT_MET | NOT_MET | ok (alternate) |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
