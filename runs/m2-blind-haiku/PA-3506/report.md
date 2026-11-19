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

The 2026-10-26 GI note states the prescriber's impression of moderately to severely active ileocolonic Crohn's disease. The note also records an HBI of 14, which supports that severity. (confidence 0.90)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Harvey-Bradshaw Index today: 14."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy in the chart is the 05/2023 colonoscopy used for diagnosis, which is outside the 12-month window. The 10/05/2026 calprotectin does not satisfy this criterion on its own, so a current endoscopy report is needed. (confidence 0.85)

- `PT-3506/outside-records-2024-10-18` (2024-10-18): "Crohn's discase,  diagnosed 05/2023 by colonoscopy."
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 (within 12 months of the request) documenting active mucosal inflammation
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

Dr. S. Adeyemi is the ordering provider on the labs and the request lists gastroenterology, but no passage in the chart states the specialty explicitly. A specialty statement or a GI consult note is needed to confirm this. (confidence 0.60)

- `PT-3506/labs-2026-09-22` (2026-09-22): "ORDERING: Dr. S. Adeyemi"
- Missing: Chart documentation of Dr. S. Adeyemi's specialty as gastroenterology (for example, provider credentials or specialty field), or a documented gastroenterology consultation about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 07/11/1981 makes the member 45 years old on the 2026-11-18 request date, which is above the 18-year minimum. (confidence 0.95)

- `PT-3506/demographics-2026-06-07` (2026-06-07): "Date of birth: 07/11/1981"
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history records oral prednisone from 06/2023 to 12/2023, stopped because of steroid dependence, which is an inadequate response. Azathioprine from 01/2024 to 03/2024 was also stopped for intolerance, so a listed conventional agent was tried and stopped for a qualifying reason. (confidence 0.90)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 06/2023 | 12/2023 | Steroid dependent (flared each time the dose went below 15 mg) |"
- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Azathioprine | 2.5 mg/kg daily | 01/2024 | 03/2024 | Intolerance (acute pancreatitis) |"

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The 10/22/2026 medication history lists adalimumab from 05/2024 to 05/2026 as stopped for loss of response, based on patient report. The 10/18/2024 outside record says the patient was biologic-naive and declined adalimumab, so the two records disagree on whether the drug was used and the chart does not resolve it. (confidence 0.70)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"
- `PT-3506/outside-records-2024-10-18` (2024-10-18): "- Biologic-naive. Adalimumab was recommended 05/2024 but the patient declined."
- Missing: Outside adalimumab treatment records confirming whether adalimumab was taken from 05/2024 to 05/2026 and the reason it was stopped

### C6 (policy B.6): **NOT MET**
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The only negative QuantiFERON was collected on 11/30/2025, which is more than 6 months before the 2026-11-18 request. No newer IGRA or tuberculin test appears in the chart, so the screen is outside the required window. (confidence 0.85)

- `PT-3506/labs-2025-11-30` (2025-11-30): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- `PT-3506/labs-2025-11-30` (2025-11-30): "COLLECTED: 11/30/2025"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

The 09/22/2026 labs report hepatitis B surface antigen as nonreactive and total hepatitis B core antibody as nonreactive. Because neither result is reactive, no prophylaxis plan is required. (confidence 0.95)

- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 10/22/2026 medication list states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The prior adalimumab row shows an end date of 05/2026, so the earlier agent is recorded as stopped. The stop is shown only as a table end date, not as a separate stop order. (confidence 0.75)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A 90.4 kg weight falls in the above-85-kg band, which takes a 520 mg IV induction, and the requested 520 mg IV dose matches. The requested 90 mg SC every 8 weeks starting 8 weeks after induction is the labeled maintenance regimen. The weight was recorded on 10/26/2026, within 90 days of the request. (confidence 0.90)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Weight 90.4 kg."
- Code checks: weight 90.4 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, criterion B.2 (direct visualization of disease activity) is open for PT-3506. The only endoscopy in the chart is the colonoscopy from 05/2023, which is outside the 12-month window, and the 10/05/2026 fecal calprotectin does not satisfy this criterion on its own. Please review whether an endoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation exists or is planned.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 (within 12 months of the 2026-11-18 request) that documents active mucosal inflammation. Laboratory markers and cross-sectional imaging do not satisfy this item.
- **C3**: Chart documentation of Dr. S. Adeyemi's specialty as gastroenterology, or a documented gastroenterology consultation about ustekinumab (who: practice_staff)
  > For PT-3506, criterion B.3 needs proof that the prescriber is a gastroenterologist. Dr. S. Adeyemi appears as ordering provider on the 09/22/2026 labs, but no chart passage states the specialty. Please check the provider credentials or specialty field in the practice system, or file a GI consult note about ustekinumab if one exists.
  - Would satisfy the policy: Policy B.3 accepts chart documentation (provider credentials or specialty field) showing Dr. S. Adeyemi is a gastroenterologist, or a documented gastroenterology consultation about this treatment. The criterion states no date window.
- **C5b**: Outside adalimumab treatment records confirming use from 05/2024 to 05/2026 and the documented reason it was stopped (who: ordering_provider)
  > Dr. Adeyemi, criterion B.5(b) is conflicting for PT-3506. The 10/22/2026 medication history lists adalimumab 05/2024 to 05/2026 as stopped for loss of response (patient report, outside records requested), but the 10/18/2024 outside record states the patient was biologic-naive and declined adalimumab. Please review the outside adalimumab records and confirm whether the drug was taken and why it was stopped.
  - Would satisfy the policy: Policy B.5(b) accepts documentation that a biologic or targeted synthetic agent for CD or UC was stopped or found insufficient for inadequate response or intolerance, or a documented contraindication to TNF blockers. The outside records must confirm adalimumab use and the stop reason. The criterion states no date window.
- **C6**: Negative interferon-gamma release assay (QuantiFERON) or tuberculin skin test dated on or after 2026-05-18 (who: ordering_provider)
  > Dr. Adeyemi, criterion B.6 (TB screening) is not met for PT-3506. The only negative QuantiFERON in the chart was collected 11/30/2025, which is more than 6 months before the 11/18/2026 request. Please review the TB screening status and the documentation needed for this criterion.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or tuberculin skin test dated on or after 2026-05-18 (within 6 months of the 2026-11-18 request). An indeterminate or borderline result does not count as negative.

## Run cost

3 model calls, 20,419 input and 13,898 output tokens, 56.3 s of model time, $0.010 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
