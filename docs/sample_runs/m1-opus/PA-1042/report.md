# PA-1042: ustekinumab-aekn for PT-1042

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 109.9 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note calls it moderately to severely active and backs this up with symptom burden (5-7 stools a day with urgency and nocturnal stooling) and a Harvey-Bradshaw Index of 8. (confidence 0.95)

- `PT-1042/problem-list-2026-11-03` (2026-11-03): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."
- `PT-1042/gi-note-2026-11-03` (2026-11-03): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-1042/gi-note-2026-11-03` (2026-11-03): "- Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."
- `PT-1042/gi-note-2026-11-03` (2026-11-03): "- Harvey-Bradshaw Index today: 8."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-10-04 is within 12 months of the 2026-11-18 request. It describes multiple ulcers in the terminal ileum, and pathology shows chronic active inflammation. The raised CRP is not needed and would not count on its own. (confidence 0.95)

- `PT-1042/colonoscopy-2026-10-04` (2026-10-04): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-1042/colonoscopy-2026-10-04` (2026-10-04): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order appears in a GI follow-up note. The request names the ordering provider as Dr. A. Rivera, Gastroenterology. (confidence 0.90)

- `PT-1042/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-aekn: 520 mg IV once (weight 109.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth is 1984-01-13, so the member is 42 on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-1042/demographics-2026-11-01` (2026-11-01): "Date of birth: 1984-01-13"
- Code checks: age 42 on 2026-11-18 from DOB 1984-01-13

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history documents methotrexate from 2023-08 to 2024-04, stopped for intolerance (nausea and ALT above 3 times normal). The outside records simply do not mention methotrexate; they do not contradict it, so this is not a conflict. The current prednisone is not relied on here. (confidence 0.80)

- `PT-1042/medication-history-2026-11-02` (2026-11-02): "| Methotrexate | 25 mg subcutaneously weekly | 2023-08 | 2024-04 | Intolerance (nausea and ALT above 3 times the upper limit of normal) |"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The outside records document infliximab, a TNF blocker, from 2024-06 to 2024-10, stopped for primary non-response. The medication history table leaves infliximab out but does not contradict it. The 2026-11-02 medication history also lists no current advanced therapy. (confidence 0.85)

- `PT-1042/outside-records-2024-11-18` (2024-11-18): "- Infliximab 5 mg/kg IV every 8 weeks, 2024-06 to 2024-10. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus (IGRA) resulted negative on 2026-09-21, within 12 months of the request. (confidence 0.95)

- `PT-1042/labs-2026-09-21` (2026-09-21): "QuantiFERON-TB Gold Plus | NEGATIVE | - | Negative"

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No passage in the chart shows an HBsAg or a total anti-HBc result. Both resulted tests are needed. (confidence 0.90)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history says the member is on no biologic, JAK inhibitor, or S1P receptor modulator. The earlier infliximab was stopped in 2024-10. (confidence 0.90)

- `PT-1042/medication-history-2026-11-02` (2026-11-02): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-1042/outside-records-2024-11-18` (2024-11-18): "- Infliximab 5 mg/kg IV every 8 weeks, 2024-06 to 2024-10. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 109.9 kg was recorded on 2026-11-03, within 30 days of the request. This is over 85 kg, which matches the 520 mg single IV induction dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.95)

- `PT-1042/gi-note-2026-11-03` (2026-11-03): "- Weight 109.9 kg."
- `PT-1042/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-aekn: 520 mg IV once (weight 109.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 109.9 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order both name ustekinumab-aekn, which is one of the policy's preferred products. (confidence 0.97)

- `PT-1042/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-aekn: 520 mg IV once (weight 109.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C7**: Resulted HBsAg and total anti-HBc tests (who: lab)
  > For PA-1042 (ustekinumab-aekn, patient PT-1042), the payer's hepatitis B screening criterion (policy 3.7) needs resulted hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) tests. We found neither result in the chart. Please send any prior results for both tests, of any date, or draw and result both if they were never done. A vaccination history, an anti-HBs result on its own or a test that was ordered but has no result will not meet this criterion.

## Run cost

3 model calls, 13,004 input and 3,382 output tokens, 28.6 s of model time, $0.145 at list price (1 served from cache).

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
