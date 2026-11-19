# PA-1197: ustekinumab-aekn for PT-1197

**Outcome: READY_FOR_REVIEW**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 73.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list records a Crohn's disease diagnosis (K50.80). The GI provider calls the disease moderately to severely active and backs this up with a Harvey-Bradshaw Index of 10 and the patient's symptoms. (confidence 0.96)

- `PT-1197/problem-list-2026-10-31` (2026-10-31): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2021."
- `PT-1197/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-1197/gi-note-2026-10-31` (2026-10-31): "Harvey-Bradshaw Index today: 10."
- `PT-1197/gi-note-2026-10-31` (2026-10-31): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy on 2026-09-24, within 12 months of the request, describes ulceration in the terminal ileum. Fecal calprotectin on 2026-10-10 was 1255 ug/g, above the lab's reference limit of <50. (confidence 0.96)

- `PT-1197/colonoscopy-2026-09-24` (2026-09-24): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-1197/labs-2026-10-10` (2026-10-10): "Calprotectin, fecal | 1255 ug/g | H | <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The plan to start the drug is in the GI follow-up note. The request lists the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.93)

- `PT-1197/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-aekn: 390 mg IV once (weight 73.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 03/13/1956, the member is 70 on the request date, which is over 18. (confidence 0.98)

- `PT-1197/demographics-2026-06-04` (2026-06-04): "Date of birth: 03/13/1956"
- Code checks: age 70 on 2026-11-18 from DOB 1956-03-13

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history gives methotrexate with dates, stopped for intolerance, and budesonide with dates, stopped for inadequate response. Current budesonide bridge use is a separate, later course and does not contradict this history. (confidence 0.92)

- `PT-1197/medication-history-2026-10-29` (2026-10-29): "Methotrexate 25 mg subcutaneously weekly, 03/2021 to 07/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-1197/medication-history-2026-10-29` (2026-10-29): "Budesonide 9 mg daily, 08/2021 to 11/2021. Reason stopped: inadequate response after 10 weeks."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Adalimumab, a TNF blocker, is documented with start and stop dates (07/2023 to 06/2026). It was stopped for intolerance (drug-induced lupus). (confidence 0.94)

- `PT-1197/medication-history-2026-10-29` (2026-10-29): "Adalimumab 40 mg every 2 weeks, 07/2023 to 06/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus (IGRA) test resulted negative on 2026-10-10, within 12 months of the request. (confidence 0.96)

- `PT-1197/labs-2026-10-10` (2026-10-10): "QuantiFERON-TB Gold Plus | NEGATIVE | - | Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc have results on file, and both are nonreactive. Because neither is positive, no monitoring or prophylaxis plan is needed. (confidence 0.97)

- `PT-1197/labs-2026-10-10` (2026-10-10): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-1197/labs-2026-10-10` (2026-10-10): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history lists no biologic, JAK inhibitor or S1P modulator. The prior biologic, adalimumab, was stopped in 06/2026. (confidence 0.92)

- `PT-1197/medication-history-2026-10-29` (2026-10-29): "- No biologic or small-molecule advanced therapy at present."
- `PT-1197/medication-history-2026-10-29` (2026-10-29): "Adalimumab 40 mg every 2 weeks, 07/2023 to 06/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 73.7 kg was recorded on 2026-10-31, 18 days before the request, and falls in the >55 to 85 kg band, so 390 mg IV is the correct induction dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.95)

- `PT-1197/gi-note-2026-10-31` (2026-10-31): "Weight 73.7 kg."
- `PT-1197/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-aekn: 390 mg IV once (weight 73.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 73.7 kg (2026-10-31) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the GI note name ustekinumab-aekn, which is a preferred product. No exception documentation is needed. (confidence 0.97)

- `PT-1197/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-aekn: 390 mg IV once (weight 73.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## Run cost

2 model calls, 10,309 input and 3,087 output tokens, 24.2 s of model time, $0.128 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: clean.

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
