# PA-3096: ustekinumab-ttwe for PT-3096

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 101.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI's 2026-11-03 note documents moderately to severely active ileocolonic Crohn's disease, with symptom burden and a Harvey-Bradshaw Index of 13. The problem list also records Crohn's disease since 2019, and the 2026-08-16 colonoscopy reports an SES-CD of 10. (confidence 0.90)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-08-16 is within 12 months before the 2026-11-18 request. It describes ulcers in the terminal ileum, which is active inflammation, and biopsy shows chronic active inflammation. (confidence 0.90)

- `PT-3096/colonoscopy-2026-08-16` (2026-08-16): "Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3096/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The 2026-11-03 GI follow-up note orders the drug, and the request names Dr. S. Adeyemi of Gastroenterology as ordering provider. The chart does not state Dr. Adeyemi's specialty in the quoted passages, so a reviewer should confirm the gastroenterology credential. (confidence 0.85)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3096/labs-2026-10-13` (2026-10-13): "ORDERING: Dr. S. Adeyemi"

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 2006-05-08 makes the member 20 years old on the 2026-11-18 request date, which meets the age 18 or older requirement. (confidence 0.95)

- `PT-3096/demographics-2026-05-27` (2026-05-27): "Date of birth: 2006-05-08"
- Code checks: age 20 on 2026-11-18 from DOB 2006-05-08

### C5 (policy 3.5): **INSUFFICIENT**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The chart shows current prednisone use with a planned taper but no start or stop dates, no documented inadequate response, and no steroid dependence or refractoriness. No azathioprine, 6-mercaptopurine, methotrexate, or aminosalicylate trial is documented. (confidence 0.80)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Prednisone 20 mg daily, taper planned after induction"
- Missing: Dates and outcome of prior systemic corticosteroid course(s), including relapse during taper or within 3 months of stopping, or steroid-refractory disease
- Missing: Documentation of any azathioprine, 6-mercaptopurine, or methotrexate trial with start and stop dates and reason stopped (or oral aminosalicylate for ulcerative colitis, not applicable here)
- Missing: Pharmacy or claims records supporting the conventional therapy history

**C5b (policy 3.5(b)): MET**: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The treating GI specifically documents that anti-TNF agents are contraindicated because of demyelinating disease, and the problem list records relapsing-remitting multiple sclerosis. This satisfies the specifically documented contraindication path; the parent C5 still depends on the conventional therapy history in C5a. (confidence 0.85)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3096/problem-list-2026-11-03` (2026-11-03): "Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy 3.6): **NOT MET**
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

The only TB screening result on file is a negative QuantiFERON dated 2025-10-20, about 13 months before the 2026-11-18 request. That falls outside the 12-month lookback, and no later TB test appears in the passages. (confidence 0.85)

- `PT-3096/labs-2025-10-20` (2025-10-20): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Resulted HBsAg (nonreactive) and total anti-HBc (reactive) are on file from 2026-10-13. Because anti-HBc is positive, the GI note documents a monitoring plan of HBV DNA and liver tests every 3 months; the phrase 'on therapy' is ambiguous and a reviewer may want to confirm the plan. (confidence 0.80)

- `PT-3096/labs-2026-10-13` (2026-10-13): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3096/labs-2026-10-13` (2026-10-13): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-11-03 GI note states there is no current biologic or small-molecule advanced therapy, and the listed medications (prednisone and omeprazole) include no excluded agent. The member is not switching from a prior biologic, JAK inhibitor, or S1P modulator. (confidence 0.90)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "No biologic or small-molecule advanced therapy at present."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Omeprazole 20 mg daily"

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 101.7 kg was recorded on 2026-11-03, 15 days before the request, which is within 30 days. The requested 520 mg IV induction matches the over-85 kg band, and the 90 mg SC every 8 weeks maintenance starting 8 weeks after IV dose matches labeling. (confidence 0.90)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Weight 101.7 kg."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 101.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The requested product, ustekinumab-ttwe, is a preferred product, so this exception is only needed if the request were treated as non-preferred. The chart contains no prior ustekinumab exposure, so there is no documented inadequate response or intolerance to either ustekinumab-aekn or ustekinumab-ttwe. (confidence 0.70)

- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to an inactive ingredient shared by both preferred ustekinumab products. The chart is silent on excipient hypersensitivity. (confidence 0.80)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C5a**: Dates and outcome of prior systemic corticosteroid course(s), including any relapse during taper or within 3 months of stopping, or steroid-refractory disease (who: ordering_provider)
  > Criterion C5a (policy 3.5(a)) needs the prior systemic corticosteroid history. The chart shows only 'Prednisone 20 mg daily, taper planned after induction' from the 2026-11-03 GI note, with no start or stop dates. Please review and document the prior steroid course dates and outcome, including any relapse during taper or within 3 months of stopping, or steroid-refractory disease, if applicable.
  - Would satisfy the policy: Policy 3.5(a) accepts documented dates and outcome of a prior systemic corticosteroid course (budesonide counts) showing an inadequate response, including relapse during taper or within 3 months of stopping, or steroid-refractory disease. The policy text sets no date window for this history. Alternatively, documented azathioprine, 6-mercaptopurine, or methotrexate use with start and stop dates and reason stopped would satisfy this criterion.
- **C6**: Negative TB screening test (QuantiFERON or tuberculin skin test) dated on or after 2025-11-18 (who: ordering_provider)
  > Criterion C6 (policy 3.6) is not met. The only TB screen on file is the negative 'QUANTIFERON TB GOLD PLUS' dated 2025-10-20, which is about 13 months before the 2026-11-18 request and outside the 12-month lookback. Please review this criterion and document a current TB screening result if one exists.
  - Would satisfy the policy: Policy 3.6 accepts a negative interferon-gamma release assay or tuberculin skin test dated on or after 2025-11-18 (12 months before the request date). An indeterminate IGRA does not count as negative.
- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe (who: ordering_provider)
  > Criterion C10a (policy 3.10(a)) is open because the chart has no prior ustekinumab exposure. Policy 3.10(a) applies only if the request is treated as non-preferred, and ustekinumab-ttwe is listed as a preferred product. Please confirm that the request is being reviewed as preferred so this exception is not needed.
  - Would satisfy the policy: Policy 3.10(a) applies only to non-preferred products. Because the requested product, ustekinumab-ttwe, is preferred, this exception is not needed for this request. If the request were treated as non-preferred, the policy would require documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > Criterion C10b (policy 3.10(b)) is open because the chart has no documented hypersensitivity to an excipient shared by both preferred ustekinumab products. Since ustekinumab-ttwe is a preferred product, this exception appears to apply only if the request is treated as non-preferred. Please confirm which review pathway applies and document any relevant excipient hypersensitivity if one exists.
  - Would satisfy the policy: Policy 3.10(b) accepts documented contraindication or hypersensitivity to an inactive ingredient that is present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product. The policy sets no date window. Because the requested product is preferred, this exception is needed only if the request is treated as non-preferred.

## Run cost

3 model calls, 24,116 input and 17,358 output tokens, 69.0 s of model time, $0.013 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
