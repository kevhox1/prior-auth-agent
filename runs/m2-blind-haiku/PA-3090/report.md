# PA-3090: ustekinumab-aekn for PT-3090

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 106.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI provider's 2026-11-07 note documents ulcerative pancolitis with moderate-to-severe activity and a partial Mayo score of 6. This meets the diagnosis and provider-described severity requirement. (confidence 0.90)

- `PT-3090/gi-note-2026-11-07` (2026-11-07): "Moderately to severely active ulcerative pancolitis."
- `PT-3090/gi-note-2026-11-07` (2026-11-07): "Partial Mayo score today: 6."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The flexible sigmoidoscopy dated 2026-08-18, within 12 months, describes friability and erosions. A fecal calprotectin of 817 ug/g on 2026-09-22 is far above the reference range of <50, so either option independently satisfies the criterion. (confidence 0.92)

- `PT-3090/flexible-sigmoidoscopy-2026-08-18` (2026-08-18): "Rectum to 36 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 2."
- `PT-3090/labs-2026-09-22` (2026-09-22): "CALPROTECTIN FECAL ................ 817 ug/g  (<50)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in the 2026-11-07 gastroenterology follow-up note, and the request names Dr. S. Adeyemi, Gastroenterology as ordering provider. The prescriber is a gastroenterologist. (confidence 0.88)

- `PT-3090/gi-note-2026-11-07` (2026-11-07): "Start ustekinumab-aekn: 520 mg IV once (weight 106.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 2006-07-11 makes the member 20 years old on the 2026-11-18 request date, which meets the 18-or-older requirement. (confidence 0.97)

- `PT-3090/demographics-2026-03-03` (2026-03-03): "Date of birth: 2006-07-11"
- Code checks: age 20 on 2026-11-18 from DOB 2006-07-11

### C5 (policy 3.5): **CONFLICTING**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **CONFLICTING****: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Outside records describe azathioprine stopped for pancreatitis intolerance and mesalamine stopped for inadequate response, both of which would satisfy the conventional-therapy step. The 2026-11-05 reconciled medication history states no prior IBD therapy is documented, so the records conflict and the policy requires clinical review rather than approval on reported history. (confidence 0.75)

- `PT-3090/outside-records-2023-12-18` (2023-12-18): "Azathioprine 2.5 mg/kg daily, 2019-12 to 2020-02. Reason stopped: intolerance (acute pancreatitis)."
- `PT-3090/outside-records-2023-12-18` (2023-12-18): "Mesalamine 4.8 g daily, 2020-03 to 2020-07. Reason stopped: inadequate response at full dose after 12 weeks."
- `PT-3090/medication-history-2026-11-05` (2026-11-05): "(no prior IBD therapy documented)"
- Missing: Pharmacy or claims records confirming azathioprine and mesalamine fills
- Missing: Reconciliation of the 2026-11-05 medication history with the 2023 outside records

**C5b (policy 3.5(b)): **CONFLICTING****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The 2023 outside records document adalimumab 2023-07 to 2023-11 stopped for primary non-response, which would satisfy the anti-TNF step. The 2026-11-05 reconciled medication history says no prior IBD therapy is documented, which contradicts it, so the chart must be reconciled before this can be accepted. (confidence 0.75)

- `PT-3090/outside-records-2023-12-18` (2023-12-18): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2023-11. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."
- `PT-3090/medication-history-2026-11-05` (2026-11-05): "(no prior IBD therapy documented)"
- Missing: Pharmacy or claims records confirming adalimumab dispensing 2023-07 to 2023-11
- Missing: Reconciliation of the 2026-11-05 medication history with the 2023 outside records

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus result of Negative is dated 2026-09-22, within 12 months of the 2026-11-18 request. No positive screen requires further action. (confidence 0.93)

- `PT-3090/labs-2026-09-22` (2026-09-22): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as Nonreactive on 2026-09-22. No lookback limit applies and no positive result requires a monitoring plan. (confidence 0.93)

