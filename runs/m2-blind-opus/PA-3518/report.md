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

The 2026-10-31 GI note states the diagnosis is UC. It also states the disease is moderately to severely active. The problem list agrees with this diagnosis (K51.00). (confidence 0.95)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A flexible sigmoidoscopy on 2026-08-14 falls within 12 months of the 2026-11-18 request. It documents active mucosal inflammation (Mayo endoscopic subscore 3), and the biopsy shows chronic active inflammation. (confidence 0.95)

- `PT-3518/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "- Rectum to 28 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-3518/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. M. Chen, Gastroenterology. The ustekinumab plan comes from a GI follow-up note. The quoted passage does not name the specialty itself, so the reviewer may want to confirm the note's author. (confidence 0.85)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The date of birth is 1971-07-19, so the member is 55 on the 2026-11-18 request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-3518/demographics-2026-10-23` (2026-10-23): "Date of birth: 1971-07-19"
- Code checks: age 55 on 2026-11-18 from DOB 1971-07-19

### C5 (policy B.5): **CONFLICTING**
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): **INSUFFICIENT****: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Prednisone is listed as a current medication, but there is no start date and no stated reason of inadequate response, intolerance or contraindication tied to it. The 2026-05-01 note does not name the therapy that symptoms persisted on. (confidence 0.70)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "- Prednisone 20 mg daily, taper planned after induction"
- `PT-3518/gi-note-2026-05-01` (2026-05-01): "Follow-up of ulcerative colitis. Ongoing symptoms despite current therapy."
- Missing: Documentation naming a conventional agent (e.g., prednisone or 5-ASA) with approximate dates of use and a documented inadequate response, intolerance, or contraindication

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The GI note says the patient was on infliximab from 2023-07 and lost response, based on patient report. Outside records from 2023-11-18 say the patient declined infliximab in 2023-07 and was biologic-naive. The two statements cannot both be true, and the outside records the GI note requested are not on file to settle it. (confidence 0.85)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-3518/outside-records-2023-11-18` (2023-11-18): "- Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON (IGRA) result dated 2026-10-04 is negative. That is within 6 months of the request. (confidence 0.95)

- `PT-3518/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg and total anti-HBc have results, and both are nonreactive. No prophylaxis plan is needed. (confidence 0.95)

- `PT-3518/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3518/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current GI note says no biologic or small-molecule advanced therapy is in use. The dermatology note mentions immunosuppression without naming an agent, and current prednisone could explain that. No concurrent advanced therapy is documented. (confidence 0.80)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The 2026-10-31 weight of 97.3 kg is within 90 days of the request and above 85 kg, so 520 mg IV is the correct induction dose. Maintenance is 90 mg SC every 8 weeks, starting 8 weeks after the infusion, which matches the label. (confidence 0.95)

- `PT-3518/gi-note-2026-10-31` (2026-10-31): "Weight 97.3 kg."
- `PT-3518/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 97.3 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C5a**: A note naming the conventional agent tried, the approximate dates of use, and the documented inadequate response, intolerance, or contraindication (who: ordering_provider)
  > Dr. Chen, for PA-3518 (ustekinumab-ttwe, UC), criterion B.5(a) is not yet documented. The 2026-10-31 GI note lists prednisone 20 mg daily but gives no start date and no reason, and the 2026-05-01 note says "ongoing symptoms despite current therapy" without naming the therapy. Please review and document which conventional agent(s) the patient used (for example prednisone or an oral 5-ASA), the approximate dates, and whether there was an inadequate response, intolerance, or contraindication.
  - Would satisfy the policy: Policy B.5(a) accepts documentation naming a conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate, or for UC an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication.
- **C5b**: Resolution of the conflicting prior-infliximab history, e.g. the outside infusion or treatment records requested in the 2026-10-31 note (who: ordering_provider)
  > Dr. Chen, for PA-3518, criterion B.5(b) has conflicting records. Your 2026-10-31 note records infliximab 5 mg/kg every 8 weeks from 2023-07 to 2026-09, stopped for loss of response per patient report. The outside records dated 2023-11-18 say the patient declined infliximab in 2023-07 and was biologic-naive. Please review and tell us which history is correct, and send any supporting records, such as the outside records your note says were requested.
  - Would satisfy the policy: Policy B.5(b) accepts documentation that a biologic or targeted synthetic agent for CD or UC was stopped or found insufficient because of inadequate response or intolerance (for example infusion or administration records showing infliximab use and the reason it was stopped), or a documented contraindication to TNF blockers.

## Run cost

3 model calls, 31,208 input and 9,840 output tokens, 82.2 s of model time, $0.332 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
