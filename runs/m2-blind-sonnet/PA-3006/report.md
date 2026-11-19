# PA-3006: ustekinumab-ttwe for PT-3006

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 90.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): **INSUFFICIENT**
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

No passages were retrieved for this criterion. The chart's diagnosis and severity description by the treating provider cannot be verified from what was given. (confidence 0.90)

- Missing: GI provider note with Crohn's disease or UC diagnosis and moderate-to-severe severity description

### C2 (policy 3.2): **INSUFFICIENT**
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

No endoscopy report or fecal calprotectin result was retrieved. Nothing shows active inflammation within 12 months of 2026-11-18. (confidence 0.90)

- Missing: Endoscopy/colonoscopy/sigmoidoscopy report dated 2025-11-18 or later describing active inflammation, or fecal calprotectin above reference range with date

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No chart passage was retrieved documenting the prescriber's specialty or a GI consultation. The request lists Gastroenterology, but that is not chart evidence. (confidence 0.85)

- Missing: Chart documentation of prescriber specialty or gastroenterology consultation

### C4 (policy 3.4): **INSUFFICIENT**
_The member is 18 years of age or older._

No passage with date of birth or age was retrieved. (confidence 0.90)

- Missing: Date of birth or age from demographics
- Code checks: age 45 on 2026-11-18 from DOB 1981-07-11

### C5 (policy 3.5): **INSUFFICIENT**
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

No passages document a conventional therapy, its dates, or why it was stopped. (confidence 0.90)

- Missing: Corticosteroid, azathioprine, 6-MP, methotrexate (or aminosalicylate for UC) history with dates, reason stopped, and supporting records

**C5b (policy 3.5(b)): **INSUFFICIENT****: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

No passages document prior adalimumab or infliximab use or a contraindication. (confidence 0.90)

- Missing: Adalimumab/infliximab (or biosimilar) history with dates, reason stopped, and supporting records, or documented contraindication

### C6 (policy 3.6): **INSUFFICIENT**
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

No resulted IGRA or TST was retrieved. (confidence 0.90)

- Missing: Resulted negative IGRA or TST dated 2025-11-18 or later

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

No HBsAg or total anti-HBc results were retrieved. (confidence 0.90)

- Missing: Resulted HBsAg
- Missing: Resulted total hepatitis B core antibody

### C8 (policy 3.8): **INSUFFICIENT**
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

No current medication list was retrieved to show absence of concurrent biologic, JAK inhibitor, or S1P modulator. (confidence 0.90)

- Missing: Current medication list showing no concurrent biologic/JAK/S1P agent, or documentation that a prior agent is stopped

### C9 (policy 3.9): **INSUFFICIENT**
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The request states 520 mg IV for 90.4 kg, which fits the band, but no chart weight dated within 30 days of the request was retrieved to document it. (confidence 0.85)

- Missing: Body weight documented between 2026-10-19 and 2026-11-18
- Code checks: no body weight cited

### C10 (policy 3.10): **INSUFFICIENT**
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, a preferred product, but no chart passage was retrieved to quote. A reviewer can confirm this directly from the request form. (confidence 0.60)

- Missing: Chart or order document naming the specific product ustekinumab-ttwe

## To-do list (gap plan)

- **C1**: GI provider note with diagnosis and severity (who: practice_staff)
  > PA-3006 (PT-3006), criterion C1 (Policy 3.1): we need the GI provider note documenting the Crohn's disease diagnosis (K50.80) and the provider's description of moderate-to-severe activity (symptom burden, activity index, or endoscopic severity). Please locate and attach the most recent note.
  - Would satisfy the policy: Policy 3.1 accepts a treating-provider note describing moderately to severely active Crohn's disease or UC, by symptom burden, a validated activity index, or endoscopic severity.
- **C2**: Endoscopy report or fecal calprotectin showing active inflammation, within 12 months (who: practice_staff)
  > PA-3006 (PT-3006), criterion C2 (Policy 3.2): we found no endoscopy report or fecal calprotectin result dated within the last 12 months. Please locate an endoscopy, colonoscopy or sigmoidoscopy report describing active inflammation, or a fecal calprotectin above the lab's reference range, dated 2025-11-18 or later. CRP, ESR and imaging alone do not count.
  - Would satisfy the policy: Policy 3.2 accepts an endoscopy, colonoscopy or sigmoidoscopy report describing active inflammation, or a fecal calprotectin above the performing lab's reference range, dated on or after 2025-11-18.
- **C3**: Chart documentation of GI prescriber specialty or GI consultation (who: practice_staff)
  > PA-3006 (PT-3006), criterion C3 (Policy 3.3): the request lists Dr. S. Adeyemi, Gastroenterology, but we have no chart document confirming it. Please attach a note, signature block or credential record showing the prescriber's gastroenterology specialty or a GI consultation.
  - Would satisfy the policy: Policy 3.3 accepts chart documentation that the medication is prescribed by, or in consultation with, a gastroenterologist.
