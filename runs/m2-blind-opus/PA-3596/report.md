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

The prescriber's GI note of 2026-11-03 names Crohn's disease and calls it moderately to severely active. A Harvey-Bradshaw Index of 13 supports that severity. (confidence 0.95)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Harvey-Bradshaw Index today: 13."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The colonoscopy on 2026-08-16 is about 3 months before the request, so it falls inside the 12-month window. It shows ulcers in the terminal ileum, and pathology confirms chronic active inflammation. (confidence 0.95)

- `PT-3596/colonoscopy-2026-08-16` (2026-08-16): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3596/colonoscopy-2026-08-16` (2026-08-16): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3596/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab plan is written in a GI follow-up note. The quoted passage does not name the author's specialty itself, so the nurse should confirm it. (confidence 0.85)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 2006-05-08, the member is 20 years old on the request date of 2026-11-18. (confidence 0.97)

- `PT-3596/demographics-2026-05-27` (2026-05-27): "Date of birth: 2006-05-08"
- Code checks: age 20 on 2026-11-18 from DOB 2006-05-08

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): **INSUFFICIENT****: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The member is currently on prednisone and still has symptoms. The chart gives no start date for prednisone and no explicit statement that it failed. The 2026-02-18 note mentions ongoing symptoms despite therapy but does not name the therapy. (confidence 0.70)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- Prednisone 20 mg daily, taper planned after induction"
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."
- Missing: Documentation of prior conventional agent (e.g., prednisone) with approximate dates of use and an explicitly documented reason (inadequate response, intolerance, or contraindication)

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The prescriber documents that TNF blockers are contraindicated because of multiple sclerosis. The problem list confirms the MS diagnosis. A documented TNF-blocker contraindication satisfies B.5(b) on its own. (confidence 0.92)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3596/problem-list-2026-11-03` (2026-11-03): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy B.6): **NOT MET**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The only TB screen in the chart is a negative QuantiFERON from 2025-10-20, about 13 months before the request. That is outside the 6-month window, and no more recent IGRA or TST was found. (confidence 0.85)

- `PT-3596/labs-2025-10-20` (2025-10-20): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg (nonreactive) and total anti-HBc (reactive) have results on file. Because the core antibody is reactive, a plan is required, and the GI note documents one: HBV DNA and liver tests every 3 months. (confidence 0.93)

- `PT-3596/labs-2026-10-13` (2026-10-13): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3596/labs-2026-10-13` (2026-10-13): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current medication list contains no other biologic, JAK inhibitor or S1P modulator. Prednisone is not an excluded agent under this policy. (confidence 0.90)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- No biologic or small-molecule advanced therapy at present."
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- Prednisone 20 mg daily, taper planned after induction"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 101.7 kg was recorded on 2026-11-03, within 90 days of the request. It is above 85 kg, so the 520 mg IV band applies. The requested maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the labeled regimen. (confidence 0.95)

- `PT-3596/gi-note-2026-11-03` (2026-11-03): "Weight 101.7 kg."
- `PT-3596/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 101.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C5a**: A documented conventional-agent trial (for example, prednisone) with approximate dates of use and an explicitly stated reason it was stopped or found insufficient (who: ordering_provider)
  > Dr. Adeyemi, for PT-3596's ustekinumab PA (PA-3596), criterion B.5(a) needs a documented trial of a conventional agent with approximate dates and a stated reason: inadequate response, intolerance, or contraindication. The 2026-11-03 GI note lists 'Prednisone 20 mg daily' and persistent symptoms, but it gives no prednisone start date and does not say the prednisone failed. The 2026-02-18 note mentions ongoing symptoms 'despite therapy' but does not name the therapy. Could you review this and document the agent(s), approximate dates of use, and the reason, if that matches the clinical history?
  - Would satisfy the policy: Policy B.5(a) accepts chart documentation that a conventional agent (oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication. The documentation must include approximate dates of use and state the reason explicitly.
- **C6**: A negative IGRA or TST result dated within 6 months of the request (on or after 2026-05-18) (who: ordering_provider)
  > Dr. Adeyemi, for PT-3596's ustekinumab PA (PA-3596), criterion B.6 requires a negative TB screen from the past 6 months. The only screen in the chart is a negative QuantiFERON TB Gold Plus dated 2025-10-20 (labs-2025-10-20), about 13 months before the 2026-11-18 request date, so it does not meet the requirement. Please review and let us know whether a more recent IGRA or TST result exists, for example one done at another facility, or how you would like to proceed.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. Indeterminate or borderline results do not count as negative. If the screen is positive, the member qualifies only if the record shows a chest radiograph without active disease and that treatment for latent TB infection has begun.

## Run cost

3 model calls, 19,747 input and 7,182 output tokens, 63.4 s of model time, $0.260 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
