# PA-1169: ustekinumab-aekn for PT-1169

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 59.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note calls it moderately to severely active and records a Harvey-Bradshaw Index of 14. (confidence 0.95)

- `PT-1169/gi-note-2026-11-07` (2026-11-07): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-1169/gi-note-2026-11-07` (2026-11-07): "Harvey-Bradshaw Index today: 14."
- `PT-1169/problem-list-2026-11-07` (2026-11-07): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2018."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-09-17 is within 12 months of the 2026-11-18 request. It describes ulceration of the terminal ileum with active inflammation on pathology. This is endoscopic evidence, so the elevated CRP is not needed. (confidence 0.95)

- `PT-1169/colonoscopy-2026-09-17` (2026-09-17): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-1169/colonoscopy-2026-09-17` (2026-09-17): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order is in the GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-1169/gi-note-2026-11-07` (2026-11-07): "- Start ustekinumab-aekn: 390 mg IV once (weight 59.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1967-07-19, the member is 59 years old on the request date. (confidence 0.97)

- `PT-1169/demographics-2026-04-21` (2026-04-21): "Date of birth: 1967-07-19"
- Code checks: age 59 on 2026-11-18 from DOB 1967-07-19

### C5 (policy 3.5): **NOT MET**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history lists azathioprine (2019-01 to 2019-03), stopped for intolerance (acute pancreatitis). It also lists budesonide (2019-04 to 2019-07), stopped for inadequate response. Each entry has the drug name, dates and reason for stopping. (confidence 0.90)

- `PT-1169/medication-history-2026-11-03` (2026-11-03): "| Azathioprine | 2.5 mg/kg daily | 2019-01 | 2019-03 | Intolerance (acute pancreatitis) |"
- `PT-1169/medication-history-2026-11-03` (2026-11-03): "| Budesonide | 9 mg daily | 2019-04 | 2019-07 | Inadequate response after 10 weeks |"

**C5b (policy 3.5(b)): **NOT MET****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Adalimumab is the only TNF blocker on record. It was stopped because insurance coverage changed while the disease was controlled, which is not non-response, loss of response, intolerance or a contraindication. The March 2026 note mentioning ongoing symptoms gives no reason for stopping and is not a documented loss of response, so it does not settle the criterion. (confidence 0.75)

- `PT-1169/medication-history-2026-11-03` (2026-11-03): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-08 | Stopped when insurance coverage changed; disease was controlled at the time |"

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The QuantiFERON-TB Gold Plus test dated 2026-09-09 is negative and within 12 months of the request. The 2023 test is older but is not needed. (confidence 0.95)

- `PT-1169/labs-2026-09-09` (2026-09-09): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted as nonreactive on 2026-09-09. Because neither is positive, no monitoring plan is required. (confidence 0.96)

- `PT-1169/labs-2026-09-09` (2026-09-09): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-1169/labs-2026-09-09` (2026-09-09): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The medication history states the patient is on no current biologic, JAK inhibitor or S1P receptor modulator. The prior adalimumab was stopped in 2026-08. (confidence 0.90)

- `PT-1169/medication-history-2026-11-03` (2026-11-03): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-1169/medication-history-2026-11-03` (2026-11-03): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-08 | Stopped when insurance coverage changed; disease was controlled at the time |"

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 59.2 kg was recorded on 2026-11-07, 11 days before the request, and falls in the >55 to 85 kg band, which calls for 390 mg IV. The maintenance order is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.94)

- `PT-1169/gi-note-2026-11-07` (2026-11-07): "Weight 59.2 kg."
- `PT-1169/gi-note-2026-11-07` (2026-11-07): "- Start ustekinumab-aekn: 390 mg IV once (weight 59.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 59.2 kg (2026-11-07) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order both name ustekinumab-aekn, which is a preferred product. (confidence 0.96)

- `PT-1169/gi-note-2026-11-07` (2026-11-07): "- Start ustekinumab-aekn: 390 mg IV once (weight 59.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Provider review of the reason adalimumab was stopped, and documentation if there was inadequate response, intolerance or contraindication to a TNF blocker (who: ordering_provider)
  > Dr. Adeyemi, for PA-1169 (PT-1169, ustekinumab-aekn), Northfield policy 3.5(b) requires a documented inadequate response, intolerance or contraindication to adalimumab or infliximab. The medication history dated 2026-11-03 says adalimumab 40 mg every 2 weeks (2023-07 to 2026-08) was "Stopped when insurance coverage changed; disease was controlled at the time." That reason does not meet the criterion, and the March 2026 note about ongoing symptoms gives no reason for stopping. Please review and tell us whether the chart or an attestation accurately documents a qualifying reason, or confirm that the criterion is not met.

## Run cost

3 model calls, 12,964 input and 3,432 output tokens, 30.8 s of model time, $0.146 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | NOT_MET | NOT_MET | NOT_MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
