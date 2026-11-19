# PA-1103: ustekinumab-ttwe for PT-1103

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 85.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents ulcerative pancolitis (K51.00). The treating GI's note describes the disease as moderately to severely active. It also records symptom burden and a partial Mayo score of 5. (confidence 0.95)

- `PT-1103/problem-list-2026-11-09` (2026-11-09): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2022."
- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Moderately to severely active ulcerative pancolitis."
- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Partial Mayo score today: 5."
- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Ongoing abdominal pain and 4-6 loose stools a day; weight down 3 kg."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The flexible sigmoidoscopy dated 2026-10-05 is within 12 months of the 2026-11-18 request. It describes continuous inflammation with friability and erosions (Mayo endoscopic subscore 3). Because the endoscopy qualifies on its own, the policy's rule that CRP alone does not count does not affect this. (confidence 0.95)

- `PT-1103/flexible-sigmoidoscopy-2026-10-05` (2026-10-05): "- Rectum to 29 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab-ttwe plan appears in a GI follow-up note. The request names the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.90)

- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-ttwe: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1961-07-27, the member is 65 on the request date. That is above the 18-year minimum. (confidence 0.98)

- `PT-1103/demographics-2025-10-18` (2025-10-18): "Date of birth: 1961-07-27"
- Code checks: age 65 on 2026-11-18 from DOB 1961-07-27

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history shows methotrexate from 2022-12 to 2023-05, stopped for intolerance. It also shows mercaptopurine from 2023-06 to 2024-01, stopped for inadequate response. Each entry gives the drug, dates and reason for stopping, as the policy requires. (confidence 0.90)

- `PT-1103/medication-history-2026-11-07` (2026-11-07): "Methotrexate 25 mg subcutaneously weekly, 2022-12 to 2023-05. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-1103/medication-history-2026-11-07` (2026-11-07): "Mercaptopurine 1.5 mg/kg daily, 2023-06 to 2024-01. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Infliximab is documented from 2024-03 to 2026-09, stopped for secondary loss of response with a low trough level and antibodies. That satisfies the TNF-blocker requirement. The record does not give a start date for vedolizumab, which is listed as on maintenance every 8 weeks; a reviewer may want to confirm whether it overlapped with infliximab, but no document contradicts the infliximab history. (confidence 0.75)

- `PT-1103/medication-history-2026-11-07` (2026-11-07): "Infliximab 5 mg/kg IV every 8 weeks, 2024-03 to 2026-09. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 42 U/mL (reference <10)."
- `PT-1103/medication-history-2026-11-07` (2026-11-07): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-29); to be discontinued when ustekinumab starts."

### C6 (policy 3.6): **NOT MET**
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The only TB screening test on file is a negative QuantiFERON dated 2025-10-09. That is more than 12 months before the 2026-11-18 request, so it falls outside the lookback window. No newer IGRA or tuberculin skin test result is documented. (confidence 0.85)

- `PT-1103/labs-2025-10-09` (2025-10-09): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total hepatitis B core antibody were resulted on 2026-10-15, and both are nonreactive. Because neither is positive, no monitoring or prophylaxis plan is required. (confidence 0.95)

- `PT-1103/labs-2026-10-15` (2026-10-15): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-1103/labs-2026-10-15` (2026-10-15): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member's current biologic is vedolizumab. Both the medication history and the GI note document that it will be stopped, with ustekinumab taking the place of the next vedolizumab infusion. Infliximab was already stopped in 2026-09. (confidence 0.85)

- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-1103/medication-history-2026-11-07` (2026-11-07): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-29); to be discontinued when ustekinumab starts."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 85.0 kg was recorded on 2026-11-09, within 30 days of the request. That weight falls in the >55 to 85 kg band, which calls for 390 mg IV, matching the requested induction dose. The maintenance dose is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.92)

- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Weight 85.0 kg."
- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-ttwe: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 85.0 kg (2026-11-09) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the GI note both name the specific product, ustekinumab-ttwe. It is one of the two preferred products, so no exception is needed. (confidence 0.95)

- `PT-1103/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-ttwe: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C6**: Negative TB screening result (IGRA or TST) dated 2025-11-18 or later (who: ordering_provider)
  > Dr. Chen, PA-1103 (ustekinumab-ttwe) for PT-1103 does not meet criterion C6 (policy 3.6, TB screening). The only TB test on file is a negative QuantiFERON TB Gold Plus dated 2025-10-09. That is more than 12 months before the 2026-11-18 request, so it falls outside the 12-month window. Please review and let us know whether a newer IGRA or TST result exists or will be documented. Under the policy, a test that is ordered but has no result yet, or an indeterminate IGRA, does not count.

## Run cost

3 model calls, 13,328 input and 4,167 output tokens, 37.4 s of model time, $0.164 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
