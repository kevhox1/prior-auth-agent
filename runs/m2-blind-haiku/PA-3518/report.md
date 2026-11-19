# PA-3518: ustekinumab-ttwe for PT-3518

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 97.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The prescriber's GI note of 2026-10-31 states moderately to severely active ulcerative pancolitis, matching the requested indication K51.00. No passage contradicts this statement. (confidence 0.90)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A flexible sigmoidoscopy dated 2026-08-14 is within 12 months of the 2026-11-18 request and documents continuous inflammation with erosions (Mayo endoscopic subscore 3). The CRP result is not relied on for this determination. (confidence 0.90)

- `PT-3518/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "Rectum to 28 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-3518/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request form names Dr. M. Chen as Gastroenterology, but no chart passage states the prescriber's specialty or documents a gastroenterology consultation about ustekinumab. The request field alone is not chart evidence. (confidence 0.60)

- Missing: Chart documentation of Dr. M. Chen's specialty as gastroenterology (for example, signed note credentials), or a documented consultation with a gastroenterologist about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth 1971-07-19 gives an age of 55 on the 2026-11-18 request date, which meets the 18-or-older requirement. (confidence 0.95)

- `PT-3518/demographics-2026-10-23` (2026-10-23): "Date of birth: 1971-07-19"
- Code checks: age 55 on 2026-11-18 from DOB 1971-07-19

### C5 (policy B.5): **CONFLICTING**
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): **INSUFFICIENT****: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The chart shows current oral prednisone, which is still ongoing and was not documented as stopped or insufficient. No dates or reason are recorded for any prior conventional agent course. (confidence 0.70)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Prednisone 20 mg daily, taper planned after induction"
- Missing: Dates of use and documented reason (inadequate response, intolerance, or contraindication) for any prior conventional agent: oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-aminosalicylate for UC

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The 2026-10-31 GI note says infliximab was taken from 2023-07 to 2026-09 and stopped for loss of response, but the 2023-11-18 outside record says the patient was biologic-naive and declined infliximab. The chart does not resolve whether any biologic was ever taken, so this criterion cannot be decided. (confidence 0.75)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-3518/outside-records-2023-11-18` (2023-11-18): "Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON TB Gold Plus result dated 2026-10-04 is within 6 months of the request date and is reported as negative. No passage reports an indeterminate or positive result. (confidence 0.92)

- `PT-3518/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both required hepatitis B results, surface antigen and total core antibody, are present on the 2026-10-04 lab report and are nonreactive. Because neither result is reactive, no antiviral plan is required. (confidence 0.93)

- `PT-3518/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3518/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 2026-10-31 GI note states there is no current biologic or small-molecule advanced therapy, so there is no concurrent agent. The infliximab history conflict in C5b does not change current concurrency, though the earlier stop is documented only by an end date. (confidence 0.72)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "No biologic or small-molecule advanced therapy at present."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 97.3 kg recorded 2026-10-31 is within 90 days of the request and is above 85 kg, which requires the 520 mg IV induction. The requested 520 mg IV then 90 mg SC every 8 weeks starting 8 weeks after induction matches the labeled regimen. (confidence 0.92)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Weight 97.3 kg."
- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 97.3 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Chart documentation of Dr. M. Chen's gastroenterology specialty (signed note credentials), or a documented gastroenterology consultation about ustekinumab (who: practice_staff)
  > For PA-3518 (criterion C3, prescriber specialty), the request form lists Dr. M. Chen as Gastroenterology, but no chart document states this. Please locate a signed note with Dr. Chen's credentials or a documented gastroenterology consultation about ustekinumab, and file it with the request. The policy does not state a date window for this item.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist (such as signed note credentials), or documentation that the prescriber consulted a gastroenterologist about this treatment. The criterion sets no date window.
- **C5a**: Dates of use and documented reason (inadequate response, intolerance, or contraindication) for any prior conventional agent: oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-aminosalicylate for UC (who: practice_staff)
  > For PA-3518 (criterion C5a, conventional agent history), the chart shows current prednisone 20 mg daily from the 2026-10-31 GI note but no dates or stop reason for any prior conventional agent. Please search the chart and pharmacy history for prior corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-ASA courses and file any dates and documented reasons. The policy does not state a date window for this item.
  - Would satisfy the policy: Policy B.5(a) accepts documentation of the dates of use and the documented reason (inadequate response, intolerance, or contraindication) for a prior conventional agent, as listed in the criterion. The criterion sets no date window. Ongoing prednisone documented as not yet stopped or found insufficient does not by itself satisfy this item.
- **C5b**: Resolution of the conflicting biologic history: outside records confirming whether infliximab was taken (2023-07 to 2026-09) and the documented reason it was stopped, or a documented contraindication to TNF blockers (who: ordering_provider)
  > For PA-3518 (criterion C5b, prior biologic), the 2026-10-31 GI note records infliximab from 2023-07 to 2026-09 stopped for loss of response, but the 2023-11-18 outside record states the patient was biologic-naive and declined infliximab. Please review both records and document which account is correct. The outside records requested in the GI note are still pending.
  - Would satisfy the policy: Policy B.5(b) accepts documentation that a biologic or targeted synthetic agent for CD or UC was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. The records must resolve the current conflict over whether infliximab was taken and why it stopped. The criterion sets no date window.

## Run cost

3 model calls, 28,541 input and 19,629 output tokens, 81.4 s of model time, $0.014 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
