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
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease. The treating GI note calls it moderately to severely active and records a Harvey-Bradshaw Index of 13. (confidence 0.95)

- `PT-3096/problem-list-2026-11-03` (2026-11-03): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2019."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Harvey-Bradshaw Index today: 13."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-08-16 is within 12 months of the 2026-11-18 request. It describes ulcers in the terminal ileum, and pathology shows active inflammation. (confidence 0.95)

- `PT-3096/colonoscopy-2026-08-16` (2026-08-16): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-3096/colonoscopy-2026-08-16` (2026-08-16): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The request lists Dr. S. Adeyemi, Gastroenterology, as the ordering provider. The ustekinumab plan is written in the GI follow-up note. (confidence 0.90)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 2006-05-08, the member is 20 years old on the 2026-11-18 request date. (confidence 0.97)

- `PT-3096/demographics-2026-05-27` (2026-05-27): "Date of birth: 2006-05-08"
- Code checks: age 20 on 2026-11-18 from DOB 2006-05-08

### C5 (policy 3.5): **INSUFFICIENT**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The patient is currently on prednisone, but no start date is given and no note says it failed, caused intolerance, or led to steroid dependence. The February note mentions symptoms despite therapy but does not name the drug. (confidence 0.75)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- Prednisone 20 mg daily, taper planned after induction"
- `PT-3096/gi-note-2026-02-18` (2026-02-18): "Follow-up of Crohn's disease. Ongoing symptoms despite current therapy."
- Missing: Start date of prednisone or other conventional therapy
- Missing: Documented reason the conventional therapy failed (inadequate response, steroid dependence or steroid-refractory disease, intolerance, or contraindication)
- Missing: Name of the 'current therapy' referred to in the 2026-02-18 note
- Missing: Supporting claims, prescription records, or prescriber attestation

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The treating GI specifically records a contraindication to TNF blockers because of multiple sclerosis, a demyelinating disease. The problem list confirms the MS diagnosis, and the policy names demyelinating disease as an example of a contraindication that qualifies. (confidence 0.85)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3096/problem-list-2026-11-03` (2026-11-03): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy 3.6): **NOT MET**
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The only TB screening test on file is dated 2025-10-20, which is more than 12 months before the 2026-11-18 request. No more recent IGRA or tuberculin skin test is documented. (confidence 0.85)

- `PT-3096/labs-2025-10-20` (2025-10-20): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"
- Code checks: no cited evidence dated on or after 2025-11-18 (12-month lookback)

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg (nonreactive) and total anti-HBc (reactive) have results on file. Because anti-HBc is positive, a monitoring plan is required, and the GI note documents one. (confidence 0.93)

- `PT-3096/labs-2026-10-13` (2026-10-13): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3096/labs-2026-10-13` (2026-10-13): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current GI note states the patient is on no biologic or small-molecule advanced therapy. The listed medications are prednisone and omeprazole. (confidence 0.90)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The 101.7 kg weight is dated 2026-11-03, within 30 days of the request, and falls in the over-85 kg band for 520 mg IV. Maintenance of 90 mg SC every 8 weeks starting 8 weeks after the IV dose matches the label. (confidence 0.93)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "Weight 101.7 kg."
- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 101.7 kg (2026-11-03) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the GI note name ustekinumab-ttwe, which is a preferred product under the policy. (confidence 0.95)

- `PT-3096/gi-note-2026-11-03` (2026-11-03): "- Start ustekinumab-ttwe: 520 mg IV once (weight 101.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5a**: Documented conventional therapy trial: drug name, approximate start/stop dates, and reason it failed (who: ordering_provider)
  > Dr. Adeyemi, for PA-3096 (PT-3096, ustekinumab-ttwe), criterion 3.5(a) on conventional therapy is not yet documented. The 2026-11-03 GI note lists "Prednisone 20 mg daily, taper planned after induction" but gives no start date and no reason it is not working. The 2026-02-18 note says "Ongoing symptoms despite current therapy" but does not name the drug. Please review and document which conventional therapy or therapies were tried, the approximate start and stop dates, and the reason: inadequate response (including steroid dependence or steroid-refractory disease), intolerance, or contraindication.
  - Would satisfy the policy: Policy 3.5(a) accepts documentation of at least one conventional therapy for Crohn's disease: a systemic corticosteroid (including budesonide), azathioprine, 6-mercaptopurine, or methotrexate. It must include the drug name, approximate start/stop dates, and the reason it was stopped or failed (inadequate response, including steroid dependence or steroid-refractory disease, intolerance, or contraindication), backed by claims, prescription records, chart notes, or prescriber attestation. Oral aminosalicylates do not count for Crohn's disease.
- **C6**: Negative TB screening result (IGRA or TST) from within the 12 months before the request (who: ordering_provider)
  > Dr. Adeyemi, for PA-3096 (PT-3096, ustekinumab-ttwe), criterion 3.6 on TB screening is not met. The only TB test on file is a QuantiFERON TB Gold Plus, negative, dated 2025-10-20 (labs-2025-10-20). That is more than 12 months before the 2026-11-18 request date. Please review and tell us if a more recent TB screening result exists or how you would like to proceed.
  - Would satisfy the policy: Policy 3.6 accepts a negative IGRA or TST dated on or after 2025-11-18. An indeterminate IGRA does not count as negative, and a test that was ordered but has no result does not satisfy the criterion. If the screening test is positive, the record must show that chest imaging excluded active TB and that treatment for latent TB has started.

## Run cost

3 model calls, 22,477 input and 7,918 output tokens, 65.5 s of model time, $0.296 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | NOT_MET | NOT_MET | NOT_MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
