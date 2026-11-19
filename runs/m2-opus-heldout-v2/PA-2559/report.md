# PA-2559: ustekinumab-aekn for PT-2559

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 108.5 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI prescriber's 2026-11-04 assessment says the patient has Crohn's disease and that it is moderately to severely active. The problem list gives the same diagnosis under code K50.80. (confidence 0.95)

- `PT-2559/gi-note-2026-11-04` (2026-11-04): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is the colonoscopy from 2023-10-18, which is more than 12 months before the 2026-11-18 request. The recent calprotectin and CRP results are lab markers, and the policy says these do not meet the requirement on their own. (confidence 0.70)

- `PT-2559/colonoscopy-2023-10-18` (2023-10-18): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-2559/labs-2026-10-08` (2026-10-08): "CALPROTECTIN FECAL ................ 1122 ug/g  (<50)"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. A. Rivera, Gastroenterology. The ustekinumab plan appears in that provider's GI follow-up note. (confidence 0.92)

- `PT-2559/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-aekn: 520 mg IV once (weight 108.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a birth date of 03/08/1974, the member is 52 on the 2026-11-18 request date. The outside records give the same birth date. (confidence 0.98)

- `PT-2559/demographics-2026-09-15` (2026-09-15): "Date of birth: 03/08/1974"
- Code checks: age 52 on 2026-11-18 from DOB 1974-03-08

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Mercaptopurine and budesonide are both conventional agents. Each is documented with dates of use and a reason of inadequate response. (confidence 0.93)

- `PT-2559/gi-note-2026-01-27` (2026-01-27): "- History: Mercaptopurine 1.5 mg/kg daily, 09/2021 to 03/2022. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."
- `PT-2559/gi-note-2026-01-27` (2026-01-27): "- History: Budesonide 9 mg daily, 04/2022 to 07/2022. Reason stopped: inadequate response after 10 weeks."

**C5b (policy B.5(b)): **CONFLICTING****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The 2026 GI note says, based on patient report, that adalimumab was taken from 07/2023 and lost response. The 2024 outside records say the patient declined adalimumab in 07/2023 and was still biologic-naive. The outside records the GI note requested are not in the chart, so nothing settles which is right; C5 can still be met through C5a. (confidence 0.75)

- `PT-2559/gi-note-2026-11-04` (2026-11-04): "- Prior biologic: Adalimumab 40 mg every 2 weeks, 07/2023 to 09/2026. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-2559/outside-records-2024-01-18` (2024-01-18): "- Biologic-naive. Adalimumab was recommended 07/2023 but the patient declined."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON (IGRA) result is negative. It is dated 2026-10-08, which is within 6 months of the request. (confidence 0.95)

- `PT-2559/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

None of the retrieved passages contain a hepatitis B surface antigen result or a total core antibody result. (confidence 0.90)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current GI note says the patient is on no biologic or small-molecule advanced therapy, so nothing would be combined with ustekinumab. Any earlier adalimumab is recorded as stopped in 09/2026. (confidence 0.85)

- `PT-2559/gi-note-2026-11-04` (2026-11-04): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 108.5 kg was recorded on 2026-11-04, within 90 days of the request, and falls in the above-85 kg band that calls for 520 mg IV. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the labeled regimen. (confidence 0.95)

- `PT-2559/gi-note-2026-11-04` (2026-11-04): "- Weight 108.5 kg."
- `PT-2559/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-aekn: 520 mg IV once (weight 108.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 108.5 kg (2026-11-04) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report from within 12 months (after 2025-11-18) showing active mucosal inflammation (who: ordering_provider)
  > Dr. Rivera, for the PA-2559 ustekinumab-aekn request, Calder policy B.2 requires an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from the past 12 months that documents active mucosal inflammation. The only endoscopy in the chart is the colonoscopy dated 2023-10-18, which is more than 12 months before the 2026-11-18 request. The fecal calprotectin of 1122 ug/g from 2026-10-08 is a lab marker, and the policy says lab markers do not meet this requirement on their own. Please review, and tell us if an endoscopy report from within the past 12 months exists that we should file.
- **C5b**: Provider review of the conflicting adalimumab history (who: ordering_provider)
  > Dr. Rivera, for PA-2559 (policy B.5(b)), the records disagree about adalimumab. Your 2026-11-04 GI note says the patient took adalimumab from 07/2023 to 09/2026 and lost response, based on patient report. The outside records dated 2024-01-18 say the patient declined adalimumab in 07/2023 and was biologic-naive. The outside records your note requested are not in the chart. Please review and document which history is accurate. B.5 can still be met through B.5(a).
- **C7**: Hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results (who: practice_staff)
  > For PA-2559 (ustekinumab-aekn), Calder policy B.7 requires results for both the hepatitis B surface antigen (HBsAg) and the total hepatitis B core antibody (anti-HBc). Results of any age are accepted. We found neither result in the chart. Please search for prior results and file them. Surface antibody results, vaccination records and pending orders do not count. If neither test was ever done, please tell Dr. Rivera.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | NOT_MET | NOT_MET | ok (alternate) |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