- `PT-3090/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3090/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-11-05 medication reconciliation states the member is not on any biologic, JAK inhibitor, or S1P modulator. A 2025 dermatology note mentions unnamed 'immunosuppression', which does not name a concurrent agent, so the reconciled list controls. (confidence 0.80)

- `PT-3090/medication-history-2026-11-05` (2026-11-05): "Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A current weight of 106.3 kg is documented 2026-11-07, within 30 days of the request. The requested 520 mg IV induction matches the >85 kg band, and 90 mg SC every 8 weeks starting 8 weeks after IV dosing matches labeling. (confidence 0.90)

- `PT-3090/gi-note-2026-11-07` (2026-11-07): "Weight 106.3 kg."
- `PT-3090/gi-note-2026-11-07` (2026-11-07): "Start ustekinumab-aekn: 520 mg IV once (weight 106.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.3 kg (2026-11-07) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

No passage documents any prior trial of either preferred ustekinumab product. The requested product, ustekinumab-aekn, is itself a preferred product, but this sub-criterion specifically requires failure of both preferred products and nothing in the chart settles it. (confidence 0.80)

- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to any inactive ingredient. Nothing in the retrieved chart settles this sub-criterion either way. (confidence 0.80)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient shared by ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C5a**: Reconciled conventional-therapy history (azathioprine, mesalamine) and pharmacy or claims confirmation of fills (who: ordering_provider)
  > Dr. Adeyemi, criterion 3.5(a) for PT-3090 is conflicting. The 2023-12-18 outside records document azathioprine stopped for pancreatitis intolerance and mesalamine stopped for inadequate response, but the 2026-11-05 reconciled medication history states no prior IBD therapy is documented. Please review and reconcile these records, and confirm whether pharmacy or claims fills are available.
  - Would satisfy the policy: Policy 3.5(a) accepts documented intolerance to, inadequate response to, or contraindication to azathioprine, 6-mercaptopurine, methotrexate, or systemic corticosteroids (budesonide included), and for ulcerative colitis oral aminosalicylates such as mesalamine. The 2023 entries (azathioprine 2019-12 to 2020-02; mesalamine 2020-03 to 2020-07) must be reconciled with the 2026-11-05 history.
- **C5b**: Reconciled anti-TNF history (adalimumab 2023-07 to 2023-11) and pharmacy or claims confirmation of dispensing (who: ordering_provider)
  > Dr. Adeyemi, criterion 3.5(b) for PT-3090 is conflicting. The 2023-12-18 outside records document adalimumab 40 mg every 2 weeks from 2023-07 to 2023-11, stopped for primary non-response, but the 2026-11-05 reconciled medication history states no prior IBD therapy is documented. Please review and reconcile these records and confirm whether dispensing records are available.
  - Would satisfy the policy: Policy 3.5(b) accepts documented primary non-response, secondary loss of response, or intolerance to adalimumab or infliximab (including biosimilars), or a specifically documented contraindication. The 2023-07 to 2023-11 adalimumab course must be reconciled with the 2026-11-05 history, with dispensing records confirming it.
- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe (who: ordering_provider)
  > Dr. Adeyemi, criterion 3.10(a) for PT-3090 has insufficient evidence. No record in the chart documents a prior trial of ustekinumab-aekn or ustekinumab-ttwe. Please review whether any prior trial of either product exists and document it if so.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to both preferred products, ustekinumab-aekn and ustekinumab-ttwe. Intolerance to only one of them does not satisfy this criterion. The policy text provided states no date window for this documentation.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient shared by both preferred products and absent from ustekinumab-aekn (who: ordering_provider)
  > Dr. Adeyemi, criterion 3.10(b) for PT-3090 has insufficient evidence. The chart contains no documented contraindication or hypersensitivity to any inactive ingredient. Please review and document whether one exists, or confirm that none does.
  - Would satisfy the policy: Policy 3.10(b) accepts a documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product. If no such history exists, no new document can satisfy this criterion.

## Run cost

3 model calls, 25,599 input and 16,093 output tokens, 63.6 s of model time, $0.012 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent NEEDS_PHYSICIAN. Case type: buried_evidence.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | CONFLICTING | CONFLICTING | wrong |
| C5b | 3.5(b) | MET | CONFLICTING | CONFLICTING | wrong |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
