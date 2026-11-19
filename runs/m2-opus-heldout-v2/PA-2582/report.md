# PA-2582: ustekinumab-ttwe for PT-2582

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: URGENT review. Decision within 24 hours of receiving all required information (policy section E). Prescriber attestation of urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 86.1 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note of 2026-10-31 states the diagnosis of ulcerative pancolitis and says it is moderately to severely active. The problem list confirms a UC diagnosis dating from 2021. (confidence 0.95)

- `PT-2582/gi-note-2026-10-31` (2026-10-31): "- Moderately to severely active ulcerative pancolitis."
- `PT-2582/problem-list-2026-10-31` (2026-10-31): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2021."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is a flexible sigmoidoscopy dated 2025-05-18. That is about 18 months before the 2026-11-18 request, outside the 12-month window (which starts 2025-11-18). The recent CRP and partial Mayo score cannot replace endoscopy under this policy. (confidence 0.80)

- `PT-2582/flexible-sigmoidoscopy-2025-05-18` (2025-05-18): "- Rectum to 38 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-2582/labs-2026-10-18` (2026-10-18): "C REACTIVE PROTEIN ................ 40.4 mg/L  (<5.0)"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. A. Rivera, Gastroenterology. The ustekinumab plan appears in a GI follow-up note. The note author's specialty is not quoted directly in the passages, so the reviewer may want to confirm it. (confidence 0.85)

- `PT-2582/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 86.1 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 1970-11-22, the member is 55 years old on the request date of 2026-11-18. That meets the 18-or-older requirement. (confidence 0.97)

- `PT-2582/demographics-2026-08-26` (2026-08-26): "Date of birth: 1970-11-22"
- Code checks: age 55 on 2026-11-18 from DOB 1970-11-22

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history shows budesonide from 2022-10 to 2023-01, stopped for inadequate response. It also shows prednisone from 2021-12 to 2022-09 with steroid dependence. The request's expedited reason says 'on steroids' while the history says 'No steroids at present', but that does not change these past documented failures. (confidence 0.92)

- `PT-2582/medication-history-2026-10-29` (2026-10-29): "| Budesonide | 9 mg daily | 2022-10 | 2023-01 | Inadequate response after 10 weeks |"
- `PT-2582/medication-history-2026-10-29` (2026-10-29): "| Prednisone | 40 mg daily, tapered | 2021-12 | 2022-09 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab was used from 2023-07 to 2023-11 and stopped for primary non-response, which counts as inadequate response. Vedolizumab is also current, but no stop reason is stated for it, so it is not relied on here. (confidence 0.92)

- `PT-2582/medication-history-2026-10-29` (2026-10-29): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2023-11 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

A QuantiFERON TB Gold Plus (an IGRA) dated 2026-10-18 was negative. That is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-2582/labs-2026-10-18` (2026-10-18): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both hepatitis B surface antigen and total core antibody have results, and both are nonreactive. Because neither is reactive, no prophylaxis or monitoring plan is needed. (confidence 0.96)

- `PT-2582/labs-2026-10-18` (2026-10-18): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2582/labs-2026-10-18` (2026-10-18): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The member is switching from vedolizumab. The prescriber documents stopping it, with ustekinumab replacing the next scheduled infusion. No other biologic, JAK inhibitor or S1P modulator is documented. (confidence 0.90)

- `PT-2582/gi-note-2026-10-31` (2026-10-31): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-2582/medication-history-2026-10-29` (2026-10-29): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-19); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 86.1 kg on 2026-10-31 is within 90 days of the request and above 85 kg, so the 520 mg IV induction band applies. The requested maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the infusion, matches the label. The older 84.0 kg weight from 2026-02-12 is outside the 90-day window. (confidence 0.93)

- `PT-2582/gi-note-2026-10-31` (2026-10-31): "- Weight 86.1 kg."
- `PT-2582/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 86.1 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 86.1 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy) dated 2025-11-18 or later that documents active mucosal inflammation (who: ordering_provider)
  > Dr. Rivera, for PA-2582 (PT-2582, ustekinumab-ttwe), Calder policy B.2 needs an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from the past 12 months (on or after 2025-11-18) showing active mucosal inflammation. The only endoscopy in the chart is the flexible sigmoidoscopy dated 2025-05-18 (Mayo endoscopic subscore 3), which is outside that window. Under this policy, the 2026-10-18 CRP of 40.4 mg/L and the partial Mayo score cannot stand in for endoscopy. Please review: was a more recent endoscopy done, here or at another facility, that we can file? If not, how would you like to proceed?

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
