# PA-3580: ustekinumab-aekn for PT-3580

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: URGENT review. Decision within 24 hours of receiving all required information (policy section E). Prescriber attestation of urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 104.9 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The 2026-10-26 GI follow-up note, written by the prescribing gastroenterology service, states moderately to severely active ulcerative pancolitis. A March 2026 GI note also records active UC, which supports the same finding. (confidence 0.90)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy in the chart is a flexible sigmoidoscopy dated 2023-07-18, which documents active inflammation but falls outside the 12-month lookback ending 2025-11-18. No colonoscopy or sigmoidoscopy within the past 12 months appears in the documents provided. (confidence 0.80)

- `PT-3580/flexible-sigmoidoscopy-2023-07-18` (2023-07-18): "Rectum to 31 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology, but no chart passage states the prescriber's specialty or documents a gastroenterology consultation about ustekinumab. The request field alone is not chart evidence of specialty. (confidence 0.60)

- Missing: Chart documentation of prescriber specialty (gastroenterology) for Dr. S. Adeyemi, or a note documenting consultation with a gastroenterologist about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

A date of birth of 2000-10-17 makes the member 26 years old on the 2026-11-18 request date, which meets the age of 18 or older requirement. (confidence 0.97)

- `PT-3580/demographics-2025-11-27` (2025-11-27): "Date of birth: 2000-10-17"
- Code checks: age 26 on 2026-11-18 from DOB 2000-10-17

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): **INSUFFICIENT****: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history says only that there are no steroids at present, and it records no prior conventional agent with dates of use and a reason it was stopped or found insufficient. The expedited reason mentions steroids, but that statement is not a chart record of a prior trial. (confidence 0.70)

- `PT-3580/medication-history-2026-10-24` (2026-10-24): "No steroids at present"
- Missing: Record of a prior conventional agent (oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-ASA for UC) with approximate dates of use and reason stopped or found insufficient

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The IBD medication history records adalimumab, a biologic, used from 2023-07 to 2026-05 and stopped for intolerance (drug-induced lupus with arthralgias). This meets the prior biologic requirement with a stated intolerance reason. (confidence 0.85)

- `PT-3580/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON TB Gold Plus collected 2026-09-10 is reported as negative. That date falls within the 6-month lookback before the 2026-11-18 request. The 2023 QuantiFERON mentioned in the GI note is outside the window and is not relied on. (confidence 0.90)

- `PT-3580/labs-2026-09-10` (2026-09-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both hepatitis B surface antigen and total core antibody are reported nonreactive on 2026-09-10. Because neither result is reactive, no antiviral plan is required. (confidence 0.92)

- `PT-3580/labs-2026-09-10` (2026-09-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3580/labs-2026-09-10` (2026-09-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 2026-10-24 medication history states there is no current biologic or small-molecule advanced therapy. The prior adalimumab was stopped in 2026-05, so the member is not on a concurrent biologic, JAK inhibitor, or S1P modulator. (confidence 0.85)

- `PT-3580/medication-history-2026-10-24` (2026-10-24): "No biologic or small-molecule advanced therapy at present."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 104.9 kg recorded 2026-10-26 is within 90 days of the request and falls in the above-85 kg band, which corresponds to 520 mg induction. The requested regimen of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the labeled adult regimen. (confidence 0.90)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Weight 104.9 kg."
- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 104.9 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Colonoscopy or flexible sigmoidoscopy dated within the past 12 months documenting active mucosal inflammation (who: ordering_provider)
  > Criterion B.2 is not met for PA-3580 (ustekinumab, request date 2026-11-18). The only endoscopy in the chart is a flexible sigmoidoscopy dated 2023-07-18, which is outside the 12-month window, and no colonoscopy or sigmoidoscopy from the past 12 months appears in the documents provided. Please review this criterion with Dr. Adeyemi.
  - Would satisfy the policy: Policy B.2 accepts a colonoscopy, ileocolonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 that documents active mucosal inflammation. Laboratory markers and cross-sectional imaging do not satisfy this criterion.
- **C3**: Chart documentation of Dr. S. Adeyemi's gastroenterology specialty, or a note documenting consultation with a gastroenterologist about ustekinumab (who: practice_staff)
  > Criterion B.3 for PA-3580 needs chart evidence that the prescriber is a gastroenterologist. The request lists Dr. S. Adeyemi, Gastroenterology, but no chart document states the specialty or records a gastroenterology consultation about ustekinumab. Please locate a credential or specialty record for Dr. Adeyemi, or a consult note on ustekinumab, and file it to the chart.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or a documented consultation with a gastroenterologist about ustekinumab. The criterion states no date window.
- **C5a**: Record of a prior conventional agent (oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-ASA for UC) with approximate dates of use and reason stopped or found insufficient (who: practice_staff)
  > Criterion B.5(a) for PA-3580 has no chart record of a prior conventional agent with dates of use and a reason it was stopped or found insufficient. The 2026-10-24 medication history says only "No steroids at present," while the expedited reason mentions steroids. Please search prior notes and medication records for a conventional agent trial with dates and the reason it was stopped, and file what you find.
  - Would satisfy the policy: Policy B.5(a) accepts a documented prior trial of a conventional agent (oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-ASA for UC) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication, with approximate dates of use. The criterion states no date window.

## Run cost

3 model calls, 19,156 input and 11,831 output tokens, 50.9 s of model time, $0.009 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
