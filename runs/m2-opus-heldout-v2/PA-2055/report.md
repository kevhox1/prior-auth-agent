# PA-2055: ustekinumab-ttwe for PT-2055

**Outcome: READY_FOR_REVIEW**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 75.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses moderately to severely active ileocolonic Crohn's disease. It describes severity with a Harvey-Bradshaw Index of 8 and with symptom burden (missing work). (confidence 0.95)

- `PT-2055/gi-note-2026-11-05` (2026-11-05): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2055/gi-note-2026-11-05` (2026-11-05): "Harvey-Bradshaw Index today: 8."
- `PT-2055/gi-note-2026-11-05` (2026-11-05): "Symptoms not controlled on current therapy; missing work."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

Fecal calprotectin was 107 ug/g on 2026-09-12. The lab's reference range is <50, so the result is above the upper limit. The test is about 2 months before the 2026-11-18 request, inside the 12-month window. (confidence 0.94)

- `PT-2055/labs-2026-09-12` (2026-09-12): "Calprotectin, fecal | 107 ug/g | H | <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order appears in a GI follow-up note. The request names the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.92)

- `PT-2055/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 75.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth is 08/18/1960, which makes the member 66 on the request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-2055/demographics-2025-12-06` (2025-12-06): "Date of birth: 08/18/1960"
- Code checks: age 66 on 2026-11-18 from DOB 1960-08-18

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records azathioprine from 08/2021 to 10/2021, stopped for intolerance (acute pancreatitis). It also records budesonide from 11/2021 to 02/2022, stopped for inadequate response. The blank treatment-history section in the 2021 outside records leaves things out but does not contradict this history. (confidence 0.88)

- `PT-2055/medication-history-2026-11-04` (2026-11-04): "| Azathioprine | 2.5 mg/kg daily | 08/2021 | 10/2021 | Intolerance (acute pancreatitis) |"
- `PT-2055/medication-history-2026-11-04` (2026-11-04): "| Budesonide | 9 mg daily | 11/2021 | 02/2022 | Inadequate response after 10 weeks |"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records infliximab from 07/2023 to 06/2026. It was stopped for intolerance (drug-induced lupus), which is a qualifying reason. (confidence 0.90)

- `PT-2055/medication-history-2026-11-04` (2026-11-04): "| Infliximab | 5 mg/kg IV every 8 weeks | 07/2023 | 06/2026 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The IGRA on 2026-09-12 was positive, which is inside the 12-month window. The positive-test exception is satisfied: the 2026-09-15 chest X-ray shows no active TB, and rifampin for latent TB was started on 09/21/2026. (confidence 0.90)

- `PT-2055/labs-2026-09-12` (2026-09-12): "QuantiFERON-TB Gold Plus | POSITIVE | A | Negative"
- `PT-2055/chest-xray-2026-09-15` (2026-09-15): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2055/gi-note-2026-11-05` (2026-11-05): "Latent TB infection: rifampin daily for 4 months, started 09/21/2026."

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc both have results on file. Anti-HBc is reactive, and the GI note documents a monitoring plan: HBV DNA and liver tests every 3 months. (confidence 0.94)

- `PT-2055/labs-2026-09-12` (2026-09-12): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-2055/labs-2026-09-12` (2026-09-12): "Anti-HBc (total) | Reactive | A | Nonreactive"
- `PT-2055/gi-note-2026-11-05` (2026-11-05): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is currently on vedolizumab, a biologic. Both the medication history and the prescriber's note say it will be stopped when ustekinumab starts. No JAK inhibitor or S1P receptor modulator is listed. (confidence 0.88)

- `PT-2055/medication-history-2026-11-04` (2026-11-04): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/24/2026); to be discontinued when ustekinumab starts."
- `PT-2055/gi-note-2026-11-05` (2026-11-05): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight was 75.6 kg on 2026-11-05, 13 days before the request. That falls in the over 55 to 85 kg band, which matches the single 390 mg IV dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.94)

- `PT-2055/gi-note-2026-11-05` (2026-11-05): "Weight 75.6 kg."
- `PT-2055/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 75.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 75.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order name a specific product, ustekinumab-ttwe. This is one of the preferred products, so no exception is needed. (confidence 0.97)

- `PT-2055/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 75.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## Run cost

2 model calls, 19,895 input and 7,283 output tokens, 54.9 s of model time, $0.275 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: borderline.

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
