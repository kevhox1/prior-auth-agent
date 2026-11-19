# PA-3018: ustekinumab-ttwe for PT-3018

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 97.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI provider documents moderately to severely active ulcerative pancolitis. Severity is described by symptom burden (5-7 stools a day with urgency and nocturnal stooling) and a partial Mayo score of 5. (confidence 0.95)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ulcerative pancolitis."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Partial Mayo score today: 5."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The flexible sigmoidoscopy dated 2026-08-14 is about 3 months before the request, so it is inside the 12-month window. It describes active inflammation with friability and erosions, with a Mayo endoscopic subscore of 3. The CRP result is not needed for this criterion. (confidence 0.95)

- `PT-3018/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "- Rectum to 28 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab-ttwe order appears in a GI follow-up note. The request names the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.90)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1971-07-19, the member is 55 years old on the request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-3018/demographics-2026-10-23` (2026-10-23): "Date of birth: 1971-07-19"
- Code checks: age 55 on 2026-11-18 from DOB 1971-07-19

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Prednisone is listed as a current medication, but the chart gives no start date and does not record inadequate response, steroid dependence, refractory disease, intolerance or contraindication. The 2026-05-01 note mentions ongoing symptoms on current therapy but does not name the therapy. No other conventional therapy is documented. (confidence 0.80)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Prednisone 20 mg daily, taper planned after induction"
- `PT-3018/gi-note-2026-05-01` (2026-05-01): "Follow-up of ulcerative colitis. Ongoing symptoms despite current therapy."
- Missing: Start date (and any prior courses/stop dates) of prednisone or other conventional therapy
- Missing: Documentation of the reason for failure (inadequate response, steroid dependence, steroid-refractory disease, intolerance, or contraindication) for a named conventional therapy
- Missing: Supporting claims, prescription records, or prescriber attestation for conventional therapy history

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The current GI note reports infliximab from 2023-07 to 2026-09, stopped for loss of response, but this rests on patient report and the outside records are still pending. The 2023-11-18 outside record says the patient was biologic-naive and declined infliximab in 2023-07, which contradicts the reported start date. Under the policy, inconsistent records go to clinical review. (confidence 0.85)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-3018/outside-records-2023-11-18` (2023-11-18): "- Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The QuantiFERON TB Gold Plus resulted negative on 2026-10-04, which is within 12 months of the request. (confidence 0.95)

- `PT-3018/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both the HBsAg and the total anti-HBc results are on file and both are nonreactive, so no monitoring plan is required. (confidence 0.96)

- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current GI note says no biologic or small-molecule advanced therapy is being taken. The reported prior infliximab is documented as stopped in 2026-09, so there is no concurrent agent whichever version of the history is correct. (confidence 0.88)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 97.3 kg was recorded on 2026-10-31, 18 days before the request, and falls in the over-85 kg band, so 520 mg IV is correct. Maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the label. (confidence 0.95)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Weight 97.3 kg."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 97.3 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order both name ustekinumab-ttwe, which is a preferred product. (confidence 0.97)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5a**: Documented conventional therapy history: a named drug with approximate start/stop dates and the reason it failed (who: ordering_provider)
  > Dr. Chen, for PA-3018 (ustekinumab, UC), criterion 3.5(a) on conventional therapy is not yet documented. The 2026-10-31 GI note lists 'Prednisone 20 mg daily, taper planned after induction' but gives no start date and no reason for failure. The 2026-05-01 note says 'ongoing symptoms despite current therapy' but does not name the therapy. Please review and document any conventional therapy the patient has had (prednisone, budesonide, mesalamine, azathioprine, 6-MP or methotrexate), with approximate dates and why it was stopped or failed.
  - Would satisfy the policy: Policy 3.5(a) accepts documentation of at least one conventional therapy (systemic corticosteroid including budesonide, azathioprine, 6-mercaptopurine, methotrexate, or for UC an oral aminosalicylate such as mesalamine). The documentation must name the drug, give approximate start/stop dates, and state the reason: inadequate response (including steroid dependence or steroid-refractory disease), intolerance, or contraindication. It must be supported by claims, prescription records, chart notes, or prescriber attestation. The policy sets no date window for this history.
- **C5b**: A resolution of the conflicting records on prior infliximab use (dates and reason stopped) (who: ordering_provider)
  > Dr. Chen, for PA-3018, criterion 3.5(b) on prior TNF blocker use has conflicting records. The 2026-10-31 GI note records infliximab from 2023-07 to 2026-09, stopped for loss of response 'per patient report; outside records requested.' The outside record dated 2023-11-18 says the patient was 'Biologic-naive. Infliximab was recommended 2023-07 but the patient declined.' Please review and confirm the patient's actual infliximab or adalimumab history, including start and stop dates and the reason stopped, and say whether the requested outside records have come in.
  - Would satisfy the policy: Policy 3.5(b) accepts documentation of adalimumab or infliximab (or a biosimilar of either) that names the drug, gives approximate start/stop dates, and states the reason stopped (primary non-response, secondary loss of response, intolerance, or a specifically documented contraindication). It must be supported by claims, prescription or infusion records, chart notes, or prescriber attestation. Under the policy, records that remain inconsistent go to clinical review.

## Run cost

3 model calls, 23,004 input and 8,153 output tokens, 69.9 s of model time, $0.305 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
