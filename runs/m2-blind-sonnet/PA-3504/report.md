# PA-3504: ustekinumab-aekn for PT-3504

**Outcome: READY_FOR_REVIEW**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note dated 2026-10-31 states moderately to severely active ileocolonic Crohn's disease. This is the prescriber's statement the criterion requires. (confidence 0.96)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy on 2026-08-16, within 12 months of the 2026-11-18 request, shows ulcers in the terminal ileum. Biopsy pathology also reports active inflammation. (confidence 0.97)

- `PT-3504/colonoscopy-2026-08-16` (2026-08-16): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3504/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. A. Rivera, Gastroenterology. The 2026-10-31 GI follow-up note on biologic planning is that provider's note. The quoted heading does not itself name the specialty, so the reviewer should confirm it. (confidence 0.82)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "#IBD follow-up (Crohn's disease)"

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Born 2000-04-27, the member is 26 on the request date of 2026-11-18, so is over 18. (confidence 0.99)

- `PT-3504/demographics-2026-02-05` (2026-02-05): "Date of birth: 2000-04-27"
- Code checks: age 26 on 2026-11-18 from DOB 2000-04-27

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Infliximab was used from 2024-03 to 2026-09 and stopped for intolerance. Prednisone was used from 2023-05 to 2024-01 with steroid dependence. Either one satisfies the criterion, and the drug, dates and reason are all recorded. (confidence 0.96)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Infliximab | 5 mg/kg IV every 8 weeks | 2024-03 | 2026-09 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"
- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Prednisone | 40 mg daily, tapered | 2023-05 | 2024-01 | Steroid dependent (flared each time the dose went below 15 mg) |"

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The QuantiFERON was negative on 2026-09-20, within 6 months of the 2026-11-18 request. It is determinate and negative. (confidence 0.95)

- `PT-3504/labs-2026-09-20` (2026-09-20): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented, and both are nonreactive. No prophylaxis plan is needed. (confidence 0.96)

- `PT-3504/labs-2026-09-20` (2026-09-20): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3504/labs-2026-09-20` (2026-09-20): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The medication history lists no current biologic, JAK inhibitor or S1P modulator. Infliximab was stopped in 2026-09, so ustekinumab would not be combined with another agent. (confidence 0.93)

- `PT-3504/medication-history-2026-10-29` (2026-10-29): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3504/medication-history-2026-10-29` (2026-10-29): "| Infliximab | 5 mg/kg IV every 8 weeks | 2024-03 | 2026-09 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

The weight of 55.0 kg was recorded on 2026-10-31, within 90 days of the request. The 260 mg IV dose fits the tier of up to and including 55 kg. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the labeled regimen. (confidence 0.95)

- `PT-3504/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3504/gi-note-2026-10-31` (2026-10-31): "- Weight 55.0 kg."
- Code checks: weight 55.0 kg (2026-10-31) -> label tier 260 mg; requested 260 mg

## Run cost

2 model calls, 14,439 input and 4,833 output tokens, 28.4 s of model time, $0.091 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: borderline.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
