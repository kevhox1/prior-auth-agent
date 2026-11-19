# PA-3045: ustekinumab-aekn for PT-3045

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

The problem list documents a Crohn's disease diagnosis (K50.80). The treating GI note calls the disease moderately to severely active and records a Harvey-Bradshaw Index of 9. (confidence 0.95)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Harvey-Bradshaw Index today: 9."
- `PT-3045/problem-list-2026-11-06` (2026-11-06): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy 3.2): **INSUFFICIENT**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only colonoscopy showing ulceration is dated 2025-04-18, which is before the 12-month cutoff of 2025-11-18. The elevated CRP (2026-10-03) does not count by itself under the policy, and no fecal calprotectin result was found. (confidence 0.88)

- `PT-3045/colonoscopy-2025-04-18` (2025-04-18): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3045/labs-2026-10-03` (2026-10-03): "C-reactive protein                    31.2 mg/L     <5.0"
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report showing active inflammation dated on or after 2025-11-18
- Missing: OR fecal calprotectin result above the lab's reference range upper limit, with the reference range, dated on or after 2025-11-18

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab-aekn order appears in a GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.93)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "1. Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 02/21/1966, the member is 60 years old on the request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-3045/demographics-2026-04-15` (2026-04-15): "Date of birth: 02/21/1966"
- Code checks: age 60 on 2026-11-18 from DOB 1966-02-21

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The outside records document 6-mercaptopurine taken from 04/2023 to 10/2023 and stopped for inadequate response at a therapeutic metabolite level. That covers the drug, dates and reason. The current budesonide bridge has no dates or reason, but this criterion does not depend on it. (confidence 0.85)

- `PT-3045/outside-records-2023-11-18` (2023-11-18): "- Mercaptopurine 1.5 mg/kg daily, 04/2023 to 10/2023. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history documents adalimumab, a TNF blocker, taken from 12/2023 to 05/2026. It was stopped for intolerance (drug-induced lupus), which qualifies. (confidence 0.90)

- `PT-3045/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A negative QuantiFERON-TB Gold Plus was resulted on 2026-10-03, within 12 months of the request. The GI note's mention of a 2023 negative test refers to an earlier screen and does not contradict this result. (confidence 0.92)

- `PT-3045/labs-2026-10-03` (2026-10-03): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc were resulted on 2026-10-03, and both are nonreactive. Because neither is positive, no monitoring or prophylaxis plan is needed. (confidence 0.96)

- `PT-3045/labs-2026-10-03` (2026-10-03): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3045/labs-2026-10-03` (2026-10-03): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The prior biologic, adalimumab, was stopped in 05/2026. (confidence 0.92)

- `PT-3045/medication-history-2026-11-04` (2026-11-04): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3045/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight was 55.0 kg on 2026-11-06, 12 days before the request, and falls in the 55 kg or less band, which calls for 260 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.92)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Weight 55.0 kg."
- `PT-3045/gi-note-2026-11-06` (2026-11-06): "1. Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-06) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-aekn, which is a preferred product. No exception documentation is needed. (confidence 0.96)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "1. Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Objective evidence of active disease dated on or after 2025-11-18: an endoscopy/colonoscopy/flexible sigmoidoscopy report showing active inflammation, or an elevated fecal calprotectin result with the lab's reference range (who: ordering_provider)
  > Dr. Adeyemi, the ustekinumab-aekn prior authorization for PT-3045 (PA-3045) does not yet meet Northfield policy criterion C2 (3.2), objective evidence of active disease. The only colonoscopy showing ulceration is dated 2025-04-18, which is before the 12-month cutoff of 2025-11-18. The CRP of 31.2 mg/L from 2026-10-03 does not count on its own under the policy, and we found no fecal calprotectin result. Can you confirm whether a qualifying endoscopy report or fecal calprotectin result dated on or after 2025-11-18 exists, including at an outside facility, and review how you would like to proceed?
  - Would satisfy the policy: Policy 3.2 accepts either an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability) dated on or after 2025-11-18, or a fecal calprotectin result above the performing lab's reference range upper limit, with the reference range shown, dated on or after 2025-11-18. Elevated CRP/ESR alone or imaging alone does not satisfy this criterion.

## Run cost

3 model calls, 21,821 input and 7,230 output tokens, 61.0 s of model time, $0.277 at list price (0 served from cache).

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
