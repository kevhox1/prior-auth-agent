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

In the 10/26/2026 GI note, the prescriber writes that the patient has moderately to severely active ileocolonic Crohn's disease. The Harvey-Bradshaw Index of 14 in the same note supports this. (confidence 0.95)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is a colonoscopy from 05/2023. That is far outside the 12-month window, and no findings report is on file. The recent calprotectin and CRP are lab markers, and the policy says these do not count on their own. (confidence 0.70)

- `PT-3506/outside-records-2024-10-18` (2024-10-18): "Dx: Crohn's discase,  diagnosed 05/2023 by colonoscopy."
- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Her calprotectin from 10/05/2026 came back at 511 ug/g (lab reference <50)."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab order appears in a GI follow-up note. (confidence 0.85)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 07/11/1981, the member is 45 on the 2026-11-18 request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-3506/demographics-2026-06-07` (2026-06-07): "Date of birth: 07/11/1981"
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history shows prednisone (06/2023–12/2023) stopped for steroid dependence, which is an inadequate response. It also shows azathioprine (01/2024–03/2024) stopped because of acute pancreatitis, which is intolerance. Each has a drug, dates and a reason. (confidence 0.92)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 06/2023 | 12/2023 | Steroid dependent (flared each time the dose went below 15 mg) |"
- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Azathioprine | 2.5 mg/kg daily | 01/2024 | 03/2024 | Intolerance (acute pancreatitis) |"

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The medication history, based only on patient report, lists adalimumab from 05/2024 to 05/2026 with loss of response. The outside records dated 10/2024 say the patient declined adalimumab and was biologic-naive. Nothing in the chart resolves which is right; the outside records that were requested would settle it. (confidence 0.80)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"
- `PT-3506/outside-records-2024-10-18` (2024-10-18): "- Biologic-naive. Adalimumab was recommended 05/2024 but the patient declined."

### C6 (policy B.6): **NOT MET**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The only TB screen is a negative QuantiFERON dated 11/30/2025. That is about 11.5 months before the request, outside the 6-month window, and no newer IGRA or TST is in the chart. (confidence 0.85)

- `PT-3506/labs-2025-11-30` (2025-11-30): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

The 09/22/2026 labs have resulted values for both HBsAg and total anti-HBc, and both are nonreactive. Because neither is reactive, no prophylaxis or monitoring plan is needed. (confidence 0.95)

- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3506/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The 10/22/2026 medication history says there is no current biologic, JAK inhibitor or S1P receptor modulator. The only prior biologic listed, adalimumab, is shown as stopped in 05/2026. The 03/2026 note mentions an unnamed 'current therapy', but no concurrent agent appears in the current record. (confidence 0.80)

- `PT-3506/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 90.4 kg was recorded on 10/26/2026, 23 days before the request, so it is within 90 days. A weight above 85 kg calls for a 520 mg IV dose. The ordered 520 mg IV, then 90 mg SC every 8 weeks starting 8 weeks after the infusion, matches the labeled regimen. (confidence 0.95)

- `PT-3506/gi-note-2026-10-26` (2026-10-26): "Weight 90.4 kg."
- `PT-3506/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 90.4 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report from the past 12 months documenting active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, for PA-3506 (ustekinumab-ttwe), policy criterion B.2 requires direct endoscopic confirmation of active disease within the past 12 months. The only endoscopy in the chart is the 05/2023 diagnostic colonoscopy noted in the outside records dated 2024-10-18, and no findings report is on file. The calprotectin of 511 ug/g from 10/05/2026 (GI note 2026-10-26) is a lab marker, and the policy says lab markers do not count on their own. Please review and tell us whether a qualifying endoscopy report exists or how you would like to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers (calprotectin, CRP, ESR) and cross-sectional imaging do not count on their own.
- **C5b**: Resolution of the conflicting adalimumab history (prior biologic failure or intolerance, or a TNF-blocker contraindication) (who: ordering_provider)
  > Dr. Adeyemi, for PA-3506, criterion B.5(b) has conflicting records. The medication history dated 2026-10-22 lists adalimumab 40 mg every 2 weeks from 05/2024 to 05/2026 with loss of response, based only on patient report. The outside records dated 2024-10-18 say the patient was biologic-naive and declined adalimumab in 05/2024. Please review and document which account is accurate. If the outside records requested on 2026-10-22 have arrived, please send them to us.
  - Would satisfy the policy: Policy B.5(b) accepts documentation that a biologic or targeted synthetic agent for CD or UC was stopped or found insufficient because of inadequate response or intolerance. Examples are prescriber records or pharmacy fill history showing adalimumab use from 05/2024 and the reason it was stopped. The policy also accepts a documented contraindication to TNF blockers.
- **C6**: TB screen (IGRA or TST) with a negative result from the past 6 months (who: ordering_provider)
  > Dr. Adeyemi, for PA-3506, criterion B.6 requires a negative TB screen within the past 6 months. The only screen on file is a negative QuantiFERON TB Gold Plus dated 2025-11-30, which is outside the window. Please review and tell us whether a newer IGRA or TST result exists or how you would like to proceed.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result does not count as negative. If the screen is positive, the policy accepts it only with a chest radiograph showing no active disease and documentation that treatment for latent TB infection has begun.

## Run cost

3 model calls, 20,228 input and 7,704 output tokens, 65.6 s of model time, $0.274 at list price (0 served from cache).

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
