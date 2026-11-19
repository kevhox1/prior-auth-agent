# PA-3045: ustekinumab-aekn for PT-3045

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses Crohn's disease and describes it as moderately to severely active. An HBI score is also given. (confidence 0.96)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Impression:
Moderately to severely active ileocolonic Crohn's disease."
- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Harvey-Bradshaw Index today: 9."

### C2 (policy 3.2): **NOT MET**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only endoscopy showing active inflammation is dated 2025-04-18, before the 12-month window that starts 2025-11-18. No fecal calprotectin is on file, and the elevated CRP alone does not qualify. (confidence 0.80)

- `PT-3045/colonoscopy-2025-04-18` (2025-04-18): "Terminal ileum: multiple ulcers 1-3 cm with surrounding erythema and edema."
- `PT-3045/labs-2026-10-03` (2026-10-03): "C-reactive protein                    31.2 mg/L     <5.0"

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The retrieved passages do not state the prescriber's specialty or a gastroenterology consultation. The request header lists Gastroenterology, but no chart passage confirms it. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (gastroenterology) or a gastroenterology consultation

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

A birth date of 02/21/1966 makes the member 60 years old at the request date, which is over 18. (confidence 0.97)

- `PT-3045/demographics-2026-04-15` (2026-04-15): "Date of birth: 02/21/1966"
- Code checks: age 60 on 2026-11-18 from DOB 1966-02-21

### C5 (policy 3.5): MET
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Mercaptopurine, a conventional therapy, is documented with start and stop dates and a reason stopped (inadequate response). It comes from an outside record, and nothing in the chart contradicts it. (confidence 0.80)

- `PT-3045/outside-records-2023-11-18` (2023-11-18): "- Mercaptopurine 1.5 mg/kg daily, 04/2023 to 10/2023. Reason stopped: inadequate response after 6 months at a therapeutic metabolite level."

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

Adalimumab is documented with dates and a reason stopped (intolerance, drug-induced lupus). Intolerance qualifies under the policy. The June 2026 note's 'ongoing symptoms despite current therapy' does not name a drug and does not contradict this. (confidence 0.75)

- `PT-3045/medication-history-2026-11-04` (2026-11-04): "Adalimumab 40 mg every 2 weeks, 12/2023 to 05/2026. Reason stopped: intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias)."

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

A negative QuantiFERON was resulted on 2026-10-03, within 12 months of the request. The 2023 result is outside the window and is not needed. (confidence 0.95)

- `PT-3045/labs-2026-10-03` (2026-10-03): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted and nonreactive, so no monitoring plan is required. (confidence 0.96)

- `PT-3045/labs-2026-10-03` (2026-10-03): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-3045/labs-2026-10-03` (2026-10-03): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history shows no concurrent biologic, JAK inhibitor, or S1P modulator. The prior adalimumab was stopped in 05/2026. (confidence 0.92)

- `PT-3045/medication-history-2026-11-04` (2026-11-04): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 55.0 kg was recorded 12 days before the request, within 30 days. It falls in the 260 mg band, and the maintenance dose is 90 mg SC every 8 weeks starting 8 weeks after the IV dose. (confidence 0.93)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Weight 55.0 kg."
- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-11-06) -> label tier 260 mg; requested 260 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names a specific product, ustekinumab-aekn, which is a preferred product. No exception is needed. (confidence 0.95)

- `PT-3045/gi-note-2026-11-06` (2026-11-06): "Start ustekinumab-aekn: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Endoscopy report with active inflammation or elevated fecal calprotectin dated within 12 months (who: ordering_provider)
  > PA-3045 (PT-3045), criterion C2 (policy 3.2): the only endoscopy showing active inflammation is the colonoscopy dated 2025-04-18, which is before the 12-month window. No fecal calprotectin is on file, and the CRP of 31.2 mg/L (2026-10-03) does not qualify alone. Please review and advise whether any qualifying endoscopy report or fecal calprotectin result dated on or after 2025-11-18 exists or will be documented.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation, or a fecal calprotectin above the performing lab's upper reference limit, dated on or after 2025-11-18. CRP/ESR alone or imaging alone does not satisfy it.
- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consultation (who: practice_staff)
  > PA-3045 (PT-3045), criterion C3 (policy 3.3): the request header lists Dr. S. Adeyemi, Gastroenterology, but no chart passage confirms the prescriber's specialty or a GI consultation. Could you locate and file a note, signature block, or consult document showing Dr. Adeyemi's gastroenterology specialty for this prescription?
  - Would satisfy the policy: Policy 3.3 accepts chart documentation that the medication is prescribed by, or in consultation with, a gastroenterologist, such as a clinic note or consult note showing the prescriber's gastroenterology specialty.

## Run cost

3 model calls, 20,531 input and 6,552 output tokens, 40.3 s of model time, $0.127 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
