# PA-3507: ustekinumab-ttwe for PT-3507

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 63.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The 11/05/2026 GI note, which is the prescriber's assessment, states moderately to severely active ileocolonic Crohn's disease. The Harvey-Bradshaw Index of 9 is consistent with that assessment, and no passage contradicts it. (confidence 0.93)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3507/gi-note-2026-11-05` (2026-11-05): "Harvey-Bradshaw Index today: 9."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

The only endoscopy documented in the passages is a colonoscopy from 12/2022, which is outside the 12-month window. The 2021 diagnostic colonoscopy and the CRP lab do not qualify, and no endoscopy from the lookback period appears in the chart; a more recent procedure may exist but is not in the record provided. (confidence 0.70)

- `PT-3507/gi-note-2026-05-13` (2026-05-13): "- Last colonoscopy 12/2022 showed active disease."
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated within 12 months before 2026-11-18 (on or after 2025-11-18) documenting active mucosal inflammation

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The 11/05/2026 GI note is authored by Dr. S. Adeyemi and the request lists the provider as Gastroenterology, but the quoted passage does not itself state the prescriber's specialty. A chart passage showing the specialty or a GI consultation is needed before this can be marked met. (confidence 0.60)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "#IBD follow-up (Crohn's disease)"
- Missing: Signed note header, credential line, or provider record showing Dr. S. Adeyemi's specialty as gastroenterology (or a documented gastroenterology consultation about ustekinumab)

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 08/01/1980 gives an age of 46 on the 2026-11-18 request date, which meets the 18-or-older requirement. The outside records show the same date of birth. (confidence 0.97)

- `PT-3507/demographics-2026-05-23` (2026-05-23): "Date of birth: 08/01/1980"
- Code checks: age 46 on 2026-11-18 from DOB 1980-08-01

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The outside records list methotrexate, a listed conventional agent, used from 06/2021 to 11/2021 and stopped for intolerance. The record gives the drug, the approximate dates, and the reason stopped. The record does not state the indication, but the Crohn's diagnosis from 05/2021 precedes it, so it fits the requirement. (confidence 0.85)

- `PT-3507/outside-records-2021-12-18` (2021-12-18): "Methotrexate 25 mg subcutaneously weekly, 06/2021 to 11/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The medication history shows adalimumab, a TNF-blocker biologic, used from 07/2023 to 11/2023 and stopped for primary non-response. This satisfies the biologic step-therapy item, and the record gives dates and reason. (confidence 0.93)

- `PT-3507/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

The QuantiFERON-TB Gold Plus result is negative and was collected on 10/03/2026. That is within 6 months of the 11/18/2026 request, so no latent-infection pathway is needed. (confidence 0.93)

- `PT-3507/labs-2026-10-03` (2026-10-03): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both required hepatitis B results are on file from 10/03/2026: HBsAg is nonreactive and total core antibody is nonreactive. Because neither result is reactive, no antiviral prophylaxis plan is required. (confidence 0.94)

- `PT-3507/labs-2026-10-03` (2026-10-03): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3507/labs-2026-10-03` (2026-10-03): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The reconciled medication list from 11/02/2026 states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The only prior biologic, adalimumab, was stopped in 11/2023, so this is not a switch or a concurrent use. (confidence 0.92)

- `PT-3507/medication-history-2026-11-02` (2026-11-02): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 63.6 kg was recorded on 11/05/2026, within 90 days of the request. That weight falls in the 390 mg band (above 55 kg up to 85 kg), and the requested 390 mg IV induction with 90 mg SC every 8 weeks starting 8 weeks later matches the labeled regimen. (confidence 0.92)

- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Weight 63.6 kg."
- `PT-3507/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 63.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 documenting active mucosal inflammation (who: practice_staff)
  > PA-3507 (ustekinumab), criterion C2 (B.2): the chart has only a colonoscopy from 12/2022, which is outside the 12-month window. Please search the chart and any outside GI or hospital records for an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Labs (CRP, calprotectin) and imaging do not satisfy this criterion. Dr. Adeyemi should be notified of the result either way.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy dated on or after 2025-11-18 (within 12 months before the 2026-11-18 request date) that documents active mucosal inflammation. Fecal calprotectin, CRP, sedimentation rate, and cross-sectional imaging do not count on their own.
- **C3**: Signed note header, credential line, or provider record showing Dr. S. Adeyemi's specialty as gastroenterology, or a documented gastroenterology consultation about ustekinumab (who: practice_staff)
  > PA-3507 (ustekinumab), criterion C3 (B.3): the 11/05/2026 GI note by Dr. S. Adeyemi quotes only "#IBD follow-up (Crohn's disease)" and does not state the prescriber's specialty. Please pull the signed note header, credential line, or provider directory record showing Dr. Adeyemi is a gastroenterologist. If a gastroenterology consultation about ustekinumab exists instead, please attach that as well.
  - Would satisfy the policy: Policy B.3 accepts a signed note header, credential line, or provider record showing the prescriber is a gastroenterologist, or documentation that the prescriber consulted with a gastroenterologist about this treatment. The policy text does not set a date window for this item.

## Run cost

3 model calls, 19,074 input and 11,416 output tokens, 49.3 s of model time, $0.009 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
