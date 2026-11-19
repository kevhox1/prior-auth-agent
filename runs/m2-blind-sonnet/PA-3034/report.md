# PA-3034: ustekinumab-aekn for PT-3034

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: EXPEDITED review. Pharmacy-benefit phase: decision within 24 hours of a complete request (policy section 7). Prescriber statement of clinical urgency is required. Work this case first.
- Ordered dose: 390 mg IV once (weight 66.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses moderately to severely active Crohn's disease. It also gives a Harvey-Bradshaw Index of 13. (confidence 0.96)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): **NOT MET**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy showing active inflammation is dated 2025-04-18, which is outside the 12 months before 2026-11-18. The only recent result is an elevated CRP, which the policy says does not satisfy this criterion. No fecal calprotectin is on file. (confidence 0.80)

- `PT-3034/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3034/labs-2026-10-21` (2026-10-21): "C-reactive protein                    22.0 mg/L     <5.0"

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No chart passage documents the prescriber's specialty or a gastroenterology consultation. The request lists Gastroenterology, but the chart passages supplied do not confirm it. (confidence 0.70)

- Missing: Documentation of the prescriber's specialty (gastroenterology) or a gastroenterology consultation note

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 03/19/1992 makes the member 34 years old at the request date, so an adult. (confidence 0.98)

- `PT-3034/demographics-2026-04-29` (2026-04-29): "Date of birth: 03/19/1992"
- Code checks: age 34 on 2026-11-18 from DOB 1992-03-19

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history names budesonide, which counts as a corticosteroid, with start and stop dates. It states the reason stopped as inadequate response. (confidence 0.88)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "Budesonide 9 mg daily, 05/2019 to 08/2019. Reason stopped: inadequate response after 10 weeks."

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

Infliximab is documented with start and stop dates. The reason stopped is secondary loss of response, supported by a low trough and antibodies. (confidence 0.90)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

A negative QuantiFERON result dated 2026-10-21 falls within 12 months before the request. (confidence 0.95)

- `PT-3034/labs-2026-10-21` (2026-10-21): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted and nonreactive. No monitoring plan is needed because neither is positive. (confidence 0.95)

- `PT-3034/labs-2026-10-21` (2026-10-21): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3034/labs-2026-10-21` (2026-10-21): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication list shows no biologic, JAK inhibitor, or S1P modulator. Infliximab was stopped in 07/2026. (confidence 0.88)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 66.2 kg was recorded 9 days before the request and falls in the 390 mg band. The maintenance dose is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as the label requires. (confidence 0.93)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Weight 66.2 kg."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.2 kg (2026-11-09) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-aekn, which is a preferred product. No exception is needed. (confidence 0.95)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Objective inflammation evidence dated on or after 2025-11-18 (endoscopy report or fecal calprotectin) (who: ordering_provider)
  > PA-3034 (PT-3034), criterion C2 (policy 3.2): the only endoscopy showing active inflammation is the colonoscopy of 2025-04-18, which falls outside the 12-month window. The 2026-10-21 labs show CRP 22.0 mg/L, which the policy does not accept alone, and no fecal calprotectin is on file. Please review and add any qualifying endoscopy report or fecal calprotectin result dated on or after 2025-11-18 if one exists.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy or flexible sigmoidoscopy report describing active inflammation, or a fecal calprotectin above the performing lab's reference range, dated on or after 2025-11-18. CRP, ESR or imaging alone do not satisfy it.
- **C3**: Documentation that the prescriber is a gastroenterologist, or a GI consultation note (who: practice_staff)
  > PA-3034 (PT-3034), criterion C3 (policy 3.3): the request lists Dr. S. Adeyemi, Gastroenterology, but no chart document confirms the specialty. Could you attach a document showing Dr. Adeyemi's gastroenterology specialty, such as a signed GI clinic note or provider credentials, or a GI consultation note?
  - Would satisfy the policy: Policy 3.3 accepts documentation that the medication is prescribed by, or in consultation with, a gastroenterologist, such as a note showing the prescriber's GI specialty or a GI consultation note.

## Run cost

3 model calls, 19,964 input and 5,534 output tokens, 34.8 s of model time, $0.114 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
