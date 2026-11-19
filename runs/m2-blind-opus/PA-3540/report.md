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

The prescriber's GI note of 2026-10-29 states moderately to severely active ileocolonic Crohn's disease. The problem list confirms the Crohn's diagnosis (K50.80). (confidence 0.95)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3540/problem-list-2026-10-29` (2026-10-29): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2020."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is a colonoscopy from 2022-12, nearly four years before the 2026-11-18 request and well outside the 12-month window. The raised CRP is a lab marker, and the policy says lab markers do not meet this criterion on their own. A colonoscopy, ileocolonoscopy or sigmoidoscopy report from within the past 12 months would be needed. (confidence 0.70)

- `PT-3540/gi-note-2026-06-02` (2026-06-02): "Last colonoscopy 2022-12 showed active disease."
- `PT-3540/labs-2026-10-09` (2026-10-09): "C-reactive protein                    15.6 mg/L     <5.0"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ordering provider is Dr. A. Rivera, Gastroenterology, according to the request. The ustekinumab order appears in the GI follow-up note of 2026-10-29. (confidence 0.90)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 1977-08-22, the member is 49 on the request date of 2026-11-18. The outside records give the same date of birth. (confidence 0.98)

- `PT-3540/demographics-2026-03-09` (2026-03-09): "Date of birth: 1977-08-22"
- Code checks: age 49 on 2026-11-18 from DOB 1977-08-22

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate (2020-07 to 2020-12) and azathioprine (2021-01 to 2021-03) were both stopped for documented intolerance. Each one is a conventional agent listed in the policy, with dates and a reason for stopping. (confidence 0.93)

- `PT-3540/outside-records-2021-04-18` (2021-04-18): "- Methotrexate 25 mg subcutaneously weekly, 2020-07 to 2020-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3540/outside-records-2021-04-18` (2021-04-18): "- Azathioprine 2.5 mg/kg daily, 2021-01 to 2021-03. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab was used from 2023-07 to 2026-09 and stopped for documented intolerance (drug-induced lupus). This shows a biologic was tried, with dates and a reason for stopping. (confidence 0.93)

- `PT-3540/medication-history-2026-10-28` (2026-10-28): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2026-09. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON-TB Gold Plus test was only ordered on 2026-10-29. No result appears in the chart, and an order is not a result. (confidence 0.92)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "- QuantiFERON-TB Gold Plus ordered today."
- Missing: Resulted QuantiFERON-TB Gold Plus (IGRA) or TST result dated within 6 months before 2026-11-18

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg (nonreactive) and total anti-HBc (reactive) have results from 2026-10-09. Because the core antibody is reactive, a plan is required, and the prescriber documents HBV DNA and liver test monitoring every 3 months on therapy. (confidence 0.92)

- `PT-3540/labs-2026-10-09` (2026-10-09): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3540/labs-2026-10-09` (2026-10-09): "Hepatitis B core antibody, total      Reactive      Nonreactive"
- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The member is switching from vedolizumab, and both the prescriber's note and the medication history say vedolizumab is being stopped when ustekinumab starts. Adalimumab was already stopped in 2026-09. (confidence 0.88)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3540/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-15); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 106.6 kg was recorded on 2026-10-29, within 90 days of the request, and it is above 85 kg, so the 520 mg IV dose band applies. The requested maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the labeled regimen. (confidence 0.93)

- `PT-3540/gi-note-2026-10-29` (2026-10-29): "Weight 106.6 kg."
- `PT-3540/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.6 kg (2026-10-29) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report from the past 12 months documenting active mucosal inflammation (who: ordering_provider)
  > Dr. Rivera, for PT-3540's ustekinumab PA (PA-3540), criterion C2 (policy B.2) requires an endoscopy within the past 12 months that documents active mucosal inflammation. The only endoscopy in the chart is the 2022-12 colonoscopy, which is mentioned in the 2026-06-02 GI note. The CRP of 15.6 mg/L from 2026-10-09 is a lab marker, and the policy says lab markers do not satisfy this criterion on their own. Please review and tell us whether a more recent endoscopy report exists, or how you would like to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers and cross-sectional imaging do not qualify.
- **C6**: Resulted QuantiFERON-TB Gold Plus (ordered 2026-10-29) (who: lab)
  > For PT-3540 (PA-3540), criterion C6 (TB screening) needs the result of the QuantiFERON-TB Gold Plus ordered on 2026-10-29. The chart shows the order (GI note 2026-10-29) but no result. Please release the result or send us the report so we can file it with the request.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result does not count. If the result is positive, the policy requires a chest radiograph showing no active disease and documentation that treatment for latent TB has begun.

## Run cost

3 model calls, 19,990 input and 7,279 output tokens, 62.9 s of model time, $0.263 at list price (0 served from cache).

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
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
