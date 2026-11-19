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

The 2026-11-05 GI note, written by the ordering gastroenterologist, states moderately to severely active ileocolonic Crohn's disease. The same note records an HBI of 13, which supports that severity. (confidence 0.90)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Harvey-Bradshaw Index today: 13."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy dated 2026-10-12, within 12 months of the 2026-11-18 request, documents ulcers, erythema and edema in the terminal ileum. Biopsy pathology also reports chronic active inflammation. This is direct endoscopic evidence, not a laboratory marker alone. (confidence 0.90)

- `PT-3593/colonoscopy-2026-10-12` (2026-10-12): "Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3593/colonoscopy-2026-10-12` (2026-10-12): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

Dr. M. Chen is identified as the ordering provider and author of the GI note, and the request lists the specialty as Gastroenterology. The quoted chart text does not itself state the specialty, so the criterion cannot be confirmed from the passages. (confidence 0.40)

- `PT-3593/labs-2026-09-25` (2026-09-25): "COLLECTED: 2026-09-25      ORDERING: Dr. M. Chen"
- Missing: Document header or signature showing Dr. M. Chen's specialty as gastroenterology (the quoted passages name Dr. M. Chen but do not show the specialty)

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 1957-02-24 makes the member 69 years old on the 2026-11-18 request date. This is well above the minimum age of 18. (confidence 0.97)

- `PT-3593/demographics-2026-05-15` (2026-05-15): "Date of birth: 1957-02-24"
- Code checks: age 69 on 2026-11-18 from DOB 1957-02-24

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The outside records document methotrexate use from 2024-03 to 2024-11, stopped for intolerance. They also document azathioprine use from 2024-12 to 2025-02, stopped for intolerance. Either one satisfies the conventional-agent step. (confidence 0.92)

- `PT-3593/outside-records-2025-03-18` (2025-03-18): "Methotrexate 25 mg subcutaneously weekly, 2024-03 to 2024-11. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3593/outside-records-2025-03-18` (2025-03-18): "Azathioprine 2.5 mg/kg daily, 2024-12 to 2025-02. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The medication history records infliximab, a TNF blocker, from 2025-04 to 2026-07. It was stopped for secondary loss of response, which is an inadequate response. This satisfies the biologic step. (confidence 0.90)

- `PT-3593/medication-history-2026-11-05` (2026-11-05): "| Infliximab | 5 mg/kg IV every 8 weeks | 2025-04 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 23 U/mL (reference <10) |"

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The IGRA on 2026-09-25 is positive, so the member follows the positive-screen pathway. The chest radiograph of 2026-09-28 shows no active TB, and the GI note documents rifampin for latent TB started 2026-10-01. The current medication list omits rifampin, but that omission is not a contradicting statement, so the reviewer should confirm rifampin use. (confidence 0.70)

- `PT-3593/labs-2026-09-25` (2026-09-25): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-3593/chest-xray-2026-09-28` (2026-09-28): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

The only hepatitis B result in the chart is a surface antibody, which the policy says is not sufficient. The vaccination series does not count. Neither HBsAg nor total core antibody is documented. (confidence 0.90)

- `PT-3593/labs-2026-09-25` (2026-09-25): "Hepatitis B surface antibody          Reactive (immune)>10 mIU/mL"
- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

Vedolizumab is still listed as current but the prescriber documents that it is being stopped as the member switches to ustekinumab. The policy allows a switch when the earlier biologic is documented as stopping. The reviewer should note that the planned induction date may not match the requested start of 2026-12-01. (confidence 0.75)

- `PT-3593/medication-history-2026-11-05` (2026-11-05): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-24); to be discontinued when ustekinumab starts."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg was recorded on 2026-11-05, within 90 days of the request. At 55.0 kg the labeled induction is 260 mg, which matches the request. The maintenance dose of 90 mg SC every 8 weeks starting 8 weeks after induction also matches. (confidence 0.92)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Weight 55.0 kg."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-05) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C3**: Document header or signature showing Dr. M. Chen's specialty as gastroenterology (who: practice_staff)
  > PA-3593 (ustekinumab), criterion B.3: the chart passages name Dr. M. Chen as ordering provider (labs collected 2026-09-25), but none show the specialty. Please locate a note header, signature block, or credentialing document for Dr. M. Chen that states gastroenterology and file it with the request.
  - Would satisfy the policy: Policy B.3 accepts a document showing that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment. The criterion sets no date window.
- **C7**: Hepatitis B surface antigen (HBsAg) result and total hepatitis B core antibody result (who: lab)
  > PA-3593 (ustekinumab), criterion B.7: the only hepatitis B result on file is a surface antibody ('Hepatitis B surface antibody Reactive (immune) >10 mIU/mL', collected 2026-09-25), which the policy does not accept. Please confirm whether HBsAg and total hepatitis B core antibody results exist, or whether they need to be drawn and the results released. If HBsAg or core antibody is reactive, the policy also requires a documented antiviral prophylaxis or monitoring plan.
  - Would satisfy the policy: Policy B.7 accepts a resulted HBsAg test and a resulted total hepatitis B core antibody test, of any age. Pending orders do not count, and surface antibody results and vaccination records do not count. If either result is reactive, a documented plan for antiviral prophylaxis or monitoring is also required. The criterion sets no date window.

## Run cost

3 model calls, 21,629 input and 17,160 output tokens, 70.6 s of model time, $0.012 at list price (0 served from cache).

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
