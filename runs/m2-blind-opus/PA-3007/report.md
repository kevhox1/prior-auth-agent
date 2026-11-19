# PA-3007: ustekinumab-ttwe for PT-3007

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 63.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80), and the GI note dated 2026-11-05 calls it moderately to severely active. The same note records a Harvey-Bradshaw Index of 9, which is a validated measure of severity. (confidence 0.93)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Harvey-Bradshaw Index today: 9."
- `PT-3007/problem-list-2026-11-05` (2026-11-05): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2021."

### C2 (policy 3.2): **INSUFFICIENT**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The most recent colonoscopy mentioned is from 12/2022, which is outside the 12-month lookback. The only recent marker is an elevated CRP, and the policy says CRP alone does not count. No fecal calprotectin result and no endoscopy report from the past 12 months is on file. (confidence 0.88)

- `PT-3007/gi-note-2026-05-13` (2026-05-13): "- Last colonoscopy 12/2022 showed active disease."
- `PT-3007/labs-2026-10-03` (2026-10-03): "C REACTIVE PROTEIN ................ 9.1 mg/L  (<5.0)"
- Missing: Endoscopy/colonoscopy/flexible sigmoidoscopy report describing active inflammation dated 2025-11-18 or later
- Missing: OR fecal calprotectin result above the lab reference range upper limit dated 2025-11-18 or later, with reference range

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order appears in a GI follow-up note for biologic planning. The request names Dr. S. Adeyemi, Gastroenterology, as the ordering provider. The quoted passage itself does not name the author's specialty, so the reviewer may want to confirm the note's author. (confidence 0.85)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth is 08/01/1980, so the member is 46 on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-3007/demographics-2026-05-23` (2026-05-23): "Date of birth: 08/01/1980"
- Code checks: age 46 on 2026-11-18 from DOB 1980-08-01

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Outside treating-provider records name methotrexate, give dates of 06/2021 to 11/2021, and say it was stopped for intolerance (nausea and ALT above 3 times normal). This meets the conventional-therapy requirement. Current budesonide is not needed to satisfy it. (confidence 0.88)

- `PT-3007/outside-records-2021-12-18` (2021-12-18): "- Methotrexate 25 mg subcutaneously weekly, 06/2021 to 11/2021. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The chart medication history names adalimumab, gives dates of 07/2023 to 11/2023, and gives primary non-response as the reason it was stopped. No claims are shown, but nothing in the chart contradicts this history. (confidence 0.85)

- `PT-3007/medication-history-2026-11-02` (2026-11-02): "| Adalimumab | 40 mg every 2 weeks | 07/2023 | 11/2023 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The QuantiFERON (IGRA) result dated 2026-10-03 is negative. That is within 12 months of the 2026-11-18 request. (confidence 0.96)

- `PT-3007/labs-2026-10-03` (2026-10-03): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc both have results on file, and both are nonreactive. Because neither is positive, no monitoring or prophylaxis plan is required. (confidence 0.97)

- `PT-3007/labs-2026-10-03` (2026-10-03): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3007/labs-2026-10-03` (2026-10-03): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The medication history dated 2026-11-02 states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The prior adalimumab was stopped in 11/2023. (confidence 0.92)

- `PT-3007/medication-history-2026-11-02` (2026-11-02): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 63.6 kg was recorded 13 days before the request, which is inside the 30-day window. That weight falls in the >55 to 85 kg band, which matches the 390 mg IV induction dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.95)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Weight 63.6 kg."
- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 63.6 kg (2026-11-05) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.97)

- `PT-3007/gi-note-2026-11-05` (2026-11-05): "- Start ustekinumab-ttwe: 390 mg IV once (weight 63.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: An endoscopy, colonoscopy or flexible sigmoidoscopy report showing active inflammation, or a fecal calprotectin result above the lab's upper reference limit, dated 2025-11-18 or later (who: ordering_provider)
  > Dr. Adeyemi, the ustekinumab-ttwe PA for PT-3007 (PA-3007) needs objective evidence of active Crohn's disease from the last 12 months under policy 3.2. The last colonoscopy we have is from 12/2022, cited in the 2026-05-13 GI note. The only recent marker is the CRP of 9.1 mg/L from 2026-10-03, and the policy does not accept CRP alone. Do you have an endoscopy report or a fecal calprotectin result dated 2025-11-18 or later, including one from an outside facility? If so, please send it to us. If not, please let us know how you would like to proceed.
  - Would satisfy the policy: Policy 3.2 accepts either an endoscopy, colonoscopy or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions or friability), or a fecal calprotectin result above the performing lab's upper reference limit with the reference range shown. Either one must be dated on or after 2025-11-18. Elevated CRP or ESR alone, and imaging alone, do not satisfy this criterion.

## Run cost

3 model calls, 21,306 input and 6,664 output tokens, 56.9 s of model time, $0.262 at list price (0 served from cache).

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
