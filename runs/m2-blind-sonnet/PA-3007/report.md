# PA-3007: ustekinumab-ttwe for PT-3007

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 63.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note on 2026-11-05 states moderately to severely active Crohn's disease. It also gives a Harvey-Bradshaw Index of 9. (confidence 0.96)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Harvey-Bradshaw Index today: 9."

### C2 (policy 3.2): **INSUFFICIENT**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy described is from 12/2022, outside the 12-month window. CRP alone does not satisfy the criterion. No recent endoscopy report or fecal calprotectin is in the passages. (confidence 0.85)

- `PT-3007/gi-note-2026-05-13` (2026-05-13): "- Last colonoscopy 12/2022 showed active disease."
- `PT-3007/labs-2026-10-03` (2026-10-03): "C REACTIVE PROTEIN ................ 9.1 mg/L  (<5.0)"
- Missing: Endoscopy/colonoscopy/flexible sigmoidoscopy report dated within 12 months before 2026-11-18 describing active inflammation
- Missing: OR fecal calprotectin result with date and reference range, dated within 12 months

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No chart passage documents the prescriber's specialty or a gastroenterology consultation. The specialty appears only in the request form, not in a quoted chart document. (confidence 0.60)

- Missing: Chart documentation that the prescriber (Dr. S. Adeyemi) is a gastroenterologist, or a GI consultation note

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

Date of birth 08/01/1980 makes the member 46 at the request date, which is over 18. (confidence 0.97)

- `PT-3007/demographics-2026-05-23` (2026-05-23): "Date of birth: 08/01/1980"
- Code checks: age 46 on 2026-11-18 from DOB 1980-08-01

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Outside records name methotrexate, give start and stop dates, and state the reason stopped as intolerance. Methotrexate is a listed conventional therapy. No conflicting record appears in the passages. (confidence 0.80)

- `PT-3007/outside-records-2021-12-18` (2021-12-18): "- Methotrexate 25 mg subcutaneously weekly, 06/2021 to 11/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history documents adalimumab with start and stop dates and the reason stopped as primary non-response. Primary non-response qualifies under the policy. (confidence 0.85)

- `PT-3007/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

A negative QuantiFERON result is dated 2026-10-03, within 12 months of the request. (confidence 0.95)

- `PT-3007/labs-2026-10-03` (2026-10-03): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc results are on file and nonreactive, so no monitoring plan is needed. (confidence 0.96)

- `PT-3007/labs-2026-10-03` (2026-10-03): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3007/labs-2026-10-03` (2026-10-03): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-11-02 medication history states no current biologic, JAK inhibitor, or S1P modulator. The prior adalimumab was stopped in 11/2023. (confidence 0.90)

- `PT-3007/medication-history-2026-11-02` (2026-11-02): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight of 63.6 kg, documented 2026-11-05 (within 30 days), falls in the 390 mg band. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.95)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Weight 63.6 kg."
- Code checks: weight 63.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopic report showing active inflammation or fecal calprotectin result, dated within 12 months (who: lab)
  > PA-3007 (PT-3007), criterion C2 (objective evidence of active disease): the chart only has a colonoscopy from 12/2022 and a CRP of 9.1 mg/L on 2026-10-03, and neither satisfies the policy. Is there a fecal calprotectin result (with date and lab reference range) or an endoscopy, colonoscopy or sigmoidoscopy report dated on or after 2025-11-18 that we can file? If one exists, please send it. Whether to obtain new testing is the provider's decision.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy or flexible sigmoidoscopy report describing active inflammation (ulceration, erosions, friability), or a fecal calprotectin above the performing lab's reference range, dated on or after 2025-11-18. CRP or ESR alone and imaging alone do not satisfy it.
- **C3**: Chart documentation that Dr. S. Adeyemi is a gastroenterologist, or a GI consultation note (who: practice_staff)
  > PA-3007 (PT-3007), criterion C3 (gastroenterologist prescriber): the specialty of Dr. S. Adeyemi appears only on the request form, not in any chart document. Can you locate and attach a chart note, such as the 2026-05-13 GI note with a signature and specialty block, or a GI consultation note that documents the prescriber's gastroenterology specialty?
  - Would satisfy the policy: Policy 3.3 accepts chart documentation that the medication is prescribed by, or in consultation with, a gastroenterologist, such as a signed note showing the prescriber's gastroenterology specialty or a GI consultation note.

## Run cost

3 model calls, 20,030 input and 6,188 output tokens, 38.7 s of model time, $0.121 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
