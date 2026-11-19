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

The 11/05/2026 GI note assessment states moderately to severely active ileocolonic Crohn's disease. This is the prescriber's own statement in the clinical record. (confidence 0.95)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "A:
- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy in the chart is a colonoscopy from 12/2022, well outside the 12-month window before 2026-11-18. The CRP is a lab marker and does not satisfy the requirement on its own. No endoscopy report from the past 12 months was found. (confidence 0.80)

- `PT-3507/gi-note-2026-05-13` (2026-05-13): "- Last colonoscopy 12/2022 showed active disease."
- `PT-3507/labs-2026-10-03` (2026-10-03): "C REACTIVE PROTEIN ................ 9.1 mg/L  (<5.0)"

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No chart passage documents the prescriber's specialty or a gastroenterology consultation. The specialty appears only in the request form, not in the retrieved chart text. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (gastroenterologist) or a gastroenterology consultation note

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth is 08/01/1980, so the member is 46 on the request date of 2026-11-18. This is at least 18 under either date reading. (confidence 0.97)

- `PT-3507/demographics-2026-05-23` (2026-05-23): "Date of birth: 08/01/1980"
- Code checks: age 46 on 2026-11-18 from DOB 1980-08-01

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Adalimumab was used 07/2023 to 11/2023 and stopped for primary non-response. Methotrexate was used 06/2021 to 11/2021 and stopped for intolerance. Either one satisfies the criterion, and both give the drug, dates and reason. (confidence 0.95)

- `PT-3507/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"
- `PT-3507/outside-records-2021-12-18` (2021-12-18): "- Methotrexate 25 mg subcutaneously weekly, 06/2021 to 11/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON was resulted 2026-10-03, within 6 months of the 2026-11-18 request. It is a determinate negative result. (confidence 0.93)

- `PT-3507/labs-2026-10-03` (2026-10-03): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented as nonreactive. No reactive result means no prophylaxis plan is required. (confidence 0.95)

- `PT-3507/labs-2026-10-03` (2026-10-03): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3507/labs-2026-10-03` (2026-10-03): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The current medication history lists no biologic, JAK inhibitor or S1P modulator. The other current medications (budesonide, vitamin D3) are not in the excluded classes, so there is nothing to combine or stop. (confidence 0.92)

- `PT-3507/medication-history-2026-11-02` (2026-11-02): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 63.6 kg was recorded 2026-11-05, within 90 days of the request. That falls in the above-55 kg to 85 kg tier (390 mg IV). The maintenance dose of 90 mg SC every 8 weeks starting 8 weeks after the infusion matches the labeled regimen. (confidence 0.93)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Weight 63.6 kg."
- Code checks: weight 63.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report within past 12 months showing active inflammation (who: ordering_provider)
  > PA-3507 (PT-3507), criterion C2 (B.2, direct visualization): the only endoscopy in the chart is the colonoscopy from 12/2022, and the CRP of 9.1 mg/L on 2026-10-03 is a lab marker that does not count on its own. Please review. Is there an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report dated within the past 12 months that documents active mucosal inflammation?
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers (calprotectin, CRP, ESR) and cross-sectional imaging do not satisfy it.
- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consult note (who: practice_staff)
  > PA-3507 (PT-3507), criterion C3 (B.3, prescriber specialty): the request form lists Dr. S. Adeyemi, Gastroenterology, but no chart document states the specialty or a GI consultation. Could you locate and attach a chart note, such as a signed visit note or letterhead, that shows the prescriber is a gastroenterologist, or a GI consult note for this treatment?
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment.

## Run cost

3 model calls, 17,180 input and 5,227 output tokens, 33.3 s of model time, $0.100 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent NEEDS_PHYSICIAN. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | NOT_MET | NOT_MET | ok (alternate) |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
