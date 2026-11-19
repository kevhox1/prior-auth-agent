# PA-3504: ustekinumab-aekn for PT-3504

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

The 2026-10-31 GI follow-up note states the prescriber's assessment of moderately to severely active ileocolonic Crohn's disease. The note also records a Harvey-Bradshaw Index of 12 and uncontrolled symptoms. (confidence 0.93)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3504/gi-note-2026-10-31` (2026-10-31): "Harvey-Bradshaw Index today: 12."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy with biopsies dated 2026-08-16 is within the 12-month lookback from the 2026-11-18 request. The report documents ulcers, erythema and edema on direct visualization, and biopsy pathology confirms chronic active inflammation. (confidence 0.92)

- `PT-3504/colonoscopy-2026-08-16` (2026-08-16): "Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3504/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The gastroenterology specialty appears only in the request form, not in any chart passage provided. No passage documents a specialty listing or a consultation about ustekinumab. (confidence 0.60)

- Missing: Chart documentation of the ordering prescriber's specialty (for example, a signature block or provider header identifying Dr. A. Rivera as gastroenterology), or a documented gastroenterology consultation about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 2000-04-27 gives an age of 26 on the 2026-11-18 request date, which is at least 18. (confidence 0.97)

- `PT-3504/demographics-2026-02-05` (2026-02-05): "Date of birth: 2000-04-27"
- Code checks: age 26 on 2026-11-18 from DOB 2000-04-27

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Oral prednisone was used from 2023-05 to 2024-01 and stopped. The record gives the reason as steroid dependence, with flares each time the dose fell below 15 mg, which is an inadequate response. (confidence 0.85)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Prednisone | 40 mg daily, tapered | 2023-05 | 2024-01 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

Infliximab, a TNF blocker, was used from 2024-03 to 2026-09 and stopped for intolerance, documented as drug-induced lupus with arthralgias. This meets the biologic prior-therapy requirement. (confidence 0.90)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Infliximab | 5 mg/kg IV every 8 weeks | 2024-03 | 2026-09 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON-TB Gold Plus test collected 2026-09-20 is negative and falls within the 6-month lookback from 2026-11-18. No positive screen is documented. (confidence 0.92)

- `PT-3504/labs-2026-09-20` (2026-09-20): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total hepatitis B core antibody were resulted as nonreactive on 2026-09-20. Because neither result is reactive, no prophylaxis plan is required. (confidence 0.92)

- `PT-3504/labs-2026-09-20` (2026-09-20): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3504/labs-2026-09-20` (2026-09-20): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 2026-10-29 medication history lists no current biologic, JAK inhibitor, or S1P receptor modulator. The prior infliximab has a stop date of 2026-09, so the earlier agent is documented as stopped before ustekinumab. (confidence 0.87)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Infliximab | 5 mg/kg IV every 8 weeks | 2024-03 | 2026-09 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg recorded 2026-10-31 is within 90 days of the request and falls in the 260 mg band (up to and including 55 kg). The requested 260 mg IV induction and 90 mg SC every 8 weeks starting 8 weeks later match the labeled regimen. (confidence 0.90)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "Weight 55.0 kg."
- `PT-3504/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-31) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C3**: Chart documentation of ordering prescriber's gastroenterology specialty (e.g., signature block or provider header identifying Dr. A. Rivera as gastroenterology), or a documented gastroenterology consultation about ustekinumab (who: ordering_provider)
  > Criterion C3 (policy B.3) is open because the chart does not show Dr. A. Rivera's gastroenterology specialty and no gastroenterology consultation about ustekinumab is documented. Please review and provide a signature block or provider header identifying Dr. Rivera as gastroenterology, or a gastroenterology consultation note about ustekinumab.
  - Would satisfy the policy: Policy B.3 accepts documentation that the prescriber is a gastroenterologist, or that a gastroenterologist was consulted about ustekinumab, dated on or before the request date of 2026-11-18.

## Run cost

3 model calls, 18,788 input and 9,761 output tokens, 40.3 s of model time, $0.008 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: borderline.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
