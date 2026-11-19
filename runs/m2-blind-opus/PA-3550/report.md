# PA-3550: ustekinumab-ttwe for PT-3550

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 66.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note of 2026-11-04 states moderately to severely active ileocolonic Crohn's disease. A Harvey-Bradshaw Index of 14 supports active disease. (confidence 0.96)

- `PT-3550/gi-note-2026-11-04` (2026-11-04): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3550/gi-note-2026-11-04` (2026-11-04): "- Harvey-Bradshaw Index today: 14."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The colonoscopy on 2026-10-11 is about 1 month before the request, well inside the 12-month window. It documents ileal ulcers with erythema and edema and an SES-CD of 15, which is active mucosal inflammation seen directly. (confidence 0.96)

- `PT-3550/colonoscopy-2026-10-11` (2026-10-11): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3550/colonoscopy-2026-10-11` (2026-10-11): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-3550/colonoscopy-2026-10-11` (2026-10-11): "SES-CD: 15"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab order appears in a GI follow-up note, which is consistent with a gastroenterology prescriber. (confidence 0.88)

- `PT-3550/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 1996-02-13, the member is 30 years old on the request date of 2026-11-18, which is at least 18. (confidence 0.98)

- `PT-3550/demographics-2026-10-23` (2026-10-23): "Date of birth: 1996-02-13"
- Code checks: age 30 on 2026-11-18 from DOB 1996-02-13

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history lists mercaptopurine (2022-08 to 2023-03) and budesonide (2023-04 to 2023-07). Both are conventional agents and both were stopped for inadequate response, with dates given. (confidence 0.95)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Mercaptopurine | 1.5 mg/kg daily | 2022-08 | 2023-03 | Inadequate response after 6 months at a therapeutic metabolite level |"
- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Budesonide | 9 mg daily | 2023-04 | 2023-07 | Inadequate response after 10 weeks |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab was used from 2023-09 to 2026-07. It was stopped for intolerance (drug-induced lupus), and the dates and reason are documented. (confidence 0.95)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The QuantiFERON-TB Gold Plus result is negative, dated 2026-09-12. That is about 2 months before the request, inside the 6-month window. (confidence 0.95)

- `PT-3550/labs-2026-09-12` (2026-09-12): "QuantiFERON-TB Gold Plus | NEGATIVE | - | Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg and total anti-HBc have results and both are nonreactive. Because neither is reactive, no prophylaxis or monitoring plan is needed. (confidence 0.96)

- `PT-3550/labs-2026-09-12` (2026-09-12): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3550/labs-2026-09-12` (2026-09-12): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The medication history states the member is on no current biologic, JAK inhibitor, or S1P receptor modulator. The prior adalimumab was already stopped in 2026-07. (confidence 0.92)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 66.0 kg was recorded on 2026-11-04, within 90 days of the request, and falls in the above-55 to 85 kg band, which calls for 390 mg IV. The 90 mg SC every 8 weeks maintenance, starting 8 weeks after the infusion, matches the labeled regimen. (confidence 0.95)

- `PT-3550/gi-note-2026-11-04` (2026-11-04): "- Weight 66.0 kg."
- `PT-3550/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.0 kg (2026-11-04) -> label tier 390 mg; requested 390 mg

## Run cost

2 model calls, 16,047 input and 5,453 output tokens, 43.9 s of model time, $0.208 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: clean.

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
