# PA-3004: ustekinumab-aekn for PT-3004

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

The treating GI provider's 2026-10-31 note documents moderately to severely active ileocolonic Crohn's disease with a Harvey-Bradshaw Index of 12. The problem list confirms the Crohn's diagnosis. The 2026-08-16 colonoscopy also has SES-CD 10, which supports the severity. (confidence 0.90)

- `PT-3004/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3004/gi-note-2026-10-31` (2026-10-31): "Harvey-Bradshaw Index today: 12."
- `PT-3004/problem-list-2026-10-31` (2026-10-31): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-08-16 is within 12 months before the 2026-11-18 request and describes ulceration, which is active inflammation under part (a). The same-day pathology also reports chronic active inflammation. CRP alone would not count, but the endoscopy report is sufficient. (confidence 0.90)

- `PT-3004/colonoscopy-2026-08-16` (2026-08-16): "Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3004/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order plan is in a gastroenterology follow-up note, and the request lists Dr. A. Rivera, Gastroenterology as the ordering provider. The quoted line itself does not name the prescriber, so the match depends on the note's GI authorship. (confidence 0.80)

- `PT-3004/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 2000-04-27 makes the member 26 years old on the 2026-11-18 request date, which is above the 18-year minimum. The outside record shows the same DOB. (confidence 0.95)

- `PT-3004/demographics-2026-02-05` (2026-02-05): "Date of birth: 2000-04-27"
- Code checks: age 26 on 2026-11-18 from DOB 2000-04-27

### C5 (policy 3.5): **INSUFFICIENT**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The reconciliation lists prednisone with dates and steroid dependence, but it was compiled by an RN from history and no pharmacy claims or treating-provider note confirm the course. The outside transfer summary has no treatment history entries, and the 2026-10-31 GI note refers to 'current therapy' without naming it, so the step-therapy history is not yet supported by qualifying records. (confidence 0.60)

- `PT-3004/medication-history-2026-10-29` (2026-10-29): "| Prednisone | 40 mg daily, tapered | 2023-05 | 2024-01 | Steroid dependent (flared each time the dose went below 15 mg) |"
- Missing: Pharmacy claims or prescription records confirming the prednisone course from about 2023-05 to 2024-01
- Missing: Treating-provider note documenting steroid dependence (relapse during taper), or the complete outside treatment history (fax pages 1 and 3 of the outside records)

**C5b (policy 3.5(b)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The reconciliation names infliximab, gives dates from 2024-03 to 2026-09, and states intolerance (drug-induced lupus). That history was compiled by an RN without pharmacy or infusion records, and the outside summary has no treatment entries, so it is not yet supported by the records the policy requires. (confidence 0.60)

- `PT-3004/medication-history-2026-10-29` (2026-10-29): "| Infliximab | 5 mg/kg IV every 8 weeks | 2024-03 | 2026-09 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"
- Missing: Infusion or pharmacy records confirming infliximab 2024-03 to 2026-09
- Missing: Treating-provider note documenting the drug-induced lupus intolerance and the positive anti-histone antibody result

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus collected 2026-09-20 is negative and falls within the 12 months before the request. No indeterminate result or positive screen is documented. (confidence 0.90)

- `PT-3004/labs-2026-09-20` (2026-09-20): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc have resulted as nonreactive on 2026-09-20. Because both are negative, no monitoring or prophylaxis plan is required. (confidence 0.90)

- `PT-3004/labs-2026-09-20` (2026-09-20): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3004/labs-2026-09-20` (2026-09-20): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-10-29 medication reconciliation documents no current biologic, JAK inhibitor, or S1P modulator. The 2026-10-31 GI note's 'current therapy' wording does not name an agent, so it does not contradict this. (confidence 0.80)

- `PT-3004/medication-history-2026-10-29` (2026-10-29): "No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The 2026-10-31 weight of 55.0 kg is within 30 days of the request, and 55.0 kg falls in the 260 mg IV induction band. The requested maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches labeling. (confidence 0.90)

- `PT-3004/gi-note-2026-10-31` (2026-10-31): "Weight 55.0 kg."
- `PT-3004/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-31) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The chart describes ustekinumab-aekn as a new start and documents no prior trial of either preferred product. The criterion requires documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe, and neither is recorded. (confidence 0.70)

- `PT-3004/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No document in the passages records a contraindication or hypersensitivity to an inactive ingredient shared by both preferred products and absent from the requested product. The chart is silent on this, so the requirement cannot be assessed as met or failed. (confidence 0.70)

- `PT-3004/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C5a**: Pharmacy claims or prescription records confirming the prednisone course (about 2023-05 to 2024-01), or the treating-provider note documenting steroid dependence (who: pharmacy)
  > Criterion 3.5(a) (conventional therapy) is open for PT-3004. Please request pharmacy claims or prescription records confirming the prednisone course from about 2023-05 to 2024-01, which the 2026-10-29 medication reconciliation lists as steroid dependent. The outside transfer summary's treatment history (fax pages 1 and 3) would also help if pharmacy records are unavailable.
  - Would satisfy the policy: Policy 3.5(a) accepts a corticosteroid course with inadequate response, including steroid dependence (relapse during taper or within 3 months of stopping) or steroid-refractory disease. The reconciliation records relapse each time the dose fell below 15 mg during the taper, and this needs confirmation by pharmacy records or a treating-provider note. The criterion text sets no separate date window for this history.
- **C5b**: Infusion or pharmacy records confirming infliximab from 2024-03 to 2026-09, plus treating-provider documentation of the drug-induced lupus intolerance and positive anti-histone antibodies (who: outside_provider)
  > Criterion 3.5(b) (TNF blocker) is open for PT-3004. Please request infusion or pharmacy records from the infusing site confirming infliximab 5 mg/kg IV every 8 weeks from 2024-03 to 2026-09, as listed in the 2026-10-29 medication reconciliation. Please also confirm the treating provider's note documents the drug-induced lupus intolerance and the positive anti-histone antibody result.
  - Would satisfy the policy: Policy 3.5(b) accepts intolerance to infliximab, which is documented as drug-induced lupus with positive anti-histone antibodies and arthralgias. The intolerance must be supported by the infusion or pharmacy record of the infliximab course and by a treating-provider note that documents the intolerance. The criterion text sets no separate date window for this history.
- **C10a**: Documented inadequate response or intolerance to ustekinumab-aekn, and documented inadequate response or intolerance to ustekinumab-ttwe (who: ordering_provider)
  > Criterion 3.10(a) (preferred ustekinumab products) is not met for PT-3004. The 2026-10-31 GI note records ustekinumab-aekn as a new start, and no prior trial of either ustekinumab-aekn or ustekinumab-ttwe is documented. Please review and document whether the patient has had an inadequate response or intolerance to both preferred products.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. Intolerance to only one preferred product does not satisfy the criterion. The criterion text sets no date window for these trials.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > Criterion 3.10(b) (inactive ingredient contraindication or hypersensitivity) is open for PT-3004. The 2026-10-31 GI note does not record any contraindication or hypersensitivity to an inactive ingredient shared by both preferred products. Please review and document whether the patient has such a contraindication or hypersensitivity, if one applies.
  - Would satisfy the policy: Policy 3.10(b) accepts a documented contraindication or hypersensitivity to an inactive ingredient that is present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product ustekinumab-aekn. The criterion text sets no date window for this documentation.

## Run cost

3 model calls, 24,957 input and 20,428 output tokens, 83.3 s of model time, $0.015 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: borderline.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C5b | 3.5(b) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
