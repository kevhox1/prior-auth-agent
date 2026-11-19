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

The GI note of 2026-11-05 states moderately to severely active ileocolonic Crohn's disease. This is the prescriber's statement in the clinical record. (confidence 0.96)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy on 2026-10-12, within 12 months of the request, shows direct visualization of terminal ileal ulcers with erythema and edema. This is active mucosal inflammation and does not rely on labs or imaging. (confidence 0.96)

- `PT-3593/colonoscopy-2026-10-12` (2026-10-12): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3593/colonoscopy-2026-10-12` (2026-10-12): "SES-CD: 14"

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No retrieved passage states the prescriber's specialty. The specialty appears only in the request form, not in a chart quote. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (gastroenterologist), such as a signed GI note identifying Dr. M. Chen as a gastroenterologist
- Missing: Documentation of consultation with a gastroenterologist if the prescriber is not one

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 1957-02-24 makes the member 69 on the request date of 2026-11-18. This is well over 18. (confidence 0.98)

- `PT-3593/demographics-2026-05-15` (2026-05-15): "Date of birth: 1957-02-24"
- Code checks: age 69 on 2026-11-18 from DOB 1957-02-24

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Infliximab was used from 2025-04 to 2026-07 and stopped for secondary loss of response. Methotrexate and azathioprine intolerance are also documented in the outside records. One qualifying therapy is enough. (confidence 0.95)

- `PT-3593/medication-history-2026-11-05` (2026-11-05): "| Infliximab | 5 mg/kg IV every 8 weeks | 2025-04 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 23 U/mL (reference <10) |"

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The IGRA on 2026-09-25 was positive and is within 6 months. The policy allows a positive screen if the chest radiograph shows no active disease and latent TB treatment has begun. The CXR on 2026-09-28 shows no active TB, and rifampin was started 2026-10-01. (confidence 0.90)

- `PT-3593/labs-2026-09-25` (2026-09-25): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-3593/chest-xray-2026-09-28` (2026-09-28): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Only a surface antibody result and a vaccination record are in the chart, and the policy says neither is sufficient. No HBsAg or total core antibody result was found. (confidence 0.93)

- `PT-3593/labs-2026-09-25` (2026-09-25): "Hepatitis B surface antibody          Reactive (immune)>10 mIU/mL"
- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The current biologic, vedolizumab, is documented as being discontinued when ustekinumab starts. The plan does not combine the two agents. (confidence 0.90)

- `PT-3593/medication-history-2026-11-05` (2026-11-05): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-24); to be discontinued when ustekinumab starts."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg was recorded on 2026-11-05, within 90 days of the request. It falls in the 260 mg tier (up to and including 55 kg). The maintenance dose is 90 mg SC every 8 weeks starting 8 weeks after the infusion, as labeled. (confidence 0.95)

- `PT-3593/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3593/gi-note-2026-11-05` (2026-11-05): "Weight 55.0 kg."
- Code checks: weight 55.0 kg (2026-11-05) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C3**: Chart documentation of prescriber's gastroenterology specialty (who: practice_staff)
  > For PA-3593 (PT-3593, ustekinumab-ttwe), criterion C3 (B.3) needs chart documentation that Dr. M. Chen is a gastroenterologist. Specialty currently appears only on the request form. Could you file a signed GI note or other chart document identifying Dr. Chen's specialty? If the prescriber is not a gastroenterologist, a documented GI consultation about this treatment would be needed instead.
  - Would satisfy the policy: Policy B.3 accepts chart documentation, such as a signed GI note, identifying the prescriber as a gastroenterologist, or documentation of a consultation with a gastroenterologist about this treatment.
- **C7**: HBsAg and total hepatitis B core antibody results (who: lab)
  > For PA-3593 (PT-3593), criterion C7 (B.7) needs both a hepatitis B surface antigen result and a total hepatitis B core antibody result. The chart (labs-2026-09-25) only has a surface antibody (reactive, immune) and a vaccination record, which the policy does not accept. Please locate existing results for these two tests, or have the provider decide whether to obtain them. Pending orders do not count.
  - Would satisfy the policy: Policy B.7 accepts resulted HBsAg and total hepatitis B core antibody tests of any date. If either is reactive, a documented plan for antiviral prophylaxis or monitoring is also required. Surface antibody results, vaccination records and pending orders are not sufficient.

## Run cost

3 model calls, 18,423 input and 5,657 output tokens, 34.4 s of model time, $0.109 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
