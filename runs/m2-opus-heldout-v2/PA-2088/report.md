# PA-2088: ustekinumab-aekn for PT-2088

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 104.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents ulcerative colitis. The treating GI describes it as moderately to severely active and gives a partial Mayo score of 8. (confidence 0.95)

- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Moderately to severely active ulcerative pancolitis."
- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Partial Mayo score today: 8."
- `PT-2088/problem-list-2026-10-26` (2026-10-26): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2023."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The flexible sigmoidoscopy of 2026-09-28, within 12 months, shows friability and erosions. Fecal calprotectin of 483 ug/g on 2026-09-12 is above the lab's reference range of <50, so either one satisfies the criterion. (confidence 0.96)

- `PT-2088/flexible-sigmoidoscopy-2026-09-28` (2026-09-28): "- Rectum to 27 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-2088/labs-2026-09-12` (2026-09-12): "CALPROTECTIN FECAL ................ 483 ug/g  (<50)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is in a GI follow-up note. The ordering provider is Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Start ustekinumab-aekn: 520 mg IV once (weight 104.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth 05/02/1964 makes the member 62 on the request date. The outside records show the same date of birth. (confidence 0.98)

- `PT-2088/demographics-2026-08-03` (2026-08-03): "Date of birth: 05/02/1964"
- Code checks: age 62 on 2026-11-18 from DOB 1964-05-02

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The outside records document budesonide, which counts as a corticosteroid, from 08/2023 to 11/2023, stopped for inadequate response. The 2026-10-26 medication history line '(no prior IBD therapy documented)' only notes missing documentation and does not say the drug was never taken. The reviewer should decide whether it is an inconsistency that needs clinical review under C5. (confidence 0.70)

- `PT-2088/outside-records-2024-06-18` (2024-06-18): "- Budesonide 9 mg daily, 08/2023 to 11/2023. Reason stopped: inadequate response after 10 weeks."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The outside records document infliximab from 01/2024 to 05/2024, stopped for primary non-response. The 2026-10-26 medication history says '(no prior IBD therapy documented)', which notes missing documentation rather than saying infliximab was never given. The reviewer should decide whether it is an inconsistency that needs clinical review under C5. (confidence 0.65)

- `PT-2088/outside-records-2024-06-18` (2024-06-18): "- Infliximab 5 mg/kg IV every 8 weeks, 01/2024 to 05/2024. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The IGRA within 12 months was positive. The chest X-ray excluded active TB, and latent TB treatment with rifampin started 09/22/2026, which meets the policy's positive-test pathway. (confidence 0.88)

- `PT-2088/labs-2026-09-12` (2026-09-12): "QUANTIFERON TB GOLD PLUS .......... POSITIVE  (Negative)"
- `PT-2088/chest-xray-2026-09-15` (2026-09-15): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Latent TB infection: rifampin daily for 4 months, started 09/22/2026."

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg (nonreactive) and total anti-HBc (reactive) are resulted. Because anti-HBc is positive, a monitoring plan is required, and the chart has one: HBV DNA and liver tests every 3 months. (confidence 0.93)

- `PT-2088/labs-2026-09-12` (2026-09-12): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2088/labs-2026-09-12` (2026-09-12): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): **NOT MET**
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

Upadacitinib, a JAK inhibitor, is on the current medication list. The GI plan explicitly continues it alongside ustekinumab, which the policy excludes. (confidence 0.95)

- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Continue upadacitinib 15 mg daily and add ustekinumab."
- `PT-2088/medication-history-2026-10-26` (2026-10-26): "- Upadacitinib 15 mg daily"

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 104.3 kg was recorded 23 days before the request, inside the 30-day window. Weight over 85 kg calls for a 520 mg single IV dose, and maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.93)

- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Weight 104.3 kg."
- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Start ustekinumab-aekn: 520 mg IV once (weight 104.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 104.3 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the chart name ustekinumab-aekn, which is a preferred product. (confidence 0.96)

- `PT-2088/gi-note-2026-10-26` (2026-10-26): "- Start ustekinumab-aekn: 520 mg IV once (weight 104.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C8**: Provider review of upadacitinib use alongside ustekinumab-aekn (who: ordering_provider)
  > Dr. Adeyemi, for PA-2088 (PT-2088, ustekinumab-aekn), criterion C8 (policy 3.8) says ustekinumab cannot be used together with a JAK inhibitor. If the member is switching, the record has to show the prior agent has been or will be stopped. Your GI note dated 2026-10-26 says "Continue upadacitinib 15 mg daily and add ustekinumab," and the 2026-10-26 medication history lists upadacitinib 15 mg daily as current. Please review this and document your plan for upadacitinib in the chart so we can update the request.

## Run cost

3 model calls, 22,381 input and 8,148 output tokens, 66.1 s of model time, $0.303 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

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
| C8 | 3.8 | NOT_MET | NOT_MET | NOT_MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
