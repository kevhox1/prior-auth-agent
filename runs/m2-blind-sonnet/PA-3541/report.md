# PA-3541: ustekinumab-aekn for PT-3541

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note dated 2026-11-08 states moderately to severely active ileocolonic Crohn's disease. This is the prescriber's statement in the clinical record. (confidence 0.95)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy on 2026-08-17, within 12 months of the request, shows terminal ileal ulcers with erythema and edema. Biopsy also shows chronic active inflammation. The finding rests on direct visualization, not on lab markers. (confidence 0.95)

- `PT-3541/colonoscopy-2026-08-17` (2026-08-17): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3541/colonoscopy-2026-08-17` (2026-08-17): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No passage from the chart states the prescriber's specialty or documents a gastroenterology consultation. Notes are titled GI follow-up, but no passage names the author or their specialty. (confidence 0.70)

- Missing: Documentation of the prescriber's specialty (gastroenterology), such as a signed GI note or provider credentials
- Missing: Documentation of a gastroenterology consultation if the prescriber is not a gastroenterologist

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 07/12/2000 makes the member 26 on the request date of 2026-11-18. That is over 18. (confidence 0.97)

- `PT-3541/demographics-2026-11-01` (2026-11-01): "Date of birth: 07/12/2000"
- Code checks: age 26 on 2026-11-18 from DOB 2000-07-12

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Adalimumab was used 07/2023 to 11/2023 and stopped for primary non-response. Prednisone was used 05/2020 to 01/2021 with steroid dependence. Either one satisfies the step requirement, and the drug, dates and reason are recorded. (confidence 0.95)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"
- `PT-3541/medication-history-2026-11-04` (2026-11-04): "| Prednisone | 40 mg daily, tapered | 05/2020 | 01/2021 | Steroid dependent (flared each time the dose went below 15 mg) |"

### C6 (policy B.6): **NOT MET**
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The only TB screen in the passages is a negative QuantiFERON collected 2025-11-29. That is about 12 months before the 2026-11-18 request, outside the 6-month window. No more recent TB result is shown. (confidence 0.85)

- `PT-3541/labs-2025-11-29` (2025-11-29): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- `PT-3541/labs-2025-11-29` (2025-11-29): "COLLECTED: 11/29/2025      ORDERING: Dr. A. Rivera"
- Code checks: no cited evidence dated on or after 2026-05-18 (6-month lookback)

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented as nonreactive on 2026-09-19. Neither is reactive, so no prophylaxis plan is needed. (confidence 0.95)

- `PT-3541/labs-2026-09-19` (2026-09-19): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3541/labs-2026-09-19` (2026-09-19): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The medication history states there is no current biologic, JAK inhibitor or S1P modulator. The other current medications listed, prednisone and ferrous sulfate, are not in the excluded classes. (confidence 0.90)

- `PT-3541/medication-history-2026-11-04` (2026-11-04): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

Weight of 55.0 kg was recorded on 2026-11-08, within 90 days of the request. The 55 kg weight falls in the 260 mg tier, and the maintenance of 90 mg SC every 8 weeks starting 8 weeks after the infusion matches the policy. (confidence 0.93)

- `PT-3541/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3541/gi-note-2026-11-08` (2026-11-08): "- Weight 55.0 kg."
- Code checks: weight 55.0 kg (2026-11-08) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C3**: Prescriber specialty documentation or GI consult note (who: practice_staff)
  > For PA-3541 (criterion C3, policy B.3), the chart does not state Dr. A. Rivera's specialty or document a GI consultation. Please attach a signed GI note showing the author and specialty, or the provider credentials. If the prescriber is not a gastroenterologist, please attach documentation of a GI consultation about this treatment.
  - Would satisfy the policy: Policy B.3 accepts documentation that the prescriber is a gastroenterologist (e.g., a signed GI note or provider credentials), or documentation that the prescriber consulted a gastroenterologist about this treatment.
- **C6**: TB screen (IGRA or TST) negative result dated within 6 months (who: ordering_provider)
  > For PA-3541 (criterion C6, policy B.6), the only TB screen on file is the negative QuantiFERON collected 2025-11-29 (labs-2025-11-29). This is about 12 months before the 2026-11-18 request and outside the 6-month window. Please review and advise whether a more recent TB screen result exists or will be documented.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result is not negative. A positive screen qualifies only with a chest radiograph showing no active disease and documentation that latent TB treatment has begun.

## Run cost

3 model calls, 17,393 input and 5,250 output tokens, 34.0 s of model time, $0.101 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
