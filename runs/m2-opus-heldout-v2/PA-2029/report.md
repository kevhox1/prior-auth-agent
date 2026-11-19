# PA-2029: ustekinumab-ttwe for PT-2029

**Outcome: READY_FOR_REVIEW**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 110.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note calls it moderately to severely active and backs this with a Harvey-Bradshaw Index of 8 and uncontrolled symptoms. (confidence 0.95)

- `PT-2029/problem-list-2026-11-03` (2026-11-03): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2021."
- `PT-2029/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2029/gi-note-2026-11-03` (2026-11-03): "Harvey-Bradshaw Index today: 8."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The 2026-08-13 colonoscopy, about 3 months before the request, shows ileal ulcers. Separately, the 2026-10-10 fecal calprotectin of 739 ug/g is above the lab's limit of <50. Either one alone satisfies the criterion. (confidence 0.96)

- `PT-2029/colonoscopy-2026-08-13` (2026-08-13): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-2029/labs-2026-10-10` (2026-10-10): "CALPROTECTIN FECAL ................ 739 ug/g  (<50)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is written in a GI follow-up note. The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The quoted line itself does not name the prescriber's specialty, so the nurse should confirm that Dr. Adeyemi wrote the note. (confidence 0.88)

- `PT-2029/gi-note-2026-11-03` (2026-11-03): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 110.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

Born 1993-06-19, the member is 33 on the request date of 2026-11-18. (confidence 0.98)

- `PT-2029/demographics-2025-10-24` (2025-10-24): "Date of birth: 1993-06-19"
- Code checks: age 33 on 2026-11-18 from DOB 1993-06-19

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Azathioprine (2021-03 to 2021-05) was stopped because of acute pancreatitis, which is intolerance. Prednisone (2021-06 to 2021-12) shows steroid dependence. Each entry gives the drug, dates and reason for stopping in the chart's medication history. (confidence 0.93)

- `PT-2029/medication-history-2026-11-03` (2026-11-03): "| Azathioprine | 2.5 mg/kg daily | 2021-03 | 2021-05 | Intolerance (acute pancreatitis) |"
- `PT-2029/medication-history-2026-11-03` (2026-11-03): "| Prednisone | 40 mg daily, tapered | 2021-06 | 2021-12 | Steroid dependent (flared each time the dose went below 15 mg) |"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Adalimumab, a TNF blocker, was given from 2023-07 to 2026-07. It was stopped for intolerance (drug-induced lupus), which qualifies. No record contradicts this history. (confidence 0.92)

- `PT-2029/medication-history-2026-11-03` (2026-11-03): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON TB Gold Plus (IGRA) dated 2026-10-10 is negative. This is within 12 months of the 2026-11-18 request. (confidence 0.96)

- `PT-2029/labs-2026-10-10` (2026-10-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc are both resulted as nonreactive on 2026-10-10. Because neither is positive, no monitoring plan is required. (confidence 0.97)

- `PT-2029/labs-2026-10-10` (2026-10-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2029/labs-2026-10-10` (2026-10-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The medication history says the member is on no biologic or small-molecule advanced therapy now. The prior biologic, adalimumab, was stopped in 2026-07. Current budesonide is a corticosteroid and is not an excluded agent. (confidence 0.93)

- `PT-2029/medication-history-2026-11-03` (2026-11-03): "- No biologic or small-molecule advanced therapy at present."
- `PT-2029/medication-history-2026-11-03` (2026-11-03): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight was 110.7 kg on 2026-11-03, 15 days before the request. Over 85 kg calls for 520 mg IV, which matches the order. Maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, follows the label. (confidence 0.95)

- `PT-2029/gi-note-2026-11-03` (2026-11-03): "Weight 110.7 kg."
- `PT-2029/gi-note-2026-11-03` (2026-11-03): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 110.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 110.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-ttwe, which is a preferred product. No exception documentation is needed. (confidence 0.97)

- `PT-2029/gi-note-2026-11-03` (2026-11-03): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 110.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## Run cost

2 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (2 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: clean.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
