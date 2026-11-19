# PA-3590: ustekinumab-aekn for PT-3590

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 106.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

In the 2026-11-07 GI note, the prescriber states the disease is moderately to severely active ulcerative pancolitis. The problem list confirms the UC diagnosis (K51.00), which matches the requested indication. (confidence 0.96)

- `PT-3590/gi-note-2026-11-07` (2026-11-07): "Moderately to severely active ulcerative pancolitis."
- `PT-3590/problem-list-2026-11-07` (2026-11-07): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2019."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A flexible sigmoidoscopy on 2026-08-18 falls about 3 months before the 2026-11-18 request, inside the 12-month window. It documents continuous inflammation with friability and erosions (Mayo endoscopic subscore 2), and pathology shows chronic active inflammation. (confidence 0.95)

- `PT-3590/flexible-sigmoidoscopy-2026-08-18` (2026-08-18): "PROCEDURE: Flexible sigmoidoscopy with biopsies"
- `PT-3590/flexible-sigmoidoscopy-2026-08-18` (2026-08-18): "- Rectum to 36 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 2."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request names the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab plan appears in a GI follow-up note. (confidence 0.90)

- `PT-3590/gi-note-2026-11-07` (2026-11-07): "- Start ustekinumab-aekn: 520 mg IV once (weight 106.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a DOB of 2006-07-11, the member is 20 years old on the 2026-11-18 request date. The outside records list the same DOB. (confidence 0.98)

- `PT-3590/demographics-2026-03-03` (2026-03-03): "Date of birth: 2006-07-11"
- Code checks: age 20 on 2026-11-18 from DOB 2006-07-11

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Outside records show azathioprine (2019-12 to 2020-02) stopped for intolerance (pancreatitis) and mesalamine (2020-03 to 2020-07) stopped for inadequate response; mesalamine counts because the diagnosis is UC. The 2026-11-05 medication history says only "no prior IBD therapy documented". That is a gap in the record, not a statement that these drugs were never given, so it does not create a conflict. (confidence 0.82)

- `PT-3590/outside-records-2023-12-18` (2023-12-18): "- Azathioprine 2.5 mg/kg daily, 2019-12 to 2020-02. Reason stopped: intolerance (acute pancreatitis)."
- `PT-3590/outside-records-2023-12-18` (2023-12-18): "- Mesalamine 4.8 g daily, 2020-03 to 2020-07. Reason stopped: inadequate response at full dose after 12 weeks."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Outside records show adalimumab was taken from 2023-07 to 2023-11 and stopped for primary non-response. The medication history line "no prior IBD therapy documented" is missing information, not an affirmative statement that the drug was never taken. (confidence 0.82)

- `PT-3590/outside-records-2023-12-18` (2023-12-18): "- Adalimumab 40 mg every 2 weeks, 2023-07 to 2023-11. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON-TB Gold Plus on 2026-09-22 was negative. That date is within 6 months of the 2026-11-18 request. (confidence 0.96)

- `PT-3590/labs-2026-09-22` (2026-09-22): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

HBsAg and total anti-HBc were both resulted on 2026-09-22, and both were nonreactive. Because neither is reactive, no prophylaxis plan is needed. (confidence 0.97)

- `PT-3590/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3590/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current medication history says the member is not on any biologic, JAK inhibitor, or S1P receptor modulator. The prior adalimumab was stopped in 2023-11. (confidence 0.92)

- `PT-3590/medication-history-2026-11-05` (2026-11-05): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 106.3 kg was recorded on 2026-11-07, within 90 days of the request. Above 85 kg, the labeled IV dose is 520 mg, which matches the request. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, also matches the label. (confidence 0.96)

- `PT-3590/gi-note-2026-11-07` (2026-11-07): "Weight 106.3 kg."
- `PT-3590/gi-note-2026-11-07` (2026-11-07): "- Start ustekinumab-aekn: 520 mg IV once (weight 106.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.3 kg (2026-11-07) -> label tier 520 mg; requested 520 mg

## Run cost

2 model calls, 17,013 input and 6,096 output tokens, 49.5 s of model time, $0.229 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: buried_evidence.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
