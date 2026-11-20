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

The treating GI provider documents moderately to severely active ulcerative pancolitis. Severity is described through symptom burden (5-7 stools a day with urgency and nocturnal stooling) and a partial Mayo score of 5. (confidence 0.95)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ulcerative pancolitis."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Partial Mayo score today: 5."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The flexible sigmoidoscopy dated 2026-08-14 falls within 12 months of the 2026-11-18 request. It describes active inflammation with friability and erosions. The elevated CRP is not needed and would not count on its own. (confidence 0.95)

- `PT-3018/flexible-sigmoidoscopy-2026-08-14` (2026-08-14): "- Rectum to 28 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ordering provider on the request is Dr. M. Chen, Gastroenterology. The order appears in the GI follow-up note. (confidence 0.93)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1971-07-19, the member is 55 on the request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-3018/demographics-2026-10-23` (2026-10-23): "Date of birth: 1971-07-19"
- Code checks: age 55 on 2026-11-18 from DOB 1971-07-19

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Prednisone 20 mg daily is listed as a current medication, but no start date is given and no inadequate response, steroid dependence, or intolerance is documented. The 2026-05-01 note mentions ongoing symptoms on current therapy without naming the therapy. No other conventional therapy is documented with dates and a reason for stopping. (confidence 0.80)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Prednisone 20 mg daily, taper planned after induction"
- `PT-3018/gi-note-2026-05-01` (2026-05-01): "Follow-up of ulcerative colitis. Ongoing symptoms despite current therapy."
- Missing: Name of a conventional therapy tried (corticosteroid, thiopurine, methotrexate, or oral aminosalicylate) with approximate start and stop dates
- Missing: Documented reason for stopping or failure (inadequate response, steroid dependence or refractoriness, intolerance, or contraindication)
- Missing: Supporting claims, prescription records, or prescriber attestation for the conventional therapy history

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The GI note reports infliximab from 2023-07 to 2026-09 with secondary loss of response, based on patient report, and says outside records were requested. The 2023-11-18 outside record says the patient was biologic-naive and declined infliximab in 2023-07, which cannot be reconciled with a course starting 2023-07. The policy refers records that are inconsistent with the reported history for clinical review. (confidence 0.85)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Prior biologic: Infliximab 5 mg/kg IV every 8 weeks, 2023-07 to 2026-09. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-3018/outside-records-2023-11-18` (2023-11-18): "- Biologic-naive. Infliximab was recommended 2023-07 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A negative QuantiFERON-TB Gold Plus result is dated 2026-10-04, within 12 months of the request. (confidence 0.96)

- `PT-3018/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted as nonreactive on 2026-10-04. Because neither is positive, no monitoring or prophylaxis plan is needed. (confidence 0.97)

- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3018/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current GI note says the patient is on no biologic or small-molecule advanced therapy. Whatever the disputed infliximab history turns out to be, no concurrent agent is documented as continuing. (confidence 0.88)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 97.3 kg was recorded on 2026-10-31, 18 days before the request, and is above 85 kg, so the 520 mg IV induction band applies. Maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the label. (confidence 0.95)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "Weight 97.3 kg."
- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 97.3 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-ttwe, which is a preferred product under the policy. (confidence 0.96)

- `PT-3018/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-ttwe: 520 mg IV once (weight 97.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5a**: Documented conventional therapy trial with name, approximate start/stop dates, and reason for failure or stopping (who: ordering_provider)
  > Dr. Chen, for PA-3018 (ustekinumab-ttwe, UC), criterion 3.5(a) on conventional therapy is not yet documented. The 2026-10-31 GI note lists prednisone 20 mg daily with a taper planned, but it gives no start date and no response outcome. The 2026-05-01 note says "ongoing symptoms despite current therapy" without naming the therapy. Could you please document the conventional therapy history, including drug name, approximate start/stop dates, and the outcome (inadequate response, steroid dependence or refractoriness, intolerance, or contraindication)?
  - Would satisfy the policy: Policy 3.5(a) accepts documentation of at least one conventional therapy (a systemic corticosteroid including budesonide, azathioprine, 6-mercaptopurine, methotrexate, or for UC an oral aminosalicylate such as mesalamine). The documentation must give the drug name, approximate start/stop dates, and an inadequate response, steroid dependence (relapse during taper or within 3 months of stopping), steroid-refractory disease, intolerance, or contraindication. It must be supported by claims, prescription records, chart notes, or prescriber attestation. The policy sets no date window for this history.
- **C5b**: Provider review reconciling conflicting infliximab history (2026-10-31 GI note vs. 2023-11-18 outside record) (who: ordering_provider)
  > Dr. Chen, for PA-3018 criterion 3.5(b) (prior TNF blocker), two records disagree. Your 2026-10-31 GI note records infliximab 5 mg/kg every 8 weeks from 2023-07 to 2026-09, stopped for secondary loss of response per patient report, with outside records requested. The outside record dated 2023-11-18 says the patient was "biologic-naive" and declined infliximab when it was recommended in 2023-07. Please review and document the accurate infliximab history, and let us know whether the requested outside infusion records have arrived.
  - Would satisfy the policy: Policy 3.5(b) accepts documentation of adalimumab or infliximab (or a biosimilar of either) with drug name, approximate start/stop dates, and a reason for stopping (primary non-response, secondary loss of response, intolerance, or a specifically documented contraindication). The documentation must be supported by claims, prescription records, chart notes, or prescriber attestation and must be consistent with the rest of the record. Infusion records or claims showing the course would resolve the conflict with the 2023-11-18 outside record.

## Run cost

3 model calls, 27,770 input and 7,102 output tokens, 57.3 s of model time, $0.247 at list price (1 served from cache).

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
