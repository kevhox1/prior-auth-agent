# PA-3592: ustekinumab-ttwe for PT-3592

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The prescriber's 10/30/2026 GI note states moderately to severely active ileocolonic Crohn's disease, which directly meets the requirement. Supporting findings in the same note are 5-7 stools a day and a Harvey-Bradshaw Index of 13. (confidence 0.93)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The chart contains only laboratory markers (fecal calprotectin and CRP), which the policy says cannot satisfy this requirement. No endoscopy report appears in the passages, so the endoscopic requirement cannot be confirmed. (confidence 0.90)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "His calprotectin from 08/23/2026 came back at 1306 ug/g (lab reference <50)."
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated within the past 12 months (on or after 2025-11-18)
- Missing: Endoscopy report documenting active mucosal inflammation

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

Dr. M. Chen is named as the ordering provider on the 09/21/2026 labs, and the request lists the specialty as gastroenterology. However, the chart passages do not state the specialty themselves, so the specialty must be confirmed from a chart document. (confidence 0.60)

- `PT-3592/labs-2026-09-21` (2026-09-21): "ORDERING: Dr. M. Chen"
- Missing: Chart document stating Dr. M. Chen's specialty as gastroenterology (or documentation of a gastroenterology consultation about ustekinumab)

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 05/12/1990 makes the member 36 years old on the 2026-11-18 request date, which satisfies the age of 18 or older requirement. (confidence 0.97)

- `PT-3592/demographics-2025-10-15` (2025-10-15): "Date of birth: 05/12/1990"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-12

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history records a budesonide course from 09/2022 to 12/2022 that was stopped for inadequate response. Budesonide is a listed conventional agent, so this sub-criterion is satisfied. (confidence 0.92)

- `PT-3592/medication-history-2026-10-28` (2026-10-28): "| Budesonide | 9 mg daily | 09/2022 | 12/2022 | Inadequate response after 10 weeks |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The 10/30/2026 GI note documents a contraindication to TNF blockers due to multiple sclerosis, and the problem list supports that diagnosis. This satisfies the alternative in this sub-criterion, and the prior biologic (vedolizumab) does not need to be assessed for it. (confidence 0.88)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3592/problem-list-2026-10-30` (2026-10-30): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

No tuberculosis screening result appears in any passage. The chart therefore has no negative IGRA or tuberculin skin test within the 6-month window. (confidence 0.92)

- Missing: Interferon-gamma release assay or tuberculin skin test result dated on or after 2026-05-18 (within 6 months of the request), reported as negative

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

The 09/21/2026 labs show a nonreactive hepatitis B surface antigen and a nonreactive total hepatitis B core antibody. Both results are determinate and reactive-result rules do not apply. (confidence 0.93)

- `PT-3592/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3592/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

Vedolizumab is currently listed, which would be a concurrent biologic, but the prescriber's 10/30/2026 note documents that it is being stopped with ustekinumab induction. No other concurrent biologic, JAK inhibitor, or S1P modulator is listed. The medication history gives no stop date, so a reviewer should confirm the final vedolizumab dose timing. (confidence 0.80)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3592/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/16/2026); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg recorded 10/30/2026 is within 90 days of the request and falls in the 260 mg induction band, and the requested 260 mg IV then 90 mg SC every 8 weeks matches the labeled regimen. A 58.0 kg weight from 06/01/2026 is outside the 90-day window but differs from the current weight, so the reviewer should confirm the current weight. (confidence 0.80)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Weight 55.0 kg."
- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-30) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C2**: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report documenting active mucosal inflammation, dated within the past 12 months (who: practice_staff)
  > PA-3592 criterion C2 (policy B.2) is open. The chart has only lab markers (fecal calprotectin 1306 ug/g on 08/23/2026 and CRP), and the policy does not accept labs alone. Please check whether an endoscopy report (colonoscopy, ileocolonoscopy, or flexible sigmoidoscopy) dated on or after 2025-11-18 that documents active mucosal inflammation is on file or held by an outside facility, and send it to Dr. M. Chen for review.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Fecal calprotectin, CRP, sedimentation rate, and cross-sectional imaging do not satisfy this item alone.
- **C3**: Chart document stating Dr. M. Chen's specialty as gastroenterology, or documentation of a gastroenterology consultation about ustekinumab (who: practice_staff)
  > PA-3592 criterion C3 (policy B.3) is open. The 09/21/2026 labs list Dr. M. Chen as ordering provider, and the request lists gastroenterology, but no chart passage states the specialty. Please file a document from Dr. M. Chen's chart (such as a credentialing or practice profile page or a visit note header) that states the gastroenterology specialty, or add a GI consult note about ustekinumab if one exists.
  - Would satisfy the policy: Policy B.3 accepts a chart document showing that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment. The policy sets no date window for this item.
- **C6**: Negative interferon-gamma release assay (IGRA) or tuberculin skin test result for tuberculosis screening (who: lab)
  > PA-3592 criterion C6 (policy B.6) is open. No tuberculosis screening result appears anywhere in the chart. Please confirm whether a TB screening test (IGRA or tuberculin skin test) has been drawn or is pending, and forward the result to Dr. M. Chen for review.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or tuberculin skin test dated on or after 2026-05-18. An indeterminate or borderline result does not count as negative. A positive screen qualifies only with a chest radiograph showing no active disease and documented treatment for latent infection.

## Run cost

3 model calls, 19,199 input and 11,929 output tokens, 51.1 s of model time, $0.009 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
