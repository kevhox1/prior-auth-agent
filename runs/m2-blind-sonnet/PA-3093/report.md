# PA-3093: ustekinumab-ttwe for PT-3093

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

The treating GI note diagnoses moderately to severely active Crohn's disease. It supports severity with a Harvey-Bradshaw Index of 13. (confidence 0.96)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A colonoscopy dated 2026-10-12 describes ulceration. A fecal calprotectin dated 2026-09-25 is far above the reference of <50. Both fall within 12 months of the request. (confidence 0.96)

- `PT-3093/colonoscopy-2026-10-12` (2026-10-12): "Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3093/labs-2026-09-25` (2026-09-25): "Fecal calprotectin                    1269 ug/g     <50"

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No passage retrieved from the chart documents the prescriber's specialty or a gastroenterology consultation. The request lists Gastroenterology, but that is not chart evidence. (confidence 0.60)

- Missing: Chart document (e.g., signed GI note) showing the prescriber's specialty is gastroenterology, or documentation of consultation with a gastroenterologist

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

Date of birth 1957-02-24 makes the member 69 on the request date, which is over 18. (confidence 0.98)

- `PT-3093/demographics-2026-05-15` (2026-05-15): "Date of birth: 1957-02-24"
- Code checks: age 69 on 2026-11-18 from DOB 1957-02-24

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Outside records name methotrexate and azathioprine, with dates and reasons stopped (intolerance). Either one satisfies the conventional therapy requirement. (confidence 0.90)

- `PT-3093/outside-records-2025-03-18` (2025-03-18): "- Methotrexate 25 mg subcutaneously weekly, 2024-03 to 2024-11. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3093/outside-records-2025-03-18` (2025-03-18): "- Azathioprine 2.5 mg/kg daily, 2024-12 to 2025-02. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history documents infliximab from 2025-04 to 2026-07, stopped for secondary loss of response. It is supported by a low trough level and antibodies, and secondary loss of response qualifies. (confidence 0.88)

- `PT-3093/medication-history-2026-11-05` (2026-11-05): "| Infliximab | 5 mg/kg IV every 8 weeks | 2025-04 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 23 U/mL (reference <10) |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

The IGRA on 2026-09-25 is positive, so the policy's positive-result pathway applies. Chest X-ray excludes active TB, and latent TB treatment was started 2026-10-01. (confidence 0.90)

- `PT-3093/labs-2026-09-25` (2026-09-25): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-3093/chest-xray-2026-09-28` (2026-09-28): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Only an anti-HBs result and vaccine history are on file, and neither satisfies this criterion. No HBsAg or total anti-HBc result appears. (confidence 0.95)

- `PT-3093/labs-2026-09-25` (2026-09-25): "Hepatitis B surface antibody          Reactive (immune)>10 mIU/mL"
- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is switching from vedolizumab, and the chart documents it will be stopped when ustekinumab starts. No other concurrent biologic, JAK inhibitor or S1P modulator is shown. (confidence 0.88)

- `PT-3093/medication-history-2026-11-05` (2026-11-05): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-24); to be discontinued when ustekinumab starts."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight of 55.0 kg, recorded 2026-11-05 (within 30 days), falls in the 260 mg band. Maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the label. (confidence 0.93)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Weight 55.0 kg."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-05) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, a preferred product, so no non-preferred exception is needed. (confidence 0.95)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C3**: Chart document showing prescriber is a gastroenterologist or GI consultation (who: practice_staff)
  > For PA-3093 (PT-3093), criterion C3 (policy 3.3) needs chart evidence that the prescriber is a gastroenterologist or that a GI was consulted. The request lists Dr. M. Chen, Gastroenterology, but no chart document shows this. Can you locate and attach a signed GI note or consultation record?
  - Would satisfy the policy: Policy 3.3 accepts chart documentation, such as a signed GI note, showing the prescriber's specialty is gastroenterology, or documentation of consultation with a gastroenterologist.
- **C7**: HBsAg result and total anti-HBc result (who: ordering_provider)
  > For PA-3093 (PT-3093), criterion C7 (policy 3.7) requires both HBsAg and total anti-HBc results on file. The chart only has an anti-HBs result (labs-2026-09-25, reactive) and vaccine history, which do not satisfy this. Please check whether HBsAg and total anti-HBc results exist elsewhere, or review whether they should be obtained.
  - Would satisfy the policy: Policy 3.7 accepts resulted HBsAg and total anti-HBc tests with no lookback limit. If either is positive, a monitoring or antiviral prophylaxis plan is also required. Anti-HBs alone, vaccination history, or tests ordered but not resulted do not satisfy it.

## Run cost

3 model calls, 21,538 input and 6,712 output tokens, 39.8 s of model time, $0.132 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
