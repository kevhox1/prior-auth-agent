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

The GI note dated 2026-10-31 states moderately to severely active ulcerative pancolitis. This is the prescriber's statement in the clinical record. (confidence 0.96)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A flexible sigmoidoscopy on 2026-08-14 is within 12 months of the request. It documents active mucosal inflammation with erosions. (confidence 0.96)

- `PT-3518/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "Rectum to 28 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No retrieved chart passage states the prescriber's specialty or documents a gastroenterology consult. The request lists Gastroenterology, but that is not chart documentation. (confidence 0.60)

- Missing: Documentation of Dr. M. Chen's specialty (gastroenterology) in the chart, or a gastroenterology consultation note

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 1971-07-19 makes the member 55 on the request date of 2026-11-18, which is over 18. (confidence 0.98)

- `PT-3518/demographics-2026-10-23` (2026-10-23): "Date of birth: 1971-07-19"
- Code checks: age 55 on 2026-11-18 from DOB 1971-07-19

### C5 (policy B.5): **CONFLICTING**
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

The GI note says infliximab was given 2023-07 to 2026-09 and stopped working. The outside records from 2023-11 say the patient was biologic-naive and declined infliximab. Nothing in the chart resolves this, and the only other therapy listed (prednisone) has no documented failure or intolerance. (confidence 0.80)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-3518/outside-records-2023-11-18` (2023-11-18): "- Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON dated 2026-10-04 is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-3518/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented and nonreactive, so no prophylaxis plan is needed. (confidence 0.96)

- `PT-3518/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3518/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The 2026-10-31 note states no current biologic or small-molecule advanced therapy. Infliximab, if used, ended 2026-09, so there is no combination. (confidence 0.90)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

Weight of 97.3 kg recorded 2026-10-31 is within 90 days and is above 85 kg, so 520 mg IV is the correct tier. Maintenance of 90 mg SC every 8 weeks starting 8 weeks after the infusion matches the label. (confidence 0.95)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Weight 97.3 kg."
- Code checks: weight 97.3 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Chart documentation of Dr. Chen's gastroenterology specialty or a GI consult note (who: practice_staff)
  > For PA-3518 (PT-3518), criterion C3 (policy B.3) needs chart documentation that Dr. M. Chen is a gastroenterologist, or a gastroenterology consultation note about ustekinumab. The request lists Gastroenterology, but no chart document states it. Can you file or point us to a document showing this?
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation of a consultation with a gastroenterologist about this treatment.
- **C5**: Provider review of conflicting infliximab history, with outside records or attestation (who: ordering_provider)
  > For PA-3518, criterion C5 (prior therapy) has conflicting records. Your GI note of 2026-10-31 lists infliximab 5 mg/kg IV q8w from 2023-07 to 2026-09, stopped because it stopped working, per patient report with outside records requested. The outside records of 2023-11-18 say "Biologic-naive. Infliximab was recommended 2023-07 but the patient declined." Please review and clarify the history, and add any documentation that supports it, such as infusion or pharmacy records or the requested outside records. Prednisone is also listed, but no failure or intolerance is documented.
  - Would satisfy the policy: Policy B.5 accepts documentation of at least one prior therapy: a conventional agent (corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate) or a biologic or targeted agent, with the drug, approximate dates and the reason it was stopped (inadequate response, intolerance or contraindication). Records that resolve the infliximab conflict would meet this, as would documented failure or intolerance of a conventional agent such as prednisone.

## Run cost

3 model calls, 17,783 input and 5,234 output tokens, 33.6 s of model time, $0.102 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | CONFLICTING | - | wrong |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
