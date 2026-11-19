# PA-2048: ustekinumab-ttwe for PT-2048

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 111.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses moderately to severely active Crohn's disease. It documents a Harvey-Bradshaw Index of 13, which is a validated activity index. (confidence 0.95)

- `PT-2048/gi-note-2026-11-10` (2026-11-10): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2048/gi-note-2026-11-10` (2026-11-10): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): **NOT MET**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy, dated 2025-04-18, shows ulcers but is more than 12 months before the 2026-11-18 request. The CRP of 26.3 is within the window, but CRP alone does not count, and no fecal calprotectin result is in the chart. A new endoscopy or calprotectin result would be needed. (confidence 0.60)

- `PT-2048/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-2048/labs-2026-09-21` (2026-09-21): "CRP | 26.3 mg/L | H | <5.0"
- Missing: Endoscopy/colonoscopy report showing active inflammation dated on or after 2025-11-18, or fecal calprotectin result above the lab reference range dated on or after 2025-11-18

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order appears in a GI follow-up note. The request names Dr. M. Chen, Gastroenterology, as the ordering provider. (confidence 0.90)

- `PT-2048/gi-note-2026-11-10` (2026-11-10): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 111.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth is 1964-01-08, so the member is 62 years old on the request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-2048/demographics-2026-01-01` (2026-01-01): "Date of birth: 1964-01-08"
- Code checks: age 62 on 2026-11-18 from DOB 1964-01-08

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records methotrexate from 2020-05 to 2020-09, stopped for intolerance (nausea and ALT above 3 times normal). The blank treatment history in the outside records is missing information, not a contradiction. (confidence 0.85)

- `PT-2048/medication-history-2026-11-10` (2026-11-10): "| Methotrexate | 25 mg subcutaneously weekly | 2020-05 | 2020-09 | Intolerance (nausea and ALT above 3 times the upper limit of normal) |"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Infliximab was given from 2023-07 to 2026-07 and stopped for secondary loss of response, with a low trough level and anti-drug antibodies. The 2026-06-01 GI note supports ongoing symptoms during that period. (confidence 0.90)

- `PT-2048/medication-history-2026-11-10` (2026-11-10): "| Infliximab | 5 mg/kg IV every 8 weeks | 2023-07 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 60 U/mL (reference <10) |"
- `PT-2048/gi-note-2026-06-01` (2026-06-01): "Follow-up of Crohn's disease. Ongoing symptoms despite current therapy."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The IGRA from 2026-09-21, within the window, is positive. A chest X-ray on 2026-09-24 excluded active TB, and latent TB treatment with rifampin started 2026-10-01, which meets the policy's positive-test pathway. (confidence 0.85)

- `PT-2048/labs-2026-09-21` (2026-09-21): "QuantiFERON-TB Gold Plus | POSITIVE | A | Negative"
- `PT-2048/chest-xray-2026-09-24` (2026-09-24): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2048/gi-note-2026-11-10` (2026-11-10): "Latent TB infection: rifampin daily for 4 months, started 2026-10-01."

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc both have results on file, and both are nonreactive. No monitoring plan is required. (confidence 0.95)

- `PT-2048/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-2048/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history says there is no biologic or small-molecule advanced therapy at present. The prior infliximab was stopped in 2026-07. (confidence 0.90)

- `PT-2048/medication-history-2026-11-10` (2026-11-10): "- No biologic or small-molecule advanced therapy at present."
- `PT-2048/medication-history-2026-11-10` (2026-11-10): "| Infliximab | 5 mg/kg IV every 8 weeks | 2023-07 | 2026-07 | Secondary loss of response; trough 0.9 mcg/mL with antibodies 60 U/mL (reference <10) |"

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 111.6 kg is dated 2026-11-10, within 30 days of the request, and is above 85 kg, so 520 mg IV is the correct induction dose. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.93)

- `PT-2048/gi-note-2026-11-10` (2026-11-10): "Weight 111.6 kg."
- `PT-2048/gi-note-2026-11-10` (2026-11-10): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 111.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 111.6 kg (2026-11-10) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.95)

- `PT-2048/gi-note-2026-11-10` (2026-11-10): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 111.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopy/colonoscopy report showing active inflammation, or fecal calprotectin above the lab reference range, dated on or after 2025-11-18 (who: ordering_provider)
  > Dr. Chen, the ustekinumab-ttwe prior auth for PT-2048 (PA-2048) does not meet criterion C2 (policy 3.2). The policy requires objective evidence of active disease from the 12 months before the request (2025-11-18 to 2026-11-18). The only endoscopy, the colonoscopy from 2025-04-18, is outside that window, and the CRP of 26.3 mg/L on 2026-09-21 does not count by itself. Please review and tell us whether there is an endoscopy report showing active inflammation or an elevated fecal calprotectin result dated on or after 2025-11-18, or how you would like to proceed.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
