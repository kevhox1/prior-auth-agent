# PA-3096: ustekinumab-ttwe for PT-3096

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 101.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note diagnoses moderately to severely active Crohn's disease. It supports this with a Harvey-Bradshaw Index of 13. (confidence 0.97)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy of 2026-08-16 is within 12 months of the request and describes ulceration. That is active inflammation, so (a) is satisfied. CRP was not relied on. (confidence 0.96)

- `PT-3096/colonoscopy-2026-08-16` (2026-08-16): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."

### C3 (policy 3.3): **INSUFFICIENT**
_The medication is prescribed by, or in consultation with, a gastroenterologist._

No passage states the prescriber's specialty or a gastroenterology consultation. The request header lists Gastroenterology, but no chart quote confirms it. (confidence 0.60)

- Missing: Chart documentation of prescriber specialty (gastroenterology) or a gastroenterology consultation note authored by the ordering provider

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

Date of birth 2006-05-08 makes the member 20 years old at the request date of 2026-11-18. (confidence 0.98)

- `PT-3096/demographics-2026-05-27` (2026-05-27): "Date of birth: 2006-05-08"
- Code checks: age 20 on 2026-11-18 from DOB 2006-05-08

### C5 (policy 3.5): **INSUFFICIENT**
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

Prednisone is listed as a current medication. No start date, outcome, or documented inadequate response, intolerance or contraindication is given. The earlier note says only 'ongoing symptoms despite current therapy' without naming the therapy. (confidence 0.80)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- Prednisone 20 mg daily, taper planned after induction"
- Missing: Documentation of a conventional therapy (corticosteroid, azathioprine, 6-MP, or methotrexate) with drug name, approximate start and stop dates, and reason stopped or inadequate response

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The treating GI note specifically documents a contraindication to anti-TNF therapy due to demyelinating disease. The problem list confirms multiple sclerosis. (confidence 0.88)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3096/problem-list-2026-11-03` (2026-11-03): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy 3.6): **NOT MET**
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

The only TB screening result is dated 2025-10-20, more than 12 months before the 2026-11-18 request. No more recent determinate result is on file. (confidence 0.90)

- `PT-3096/labs-2025-10-20` (2025-10-20): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted. Anti-HBc is positive, and the GI note documents a monitoring plan. (confidence 0.93)

- `PT-3096/labs-2026-10-13` (2026-10-13): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3096/labs-2026-10-13` (2026-10-13): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication list in the GI note states no biologic or small-molecule advanced therapy. Nothing in the chart shows a concurrent biologic, JAK inhibitor or S1P modulator. (confidence 0.90)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight of 101.7 kg was recorded 15 days before the request, within 30 days. It falls in the over-85 kg band, which takes 520 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose. (confidence 0.95)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Weight 101.7 kg."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 101.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-ttwe, which is a preferred product. No exception is needed. (confidence 0.96)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C3**: Documentation of gastroenterology prescriber specialty or GI consultation note (who: practice_staff)
  > For PA-3096 (PT-3096), criterion C3 (policy 3.3) needs chart documentation that ustekinumab is prescribed by or in consultation with a gastroenterologist. The request header lists Dr. S. Adeyemi, Gastroenterology, but no chart note confirms it. Can you locate and file a note or signature block showing the specialty?
  - Would satisfy the policy: Policy 3.3 accepts chart documentation of the prescriber's gastroenterology specialty, or a gastroenterology consultation note authored by the ordering provider.
- **C5a**: Documented conventional therapy (drug, dates, outcome) with inadequate response, intolerance or contraindication (who: ordering_provider)
  > For PA-3096 (PT-3096), criterion C5a (policy 3.5(a)) needs a documented conventional therapy. The GI note of 2026-11-03 lists prednisone 20 mg daily with a taper planned, but gives no start date, outcome, or inadequate response, intolerance or contraindication. Please review and document the drug, approximate start and stop dates, and the reason for stopping or the inadequate response for any corticosteroid (including budesonide), azathioprine, 6-MP or methotrexate used.
  - Would satisfy the policy: Policy 3.5(a) accepts documentation of at least one conventional therapy (systemic corticosteroid including budesonide, azathioprine, 6-MP, or methotrexate) with drug name, approximate start and stop dates, and an inadequate response (including steroid dependence or refractory disease), intolerance, or contraindication.
- **C6**: Negative IGRA or TST dated within 12 months before the request (who: ordering_provider)
  > For PA-3096 (PT-3096), criterion C6 (policy 3.6) is not met. The only TB screen on file is the QuantiFERON TB Gold Plus negative result dated 2025-10-20, which is more than 12 months before the 2026-11-18 request. Please review and advise how you would like to address this; a newer determinate result would be needed.
  - Would satisfy the policy: Policy 3.6 accepts a negative IGRA or TST dated on or after 2025-11-18. An indeterminate IGRA does not count, and a test ordered but not resulted does not count. A positive screen needs chest imaging excluding active TB and documented start of latent TB treatment.

## Run cost

3 model calls, 21,000 input and 6,555 output tokens, 40.2 s of model time, $0.129 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
