# PA-3091: ustekinumab-ttwe for PT-3091

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 87.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note calls it moderately to severely active and gives a Harvey-Bradshaw Index of 10, which describes severity. (confidence 0.95)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Harvey-Bradshaw Index today: 10."
- `PT-3091/problem-list-2026-10-31` (2026-10-31): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2024."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A colonoscopy dated 2026-08-29, about 3 months before the request, describes multiple ulcers in the terminal ileum. Pathology confirms active inflammation. The elevated CRP is not needed and would not count on its own. (confidence 0.95)

- `PT-3091/colonoscopy-2026-08-29` (2026-08-29): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3091/colonoscopy-2026-08-29` (2026-08-29): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The request lists Dr. S. Adeyemi, Gastroenterology, as the ordering provider. The prescribing order appears in a GI follow-up note. The quoted passage does not itself state the prescriber's specialty, so the nurse should confirm it. (confidence 0.88)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

The date of birth 1973-05-02 makes the member 53 years old on the request date. The outside records give the same date of birth. (confidence 0.97)

- `PT-3091/demographics-2026-02-06` (2026-02-06): "Date of birth: 1973-05-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-05-02

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Outside records show methotrexate from 2024-05 to 2024-12, stopped for intolerance (nausea and raised ALT). This gives the drug, dates and reason. The current prednisone has no failure reason, but it is not needed for this criterion. (confidence 0.88)

- `PT-3091/outside-records-2025-01-18` (2025-01-18): "- Methotrexate 25 mg subcutaneously weekly, 2024-05 to 2024-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history shows infliximab, a TNF blocker, from 2025-02 to 2026-07, stopped for intolerance (drug-induced lupus). Drug, dates and reason are all documented, and nothing in the record contradicts it. (confidence 0.88)

- `PT-3091/medication-history-2026-10-28` (2026-10-28): "Infliximab 5 mg/kg IV every 8 weeks, 2025-02 to 2026-07. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON TB Gold Plus test (an IGRA) resulted negative on 2026-10-08. That is within 12 months of the 2026-11-18 request. (confidence 0.95)

- `PT-3091/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No hepatitis B test results were found in the chart passages. Both HBsAg and total anti-HBc results must be on file. (confidence 0.90)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The patient is currently on vedolizumab, a biologic. Both the medication history and the prescriber's plan say it will be stopped when ustekinumab starts, which the policy allows for a switch. No JAK inhibitor or S1P modulator is listed. (confidence 0.85)

- `PT-3091/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-09); to be discontinued when ustekinumab starts."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): **CONFLICTING**
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The 2026-10-31 weight of 87.0 kg (within 30 days) would put the patient in the 520 mg band, and the maintenance plan matches the label. But the same note says weight is down 3 kg, while the earlier weight was 84.9 kg, which is in the 390 mg band. The current weight sits near the 85 kg cutoff and the band depends on it, so the weight needs to be confirmed. (confidence 0.55)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Weight 87.0 kg."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Ongoing abdominal pain and 4-6 loose stools a day; weight down 3 kg."
- `PT-3091/gi-note-2026-05-24` (2026-05-24): "Weight 84.9 kg."
- Code checks: weight 87.0 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the prescriber's order both name ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.95)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C7**: Hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) results (who: practice_staff)
  > For PA-3091 (ustekinumab-ttwe, PT-3091), criterion C7 needs both an HBsAg result and a total anti-HBc result on file. We found no hepatitis B results in the chart passages we reviewed. Can you check the chart, including outside or scanned labs, for these results and file them? Vaccination history or an anti-HBs result alone does not count, and neither does a test that was ordered but has no result.
  - Would satisfy the policy: Policy 3.7 accepts resulted HBsAg and total anti-HBc tests of any date (no lookback limit). If either result is positive, the record must also include a plan for monitoring or antiviral prophylaxis.
- **C9**: Provider confirmation of current body weight for induction dose band (who: ordering_provider)
  > Dr. Adeyemi, for PA-3091 (PT-3091), criterion C9 bases the IV induction dose on current body weight. The 2026-10-31 GI note records 'Weight 87.0 kg' (520 mg band) and also says 'weight down 3 kg', but the 2026-05-24 note records 84.9 kg (390 mg band). The weight is close to the 85 kg cutoff, so please review and confirm or document the patient's current weight.
  - Would satisfy the policy: Policy 3.9 accepts a body weight documented on or after 2026-10-19 (within 30 days of the 2026-11-18 request) that clearly places the patient in a dose band: more than 85 kg for 520 mg, more than 55 kg up to 85 kg for 390 mg, or 55 kg or less for 260 mg. The requested induction dose must match that band.

## Run cost

3 model calls, 22,372 input and 7,731 output tokens, 66.4 s of model time, $0.291 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent NEEDS_PHYSICIAN. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | CONFLICTING | CONFLICTING | wrong |
| C10 | 3.10 | MET | MET | MET | ok |
