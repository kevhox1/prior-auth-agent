# PA-2082: ustekinumab-ttwe for PT-2082

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: EXPEDITED review. Pharmacy-benefit phase: decision within 24 hours of a complete request (policy section 7). Prescriber statement of clinical urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 86.1 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents ulcerative pancolitis diagnosed in 2021. The treating GI note calls it moderately to severely active and gives a partial Mayo score of 7, which is a validated activity index. (confidence 0.95)

- `PT-2082/problem-list-2026-10-31` (2026-10-31): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2021."
- `PT-2082/gi-note-2026-10-31` (2026-10-31): "- Moderately to severely active ulcerative pancolitis."
- `PT-2082/gi-note-2026-10-31` (2026-10-31): "- Partial Mayo score today: 7."

### C2 (policy 3.2): **NOT MET**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopic evidence is the sigmoidoscopy from 2025-05-18, about 18 months before the request, which is outside the 12-month window. The elevated CRP is within the window, but the policy says CRP alone does not count, and no fecal calprotectin is on file. (confidence 0.60)

- `PT-2082/flexible-sigmoidoscopy-2025-05-18` (2025-05-18): "- Rectum to 38 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-2082/labs-2026-10-18` (2026-10-18): "C REACTIVE PROTEIN ................ 40.4 mg/L  (<5.0)"
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report showing active inflammation dated on or after 2025-11-18, or a fecal calprotectin result above the lab's reference range dated on or after 2025-11-18

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order appears in the GI follow-up note, and the request names the ordering provider as Dr. A. Rivera, Gastroenterology. (confidence 0.90)

- `PT-2082/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 86.1 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a birth date of 1970-11-22, the member is 55 years old on the request date of 2026-11-18, which is over 18. (confidence 0.97)

- `PT-2082/demographics-2026-08-26` (2026-08-26): "Date of birth: 1970-11-22"
- Code checks: age 55 on 2026-11-18 from DOB 1970-11-22

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records prednisone from 2021-12 to 2022-09, stopped for steroid dependence, and budesonide from 2022-10 to 2023-01, stopped for inadequate response, each with dates and a reason. The request's expedited reason says the patient is 'on steroids', while the history says 'No steroids at present'; this is about current use and does not change the documented prior failures, but the reviewer may want to note it. (confidence 0.88)

- `PT-2082/medication-history-2026-10-29` (2026-10-29): "| Prednisone | 40 mg daily, tapered | 2021-12 | 2022-09 | Steroid dependent (flared each time the dose went below 15 mg) |"
- `PT-2082/medication-history-2026-10-29` (2026-10-29): "| Budesonide | 9 mg daily | 2022-10 | 2023-01 | Inadequate response after 10 weeks |"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Adalimumab, a TNF blocker, is recorded from 2023-07 to 2023-11 and was stopped for primary non-response. That reason qualifies under the policy. (confidence 0.92)

- `PT-2082/medication-history-2026-10-29` (2026-10-29): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2023-11 | Primary non-response: no clinical improvement after induction and 8 weeks of maintenance |"

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A negative QuantiFERON (IGRA) was resulted on 2026-10-18, one month before the request and inside the 12-month window. (confidence 0.96)

- `PT-2082/labs-2026-10-18` (2026-10-18): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-10-18. Because both are negative, no monitoring or prophylaxis plan is needed. (confidence 0.96)

- `PT-2082/labs-2026-10-18` (2026-10-18): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2082/labs-2026-10-18` (2026-10-18): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The patient is currently on vedolizumab, a biologic. Both the medication history and the prescriber's note document that it will be stopped, with ustekinumab replacing it, so the two will not be used together. (confidence 0.88)

- `PT-2082/medication-history-2026-10-29` (2026-10-29): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-19); to be discontinued when ustekinumab starts."
- `PT-2082/gi-note-2026-10-31` (2026-10-31): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 86.1 kg was recorded on 2026-10-31, 18 days before the request. That is over 85 kg, so the 520 mg IV band applies. Maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.94)

- `PT-2082/gi-note-2026-10-31` (2026-10-31): "- Weight 86.1 kg."
- `PT-2082/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 86.1 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 86.1 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the prescriber's note both name ustekinumab-ttwe, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-2082/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 86.1 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopy/colonoscopy/flexible sigmoidoscopy report showing active inflammation, or a fecal calprotectin result above the lab's reference range, dated on or after 2025-11-18 (who: ordering_provider)
  > Dr. Rivera, for PA-2082 (ustekinumab-ttwe), criterion C2 (policy 3.2) needs objective evidence of active disease dated on or after 2025-11-18, and it is currently NOT_MET. The only endoscopy on file is the flexible sigmoidoscopy from 2025-05-18, which falls outside the 12-month window. The CRP of 40.4 mg/L on 2026-10-18 does not count on its own under the policy, and we have no fecal calprotectin on file. Please review and tell us whether an endoscopy report or an elevated fecal calprotectin result from on or after 2025-11-18 exists, or document how you want to proceed.

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
