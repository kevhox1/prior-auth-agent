# PA-3591: ustekinumab-ttwe for PT-3591

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 87.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note dated 2026-10-31 states moderately to severely active ileocolonic Crohn's disease. This is the prescriber's statement in the clinical record. (confidence 0.96)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The colonoscopy on 2026-08-29 is within 12 months of the 2026-11-18 request. It shows ulcers with erythema and edema in the terminal ileum, and pathology shows chronic active inflammation. (confidence 0.96)

- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3591/colonoscopy-2026-08-29` (2026-08-29): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No passage states the prescriber's specialty or documents a gastroenterology consultation. The passages show only that GI follow-up notes exist, with no quoted specialty. (confidence 0.70)

- Missing: Documentation of the prescriber's specialty (gastroenterology) or of a consultation with a gastroenterologist

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 1973-05-02 makes the member 53 on the request date 2026-11-18, which is over 18. (confidence 0.98)

- `PT-3591/demographics-2026-02-06` (2026-02-06): "Date of birth: 1973-05-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-05-02

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Methotrexate, a conventional agent, was used 2024-05 to 2024-12 and stopped for intolerance. Infliximab was also stopped for intolerance. Either one satisfies the criterion. (confidence 0.95)

- `PT-3591/outside-records-2025-01-18` (2025-01-18): "Methotrexate 25 mg subcutaneously weekly, 2024-05 to 2024-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3591/medication-history-2026-10-28` (2026-10-28): "Infliximab 5 mg/kg IV every 8 weeks, 2025-02 to 2026-07. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON was resulted 2026-10-08, within 6 months of the request date. No contradicting result is in the passages. (confidence 0.93)

- `PT-3591/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): **INSUFFICIENT**
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

The passages contain no HBsAg result and no total hepatitis B core antibody result. The only liver-related lab is an ALT, which does not document hepatitis B status. (confidence 0.92)

- Missing: HBsAg result
- Missing: Total hepatitis B core antibody result

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The current biologic, vedolizumab, is documented as being discontinued when ustekinumab starts. The GI plan says to stop vedolizumab, so the two will not be combined. (confidence 0.90)

- `PT-3591/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-09); to be discontinued when ustekinumab starts."
- `PT-3591/gi-note-2026-10-31` (2026-10-31): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

The weight of 87.0 kg, recorded 2026-10-31, is within 90 days of the request and falls in the above-85 kg tier, which calls for 520 mg IV. The maintenance dose of 90 mg SC every 8 weeks starting 8 weeks after the infusion matches the label. (confidence 0.94)

- `PT-3591/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3591/gi-note-2026-10-31` (2026-10-31): "Weight 87.0 kg."
- Code checks: weight 87.0 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C3**: Prescriber specialty documentation or GI consultation note (who: practice_staff)
  > For PA-3591 (ustekinumab-ttwe), criterion B.3 requires that the prescriber is a gastroenterologist or has consulted one. The chart shows GI follow-up notes but no documented specialty. Please attach documentation of Dr. Adeyemi's gastroenterology specialty (e.g., credentials or a signed note listing the specialty), or a GI consultation note.
  - Would satisfy the policy: Policy B.3 accepts documentation that the prescriber is a gastroenterologist, or documentation of a consultation with a gastroenterologist about this treatment.
- **C7**: HBsAg and total hepatitis B core antibody results (who: practice_staff)
  > For PA-3591, criterion B.7 requires documented results for both HBsAg and total hepatitis B core antibody. The chart has neither; only an ALT is present. Please locate and file any existing results (any date), or if none exist, ask Dr. Adeyemi to review whether to obtain them. Surface antibody, vaccination records and pending orders are not accepted.
  - Would satisfy the policy: Policy B.7 accepts resulted HBsAg and total hepatitis B core antibody tests of any date. If either is reactive, a documented plan for antiviral prophylaxis or monitoring is also required. Surface antibody, vaccination records and pending orders are not sufficient.

## Run cost

3 model calls, 17,483 input and 5,054 output tokens, 31.9 s of model time, $0.099 at list price (0 served from cache).

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
