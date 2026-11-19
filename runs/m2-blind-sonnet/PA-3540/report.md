# PA-3540: ustekinumab-ttwe for PT-3540

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 106.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note of 2026-10-29 states moderately to severely active ileocolonic Crohn's disease. Nothing in the chart contradicts it. (confidence 0.95)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy in the chart is from 2022-12, well outside the 12 months before 2026-11-18. The CRP of 15.6 mg/L is a lab marker and does not count on its own. (confidence 0.75)

- `PT-3540/gi-note-2026-06-02` (2026-06-02): "Last colonoscopy 2022-12 showed active disease."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The retrieved chart passages do not state the prescriber's specialty or any gastroenterology consultation. The specialty appears only in the request form, not in a chart passage. (confidence 0.60)

- Missing: Chart documentation that the prescriber (Dr. A. Rivera) is a gastroenterologist, or a documented gastroenterology consultation

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Born 1977-08-22, the member is 49 on the request date 2026-11-18, which is over 18. (confidence 0.98)

- `PT-3540/demographics-2026-03-09` (2026-03-09): "Date of birth: 1977-08-22"
- Code checks: age 49 on 2026-11-18 from DOB 1977-08-22

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Adalimumab was used 2023-07 to 2026-09 and stopped for intolerance. Azathioprine was also stopped for intolerance. Each record gives the drug, dates and reason, and one is enough. (confidence 0.96)

- `PT-3540/medication-history-2026-10-28` (2026-10-28): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2026-09. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."
- `PT-3540/outside-records-2021-04-18` (2021-04-18): "Azathioprine 2.5 mg/kg daily, 2021-01 to 2021-03. Reason stopped: intolerance (acute pancreatitis)."

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The QuantiFERON was only ordered on 2026-10-29, and no result is in the chart. An order is not a result. (confidence 0.95)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "QuantiFERON-TB Gold Plus ordered today."
- Missing: IGRA or TST result dated within 6 months before 2026-11-18

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg (nonreactive) and total anti-HBc (reactive) results are on file. The reactive core antibody is covered by a documented plan to monitor HBV DNA and liver tests every 3 months. (confidence 0.93)

- `PT-3540/labs-2026-10-09` (2026-10-09): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3540/labs-2026-10-09` (2026-10-09): "Hepatitis B core antibody, total      Reactive      Nonreactive"
- `PT-3540/gi-note-2026-10-29` (2026-10-29): "monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The member is on vedolizumab now, and the record shows it will be stopped when ustekinumab starts. No other biologic, JAK inhibitor or S1P modulator is listed. (confidence 0.94)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3540/medication-history-2026-10-28` (2026-10-28): "to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

The weight of 106.6 kg was recorded 2026-10-29, within 90 days of the request. It is above 85 kg, so 520 mg IV is the correct tier, followed by 90 mg SC every 8 weeks starting 8 weeks after the infusion. (confidence 0.95)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Weight 106.6 kg."
- Code checks: weight 106.6 kg (2026-10-29) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy within 12 months showing active mucosal inflammation (who: ordering_provider)
  > PA-3540 (ustekinumab-ttwe), criterion C2 (B.2): the only endoscopy on file is the colonoscopy from 2022-12, cited in the 2026-06-02 GI note. That is outside the 12-month window, and the CRP of 15.6 mg/L does not count on its own. Please review and tell us whether a more recent ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report exists, or how you wish to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers and cross-sectional imaging do not satisfy it.
- **C3**: Chart documentation that Dr. Rivera is a gastroenterologist, or a GI consultation note (who: practice_staff)
  > PA-3540, criterion C3 (B.3): the chart passages do not state Dr. A. Rivera's specialty, which appears only on the request form. Could you locate or file a signed note or provider credential record showing Dr. Rivera is a gastroenterologist, or a documented gastroenterology consultation about this treatment?
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment.
- **C6**: Resulted QuantiFERON-TB Gold Plus (or TST) with negative result (who: lab)
  > PA-3540, criterion C6 (B.6): the 2026-10-29 GI note says QuantiFERON-TB Gold Plus was ordered, but no result is in the chart. Please check whether the lab has resulted it and send us the report. If it was not drawn, the ordering provider would need to decide how to proceed.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. Indeterminate or borderline results are not negative. A positive screen qualifies only with a chest radiograph showing no active disease and documented start of latent infection treatment.

## Run cost

3 model calls, 17,950 input and 6,166 output tokens, 38.0 s of model time, $0.112 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
