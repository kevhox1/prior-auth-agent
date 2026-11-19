# PA-3591: ustekinumab-ttwe for PT-3591

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 87.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI prescriber's note dated 2026-10-31 states moderately to severely active ileocolonic Crohn's disease. The Harvey-Bradshaw Index of 10 in the same note is consistent with that assessment. (confidence 0.90)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy with biopsies dated 2026-08-29 falls within the 12-month lookback and documents ulceration, erythema and edema of the terminal ileum. The pathology from the same procedure shows chronic active inflammation. The 2024 colonoscopy and the CRP result do not affect this finding. (confidence 0.90)

- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ordering provider is listed as Gastroenterology in the request, but no chart passage provided quotes the prescriber's specialty or a consultation with a gastroenterologist about ustekinumab. The request header alone is not chart documentation. (confidence 0.60)

- Missing: Chart documentation of prescriber specialty (gastroenterology) for Dr. S. Adeyemi, or a documented gastroenterology consultation about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 1973-05-02 makes the member 53 years old on the 2026-11-18 request date, which is above the age of 18. (confidence 0.95)

- `PT-3591/demographics-2026-02-06` (2026-02-06): "Date of birth: 1973-05-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-05-02

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The outside records document methotrexate 25 mg weekly from 2024-05 to 2024-12, a listed conventional agent. The record gives the stop reason as intolerance (nausea and ALT above 3 times the upper limit of normal). (confidence 0.90)

- `PT-3591/outside-records-2025-01-18` (2025-01-18): "Methotrexate 25 mg subcutaneously weekly, 2024-05 to 2024-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

Infliximab, a TNF-blocker biologic, was used from 2025-02 to 2026-07 and the record gives the stop reason as intolerance (drug-induced lupus). This satisfies the biologic intolerance pathway. (confidence 0.85)

- `PT-3591/medication-history-2026-10-28` (2026-10-28): "Infliximab 5 mg/kg IV every 8 weeks, 2025-02 to 2026-07. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON TB Gold Plus collected 2026-10-08 is within 6 months of the 2026-11-18 request and is reported as negative. No positive screen is recorded that would require further documentation. (confidence 0.90)

- `PT-3591/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

No passage provided contains a hepatitis B surface antigen result or a total hepatitis B core antibody result. The criterion cannot be assessed from the passages given. (confidence 0.90)

- Missing: Hepatitis B surface antigen result
- Missing: Total hepatitis B core antibody result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

Vedolizumab is on the current medication list, and this is a switch. The prescriber's 2026-10-31 note orders vedolizumab stopped, with ustekinumab induction timed to the next scheduled vedolizumab infusion. The stop is documented as a plan, so a reviewer should confirm that the vedolizumab discontinuation is carried out. (confidence 0.70)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3591/medication-history-2026-10-28` (2026-10-28): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-09); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 87.0 kg recorded 2026-10-31 is within 90 days of the request and is above 85 kg, so the labeled induction is 520 mg IV. The requested regimen is 520 mg IV followed by 90 mg SC every 8 weeks starting 8 weeks after induction, which matches the labeled dosing. (confidence 0.90)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Weight 87.0 kg."
- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 87.0 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Chart documentation of Dr. S. Adeyemi's gastroenterology specialty, or a documented gastroenterology consultation about ustekinumab (who: practice_staff)
  > PA-3591 (ustekinumab-ttwe) criterion C3 needs chart documentation that the prescriber is a gastroenterologist or that a gastroenterologist was consulted about ustekinumab. The request header lists Dr. S. Adeyemi as Gastroenterology, but no chart passage states this. Please locate a note, credentialing record, or consult note that documents the specialty or the consult and file it with the request.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or a documented consultation with a gastroenterologist about this treatment. The criterion sets no date window.
- **C7**: Hepatitis B surface antigen result and total hepatitis B core antibody result (who: practice_staff)
  > PA-3591 (ustekinumab-ttwe) criterion C7 needs both a hepatitis B surface antigen (HBsAg) result and a total hepatitis B core antibody (anti-HBc total) result. Neither appears in the passages reviewed, and surface antibody results or pending orders do not count. Please search the chart and any outside lab records for these two results and file them with the request. If a result is reactive, the chart must also document an antiviral prophylaxis or monitoring plan.
  - Would satisfy the policy: Policy B.7 accepts a result for both HBsAg and total hepatitis B core antibody, of any age; the criterion sets no date window. A reactive result must be accompanied by a documented antiviral prophylaxis or monitoring plan. Surface antibody results, vaccination records, and pending orders are not sufficient.

## Run cost

3 model calls, 19,286 input and 12,433 output tokens, 52.6 s of model time, $0.009 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
