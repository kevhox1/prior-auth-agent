# PA-3040: ustekinumab-ttwe for PT-3040

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 106.6 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI's 2026-10-29 note documents moderately to severely active ileocolonic Crohn's disease. It also records a Harvey-Bradshaw Index of 12, a validated activity score, which meets the provider-described severity requirement. (confidence 0.92)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Harvey-Bradshaw Index today: 12."

### C2 (policy 3.2): **INSUFFICIENT**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy showing active disease is from 2022-12, outside the 12-month lookback. The CRP does not satisfy this criterion by itself, and no fecal calprotectin result is in the chart. (confidence 0.85)

- `PT-3040/gi-note-2026-06-02` (2026-06-02): "Last colonoscopy 2022-12 showed active disease."
- `PT-3040/labs-2026-10-09` (2026-10-09): "C-reactive protein                    15.6 mg/L     <5.0"
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 describing active inflammation (ulceration, erosions, or friability)
- Missing: Fecal calprotectin result dated on or after 2025-11-18 above the performing laboratory's upper reference limit

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab order is written in the 2026-10-29 GI follow-up note, and the request names Dr. A. Rivera, Gastroenterology as ordering provider. This satisfies the gastroenterologist-prescriber requirement. (confidence 0.85)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A date of birth of 1977-08-22 makes the member 49 years old on the 2026-11-18 request date, which meets the 18-or-older requirement. (confidence 0.97)

- `PT-3040/demographics-2026-03-09` (2026-03-09): "Date of birth: 1977-08-22"
- Code checks: age 49 on 2026-11-18 from DOB 1977-08-22

### C5 (policy 3.5): **INSUFFICIENT**
_Both of the following are documented: (a) conventional therapy and (b) anti-TNF therapy, as specified in the sub-criteria. The record must name each drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: An inadequate response to, intolerance of, or contraindication to at least one conventional therapy: systemic corticosteroids, azathioprine, 6-mercaptopurine, or methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The outside provider records document methotrexate stopped for intolerance (2020-07 to 2020-12) and azathioprine stopped for intolerance (2021-01 to 2021-03). These are conventional therapies with dates and reasons, and no contrary record is on file; the support is provider history rather than claims, so confidence is moderate. (confidence 0.75)

- `PT-3040/outside-records-2021-04-18` (2021-04-18): "Methotrexate 25 mg subcutaneously weekly, 2020-07 to 2020-12. Reason stopped: intolerance (nausea and ALT above 3 times the upper limit of normal)."
- `PT-3040/outside-records-2021-04-18` (2021-04-18): "Azathioprine 2.5 mg/kg daily, 2021-01 to 2021-03. Reason stopped: intolerance (acute pancreatitis)."

**C5b (policy 3.5(b)): **INSUFFICIENT****: An inadequate response to, intolerance of, or contraindication to at least one tumor necrosis factor (TNF) blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The 2026-10-28 medication history lists adalimumab stopped for drug-induced lupus, which would qualify as intolerance. However, that entry was reconciled by an RN and no claims or treating-provider note supporting it are in the chart. (confidence 0.50)

- `PT-3040/medication-history-2026-10-28` (2026-10-28): "Adalimumab 40 mg every 2 weeks, 2023-07 to 2026-09. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."
- Missing: Pharmacy or medical claims for adalimumab, or a treating-provider chart note documenting the adalimumab trial and lupus intolerance
- Missing: Or prescriber attestation of the adalimumab history

### C6 (policy 3.6): **INSUFFICIENT**
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started._

The only TB item is an order placed on 2026-10-29 with no result. An order does not count as a screening result, so no negative TB test is on file. (confidence 0.90)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "QuantiFERON-TB Gold Plus ordered today."
- Missing: Resulted QuantiFERON-TB Gold Plus (or tuberculin skin test) result dated within 12 months before 2026-11-18, showing a negative result

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit for this criterion. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc are both resulted on 2026-10-09. Because anti-HBc is reactive, the 2026-10-29 GI note documents a monitoring plan (HBV DNA and liver tests every 3 months), as the criterion requires. (confidence 0.85)

