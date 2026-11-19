# PA-3092: ustekinumab-ttwe for PT-3092

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses moderately to severely active Crohn's disease. It supports severity with a Harvey-Bradshaw Index of 13 and a description of symptom burden. (confidence 0.97)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The GI note gives a fecal calprotectin result dated 08/23/2026, within 12 months of the request. The value of 1306 ug/g is well above the stated lab reference of <50. The original lab report is not among the passages, so the reviewer may want to confirm it. (confidence 0.80)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "His calprotectin from 08/23/2026 came back at 1306 ug/g (lab reference <50)."

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No chart passage shows the prescriber's specialty or a gastroenterology consultation. The specialty appears only in the request form, not in a chart quote. (confidence 0.60)

- Missing: Chart documentation (note signature or credentials) showing Dr. M. Chen is a gastroenterologist, or a gastroenterology consultation

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 05/12/1990 makes the member 36 years old at the request date, which is over 18. (confidence 0.98)

- `PT-3092/demographics-2025-10-15` (2025-10-15): "Date of birth: 05/12/1990"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-12

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history names budesonide, which counts as a corticosteroid. It gives start and stop dates (09/2022 to 12/2022) and the reason stopped (inadequate response). (confidence 0.90)

- `PT-3092/medication-history-2026-10-28` (2026-10-28): "| Budesonide | 9 mg daily | 09/2022 | 12/2022 | Inadequate response after 10 weeks |"

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The GI note specifically documents a contraindication to anti-TNF therapy because of demyelinating disease. The problem list confirms the multiple sclerosis diagnosis. (confidence 0.88)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3092/problem-list-2026-10-30` (2026-10-30): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy 3.6): **INSUFFICIENT**
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

No tuberculosis screening result appears in the passages. (confidence 0.90)

- Missing: Resulted IGRA or TST with date within 12 months before 2026-11-18 and a negative result

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive. Neither is positive, so no monitoring plan is needed. (confidence 0.96)

- `PT-3092/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3092/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member currently takes vedolizumab, a biologic. Two documents state it will be stopped when ustekinumab starts, which meets the switching requirement. (confidence 0.85)

- `PT-3092/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/16/2026); to be discontinued when ustekinumab starts."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight of 55.0 kg was recorded 19 days before the request, inside the 30-day window. The 260 mg IV dose matches the 55 kg or less band. Maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the label. (confidence 0.93)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Weight 55.0 kg."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-30) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names a specific product, ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.96)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C3**: Chart document showing Dr. Chen is a gastroenterologist, or a GI consultation note (who: practice_staff)
  > PA-3092 (criterion C3, policy 3.3): the chart has no passage showing Dr. M. Chen's specialty. Specialty appears only on the request form. Could you attach a signed note with credentials showing Dr. Chen is a gastroenterologist, or a gastroenterology consultation note?
  - Would satisfy the policy: Policy 3.3 accepts chart documentation (e.g., a note signature or credentials) showing the prescriber is a gastroenterologist, or documentation of a consultation with a gastroenterologist.
- **C6**: Resulted negative IGRA or TST dated within 12 months before request (who: ordering_provider)
  > PA-3092 (criterion C6, policy 3.6): no tuberculosis screening result is in the chart. Please check whether a resulted IGRA or TST dated on or after 2025-11-18 exists, and if so send the report. If none exists, please review and advise how you would like to proceed.
  - Would satisfy the policy: Policy 3.6 accepts a negative IGRA or TST, resulted and dated on or after 2025-11-18. An indeterminate IGRA is not negative, and an ordered but unresulted test does not count. If the screen is positive, the policy requires documentation that chest imaging excluded active TB and that latent TB treatment has started.

## Run cost

3 model calls, 19,520 input and 5,720 output tokens, 36.0 s of model time, $0.114 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
