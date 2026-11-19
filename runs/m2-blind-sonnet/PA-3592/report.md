# PA-3592: ustekinumab-ttwe for PT-3592

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

The GI note dated 2026-10-30 states moderately to severely active Crohn's disease. Nothing in the passages contradicts this. (confidence 0.95)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only activity evidence is fecal calprotectin and CRP, which the policy says do not satisfy this criterion alone. No endoscopy report within 12 months appears in the passages. (confidence 0.90)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "His calprotectin from 08/23/2026 came back at 1306 ug/g (lab reference <50)."
- `PT-3592/labs-2026-09-21` (2026-09-21): "CRP | 24.1 mg/L | H | <5.0"
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report within the past 12 months documenting active mucosal inflammation

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No passage in the chart states the prescriber's specialty or documents a gastroenterology consultation. The specialty appears only in the request form, not in a chart passage. (confidence 0.70)

- Missing: Chart documentation of the prescriber's specialty (gastroenterology) or of a consultation with a gastroenterologist

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 05/12/1990 makes the member 36 on the request date of 2026-11-18, which is over 18. (confidence 0.97)

- `PT-3592/demographics-2025-10-15` (2025-10-15): "Date of birth: 05/12/1990"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-12

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Budesonide, a conventional agent, was used 09/2022 to 12/2022 and stopped for inadequate response. This identifies the drug, dates and reason, so one prior therapy is shown. (confidence 0.93)

- `PT-3592/medication-history-2026-10-28` (2026-10-28): "| Budesonide | 9 mg daily | 09/2022 | 12/2022 | Inadequate response after 10 weeks |"

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

No IGRA or TST result appears in the passages. A negative result within 6 months of 2026-11-18 is required. (confidence 0.92)

- Missing: IGRA or TST result dated within the past 6 months

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented as nonreactive. No reactive result means no prophylaxis plan is needed. (confidence 0.95)

- `PT-3592/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3592/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The member is switching from vedolizumab, and two notes document that it will be stopped when ustekinumab starts. No other biologic, JAK inhibitor or S1P modulator is listed. (confidence 0.90)

- `PT-3592/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/16/2026); to be discontinued when ustekinumab starts."
- `PT-3592/gi-note-2026-10-30` (2026-10-30): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 55.0 kg recorded 2026-10-30 is within 90 days of the request. The 260 mg IV dose fits the up-to-55 kg tier, and the maintenance of 90 mg SC every 8 weeks matches the label. (confidence 0.93)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Weight 55.0 kg."
- Code checks: weight 55.0 kg (2026-10-30) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C2**: Endoscopy report within 12 months showing active mucosal inflammation (who: practice_staff)
  > PA-3592 (PT-3592), criterion C2 (B.2): the chart only has fecal calprotectin (1306 ug/g, 08/23/2026) and CRP (24.1 mg/L, 2026-09-21), which the policy does not accept alone. Can you locate and file any ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report from the past 12 months that documents active mucosal inflammation? If one exists at another facility, please let us know where.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation. Labs and cross-sectional imaging do not satisfy it.
- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consultation (who: practice_staff)
  > PA-3592 (PT-3592), criterion C3 (B.3): the specialty of Dr. M. Chen (Gastroenterology) appears only on the request form, not in a chart document. Can you file a chart note, signature block, or provider credential that shows the prescriber is a gastroenterologist, or a note documenting a GI consultation about this treatment?
  - Would satisfy the policy: Policy B.3 accepts chart documentation that the prescriber is a gastroenterologist, or documentation that the prescriber consulted a gastroenterologist about this treatment.
- **C6**: Negative IGRA or TST result within the past 6 months (who: lab)
  > PA-3592 (PT-3592), criterion C6 (B.6): we found no IGRA or TST result in the chart. Is there a tuberculosis screening result dated on or after 2026-05-18 that we can file or request from the lab or an outside provider? If none exists, please review how you want to proceed.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. Indeterminate or borderline results do not count as negative. A positive screen qualifies only with a chest radiograph showing no active disease and documentation that latent TB treatment has begun.

## Run cost

3 model calls, 17,195 input and 5,271 output tokens, 33.5 s of model time, $0.100 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
