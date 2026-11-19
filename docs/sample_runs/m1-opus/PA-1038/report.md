# PA-1038: ustekinumab-ttwe for PT-1038

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 260 mg IV once (weight 53.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note calls it moderately to severely active, gives a Harvey-Bradshaw Index of 11 and describes 5-7 stools a day with urgency. (confidence 0.95)

- `PT-1038/problem-list-2026-10-25` (2026-10-25): "Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2019."
- `PT-1038/gi-note-2026-10-25` (2026-10-25): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-1038/gi-note-2026-10-25` (2026-10-25): "Harvey-Bradshaw Index today: 11."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-09-06 is within 12 months of the 2026-11-18 request. It describes multiple ulcers in the terminal ileum, and pathology shows chronic active inflammation. This meets the endoscopy option, so the elevated CRP is not needed. (confidence 0.95)

- `PT-1038/colonoscopy-2026-09-06` (2026-09-06): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-1038/colonoscopy-2026-09-06` (2026-09-06): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ordering provider on the request is Dr. A. Rivera, Gastroenterology. The order appears in the GI follow-up note. (confidence 0.90)

- `PT-1038/gi-note-2026-10-25` (2026-10-25): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 53.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 2005-07-25, the member is 21 on the request date of 2026-11-18. The outside records show the same date of birth. (confidence 0.98)

- `PT-1038/demographics-2026-07-22` (2026-07-22): "Date of birth: 2005-07-25"
- Code checks: age 21 on 2026-11-18 from DOB 2005-07-25

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Outside records document budesonide (2019-02 to 2019-05, stopped for inadequate response) and methotrexate (2019-06 to 2020-02, stopped for intolerance), each with dates and a reason. Both are conventional therapies under the policy. (confidence 0.88)

- `PT-1038/outside-records-2024-02-18` (2024-02-18): "- Budesonide 9 mg daily, 2019-02 to 2019-05. Reason stopped: inadequate response after 10 weeks."
- `PT-1038/outside-records-2024-02-18` (2024-02-18): "- Methotrexate 25 mg subcutaneously weekly, 2019-06 to 2020-02. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The 2026 medication history, based on patient report, says adalimumab ran from 2023-07 to 2026-08 and stopped for loss of response. The 2024-02 outside records say the patient declined adalimumab in 2023-07 and was still biologic-naive. These statements are incompatible, nothing in the chart resolves them, and the policy refers inconsistent records for clinical review. (confidence 0.88)

- `PT-1038/medication-history-2026-10-21` (2026-10-21): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2026-08. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-1038/outside-records-2024-02-18` (2024-02-18): "- Biologic-naive. Adalimumab was recommended 2023-07 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON (IGRA) resulted negative on 2026-10-17, within 12 months of the request. The older 2023 test is not needed. (confidence 0.95)

- `PT-1038/labs-2026-10-17` (2026-10-17): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc resulted nonreactive on 2026-10-17. No monitoring plan is required. (confidence 0.96)

- `PT-1038/labs-2026-10-17` (2026-10-17): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-1038/labs-2026-10-17` (2026-10-17): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The medication history states the member is not on any biologic, JAK inhibitor or S1P receptor modulator. The adalimumab it reports is listed as stopped in 2026-08. (confidence 0.88)

- `PT-1038/medication-history-2026-10-21` (2026-10-21): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 53.2 kg is dated 2026-10-25, 24 days before the request, and falls in the 55 kg or less band for a 260 mg IV dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.93)

- `PT-1038/gi-note-2026-10-25` (2026-10-25): "Weight 53.2 kg."
- `PT-1038/gi-note-2026-10-25` (2026-10-25): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 53.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 53.2 kg (2026-10-25) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order name ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.96)

- `PT-1038/gi-note-2026-10-25` (2026-10-25): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 53.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Ordering provider's review and documentation of the patient's adalimumab history: whether it was taken, dates, and reason stopped (who: ordering_provider)
  > Dr. Rivera, for PA-1038 (ustekinumab-ttwe, Northfield) the TNF-blocker criterion (policy 3.5(b)) has conflicting records. The medication history from 2026-10-21 lists adalimumab 40 mg every 2 weeks from 2023-07 to 2026-08, stopped for loss of response, based on patient report. The outside records from 2024-02-18 say the patient declined adalimumab in 2023-07 and was still biologic-naive. Please review both and document the actual adalimumab history (start and stop dates, reason stopped) with supporting records such as claims, prescription records or chart notes, or give a prescriber attestation.

## Run cost

3 model calls, 13,602 input and 3,415 output tokens, 28.8 s of model time, $0.151 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: conflicting.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
