# PA-2063: ustekinumab-aekn for PT-2063

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 85.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease. The GI note grades it as moderately to severely active and gives a Harvey-Bradshaw Index of 13, which is a validated activity index. (confidence 0.95)

- `PT-2063/problem-list-2026-10-28` (2026-10-28): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2020."
- `PT-2063/gi-note-2026-10-28` (2026-10-28): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2063/gi-note-2026-10-28` (2026-10-28): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): **INSUFFICIENT**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only colonoscopy mentioned is from 2023-02, which is outside the 12-month window. The CRP is elevated, but the policy says CRP alone does not count. No fecal calprotectin result is on file. (confidence 0.90)

- `PT-2063/gi-note-2026-04-08` (2026-04-08): "Last colonoscopy 2023-02 showed active disease."
- `PT-2063/labs-2026-09-26` (2026-09-26): "C REACTIVE PROTEIN ................ 14.6 mg/L  (<5.0)"
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation dated 2025-11-18 or later
- Missing: OR fecal calprotectin result above the lab reference range upper limit dated 2025-11-18 or later

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The request names Dr. A. Rivera, Gastroenterology, as the ordering provider. The ustekinumab plan appears in a GI follow-up note. (confidence 0.90)

- `PT-2063/gi-note-2026-10-28` (2026-10-28): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth is 1963-04-22, so the member is 63 years old on the request date. The outside records list the same date of birth. (confidence 0.98)

- `PT-2063/demographics-2026-06-06` (2026-06-06): "Date of birth: 1963-04-22"
- Code checks: age 63 on 2026-11-18 from DOB 1963-04-22

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The treating GI's chart note documents mercaptopurine (2020-06 to 2021-01, stopped for inadequate response) and methotrexate (2021-02 to 2021-08, stopped for intolerance). Each entry gives the drug, dates and reason. The outside records' treatment history section is blank, but that is a missing record, not a contradiction. (confidence 0.88)

- `PT-2063/gi-note-2026-04-08` (2026-04-08): "History: Mercaptopurine 1.5 mg/kg daily, 2020-06 to 2021-01. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."
- `PT-2063/gi-note-2026-04-08` (2026-04-08): "History: Methotrexate 25 mg subcutaneously weekly, 2021-02 to 2021-08. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The GI chart note documents infliximab from 2023-07 to 2026-08, stopped for intolerance (drug-induced lupus). Vedolizumab is listed as the current drug, with its last infusion on 2026-10-12. That fits a switch after infliximab ended in 2026-08, and no record contradicts the infliximab history. (confidence 0.78)

- `PT-2063/gi-note-2026-10-28` (2026-10-28): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-08. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON (IGRA) test dated 2026-09-26 is negative. That is within 12 months of the 2026-11-18 request. (confidence 0.95)

- `PT-2063/labs-2026-09-26` (2026-09-26): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc both resulted nonreactive on 2026-09-26. Because neither is positive, no monitoring or prophylaxis plan is needed. (confidence 0.96)

- `PT-2063/labs-2026-09-26` (2026-09-26): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2063/labs-2026-09-26` (2026-09-26): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is currently on vedolizumab, which is a biologic. The plan explicitly says to stop it, with ustekinumab replacing the next scheduled infusion. No other biologic, JAK inhibitor or S1P modulator is listed. (confidence 0.88)

- `PT-2063/gi-note-2026-10-28` (2026-10-28): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-12); to be discontinued when ustekinumab starts."
- `PT-2063/gi-note-2026-10-28` (2026-10-28): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 85.0 kg was recorded on 2026-10-28, 21 days before the request. That falls in the more-than-55 to 85 kg band, which calls for 390 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.93)

- `PT-2063/gi-note-2026-10-28` (2026-10-28): "Weight 85.0 kg."
- `PT-2063/gi-note-2026-10-28` (2026-10-28): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 85.0 kg (2026-10-28) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the plan name ustekinumab-aekn, which is a preferred product, so no exception needs to be documented. (confidence 0.96)

- `PT-2063/gi-note-2026-10-28` (2026-10-28): "1. Start ustekinumab-aekn: 390 mg IV once (weight 85.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopy/colonoscopy/sigmoidoscopy report showing active inflammation, or fecal calprotectin above the lab's reference range, dated 2025-11-18 or later (who: lab)
  > For PA-2063 (PT-2063, ustekinumab-aekn), criterion C2 requires objective evidence of active disease dated 2025-11-18 or later. The only colonoscopy on file is from 2023-02 (cited in gi-note-2026-04-08), which is too old. The CRP of 14.6 mg/L on labs-2026-09-26 does not count on its own under the policy. Please send any fecal calprotectin result above the lab's reference range, or an endoscopy report showing active inflammation, from that period. If neither exists, please let us know whether a fecal calprotectin will be collected.

## Run cost

3 model calls, 21,572 input and 7,471 output tokens, 59.0 s of model time, $0.283 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
