# PA-3545: ustekinumab-aekn for PT-3545

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

The 2026-11-06 GI follow-up note states the disease is moderately to severely active, which meets the prescriber-statement requirement. The note also records a Harvey-Bradshaw Index of 9, which supports that severity. (confidence 0.85)

- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy in the chart is the colonoscopy dated 2025-04-18, which falls outside the 12-month lookback from the 2026-11-18 request date (window starts 2025-11-18). Although that colonoscopy showed active inflammation, it is too old to satisfy this criterion. (confidence 0.80)

- `PT-3545/colonoscopy-2025-04-18` (2025-04-18): "INDICATION: Crohn's disease, assessment of disease activity"
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The chart shows Dr. S. Adeyemi as the ordering and GI follow-up provider, but no quoted passage states Dr. Adeyemi's specialty as gastroenterology. The gastroenterology specialty appears only in the request header, which is not chart evidence. (confidence 0.50)

- `PT-3545/labs-2026-10-03` (2026-10-03): "COLLECTED: 10/03/2026      ORDERING: Dr. S. Adeyemi"
- Missing: Documented specialty of Dr. S. Adeyemi as gastroenterology in the chart (for example, provider credentials or signature block)
- Missing: Or documentation of a consultation with a gastroenterologist about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

A date of birth of 02/21/1966 makes the member 60 years old on the 2026-11-18 request date. This satisfies the age of 18 or older requirement. (confidence 0.97)

- `PT-3545/demographics-2026-04-15` (2026-04-15): "Date of birth: 02/21/1966"
- Code checks: age 60 on 2026-11-18 from DOB 1966-02-21

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Mercaptopurine, a listed conventional agent, was used from 04/2023 to 10/2023 and stopped for inadequate response. The record gives the drug, the approximate dates, and the reason stopped. (confidence 0.90)

- `PT-3545/outside-records-2023-11-18` (2023-11-18): "Mercaptopurine 1.5 mg/kg daily, 04/2023 to 10/2023. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

Adalimumab, a biologic TNF blocker, was used from 12/2023 to 05/2026 and stopped for intolerance. The record gives the drug, the dates, and the reason stopped. (confidence 0.90)

- `PT-3545/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON-TB Gold Plus collected 2026-10-03 is reported as negative. That date is within the 6-month lookback from 2026-11-18. The 2023 QuantiFERON mentioned in the note is outside the window and is not relied on. (confidence 0.92)

- `PT-3545/labs-2026-10-03` (2026-10-03): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total hepatitis B core antibody are reported as nonreactive on 2026-10-03. Both required results are documented, and no reactive result requires a prophylaxis plan. (confidence 0.92)

- `PT-3545/labs-2026-10-03` (2026-10-03): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3545/labs-2026-10-03` (2026-10-03): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 2026-11-04 medication reconciliation states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The prior adalimumab was stopped in 05/2026, so the member is not on a concurrent excluded agent. (confidence 0.88)

- `PT-3545/medication-history-2026-11-04` (2026-11-04): "No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg recorded 2026-11-06 is within 90 days of the request and falls in the 260 mg band (up to and including 55 kg). The requested 260 mg IV induction followed by 90 mg SC every 8 weeks starting 8 weeks later matches the labeled regimen. (confidence 0.90)

- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Weight 55.0 kg."
- `PT-3545/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-06) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C2**: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 documenting active mucosal inflammation (who: ordering_provider)
  > Criterion B.2 (endoscopic confirmation of disease activity) is not met for PA-3545. The only endoscopy in the chart is the colonoscopy dated 2025-04-18, which falls outside the 12-month lookback from the 2026-11-18 request date. Please review this criterion and document whether a qualifying endoscopy exists or is planned.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 that documents active mucosal inflammation. Laboratory markers and cross-sectional imaging do not satisfy this criterion on their own.
- **C3**: Chart documentation of Dr. S. Adeyemi's gastroenterology specialty (credentials or signature block), or a documented consultation with a gastroenterologist about ustekinumab (who: practice_staff)
  > Criterion B.3 (prescriber specialty) is unverified for PA-3545. The cited chart item, labs dated 10/03/2026, lists Dr. S. Adeyemi as ordering provider but does not state a specialty, and gastroenterology appears only in the request header. Please locate a chart document showing Dr. Adeyemi's gastroenterology credentials or signature block, or a note documenting a consultation with a gastroenterologist about ustekinumab, and add it to the file.
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist (such as provider credentials or a signature block), or documentation that the prescriber consulted with a gastroenterologist about this treatment. The policy text provided sets no date window for this criterion.

## Run cost

3 model calls, 29,240 input and 17,863 output tokens, 72.2 s of model time, $0.013 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
