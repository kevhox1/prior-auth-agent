# PA-3091: ustekinumab-ttwe for PT-3091

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 87.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI provider's 2026-10-31 note documents moderately to severely active ileocolonic Crohn's disease, with a Harvey-Bradshaw Index of 10 as the validated activity score. The 2026-08-29 colonoscopy also records SES-CD 13, which supports the severity. (confidence 0.93)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Harvey-Bradshaw Index today: 10."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-08-29 is within 12 months before the 2026-11-18 request and describes ulcers, which is active inflammation. The elevated CRP alone does not count, but the endoscopy independently satisfies (a). (confidence 0.92)

- `PT-3091/colonoscopy-2026-08-29` (2026-08-29): "Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in the 2026-10-31 GI follow-up note by Dr. S. Adeyemi, and the request lists the ordering provider as Gastroenterology. The note header naming the specialty was not among the quoted passages, so the reviewer should confirm it. (confidence 0.80)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 1973-05-02 makes the member 53 years old on the 2026-11-18 request date, which is over 18. (confidence 0.97)

- `PT-3091/demographics-2026-02-06` (2026-02-06): "Date of birth: 1973-05-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-05-02

### C5 (policy 3.5): MET
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The outside transfer summary records methotrexate from 2024-05 to 2024-12, stopped for intolerance (nausea and ALT above 3 times the upper limit of normal). Policy accepts treating-provider chart history, but no pharmacy claims are in the chart and the 2026-10-28 medication history does not list methotrexate; that is an omission, not a conflict. (confidence 0.72)

- `PT-3091/outside-records-2025-01-18` (2025-01-18): "Methotrexate 25 mg subcutaneously weekly, 2024-05 to 2024-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The 2026-10-28 medication history names infliximab, gives dates 2025-02 to 2026-07, and states intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias). It is supported only by RN reconciliation with no claims in the chart, so the reviewer should confirm the source. (confidence 0.75)

- `PT-3091/medication-history-2026-10-28` (2026-10-28): "Infliximab 5 mg/kg IV every 8 weeks, 2025-02 to 2026-07. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus result of NEGATIVE is dated 2026-10-08, within 12 months of the request. The result is determinate and not indeterminate. (confidence 0.95)

- `PT-3091/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No passage in the chart shows a resulted HBsAg or total anti-HBc test. The 2026-10-08 labs passage quoted only the QuantiFERON result, and vaccination or anti-HBs alone would not satisfy the criterion. (confidence 0.90)

- Missing: Resulted hepatitis B surface antigen (HBsAg) test
- Missing: Resulted total hepatitis B core antibody (anti-HBc) test

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

Current vedolizumab, a biologic, is documented as stopping when ustekinumab induction begins, and the GI note orders this. No JAK inhibitor or S1P modulator appears in the medication history passages. (confidence 0.85)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3091/medication-history-2026-10-28` (2026-10-28): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-09); to be discontinued when ustekinumab starts."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 87.0 kg was recorded on 2026-10-31, within 30 days of the request, and falls in the over-85 kg band that matches 520 mg IV. The requested maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the labeling. (confidence 0.92)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Weight 87.0 kg."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 87.0 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

No passage documents any prior ustekinumab trial, including ustekinumab-aekn or ustekinumab-ttwe. The requested product is itself a preferred product, so this exception path bears on the requirement only if the reviewer treats it as relevant. (confidence 0.80)

- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to an inactive ingredient. The requested product is named explicitly as ustekinumab-ttwe, which is a preferred product, so this exception does not otherwise apply. (confidence 0.80)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C7**: Resulted hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) tests (who: practice_staff)
  > PA-3091 (PT-3091), criterion 3.7: the chart has no resulted HBsAg or total anti-HBc test. The 2026-10-08 lab passage shows only the QuantiFERON result. Please check the lab system for any resulted HBsAg or anti-HBc and file them if found. If none exist, Dr. Adeyemi will need to review whether these tests should be ordered.
  - Would satisfy the policy: Policy 3.7 accepts a resulted HBsAg and a resulted total anti-HBc with no lookback limit, so the result date does not matter. If either result is positive, the record must also include a plan for monitoring or antiviral prophylaxis. Vaccination history or anti-HBs alone does not satisfy this item, and an ordered but unresulted test does not count.
- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe (who: ordering_provider)
  > PA-3091 (PT-3091), criterion 3.10(a): the chart contains no documented prior ustekinumab trial, including ustekinumab-aekn or ustekinumab-ttwe. Policy 3.10(a) requires an inadequate response to, or intolerance of, both preferred products, and intolerance of only one does not satisfy it. Dr. Adeyemi, please review whether prior treatment history for both products is documented and whether this criterion can be addressed.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response to, or intolerance of, both ustekinumab-aekn and ustekinumab-ttwe. The policy sets no date window for this documentation. Intolerance of only one of the two products does not satisfy the criterion.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > PA-3091 (PT-3091), criterion 3.10(b): no contraindication or hypersensitivity to an inactive ingredient is documented in the chart. The requested product is ustekinumab-ttwe, which is itself one of the two preferred products, so the criterion's requirement that the ingredient be absent from the requested product cannot be met by that product. Dr. Adeyemi, please review this criterion against the request.

## Run cost

3 model calls, 23,938 input and 16,953 output tokens, 70.3 s of model time, $0.012 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
