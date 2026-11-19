# PA-2570: ustekinumab-aekn for PT-2570

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 108.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-11-04 states moderately to severely active ileocolonic Crohn's disease. The problem list confirms the Crohn's diagnosis with code K50.80. (confidence 0.96)

- `PT-2570/gi-note-2026-11-04` (2026-11-04): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2570/problem-list-2026-11-04` (2026-11-04): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A colonoscopy on 2026-09-21, about 2 months before the request, found ulcers in the terminal ileum. Pathology confirmed chronic active inflammation. The visualization requirement is met directly, without relying on the lab markers. (confidence 0.95)

- `PT-2570/colonoscopy-2026-09-21` (2026-09-21): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-2570/colonoscopy-2026-09-21` (2026-09-21): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. A. Rivera, Gastroenterology. The ustekinumab plan appears in a GI follow-up note. The quoted passage itself does not name the specialty, so the nurse may want to confirm credentials. (confidence 0.90)

- `PT-2570/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-aekn: 520 mg IV once (weight 108.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

Two documents give the same date of birth, 1996-11-13. That makes the member 30 years old on the request date of 2026-11-18. (confidence 0.98)

- `PT-2570/demographics-2026-11-03` (2026-11-03): "Date of birth: 1996-11-13"
- `PT-2570/outside-records-2024-01-18` (2024-01-18): "PT: DELACROIX, SAMUEL     DOB 1996-11-13"
- Code checks: age 30 on 2026-11-18 from DOB 1996-11-13

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Budesonide is a conventional agent under the policy. It was used from 2023-03 to 2023-06 and stopped for inadequate response. (confidence 0.93)

- `PT-2570/medication-history-2026-11-03` (2026-11-03): "Budesonide 9 mg daily, 2023-03 to 2023-06. Reason stopped: inadequate response after 10 weeks."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Infliximab, a biologic, was used from 2023-08 to 2023-12. It was stopped for primary non-response, which is an inadequate response. (confidence 0.93)

- `PT-2570/outside-records-2024-01-18` (2024-01-18): "- Infliximab 5 mg/kg IV every 8 weeks, 2023-08 to 2023-12. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON test on 2026-10-04 is within 6 months and was positive. The positive-screen exception is satisfied: the 2026-10-07 chest X-ray shows no active TB, and rifampin for latent TB started on 2026-10-14. (confidence 0.92)

- `PT-2570/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... POSITIVE  (Negative)"
- `PT-2570/chest-xray-2026-10-07` (2026-10-07): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2570/gi-note-2026-11-04` (2026-11-04): "Latent TB infection: rifampin daily for 4 months, started 2026-10-14."

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg (nonreactive) and total anti-HBc (reactive) have results on file. Because anti-HBc is reactive, a plan is required, and the 2026-11-04 note documents HBV DNA and liver test monitoring every 3 months. (confidence 0.94)

- `PT-2570/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2570/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-2570/gi-note-2026-11-04` (2026-11-04): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The current medication history states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The earlier infliximab was stopped in 2023-12. (confidence 0.92)

- `PT-2570/medication-history-2026-11-03` (2026-11-03): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 108.4 kg was recorded on 2026-11-04, within 90 days of the request, and is above 85 kg, so the 520 mg IV dose is the right one. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the labeled regimen. (confidence 0.95)

- `PT-2570/gi-note-2026-11-04` (2026-11-04): "Weight 108.4 kg."
- `PT-2570/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-aekn: 520 mg IV once (weight 108.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 108.4 kg (2026-11-04) -> label tier 520 mg; requested 520 mg

## Run cost

2 model calls, 17,247 input and 6,399 output tokens, 48.4 s of model time, $0.237 at list price (0 served from cache).

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
