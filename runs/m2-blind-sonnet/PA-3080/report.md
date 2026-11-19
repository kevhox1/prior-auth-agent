# PA-3080: ustekinumab-aekn for PT-3080

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: EXPEDITED review. Pharmacy-benefit phase: decision within 24 hours of a complete request (policy section 7). Prescriber statement of clinical urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 104.9 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. Disease severity must be described by the treating provider (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The GI note gives a diagnosis of ulcerative pancolitis and describes it as moderately to severely active. A partial Mayo score of 7 supports the severity. (confidence 0.96)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Impression:
Moderately to severely active ulcerative pancolitis."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Partial Mayo score today: 7."

### C2 (policy 3.2): MET
_The record includes at least one of the following, dated within the 12 months before the request: (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability); or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

Fecal calprotectin of 64 ug/g is above the lab reference of <50 and was dated 2026-09-10, within 12 months of the request. The 2023 sigmoidoscopy is outside the window and is not relied on. (confidence 0.93)

- `PT-3080/labs-2026-09-10` (2026-09-10): "CALPROTECTIN FECAL ................ 64 ug/g  (<50)"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan is in the GI follow-up note by Dr. Adeyemi, Gastroenterology, who is also the ordering provider on the request. The quoted plan is from the gastroenterology visit. (confidence 0.85)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older._

Date of birth 2000-10-17 makes the member 26 at the request date, which is 18 or older. (confidence 0.97)

- `PT-3080/demographics-2025-11-27` (2025-11-27): "Date of birth: 2000-10-17"
- Code checks: age 26 on 2026-11-18 from DOB 2000-10-17

### C5 (policy 3.5): **INSUFFICIENT**
_Both prior therapy requirements are documented. The record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes. A treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): **INSUFFICIENT****: Conventional therapy: an inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids, azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis, oral aminosalicylates (such as mesalamine) also count. An inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Budesonide counts as a corticosteroid for this purpose.

The medication history lists only adalimumab as prior therapy and states no steroids at present. No conventional therapy, dates, or outcome is documented in the passages, so the requirement is not settled. (confidence 0.80)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "- No steroids at present"
- Missing: Documentation of prior use of a conventional therapy (systemic corticosteroid including budesonide, azathioprine, 6-mercaptopurine, methotrexate, or oral aminosalicylate such as mesalamine) with drug name, approximate start and stop dates, and reason stopped (inadequate response, intolerance, or contraindication)

**C5b (policy 3.5(b)): MET**: Anti-TNF therapy: an inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure).

The medication history names adalimumab with start 2023-07, stop 2026-05, and the reason stopped as intolerance (drug-induced lupus). Intolerance qualifies under the policy. (confidence 0.92)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy 3.6): MET
_The member has a negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate interferon-gamma release assay is not a negative result. If the screening test is positive, the record must show that active tuberculosis has been excluded by chest imaging and that treatment for latent tuberculosis has been started. A test ordered but not resulted does not satisfy this criterion._

A negative QuantiFERON was resulted 2026-09-10, within 12 months of the request. The 2023 screening mentioned in the note is not relied on. (confidence 0.95)

- `PT-3080/labs-2026-09-10` (2026-09-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. There is no lookback limit. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc are resulted and nonreactive. Neither is positive, so no monitoring plan is needed. (confidence 0.96)

- `PT-3080/labs-2026-09-10` (2026-09-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3080/labs-2026-09-10` (2026-09-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history shows no biologic, JAK inhibitor, or S1P modulator at present. The prior adalimumab was stopped in 2026-05. (confidence 0.93)

- `PT-3080/medication-history-2026-10-24` (2026-10-24): "- No biologic or small-molecule advanced therapy at present."
- `PT-3080/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy 3.9): MET
_The requested dose follows the FDA-approved adult labeling. Induction: a single intravenous dose based on body weight: 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the intravenous dose. A current body weight (within 30 days of the request) must be documented for the induction dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 104.9 kg was recorded 23 days before the request, which is within 30 days. It is over 85 kg, so 520 mg IV is correct, and maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose. (confidence 0.95)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Weight 104.9 kg."
- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 104.9 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request names the specific ustekinumab product (a request for 'ustekinumab' without a product is incomplete). Preferred products are ustekinumab-aekn and ustekinumab-ttwe, in IV and SC forms. All other ustekinumab products, including the reference (originator) product, are non-preferred. A non-preferred product is covered only when the record documents one of: (a) an inadequate response to, or intolerance of, both preferred products; or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product. Intolerance of one preferred product does not satisfy (a)._

The request names ustekinumab-aekn, which is a preferred product. No exception is needed. (confidence 0.96)

- `PT-3080/gi-note-2026-10-26` (2026-10-26): "Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5a**: Prior conventional therapy record (drug, dates, outcome) (who: practice_staff)
  > PA-3080 (PT-3080), criterion C5a, conventional therapy: the 2026-10-24 medication history lists only adalimumab and notes 'No steroids at present'. Please locate or document any prior systemic corticosteroid (including budesonide), azathioprine, 6-mercaptopurine, methotrexate, or oral aminosalicylate such as mesalamine. Include drug name, approximate start and stop dates, and reason stopped (inadequate response, intolerance, or contraindication). The expedited reason mentions a flare on steroids, so please clarify any steroid course and reconcile it with the medication history. If no conventional therapy was used, please review and advise.
  - Would satisfy the policy: Policy 3.5(a) accepts documentation of at least one conventional therapy (systemic corticosteroid including budesonide, azathioprine, 6-mercaptopurine, methotrexate, or for UC an oral aminosalicylate such as mesalamine) with an inadequate response (including steroid dependence or refractory disease), intolerance, or contraindication. Documentation should include the drug name, dates, and outcome.

## Run cost

3 model calls, 30,342 input and 9,163 output tokens, 54.9 s of model time, $0.184 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
