# PA-3080: ustekinumab-aekn for PT-3080

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: EXPEDITED review. Pharmacy-benefit phase: decision within 24 hours of a complete request (policy section 7). Prescriber statement of clinical urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 104.9 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI's 2026-10-26 note documents moderately to severely active ulcerative pancolitis, with a Partial Mayo score of 7 recorded the same day. This meets the diagnosis and provider-described severity requirement. (confidence 0.90)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ulcerative pancolitis."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Partial Mayo score today: 7."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A fecal calprotectin of 64 ug/g dated 2026-09-10 is above the reference upper limit of <50, and it falls within 12 months before the 2026-11-18 request. The 2023 sigmoidoscopy is outside the lookback and is not relied on here. (confidence 0.90)

- `PT-3080/labs-2026-09-10` (2026-09-10): "CALPROTECTIN FECAL ................ 64 ug/g  (<50)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The GI follow-up note from 2026-10-26 contains the ustekinumab start order, and the request names Dr. S. Adeyemi, Gastroenterology, as ordering provider. The gastroenterology specialty comes from the request form rather than a quoted passage, which is why confidence is not higher. (confidence 0.80)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3080/labs-2026-09-10` (2026-09-10): "ORDERING: Dr. S. Adeyemi"

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 2000-10-17 gives an age of 26 on the 2026-11-18 request date, which satisfies the 18-or-older requirement. (confidence 0.97)

- `PT-3080/demographics-2025-11-27` (2025-11-27): "Date of birth: 2000-10-17"
- Code checks: age 26 on 2026-11-18 from DOB 2000-10-17

### C5 (policy 3.5): **INSUFFICIENT**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The chart contains no documented trial of a corticosteroid, budesonide, azathioprine, 6-MP, methotrexate, or aminosalicylate with dates and reason for stopping. The 'No steroids at present' line reflects current status only, and the request's statement that the flare is 'on steroids' is not supported by the chart. (confidence 0.80)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "No steroids at present"
- Missing: Dated record of a conventional therapy trial (systemic corticosteroid, budesonide, azathioprine, 6-MP, methotrexate, or oral aminosalicylate) with start and stop dates and reason stopped
- Missing: Documentation of steroid dependence or steroid-refractory disease, if corticosteroid failure is the basis
- Missing: Clarification of whether the flare is currently being treated with steroids, since the 2026-10-24 medication history says no steroids

