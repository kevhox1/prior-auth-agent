# PA-3534: ustekinumab-aekn for PT-3534

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: URGENT review. Decision within 24 hours of receiving all required information (policy section E). Prescriber attestation of urgency is required. Work this case first.
- Ordered dose: 390 mg IV once (weight 66.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The 2026-11-09 GI follow-up note states the prescriber's assessment of moderately to severely active ileocolonic Crohn's disease. The same note records a Harvey-Bradshaw Index of 13 and uncontrolled symptoms. (confidence 0.93)

- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3534/gi-note-2026-11-09` (2026-11-09): "Symptoms not controlled on current therapy; missing work."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy in the chart is a colonoscopy dated 2025-04-18, which is outside the 12-month lookback from the 2026-11-18 request date. No endoscopy within the past 12 months is documented, so the direct-visualization requirement is not met. (confidence 0.80)

- `PT-3534/colonoscopy-2025-04-18` (2025-04-18): "PROCEDURE: Colonoscopy with biopsies"
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The GI note and the request name a gastroenterology ordering provider, but no passage in the chart explicitly states Dr. Adeyemi's specialty or documents a GI consultation about ustekinumab. The specialty listed on the request form alone is not a chart passage. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (gastroenterology) for Dr. S. Adeyemi
- Missing: Or a documented consultation with a gastroenterologist about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 03/19/1992 gives an age of 34 on the 2026-11-18 request date, which is at least 18. (confidence 0.97)

- `PT-3534/demographics-2026-04-29` (2026-04-29): "Date of birth: 03/19/1992"
- Code checks: age 34 on 2026-11-18 from DOB 1992-03-19

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history records budesonide (a listed conventional agent) used from 05/2019 to 08/2019. It was stopped for inadequate response after 10 weeks, which satisfies sub-criterion (a). (confidence 0.90)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Budesonide 9 mg daily, 05/2019 to 08/2019. Reason stopped: inadequate response after 10 weeks."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The medication history records infliximab, a biologic, used from 07/2023 to 07/2026. It was stopped for secondary loss of response, which satisfies sub-criterion (b). Under C5 (any part), this alone is enough. (confidence 0.90)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON-TB Gold Plus (IGRA) result of negative was collected 2026-10-21. That is within the 6-month lookback from the 2026-11-18 request date. (confidence 0.92)

- `PT-3534/labs-2026-10-21` (2026-10-21): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total hepatitis B core antibody are documented as nonreactive on 2026-10-21. Because neither result is reactive, no antiviral plan is required. (confidence 0.92)

- `PT-3534/labs-2026-10-21` (2026-10-21): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3534/labs-2026-10-21` (2026-10-21): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The reconciled medication list states there is no current biologic, JAK inhibitor, or S1P modulator. The prior infliximab is documented as stopped in 07/2026, so the switch has the earlier agent ending. (confidence 0.88)

- `PT-3534/medication-history-2026-11-08` (2026-11-08): "No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3534/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 66.2 kg recorded 2026-11-09 is within 90 days of the request and falls in the 390 mg band (above 55 kg up to 85 kg). The requested 390 mg IV induction followed by 90 mg SC every 8 weeks from 8 weeks after induction matches the labeled regimen. (confidence 0.93)

- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Weight 66.2 kg."
- `PT-3534/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.2 kg (2026-11-09) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy dated within the past 12 months documenting active mucosal inflammation (ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy) (who: ordering_provider)
  > PA-3534 (ustekinumab) criterion C2 is not met. The only endoscopy in the chart is the colonoscopy dated 2025-04-18, which is outside the 12-month lookback from the 2026-11-18 request date. Please review whether an endoscopy within the policy window exists or is planned, since B.2 requires direct visualization with documented active mucosal inflammation.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 that documents active mucosal inflammation. Fecal calprotectin, CRP, sedimentation rate, or cross-sectional imaging do not satisfy this criterion on their own.
- **C3**: Chart documentation of Dr. S. Adeyemi's gastroenterology specialty, or a documented GI consultation about ustekinumab (who: practice_staff)
  > PA-3534 criterion C3 has insufficient evidence. The request names Dr. S. Adeyemi as Gastroenterology, but no chart passage states the specialty or documents a GI consultation about ustekinumab. Please locate a chart document (for example a signed note header, credentialing record, or consult note) that shows Dr. Adeyemi's gastroenterology specialty, or a consult note about ustekinumab, and file it to the request.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted with a gastroenterologist about this treatment. The criterion states no date window.

## Run cost

3 model calls, 19,083 input and 10,769 output tokens, 47.0 s of model time, $0.008 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
