# PA-2010: ustekinumab-aekn for PT-2010

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

The problem list documents Crohn's disease (K50.80). The treating GI note calls it moderately to severely active and gives a Harvey-Bradshaw Index of 14, so severity is described. (confidence 0.95)

- `PT-2010/gi-note-2026-11-02` (2026-11-02): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2010/gi-note-2026-11-02` (2026-11-02): "Harvey-Bradshaw Index today: 14."
- `PT-2010/problem-list-2026-11-02` (2026-11-02): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2020."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy of 2026-08-31, within 12 months, shows ileal ulcers. Fecal calprotectin of 1082 ug/g on 2026-09-16 is well above the lab's reference range of <50. Either one meets the criterion on its own. (confidence 0.95)

- `PT-2010/colonoscopy-2026-08-31` (2026-08-31): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-2010/labs-2026-09-16` (2026-09-16): "Fecal calprotectin                    1082 ug/g     <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in a GI follow-up note, and the request names the ordering provider as Dr. M. Chen, Gastroenterology. The quoted passage does not itself state the specialty, so the reviewer may want to confirm the note's author. (confidence 0.85)

- `PT-2010/gi-note-2026-11-02` (2026-11-02): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

A date of birth of 1973-11-02 makes the member 53 on the 2026-11-18 request date. The outside records show the same date of birth. (confidence 0.97)

- `PT-2010/demographics-2026-09-03` (2026-09-03): "Date of birth: 1973-11-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-11-02

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records budesonide (2020-05 to 2020-08, inadequate response) and methotrexate (2020-09 to 2021-03, intolerance), each with dates and a reason for stopping. No record on file contradicts these conventional therapy trials. (confidence 0.88)

- `PT-2010/medication-history-2026-10-31` (2026-10-31): "Budesonide 9 mg daily, 2020-05 to 2020-08. Reason stopped: inadequate response after 10 weeks."
- `PT-2010/medication-history-2026-10-31` (2026-10-31): "Methotrexate 25 mg subcutaneously weekly, 2020-09 to 2021-03. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history says infliximab ran from 2023-07 to 2026-05, based on patient report. The 2023-12 outside records say the patient declined infliximab in 2023-07 and was biologic-naive, which cannot both be true. The requested outside records are not on file to resolve this, and the policy says inconsistent records go to clinical review. (confidence 0.85)

- `PT-2010/medication-history-2026-10-31` (2026-10-31): "Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-05. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-2010/outside-records-2023-12-18` (2023-12-18): "- Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A resulted negative QuantiFERON (IGRA) dated 2026-09-16 falls within 12 months of the request. The 2023 test is outside the window but is not needed. (confidence 0.95)

- `PT-2010/labs-2026-09-16` (2026-09-16): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted on 2026-09-16, and both are nonreactive. Because neither is positive, no monitoring or prophylaxis plan is required. (confidence 0.96)

- `PT-2010/labs-2026-09-16` (2026-09-16): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-2010/labs-2026-09-16` (2026-09-16): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history lists no biologic, JAK inhibitor or S1P modulator, so no concurrent use is documented. The reported prior infliximab is recorded as stopped in 2026-05. (confidence 0.90)

- `PT-2010/medication-history-2026-10-31` (2026-10-31): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight of 85.0 kg on 2026-11-02 is within 30 days of the request and falls in the >55 to 85 kg band, which matches 390 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which follows the label. (confidence 0.93)

- `PT-2010/gi-note-2026-11-02` (2026-11-02): "Weight 85.0 kg."
- `PT-2010/gi-note-2026-11-02` (2026-11-02): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 85.0 kg (2026-11-02) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order both name ustekinumab-aekn, which is a preferred product. No exception documentation is needed. (confidence 0.96)

- `PT-2010/gi-note-2026-11-02` (2026-11-02): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Provider review and documentation settling whether infliximab was ever given (drug, start/stop dates, reason stopped), backed by records or attestation (who: ordering_provider)
  > Dr. Chen, for PA-2010 (ustekinumab-aekn, criterion 3.5(b) prior TNF blocker), the chart has two records that disagree. The medication history dated 2026-10-31 lists infliximab 5 mg/kg IV every 8 weeks from 2023-07 to 2026-05, stopped for loss of response. That entry is based on what the patient reported. The outside records dated 2023-12-18 say the patient was "biologic-naive" and declined infliximab in 2023-07. Please review both and document which is accurate: drug, approximate start and stop dates, and reason stopped. Please include supporting infusion records, claims or chart notes, or your attestation. The outside records already requested may also help.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

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
