# PA-3507: ustekinumab-ttwe for PT-3507

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 63.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The prescriber's GI note of 2026-11-05 names the diagnosis as Crohn's disease. The same note states the disease is moderately to severely active. (confidence 0.95)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is a colonoscopy from 12/2022 (plus the 2021 diagnostic one), which is well outside the 12-month window before 2026-11-18. The raised CRP is a lab marker, and the policy says lab markers do not meet this requirement on their own. If a colonoscopy or sigmoidoscopy was done within the past 12 months, its report would be needed. (confidence 0.70)

- `PT-3507/gi-note-2026-05-13` (2026-05-13): "- Last colonoscopy 12/2022 showed active disease."
- `PT-3507/labs-2026-10-03` (2026-10-03): "C REACTIVE PROTEIN ................ 9.1 mg/L  (<5.0)"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab order appears in a GI follow-up note. The quoted passage itself does not name the specialty, so the reviewer should confirm the note author. (confidence 0.85)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 08/01/1980, the member is 46 on the 2026-11-18 request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-3507/demographics-2026-05-23` (2026-05-23): "Date of birth: 08/01/1980"
- Code checks: age 46 on 2026-11-18 from DOB 1980-08-01

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate is a conventional agent. It was used from 06/2021 to 11/2021 and was stopped for intolerance (nausea and raised ALT). (confidence 0.93)

- `PT-3507/outside-records-2021-12-18` (2021-12-18): "Methotrexate 25 mg subcutaneously weekly, 06/2021 to 11/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab, a biologic, was used from 07/2023 to 11/2023. It was stopped for primary non-response, which is an inadequate response. (confidence 0.93)

- `PT-3507/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON (IGRA) result was negative on 2026-10-03, which is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-3507/labs-2026-10-03` (2026-10-03): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both hepatitis B surface antigen and total core antibody were resulted on 2026-10-03, and both are nonreactive. Because neither is reactive, no prophylaxis plan is required. (confidence 0.96)

- `PT-3507/labs-2026-10-03` (2026-10-03): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3507/labs-2026-10-03` (2026-10-03): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current medication history states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The only prior biologic, adalimumab, was stopped in 11/2023. (confidence 0.92)

- `PT-3507/medication-history-2026-11-02` (2026-11-02): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3507/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 63.6 kg was recorded on 2026-11-05, within 90 days of the request. That weight falls in the >55 to 85 kg band, which calls for 390 mg IV. The ordered maintenance is 90 mg SC every 8 weeks starting 8 weeks after the infusion, which matches the labeled regimen. (confidence 0.95)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Weight 63.6 kg."
- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 63.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report from the past 12 months documenting active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, for PA-3507 (PT-3507, ustekinumab-ttwe), criterion C2 (policy B.2) is NOT_MET. The policy requires direct visualization of disease activity within 12 months. The most recent endoscopy in the chart is the 12/2022 colonoscopy noted in the 2026-05-13 GI note, and the 2026-10-03 CRP of 9.1 mg/L is a lab marker, which the policy does not accept on its own. Please review and tell us whether an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy was done on or after 2025-11-18. If so, please send us the report or tell us where it was done so we can get it.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers (CRP, fecal calprotectin, ESR) and cross-sectional imaging do not meet it on their own.

## Run cost

3 model calls, 18,709 input and 5,907 output tokens, 49.9 s of model time, $0.226 at list price (0 served from cache).

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
