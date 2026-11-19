# PA-3045: ustekinumab-aekn for PT-3045

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

The treating GI provider's 2026-11-06 note documents Crohn's disease and describes it as moderately to severely active. A Harvey-Bradshaw Index of 9 is recorded at the same visit, which supports the severity description. (confidence 0.93)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Harvey-Bradshaw Index today: 9."

### C2 (policy 3.2): **INSUFFICIENT**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy describing ulceration is the 2025-04-18 colonoscopy, which is outside the 12-month window before the 2026-11-18 request. The 2026-10-03 CRP is elevated but does not satisfy this criterion, and no fecal calprotectin result is in the chart. (confidence 0.80)

- `PT-3045/colonoscopy-2025-04-18` (2025-04-18): "Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 describing active inflammation (ulceration, erosions, or friability)
- Missing: Fecal calprotectin result dated within 12 months before 2026-11-18, with the performing laboratory's reference range
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab start order appears in a GI follow-up note authored by Dr. S. Adeyemi, the gastroenterologist. This satisfies the requirement that the medication be prescribed by a gastroenterologist. (confidence 0.85)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 02/21/1966 makes the member 60 years old on the 2026-11-18 request date, which meets the age-18 requirement. (confidence 0.97)

- `PT-3045/demographics-2026-04-15` (2026-04-15): "Date of birth: 02/21/1966"
- Code checks: age 60 on 2026-11-18 from DOB 1966-02-21

### C5 (policy 3.5): **INSUFFICIENT**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

An outside practice transfer summary documents a 6-mercaptopurine trial from 04/2023 to 10/2023, stopped for inadequate response. This is a treating-provider record, though not pharmacy claims, and nothing in the passages contradicts it. Current budesonide is listed without any failure history, so it does not add to this criterion. (confidence 0.70)

- `PT-3045/outside-records-2023-11-18` (2023-11-18): "Mercaptopurine 1.5 mg/kg daily, 04/2023 to 10/2023. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."

**C5b (policy 3.5(b)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history documents an adalimumab trial from 12/2023 to 05/2026 stopped for intolerance (drug-induced lupus). That entry was reconciled by an RN with no prescriber note or pharmacy claims in the chart. The 2026-06-13 note refers to 'current therapy' after the stated adalimumab stop date, which the reviewer should clarify. (confidence 0.60)

- `PT-3045/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."
- `PT-3045/gi-note-2026-06-13` (2026-06-13): "Ongoing symptoms despite current therapy."
- Missing: Pharmacy or medical claims, or a prescriber chart note, documenting adalimumab start/stop dates and the reason stopped (the current source is an RN-reconciled medication history)
- Missing: Treating-provider documentation of the drug-induced lupus and positive anti-histone antibody result
- Missing: Clarification of which therapy the 2026-06-13 note means by 'current therapy', since adalimumab is listed as stopped in 05/2026

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus collected 2026-10-03 is negative. That date is within 12 months before the 2026-11-18 request. The 2023 QuantiFERON is outside the window and was not relied on. (confidence 0.95)

- `PT-3045/labs-2026-10-03` (2026-10-03): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-10-03. Because both results are negative, no monitoring or prophylaxis plan is required, and this criterion has no lookback limit. (confidence 0.93)

- `PT-3045/labs-2026-10-03` (2026-10-03): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3045/labs-2026-10-03` (2026-10-03): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-11-04 medication reconciliation states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The only prior biologic, adalimumab, is listed as stopped in 05/2026, so there is no overlap with ustekinumab. (confidence 0.90)

- `PT-3045/medication-history-2026-11-04` (2026-11-04): "No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3045/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The 2026-11-06 weight of 55.0 kg is within 30 days of the request and falls in the 260 mg induction band. The requested maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches labeling. (confidence 0.90)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Weight 55.0 kg."
- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-06) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The chart names ustekinumab-aekn as the requested product and does not document any prior ustekinumab product. It contains no documented inadequate response or intolerance to either preferred product, so this requirement cannot be confirmed from the chart. (confidence 0.75)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to an inactive ingredient. The requested product is itself a preferred product, so this exception may not be needed, but the reviewer should confirm no such documentation exists elsewhere. (confidence 0.70)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product, if one exists

## To-do list (gap plan)

- **C2**: Endoscopy report dated on or after 2025-11-18 describing active inflammation (ulceration, erosions, or friability), or a fecal calprotectin result dated on or after 2025-11-18 above the performing lab's reference upper limit (who: ordering_provider)
  > PA-3045 criterion C2 (Policy 3.2) is not met. The only endoscopy describing ulceration is the colonoscopy dated 2025-04-18, which is outside the 12-month window starting 2025-11-18, and no fecal calprotectin is in the chart. Dr. Adeyemi, please review whether a qualifying endoscopy or fecal calprotectin result exists or is needed for this request.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 describing active inflammation (ulceration, erosions, or friability), or a fecal calprotectin result dated on or after 2025-11-18 above the performing laboratory's reference upper limit. CRP, ESR, and imaging alone do not qualify.
- **C5b**: Prescriber documentation of adalimumab start and stop dates and the drug-induced lupus intolerance (with positive anti-histone antibodies), supported by pharmacy or medical claims, plus clarification of 'current therapy' in the 2026-06-13 GI note (who: ordering_provider)
  > PA-3045 criterion C5b (Policy 3.5(b)) is not yet supported. The adalimumab entry (12/2023 to 05/2026, stopped for drug-induced lupus) comes only from an RN-reconciled medication history dated 2026-11-04, and the 2026-06-13 note says 'ongoing symptoms despite current therapy' after adalimumab was listed as stopped. Dr. Adeyemi, please review and document the adalimumab course and reason stopped, and clarify which therapy the 2026-06-13 note refers to.
  - Would satisfy the policy: Policy 3.5(b) accepts documentation of an inadequate response, loss of response, or intolerance to adalimumab or infliximab (including biosimilars), or a specifically documented contraindication. The criterion states no lookback window. The record should show the drug, dates, and reason stopped, supported by a prescriber note or pharmacy or medical claims rather than only an RN-reconciled history.
- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe; the chart shows no prior ustekinumab exposure to either product (who: practice_staff)
  > PA-3045 criterion C10a (Policy 3.10(a)) needs documented inadequate response or intolerance to both preferred products, ustekinumab-aekn and ustekinumab-ttwe. The chart lists only the requested start order dated 2026-11-06 and no prior ustekinumab. Please check whether any outside or prior record documents ustekinumab exposure to either product.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. Intolerance of only one preferred product does not satisfy it. The policy states no date window. If the patient has never received either product, no new document can satisfy this item.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product, if one exists (who: ordering_provider)
  > PA-3045 criterion C10b (Policy 3.10(b)) has no supporting documentation in the chart. The requested product is itself a preferred product, so this exception may not apply. Dr. Adeyemi, please confirm whether any documented hypersensitivity or contraindication to an inactive ingredient exists that would apply here.
  - Would satisfy the policy: Policy 3.10(b) accepts a documented contraindication or hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product. This item is only relevant if such documentation exists; the policy states no date window.

## Run cost

3 model calls, 24,879 input and 20,867 output tokens, 84.7 s of model time, $0.014 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent GAPS_TO_CLOSE. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
