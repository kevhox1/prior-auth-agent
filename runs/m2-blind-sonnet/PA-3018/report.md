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

The treating GI note diagnoses moderately to severely active ulcerative pancolitis and supports severity with a partial Mayo score and symptom burden. The problem list confirms the diagnosis (K51.00). (confidence 0.96)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ulcerative pancolitis."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Partial Mayo score today: 5."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A flexible sigmoidoscopy dated 2026-08-14, within 12 months of the 2026-11-18 request, describes friability and erosions. This qualifies as active inflammation on endoscopy. (confidence 0.96)

- `PT-3018/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "Rectum to 28 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No passage from the chart states the prescriber's specialty or documents a gastroenterology consultation. The specialty appears only in the request form, not in a quoted chart passage. (confidence 0.60)

- Missing: Signed note or order showing the prescriber's specialty is gastroenterology, or documentation of consultation with a gastroenterologist

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

Date of birth 1971-07-19 makes the member 55 years old at the request date, which is over 18. (confidence 0.98)

- `PT-3018/demographics-2026-10-23` (2026-10-23): "Date of birth: 1971-07-19"
- Code checks: age 55 on 2026-11-18 from DOB 1971-07-19

### C5 (policy 3.5): **CONFLICTING**
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Prednisone is currently listed, but the chart gives no start date, no stop date, and no documented inadequate response, steroid dependence, or intolerance. No azathioprine, 6-MP, methotrexate or mesalamine history is shown. (confidence 0.80)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Prednisone 20 mg daily, taper planned after induction"
- Missing: Conventional therapy (corticosteroid, azathioprine, 6-mercaptopurine, methotrexate, or mesalamine) with approximate start/stop dates and documented inadequate response, intolerance, or contraindication
- Missing: Supporting pharmacy claims, prescription records, or chart notes

**C5b (policy 3.5(b)): **CONFLICTING****: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The 2026-10-31 GI note reports infliximab from 2023-07 to 2026-09, based on patient report. The 2023-11-18 outside records say the patient was biologic-naive and declined infliximab in 2023-07. Nothing in the chart resolves which is correct, and the GI note says outside records were requested. (confidence 0.85)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09."
- `PT-3018/outside-records-2023-11-18` (2023-11-18): "- Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

A negative QuantiFERON result dated 2026-10-04 is within 12 months of the request. (confidence 0.96)

- `PT-3018/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted and nonreactive, so no monitoring plan is required. (confidence 0.96)

- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current GI note states no biologic or small-molecule advanced therapy is in use. The reported prior infliximab ended 2026-09, so there is no concurrent agent. (confidence 0.90)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight of 97.3 kg was documented 18 days before the request, which falls in the over-85 kg band requiring 520 mg IV. Maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the label. (confidence 0.95)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Weight 97.3 kg."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 97.3 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C3**: Signed note or order showing prescriber specialty is gastroenterology (who: practice_staff)
  > PA-3018 (PT-3018), criterion 3.3 (gastroenterologist prescriber): the specialty appears only on the request form, not in a chart passage. Please locate and attach a signed note or order from Dr. M. Chen that shows gastroenterology as the specialty, or documentation of a consultation with a gastroenterologist.
  - Would satisfy the policy: Policy 3.3 accepts a signed chart note or order showing the prescriber is a gastroenterologist, or documentation that the drug is prescribed in consultation with a gastroenterologist.
- **C5a**: Conventional therapy history with dates and documented inadequate response, intolerance, or contraindication (who: ordering_provider)
  > PA-3018 (PT-3018), criterion 3.5(a) (conventional therapy): the 2026-10-31 GI note lists only 'Prednisone 20 mg daily, taper planned after induction', with no start or stop dates and no documented response. Please document approximate start and stop dates and any inadequate response, steroid dependence, or intolerance for prednisone, budesonide, azathioprine, 6-MP, or methotrexate, if any were used. Supporting pharmacy claims or prescription records would help.
  - Would satisfy the policy: Policy 3.5(a) accepts documentation of an inadequate response to (including steroid dependence or steroid-refractory disease), intolerance of, or contraindication to at least one of: systemic corticosteroids (including budesonide), azathioprine, 6-mercaptopurine, or methotrexate. Oral aminosalicylates count only for ulcerative colitis. The request is for K51.00.
- **C5b**: Provider reconciliation of conflicting infliximab history, with source records (who: ordering_provider)
  > PA-3018 (PT-3018), criterion 3.5(b) (anti-TNF): the 2026-10-31 GI note says 'Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09' (per patient report). The 2023-11-18 outside records say 'Biologic-naive. Infliximab was recommended 2023-07 but the patient declined.' Please review both and document which is accurate, including any outside records or fill history you received.
  - Would satisfy the policy: Policy 3.5(b) accepts documented inadequate response (primary non-response or secondary loss of response), intolerance, or a specifically documented contraindication to adalimumab or infliximab, including biosimilars. The documentation must be consistent across the chart.

## Run cost

3 model calls, 21,263 input and 7,133 output tokens, 44.0 s of model time, $0.135 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
