# PA-3040: ustekinumab-ttwe for PT-3040

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 106.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI documents moderately to severely active ileocolonic Crohn's disease. Severity is supported by a Harvey-Bradshaw Index of 12 and uncontrolled symptoms. (confidence 0.95)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Harvey-Bradshaw Index today: 12."

### C2 (policy 3.2): **INSUFFICIENT**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only colonoscopy mentioned is from 2022-12, which is outside the 12-month window. An elevated CRP does not count on its own, and there is no fecal calprotectin result on file. (confidence 0.88)

- `PT-3040/gi-note-2026-06-02` (2026-06-02): "Last colonoscopy 2022-12 showed active disease."
- `PT-3040/labs-2026-10-09` (2026-10-09): "C-reactive protein                    15.6 mg/L     <5.0"
- Missing: Endoscopy/colonoscopy/flexible sigmoidoscopy report showing active inflammation dated on or after 2025-11-18, OR fecal calprotectin result above the lab reference range dated on or after 2025-11-18

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The request lists Dr. A. Rivera, Gastroenterology, as the ordering provider. The drug is ordered in the GI follow-up note. (confidence 0.93)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1977-08-22, the member is 49 on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-3040/demographics-2026-03-09` (2026-03-09): "Date of birth: 1977-08-22"
- Code checks: age 49 on 2026-11-18 from DOB 1977-08-22

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Outside records show methotrexate (2020-07 to 2020-12) and azathioprine (2021-01 to 2021-03), each stopped for documented intolerance. Each entry gives the drug name, dates and reason. Current prednisone is not needed to meet this criterion. (confidence 0.90)

- `PT-3040/outside-records-2021-04-18` (2021-04-18): "- Methotrexate 25 mg subcutaneously weekly, 2020-07 to 2020-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3040/outside-records-2021-04-18` (2021-04-18): "- Azathioprine 2.5 mg/kg daily, 2021-01 to 2021-03. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history shows adalimumab from 2023-07 to 2026-09, stopped for intolerance (drug-induced lupus). This gives the drug name, dates and a qualifying reason. (confidence 0.90)

- `PT-3040/medication-history-2026-10-28` (2026-10-28): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2026-09. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): **INSUFFICIENT**
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

An IGRA was ordered on 2026-10-29, but no result is on file. Under the policy, an order without a result does not count. (confidence 0.95)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- QuantiFERON-TB Gold Plus ordered today."
- Missing: Resulted QuantiFERON-TB Gold Plus (IGRA) or tuberculin skin test dated within 12 months before the request

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg (nonreactive) and total anti-HBc (reactive) have results on file. Because anti-HBc is positive, a monitoring plan is required, and the GI note documents one. (confidence 0.93)

- `PT-3040/labs-2026-10-09` (2026-10-09): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3040/labs-2026-10-09` (2026-10-09): "Hepatitis B core antibody, total      Reactive      Nonreactive"
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The patient is switching from vedolizumab, and two documents say it will be stopped when ustekinumab starts. Adalimumab was already stopped in 2026-09. (confidence 0.88)

- `PT-3040/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-15); to be discontinued when ustekinumab starts."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 106.6 kg was recorded on 2026-10-29, 20 days before the request, and falls in the >85 kg band for 520 mg IV. Maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.94)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Weight 106.6 kg."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.6 kg (2026-10-29) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request names ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.96)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "- Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopy/colonoscopy/sigmoidoscopy report showing active inflammation, or elevated fecal calprotectin result, dated within the past 12 months (who: ordering_provider)
  > Dr. Rivera, for PT-3040's ustekinumab-ttwe request (PA-3040), criterion C2 (policy 3.2) needs objective evidence of active disease from the past 12 months. The chart only has a reference in the 2026-06-02 GI note to a colonoscopy from 2022-12, which is outside the window, and a CRP of 15.6 mg/L (2026-10-09), which does not count by itself. Is there an endoscopy report or fecal calprotectin result dated on or after 2025-11-18 that we have not filed? If not, please review and tell us how you would like to proceed.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (e.g., ulceration, erosions, friability), or a fecal calprotectin result above the performing lab's upper reference limit, dated on or after 2025-11-18. Elevated CRP/ESR alone or imaging alone does not qualify.
- **C6**: Resulted QuantiFERON-TB Gold Plus (IGRA) from the order placed 2026-10-29 (who: lab)
  > For PT-3040 (PA-3040), criterion C6 (policy 3.6) needs a resulted TB screening test. The 2026-10-29 GI note shows that a QuantiFERON-TB Gold Plus was ordered, but we have no result on file. Please send the final result, or tell us whether the sample was collected and is still pending.
  - Would satisfy the policy: Policy 3.6 accepts a negative IGRA or TST dated on or after 2025-11-18. An indeterminate result or an order without a result does not qualify. If the result is positive, the record must show chest imaging ruling out active TB and that latent TB treatment has started.

## Run cost

3 model calls, 22,242 input and 7,451 output tokens, 62.2 s of model time, $0.285 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
