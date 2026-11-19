# PA-3041: ustekinumab-aekn for PT-3041

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

The treating GI note dated 2026-11-08 documents Crohn's disease described as moderately to severely active. It also records a Harvey-Bradshaw Index of 11 by the treating provider, which supports the severity description. (confidence 0.93)

- `PT-3041/gi-note-2026-11-08` (2026-11-08): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3041/gi-note-2026-11-08` (2026-11-08): "Harvey-Bradshaw Index today: 11."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-08-17 is within 12 months before the 2026-11-18 request and describes ulcers, which is active inflammation under option (a). The same report's pathology reads chronic active inflammation. CRP alone was not used for this finding. (confidence 0.92)

- `PT-3041/colonoscopy-2026-08-17` (2026-08-17): "Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in a GI follow-up note dated 2026-11-08, and the request names Dr. A. Rivera, Gastroenterology as ordering provider. The quoted passages do not themselves state the specialty, so the reviewer should confirm the specialty from the provider record. (confidence 0.85)

- `PT-3041/gi-note-2026-11-08` (2026-11-08): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3041/labs-2025-11-29` (2025-11-29): "ORDERING: Dr. A. Rivera"

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 07/12/2000 gives an age of 26 on the 2026-11-18 request date, which is 18 or older. (confidence 0.97)

- `PT-3041/demographics-2026-11-01` (2026-11-01): "Date of birth: 07/12/2000"
- Code checks: age 26 on 2026-11-18 from DOB 2000-07-12

### C5 (policy 3.5): MET
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history records prednisone from 05/2020 to 01/2021 with stop reason documented as steroid dependence, with flares on dose reduction below 15 mg. This meets the steroid-dependence route for conventional therapy failure. The source is a medication history rather than pharmacy claims, so the reviewer should confirm it is treating-provider or prescription-supported. (confidence 0.80)

- `PT-3041/medication-history-2026-11-04` (2026-11-04): "Prednisone | 40 mg daily, tapered | 05/2020 | 01/2021 | Steroid dependent (flared each time the dose went below 15 mg)"

**C5b (policy 3.5(b)): MET**: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history records adalimumab from 07/2023 to 11/2023 stopped for primary non-response, which is an anti-TNF failure. The source is a medication history rather than pharmacy claims, so the reviewer should confirm claims or prescription support. (confidence 0.80)

- `PT-3041/medication-history-2026-11-04` (2026-11-04): "Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON TB Gold Plus result of NEGATIVE was collected 2025-11-29, which is within 12 months before the 2026-11-18 request. The result is determinate and negative. (confidence 0.94)

- `PT-3041/labs-2025-11-29` (2025-11-29): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-09-19. Because both are negative, no monitoring or prophylaxis plan is required by this criterion. (confidence 0.93)

- `PT-3041/labs-2026-09-19` (2026-09-19): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3041/labs-2026-09-19` (2026-09-19): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The reconciled medication history dated 2026-11-04 states there is no current biologic, JAK inhibitor, or S1P receptor modulator. No passage contradicts this, and no switch from another agent is documented. (confidence 0.88)

- `PT-3041/medication-history-2026-11-04` (2026-11-04): "No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 55.0 kg recorded 2026-11-08 is within 30 days of the request and falls in the 55 kg or less band for 260 mg induction. The requested maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the labeling. The older 58.0 kg weight from 2026-05-29 was not used. (confidence 0.90)

- `PT-3041/gi-note-2026-11-08` (2026-11-08): "Weight 55.0 kg."
- `PT-3041/gi-note-2026-11-08` (2026-11-08): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-08) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The chart has no documented trial of either ustekinumab-aekn or ustekinumab-ttwe, so neither inadequate response nor intolerance is recorded. The requested product is itself a preferred product, so the C10 parent path does not depend on this sub-criterion. (confidence 0.75)

- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage in the chart documents a contraindication or hypersensitivity to any excipient. The absence of such documentation is not an affirmative failure, so the status is insufficient evidence rather than not met. (confidence 0.80)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe (who: practice_staff)
  > PA-3041 (patient PT-3041): criterion C10a (policy 3.10(a)) is open. The chart has no record of a trial of ustekinumab-aekn or ustekinumab-ttwe. Please check the chart and any outside records for documented inadequate response or intolerance to each product, and let Dr. Rivera know what you find.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. Intolerance to only one of the two does not satisfy it. The criterion text states no date window, so none is applied here.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > Dr. Rivera, PA-3041 criterion C10b (policy 3.10(b)) is open. The chart has no documented contraindication or hypersensitivity to any excipient shared by ustekinumab-aekn and ustekinumab-ttwe but absent from the requested product. Please review the patient's history and document whether such a contraindication or hypersensitivity exists.
  - Would satisfy the policy: Policy 3.10(b) accepts a documented contraindication or hypersensitivity to an inactive ingredient that is present in both preferred products and absent from ustekinumab-aekn. The criterion text states no date window, so none is applied here.

## Run cost

3 model calls, 22,335 input and 15,206 output tokens, 62.0 s of model time, $0.011 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: borderline.

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