- `PT-3040/labs-2026-10-09` (2026-10-09): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3040/labs-2026-10-09` (2026-10-09): "Hepatitis B core antibody, total      Reactive      Nonreactive"
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The member is currently on vedolizumab, a biologic, and both records state it will be stopped when ustekinumab starts. No JAK inhibitor or S1P modulator appears in the chart, so the switch rule is satisfied. (confidence 0.85)

- `PT-3040/medication-history-2026-10-28` (2026-10-28): "Vedolizumab 300 mg IV every 8 weeks (last infusion 2026-10-15); to be discontinued when ustekinumab starts."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling for the indication. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

A weight of 106.6 kg recorded on 2026-10-29 is within 30 days of the request. The 520 mg induction matches the over-85 kg band, and the 90 mg every-8-week maintenance schedule starts 8 weeks after the IV dose as labeled. (confidence 0.90)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Weight 106.6 kg."
- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 106.6 kg (2026-10-29) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): **NOT MET**
_The requested product is a preferred product (ustekinumab-aekn or ustekinumab-ttwe, intravenous or subcutaneous form). A non-preferred product, including the reference (originator) product, is covered only when one of the following is documented: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a). The request must name the specific product; a request for 'ustekinumab' without a product is incomplete._

**C10a (policy 3.10(a)): **NOT MET****: An inadequate response to, or intolerance of, both preferred products (ustekinumab-aekn and ustekinumab-ttwe). Intolerance of only one preferred product does not satisfy this requirement.

The requested product, ustekinumab-ttwe, is itself a preferred product, so this non-preferred pathway does not apply. The chart documents no prior ustekinumab trial, and no inadequate response or intolerance to ustekinumab-aekn or ustekinumab-ttwe is recorded. (confidence 0.70)

- `PT-3040/gi-note-2026-10-29` (2026-10-29): "Start ustekinumab-ttwe: 520 mg IV once (weight 106.6 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

**C10b (policy 3.10(b)): **NOT MET****: A contraindication or documented hypersensitivity to an inactive ingredient that is present in both preferred products and absent from the requested product.

No contraindication or hypersensitivity to an inactive ingredient is documented in the chart. This pathway is not needed because the requested product is preferred. (confidence 0.70)


## To-do list (gap plan)

- **C2**: Endoscopy, colonoscopy, or flexible sigmoidoscopy report showing active inflammation, or a fecal calprotectin result above the lab's upper reference limit (who: ordering_provider)
  > Criterion C2 (policy 3.2) is open for PT-3040. The only endoscopy showing active disease is the 2022-12 colonoscopy, which is outside the 12-month lookback ending 2025-11-18, and no fecal calprotectin is on file. Please review whether a qualifying report or result dated on or after 2025-11-18 is available or needed; the CRP of 15.6 mg/L alone does not satisfy this criterion.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 describing active inflammation (ulceration, erosions, or friability), or a fecal calprotectin result dated on or after 2025-11-18 above the performing laboratory's upper reference limit. The 2022-12 colonoscopy and the CRP of 2026-10-09 do not meet this criterion.
- **C5b**: Pharmacy or medical claims for adalimumab, or a treating-provider note or prescriber attestation documenting the adalimumab trial and lupus intolerance (who: pharmacy)
  > Criterion C5b (policy 3.5(b)) is open for PT-3040. The 2026-10-28 medication history lists adalimumab 40 mg every 2 weeks from 2023-07 to 2026-09, stopped for drug-induced lupus, but no pharmacy claims or treating-provider note supporting it are in the chart. Please pull the adalimumab fill or claims history, or confirm the trial and lupus intolerance in a provider note or attestation.
  - Would satisfy the policy: Policy 3.5(b) accepts documentation of an intolerance to adalimumab, such as pharmacy or medical claims for adalimumab showing the trial, or a treating-provider chart note or prescriber attestation documenting the trial and the drug-induced lupus intolerance. The 2026-10-28 medication history entry, reconciled by an RN, does not on its own meet this criterion.
- **C6**: Resulted negative QuantiFERON-TB Gold Plus or tuberculin skin test result (who: lab)
  > Criterion C6 (policy 3.6) is open for PT-3040. The QuantiFERON-TB Gold Plus ordered on 2026-10-29 has no result in the chart, and no negative TB screen is on file. Please confirm whether this result has been released; a negative result dated on or after 2025-11-18 is needed.
  - Would satisfy the policy: Policy 3.6 accepts a negative interferon-gamma release assay or tuberculin skin test dated on or after 2025-11-18. An indeterminate IGRA is not a negative result, and the 2026-10-29 order without a result does not count.
- **C10a**: No additional documentation applies; the requested product ustekinumab-ttwe is itself a preferred product (who: ordering_provider)
  > Criterion C10a (policy 3.10(a)) is marked NOT MET for PT-3040, but the requested product ustekinumab-ttwe is a preferred product, so this non-preferred pathway does not apply. The chart documents no prior ustekinumab trial and no intolerance or inadequate response to ustekinumab-aekn or ustekinumab-ttwe. Please review the criterion status with this in mind.
- **C10b**: Documented contraindication or hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product (who: ordering_provider)
  > Criterion C10b (policy 3.10(b)) is marked NOT MET for PT-3040, and no contraindication or hypersensitivity to an inactive ingredient is documented in the chart. This pathway is not needed because the requested product ustekinumab-ttwe is preferred. Please review whether any action is needed on this criterion.

## Run cost

3 model calls, 24,593 input and 17,613 output tokens, 69.8 s of model time, $0.013 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | NOT_MET | - | wrong |
