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

The 2026-10-29 GI note states the prescriber's assessment of moderately to severely active ileocolonic Crohn's disease. The same note records Harvey-Bradshaw Index 12 and symptoms not controlled on current therapy, which support that grading. Nothing in the chart contradicts it. (confidence 0.90)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The most recent endoscopy recorded in the chart is a colonoscopy from 2022-12, and the 2026-06-02 GI note confirms it as the last colonoscopy. That is outside the 12-month lookback before the 2026-11-18 request. CRP and the other laboratory values cannot satisfy this item on their own. (confidence 0.75)

- `PT-3540/gi-note-2026-06-02` (2026-06-02): "Last colonoscopy 2022-12 showed active disease."
- `PT-3540/outside-records-2021-04-18` (2021-04-18): "Dx: Crohn's disease, diagnosed 2020-06 by colonoscopy."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ustekinumab plan is written in a GI follow-up note, and the request lists the ordering provider as Dr. A. Rivera, Gastroenterology. The chart passage does not state the specialty itself, so the confidence is somewhat lower than for a clearly labeled specialty entry. (confidence 0.80)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 1977-08-22 gives an age of 49 on the 2026-11-18 request date, which is above the 18-year minimum. (confidence 0.97)

- `PT-3540/demographics-2026-03-09` (2026-03-09): "Date of birth: 1977-08-22"
- Code checks: age 49 on 2026-11-18 from DOB 1977-08-22

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate was used from 2020-07 to 2020-12 and stopped for intolerance, and azathioprine was used from 2021-01 to 2021-03 and stopped for intolerance. Both are listed conventional agents with dates and reasons documented in the outside records. The current prednisone entry has no start date or stop reason and is not relied on. (confidence 0.90)

- `PT-3540/outside-records-2021-04-18` (2021-04-18): "Methotrexate 25 mg subcutaneously weekly, 2020-07 to 2020-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3540/outside-records-2021-04-18` (2021-04-18): "Azathioprine 2.5 mg/kg daily, 2021-01 to 2021-03. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

Adalimumab, a TNF blocker, was used from 2023-07 to 2026-09 and stopped for intolerance (drug-induced lupus with arthralgias). This documents a prior biologic stopped for intolerance with dates and reason. (confidence 0.90)

- `PT-3540/medication-history-2026-10-28` (2026-10-28): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2026-09. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The only tuberculosis item in the chart is a QuantiFERON order placed on 2026-10-29, and no result is on file. A pending order does not count as a negative screen. (confidence 0.90)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "QuantiFERON-TB Gold Plus ordered today."
- Missing: QuantiFERON-TB Gold Plus (or tuberculin skin test) result dated within the past 6 months, reported as negative

### C7 (policy B.7): **CONFLICTING**
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

The 2026-10-09 lab report gives total hepatitis B core antibody as reactive in one column and nonreactive in the other, with no column headers, and the surface antigen row is nonreactive in both columns. The 2026-10-29 GI note records anti-HBc positive and a monitoring plan, but the lab report itself does not say which column is current. This needs to be resolved from the source report before the criterion can be assessed. (confidence 0.60)

- `PT-3540/labs-2026-10-09` (2026-10-09): "Hepatitis B core antibody, total      Reactive      Nonreactive"
- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

Vedolizumab is still on the current medication list, but the GI note documents that it is being stopped and that ustekinumab replaces the next scheduled vedolizumab infusion. This meets the switching clause, and nothing in the chart shows an ongoing overlap. The requested start of 2026-12-01 differs from the approximately 2026-12-10 vedolizumab date, so the timing should be checked by the reviewer. (confidence 0.70)

- `PT-3540/medication-history-2026-10-28` (2026-10-28): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-15); to be discontinued when ustekinumab starts."
- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 106.6 kg was recorded on 2026-10-29, which is 20 days before the request and inside the 90-day window. A weight above 85 kg maps to the 520 mg induction band, and the requested regimen is 520 mg IV followed by 90 mg SC every 8 weeks starting 8 weeks after induction. (confidence 0.92)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Weight 106.6 kg."
- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.6 kg (2026-10-29) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy) within the past 12 months documenting active mucosal inflammation (who: ordering_provider)
  > Criterion C2 (B.2, endoscopic confirmation of disease activity) is not met for PA-3540. The only colonoscopy in the chart is from 2022-12, per the 2026-06-02 GI note, which is outside the 12-month lookback before the 2026-11-18 request. Please review; the policy accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 that documents active mucosal inflammation.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 that documents active mucosal inflammation. Laboratory markers and cross-sectional imaging do not satisfy this item.
- **C6**: QuantiFERON-TB Gold Plus (or tuberculin skin test) result reported as negative (who: lab)
  > Criterion C6 (B.6, tuberculosis screening) for PA-3540 is missing a result. The 2026-10-29 GI note documents 'QuantiFERON-TB Gold Plus ordered today,' but no result is on file. Please release the result to the chart so it can be reviewed against the policy.
  - Would satisfy the policy: Policy B.6 accepts a negative interferon-gamma release assay or tuberculin skin test dated on or after 2026-05-18. An indeterminate or borderline result is not negative. Pending orders do not count.
- **C7**: Clarified hepatitis B core antibody (total) result from the 2026-10-09 lab report, showing which column is current (who: ordering_provider)
  > Criterion C7 (B.7, hepatitis B status) for PA-3540 is conflicting. The 2026-10-09 lab report lists total hepatitis B core antibody as both 'Reactive' and 'Nonreactive' with no column headers, while the 2026-10-29 GI note records anti-HBc positive with a monitoring plan. Please review the source report and confirm which result is current so the criterion can be assessed.
  - Would satisfy the policy: Policy B.7 accepts HBsAg and total hepatitis B core antibody results of any age. A reactive anti-HBc result is accepted with a documented antiviral prophylaxis or monitoring plan, which the 2026-10-29 GI note records. The policy sets no date window for this item, but the conflicting 2026-10-09 report must be resolved from the source.

## Run cost

3 model calls, 20,658 input and 16,941 output tokens, 68.8 s of model time, $0.012 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | B.7 | MET | CONFLICTING | CONFLICTING | wrong |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
