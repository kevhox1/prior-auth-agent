# PA-3018: ustekinumab-ttwe for PT-3018

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 97.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI provider documents ulcerative pancolitis with moderately to severely active disease on 2026-10-31, supported by a partial Mayo score of 5 and 5-7 stools a day with urgency. The diagnosis matches the requested ICD-10 K51.00 on the active problem list. (confidence 0.92)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ulcerative pancolitis."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Partial Mayo score today: 5."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A flexible sigmoidoscopy dated 2026-08-14 falls within 12 months before the 2026-11-18 request and describes friability and erosions, which is active inflammation under part (a). The CRP result is not relied on. (confidence 0.93)

- `PT-3018/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "Rectum to 28 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in a gastroenterology follow-up note, and the request names Dr. M. Chen, Gastroenterology as ordering provider. The gastroenterologist authorship rests on the document header, which was not included in the quoted text. (confidence 0.85)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Submit prior authorization to Northfield."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth of 1971-07-19 makes the member 55 years old on the 2026-11-18 request date, which is above the age-18 threshold. (confidence 0.97)

- `PT-3018/demographics-2026-10-23` (2026-10-23): "Date of birth: 1971-07-19"
- Code checks: age 55 on 2026-11-18 from DOB 1971-07-19

### C5 (policy 3.5): **CONFLICTING**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The chart shows current prednisone use, but it does not document a prior conventional therapy course with dates and reason stopped. There is no documented steroid dependence, steroid-refractory disease, or intolerance to any conventional agent. (confidence 0.80)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Prednisone 20 mg daily, taper planned after induction"
- Missing: Prior conventional therapy course records (agent, start and stop dates) for systemic corticosteroid, azathioprine, 6-mercaptopurine, methotrexate, or oral aminosalicylate
- Missing: Documentation of inadequate response, intolerance, or contraindication to that conventional agent
- Missing: For corticosteroid failure: documentation of steroid dependence (relapse during taper or within 3 months of stopping) or steroid-refractory disease

**C5b (policy 3.5(b)): **CONFLICTING****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The 2026 GI note reports an infliximab trial from 2023-07 to 2026-09 stopped for loss of response. The 2023 outside record says the patient was biologic-naive and declined infliximab in 2023-07. The chart does not resolve which account is correct, and the stop reason rests on patient report with outside records still requested. (confidence 0.85)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-3018/outside-records-2023-11-18` (2023-11-18): "Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus result of negative is dated 2026-10-04, within 12 months before the 2026-11-18 request. It is a determinate negative, not an indeterminate result. (confidence 0.93)

- `PT-3018/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-10-04. No lookback applies, and no positive result requires a monitoring plan. (confidence 0.92)

- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The 2026-10-31 GI note states there is no current biologic or small-molecule advanced therapy. The listed current medications are prednisone and omeprazole, with no JAK inhibitor or S1P modulator. (confidence 0.88)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "No biologic or small-molecule advanced therapy at present."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Omeprazole 20 mg daily"

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The current weight of 97.3 kg was recorded 2026-10-31, within 30 days of the request. The requested 520 mg IV induction matches the above-85 kg band, and the 90 mg SC every 8 weeks maintenance starts 8 weeks after the IV dose. (confidence 0.90)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Weight 97.3 kg."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 97.3 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The chart contains no documented inadequate response or intolerance to ustekinumab-aekn or to ustekinumab-ttwe. The requested product is itself a preferred product, so this sub-criterion's outcome depends on how the plan applies it. (confidence 0.80)

- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No contraindication or hypersensitivity to an inactive ingredient is documented anywhere in the passages. The requested product is preferred, so this exception is not needed for the request as written. (confidence 0.85)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C5a**: Prior conventional therapy course records (agent, start and stop dates, reason stopped) for systemic corticosteroid, azathioprine, 6-MP, methotrexate, or oral aminosalicylate, plus documentation of inadequate response, intolerance, or contraindication (who: ordering_provider)
  > Criterion C5a (policy 3.5(a)) is open for PT-3018. The chart shows prednisone 20 mg daily in the 2026-10-31 GI note, but no prior conventional therapy course with start and stop dates or a reason stopped. Please review and document any prior course of a corticosteroid, azathioprine, 6-MP, methotrexate, or oral aminosalicylate, including steroid dependence or steroid-refractory disease if applicable.
  - Would satisfy the policy: Policy 3.5(a) accepts a dated record of a prior course of a listed conventional agent (systemic corticosteroid, azathioprine, 6-mercaptopurine, methotrexate, or, for ulcerative colitis, an oral aminosalicylate such as mesalamine) showing an inadequate response, intolerance, or contraindication. For corticosteroids, steroid dependence (relapse during taper or within 3 months of stopping) or steroid-refractory disease also qualifies. The criterion sets no look-back date window.
- **C5b**: Outside records that resolve the conflict on infliximab history: confirmed infliximab trial dates (2023-07 to 2026-09) and stop reason (loss of response), or confirmation of biologic-naive status (who: ordering_provider)
  > Criterion C5b (policy 3.5(b)) is in conflict for PT-3018. The 2026-10-31 GI note records an infliximab trial from 2023-07 to 2026-09 stopped for loss of response, but the 2023-11-18 outside record states the patient was biologic-naive and declined infliximab. Please review the outside records once received and document which account is correct, with the stop reason if infliximab was given.
  - Would satisfy the policy: Policy 3.5(b) accepts documentation of an inadequate response, intolerance, or contraindication to adalimumab or infliximab (including biosimilars), such as primary non-response, secondary loss of response, or intolerance, with the record resolving the conflicting accounts. A contraindication must be specifically documented. The criterion sets no look-back date window.
- **C10a**: Documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe (intolerance to only one does not satisfy this requirement) (who: ordering_provider)
  > Criterion C10a (policy 3.10(a)) is open for PT-3018. The chart documents no inadequate response or intolerance to ustekinumab-aekn or ustekinumab-ttwe, and the requested product is ustekinumab-ttwe. Please confirm whether the patient has any prior ustekinumab exposure and document it, or indicate how this criterion applies to this request.
  - Would satisfy the policy: Policy 3.10(a) accepts documentation of an inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. Intolerance to only one of the two preferred products does not satisfy the criterion. The criterion sets no look-back date window.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > Criterion C10b (policy 3.10(b)) is open for PT-3018. No hypersensitivity or contraindication to an inactive ingredient is documented, and the requested product ustekinumab-ttwe is itself one of the two preferred products, so this exception may not apply as written. Please review and document whether any such contraindication exists, or confirm that this exception is not being relied on.

## Run cost

3 model calls, 24,201 input and 15,649 output tokens, 63.5 s of model time, $0.012 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
