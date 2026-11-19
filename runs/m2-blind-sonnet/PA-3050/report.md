# PA-3050: ustekinumab-ttwe for PT-3050

**Outcome: READY_FOR_REVIEW**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 66.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses moderately to severely active Crohn's disease and supports it with a Harvey-Bradshaw Index of 14. The problem list also carries the Crohn's diagnosis. (confidence 0.96)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "A:
- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Harvey-Bradshaw Index today: 14."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A colonoscopy on 2026-10-11 describes ulcers, and fecal calprotectin on 2026-09-12 is 1198 against a reference of <50. Both fall within 12 months of the request, and either one satisfies the criterion. (confidence 0.97)

- `PT-3050/colonoscopy-2026-10-11` (2026-10-11): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-3050/labs-2026-09-12` (2026-09-12): "Calprotectin, fecal | 1198 ug/g | H | <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in the GI follow-up progress note of 2026-11-04. The request lists the ordering provider as Gastroenterology. (confidence 0.80)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 1996-02-13 makes the member 30 years old at the request date, so over 18. (confidence 0.98)

- `PT-3050/demographics-2026-10-23` (2026-10-23): "Date of birth: 1996-02-13"
- Code checks: age 30 on 2026-11-18 from DOB 1996-02-13

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history names mercaptopurine and budesonide, each with start and stop dates and a reason stopped (inadequate response). Both are conventional therapies, and nothing in the chart contradicts this history. (confidence 0.90)

- `PT-3050/medication-history-2026-10-31` (2026-10-31): "| Mercaptopurine | 1.5 mg/kg daily | 2022-08 | 2023-03 | Inadequate response after 6 months at a therapeutic metabolite level |"
- `PT-3050/medication-history-2026-10-31` (2026-10-31): "| Budesonide | 9 mg daily | 2023-04 | 2023-07 | Inadequate response after 10 weeks |"

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

Adalimumab is documented with dates (2023-09 to 2026-07) and a stated reason stopped, intolerance from drug-induced lupus. Intolerance qualifies, and nothing in the chart contradicts it. (confidence 0.90)

- `PT-3050/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

A resulted QuantiFERON on 2026-09-12 is negative, within 12 months of the 2026-11-18 request. (confidence 0.96)

- `PT-3050/labs-2026-09-12` (2026-09-12): "QuantiFERON-TB Gold Plus | NEGATIVE | - | Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive. Neither is positive, so no monitoring plan is needed. (confidence 0.96)

- `PT-3050/labs-2026-09-12` (2026-09-12): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3050/labs-2026-09-12` (2026-09-12): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history states no biologic, JAK inhibitor or S1P modulator is in use. The prior adalimumab was stopped in 2026-07. (confidence 0.92)

- `PT-3050/medication-history-2026-10-31` (2026-10-31): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-3050/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight of 66.0 kg was recorded on 2026-11-04, 14 days before the request, and falls in the 390 mg band (over 55 kg up to 85 kg). Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.95)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Weight 66.0 kg."
- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.0 kg (2026-11-04) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-3050/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## Run cost

2 model calls, 17,564 input and 6,049 output tokens, 34.4 s of model time, $0.116 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: clean.

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
| C10 | 3.10 | MET | MET | MET | ok |
