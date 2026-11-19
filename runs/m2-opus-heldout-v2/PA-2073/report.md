# PA-2073: ustekinumab (reference product) for PT-2073

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 61.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents a Crohn's disease diagnosis. The treating GI note calls the disease moderately to severely active and records a Harvey-Bradshaw Index of 13. (confidence 0.95)

- `PT-2073/problem-list-2026-11-08` (2026-11-08): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2021."
- `PT-2073/gi-note-2026-11-08` (2026-11-08): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2073/gi-note-2026-11-08` (2026-11-08): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

Fecal calprotectin was 527 ug/g against a lab reference range of <50. It was drawn 2026-09-05, within 12 months of the 2026-11-18 request. The elevated CRP is not relied on. (confidence 0.95)

- `PT-2073/labs-2026-09-05` (2026-09-05): "Fecal calprotectin                    527 ug/g      <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is written in a GI follow-up note, and the request lists the ordering provider as Dr. M. Chen, Gastroenterology. The quote itself does not state the prescriber's specialty, so the reviewer may want to confirm who wrote the note. (confidence 0.85)

- `PT-2073/gi-note-2026-11-08` (2026-11-08): "1. Start ustekinumab (reference product): 390 mg IV once (weight 61.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

A date of birth of 1990-05-21 makes the member 36 on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-2073/demographics-2026-05-31` (2026-05-31): "Date of birth: 1990-05-21"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-21

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Outside chart records name methotrexate (2022-01 to 2022-07, stopped for intolerance) and budesonide (2022-08 to 2022-11, stopped for inadequate response). Each entry gives the drug, dates and reason for stopping. Budesonide being restarted now as a bridge does not contradict this history. (confidence 0.92)

- `PT-2073/outside-records-2022-12-18` (2022-12-18): "- Methotrexate 25 mg subcutaneously weekly, 2022-01 to 2022-07. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-2073/outside-records-2022-12-18` (2022-12-18): "- Budesonide 9 mg daily, 2022-08 to 2022-11. Reason stopped: inadequate response after 10 weeks."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

A treating-provider chart note documents adalimumab from 2023-07 to 2023-11, stopped for primary non-response. Chart notes are acceptable support under the policy. No claims on file contradict this history. (confidence 0.88)

- `PT-2073/gi-note-2026-11-08` (2026-11-08): "Prior biologic: Adalimumab 40 mg every 2 weeks, 2023-07 to 2023-11. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A negative QuantiFERON-TB Gold Plus IGRA was resulted on 2026-09-05, within 12 months of the request. (confidence 0.96)

- `PT-2073/labs-2026-09-05` (2026-09-05): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted and nonreactive. Because neither is positive, no monitoring or prophylaxis plan is needed. (confidence 0.96)

- `PT-2073/labs-2026-09-05` (2026-09-05): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-2073/labs-2026-09-05` (2026-09-05): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The most recent GI note states the patient is on no biologic, JAK inhibitor, or S1P receptor modulator. The current medications listed are budesonide and vitamin D3. Adalimumab was stopped in 2023. (confidence 0.92)

- `PT-2073/gi-note-2026-11-08` (2026-11-08): "Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."

### C9 (policy 3.9): **INSUFFICIENT**
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The requested 390 mg IV induction and 90 mg SC every 8 weeks match the label for weight over 55 kg up to 85 kg. However, the only measured weight (61.2 kg) is dated 2026-10-03, 46 days before the request, which is outside the 30-day window. The 11-08 visit recorded no vitals and notes a 3 kg weight loss. (confidence 0.88)

- `PT-2073/gi-note-2026-10-03` (2026-10-03): "Weight 61.2 kg."
- `PT-2073/gi-note-2026-11-08` (2026-11-08): "Video visit; no vitals obtained."
- `PT-2073/gi-note-2026-11-08` (2026-11-08): "Ongoing abdominal pain and 4-6 loose stools a day; weight down 3 kg."
- Missing: Measured body weight dated within 30 days of the 2026-11-18 request (on or after 2026-10-19)
- Code checks: weight 61.2 kg (2026-10-03) -> label tier 390 mg; requested 390 mg; most recent cited weight is from 2026-10-03, older than 30 days

### C10 (policy 3.10): **NOT MET**
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request names the reference ustekinumab product, which the policy lists as non-preferred. The chart shows no trial of, intolerance of, or hypersensitivity to ustekinumab-aekn or ustekinumab-ttwe, so neither exception is documented. (confidence 0.85)

- `PT-2073/gi-note-2026-11-08` (2026-11-08): "1. Start ustekinumab (reference product): 390 mg IV once (weight 61.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-2073/gi-note-2026-11-08` (2026-11-08): "Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."

## To-do list (gap plan)

- **C9**: Measured body weight dated on or after 2026-10-19 (within 30 days of the 2026-11-18 request) (who: practice_staff)
  > For PA-2073 (ustekinumab, criterion C9, dose by weight), the policy requires a measured body weight dated within 30 days of the 2026-11-18 request, so on or after 2026-10-19. The only weight in the chart is 61.2 kg from the 2026-10-03 GI note. The 2026-11-08 video visit recorded no vitals and notes "weight down 3 kg." Please check for a weight recorded on or after 2026-10-19 and file it. If there isn't one, please arrange a measured weight and send it to us.
- **C10**: Provider review of the non-preferred product request (reference ustekinumab) against the policy's documented exceptions (who: ordering_provider)
  > Dr. Chen, for PA-2073 (criterion C10), the request is for the reference ustekinumab product, which Northfield lists as non-preferred. The policy covers it only if the record shows (a) an inadequate response to, or intolerance of, both ustekinumab-aekn and ustekinumab-ttwe, or (b) a contraindication or hypersensitivity to an inactive ingredient that is in both preferred products and not in the reference product. The 2026-11-08 note says the patient is on no advanced therapy, and the chart has no record of either exception. Please review the request and tell us how you'd like to proceed.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C10 | 3.10 | NOT_MET | NOT_MET | NOT_MET | ok |
