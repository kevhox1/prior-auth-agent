# PA-3506: ustekinumab-ttwe for PT-3506

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 90.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The prescriber's GI note of 2026-10-26 states moderately to severely active Crohn's disease. This is the required prescriber statement. (confidence 0.95)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

Calprotectin is a lab marker and does not meet the policy alone. The only colonoscopy mentioned was in 2023, outside the 12-month window, and no report is present. No endoscopy within the past 12 months is documented. (confidence 0.88)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Her calprotectin from 10/05/2026 came back at 511 ug/g (lab reference <50)."
- `PT-3506/outside-records-2024-10-18` (2024-10-18): "Dx: Crohn's discase,  diagnosed 05/2023 by colonoscopy."
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated 2025-11-18 or later documenting active mucosal inflammation

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No chart passage was retrieved documenting the prescriber's specialty or a GI consultation. The request lists Gastroenterology, but that is not chart evidence quoted here. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (gastroenterology) or of a consultation with a gastroenterologist

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Born 07/11/1981, the member is 45 on the request date of 2026-11-18, which is over 18. (confidence 0.97)

- `PT-3506/demographics-2026-06-07` (2026-06-07): "Date of birth: 07/11/1981"
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Azathioprine was stopped in 03/2024 for intolerance (pancreatitis), and prednisone 06/2023–12/2023 was insufficient due to steroid dependence. Either conventional agent satisfies the policy. The conflicting adalimumab history does not affect this, since only one qualifying therapy is needed. (confidence 0.90)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Azathioprine | 2.5 mg/kg daily | 01/2024 | 03/2024 | Intolerance (acute pancreatitis) |"
- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 06/2023 | 12/2023 | Steroid dependent (flared each time the dose went below 15 mg) |"

### C6 (policy B.6): **NOT MET**
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The only TB screen is a negative QuantiFERON dated 2025-11-30, which is nearly 12 months before the 2026-11-18 request and outside the 6-month window. No more recent result is present. (confidence 0.90)

- `PT-3506/labs-2025-11-30` (2025-11-30): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented as nonreactive on 2026-09-22. No reactive result, so no prophylaxis plan is needed. (confidence 0.96)

- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The medication history states the member is on no current biologic, JAK inhibitor, or S1P modulator, so there is no combination. (confidence 0.90)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

Weight 90.4 kg (above 85 kg) matches the 520 mg IV induction, followed by 90 mg SC every 8 weeks starting 8 weeks later. The weight was recorded 2026-10-26, within 90 days of the request. (confidence 0.95)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Weight 90.4 kg."
- Code checks: weight 90.4 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report within 12 months showing active mucosal inflammation (who: practice_staff)
  > PA-3506, criterion C2 (B.2): the chart has only the calprotectin of 511 ug/g from 10/05/2026 and a 2023 colonoscopy mentioned in outside records dated 2024-10-18, with no report. Please check whether an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report dated 2025-11-18 or later, documenting active mucosal inflammation, exists and can be filed. If none exists, Dr. Adeyemi should review how to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation. Lab markers such as calprotectin and cross-sectional imaging do not satisfy it.
- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consultation (who: practice_staff)
  > PA-3506, criterion C3 (B.3): the request lists Dr. S. Adeyemi as Gastroenterology, but no chart document confirms the specialty or a GI consultation. Please attach a chart document, such as a signed GI clinic note or provider credentials on file, that shows the prescriber's specialty.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or that the prescriber consulted a gastroenterologist about this treatment.
- **C6**: Negative IGRA or TST dated within the past 6 months (who: ordering_provider)
  > PA-3506, criterion C6 (B.6): the only TB screen on file is a negative QuantiFERON-TB Gold Plus dated 2025-11-30. That is outside the 6-month window for a 2026-11-18 request. Dr. Adeyemi, please review. Is there a more recent IGRA or TST result, or does the chart need an updated screen?
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result is not negative.

## Run cost

3 model calls, 17,812 input and 5,520 output tokens, 34.9 s of model time, $0.105 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | CONFLICTING | MET | - | FALSE MET |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
