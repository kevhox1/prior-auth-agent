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

The treating gastroenterologist's 10/30/2026 note documents ileocolonic Crohn's disease described as moderately to severely active. The note supports this with a Harvey-Bradshaw Index of 13 and a described symptom burden. (confidence 0.90)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Harvey-Bradshaw Index today: 13."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A fecal calprotectin of 1306 ug/g dated 08/23/2026 is within 12 months before the 11/18/2026 request and is above the stated reference of <50. The result is quoted in the GI note; the original lab report is not in the chart, so the reviewer may want to confirm it against the lab record. (confidence 0.80)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "His calprotectin from 08/23/2026 came back at 1306 ug/g (lab reference <50)."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in the GI follow-up note by Dr. M. Chen, who is listed as the ordering gastroenterologist on the request. The chart identifies Dr. Chen as the GI prescriber, so this criterion is satisfied. (confidence 0.88)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 05/12/1990 makes the member 36 years old on the 11/18/2026 request date, which meets the 18-or-older requirement. (confidence 0.95)

- `PT-3092/demographics-2025-10-15` (2025-10-15): "Date of birth: 05/12/1990"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-12

### C5 (policy 3.5): **INSUFFICIENT**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history lists budesonide, a corticosteroid, from 09/2022 to 12/2022 stopped for inadequate response, which would qualify on substance. The only source is an RN reconciliation from history with no pharmacy claims, and the policy requires treating-provider notes, records, or prescriber attestation to support it. (confidence 0.60)

- `PT-3092/medication-history-2026-10-28` (2026-10-28): "| Budesonide | 9 mg daily | 09/2022 | 12/2022 | Inadequate response after 10 weeks |"
- Missing: Treating-provider chart note or prescriber attestation confirming the budesonide trial (09/2022 to 12/2022) and the inadequate response, or pharmacy/claims records for that trial
- Missing: Pharmacy or claims record for budesonide 09/2022 to 12/2022 (none is on file; the medication history was reconciled by RN from patient history)

**C5b (policy 3.5(b)): MET**: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The treating gastroenterologist specifically documents that anti-TNF agents are contraindicated because of demyelinating disease. The active problem list supports this with relapsing-remitting multiple sclerosis, so the policy's contraindication route is met even though no adalimumab or infliximab trial is documented. (confidence 0.85)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3092/problem-list-2026-10-30` (2026-10-30): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy 3.6): **INSUFFICIENT**
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

No tuberculosis screening result appears in the passages for this member. A test within the 12 months before the request is needed before this criterion can be assessed. (confidence 0.90)

- Missing: Negative interferon-gamma release assay or tuberculin skin test dated on or after 11/18/2025

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 09/21/2026. Because neither result is positive, no monitoring or prophylaxis plan is required. (confidence 0.92)

- `PT-3092/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3092/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is currently on vedolizumab, a biologic, and the GI note documents that it will be stopped at ustekinumab induction, which the switch rule allows. No JAK inhibitor or S1P modulator appears on the medication list. (confidence 0.80)

- `PT-3092/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/16/2026); to be discontinued when ustekinumab starts."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The 10/30/2026 weight of 55.0 kg is within 30 days of the request and matches the 260 mg induction band, and the maintenance schedule is 90 mg every 8 weeks starting 8 weeks after IV. The 06/01/2026 weight of 58.0 kg would fall in the 390 mg band, so the reviewer should confirm the current weight before dosing. (confidence 0.80)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Weight 55.0 kg."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3092/gi-note-2026-06-01` (2026-06-01): "Weight 58.0 kg."
- Code checks: weight 55.0 kg (2026-10-30) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

No prior trial or inadequate response or intolerance to either preferred ustekinumab product is documented. The requested product, ustekinumab-ttwe, is itself a preferred product, so this two-product exception is not the basis for coverage of this request. (confidence 0.75)

- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

The chart documents no hypersensitivity or contraindication to any inactive ingredient. The requested product is itself a preferred product, so this exception is not the basis for coverage. (confidence 0.75)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C5a**: Treating-provider chart note or prescriber attestation for the budesonide trial (09/2022 to 12/2022) with the inadequate response, or pharmacy/claims record for that trial (who: practice_staff)
  > Criterion C5a (policy 3.5(a)) is open because the budesonide trial (09/2022 to 12/2022, stopped for inadequate response) appears only in the RN medication history dated 2026-10-28. Please search the chart and pharmacy records for a 2022 provider note or a claims record for budesonide that documents this trial. If none exists, the ordering provider will need to attest to the trial.
  - Would satisfy the policy: Policy 3.5(a) accepts a treating-provider note, prescriber attestation, or pharmacy/claims record confirming budesonide 9 mg daily from 09/2022 to 12/2022 stopped for inadequate response. The policy sets no look-back window for this prior-therapy history.
- **C6**: Negative interferon-gamma release assay or tuberculin skin test result (who: lab)
  > Criterion C6 (policy 3.6) has no tuberculosis screening result on file for this member. The policy accepts a negative IGRA or TST dated on or after 2025-11-18. Please send any TB screening result from the lab that falls in that window, and confirm whether one has been drawn.
  - Would satisfy the policy: Policy 3.6 accepts a negative interferon-gamma release assay or tuberculin skin test dated on or after 2025-11-18. An indeterminate IGRA does not count as negative.
- **C10a**: Documented inadequate response or intolerance to ustekinumab-aekn, and to ustekinumab-ttwe (who: ordering_provider)
  > Criterion C10a (policy 3.10(a)) is open: no prior trial or inadequate response/intolerance to ustekinumab-aekn or ustekinumab-ttwe is documented in the chart. Dr. Chen, please review whether the record supports documentation of both products. The policy requires documentation for both, not just one.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. Intolerance of only one preferred product does not satisfy it.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > Criterion C10b (policy 3.10(b)) is open: the chart documents no hypersensitivity or contraindication to any inactive ingredient. Dr. Chen, please review the chart and confirm whether any such documented reaction exists. If none exists, this criterion remains unmet.
  - Would satisfy the policy: Policy 3.10(b) accepts a documented contraindication or hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

## Run cost

3 model calls, 23,461 input and 19,047 output tokens, 79.8 s of model time, $0.013 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
