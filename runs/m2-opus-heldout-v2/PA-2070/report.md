# PA-2070: ustekinumab-aekn for PT-2070

**Outcome: READY_FOR_REVIEW**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 108.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Request lists the pharmacy benefit for the whole order, but this payer splits the phases (iv_induction -> medical, sc_maintenance -> pharmacy). Submit each phase on its own benefit.
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note calls it moderately to severely active and records a Harvey-Bradshaw Index of 8, so disease severity is described. (confidence 0.95)

- `PT-2070/gi-note-2026-11-04` (2026-11-04): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-2070/gi-note-2026-11-04` (2026-11-04): "Harvey-Bradshaw Index today: 8."
- `PT-2070/problem-list-2026-11-04` (2026-11-04): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The 2026-09-21 colonoscopy, about 2 months before the request, describes ileal ulcers. Fecal calprotectin on 2026-10-04 was 462 ug/g against a reference range of <50, which also qualifies on its own. (confidence 0.95)

- `PT-2070/colonoscopy-2026-09-21` (2026-09-21): "- Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-2070/labs-2026-10-04` (2026-10-04): "CALPROTECTIN FECAL ................ 462 ug/g  (<50)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The drug is prescribed in a GI follow-up note. The request lists the ordering provider as Dr. A. Rivera, Gastroenterology. (confidence 0.88)

- `PT-2070/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-aekn: 520 mg IV once (weight 108.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1996-11-13, the member is 30 on the 2026-11-18 request date. The outside records list the same date of birth. (confidence 0.97)

- `PT-2070/demographics-2026-11-03` (2026-11-03): "Date of birth: 1996-11-13"
- Code checks: age 30 on 2026-11-18 from DOB 1996-11-13

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history names budesonide, which counts as a corticosteroid, with start and stop dates (2023-03 to 2023-06) and inadequate response as the reason it was stopped. This is a chart record supporting the history. (confidence 0.90)

- `PT-2070/medication-history-2026-11-03` (2026-11-03): "Budesonide 9 mg daily, 2023-03 to 2023-06. Reason stopped: inadequate response after 10 weeks."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Outside records document infliximab from 2023-08 to 2023-12, stopped for primary non-response, which qualifies. Drug name, dates and reason are all present. (confidence 0.90)

- `PT-2070/outside-records-2024-01-18` (2024-01-18): "- Infliximab 5 mg/kg IV every 8 weeks, 2023-08 to 2023-12. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The IGRA from 2026-10-04 is positive, so the positive-result pathway applies. A chest X-ray on 2026-10-07 shows no active TB, and rifampin for latent TB was started on 2026-10-14. (confidence 0.90)

- `PT-2070/labs-2026-10-04` (2026-10-04): "QUANTIFERON TB GOLD PLUS .......... POSITIVE  (Negative)"
- `PT-2070/chest-xray-2026-10-07` (2026-10-07): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2070/gi-note-2026-11-04` (2026-11-04): "Latent TB infection: rifampin daily for 4 months, started 2026-10-14."

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg (nonreactive) and total anti-HBc (reactive) have results. Because anti-HBc is positive, a plan is required, and the GI note documents HBV DNA and liver test monitoring every 3 months. (confidence 0.93)

- `PT-2070/labs-2026-10-04` (2026-10-04): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2070/labs-2026-10-04` (2026-10-04): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-2070/gi-note-2026-11-04` (2026-11-04): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history affirmatively states there is no concurrent biologic, JAK inhibitor or S1P receptor modulator. The 2025 dermatology mention of immunosuppression names no agent and is consistent with the documented steroid use, so it is not a conflict. (confidence 0.85)

- `PT-2070/medication-history-2026-11-03` (2026-11-03): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 108.4 kg was recorded on 2026-11-04, 14 days before the request, and falls in the over-85 kg band, which matches the 520 mg IV dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as labeled. (confidence 0.93)

- `PT-2070/gi-note-2026-11-04` (2026-11-04): "Weight 108.4 kg."
- `PT-2070/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-aekn: 520 mg IV once (weight 108.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 108.4 kg (2026-11-04) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the order name ustekinumab-aekn, which is a preferred product. No exception is needed. (confidence 0.95)

- `PT-2070/gi-note-2026-11-04` (2026-11-04): "1. Start ustekinumab-aekn: 520 mg IV once (weight 108.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## Run cost

2 model calls, 19,749 input and 6,795 output tokens, 49.9 s of model time, $0.265 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: buried_evidence.

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
