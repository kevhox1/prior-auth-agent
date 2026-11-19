# PA-3006: ustekinumab-ttwe for PT-3006

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 90.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list records a diagnosis of Crohn's disease (K50.80). The treating GI note calls the disease moderately to severely active and gives a Harvey-Bradshaw Index of 14 along with symptom burden. (confidence 0.95)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Harvey-Bradshaw Index today: 14."
- `PT-3006/problem-list-2026-10-26` (2026-10-26): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The treating GI note reports a fecal calprotectin of 511 ug/g on 10/05/2026, against a lab reference of <50. That date is within 12 months of the request. The result is recorded only in the provider note and no lab report is on file, so the reviewer may want to confirm it against the original lab report. (confidence 0.70)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Her calprotectin from 10/05/2026 came back at 511 ug/g (lab reference <50)."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order is in the GI follow-up note. The request names Dr. S. Adeyemi, Gastroenterology, as the ordering provider. (confidence 0.93)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 07/11/1981, the member is 45 on the request date. The outside records list the same date of birth. (confidence 0.98)

- `PT-3006/demographics-2026-06-07` (2026-06-07): "Date of birth: 07/11/1981"
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history lists prednisone from 06/2023 to 12/2023, stopped for steroid dependence. It also lists azathioprine from 01/2024 to 03/2024, stopped for intolerance (pancreatitis). Each entry gives the drug name, dates and reason for stopping. (confidence 0.88)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 06/2023 | 12/2023 | Steroid dependent (flared each time the dose went below 15 mg) |"
- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Azathioprine | 2.5 mg/kg daily | 01/2024 | 03/2024 | Intolerance (acute pancreatitis) |"

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The 2026 medication history, based on patient report, says adalimumab ran from 05/2024 to 05/2026 and was stopped for loss of response. The outside records from 10/2024 say the patient declined adalimumab in 05/2024 and was biologic-naive. Under the policy, inconsistent records on file send the request to clinical review, and the outside records requested to settle this are not in the chart. (confidence 0.88)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"
- `PT-3006/outside-records-2024-10-18` (2024-10-18): "- Biologic-naive. Adalimumab was recommended 05/2024 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The QuantiFERON (IGRA) result from 2025-11-30 is negative. That date is within 12 months before the 2026-11-18 request. (confidence 0.92)

- `PT-3006/labs-2025-11-30` (2025-11-30): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both the HBsAg and the total anti-HBc results from 2026-09-22 are nonreactive. Because both are negative, no monitoring plan is needed. (confidence 0.96)

- `PT-3006/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3006/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history says the member is on no biologic, JAK inhibitor or S1P receptor modulator. The only current medication listed is ferrous sulfate. (confidence 0.88)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 90.4 kg was recorded on 2026-10-26, 23 days before the request. Since that is over 85 kg, the 520 mg IV induction dose is the correct band. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.94)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Weight 90.4 kg."
- `PT-3006/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 90.4 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-ttwe, which is a preferred product under the policy. (confidence 0.96)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Reconciled TNF-blocker history: whether adalimumab was actually taken (05/2024–05/2026) or declined, with supporting records (who: ordering_provider)
  > Dr. Adeyemi, for PA-3006 (ustekinumab-ttwe), the prior TNF-blocker criterion (policy 3.5(b)) has conflicting records. The medication history dated 2026-10-22 lists adalimumab 40 mg every 2 weeks from 05/2024 to 05/2026, stopped for loss of response, but this is based on what the patient reported. The outside records dated 2024-10-18 say the patient was biologic-naive and declined adalimumab in 05/2024. Could you review this and document which account is correct? The outside records requested in the 2026-10-22 note have not been added to the chart yet.
  - Would satisfy the policy: Policy 3.5(b) accepts documentation of an adalimumab or infliximab trial (or a biosimilar of either) that gives the drug name, approximate start and stop dates, and the reason for stopping (primary non-response, secondary loss of response, or intolerance), or a specifically documented contraindication. The trial must be supported by claims, prescription records, chart notes, or prescriber attestation, and it must resolve the conflict with the 2024-10-18 outside records.

## Run cost

3 model calls, 22,064 input and 7,306 output tokens, 65.1 s of model time, $0.293 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: conflicting.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
