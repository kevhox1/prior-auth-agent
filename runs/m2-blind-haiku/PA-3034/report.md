# PA-3034: ustekinumab-aekn for PT-3034

**Outcome: GAPS_TO_CLOSE**

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

The treating GI provider's note of 2026-11-09 documents moderately to severely active ileocolonic Crohn's disease. The same note gives a Harvey-Bradshaw Index of 13, a validated activity score. (confidence 0.93)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): **INSUFFICIENT**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy with active inflammation (colonoscopy 2025-04-18) falls outside the 12-month lookback. The 2026-10-21 CRP alone does not satisfy this criterion, and no fecal calprotectin is on file. (confidence 0.80)

- `PT-3034/colonoscopy-2025-04-18` (2025-04-18): "Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 describing active inflammation
- Missing: Fecal calprotectin result dated within 12 months before 2026-11-18 above the performing laboratory's upper reference limit
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The gastroenterology follow-up note of 2026-11-09 orders ustekinumab-aekn and directs submission of this prior authorization. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "Submit prior authorization to Northfield."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth 03/19/1992 makes the member 34 years old on the 2026-11-18 request date, which meets the 18-or-older requirement. (confidence 0.97)

- `PT-3034/demographics-2026-04-29` (2026-04-29): "Date of birth: 03/19/1992"
- Code checks: age 34 on 2026-11-18 from DOB 1992-03-19

### C5 (policy 3.5): **INSUFFICIENT**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history records budesonide (a corticosteroid) from 05/2019 to 08/2019, stopped for inadequate response, which meets the clinical content. The chart contains no claims or prescription records supporting that 2019 course, so the required supporting documentation is missing. (confidence 0.60)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "Budesonide 9 mg daily, 05/2019 to 08/2019. Reason stopped: inadequate response after 10 weeks."
- Missing: Pharmacy or claims record, or prescription record, for budesonide 9 mg daily 05/2019 to 08/2019
- Missing: Or prescriber attestation of the budesonide history, since the chart holds no supporting record

**C5b (policy 3.5(b)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history documents infliximab from 07/2023 to 07/2026, stopped for secondary loss of response with a low trough and high antibodies. This clinical content meets the anti-TNF requirement, but the chart holds no pharmacy or claims record supporting the trial. (confidence 0.60)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."
- Missing: Pharmacy or claims record, or prescription record, for infliximab 07/2023 to 07/2026
- Missing: Or prescriber attestation of the infliximab history, since the chart holds no supporting record

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus result of NEGATIVE is dated 2026-10-21, within 12 months before the request. The result is determinate, not indeterminate. (confidence 0.93)

- `PT-3034/labs-2026-10-21` (2026-10-21): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-10-21. Neither result is positive, so no monitoring or prophylaxis plan is required, and the criterion has no lookback limit. (confidence 0.93)

- `PT-3034/labs-2026-10-21` (2026-10-21): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3034/labs-2026-10-21` (2026-10-21): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The reconciled medication history of 2026-11-08 states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The prior infliximab course is documented as ended in 07/2026. (confidence 0.90)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 66.2 kg is documented on 2026-11-09, within 30 days of the request, and falls in the 390 mg band (more than 55 kg up to 85 kg). The requested maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the labeling. (confidence 0.90)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "Weight 66.2 kg."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.2 kg (2026-11-09) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The requested product is ustekinumab-aekn, a preferred product, and the chart contains no prior ustekinumab trial of either product. Nothing in the passages documents inadequate response or intolerance to both preferred products. (confidence 0.75)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to any inactive ingredient. The chart is silent on this point, so the criterion cannot be confirmed from the record. (confidence 0.75)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C2**: Endoscopy report dated on or after 2025-11-18 describing active inflammation, or fecal calprotectin above the lab's upper reference limit (who: ordering_provider)
  > Dr. Adeyemi, criterion C2 (Policy 3.2) is not met for PT-3034. The only endoscopy showing active inflammation is the colonoscopy dated 2025-04-18, which is outside the 12-month lookback, and the 2026-10-21 CRP does not count on its own. Please review; the policy accepts a report dated on or after 2025-11-18 describing active inflammation, or a fecal calprotectin dated on or after 2025-11-18 above the lab's upper reference limit.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that describes active inflammation (ulceration, erosions, or friability), or a fecal calprotectin result dated on or after 2025-11-18 above the performing laboratory's upper reference limit. CRP, ESR, and imaging alone do not qualify.
- **C5a**: Pharmacy or claims record, or prescription record, for budesonide 9 mg daily, 05/2019 to 08/2019 (who: pharmacy)
  > Criterion C5a (Policy 3.5(a)) needs support for the budesonide course in the medication history dated 2026-11-08: budesonide 9 mg daily, 05/2019 to 08/2019, stopped for inadequate response. Please request the pharmacy or claims history covering that period from the dispensing pharmacy or payer. If no record exists, Dr. Adeyemi can provide a prescriber attestation of the course.
  - Would satisfy the policy: Policy 3.5(a) accepts a pharmacy or claims record, or prescription record, showing budesonide (a corticosteroid) for 05/2019 to 08/2019, or a prescriber attestation of that course. No request-date window applies to this historical trial.
- **C5b**: Pharmacy or claims record, or prescription record, for infliximab 07/2023 to 07/2026 (who: pharmacy)
  > Criterion C5b (Policy 3.5(b)) needs support for the infliximab course in the medication history dated 2026-11-08: infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026, stopped for secondary loss of response. Please request the pharmacy or claims history covering that period from the infusion or dispensing source. If no record exists, Dr. Adeyemi can provide a prescriber attestation of the course.
  - Would satisfy the policy: Policy 3.5(b) accepts a pharmacy or claims record, or prescription record, showing infliximab (or adalimumab) therapy for 07/2023 to 07/2026, or a prescriber attestation of that course. No request-date window applies to this historical trial.
- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe (who: ordering_provider)
  > Dr. Adeyemi, criterion C10a (Policy 3.10(a)) is not met for PT-3034. The chart shows no prior ustekinumab trial of either preferred product, and the 2026-11-09 GI note starts ustekinumab-aekn as a first exposure. Please review; the policy requires documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response to, or intolerance of, both ustekinumab-aekn and ustekinumab-ttwe. Intolerance of only one preferred product does not satisfy it. No date window is specified.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product (who: ordering_provider)
  > Dr. Adeyemi, criterion C10b (Policy 3.10(b)) is not met for PT-3034. The chart has no documented contraindication or hypersensitivity to any inactive ingredient. The criterion asks for an ingredient absent from the requested product, but ustekinumab-aekn is one of the two preferred products, so please review whether this criterion can apply to this request.

## Run cost

3 model calls, 24,849 input and 18,273 output tokens, 74.7 s of model time, $0.013 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent GAPS_TO_CLOSE. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C5b | 3.5(b) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
