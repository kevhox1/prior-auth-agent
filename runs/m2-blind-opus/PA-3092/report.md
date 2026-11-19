# PA-3092: ustekinumab-ttwe for PT-3092

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

The problem list shows a Crohn's disease diagnosis (K50.80). The treating GI note calls the disease moderately to severely active and gives a Harvey-Bradshaw Index of 13. (confidence 0.95)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Harvey-Bradshaw Index today: 13."
- `PT-3092/problem-list-2026-10-30` (2026-10-30): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2022."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The GI note gives a fecal calprotectin of 1306 ug/g dated 08/23/2026, which is within 12 months of the request. The lab reference is <50, so the result is above the upper limit. The result appears only in the provider note; the original lab report is not among the passages. (confidence 0.70)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "His calprotectin from 08/23/2026 came back at 1306 ug/g (lab reference <50)."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The GI follow-up note orders the drug. The request names the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.95)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth is 05/12/1990, so the member is 36 on the request date. (confidence 0.97)

- `PT-3092/demographics-2025-10-15` (2025-10-15): "Date of birth: 05/12/1990"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-12

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history shows budesonide, which counts as a conventional corticosteroid. It gives start and stop dates (09/2022 to 12/2022) and the reason stopped: inadequate response. (confidence 0.90)

- `PT-3092/medication-history-2026-10-28` (2026-10-28): "| Budesonide | 9 mg daily | 09/2022 | 12/2022 | Inadequate response after 10 weeks |"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The policy accepts a specifically documented contraindication such as demyelinating disease. The GI note documents an anti-TNF contraindication due to multiple sclerosis, and the problem list confirms relapsing-remitting MS. (confidence 0.85)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3092/problem-list-2026-10-30` (2026-10-30): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy 3.6): **INSUFFICIENT**
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

No tuberculosis screening result was found in the documents searched. A negative resulted IGRA or TST dated within 12 months of the request is required. (confidence 0.90)

- Missing: Resulted interferon-gamma release assay or tuberculin skin test dated within 12 months before 2026-11-18

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc were resulted on 2026-09-21, and both are nonreactive. No monitoring plan is needed. (confidence 0.95)

- `PT-3092/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3092/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is currently on vedolizumab, a biologic. Both the medication history and the GI note document that vedolizumab will be stopped when ustekinumab starts, which is what the policy requires for a switch. (confidence 0.85)

- `PT-3092/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/16/2026); to be discontinued when ustekinumab starts."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 55.0 kg is dated 2026-10-30, 19 days before the request, and falls in the 260 mg band (55 kg or less). Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. The older 58.0 kg weight is outside the 30-day window. (confidence 0.90)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "Weight 55.0 kg."
- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-30) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the GI note name ustekinumab-ttwe, which is a preferred product. (confidence 0.95)

- `PT-3092/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C6**: Resulted negative IGRA or TST dated on or after 2025-11-18 (who: practice_staff)
  > For PA-3092 (ustekinumab-ttwe, patient PT-3092), we could not find a tuberculosis screening result for criterion C6 (Policy 3.6) in the documents we searched. Please find and file any resulted IGRA (e.g., QuantiFERON) or TST dated on or after 2025-11-18. If the result was positive, please also file the chest imaging that ruled out active TB and the record showing latent TB treatment was started. If no such test is on file, please let Dr. M. Chen know so the provider can decide how to proceed.
  - Would satisfy the policy: Policy 3.6 accepts a negative resulted IGRA or TST dated on or after 2025-11-18 (within 12 months before the 2026-11-18 request). It does not accept an indeterminate IGRA or a test that was ordered but has no result. If the test was positive, the policy accepts it only when the record also shows chest imaging that excluded active TB and documents that latent TB treatment was started.

## Run cost

3 model calls, 41,829 input and 11,807 output tokens, 98.3 s of model time, $0.437 at list price (0 served from cache).

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