- **C4**: Date of birth or age from demographics (who: practice_staff)
  > PA-3006 (PT-3006), criterion C4 (Policy 3.4): no chart document showing age or date of birth was retrieved. Please attach the demographics page; a DOB of 1981-07-11 would make the patient 45 at the request date.
  - Would satisfy the policy: Policy 3.4 accepts chart demographics showing the member is 18 years or older on the request date.
- **C5a**: Conventional therapy history with dates, outcome and records (who: ordering_provider)
  > PA-3006 (PT-3006), criterion C5a (Policy 3.5(a)): no conventional therapy is documented. Please document any systemic corticosteroid (including budesonide), azathioprine, 6-MP or methotrexate use, with dates and the reason stopped (inadequate response, steroid dependence, intolerance or contraindication), and attach supporting records.
  - Would satisfy the policy: Policy 3.5(a) accepts documented inadequate response to, intolerance of, or contraindication to at least one of systemic corticosteroids (including budesonide), azathioprine, 6-MP or methotrexate, with dates and reason stopped.
- **C5b**: Adalimumab/infliximab history or documented contraindication (who: ordering_provider)
  > PA-3006 (PT-3006), criterion C5b (Policy 3.5(b)): no prior adalimumab or infliximab (or biosimilar) use is documented. Please document any trial with dates and outcome (primary non-response, loss of response or intolerance), or a specifically documented contraindication, with supporting records.
  - Would satisfy the policy: Policy 3.5(b) accepts documented inadequate response, intolerance or a specifically documented contraindication for adalimumab or infliximab (including biosimilars).
- **C6**: Resulted negative IGRA or TST dated within 12 months (who: lab)
  > PA-3006 (PT-3006), criterion C6 (Policy 3.6): no resulted TB screening test was found. Please check for a resulted negative IGRA or TST dated 2025-11-18 or later, or a pending result that can be released. An indeterminate IGRA or an unresulted order does not count.
  - Would satisfy the policy: Policy 3.6 accepts a negative IGRA or TST dated on or after 2025-11-18. If positive, it requires chest imaging excluding active TB and started latent TB treatment.
- **C7**: Resulted HBsAg and total anti-HBc (who: lab)
  > PA-3006 (PT-3006), criterion C7 (Policy 3.7): no HBsAg or total hepatitis B core antibody result is on file. Please locate resulted values for both (any date), or a pending result that can be released. Anti-HBs or vaccination history alone does not count.
  - Would satisfy the policy: Policy 3.7 accepts resulted HBsAg and total anti-HBc of any date; if either is positive, a monitoring or antiviral prophylaxis plan is also required.
- **C8**: Current medication list showing no concurrent biologic, JAK or S1P agent (who: practice_staff)
  > PA-3006 (PT-3006), criterion C8 (Policy 3.8): no current medication list was retrieved. Please attach a current list showing no other biologic, JAK inhibitor or S1P modulator, or documentation that any prior such agent has been or will be stopped.
  - Would satisfy the policy: Policy 3.8 accepts a current medication list showing no concurrent biologic, JAK inhibitor or S1P modulator, or documentation that a prior agent has been or will be stopped.
- **C9**: Body weight dated 2026-10-19 to 2026-11-18 (who: practice_staff)
  > PA-3006 (PT-3006), criterion C9 (Policy 3.9): the request states 90.4 kg for the 520 mg IV induction dose, but no chart weight within 30 days was found. Please attach a weight recorded between 2026-10-19 and 2026-11-18.
  - Would satisfy the policy: Policy 3.9 accepts a documented body weight dated between 2026-10-19 and 2026-11-18 to support the induction dose band.
- **C10**: Order or chart document naming ustekinumab-ttwe (who: practice_staff)
  > PA-3006 (PT-3006), criterion C10 (Policy 3.10): please attach the signed order or chart document naming the specific product ustekinumab-ttwe, matching the request form.
  - Would satisfy the policy: Policy 3.10 accepts a request naming a specific preferred product (ustekinumab-ttwe or ustekinumab-aekn); the order should name the product.

## Run cost

3 model calls, 20,748 input and 4,597 output tokens, 31.9 s of model time, $0.129 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent GAPS_TO_CLOSE. Case type: conflicting.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C2 | 3.2 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C5a | 3.5(a) | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C5b | 3.5(b) | CONFLICTING | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C6 | 3.6 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C7 | 3.7 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C8 | 3.8 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C9 | 3.9 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C10 | 3.10 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
