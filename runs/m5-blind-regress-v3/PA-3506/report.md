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

The GI note of 2026-10-26 states the diagnosis is Crohn's disease and that it is moderately to severely active. The problem list confirms the Crohn's diagnosis (K50.80). (confidence 0.95)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3506/problem-list-2026-10-26` (2026-10-26): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is the 05/2023 colonoscopy. That is far outside the 12-month window, and no findings report is on file. The recent calprotectin and CRP are lab markers, and the policy says they do not meet this requirement on their own. (confidence 0.80)

- `PT-3506/outside-records-2024-10-18` (2024-10-18): "Dx: Crohn's discase,  diagnosed 05/2023 by colonoscopy."
- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Her calprotectin from 10/05/2026 came back at 511 ug/g (lab reference <50)."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ustekinumab order is in a GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. None of the quoted passages states the prescriber's specialty in so many words, so the reviewer may want to confirm the credential. (confidence 0.85)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The date of birth is 07/11/1981, which makes the member 45 on the 2026-11-18 request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-3506/demographics-2026-06-07` (2026-06-07): "Date of birth: 07/11/1981"
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Prednisone was used 06/2023 to 12/2023 and was inadequate because of steroid dependence. Azathioprine was used 01/2024 to 03/2024 and was stopped for intolerance (acute pancreatitis). Both are conventional agents, and each entry gives dates and a reason. (confidence 0.93)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 06/2023 | 12/2023 | Steroid dependent (flared each time the dose went below 15 mg) |"
- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Azathioprine | 2.5 mg/kg daily | 01/2024 | 03/2024 | Intolerance (acute pancreatitis) |"

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The medication history, based on patient report, lists adalimumab from 05/2024 to 05/2026, stopped for loss of response. The 10/2024 outside records say the patient declined adalimumab in 05/2024 and was biologic-naive. These statements cannot both be true, and the outside records requested to settle it are not in the chart. (confidence 0.80)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"
- `PT-3506/outside-records-2024-10-18` (2024-10-18): "- Biologic-naive. Adalimumab was recommended 05/2024 but the patient declined."

### C6 (policy B.6): **NOT MET**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The only TB screen in the chart is a negative QuantiFERON dated 2025-11-30. That is about 11.5 months before the 2026-11-18 request, outside the 6-month window. No newer IGRA or TST is on file. (confidence 0.88)

- `PT-3506/labs-2025-11-30` (2025-11-30): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

HBsAg and total hepatitis B core antibody were both resulted on 2026-09-22 and both are nonreactive. Because neither is reactive, no prophylaxis or monitoring plan is needed. (confidence 0.96)

- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The 2026-10-22 medication history states there is no current biologic, JAK inhibitor, or S1P receptor modulator. Any prior adalimumab is listed as stopped 05/2026, so nothing would be combined with ustekinumab. (confidence 0.88)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 90.4 kg was recorded on 2026-10-26, within 90 days of the request. That is above 85 kg, so the 520 mg IV band applies. The order is 520 mg IV once, then 90 mg SC every 8 weeks starting 8 weeks after the infusion, which matches the labeled regimen. (confidence 0.95)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Weight 90.4 kg."
- `PT-3506/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 90.4 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report from the past 12 months documenting active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, for PT-3506's ustekinumab-ttwe request (PA-3506), criterion B.2 requires endoscopic confirmation of active disease within the past 12 months. The only endoscopy in the chart is the 05/2023 diagnostic colonoscopy, cited in the 2024-10-18 outside records, and no findings report for it is on file. The 10/05/2026 calprotectin of 511 ug/g is a lab marker, and the policy says lab markers do not meet this requirement on their own. Please review and tell us whether a qualifying endoscopy report exists or how you would like to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers and cross-sectional imaging do not count on their own.
- **C6**: Negative IGRA or TST result from the past 6 months (who: ordering_provider)
  > Dr. Adeyemi, for PT-3506's ustekinumab-ttwe request (PA-3506), criterion B.6 requires a negative TB screen within the past 6 months. The only screen on file is a negative QuantiFERON TB Gold Plus dated 2025-11-30 (labs-2025-11-30), which falls outside that window. Please review and tell us whether a newer IGRA or TST result exists or how you would like to proceed.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. Indeterminate or borderline results do not count. If the screen is positive, the policy requires a chest radiograph showing no active disease plus documentation that latent TB treatment has started.

## Run cost

3 model calls, 12,739 input and 4,047 output tokens, 35.2 s of model time, $0.152 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | NOT_MET | NOT_MET | ok (alternate) |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
