# PA-3093: ustekinumab-ttwe for PT-3093

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

The treating GI provider documents moderately to severely active ileocolonic Crohn's disease on 2026-11-05, with a Harvey-Bradshaw Index of 13. The diagnosis of Crohn's disease is also documented in the 2025 outside record and the active problem list. (confidence 0.93)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-10-12, within 12 months of the 2026-11-18 request, describes ulcers in the terminal ileum, which is active inflammation. A fecal calprotectin of 1269 ug/g on 2026-09-25 is also well above the <50 reference limit. (confidence 0.93)

- `PT-3093/colonoscopy-2026-10-12` (2026-10-12): "Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3093/labs-2026-09-25` (2026-09-25): "1269 ug/g"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The requested ustekinumab order is written in the gastroenterology note by Dr. M. Chen, who is listed as the ordering provider and is a gastroenterologist. The request is therefore prescribed by a gastroenterologist. (confidence 0.95)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 1957-02-24 gives an age of 69 on the 2026-11-18 request date, which is 18 or older. The 2025 outside record shows the same date of birth. (confidence 0.98)

- `PT-3093/demographics-2026-05-15` (2026-05-15): "Date of birth: 1957-02-24"
- Code checks: age 69 on 2026-11-18 from DOB 1957-02-24

### C5 (policy 3.5): MET
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Methotrexate was given from 2024-03 to 2024-11 and stopped for intolerance (nausea, ALT above 3 times the upper limit). Azathioprine was given from 2024-12 to 2025-02 and stopped for intolerance (acute pancreatitis). Either trial satisfies the conventional therapy requirement, and no passage contradicts these records. (confidence 0.85)

- `PT-3093/outside-records-2025-03-18` (2025-03-18): "Methotrexate 25 mg subcutaneously weekly, 2024-03 to 2024-11. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3093/outside-records-2025-03-18` (2025-03-18): "Azathioprine 2.5 mg/kg daily, 2024-12 to 2025-02. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): MET**: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

Infliximab was given from 2025-04 to 2026-07 and stopped for secondary loss of response, with a low trough level and positive antibodies. This is a documented anti-TNF trial with dates and reason, which meets the anti-TNF requirement. (confidence 0.90)

- `PT-3093/medication-history-2026-11-05` (2026-11-05): "| Infliximab | 5 mg/kg IV every 8 weeks | 2025-04 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 23 U/mL (reference <10) |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

The 2026-09-25 IGRA was positive, so the record must show the positive-screen pathway. The 2026-09-28 chest radiograph excludes active pulmonary TB, and latent TB treatment with rifampin was started 2026-10-01. No negative screen within 12 months is on file, so this rests on the positive pathway, and the reviewer should confirm that reading. (confidence 0.75)

- `PT-3093/labs-2026-09-25` (2026-09-25): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-3093/chest-xray-2026-09-28` (2026-09-28): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

The only hepatitis B result in the passages is anti-HBs, which does not satisfy this criterion. The HBsAg and total anti-HBc results are not in the record, and the vaccine history does not count. (confidence 0.85)

- `PT-3093/labs-2026-09-25` (2026-09-25): "Reactive (immune)>10 mIU/mL"
- Missing: Resulted hepatitis B surface antigen (HBsAg) test
- Missing: Resulted total hepatitis B core antibody (anti-HBc) test

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current list shows vedolizumab, a concurrent biologic, but the GI plan documents that it will be stopped on the date ustekinumab induction starts. No JAK inhibitor or S1P modulator is listed. Under the switching clause, documented stopping of the prior agent satisfies the criterion. (confidence 0.80)

- `PT-3093/medication-history-2026-11-05` (2026-11-05): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-24); to be discontinued when ustekinumab starts."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 55.0 kg was recorded on 2026-11-05, 13 days before the request. That weight falls in the 55 kg or less band, which requires 260 mg IV, and the requested induction dose is 260 mg. The maintenance schedule of 90 mg every 8 weeks starting 8 weeks after the IV dose matches labeling. (confidence 0.92)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Weight 55.0 kg."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-05) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **NOT MET****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The criterion requires documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. No ustekinumab trial, and no failure of either preferred product, is documented in the passages. The requested product is itself preferred, so reviewers should note that this leaf is not met as written. (confidence 0.70)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No contraindication or hypersensitivity to an inactive ingredient is documented in the retrieved passages. The chart does not settle this either way, so it is left for reviewer follow-up. (confidence 0.60)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C7**: Resulted HBsAg and total anti-HBc tests (both) (who: lab)
  > Criterion C7 (Policy 3.7) for PA-3093 needs both a resulted hepatitis B surface antigen (HBsAg) and a resulted total hepatitis B core antibody (anti-HBc) on file. The only hepatitis B result in the chart is anti-HBs dated 2026-09-25, which does not satisfy this criterion. Please confirm whether these two tests have been drawn and resulted, and if either is positive, the chart must include a monitoring or prophylaxis plan.
  - Would satisfy the policy: Policy 3.7 accepts a resulted HBsAg and a resulted total anti-HBc with no lookback limit, so a result of any date counts. If either result is positive, the record must also include a monitoring or antiviral prophylaxis plan. The anti-HBs result dated 2026-09-25, vaccination history, and an ordered-but-unresulted test do not satisfy this criterion.
- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe (who: ordering_provider)
  > Criterion C10a (Policy 3.10(a)) for PA-3093 is not met: the chart has no documented inadequate response or intolerance to ustekinumab-aekn or ustekinumab-ttwe. The requested product, ustekinumab-ttwe, is one of the two preferred products, so the policy requires documented failure or intolerance of both. Please review this criterion with the treating gastroenterologist, Dr. M. Chen, and document any relevant history.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response to, or intolerance of, both ustekinumab-aekn and ustekinumab-ttwe. Intolerance of only one preferred product does not meet this requirement. The requested product, ustekinumab-ttwe, is itself one of the two preferred products, so the criterion as written depends on the record of prior use of each product.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > Criterion C10b (Policy 3.10(b)) for PA-3093 has no documented contraindication or hypersensitivity to an inactive ingredient. The policy requires an ingredient present in both ustekinumab-aekn and ustekinumab-ttwe but absent from the requested product, ustekinumab-ttwe. Please review with Dr. M. Chen whether any such contraindication or hypersensitivity exists and document it, or confirm that none applies.
  - Would satisfy the policy: Policy 3.10(b) accepts a documented contraindication or hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product. Because the requested product, ustekinumab-ttwe, is one of the two preferred products, an ingredient present in both cannot be absent from it as written, so reviewer confirmation of the criterion's intent is needed.

## Run cost

3 model calls, 25,366 input and 21,680 output tokens, 84.9 s of model time, $0.015 at list price (0 served from cache).

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
