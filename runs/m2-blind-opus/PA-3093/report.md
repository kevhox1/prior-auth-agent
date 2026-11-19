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
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The GI provider calls the disease moderately to severely active and backs this with a Harvey-Bradshaw Index of 13 and a heavy symptom burden. (confidence 0.95)

- `PT-3093/problem-list-2026-11-05` (2026-11-05): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2024."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy on 2026-10-12, about 1 month before the request, describes ileal ulcers. Fecal calprotectin on 2026-09-25 was 1269 ug/g against a reference of <50. Either result alone satisfies the criterion within 12 months. (confidence 0.95)

- `PT-3093/colonoscopy-2026-10-12` (2026-10-12): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3093/labs-2026-09-25` (2026-09-25): "Fecal calprotectin                    1269 ug/g     <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The prescription plan is written in a GI follow-up note. The request lists the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.90)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

A date of birth of 1957-02-24 makes the member 69 on the request date. The outside records give the same date of birth. (confidence 0.97)

- `PT-3093/demographics-2026-05-15` (2026-05-15): "Date of birth: 1957-02-24"
- Code checks: age 69 on 2026-11-18 from DOB 1957-02-24

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Outside records give methotrexate and azathioprine with start/stop dates, and both were stopped for intolerance. The 2026 medication history leaves these drugs out, but a missing entry is not a conflict, so the outside records still count. (confidence 0.88)

- `PT-3093/outside-records-2025-03-18` (2025-03-18): "- Methotrexate 25 mg subcutaneously weekly, 2024-03 to 2024-11. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3093/outside-records-2025-03-18` (2025-03-18): "- Azathioprine 2.5 mg/kg daily, 2024-12 to 2025-02. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Infliximab was given from 2025-04 to 2026-07. It was stopped for secondary loss of response, supported by a low trough level and anti-drug antibodies. (confidence 0.92)

- `PT-3093/medication-history-2026-11-05` (2026-11-05): "| Infliximab | 5 mg/kg IV every 8 weeks | 2025-04 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 23 U/mL (reference <10) |"

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The IGRA within 12 months was positive. A chest X-ray on 2026-09-28 excluded active TB, and latent TB treatment with rifampin started 2026-10-01, which meets the policy's pathway for a positive test. (confidence 0.90)

- `PT-3093/labs-2026-09-25` (2026-09-25): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-3093/chest-xray-2026-09-28` (2026-09-28): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

The chart has only a hepatitis B surface antibody result and a vaccination record. The policy says neither counts, and no HBsAg or total anti-HBc result is on file. (confidence 0.93)

- `PT-3093/labs-2026-09-25` (2026-09-25): "Hepatitis B surface antibody          Reactive (immune)>10 mIU/mL"
- `PT-3093/outside-records-2025-03-18` (2025-03-18): "Immunizations: hepatitis B vaccine series x3, completed."
- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is on vedolizumab, a biologic. Both the GI note and the medication history say it will be stopped, with ustekinumab replacing the next vedolizumab infusion, which meets the switching rule. (confidence 0.88)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3093/medication-history-2026-11-05` (2026-11-05): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-24); to be discontinued when ustekinumab starts."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 55.0 kg was recorded 13 days before the request and falls in the 55 kg or less band, which calls for 260 mg IV. Maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.93)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "Weight 55.0 kg."
- `PT-3093/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-05) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the GI note both name ustekinumab-ttwe. It is one of the two preferred products, so no exception is needed. (confidence 0.96)

- `PT-3093/gi-note-2026-11-05` (2026-11-05): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C7**: Hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results (who: practice_staff)
  > For PA-3093 (ustekinumab-ttwe, PT-3093), criterion C7 (policy 3.7) needs both an HBsAg result and a total anti-HBc result on file. The chart only has a hepatitis B surface antibody result (labs 2026-09-25, 'Reactive (immune)') and a vaccine series record (outside records 2025-03-18), and the policy does not accept either one. Please check the chart, the lab portal and the outside records for HBsAg and total anti-HBc results from any date. If you can't find them, please let Dr. Chen know.
  - Would satisfy the policy: Policy 3.7 accepts resulted HBsAg and total anti-HBc tests from any date (no lookback limit). If either result is positive, the record must also include a plan for monitoring or antiviral prophylaxis. Tests that were ordered but have no result yet, anti-HBs alone, and vaccination history do not count.

## Run cost

3 model calls, 22,755 input and 7,361 output tokens, 62.3 s of model time, $0.287 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
