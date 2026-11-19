# PA-3034: ustekinumab-aekn for PT-3034

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: EXPEDITED review. Pharmacy-benefit phase: decision within 24 hours of a complete request (policy section 7). Prescriber statement of clinical urgency is required. Work this case first.
- Ordered dose: 390 mg IV once (weight 66.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list records a Crohn's disease diagnosis. The treating GI note describes moderately to severely active disease and gives a Harvey-Bradshaw Index of 13, which is a validated measure of disease severity. (confidence 0.93)

- `PT-3034/problem-list-2026-11-09` (2026-11-09): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2019."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): **INSUFFICIENT**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy showing ulceration is dated 2025-04-18, which is outside the 12-month window (the window starts 2025-11-18). The elevated CRP alone does not count under the policy, and no fecal calprotectin result was found. (confidence 0.88)

- `PT-3034/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3034/labs-2026-10-21` (2026-10-21): "C-reactive protein                    22.0 mg/L     <5.0"
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report showing active inflammation dated on or after 2025-11-18
- Missing: Fecal calprotectin result above the lab reference range upper limit, with the reference range, dated on or after 2025-11-18

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The GI follow-up note orders the drug, and the request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 03/19/1992, the member is 34 years old on the request date of 2026-11-18. (confidence 0.97)

- `PT-3034/demographics-2026-04-29` (2026-04-29): "Date of birth: 03/19/1992"
- Code checks: age 34 on 2026-11-18 from DOB 1992-03-19

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history shows budesonide, which the policy counts as a corticosteroid, with start and stop dates and a stop reason of inadequate response. This alone satisfies the conventional-therapy requirement, without relying on the current prednisone. (confidence 0.88)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "Budesonide 9 mg daily, 05/2019 to 08/2019. Reason stopped: inadequate response after 10 weeks."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The member took infliximab from 07/2023 to 07/2026 and stopped it for secondary loss of response, backed by a low trough level and antidrug antibodies. (confidence 0.92)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The QuantiFERON-TB Gold Plus (an IGRA) resulted negative on 2026-10-21, which is within 12 months of the request. (confidence 0.95)

- `PT-3034/labs-2026-10-21` (2026-10-21): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted and nonreactive, so no monitoring or prophylaxis plan is required. (confidence 0.96)

- `PT-3034/labs-2026-10-21` (2026-10-21): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3034/labs-2026-10-21` (2026-10-21): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The medication history states the member is on no current biologic, JAK inhibitor, or S1P modulator. The prior biologic, infliximab, was stopped in 07/2026. (confidence 0.92)

- `PT-3034/medication-history-2026-11-08` (2026-11-08): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3034/medication-history-2026-11-08` (2026-11-08): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 07/2026. Reason stopped: secondary loss of response; trough 0.9 mcg/mL with antibodies 54 U/mL (reference <10)."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 66.2 kg was recorded 9 days before the request and falls in the >55-85 kg band, which calls for 390 mg IV. The requested maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.94)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Weight 66.2 kg."
- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.2 kg (2026-11-09) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the prescribing note name ustekinumab-aekn, which is a preferred product. (confidence 0.96)

- `PT-3034/gi-note-2026-11-09` (2026-11-09): "- Start ustekinumab-aekn: 390 mg IV once (weight 66.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopy/colonoscopy/flexible sigmoidoscopy report showing active inflammation, or an elevated fecal calprotectin with reference range, dated on or after 2025-11-18 (who: practice_staff)
  > For PT-3034 (ustekinumab-aekn, PA-3034), criterion C2 (policy 3.2) needs objective evidence of active disease from the 12 months before the 2026-11-18 request. The only endoscopy on file is the colonoscopy dated 2025-04-18, which is outside that window. The CRP of 22.0 mg/L from 2026-10-21 does not count on its own under the policy. Can you check whether the chart, or any outside facility, has an endoscopy, colonoscopy or flexible sigmoidoscopy report, or a fecal calprotectin result, dated on or after 2025-11-18? If none exists, please send this to Dr. Adeyemi to review.
  - Would satisfy the policy: Policy 3.2 accepts either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability) dated on or after 2025-11-18, or (b) a fecal calprotectin result above the performing lab's upper reference limit, with the reference range shown, dated on or after 2025-11-18. CRP/ESR alone or imaging alone is not accepted.

## Run cost

3 model calls, 31,577 input and 9,318 output tokens, 80.7 s of model time, $0.380 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent GAPS_TO_CLOSE. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
