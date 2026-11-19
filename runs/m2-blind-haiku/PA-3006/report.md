# PA-3006: ustekinumab-ttwe for PT-3006

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 90.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI provider's 10/26/2026 note documents moderately to severely active ileocolonic Crohn's disease, supported by a Harvey-Bradshaw Index of 14 and 5-7 stools a day. The problem list confirms the Crohn's diagnosis. (confidence 0.93)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Harvey-Bradshaw Index today: 14."
- `PT-3006/problem-list-2026-10-26` (2026-10-26): "Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A fecal calprotectin of 511 ug/g from 10/05/2026 is within 12 months of the request and is above the lab reference of <50, as reported in the GI note. The primary laboratory report is not in the chart, so the result rests on the provider's transcription; a reviewer may want the lab report attached. (confidence 0.80)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Her calprotectin from 10/05/2026 came back at 511 ug/g (lab reference <50)."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in the GI follow-up note, and the ordering provider is listed as Dr. S. Adeyemi, Gastroenterology. This meets the gastroenterologist prescriber requirement. (confidence 0.90)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3006/labs-2026-09-22` (2026-09-22): "ORDERING: Dr. S. Adeyemi"

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 07/11/1981 makes the member 45 years old on the 2026-11-18 request date, which is over 18. (confidence 0.97)

- `PT-3006/demographics-2026-06-07` (2026-06-07): "Date of birth: 07/11/1981"
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy 3.5): **CONFLICTING**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history documents prednisone 06/2023 to 12/2023 with steroid dependence (flares below 15 mg), and azathioprine 01/2024 to 03/2024 stopped for acute pancreatitis. Either trial satisfies the conventional therapy requirement. The 2024 outside record does not mention these drugs, and the criterion's referral rule for inconsistent records should be considered by the reviewer alongside the adalimumab conflict. (confidence 0.72)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 06/2023 | 12/2023 | Steroid dependent (flared each time the dose went below 15 mg) |"
- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Azathioprine | 2.5 mg/kg daily | 01/2024 | 03/2024 | Intolerance (acute pancreatitis) |"

**C5b (policy 3.5(b)): **CONFLICTING****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history records an adalimumab trial from 05/2024 to 05/2026 stopped for loss of response, based only on patient report. The 10/2024 outside record says the patient was biologic-naive and declined adalimumab, which is incompatible, and nothing in the chart resolves it. (confidence 0.85)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"
- `PT-3006/outside-records-2024-10-18` (2024-10-18): "Biologic-naive. Adalimumab was recommended 05/2024 but the patient declined."
- Missing: Outside adalimumab dispensing or pharmacy records for 05/2024 to 05/2026
- Missing: Treating-provider documentation of adalimumab start and stop dates and reason stopped

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON TB Gold Plus result of NEGATIVE was collected 11/30/2025, which falls within the 12 months before the 2026-11-18 request. (confidence 0.92)

- `PT-3006/labs-2025-11-30` (2025-11-30): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 09/22/2026. No positive result requires a monitoring or prophylaxis plan. (confidence 0.95)

- `PT-3006/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3006/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication reconciliation states there is no current biologic, JAK inhibitor, or S1P modulator. The prior adalimumab is recorded as stopped 05/2026, though that stop date rests on patient report and is disputed under C5b. (confidence 0.80)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The current weight of 90.4 kg is dated 10/26/2026, within 30 days of the request, and falls in the over-85 kg band for a 520 mg induction dose. The requested maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches labeling. (confidence 0.92)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Weight 90.4 kg."
- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 90.4 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): **INSUFFICIENT**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **INSUFFICIENT****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The chart contains no documented trial of either ustekinumab-aekn or ustekinumab-ttwe, so the both-products requirement cannot be assessed. The requested product is itself a preferred product, so the reviewer should confirm whether this exception applies. (confidence 0.70)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Missing: Documented inadequate response or intolerance to ustekinumab-aekn
- Missing: Documented inadequate response or intolerance to ustekinumab-ttwe

**C10b (policy 3.10(b)): **INSUFFICIENT****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No passage documents a contraindication or hypersensitivity to any inactive ingredient. The requested product is itself preferred, so this exception may not apply; the reviewer should confirm. (confidence 0.80)

- Missing: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product

## To-do list (gap plan)

- **C5b**: Reconciled adalimumab treatment history: outside dispensing or pharmacy records for 05/2024 to 05/2026, plus provider documentation of start and stop dates and reason stopped (who: ordering_provider)
  > Criterion 3.5(b) (TNF blocker history) for PT-3006 is CONFLICTING. The 2026-10-22 medication history lists adalimumab 40 mg every 2 weeks from 05/2024 to 05/2026 stopped for loss of response (patient report only), but the 2024-10-18 outside record states the patient was biologic-naive and declined adalimumab. Please review and document the adalimumab start and stop dates and reason stopped, and confirm whether outside adalimumab dispensing records for 05/2024 to 05/2026 are available.
  - Would satisfy the policy: Policy 3.5(b) accepts documented adalimumab or infliximab (including biosimilars) inadequate response, loss of response, intolerance, or a specifically documented contraindication. The provided criterion text sets no lookback date, so the documentation must resolve the 05/2024 to 05/2026 adalimumab trial against the 2024-10-18 record that states the patient declined adalimumab.
- **C10a**: Documented inadequate response or intolerance to ustekinumab-aekn (who: ordering_provider)
  > Criterion 3.10(a) (both preferred ustekinumab products) for PT-3006 is INSUFFICIENT_EVIDENCE. The chart has no documented trial of ustekinumab-aekn, and the requested product ustekinumab-ttwe (2026-10-26 GI note) is itself a preferred product. Please review whether this exception applies and document any prior ustekinumab-aekn trial and outcome if one exists.
  - Would satisfy the policy: Policy 3.10(a) accepts documented inadequate response or intolerance to both ustekinumab-aekn and ustekinumab-ttwe. Intolerance to only one preferred product does not satisfy it. The provided criterion text sets no lookback date.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both ustekinumab-aekn and ustekinumab-ttwe and absent from the requested product (who: ordering_provider)
  > Criterion 3.10(b) (inactive-ingredient contraindication) for PT-3006 is INSUFFICIENT_EVIDENCE. No chart passage documents a contraindication or hypersensitivity to any inactive ingredient. Because the requested product ustekinumab-ttwe is one of the two preferred products, any ingredient present in both would also be present in the requested product, so please review whether this exception applies.

## Run cost

3 model calls, 23,904 input and 17,908 output tokens, 72.9 s of model time, $0.014 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: conflicting.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | - | wrong |
