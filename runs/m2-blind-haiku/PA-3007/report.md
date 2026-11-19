# PA-3007: ustekinumab-ttwe for PT-3007

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 63.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI provider's 2026-11-05 note documents moderately to severely active ileocolonic Crohn's disease with a Harvey-Bradshaw Index of 9. The diagnosis dates to 2021 per the outside records. (confidence 0.90)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3007/gi-note-2026-11-05` (2026-11-05): "Harvey-Bradshaw Index today: 9."

### C2 (policy 3.2): **NOT MET**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy on file is the colonoscopy from 12/2022, which is outside the 12-month lookback before the 2026-11-18 request. The only inflammatory marker on file is a CRP, which the policy says does not satisfy this criterion, and no fecal calprotectin is on file. (confidence 0.70)

- `PT-3007/gi-note-2026-05-13` (2026-05-13): "Last colonoscopy 12/2022 showed active disease."
- `PT-3007/labs-2026-10-03` (2026-10-03): "C REACTIVE PROTEIN ................ 9.1 mg/L  (<5.0)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in the 2026-11-05 GI follow-up note by Dr. S. Adeyemi, who the request lists as Gastroenterology. The 2026-10-03 labs also name Dr. S. Adeyemi as ordering provider. (confidence 0.85)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3007/labs-2026-10-03` (2026-10-03): "ORDERING: Dr. S. Adeyemi"

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 08/01/1980 makes the member 46 years old on the 2026-11-18 request date. The outside records give the same date of birth. (confidence 0.97)

- `PT-3007/demographics-2026-05-23` (2026-05-23): "Date of birth: 08/01/1980"
- Code checks: age 46 on 2026-11-18 from DOB 1980-08-01

### C5 (policy 3.5): MET
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The outside records document methotrexate 25 mg weekly from 06/2021 to 11/2021, stopped for intolerance (nausea and ALT above 3 times the upper limit of normal). The 2026-11-02 reconciled medication history omits methotrexate; that is an omission, not a contradiction, so the reviewer should confirm the 2021 history. (confidence 0.70)

- `PT-3007/outside-records-2021-12-18` (2021-12-18): "Methotrexate 25 mg subcutaneously weekly, 06/2021 to 11/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The reconciled medication history records adalimumab 40 mg every 2 weeks from 07/2023 to 11/2023, stopped for primary non-response. This satisfies the TNF blocker step with a named drug, dates, and stop reason. (confidence 0.85)

- `PT-3007/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus result of NEGATIVE was collected 2026-10-03, within 12 months before the 2026-11-18 request. The result is determinate, not indeterminate. (confidence 0.90)

- `PT-3007/labs-2026-10-03` (2026-10-03): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-10-03. No positive result requires a monitoring or prophylaxis plan. (confidence 0.90)

- `PT-3007/labs-2026-10-03` (2026-10-03): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3007/labs-2026-10-03` (2026-10-03): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The reconciled medication history of 2026-11-02 states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The only current listed agent is budesonide, which is not an excluded class. (confidence 0.85)

- `PT-3007/medication-history-2026-11-02` (2026-11-02): "No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 63.6 kg dated 2026-11-05 is within 30 days of the request, and falls in the more than 55 kg to 85 kg band that takes 390 mg IV. The requested maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the labeling. (confidence 0.90)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "Weight 63.6 kg."
- `PT-3007/gi-note-2026-11-05` (2026-11-05): "Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 63.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): **NOT MET**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **NOT MET****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The requirement needs documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. The reconciled medication history lists no prior trial of either product, so neither failure is documented. (confidence 0.60)

- `PT-3007/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

**C10b (policy 3.10(b)): **NOT MET****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to an inactive ingredient shared by both preferred products. The requested product is itself a preferred product, so this exception is not documented as needed or present. (confidence 0.60)


## To-do list (gap plan)

- **C2**: Endoscopy, colonoscopy, or flexible sigmoidoscopy report showing active inflammation, or a fecal calprotectin above the lab's upper reference limit, dated within the 12 months before the request (who: ordering_provider)
  > Criterion C2 (Policy 3.2) is not met. The only endoscopy on file is the colonoscopy from 12/2022, which is outside the lookback, and the only inflammatory marker is CRP 9.1 mg/L on 2026-10-03, which the policy does not accept. No fecal calprotectin is on file. Please review.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or a fecal calprotectin above the performing lab's upper reference limit, dated on or after 2025-11-18. CRP or ESR alone and imaging alone do not satisfy it.
- **C10a**: Documented inadequate response to, or intolerance of, both ustekinumab-aekn and ustekinumab-ttwe (who: ordering_provider)
  > Criterion C10a (Policy 3.10(a)) is not met. The reconciled medication history lists no prior trial of ustekinumab-aekn or ustekinumab-ttwe, and the only documented failure is adalimumab (primary non-response, 07/2023 to 11/2023). Please review.
  - Would satisfy the policy: Policy 3.10(a) requires documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. Intolerance to only one of the two does not satisfy it. The policy text sets no date window for this item.
- **C10b**: Contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product (who: ordering_provider)
  > Criterion C10b (Policy 3.10(b)) is not met. No note documents a contraindication or hypersensitivity to an inactive ingredient shared by both preferred products. The requested product, ustekinumab-ttwe, is itself a preferred product, so the exception as written cannot apply to it. Please review.

## Run cost

3 model calls, 22,769 input and 15,884 output tokens, 64.0 s of model time, $0.011 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent NEEDS_PHYSICIAN. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | INSUFFICIENT_EVIDENCE | NOT_MET | NOT_MET | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | NOT_MET | - | wrong |
