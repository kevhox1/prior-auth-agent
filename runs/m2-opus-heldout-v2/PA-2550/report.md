# PA-2550: ustekinumab-aekn for PT-2550

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 71.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

In the 2026-11-08 GI note, the prescriber writes that the patient has moderately to severely active ileocolonic Crohn's disease. The problem list and outside records also record the Crohn's diagnosis. (confidence 0.95)

- `PT-2550/gi-note-2026-11-08` (2026-11-08): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is the colonoscopy of 2025-03-18. It shows active inflammation but is about 20 months before the 2026-11-18 request, outside the 12-month window. The raised CRP and the Harvey-Bradshaw score do not count under the policy, and no endoscopy within the window was found. (confidence 0.80)

- `PT-2550/colonoscopy-2025-03-18` (2025-03-18): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-2550/labs-2026-09-07` (2026-09-07): "C-reactive protein                    12.2 mg/L     <5.0"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ustekinumab order is in a GI follow-up note. The request lists the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.85)

- `PT-2550/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 390 mg IV once (weight 71.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a birth date of 1989-08-06, the member is 37 on the 2026-11-18 request date. The outside records show the same birth date. (confidence 0.97)

- `PT-2550/demographics-2026-02-20` (2026-02-20): "Date of birth: 1989-08-06"
- Code checks: age 37 on 2026-11-18 from DOB 1989-08-06

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Budesonide was used from 2023-12 to 2024-03 and stopped for inadequate response. Prednisone was used from 2024-04 to 2024-12 and stopped because of steroid dependence. Both are conventional agents, and each entry gives dates and a reason. (confidence 0.92)

- `PT-2550/medication-history-2026-11-06` (2026-11-06): "Budesonide 9 mg daily, 2023-12 to 2024-03. Reason stopped: inadequate response after 10 weeks."
- `PT-2550/medication-history-2026-11-06` (2026-11-06): "Prednisone 40 mg daily, tapered, 2024-04 to 2024-12. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The medication history, based on patient report, says adalimumab was taken from 2025-02 and stopped for loss of response. The 2025-06 outside records say the patient declined adalimumab in 2025-02 and had never had a biologic. Nothing in the chart settles which is right, and the confirming outside records are still on request. (confidence 0.80)

- `PT-2550/medication-history-2026-11-06` (2026-11-06): "Adalimumab 40 mg every 2 weeks, 2025-02 to 2026-05. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-2550/outside-records-2025-06-18` (2025-06-18): "- Biologic-naive. Adalimumab was recommended 2025-02 but the patient declined."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON-TB Gold Plus test of 2026-09-07 is negative. That is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-2550/labs-2026-09-07` (2026-09-07): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both the hepatitis B surface antigen and the total core antibody were resulted as nonreactive on 2026-09-07. Because neither is reactive, no antiviral plan is required. (confidence 0.96)

- `PT-2550/labs-2026-09-07` (2026-09-07): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-2550/labs-2026-09-07` (2026-09-07): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current medication list shows no biologic, JAK inhibitor or S1P modulator. The only current IBD drug is a budesonide bridge, which is a conventional agent. The reported prior adalimumab ended 2026-05. (confidence 0.88)

- `PT-2550/medication-history-2026-11-06` (2026-11-06): "- No biologic or small-molecule advanced therapy at present."
- `PT-2550/medication-history-2026-11-06` (2026-11-06): "- Budesonide 9 mg daily (bridge)"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 71.4 kg was recorded on 2026-11-08, within 90 days of the request, and falls in the >55 to 85 kg band, which calls for a 390 mg IV dose. The order is 390 mg IV once, then 90 mg SC every 8 weeks starting 8 weeks after the infusion, which matches the labeled regimen. (confidence 0.95)

- `PT-2550/gi-note-2026-11-08` (2026-11-08): "- Weight 71.4 kg."
- `PT-2550/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 390 mg IV once (weight 71.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 71.4 kg (2026-11-08) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report dated on or after 2025-11-18 showing active mucosal inflammation (who: ordering_provider)
  > Dr. Chen, for PT-2550 (ustekinumab-aekn, PA-2550), Calder policy B.2 requires an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from the past 12 months that shows active mucosal inflammation. The only endoscopy in the chart is the colonoscopy of 2025-03-18, which is about 20 months old. Under the policy, the CRP of 12.2 mg/L (2026-09-07) and the Harvey-Bradshaw score do not count. Please review and tell us whether a qualifying endoscopy done on or after 2025-11-18 exists, or how you want to proceed.
- **C5b**: Resolution of whether adalimumab was taken and stopped for inadequate response, with supporting outside records (who: ordering_provider)
  > Dr. Chen, for PT-2550 (PA-2550), Calder policy B.5(b) requires a prior biologic or targeted synthetic agent that failed or was not tolerated, or a documented TNF-blocker contraindication. Two chart records disagree. The medication history of 2026-11-06 (from patient report) lists adalimumab 40 mg every 2 weeks from 2025-02 to 2026-05, stopped for loss of response. The outside records of 2025-06-18 say the patient declined adalimumab in 2025-02 and was biologic-naive. Please review and document which is correct, and send any confirming records (such as the outside records already requested) if available.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
