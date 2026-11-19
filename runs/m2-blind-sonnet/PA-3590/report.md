# PA-3590: ustekinumab-aekn for PT-3590

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 106.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note dated 2026-11-07 states moderately to severely active ulcerative pancolitis. This is the prescriber's statement in the clinical record. (confidence 0.96)

- `PT-3590/gi-note-2026-11-07` (2026-11-07): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A flexible sigmoidoscopy on 2026-08-18, within 12 months of the 2026-11-18 request, documents active mucosal inflammation. Biopsy also shows chronic active inflammation. (confidence 0.96)

- `PT-3590/flexible-sigmoidoscopy-2026-08-18` (2026-08-18): "- Rectum to 36 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 2."
- `PT-3590/flexible-sigmoidoscopy-2026-08-18` (2026-08-18): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No retrieved chart passage states the prescriber's specialty or a gastroenterology consultation. The specialty appears only in the request form, not in a chart passage. (confidence 0.70)

- Missing: Documentation in the chart of the prescriber's specialty (gastroenterology) for Dr. S. Adeyemi, or a documented gastroenterology consultation

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 2006-07-11 makes the member 20 years old on the 2026-11-18 request date. A second document gives the same DOB. (confidence 0.98)

- `PT-3590/demographics-2026-03-03` (2026-03-03): "Date of birth: 2006-07-11"
- Code checks: age 20 on 2026-11-18 from DOB 2006-07-11

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Outside records name azathioprine (stopped for intolerance), mesalamine and adalimumab (stopped for primary non-response), with dates and reasons. The 2026-11-05 medication history says 'no prior IBD therapy documented', which is an omission and not an affirmative statement that these were never given. (confidence 0.88)

- `PT-3590/outside-records-2023-12-18` (2023-12-18): "- Azathioprine 2.5 mg/kg daily, 2019-12 to 2020-02. Reason stopped: intolerance (acute pancreatitis)."
- `PT-3590/outside-records-2023-12-18` (2023-12-18): "- Adalimumab 40 mg every 2 weeks, 2023-07 to 2023-11. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON dated 2026-09-22 falls within 6 months of the request date. (confidence 0.95)

- `PT-3590/labs-2026-09-22` (2026-09-22): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented and nonreactive. No prophylaxis plan is needed. (confidence 0.96)

- `PT-3590/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3590/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The current medication history states the member is on no biologic, JAK inhibitor or S1P modulator. Prior adalimumab ended in 2023, so nothing would be combined with ustekinumab. (confidence 0.93)

- `PT-3590/medication-history-2026-11-05` (2026-11-05): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

Weight 106.3 kg is above 85 kg, so 520 mg IV is the correct tier, followed by 90 mg SC every 8 weeks starting 8 weeks later. The weight was recorded on 2026-11-07, within 90 days of the request. (confidence 0.95)

- `PT-3590/gi-note-2026-11-07` (2026-11-07): "- Start ustekinumab-aekn: 520 mg IV once (weight 106.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3590/gi-note-2026-11-07` (2026-11-07): "Weight 106.3 kg."
- Code checks: weight 106.3 kg (2026-11-07) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Chart documentation of Dr. Adeyemi's gastroenterology specialty or a documented GI consultation (who: practice_staff)
  > For PA-3590 (PT-3590, ustekinumab-aekn), criterion C3 (policy B.3) requires the prescriber to be a gastroenterologist or to have consulted one. The specialty of Dr. S. Adeyemi appears only on the request form, not in a chart passage. Can you locate and file a chart document, such as a clinic note, signature block or credentialing record, showing Dr. Adeyemi's gastroenterology specialty? If none exists, a documented GI consultation would also work.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist (e.g., a note or signature block listing Gastroenterology for Dr. S. Adeyemi) or documentation of a consultation with a gastroenterologist about this treatment.

## Run cost

3 model calls, 18,057 input and 5,447 output tokens, 33.9 s of model time, $0.106 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: buried_evidence.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
