# PA-3580: ustekinumab-aekn for PT-3580

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: URGENT review. Decision within 24 hours of receiving all required information (policy section E). Prescriber attestation of urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 104.9 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note dated 2026-10-26 states moderately to severely active ulcerative pancolitis. This is the prescriber's statement in the clinical record. (confidence 0.96)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): **NOT MET**
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy in the chart is the 2023-07-18 sigmoidoscopy, which is well outside the 12-month window before 2026-11-18. Fecal calprotectin and CRP are lab markers and do not satisfy the policy on their own. (confidence 0.85)

- `PT-3580/flexible-sigmoidoscopy-2023-07-18` (2023-07-18): "Rectum to 31 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-3580/labs-2026-09-10` (2026-09-10): "CALPROTECTIN FECAL ................ 64 ug/g  (<50)"

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No passage from the chart documents the prescriber's specialty or a gastroenterology consultation. The request lists Gastroenterology, but no chart document supports it in the passages provided. (confidence 0.70)

- Missing: Chart documentation of the ordering prescriber's specialty (gastroenterology), or a gastroenterologist consultation note

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth is 2000-10-17, so the member is 26 on the request date of 2026-11-18. This is over 18. (confidence 0.98)

- `PT-3580/demographics-2025-11-27` (2025-11-27): "Date of birth: 2000-10-17"
- Code checks: age 26 on 2026-11-18 from DOB 2000-10-17

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Adalimumab was used from 2023-07 to 2026-05 and stopped for intolerance (drug-induced lupus). This identifies the drug, the dates and the reason stopped, which satisfies option (b). (confidence 0.96)

- `PT-3580/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON dated 2026-09-10 falls within 6 months of the 2026-11-18 request. The 2023 screen is older but is not needed. (confidence 0.95)

- `PT-3580/labs-2026-09-10` (2026-09-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented and nonreactive. No prophylaxis plan is required because neither is reactive. (confidence 0.96)

- `PT-3580/labs-2026-09-10` (2026-09-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3580/labs-2026-09-10` (2026-09-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The current medication history lists no biologic, JAK inhibitor or S1P modulator. Ustekinumab would therefore not be combined with another advanced therapy, and adalimumab was already stopped in 2026-05. (confidence 0.93)

- `PT-3580/medication-history-2026-10-24` (2026-10-24): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

Weight is 104.9 kg, above 85 kg, so the 520 mg IV induction is the correct tier. The maintenance dose of 90 mg SC every 8 weeks matches the label. The weight was recorded 2026-10-26, within 90 days of the request. (confidence 0.95)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Weight 104.9 kg."
- Code checks: weight 104.9 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report within 12 months showing active mucosal inflammation (who: ordering_provider)
  > PA-3580 (criterion C2, policy B.2): the only endoscopy on file is the flexible sigmoidoscopy dated 2023-07-18, which is outside the 12-month window. The 2026-09-10 fecal calprotectin (64 ug/g) is a lab marker and does not satisfy B.2 alone. Please review and advise whether a more recent ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report exists or is to be documented.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation. Lab markers and cross-sectional imaging do not qualify.
- **C3**: Documentation of prescriber's gastroenterology specialty or GI consult note (who: practice_staff)
  > PA-3580 (criterion C3, policy B.3): the request lists Dr. S. Adeyemi as Gastroenterology, but no chart document confirms this. Could you file the prescriber's specialty documentation (e.g., credentials/provider profile or a signed note under the GI department), or a gastroenterologist consultation note for this treatment?
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment.

## Run cost

3 model calls, 17,450 input and 5,130 output tokens, 33.1 s of model time, $0.100 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | MET | - | FALSE MET |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
