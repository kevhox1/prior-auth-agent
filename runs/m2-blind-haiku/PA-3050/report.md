# PA-3050: ustekinumab-ttwe for PT-3050

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 66.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI documented Crohn's disease as moderately to severely active on 2026-11-04, with a Harvey-Bradshaw Index of 14. The problem list independently records the Crohn's diagnosis. (confidence 0.93)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3050/gi-note-2026-11-04` (2026-11-04): "Harvey-Bradshaw Index today: 14."
- `PT-3050/problem-list-2026-11-04` (2026-11-04): "Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2022."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-10-11 is within 12 months of the 2026-11-18 request and describes ulceration in the terminal ileum. A fecal calprotectin of 1198 ug/g dated 2026-09-12 is flagged high against a reference of <50, which independently satisfies option (b). (confidence 0.93)

- `PT-3050/colonoscopy-2026-10-11` (2026-10-11): "Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-3050/labs-2026-09-12` (2026-09-12): "Calprotectin, fecal | 1198 ug/g | H | <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order to start ustekinumab-ttwe appears in a gastroenterology follow-up note, and the request names Dr. S. Adeyemi (Gastroenterology) as ordering provider. Dr. Adeyemi is also the ordering clinician on the 2026-09-12 labs. The note's author credentials are not restated in the quoted lines, so confidence is moderate. (confidence 0.80)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3050/labs-2026-09-12` (2026-09-12): "ORDERING: Dr. S. Adeyemi"

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 1996-02-13 makes the member 30 years old on the 2026-11-18 request date, which is above the 18-year minimum. (confidence 0.97)

- `PT-3050/demographics-2026-10-23` (2026-10-23): "Date of birth: 1996-02-13"
- Code checks: age 30 on 2026-11-18 from DOB 1996-02-13

### C5 (policy 3.5): MET
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history records a mercaptopurine trial from 2022-08 to 2023-03, stopped for inadequate response at a therapeutic metabolite level. This satisfies the conventional-therapy step, which requires only one qualifying agent. Confidence is moderate because the policy requires claims or prescription support, and those records are not among the passages. (confidence 0.80)

- `PT-3050/medication-history-2026-10-31` (2026-10-31): "| Mercaptopurine | 1.5 mg/kg daily | 2022-08 | 2023-03 | Inadequate response after 6 months at a therapeutic metabolite level |"

**C5b (policy 3.5(b)): MET**: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history records an adalimumab trial from 2023-09 to 2026-07, stopped for documented intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias). Intolerance of a TNF blocker satisfies this criterion. Confidence is moderate because the policy requires claims or prescription support, which is not among the passages. (confidence 0.80)

- `PT-3050/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus result of NEGATIVE dated 2026-09-12 falls within 12 months before the request. The result is determinate and not indeterminate. (confidence 0.95)

- `PT-3050/labs-2026-09-12` (2026-09-12): "QuantiFERON-TB Gold Plus | NEGATIVE | - | Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-09-12. Both are negative, so no monitoring or prophylaxis plan is required, and the criterion has no lookback limit. (confidence 0.93)

- `PT-3050/labs-2026-09-12` (2026-09-12): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3050/labs-2026-09-12` (2026-09-12): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-10-31 medication history states the member is not on any biologic, JAK inhibitor, or S1P modulator. The prior adalimumab is recorded as stopped in 2026-07, and no later passage contradicts this. (confidence 0.88)

- `PT-3050/medication-history-2026-10-31` (2026-10-31): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-3050/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The current weight of 66.0 kg is dated 2026-11-04, within 30 days of the request. That weight falls in the more than 55 kg to 85 kg band, which calls for 390 mg IV, and the request matches. The maintenance schedule of 90 mg SC every 8 weeks starting 8 weeks after the IV dose also matches. (confidence 0.92)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Weight 66.0 kg."
- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.0 kg (2026-11-04) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The requested product, ustekinumab-ttwe, is itself a preferred product, but this criterion requires documented failure of both preferred products. No passage documents any prior trial, response, or intolerance to ustekinumab-aekn or ustekinumab-ttwe. The gap cannot be resolved from the chart, so it is recorded as missing rather than as a failure. (confidence 0.80)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage in the chart documents a contraindication or hypersensitivity to any excipient. The adalimumab intolerance (drug-induced lupus) concerns a different drug and does not address this requirement. The criterion therefore cannot be met on the current record. (confidence 0.85)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C10a**: Documented inadequate response or intolerance to ustekinumab-aekn and to ustekinumab-ttwe (both preferred products) (who: ordering_provider)
  > Criterion 3.10(a) for PA-3050 (ustekinumab-ttwe) needs documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. The chart has no prior trial, response, or intolerance for either product; the 2026-11-04 GI note only orders ustekinumab-ttwe as a start. Please review and document whether either product has been tried and, if so, the outcome, or note that no prior trial exists.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to each of ustekinumab-aekn and ustekinumab-ttwe. The excerpt provided does not state a lookback window for this evidence.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product (who: ordering_provider)
  > Criterion 3.10(b) for PA-3050 is open: the chart has no documented contraindication or hypersensitivity to any excipient, and the adalimumab intolerance (drug-induced lupus) is a different drug. Note also that the requested product, ustekinumab-ttwe, is itself one of the two preferred products, so an excipient shared by both preferred products would also be in the requested product. Please review how this criterion applies to this request.

## Run cost

3 model calls, 22,882 input and 13,930 output tokens, 56.1 s of model time, $0.011 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: clean.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
