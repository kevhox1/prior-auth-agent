# PA-3596: ustekinumab-ttwe for PT-3596

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 101.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-11-03 states moderately to severely active ileocolonic Crohn's disease. This is the prescriber statement the criterion requires. (confidence 0.96)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy on 2026-08-16 is within 12 months of the 2026-11-18 request. It shows terminal ileal ulcers, and biopsy confirms active inflammation. (confidence 0.96)

- `PT-3596/colonoscopy-2026-08-16` (2026-08-16): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3596/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No passage from the chart states the prescriber's specialty or documents a gastroenterology consultation. The specialty appears only in the request form, not in a quoted chart passage. (confidence 0.70)

- Missing: Chart documentation of the prescriber's specialty (gastroenterologist), such as a signed note or provider credentials
- Missing: Documentation of gastroenterology consultation if the prescriber is not a gastroenterologist

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 2006-05-08 makes the member 20 years old on the request date 2026-11-18. This is over 18. (confidence 0.98)

- `PT-3596/demographics-2026-05-27` (2026-05-27): "Date of birth: 2006-05-08"
- Code checks: age 20 on 2026-11-18 from DOB 2006-05-08

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

The policy accepts a documented contraindication to TNF blockers under option (b). The GI note documents one because of multiple sclerosis, and the problem list confirms the MS diagnosis. (confidence 0.85)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3596/problem-list-2026-11-03` (2026-11-03): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy B.6): **NOT MET**
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The only TB screen is a negative QuantiFERON dated 2025-10-20, about 13 months before the request. That is outside the 6-month window, and no more recent IGRA or TST is in the chart. (confidence 0.88)

- `PT-3596/labs-2025-10-20` (2025-10-20): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg (nonreactive) and total core antibody (reactive) results are on file. The reactive core antibody has a documented monitoring plan of HBV DNA and liver tests every 3 months. (confidence 0.92)

- `PT-3596/labs-2026-10-13` (2026-10-13): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3596/labs-2026-10-13` (2026-10-13): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The current medication list shows no biologic, JAK inhibitor or S1P modulator. Prednisone and omeprazole are not in the excluded classes, so there is nothing to combine or stop. (confidence 0.88)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

Weight of 101.7 kg is above 85 kg, so the 520 mg IV induction is correct. The 90 mg SC every 8 weeks maintenance starting 8 weeks later matches the label. The weight was recorded on 2026-11-03, within 90 days of the request. (confidence 0.95)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Weight 101.7 kg."
- Code checks: weight 101.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consultation (who: practice_staff)
  > For PA-3596 (PT-3596), criterion C3 (policy B.3) needs chart documentation that the prescriber is a gastroenterologist. Could you locate or file a signed note or provider credentials showing Dr. S. Adeyemi's specialty? The specialty currently appears only on the request form.
  - Would satisfy the policy: Policy B.3 accepts chart documentation, such as a signed note or provider credentials, showing the prescriber is a gastroenterologist, or documentation of a consultation with a gastroenterologist about this treatment.
- **C6**: Negative IGRA or TST dated within 6 months of request, or the policy's positive-screen documentation (who: ordering_provider)
  > For PA-3596 (PT-3596), criterion C6 (policy B.6) is not met on the current record. The only TB screen is a negative QuantiFERON dated 2025-10-20 (labs-2025-10-20), about 13 months before the 2026-11-18 request and outside the 6-month window. Please review and advise whether a more recent IGRA or TST result exists or will be documented.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result does not count as negative. A positive screen qualifies only with a chest radiograph showing no active disease and documentation that latent TB treatment has begun.

## Run cost

3 model calls, 17,658 input and 5,546 output tokens, 34.8 s of model time, $0.105 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | MET | - | FALSE MET |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
