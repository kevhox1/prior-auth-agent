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

The GI note from 2026-10-31 names Crohn's disease and says it is moderately to severely active. The problem list and outside records also show the Crohn's diagnosis. (confidence 0.95)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The colonoscopy on 2026-08-29 is within 12 months of the 2026-11-18 request. It shows ulcers in the terminal ileum, and the biopsies show chronic active inflammation. The CRP result was not used to decide this criterion. (confidence 0.95)

- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab plan is written in the GI follow-up note. (confidence 0.90)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a birth date of 1973-05-02, the patient is 53 on the 2026-11-18 request date. The outside records show the same birth date. (confidence 0.98)

- `PT-3591/demographics-2026-02-06` (2026-02-06): "Date of birth: 1973-05-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-05-02

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Methotrexate is a conventional agent. It was used from 2024-05 to 2024-12 and stopped for intolerance (nausea and ALT above 3 times the upper limit of normal). The current prednisone was not used for this criterion. (confidence 0.92)

- `PT-3591/outside-records-2025-01-18` (2025-01-18): "- Methotrexate 25 mg subcutaneously weekly, 2024-05 to 2024-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab, a biologic, was used from 2025-02 to 2026-07. It was stopped for intolerance (drug-induced lupus). The vedolizumab reason is only implied, so it was not relied on. (confidence 0.92)

- `PT-3591/medication-history-2026-10-28` (2026-10-28): "Infliximab 5 mg/kg IV every 8 weeks, 2025-02 to 2026-07. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON TB Gold Plus test on 2026-10-08 was negative. That is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-3591/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

None of the passages contain a hepatitis B surface antigen result or a total core antibody result. Both results are required. (confidence 0.90)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

Vedolizumab is the only current biologic. Both the prescriber's note and the medication history say it will be stopped when ustekinumab starts. Prednisone is not a biologic, JAK inhibitor or S1P receptor modulator. (confidence 0.88)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3591/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-09); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 87.0 kg on 2026-10-31 is within 90 days and above 85 kg, so 520 mg IV is the right dose. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the label. The note says 'weight down 3 kg' but gives no starting point. The only other weight, 84.9 kg on 2026-05-24, is outside the 90-day window, so it was not treated as a conflict, but the reviewer may want to confirm the current weight. (confidence 0.75)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Weight 87.0 kg."
- `PT-3591/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 87.0 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C7**: Hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results (who: practice_staff)
  > For PA-3591 (PT-3591, ustekinumab-ttwe), the reviewed records have no hepatitis B surface antigen result and no total hepatitis B core antibody result. Calder policy B.7 needs both results. Can you find and file both lab reports from any date? If either one is reactive, please also include the documented plan for antiviral prophylaxis or monitoring.
  - Would satisfy the policy: Policy B.7 accepts resulted HBsAg and total anti-HBc tests of any date (on or before the 2026-11-18 request). If either is reactive, it also needs a documented plan for antiviral prophylaxis or monitoring. Surface antibody (anti-HBs) results, vaccination records and pending orders do not count.

## Run cost

3 model calls, 19,583 input and 6,771 output tokens, 61.1 s of model time, $0.250 at list price (0 served from cache).

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
