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

The treating GI note diagnoses moderately to severely active Crohn's disease and gives a Harvey-Bradshaw Index of 11. The problem list also carries the Crohn's diagnosis. (confidence 0.96)

- `PT-3041/gi-note-2026-11-08` (2026-11-08): "A:
- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3041/gi-note-2026-11-08` (2026-11-08): "- Harvey-Bradshaw Index today: 11."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The 08/17/2026 colonoscopy describes ulceration, which is active inflammation. It falls within 12 months before the 11/18/2026 request. (confidence 0.96)

- `PT-3041/colonoscopy-2026-08-17` (2026-08-17): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No passage from the chart states the prescriber's specialty. The request lists Gastroenterology, but the chart passages do not confirm it. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty as gastroenterology, or a gastroenterology consultation note

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 07/12/2000 makes the member 26 at the request date, which is over 18. (confidence 0.98)

- `PT-3041/demographics-2026-11-01` (2026-11-01): "Date of birth: 07/12/2000"
- Code checks: age 26 on 2026-11-18 from DOB 2000-07-12

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history names prednisone with start and stop dates and documents steroid dependence, which qualifies as inadequate response. Nothing in the passages contradicts it. (confidence 0.85)

- `PT-3041/medication-history-2026-11-04` (2026-11-04): "| Prednisone | 40 mg daily, tapered | 05/2020 | 01/2021 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The chart medication history names adalimumab with start and stop dates and primary non-response, which qualifies. No claims are in the passages, but no record contradicts the history. (confidence 0.80)

- `PT-3041/medication-history-2026-11-04` (2026-11-04): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

The negative QuantiFERON was dated 11/29/2025. That is inside the 12-month window, which begins 11/18/2025. (confidence 0.90)

- `PT-3041/labs-2025-11-29` (2025-11-29): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted and nonreactive, so no monitoring plan is needed. (confidence 0.97)

- `PT-3041/labs-2026-09-19` (2026-09-19): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3041/labs-2026-09-19` (2026-09-19): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication list shows no biologic, JAK inhibitor, or S1P modulator, so there is no concurrent excluded agent. (confidence 0.92)

- `PT-3041/medication-history-2026-11-04` (2026-11-04): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The 55.0 kg weight is dated 11/08/2026, within 30 days of the request. 260 mg IV matches the 55 kg or less band, and maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose. (confidence 0.95)

- `PT-3041/gi-note-2026-11-08` (2026-11-08): "- Weight 55.0 kg."
- `PT-3041/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-08) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-aekn, which is a preferred product, so no exception is needed. (confidence 0.97)

- `PT-3041/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C3**: Documentation of prescriber's gastroenterology specialty or GI consultation note (who: practice_staff)
  > For PA-3041 (PT-3041, ustekinumab-aekn), criterion C3 (policy 3.3) requires the prescriber to be a gastroenterologist or to be prescribing in consultation with one. The request lists Dr. A. Rivera, Gastroenterology, but the chart passages do not confirm the specialty. Could you locate and file chart documentation of Dr. Rivera's specialty (e.g., a signed note with credentials or specialty) or a gastroenterology consultation note?
  - Would satisfy the policy: Policy 3.3 accepts chart documentation that the prescriber's specialty is gastroenterology, or a gastroenterology consultation note, supporting prescribing by or in consultation with a gastroenterologist.

## Run cost

3 model calls, 19,633 input and 5,539 output tokens, 34.5 s of model time, $0.113 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: borderline.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
