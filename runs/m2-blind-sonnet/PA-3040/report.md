# PA-3040: ustekinumab-ttwe for PT-3040

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 106.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI documents Crohn's disease described as moderately to severely active. A Harvey-Bradshaw Index of 12 supports the severity. (confidence 0.96)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Harvey-Bradshaw Index today: 12."

### C2 (policy 3.2): **INSUFFICIENT**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only colonoscopy cited is from 2022-12, outside the 12-month window. CRP alone does not satisfy the criterion, and no fecal calprotectin is in the passages. (confidence 0.90)

- `PT-3040/gi-note-2026-06-02` (2026-06-02): "Last colonoscopy 2022-12 showed active disease."
- `PT-3040/labs-2026-10-09` (2026-10-09): "C-reactive protein                    15.6 mg/L     <5.0"
- Missing: Endoscopy/colonoscopy/flexible sigmoidoscopy report dated within 12 months before 2026-11-18 describing active inflammation
- Missing: OR fecal calprotectin result above the laboratory reference range, dated within 12 months

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is in the GI follow-up note (biologic planning). The request also lists the ordering provider as Gastroenterology. (confidence 0.80)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

Born 1977-08-22, the member is 49 at the request date, which is over 18. (confidence 0.98)

- `PT-3040/demographics-2026-03-09` (2026-03-09): "Date of birth: 1977-08-22"
- Code checks: age 49 on 2026-11-18 from DOB 1977-08-22

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Methotrexate and azathioprine are both conventional therapies. Each is documented with drug, dates and an intolerance reason in outside records. Nothing in the chart contradicts this. (confidence 0.90)

- `PT-3040/outside-records-2021-04-18` (2021-04-18): "Methotrexate 25 mg subcutaneously weekly, 2020-07 to 2020-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3040/outside-records-2021-04-18` (2021-04-18): "Azathioprine 2.5 mg/kg daily, 2021-01 to 2021-03. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

Adalimumab is documented with start and stop dates and a stated intolerance reason. Intolerance qualifies under the policy. (confidence 0.90)

- `PT-3040/medication-history-2026-10-28` (2026-10-28): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2026-09. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): **INSUFFICIENT**
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

The TB test was only ordered on 2026-10-29. No result is in the chart, and an order does not satisfy the criterion. (confidence 0.95)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- QuantiFERON-TB Gold Plus ordered today."
- Missing: Resulted QuantiFERON-TB Gold Plus (or TST) dated within 12 months before the request, showing a negative result

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted. Anti-HBc is positive, and the GI note gives a monitoring plan of HBV DNA and liver tests every 3 months. (confidence 0.93)

- `PT-3040/labs-2026-10-09` (2026-10-09): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3040/labs-2026-10-09` (2026-10-09): "Hepatitis B core antibody, total      Reactive      Nonreactive"
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is switching from vedolizumab. Two documents show it will be stopped when ustekinumab starts, so there is no concurrent biologic. (confidence 0.90)

- `PT-3040/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-15); to be discontinued when ustekinumab starts."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 106.6 kg was recorded 20 days before the request, which is within 30 days. It falls in the over-85 kg band, which takes 520 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.94)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Weight 106.6 kg."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.6 kg (2026-10-29) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.95)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopic report or fecal calprotectin within 12 months (who: ordering_provider)
  > PA-3040 (PT-3040), criterion C2 (policy 3.2): the only colonoscopy cited is from 2022-12, outside the 12-month window, and the 2026-10-09 CRP of 15.6 mg/L does not satisfy this criterion alone. Please review whether the chart has an endoscopy/colonoscopy/flex sig report describing active inflammation, or an elevated fecal calprotectin, dated on or after 2025-11-18, and add it if so.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation, or a fecal calprotectin above the performing lab's reference range, dated on or after 2025-11-18. CRP/ESR alone or imaging alone are not accepted.
- **C6**: Resulted negative QuantiFERON-TB Gold Plus (or TST) (who: lab)
  > PA-3040 (PT-3040), criterion C6 (policy 3.6): the QuantiFERON-TB Gold Plus ordered 2026-10-29 (GI note) has no result in the chart. Could you check with the lab and release the result, or confirm whether the sample was drawn? The result must be negative and not indeterminate.
  - Would satisfy the policy: Policy 3.6 accepts a negative IGRA or TST dated on or after 2025-11-18. An order without a result, or an indeterminate IGRA, does not satisfy it. If the result is positive, the policy requires chest imaging excluding active TB and documented start of latent TB treatment.

## Run cost

3 model calls, 20,981 input and 6,713 output tokens, 40.1 s of model time, $0.130 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
