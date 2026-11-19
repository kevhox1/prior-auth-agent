# PA-1121: ustekinumab-ttwe for PT-1121

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: EXPEDITED review. Pharmacy-benefit phase: decision within 24 hours of a complete request (policy section 7). Prescriber statement of clinical urgency is required. Work this case first.
- Ordered dose: 260 mg IV once (weight 54.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note documents ulcerative pancolitis and calls it moderately to severely active. It also records symptom burden (5-7 stools a day with urgency) and a partial Mayo score of 6. (confidence 0.95)

- `PT-1121/gi-note-2026-11-04` (2026-11-04): "Moderately to severely active ulcerative pancolitis."
- `PT-1121/gi-note-2026-11-04` (2026-11-04): "Partial Mayo score today: 6."
- `PT-1121/gi-note-2026-11-04` (2026-11-04): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."

### C2 (policy 3.2): **INSUFFICIENT**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy (2025-08-18) shows active inflammation, but it is dated before the 12-month window, which starts 2025-11-18. The elevated CRP does not count on its own, and the chart has no fecal calprotectin result. (confidence 0.80)

- `PT-1121/flexible-sigmoidoscopy-2025-08-18` (2025-08-18): "- Rectum to 27 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 2."
- `PT-1121/labs-2026-09-28` (2026-09-28): "C REACTIVE PROTEIN ................ 28.9 mg/L  (<5.0)"
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report showing active inflammation dated on or after 2025-11-18
- Missing: OR fecal calprotectin result above the lab's reference range upper limit dated on or after 2025-11-18, with the reference range

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is in a GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-1121/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 54.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 09/10/1952, the member is 74 years old on the request date. (confidence 0.98)

- `PT-1121/demographics-2026-01-08` (2026-01-08): "Date of birth: 09/10/1952"
- Code checks: age 74 on 2026-11-18 from DOB 1952-09-10

### C5 (policy 3.5): **NOT MET**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Azathioprine is a conventional therapy. The medication history gives its start and stop dates and says it was stopped for intolerance (acute pancreatitis). The chart has no corticosteroid history, but one qualifying conventional therapy is enough. (confidence 0.88)

- `PT-1121/medication-history-2026-11-02` (2026-11-02): "Azathioprine 2.5 mg/kg daily, 06/2023 to 08/2023. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): **NOT MET****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Adalimumab was tried, but the documented reason for stopping is an insurance change while disease was controlled. That is not non-response, loss of response, intolerance, or a contraindication. The 03/2026 note mentions ongoing symptoms on therapy, but it does not name the therapy or give a reason for stopping, so the reviewer may want to confirm the adalimumab history. (confidence 0.65)

- `PT-1121/medication-history-2026-11-02` (2026-11-02): "Adalimumab 40 mg every 2 weeks, 10/2023 to 09/2026. Reason stopped: stopped when insurance coverage changed; disease was controlled at the time."
- `PT-1121/gi-note-2026-03-17` (2026-03-17): "Follow-up of ulcerative colitis. Ongoing symptoms despite current therapy."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The QuantiFERON (IGRA) result dated 2026-09-28 is negative. That date is within 12 months of the request. (confidence 0.95)

- `PT-1121/labs-2026-09-28` (2026-09-28): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc have results on file, and both are nonreactive. Because neither is positive, no monitoring plan is required. (confidence 0.96)

- `PT-1121/labs-2026-09-28` (2026-09-28): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-1121/labs-2026-09-28` (2026-09-28): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The medication history says the member is on no biologic, JAK inhibitor, or S1P receptor modulator. The prior biologic, adalimumab, was stopped in 09/2026. (confidence 0.90)

- `PT-1121/medication-history-2026-11-02` (2026-11-02): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-1121/medication-history-2026-11-02` (2026-11-02): "Adalimumab 40 mg every 2 weeks, 10/2023 to 09/2026."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 54.7 kg is dated 2026-11-04, within 30 days of the request, and falls in the 55 kg or less band, which calls for 260 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.93)

- `PT-1121/gi-note-2026-11-04` (2026-11-04): "Weight 54.7 kg."
- `PT-1121/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 54.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 54.7 kg (2026-11-04) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order both name ustekinumab-ttwe, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-1121/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-ttwe: 260 mg IV once (weight 54.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Fecal calprotectin above the lab's reference range (with the range), or an endoscopy/sigmoidoscopy report showing active inflammation, dated on or after 2025-11-18 (who: lab)
  > For PA-1121 (ustekinumab-ttwe, PT-1121), criterion C2 needs objective evidence of active disease dated on or after 2025-11-18. The only endoscopy on file is the flexible sigmoidoscopy from 2025-08-18, which is outside the 12-month window, and the elevated CRP (28.9 mg/L on 2026-09-28) does not count on its own. Please send a fecal calprotectin result from on or after 2025-11-18 with the performing lab's reference range, or an endoscopy, colonoscopy, or sigmoidoscopy report from that period describing active inflammation. If neither exists, a calprotectin will need to be collected and resulted.
- **C5b**: Provider review of the TNF-blocker history: documented non-response, loss of response, intolerance, or contraindication (who: ordering_provider)
  > Dr. Adeyemi, for PA-1121 (PT-1121), criterion C5b requires that at least one TNF blocker (adalimumab or infliximab) failed through non-response, loss of response, intolerance, or a documented contraindication. The medication history dated 2026-11-02 lists adalimumab 40 mg every 2 weeks from 10/2023 to 09/2026, stopped "when insurance coverage changed; disease was controlled at the time." Your GI note from 2026-03-17 says "ongoing symptoms despite current therapy" but does not name the therapy or give a reason for stopping. Please review the adalimumab history and confirm the accurate reason it was stopped, documenting or attesting to it as appropriate.

## Run cost

3 model calls, 13,692 input and 4,514 output tokens, 40.8 s of model time, $0.173 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | NOT_MET | NOT_MET | NOT_MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
