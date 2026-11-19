# PA-2059: ustekinumab-aekn for PT-2059

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 108.5 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note calls the disease moderately to severely active and records a Harvey-Bradshaw Index of 12, which is a validated activity index. (confidence 0.95)

- `PT-2059/problem-list-2026-11-04` (2026-11-04): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2021."
- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- Harvey-Bradshaw Index today: 12."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

Fecal calprotectin was 1122 ug/g against a lab reference range of <50, collected 10/08/2026. That is within 12 months of the 2026-11-18 request. The 2023 colonoscopy falls outside the window and was not relied on. (confidence 0.95)

- `PT-2059/labs-2026-10-08` (2026-10-08): "CALPROTECTIN FECAL ................ 1122 ug/g  (<50)"
- `PT-2059/labs-2026-10-08` (2026-10-08): "COLLECTED: 10/08/2026      ORDERING: Dr. A. Rivera"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order appears in a GI follow-up note. The request names the ordering provider as Dr. A. Rivera, Gastroenterology. The quoted passage does not state the specialty itself, so the reviewer may want to confirm it. (confidence 0.80)

- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-aekn: 520 mg IV once (weight 108.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

A date of birth of 03/08/1974 makes the member 52 on the request date. Outside records list the same date of birth. (confidence 0.98)

- `PT-2059/demographics-2026-09-15` (2026-09-15): "Date of birth: 03/08/1974"
- Code checks: age 52 on 2026-11-18 from DOB 1974-03-08

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Treating-provider chart notes document 6-mercaptopurine (09/2021 to 03/2022) and budesonide (04/2022 to 07/2022). Both were stopped for inadequate response, and each entry gives the drug name, dates and reason. (confidence 0.90)

- `PT-2059/gi-note-2026-01-27` (2026-01-27): "- History: Mercaptopurine 1.5 mg/kg daily, 09/2021 to 03/2022. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."
- `PT-2059/gi-note-2026-01-27` (2026-01-27): "- History: Budesonide 9 mg daily, 04/2022 to 07/2022. Reason stopped: inadequate response after 10 weeks."

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The current GI note reports adalimumab from 07/2023 to 09/2026, based on patient report only. Outside records dated 01/2024 say the patient declined adalimumab in 07/2023 and was biologic-naive. Under the policy, records inconsistent with the reported history need clinical review, and the requested outside records have not been received. (confidence 0.88)

- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- Prior biologic: Adalimumab 40 mg every 2 weeks, 07/2023 to 09/2026. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-2059/outside-records-2024-01-18` (2024-01-18): "- Biologic-naive. Adalimumab was recommended 07/2023 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON TB Gold Plus collected 10/08/2026 is negative. That is within 12 months of the request. (confidence 0.95)

- `PT-2059/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No hepatitis B surface antigen or total core antibody result was found in the passages retrieved from the chart. Both results are required. (confidence 0.90)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current GI note states the patient is on no biologic or small-molecule advanced therapy. The only other current therapy is a budesonide bridge, which this criterion does not exclude. (confidence 0.85)

- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 108.5 kg is dated 11/04/2026, within 30 days of the request. Above 85 kg the label calls for a single 520 mg IV induction dose. Maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.93)

- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- Weight 108.5 kg."
- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-aekn: 520 mg IV once (weight 108.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 108.5 kg (2026-11-04) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-aekn specifically. This is one of the plan's preferred products, so no exception is needed. (confidence 0.95)

- `PT-2059/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-aekn: 520 mg IV once (weight 108.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Provider review and documentation reconciling the conflicting adalimumab history (dates, reason stopped, supporting records) (who: ordering_provider)
  > Dr. Rivera, for PA-2059 (ustekinumab-aekn, PT-2059), policy 3.5(b) requires a documented prior TNF blocker trial. Your GI note of 11/04/2026 lists adalimumab 40 mg every 2 weeks from 07/2023 to 09/2026 with secondary loss of response, based on patient report only. The outside records dated 01/18/2024 say the patient declined adalimumab in 07/2023 and was biologic-naive, and the outside records you requested have not arrived. Please review this conflict and document the actual adalimumab history, with claims, prescription records, chart notes or your attestation as support.
- **C7**: Resulted HBsAg and total anti-HBc tests (who: lab)
  > For PA-2059 (PT-2059, ustekinumab-aekn), policy 3.7 requires resulted hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) tests on file. We could not find either result in the chart. Please send any prior results for both tests, or draw and result them if they have never been done. An anti-HBs result or vaccination history alone does not meet this requirement.

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
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
