# PA-2052: ustekinumab-ttwe for PT-2052

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

The problem list documents a Crohn's disease diagnosis (K50.80). The treating GI note calls the disease moderately to severely active and gives a Harvey-Bradshaw Index of 13. (confidence 0.95)

- `PT-2052/problem-list-2026-10-31` (2026-10-31): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2020."
- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

Fecal calprotectin was 76 ug/g on 2026-09-26. That is above the lab's reference limit of <50 and within 12 months of the 2026-11-18 request. The CRP result was not relied on. (confidence 0.93)

- `PT-2052/labs-2026-09-26` (2026-09-26): "Calprotectin, fecal | 76 ug/g | H | <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is written in a GI follow-up note. The request lists the ordering provider as Dr. M. Chen, Gastroenterology. The quoted passage itself does not show the author's specialty, so the reviewer may want to confirm the note's signature. (confidence 0.80)

- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 04/03/1957, the member is 69 years old on the request date, which is over 18. (confidence 0.98)

- `PT-2052/demographics-2026-08-05` (2026-08-05): "Date of birth: 04/03/1957"
- Code checks: age 69 on 2026-11-18 from DOB 1957-04-03

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The treating-provider chart notes record prednisone (05/2020 to 12/2020), stopped for steroid dependence. They also record methotrexate (01/2021 to 06/2021), stopped for intolerance. Each entry gives the drug, the dates and the reason stopped. (confidence 0.92)

- `PT-2052/gi-note-2026-06-17` (2026-06-17): "- History: Prednisone 40 mg daily, tapered, 05/2020 to 12/2020. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."
- `PT-2052/gi-note-2026-06-17` (2026-06-17): "- History: Methotrexate 25 mg subcutaneously weekly, 01/2021 to 06/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The GI note records infliximab, a TNF blocker, from 07/2023 to 08/2026. It was stopped for intolerance (drug-induced lupus), which is a qualifying reason. (confidence 0.92)

- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 08/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): **INSUFFICIENT**
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The IGRA was ordered on 2026-10-31, but no result is in the passages. Under the policy, a test that is ordered but not resulted does not count. (confidence 0.95)

- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- QuantiFERON-TB Gold Plus ordered today."
- Missing: Resulted QuantiFERON-TB Gold Plus (IGRA) or tuberculin skin test dated within 12 months before the request

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No passages show results for hepatitis B surface antigen or total core antibody. Both results are required. (confidence 0.95)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The GI note says there is no current biologic, JAK inhibitor, or S1P receptor modulator. The prior biologic, infliximab, was stopped in 08/2026. (confidence 0.90)

- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 08/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 55.0 kg is recorded on 2026-10-31, 18 days before the request, and it falls in the 55 kg or less band for 260 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the labeling. (confidence 0.90)

- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Weight 55.0 kg."
- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-31) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the GI note name ustekinumab-ttwe, which is a preferred product. No exception documentation is needed. (confidence 0.95)

- `PT-2052/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C6**: Resulted QuantiFERON-TB Gold Plus (IGRA) or TST within 12 months of request (who: lab)
  > For PT-2052's ustekinumab-ttwe prior authorization (criterion C6, TB screening), the QuantiFERON-TB Gold Plus was ordered on 2026-10-31 (GI note 2026-10-31), but we have no result on file. Please send the final IGRA result with its collection date. The policy does not count an ordered test that has no result, and an indeterminate result does not count as negative.
- **C7**: Hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results (who: practice_staff)
  > For PT-2052's ustekinumab-ttwe prior authorization (criterion C7, hepatitis B screening), we need both an HBsAg result and a total anti-HBc result. Any date is acceptable. Please search the chart and outside records for these results and file them. A vaccination history or an anti-HBs result alone does not meet the requirement. If neither test has ever been done, please tell Dr. Chen so both can be ordered.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
