# PA-1029: ustekinumab-ttwe for PT-1029

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

The treating gastroenterologist documents moderately to severely active ileocolonic Crohn's disease. Severity is supported by a Harvey-Bradshaw Index of 13 and the symptom burden described. (confidence 0.95)

- `PT-1029/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-1029/gi-note-2026-10-31` (2026-10-31): "Harvey-Bradshaw Index today: 13."
- `PT-1029/gi-note-2026-10-31` (2026-10-31): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-09-28, within 12 months of the request, shows ulceration in the terminal ileum. Fecal calprotectin of 441 ug/g on 2026-10-04 is also above the lab's reference limit of <50. (confidence 0.96)

- `PT-1029/colonoscopy-2026-09-28` (2026-09-28): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-1029/labs-2026-10-04` (2026-10-04): "CALPROTECTIN FECAL ................ 441 ug/g  (<50)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The drug is prescribed in the GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.95)

- `PT-1029/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1973-09-14, the member is 53 years old on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-1029/demographics-2026-06-14` (2026-06-14): "Date of birth: 1973-09-14"
- Code checks: age 53 on 2026-11-18 from DOB 1973-09-14

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history names methotrexate and azathioprine, gives dates for each, and records that both were stopped for intolerance. The treatment history section of the outside records is blank, so it neither supports nor contradicts this history. (confidence 0.88)

- `PT-1029/medication-history-2026-10-27` (2026-10-27): "Methotrexate 25 mg subcutaneously weekly, 2024-06 to 2024-10. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-1029/medication-history-2026-10-27` (2026-10-27): "Azathioprine 2.5 mg/kg daily, 2024-11 to 2025-01. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Infliximab, a TNF blocker, is documented with dates of 2025-03 to 2025-07. It was stopped for primary non-response, which qualifies under the policy. (confidence 0.90)

- `PT-1029/medication-history-2026-10-27` (2026-10-27): "Infliximab 5 mg/kg IV every 8 weeks, 2025-03 to 2025-07. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy 3.6): **INSUFFICIENT**
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The only TB screening test, a QuantiFERON on 2026-10-04, was indeterminate, and the policy says an indeterminate IGRA is not a negative result. A repeat test is needed; no negative result is on file. (confidence 0.93)

- `PT-1029/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... INDETERMINATE  (Negative)"
- `PT-1029/labs-2026-10-04` (2026-10-04): "Mitogen response below assay threshold; result cannot be interpreted."
- Missing: Repeat IGRA or tuberculin skin test with a determinate negative result dated within 12 months before the request

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted on 2026-10-04, and both are nonreactive. Because neither is positive, no monitoring plan is required. (confidence 0.96)

- `PT-1029/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-1029/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history lists no biologic, JAK inhibitor, or S1P receptor modulator. The prior biologic, infliximab, ended in 2025-07. (confidence 0.90)

- `PT-1029/medication-history-2026-10-27` (2026-10-27): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-1029/medication-history-2026-10-27` (2026-10-27): "Infliximab 5 mg/kg IV every 8 weeks, 2025-03 to 2025-07."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 55.0 kg is dated 2026-10-31, 18 days before the request, and falls in the 55 kg or less band that calls for 260 mg IV. The maintenance dose of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.92)

- `PT-1029/gi-note-2026-10-31` (2026-10-31): "Weight 55.0 kg."
- `PT-1029/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-31) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request names ustekinumab-ttwe, which is one of the policy's preferred products. No exception is needed. (confidence 0.96)

- `PT-1029/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C6**: Repeat IGRA or tuberculin skin test with a determinate negative result, dated within 12 months before the 2026-11-18 request (who: lab)
  > For PA-1029 (ustekinumab-ttwe), policy criterion 3.6 needs a negative TB screening test from the last 12 months. The only result on file is the QuantiFERON TB Gold Plus from 2026-10-04 (labs-2026-10-04). It came back INDETERMINATE because the mitogen response was below the assay threshold, and the policy does not count an indeterminate result as negative. Please send any repeat IGRA or TST result that has a clear reading, or let us know if a repeat test needs to be ordered and drawn.

## Run cost

3 model calls, 26,054 input and 6,232 output tokens, 51.6 s of model time, $0.222 at list price (1 served from cache).

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
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
