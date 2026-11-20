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

The treating GI provider documents moderately to severely active ileocolonic Crohn's disease. Severity is supported by a Harvey-Bradshaw Index of 14 and by the symptom burden described. (confidence 0.95)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Harvey-Bradshaw Index today: 14."
- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Persistent symptoms: 5-7 stools a day with urgency and nocturnal stooling."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The fecal calprotectin dated 10/05/2026 was 511 ug/g against a lab upper limit of <50, and that date is within 12 months of the request. The result is recorded in the GI note with its date and reference range, but the lab report itself is not in the chart, so the reviewer may want the source report. The CRP and the 2023 colonoscopy do not count toward this criterion. (confidence 0.70)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Her calprotectin from 10/05/2026 came back at 511 ug/g (lab reference <50)."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is in the GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.93)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 07/11/1981, the member is 45 on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-3006/demographics-2026-06-07` (2026-06-07): "Date of birth: 07/11/1981"
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records prednisone from 06/2023 to 12/2023, stopped for steroid dependence. It also records azathioprine from 01/2024 to 03/2024, stopped for intolerance (pancreatitis). Each entry has the drug name, dates and reason for stopping. (confidence 0.88)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 06/2023 | 12/2023 | Steroid dependent (flared each time the dose went below 15 mg) |"
- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Azathioprine | 2.5 mg/kg daily | 01/2024 | 03/2024 | Intolerance (acute pancreatitis) |"

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history, based on patient report, says adalimumab was taken from 05/2024 to 05/2026 and stopped for loss of response. The outside records say the patient declined adalimumab in 05/2024 and was still biologic-naive in 10/2024. The outside records that were requested to settle this are not in the chart, and under policy an inconsistent history goes to clinical review. (confidence 0.85)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "| Adalimumab | 40 mg every 2 weeks | 05/2024 | 05/2026 | Per patient report, worked at first and then stopped working; outside records requested |"
- `PT-3006/outside-records-2024-10-18` (2024-10-18): "- Biologic-naive. Adalimumab was recommended 05/2024 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A negative QuantiFERON was collected on 2025-11-30. That is within 12 months before the 2026-11-18 request. (confidence 0.92)

- `PT-3006/labs-2025-11-30` (2025-11-30): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted on 2026-09-22, and both were nonreactive. Because neither is positive, no monitoring plan is needed. (confidence 0.96)

- `PT-3006/labs-2026-09-22` (2026-09-22): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3006/labs-2026-09-22` (2026-09-22): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication list states there is no current biologic, JAK inhibitor or S1P modulator, and ferrous sulfate is the only medication listed. The adalimumab entry, if it was taken at all, shows it stopped in 05/2026. (confidence 0.88)

- `PT-3006/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-3006/medication-history-2026-10-22` (2026-10-22): "- Ferrous sulfate 325 mg daily"

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 90.4 kg on 2026-10-26 is 23 days before the request and above 85 kg, so the 520 mg IV induction dose matches the weight band. The maintenance dose is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which follows the label. (confidence 0.93)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "Weight 90.4 kg."
- `PT-3006/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 90.4 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the GI note name ustekinumab-ttwe. That is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-3006/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 90.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Resolution of the conflicting adalimumab history: drug, start/stop dates and reason for stopping, backed by supporting records (who: ordering_provider)
  > Dr. Adeyemi, the PA for ustekinumab-ttwe (PA-3006, PT-3006) has a conflict on the TNF-blocker trial criterion (policy 3.5(b)). The medication history dated 2026-10-22 lists adalimumab 40 mg every 2 weeks from 05/2024 to 05/2026, stopped for loss of response, based on what the patient reported. The outside records dated 2024-10-18 say the patient declined adalimumab in 05/2024 and was still biologic-naive then. The outside records you requested are not in the chart yet. Please review and document the actual adalimumab history, including start/stop dates and why it was stopped, along with any supporting records you have.
  - Would satisfy the policy: Policy 3.5(b) accepts documentation of an adalimumab or infliximab trial (or a biosimilar of either) that gives the drug name, approximate start and stop dates, and the reason for stopping (primary non-response, secondary loss of response, or intolerance), or a specifically documented contraindication. This must be supported by claims, prescription records, chart notes, or prescriber attestation. Because the current history is inconsistent, it goes to clinical review under policy.

## Run cost

3 model calls, 13,921 input and 3,906 output tokens, 33.9 s of model time, $0.159 at list price (1 served from cache).

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
