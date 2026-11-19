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

The GI follow-up note dated 2026-11-07 states the member has moderately to severely active ulcerative pancolitis. The problem list entry only gives the diagnosis without severity, but the GI note supplies the required statement. (confidence 0.88)

- `PT-3590/gi-note-2026-11-07` (2026-11-07): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A flexible sigmoidoscopy dated 2026-08-18 falls within the 12 months before the 2026-11-18 request and documents continuous inflammation with erosions and a Mayo endoscopic subscore of 2. The same-day pathology shows chronic active inflammation. The calprotectin and CRP values were not used to satisfy this item. (confidence 0.90)

- `PT-3590/flexible-sigmoidoscopy-2026-08-18` (2026-08-18): "Rectum to 36 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 2."
- `PT-3590/flexible-sigmoidoscopy-2026-08-18` (2026-08-18): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider's specialty as Gastroenterology, but no chart passage shows the prescriber's specialty or a consult with a gastroenterologist about ustekinumab. The PCP note only says the bowel disease is followed by GI, which does not confirm the prescriber's specialty. (confidence 0.60)

- `PT-3590/pcp-visit-2026-06-30` (2026-06-30): "No acute complaints today besides known bowel disease (followed by GI)."
- Missing: Chart document confirming Dr. S. Adeyemi's specialty as gastroenterology (for example, a signed GI note showing the author and credentials)
- Missing: Or documentation of a consultation with a gastroenterologist about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 2006-07-11 makes the member 20 years old on the 2026-11-18 request date, which meets the 18-year minimum. (confidence 0.97)

- `PT-3590/demographics-2026-03-03` (2026-03-03): "Date of birth: 2006-07-11"
- Code checks: age 20 on 2026-11-18 from DOB 2006-07-11

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The outside records list azathioprine from 2019-12 to 2020-02, stopped for intolerance (acute pancreatitis), and oral mesalamine from 2020-03 to 2020-07, stopped for inadequate response. The 2026-11-05 medication history says no prior IBD therapy is documented, but that is an omission rather than a statement that the drugs were never given, so it is not treated as a conflict; a reviewer should still check it. (confidence 0.80)

- `PT-3590/outside-records-2023-12-18` (2023-12-18): "Azathioprine 2.5 mg/kg daily, 2019-12 to 2020-02. Reason stopped: intolerance (acute pancreatitis)."
- `PT-3590/outside-records-2023-12-18` (2023-12-18): "Mesalamine 4.8 g daily, 2020-03 to 2020-07. Reason stopped: inadequate response at full dose after 12 weeks."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The outside records show adalimumab, a TNF-blocker biologic, given 2023-07 to 2023-11 and stopped for primary non-response. The 2026-11-05 medication history omits it, which is treated as an omission, not a contradiction. A TNF-blocker trial before ustekinumab is not required in any case. (confidence 0.80)

- `PT-3590/outside-records-2023-12-18` (2023-12-18): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2023-11. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON-TB Gold Plus result dated 2026-09-22 is negative and falls within 6 months of the 2026-11-18 request. No positive screen is documented, so the chest radiograph and latent TB treatment clause does not apply. (confidence 0.92)

- `PT-3590/labs-2026-09-22` (2026-09-22): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

The 2026-09-22 labs include a nonreactive hepatitis B surface antigen and a nonreactive total hepatitis B core antibody. Both results are required by the policy and both are nonreactive, so no antiviral plan is needed. (confidence 0.93)

- `PT-3590/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3590/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 2026-11-05 medication history states the member is not currently on any biologic, JAK inhibitor, or S1P receptor modulator. The dermatology reference to immunosuppression is non-specific and does not name an agent, so it does not contradict this. (confidence 0.85)

- `PT-3590/medication-history-2026-11-05` (2026-11-05): "Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 106.3 kg recorded 2026-11-07 is within 90 days of the request. At that weight the 520 mg IV induction matches the above-85 kg band, and the 90 mg SC every 8 weeks starting 8 weeks after induction matches the labeled maintenance. (confidence 0.90)

- `PT-3590/gi-note-2026-11-07` (2026-11-07): "Weight 106.3 kg."
- `PT-3590/gi-note-2026-11-07` (2026-11-07): "Start ustekinumab-aekn: 520 mg IV once (weight 106.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.3 kg (2026-11-07) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Chart document confirming Dr. S. Adeyemi's gastroenterology specialty (e.g., a signed GI note showing author and credentials), or documentation of a consult with a gastroenterologist about ustekinumab (who: practice_staff)
  > For PA-3590 (ustekinumab), criterion C3 (B.3) is open because the chart does not show Dr. S. Adeyemi's specialty or a GI consult about ustekinumab. The 2026-06-30 PCP note only says the bowel disease is 'followed by GI.' Please locate a signed gastroenterology note or credential record for Dr. Adeyemi, or any note documenting a GI consult about ustekinumab, and file it with the request.
  - Would satisfy the policy: Criterion B.3 is met by documentation that the prescriber is a gastroenterologist, or that the prescriber consulted with a gastroenterologist about ustekinumab. The criterion sets no date window for this evidence.

## Run cost

3 model calls, 31,780 input and 15,722 output tokens, 61.8 s of model time, $0.012 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: buried_evidence.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
