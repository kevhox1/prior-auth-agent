# PA-3080: ustekinumab-aekn for PT-3080

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: EXPEDITED review. Pharmacy-benefit phase: decision within 24 hours of a complete request (policy section 7). Prescriber statement of clinical urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 104.9 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents ulcerative pancolitis (K51.00). The treating GI note describes the disease as moderately to severely active and gives a partial Mayo score of 7. (confidence 0.95)

- `PT-3080/problem-list-2026-10-26` (2026-10-26): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2020."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ulcerative pancolitis."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Partial Mayo score today: 7."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

Fecal calprotectin was 64 ug/g, above the lab's upper limit of <50. It was collected 2026-09-10, within 12 months of the 2026-11-18 request. The 2023 sigmoidoscopy is outside the window and was not relied on. (confidence 0.93)

- `PT-3080/labs-2026-09-10` (2026-09-10): "CALPROTECTIN FECAL ................ 64 ug/g  (<50)"
- `PT-3080/labs-2026-09-10` (2026-09-10): "COLLECTED: 2026-09-10      ORDERING: Dr. S. Adeyemi"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is written in a GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 2000-10-17, the member is 26 on the 2026-11-18 request date, so is 18 or older. (confidence 0.97)

- `PT-3080/demographics-2025-11-27` (2025-11-27): "Date of birth: 2000-10-17"
- Code checks: age 26 on 2026-11-18 from DOB 2000-10-17

### C5 (policy 3.5): **INSUFFICIENT**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

None of the chart passages name a conventional therapy with dates and a reason for stopping. The GI notes only mention an unnamed 'current therapy'. The request's expedited reason says the patient is on steroids, but the medication history says no steroids at present, so this needs clarifying and clinical review. (confidence 0.75)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "- No steroids at present"
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Symptoms not controlled on current therapy; missing work."
- Missing: Documentation of a named conventional therapy (systemic corticosteroid/budesonide, azathioprine, 6-mercaptopurine, methotrexate, or oral mesalamine/aminosalicylate) with approximate start and stop dates
- Missing: Reason the conventional therapy was stopped (inadequate response incl. steroid dependence/refractory, intolerance, or contraindication)
- Missing: Supporting claims, prescription records, chart notes, or prescriber attestation for the conventional therapy; clarification of current steroid use, since the request says the patient is on steroids but the 2026-10-24 medication history says no steroids at present

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records adalimumab from 2023-07 to 2026-05. It was stopped for intolerance (drug-induced lupus), which is a qualifying reason. (confidence 0.90)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON (IGRA) dated 2026-09-10 is negative, within 12 months of the request. The GI note cites only an older 2023 test; leaving out the newer result is not a conflict. (confidence 0.92)

- `PT-3080/labs-2026-09-10` (2026-09-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted as nonreactive on 2026-09-10. Because neither is positive, no monitoring plan is required. (confidence 0.96)

- `PT-3080/labs-2026-09-10` (2026-09-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3080/labs-2026-09-10` (2026-09-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The medication history lists no current biologic or small-molecule advanced therapy. The prior adalimumab was stopped in 2026-05. (confidence 0.90)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "- No biologic or small-molecule advanced therapy at present."
- `PT-3080/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 104.9 kg was recorded on 2026-10-26, 23 days before the request. That is above 85 kg, so the 520 mg IV dose matches the weight band. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose. (confidence 0.94)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Weight 104.9 kg."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 104.9 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the GI note name ustekinumab-aekn, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5a**: A named prior conventional therapy with approximate start/stop dates and the reason it was stopped, plus clarification of current steroid use (who: ordering_provider)
  > Dr. Adeyemi, for PA-3080 (ustekinumab-aekn, UC), criterion 3.5(a) needs a named conventional therapy with approximate start and stop dates and the reason it was stopped. The 2026-10-26 GI note says only 'Symptoms not controlled on current therapy' and does not name the drug. The request's expedited reason says the patient is on steroids, but the 2026-10-24 medication history says 'No steroids at present.' Please review and document or attest which conventional therapies were used, with dates and outcomes, and clarify whether the patient is on steroids now.
  - Would satisfy the policy: Policy 3.5(a) accepts documentation of inadequate response to, intolerance of, or contraindication to at least one conventional therapy. For UC this means a systemic corticosteroid or budesonide (steroid dependence and steroid-refractory disease count as inadequate response), azathioprine, 6-mercaptopurine, methotrexate, or an oral aminosalicylate such as mesalamine. The documentation must give the drug name, approximate start and stop dates, and the reason for stopping, supported by claims, prescription records, chart notes, or prescriber attestation.

## Run cost

3 model calls, 57,331 input and 16,234 output tokens, 135.2 s of model time, $0.561 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
