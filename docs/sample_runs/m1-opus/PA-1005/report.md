# PA-1005: ustekinumab-aekn for PT-1005

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 65.5 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI calls it moderately to severely active and records a Harvey-Bradshaw Index of 13, a validated activity score. (confidence 0.95)

- `PT-1005/problem-list-2026-10-31` (2026-10-31): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2020."
- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

Fecal calprotectin was 685 ug/g on 09/10/2026, which is above the lab reference of <50 and within 12 months of the 2026-11-18 request. The result and the reference range are reported in the treating GI note; the lab report itself is not in the chart, so the reviewer may want it attached. The elevated CRP was not used, because CRP alone does not count. (confidence 0.75)

- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Her calprotectin from 09/10/2026 came back at 685 ug/g (lab reference <50)."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

Ustekinumab is prescribed in the GI follow-up note. The ordering provider on the request is Dr. M. Chen, Gastroenterology. (confidence 0.92)

- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-aekn: 390 mg IV once (weight 65.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 12/01/1986, the member is 39 years old on the 2026-11-18 request date, so she is 18 or older. (confidence 0.97)

- `PT-1005/demographics-2026-02-27` (2026-02-27): "Date of birth: 12/01/1986"
- Code checks: age 39 on 2026-11-18 from DOB 1986-12-01

### C5 (policy 3.5): **INSUFFICIENT**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The only conventional therapy found is current prednisone, with no start date and no documented inadequate response, steroid dependence, refractoriness, intolerance or contraindication. The note says symptoms are not controlled on current therapy but does not name the drug or describe the steroid response. (confidence 0.80)

- `PT-1005/medication-history-2026-10-30` (2026-10-30): "- Prednisone 20 mg daily, taper planned after induction"
- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Symptoms not controlled on current therapy; missing work."
- Missing: Documentation of a conventional therapy (corticosteroid/budesonide, azathioprine, 6-MP, or methotrexate) with approximate start/stop dates and reason stopped (e.g., steroid dependence or steroid-refractory disease, intolerance, contraindication)
- Missing: Supporting claims, prescription records, chart notes, or prescriber attestation for that therapy

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history names infliximab, a TNF blocker, with dates (07/2023 to 08/2026) and a reason for stopping: intolerance from drug-induced lupus. Intolerance qualifies under the policy, and nothing in the passages contradicts this history. (confidence 0.82)

- `PT-1005/medication-history-2026-10-30` (2026-10-30): "Infliximab 5 mg/kg IV every 8 weeks, 07/2023 to 08/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

QuantiFERON TB Gold Plus was negative on 2026-10-15, which is within 12 months of the request. (confidence 0.95)

- `PT-1005/labs-2026-10-15` (2026-10-15): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted as nonreactive on 2026-10-15. Because neither is positive, no monitoring or prophylaxis plan is needed. (confidence 0.96)

- `PT-1005/labs-2026-10-15` (2026-10-15): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-1005/labs-2026-10-15` (2026-10-15): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is switching from vedolizumab, a biologic, and both the medication history and the prescriber note document that it will be stopped when ustekinumab starts. Infliximab was stopped in 08/2026, and no JAK inhibitor or S1P modulator is listed. (confidence 0.88)

- `PT-1005/medication-history-2026-10-30` (2026-10-30): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/13/2026); to be discontinued when ustekinumab starts."
- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 65.5 kg was recorded on 2026-10-31, 18 days before the request, so it is within the 30-day window. It falls in the >55 to 85 kg band, which matches the 390 mg single IV dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which follows the label. (confidence 0.93)

- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Weight 65.5 kg."
- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-aekn: 390 mg IV once (weight 65.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 65.5 kg (2026-10-31) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the prescriber note name ustekinumab-aekn specifically, and it is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-1005/gi-note-2026-10-31` (2026-10-31): "- Start ustekinumab-aekn: 390 mg IV once (weight 65.5 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5a**: Documented conventional therapy trial with start/stop dates and the outcome (inadequate response, steroid dependence or refractoriness, intolerance, or contraindication), backed by records or a prescriber attestation (who: ordering_provider)
  > Dr. Chen, the ustekinumab-aekn prior authorization for PT-1005 (PA-1005, Northfield commercial) needs documentation for policy criterion 3.5(a), the conventional therapy trial. The medication history dated 2026-10-30 lists "Prednisone 20 mg daily, taper planned after induction," and your GI note dated 2026-10-31 says "Symptoms not controlled on current therapy." Neither gives a prednisone start date or describes how the patient responded, such as steroid dependence, steroid-refractory disease, intolerance or a contraindication. Please document a conventional therapy (corticosteroid/budesonide, azathioprine, 6-MP or methotrexate) with approximate start and stop dates and the outcome, in a chart note or a signed attestation.

## Run cost

3 model calls, 12,774 input and 4,111 output tokens, 34.7 s of model time, $0.158 at list price (1 served from cache).

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
