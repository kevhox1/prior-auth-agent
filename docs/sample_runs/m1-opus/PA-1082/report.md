# PA-1082: ustekinumab-aekn for PT-1082

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 260 mg IV once (weight 53.5 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

Crohn's disease (K50.80) is on the problem list. The treating GI note calls it moderately to severely active and gives a Harvey-Bradshaw Index of 12, which is a validated activity index. (confidence 0.95)

- `PT-1082/problem-list-2026-10-25` (2026-10-25): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2024."
- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Harvey-Bradshaw Index today: 12."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-09-07 is within 12 months of the 2026-11-18 request. It describes ulcers in the terminal ileum, and pathology shows chronic active inflammation. The CRP is not needed for this criterion. (confidence 0.95)

- `PT-1082/colonoscopy-2026-09-07` (2026-09-07): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-1082/colonoscopy-2026-09-07` (2026-09-07): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is in a GI follow-up note. The request lists the ordering provider as Dr. A. Rivera, Gastroenterology. (confidence 0.90)

- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Start ustekinumab-aekn: 260 mg IV once (weight 53.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1966-09-19, the member is 60 years old on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-1082/demographics-2026-11-01` (2026-11-01): "Date of birth: 1966-09-19"
- Code checks: age 60 on 2026-11-18 from DOB 1966-09-19

### C5 (policy 3.5): **NOT MET**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history records mercaptopurine from 2024-08 to 2025-03, stopped for inadequate response. It also records prednisone from 2024-03 to 2024-07 with steroid dependence. Current prednisone 20 mg reads as a later course and does not contradict the 2024 course; the empty treatment-history section in the outside records is an omission, not a conflict. (confidence 0.85)

- `PT-1082/medication-history-2026-10-22` (2026-10-22): "| Mercaptopurine | 1.5 mg/kg daily | 2024-08 | 2025-03 | Inadequate response after 6 months at a therapeutic metabolite level |"
- `PT-1082/medication-history-2026-10-22` (2026-10-22): "| Prednisone | 40 mg daily, tapered | 2024-03 | 2024-07 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy 3.5(b)): **NOT MET****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The treating GI note says outright that the patient is biologic-naive with no prior anti-TNF therapy. No trial of, or documented contraindication to, adalimumab or infliximab appears in the chart. (confidence 0.92)

- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Biologic-naive; no prior anti-TNF therapy."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The negative QuantiFERON dated 2025-11-26 falls inside the 12-month window, which starts 2025-11-18. The GI note mentions a separate negative QuantiFERON from 2023; that is an older test and does not contradict the 2025 result. (confidence 0.80)

- `PT-1082/labs-2025-11-26` (2025-11-26): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No hepatitis B surface antigen or total core antibody result was found in the passages retrieved from the chart. (confidence 0.90)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history lists no biologic, JAK inhibitor or S1P receptor modulator. The patient is biologic-naive, so this is not a switch from another agent. (confidence 0.92)

- `PT-1082/medication-history-2026-10-22` (2026-10-22): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Biologic-naive; no prior anti-TNF therapy."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 53.5 kg was recorded on 2026-10-25, 24 days before the request, and falls in the 260 mg band (55 kg or less). Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. The 56.5 kg weight from July is outside the 30-day window and does not apply. (confidence 0.92)

- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Weight 53.5 kg."
- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Start ustekinumab-aekn: 260 mg IV once (weight 53.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 53.5 kg (2026-10-25) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the GI note name ustekinumab-aekn, which is a preferred product, so no exception is needed. (confidence 0.95)

- `PT-1082/gi-note-2026-10-25` (2026-10-25): "- Start ustekinumab-aekn: 260 mg IV once (weight 53.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Provider review of the TNF blocker trial requirement (adalimumab or infliximab), with drug, dates and reason stopped, or a documented contraindication (who: ordering_provider)
  > Dr. Rivera, for the ustekinumab-aekn PA (PA-1082, PT-1082), Northfield policy 3.5(b) requires an inadequate response to, intolerance of, or a documented contraindication to adalimumab or infliximab (or a biosimilar of either). Your GI note dated 2026-10-25 says: "Biologic-naive; no prior anti-TNF therapy." We found no TNF blocker trial or documented contraindication in the chart. Please review and tell us how you want to proceed with this criterion.
- **C7**: Resulted HBsAg and total anti-HBc lab reports (who: practice_staff)
  > For the ustekinumab-aekn PA for PT-1082 (PA-1082), Northfield policy 3.7 requires resulted hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results. Any date is accepted. We could not find either result in the chart. Please find and file both lab reports, or tell Dr. Rivera if they were never drawn. An anti-HBs result, vaccine history or a pending order does not count, and if either result is positive the record must also include a monitoring or prophylaxis plan.

## Run cost

3 model calls, 13,687 input and 3,890 output tokens, 34.1 s of model time, $0.161 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | NOT_MET | NOT_MET | NOT_MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
