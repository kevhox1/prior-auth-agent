# PA-3091: ustekinumab-ttwe for PT-3091

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 87.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses Crohn's disease and describes it as moderately to severely active. An HBI of 10 supports the severity. (confidence 0.97)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Harvey-Bradshaw Index today: 10."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

A colonoscopy dated 2026-08-29, within 12 months of the request, describes ulceration. This meets option (a); the CRP is not relied on. (confidence 0.96)

- `PT-3091/colonoscopy-2026-08-29` (2026-08-29): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No chart passage documents the prescriber's specialty or a gastroenterology consultation. The request form lists Gastroenterology, but that is not chart documentation. (confidence 0.60)

- Missing: Chart documentation (e.g., signed GI note or provider credentials) showing the prescriber is a gastroenterologist or that a gastroenterologist was consulted

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

The date of birth gives an age of 53 at the request date, which is over 18. (confidence 0.98)

- `PT-3091/demographics-2026-02-06` (2026-02-06): "Date of birth: 1973-05-02"
- Code checks: age 53 on 2026-11-18 from DOB 1973-05-02

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The record names methotrexate, gives the dates, and states it was stopped for intolerance. Methotrexate is a listed conventional therapy. No passage contradicts this history. (confidence 0.85)

- `PT-3091/outside-records-2025-01-18` (2025-01-18): "Methotrexate 25 mg subcutaneously weekly, 2024-05 to 2024-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The record names infliximab, gives start and stop dates, and states it was stopped for intolerance. Intolerance to an anti-TNF qualifies. (confidence 0.90)

- `PT-3091/medication-history-2026-10-28` (2026-10-28): "Infliximab 5 mg/kg IV every 8 weeks, 2025-02 to 2026-07. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

A negative QuantiFERON resulted on 2026-10-08, within 12 months of the request. (confidence 0.95)

- `PT-3091/labs-2026-10-08` (2026-10-08): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No hepatitis B results appear in the passages. Neither HBsAg nor total anti-HBc is documented. (confidence 0.93)

- Missing: Hepatitis B surface antigen (HBsAg) result
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

Vedolizumab is the current biologic, and the chart documents it will be stopped when ustekinumab starts. No concurrent JAK inhibitor or S1P modulator is shown. (confidence 0.90)

- `PT-3091/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-09); to be discontinued when ustekinumab starts."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "2. Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 87.0 kg is dated 18 days before the request and falls in the over-85 kg tier, which calls for 520 mg IV. The maintenance dose of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the policy. (confidence 0.95)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "Weight 87.0 kg."
- `PT-3091/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 87.0 kg (2026-10-31) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-3091/gi-note-2026-10-31` (2026-10-31): "1. Start ustekinumab-ttwe: 520 mg IV once (weight 87.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C3**: Chart documentation of gastroenterologist prescriber or GI consultation (who: practice_staff)
  > For PA-3091 (ustekinumab-ttwe), criterion 3.3 requires the drug be prescribed by or in consultation with a gastroenterologist. The request form lists Dr. S. Adeyemi, Gastroenterology, but no chart document shows this. Could you file a signed GI note or provider credentials showing Dr. Adeyemi's specialty, or a GI consultation note?
  - Would satisfy the policy: Policy 3.3 accepts chart documentation, such as a signed GI note or provider credentials, showing the prescriber is a gastroenterologist or that a gastroenterologist was consulted.
- **C7**: HBsAg and total anti-HBc results (who: practice_staff)
  > For PA-3091, criterion 3.7 requires both HBsAg and total hepatitis B core antibody (anti-HBc) results on file. Neither appears in the chart. Please locate and file any existing results, or let us know if none exist so the ordering provider can review. If either is positive, a monitoring or antiviral prophylaxis plan must also be documented.
  - Would satisfy the policy: Policy 3.7 accepts resulted HBsAg and total anti-HBc tests of any date (no lookback limit). A vaccination history, an anti-HBs result alone, or an ordered but unresulted test does not satisfy it. If either result is positive, a monitoring or antiviral prophylaxis plan is also required.

## Run cost

3 model calls, 20,101 input and 5,634 output tokens, 35.7 s of model time, $0.116 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