**C5b (policy 3.5(b)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history lists an adalimumab trial from 2023-07 to 2026-05 stopped for intolerance, which would satisfy the TNF step if supported. However, the lupus basis has no supporting anti-histone lab or claims record in the chart, and the 2026-10-26 note refers to unnamed 'current therapy' while the medication history lists none, so the record needs review before this can be accepted. (confidence 0.60)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Symptoms not controlled on current therapy; missing work."
- Missing: Anti-histone antibody lab result or other supporting record for the drug-induced lupus intolerance
- Missing: Pharmacy or claims record for the adalimumab trial dates
- Missing: Clarification of the 'current therapy' referenced in the 2026-10-26 GI note

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON TB Gold Plus result of NEGATIVE dated 2026-09-10 is within the 12 months before the request. The 2023 QuantiFERON mentioned in the 2026-10-26 note is outside the window and is not relied on. (confidence 0.93)

- `PT-3080/labs-2026-09-10` (2026-09-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-09-10. With both negative, no monitoring or prophylaxis plan is required, and the criterion has no lookback limit. (confidence 0.93)

- `PT-3080/labs-2026-09-10` (2026-09-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3080/labs-2026-09-10` (2026-09-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): **INSUFFICIENT**
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-10-24 medication history lists no concurrent biologic, JAK inhibitor, or S1P modulator. The 2026-10-26 GI note refers to an unnamed 'current therapy', which should be clarified before confirming there is no concurrent excluded agent. (confidence 0.60)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "No biologic or small-molecule advanced therapy at present."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Symptoms not controlled on current therapy; missing work."
- Missing: Clarification of the unnamed 'current therapy' referenced in the 2026-10-26 GI note, confirming no concurrent biologic, JAK inhibitor, or S1P modulator

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 104.9 kg recorded 2026-10-26 is within 30 days of the request and falls in the more than 85 kg band, which corresponds to 520 mg IV induction. The requested 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the labeled maintenance schedule. (confidence 0.90)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Weight 104.9 kg."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 104.9 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **NOT MET****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The chart documents no inadequate response or intolerance to ustekinumab-aekn or ustekinumab-ttwe, and the reconciled medication history shows no prior ustekinumab. This sub-criterion is only needed for non-preferred products; the requested product, ustekinumab-aekn, is itself preferred. (confidence 0.70)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "No biologic or small-molecule advanced therapy at present."

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to an inactive ingredient. This exception is only needed for a non-preferred product, and the requested product is preferred, so it is not the basis for this request. (confidence 0.70)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (only if a non-preferred product were requested)

## To-do list (gap plan)

- **C5a**: Dated record of a conventional therapy trial (systemic corticosteroid, budesonide, azathioprine, 6-MP, methotrexate, or oral aminosalicylate) with start and stop dates and reason stopped, or documentation of steroid dependence or steroid-refractory disease (who: ordering_provider)
  > Criterion C5a (policy 3.5(a)) is not met. The 2026-10-24 medication history says 'No steroids at present', and the request describes the flare as 'on steroids'. Please review and document any prior conventional therapy trial with start and stop dates and reason stopped, or steroid dependence or steroid-refractory disease, and clarify whether steroids are currently being given.
  - Would satisfy the policy: Policy 3.5(a) accepts a dated trial of a listed conventional therapy showing an inadequate response, intolerance, or contraindication. For corticosteroids, it accepts steroid dependence (relapse during taper or within 3 months of stopping) or steroid-refractory disease. Budesonide counts as a corticosteroid.
- **C5b**: Anti-histone antibody result or other supporting record for the drug-induced lupus intolerance to adalimumab, pharmacy or claims record for the 2023-07 to 2026-05 adalimumab trial, and clarification of the 'current therapy' in the 2026-10-26 GI note (who: ordering_provider)
  > Criterion C5b (policy 3.5(b)) has insufficient evidence. The 2026-10-24 medication history lists adalimumab 2023-07 to 2026-05 stopped for drug-induced lupus with positive anti-histone antibodies, but no lab result or claims record is in the chart. The 2026-10-26 GI note says 'Symptoms not controlled on current therapy' while the medication history lists no current therapy; please review and clarify, and attach the anti-histone result and adalimumab dispensing or claims dates if available.
  - Would satisfy the policy: Policy 3.5(b) accepts a documented adalimumab or infliximab (including biosimilar) trial with inadequate response, loss of response, or intolerance. Intolerance must be supported by the chart. A contraindication must be specifically documented, such as demyelinating disease or moderate to severe heart failure.
- **C8**: Clarification of the unnamed 'current therapy' in the 2026-10-26 GI note, confirming no concurrent biologic, JAK inhibitor, or S1P receptor modulator (who: ordering_provider)
  > Criterion C8 (policy 3.8) has insufficient evidence. The 2026-10-24 medication history says 'No biologic or small-molecule advanced therapy at present', but the 2026-10-26 GI note says 'Symptoms not controlled on current therapy' without naming the therapy. Please review and document the agent referred to, and confirm that no biologic, JAK inhibitor, or S1P modulator is being used with ustekinumab.
  - Would satisfy the policy: Policy 3.8 accepts a record confirming that no biologic, JAK inhibitor, or S1P receptor modulator is being used with ustekinumab. If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped.
- **C10a**: Inadequate response or intolerance to both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Not required for this request because the requested product is preferred. (who: ordering_provider)
  > Criterion C10a (policy 3.10(a)) is marked not met, with no prior ustekinumab in the chart. The request is for ustekinumab-aekn, which is a preferred product, so this sub-criterion appears not to apply. Please confirm whether it applies to this request, since no documentation is requested unless you believe it does.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. This applies only to non-preferred products.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Not required for this request because the requested product is preferred. (who: ordering_provider)
  > Criterion C10b (policy 3.10(b)) has insufficient evidence, and no inactive-ingredient contraindication or hypersensitivity is documented. The request is for ustekinumab-aekn, a preferred product, so this exception appears not to apply. Please confirm whether it applies to this request.
  - Would satisfy the policy: Policy 3.10(b) accepts a documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product. This applies only to non-preferred products.

## Run cost

3 model calls, 25,750 input and 21,935 output tokens, 90.7 s of model time, $0.015 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
