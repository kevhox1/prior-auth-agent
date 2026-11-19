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

The 2026-11-03 GI note contains the prescriber's direct statement of moderately to severely active Crohn's disease. The 2026-02-18 note also records active Crohn's disease, and nothing in the chart contradicts this. (confidence 0.93)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The colonoscopy dated 2026-08-16 is within 12 months of the 2026-11-18 request and directly visualizes ulcers, erythema and edema in the terminal ileum. Biopsy pathology from the same procedure shows chronic active inflammation. (confidence 0.90)

- `PT-3596/colonoscopy-2026-08-16` (2026-08-16): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3596/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The lab and note passages name Dr. S. Adeyemi as the ordering provider, but no passage states that Dr. Adeyemi's specialty is gastroenterology. The request form lists the specialty, but that is not a chart document, so the chart does not yet confirm it. (confidence 0.60)

- Missing: Chart documentation of Dr. S. Adeyemi's specialty (gastroenterology), such as a signature block or credentials line in the GI note
- Missing: Or a documented consultation with a gastroenterologist about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

A date of birth of 2006-05-08 makes the member 20 years old on the 2026-11-18 request date, which satisfies the 18-or-older requirement. (confidence 0.97)

- `PT-3596/demographics-2026-05-27` (2026-05-27): "Date of birth: 2006-05-08"
- Code checks: age 20 on 2026-11-18 from DOB 2006-05-08

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): **INSUFFICIENT****: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Prednisone is listed only as current therapy with no start date, and no note says a conventional agent was stopped or found insufficient. The phrase 'ongoing symptoms despite current therapy' does not name the agent or give a reason it was stopped. (confidence 0.70)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Prednisone 20 mg daily, taper planned after induction"
- `PT-3596/gi-note-2026-02-18` (2026-02-18): "Ongoing symptoms despite current therapy."
- Missing: Record of a prior conventional agent (corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-ASA for UC) with approximate dates of use
- Missing: Documented reason that agent was stopped or found insufficient (inadequate response, intolerance, or contraindication)

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The prescriber's 2026-11-03 note documents a contraindication to TNF blockers, which the policy accepts as an alternative to a prior biologic trial. The problem list confirms the relapsing-remitting multiple sclerosis diagnosis the contraindication cites. (confidence 0.80)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3596/problem-list-2026-11-03` (2026-11-03): "Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy B.6): **NOT MET**
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The only TB screen in the documents is a negative QuantiFERON collected 2025-10-20, about 13 months before the 2026-11-18 request. That falls outside the 6-month lookback, and no TB test within the window appears in the records searched. (confidence 0.80)

- `PT-3596/labs-2025-10-20` (2025-10-20): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- `PT-3596/labs-2025-10-20` (2025-10-20): "COLLECTED: 2025-10-20      ORDERING: Dr. S. Adeyemi"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both required results are on file from 2026-10-13: HBsAg nonreactive and total core antibody reactive. Because the core antibody is reactive, the 2026-11-03 note documents a monitoring plan (HBV DNA and liver tests every 3 months). The note's wording 'on therapy' is slightly unclear, so confidence is moderate. (confidence 0.72)

- `PT-3596/labs-2026-10-13` (2026-10-13): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3596/labs-2026-10-13` (2026-10-13): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 2026-11-03 GI note states there is no current biologic or small-molecule advanced therapy, and the current medication list shows no such agent. The member is not switching, so no stop documentation is needed. (confidence 0.88)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "No biologic or small-molecule advanced therapy at present."
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- Omeprazole 20 mg daily"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 101.7 kg recorded 2026-11-03 is within 90 days of the request and is above 85 kg, which maps to the 520 mg induction band. The requested 520 mg IV induction followed by 90 mg SC every 8 weeks starting 8 weeks later matches the labeled regimen. (confidence 0.93)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Weight 101.7 kg."
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 101.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Chart documentation of Dr. S. Adeyemi's specialty (gastroenterology), such as a signature block or credentials line, or a documented consultation with a gastroenterologist about ustekinumab (who: practice_staff)
  > Criterion B.3 (prescriber specialty) is not yet confirmed from the chart for PA-3596. The request form lists Dr. S. Adeyemi as Gastroenterology, but no chart document states it. Please locate a signature block or credentials line from Dr. Adeyemi's GI note, or a note documenting a consult with a gastroenterologist about ustekinumab.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted with a gastroenterologist about this treatment. The criterion sets no date window.
- **C5a**: Record of a prior conventional agent (corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or oral 5-ASA for UC) with approximate dates of use, and the documented reason it was stopped or found insufficient (who: ordering_provider)
  > Criterion B.5(a) (prior conventional therapy) is not met for PA-3596. The chart lists prednisone 20 mg daily (GI note 2026-11-03) and 'ongoing symptoms despite current therapy' (GI note 2026-02-18), but no prior conventional agent is named with dates or a reason it was stopped or found insufficient. Please review and document any prior conventional agent, its approximate dates, and the reason it was stopped or found insufficient.
  - Would satisfy the policy: Policy B.5(a) accepts documentation that a listed conventional agent was stopped or found insufficient because of inadequate response, intolerance, or contraindication, with approximate dates of use. The criterion sets no date window.
- **C6**: Negative interferon-gamma release assay (QuantiFERON) or tuberculin skin test dated within the 6-month lookback; the only screen on file is the negative QuantiFERON collected 2025-10-20 (who: ordering_provider)
  > Criterion B.6 (TB screening) is not met for PA-3596. The only TB screen in the records is the negative QuantiFERON collected 2025-10-20, which is outside the 6-month window. Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. Please review whether a TB screen within that window is documented or needed.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result does not count as negative. A positive screen qualifies only with a chest radiograph showing no active disease and documented treatment for latent infection that has begun.

## Run cost

3 model calls, 20,104 input and 13,117 output tokens, 56.0 s of model time, $0.010 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
