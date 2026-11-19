# PA-2054: ustekinumab-aekn for PT-2054

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents ulcerative pancolitis diagnosed in 2019. The treating GI calls the disease moderately to severely active and records a partial Mayo score of 6, which is a validated activity index. (confidence 0.95)

- `PT-2054/problem-list-2026-11-09` (2026-11-09): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2019."
- `PT-2054/gi-note-2026-11-09` (2026-11-09): "Moderately to severely active ulcerative pancolitis."
- `PT-2054/gi-note-2026-11-09` (2026-11-09): "Partial Mayo score today: 6."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The flexible sigmoidoscopy of 2026-08-19, within 12 months of the request, describes friability and erosions. Fecal calprotectin of 782 ug/g on 2026-10-04 is also above the lab's upper limit of <50. (confidence 0.95)

- `PT-2054/flexible-sigmoidoscopy-2026-08-19` (2026-08-19): "- Rectum to 27 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-2054/labs-2026-10-04` (2026-10-04): "Fecal calprotectin                    782 ug/g      <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan comes from the GI follow-up note. The request names the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-2054/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1974-08-12, the member is 52 on the request date of 2026-11-18. (confidence 0.98)

- `PT-2054/demographics-2025-12-01` (2025-12-01): "Date of birth: 1974-08-12"
- Code checks: age 52 on 2026-11-18 from DOB 1974-08-12

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history lists budesonide (inadequate response) and prednisone (steroid dependent, flared during taper), each with start and stop dates. Both are qualifying conventional therapies. (confidence 0.92)

- `PT-2054/medication-history-2026-11-09` (2026-11-09): "Budesonide 9 mg daily, 2019-06 to 2019-09. Reason stopped: inadequate response after 10 weeks."
- `PT-2054/medication-history-2026-11-09` (2026-11-09): "Prednisone 40 mg daily, tapered, 2019-10 to 2020-02. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Infliximab, a TNF blocker, is documented from 2023-07 to 2026-06. It was stopped for intolerance (drug-induced lupus), which qualifies. (confidence 0.92)

- `PT-2054/medication-history-2026-11-09` (2026-11-09): "Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-06. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The IGRA on 2026-10-04 was positive. The policy's positive-result pathway is satisfied: the 2026-10-07 chest X-ray found no active TB, and rifampin for latent TB was started on 2026-10-12. (confidence 0.90)

- `PT-2054/labs-2026-10-04` (2026-10-04): "QuantiFERON-TB Gold Plus              POSITIVE      Negative"
- `PT-2054/chest-xray-2026-10-07` (2026-10-07): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2054/gi-note-2026-11-09` (2026-11-09): "Latent TB infection: rifampin daily for 4 months, started 2026-10-12."

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No hepatitis B screening results were found in the passages. Both an HBsAg result and a total anti-HBc result are required. (confidence 0.90)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history states there is no concurrent biologic, JAK inhibitor, or S1P modulator. Prior infliximab was stopped in 2026-06. (confidence 0.92)

- `PT-2054/medication-history-2026-11-09` (2026-11-09): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-2054/medication-history-2026-11-09` (2026-11-09): "Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-06. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 55.0 kg on 2026-11-09 is within 30 days of the request and falls in the 55 kg or less band, so 260 mg IV is the correct induction dose. Maintenance at 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. The older 58.0 kg weight from 2026-03-03 is outside the 30-day window. (confidence 0.90)

- `PT-2054/gi-note-2026-11-09` (2026-11-09): "Weight 55.0 kg."
- `PT-2054/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-09) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the GI note both name ustekinumab-aekn, which is a preferred product, so no exception is needed. (confidence 0.95)

- `PT-2054/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C7**: Resulted HBsAg and total anti-HBc lab reports (who: practice_staff)
  > For PA-2054 (ustekinumab-aekn, PT-2054), criterion C7 (policy 3.7) requires resulted hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) reports, and none were found in the submitted records. Please locate both results in the chart and attach them. Any date is acceptable, but vaccination history, an anti-HBs result alone, or a test that was ordered without a result will not count. If either result is positive, please also attach the documented monitoring or antiviral prophylaxis plan. If the tests were never drawn, please let Dr. Adeyemi know so the screening can be ordered.

## Run cost

3 model calls, 20,941 input and 6,568 output tokens, 54.4 s of model time, $0.260 at list price (0 served from cache).

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
