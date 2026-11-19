# PA-3593: ustekinumab-ttwe for PT-3593

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

In the 2026-11-05 GI note, the prescriber writes that the patient has moderately to severely active ileocolonic Crohn's disease. That one statement gives both the diagnosis and the severity. (confidence 0.95)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A colonoscopy on 2026-10-12, which is within 12 months of the request, found multiple ulcers in the terminal ileum, and pathology showed chronic active inflammation. The lab markers are not needed to meet this criterion. (confidence 0.95)

- `PT-3593/colonoscopy-2026-10-12` (2026-10-12): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3593/colonoscopy-2026-10-12` (2026-10-12): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. M. Chen, Gastroenterology. The ustekinumab plan was written in a GI follow-up note. The quoted passage does not state the specialty itself, so the reviewer should check the note header. (confidence 0.85)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

Date of birth 1957-02-24 makes the member 69 on the request date of 2026-11-18. The outside records show the same date of birth. (confidence 0.97)

- `PT-3593/demographics-2026-05-15` (2026-05-15): "Date of birth: 1957-02-24"
- Code checks: age 69 on 2026-11-18 from DOB 1957-02-24

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate (2024-03 to 2024-11) and azathioprine (2024-12 to 2025-02) were both stopped for documented intolerance. Each is a conventional agent listed in the policy. (confidence 0.93)

- `PT-3593/outside-records-2025-03-18` (2025-03-18): "- Methotrexate 25 mg subcutaneously weekly, 2024-03 to 2024-11. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3593/outside-records-2025-03-18` (2025-03-18): "- Azathioprine 2.5 mg/kg daily, 2024-12 to 2025-02. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab was used from 2025-04 to 2026-07 and stopped for secondary loss of response. Drug levels and antibody results back this up. That counts as inadequate response to a biologic. (confidence 0.93)

- `PT-3593/medication-history-2026-11-05` (2026-11-05): "| Infliximab | 5 mg/kg IV every 8 weeks | 2025-04 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 23 U/mL (reference <10) |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The IGRA on 2026-09-25, within 6 months, was positive. The policy's exception for a positive screen is satisfied: the 2026-09-28 chest radiograph shows no active TB, and rifampin for latent TB started on 2026-10-01. (confidence 0.90)

- `PT-3593/labs-2026-09-25` (2026-09-25): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-3593/chest-xray-2026-09-28` (2026-09-28): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

The chart has only a surface antibody result and a vaccination record. The policy says neither is enough. No resulted HBsAg or total anti-HBc test was found. (confidence 0.93)

- `PT-3593/labs-2026-09-25` (2026-09-25): "Hepatitis B surface antibody          Reactive (immune)>10 mIU/mL"
- `PT-3593/outside-records-2025-03-18` (2025-03-18): "Immunizations: hepatitis B vaccine series x3, completed."
- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The patient is switching from vedolizumab, and both the GI note and the medication history say it is being stopped when ustekinumab starts. The only other current CD drug listed is budesonide, which is not a biologic, JAK inhibitor or S1P modulator. (confidence 0.90)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3593/medication-history-2026-11-05` (2026-11-05): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-24); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 55.0 kg was recorded on 2026-11-05, within 90 days of the request, and falls in the band up to and including 55 kg, which calls for 260 mg IV. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the label. (confidence 0.92)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Weight 55.0 kg."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-05) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C7**: Resulted HBsAg and total anti-HBc (core antibody) results (who: practice_staff)
  > For PA-3593 (ustekinumab-ttwe, PT-3593), criterion B.7 needs resulted hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results. The chart only has a surface antibody result (labs 2026-09-25, 'Reactive (immune)') and a vaccination record (outside records 2025-03-18), and the policy does not accept either one. Can you check the chart, the outside records and past lab reports for HBsAg and total anti-HBc results of any date and file them? If none exist, please tell Dr. Chen so the provider can decide how to proceed.
  - Would satisfy the policy: Policy B.7 accepts resulted HBsAg and total anti-HBc tests from any date (no recency window). If either result is reactive, the policy also needs a documented plan for antiviral prophylaxis or monitoring. Pending orders, surface antibody results and vaccination records are not accepted.

## Run cost

3 model calls, 20,569 input and 7,176 output tokens, 65.9 s of model time, $0.266 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
