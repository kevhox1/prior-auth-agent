# PA-0002: ustekinumab-ttwe for PT-0002

**Outcome: GAPS_TO_CLOSE**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 58.2 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents ulcerative pancolitis (K51.00). The treating GI note calls the disease moderately to severely active and records a partial Mayo score of 7 with 5-6 bloody stools a day. (confidence 0.96)

- `PT-0002/problem-list-2026-10-30` (2026-10-30): "1. Ulcerative (chronic) pancolitis without complications (K51.00). Diagnosed 2023."
- `PT-0002/gi-note-2026-10-30` (2026-10-30): "Moderately to severely active ulcerative pancolitis."
- `PT-0002/gi-note-2026-10-30` (2026-10-30): "Partial Mayo score today: 7."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The flexible sigmoidoscopy on 2026-10-01, within 12 months of the request, describes friability and ulcerations. Fecal calprotectin on 2026-10-06 was 1150 ug/g against a reference of <50, which also qualifies on its own. (confidence 0.97)

- `PT-0002/flex-sig-2026-10-01` (2026-10-01): "- Rectum to 40 cm (limit of exam): continuous inflammation with marked erythema, absent vascular pattern, friability, spontaneous bleeding, and multiple shallow ulcerations."
- `PT-0002/labs-2026-10-06` (2026-10-06): "Fecal calprotectin                    1150 ug/g     <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab plan was written in a GI follow-up note. The request names the ordering provider as Dr. A. Rivera, Gastroenterology. The quoted passage does not itself state the author's specialty, so the reviewer may want to confirm the signature on the note. (confidence 0.88)

- `PT-0002/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe (preferred biosimilar): 390 mg IV once (weight 58.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 11/02/1984, the member is 42 on the request date of 2026-11-18. The outside records show the same date of birth. (confidence 0.98)

- `PT-0002/demographics-2026-10-30` (2026-10-30): "Date of birth: 11/02/1984"
- Code checks: age 42 on 2026-11-18 from DOB 1984-11-02

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The reconciled medication history lists oral mesalamine, prednisone and azathioprine, each with start and stop dates and a reason for stopping: inadequate response, steroid dependence and pancreatitis. The problem list and allergy list separately confirm the azathioprine pancreatitis. (confidence 0.95)

- `PT-0002/medication-history-2026-10-30` (2026-10-30): "| Mesalamine (oral) | 4.8 g daily | 2023-05 | 2024-03 | Inadequate response at full dose; added rectal mesalamine 2023-10 without benefit |"
- `PT-0002/medication-history-2026-10-30` (2026-10-30): "| Prednisone | 40 mg taper (two courses) | 2023-09 | 2024-06 | Steroid dependent: flared within 6 weeks of each taper |"
- `PT-0002/medication-history-2026-10-30` (2026-10-30): "| Azathioprine | 100 mg daily | 2024-04 | 2024-07 | Intolerance: acute pancreatitis (lipase 1,840) |"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Infliximab ran from 2024-09 to its last infusion on 2026-07-08 and was stopped for secondary loss of response. The 2026-07-22 note supports this with an undetectable trough level and positive antibodies to infliximab. (confidence 0.95)

- `PT-0002/medication-history-2026-10-30` (2026-10-30): "| Infliximab | 5 mg/kg IV weeks 0, 2, 6 then every 8 weeks; escalated to 10 mg/kg every 6 weeks 2026-02 | 2024-09 | 2026-07-08 (last infusion) | Secondary loss of response; infliximab level undetectable with high-titer antibodies to infliximab |"
- `PT-0002/gi-note-2026-07-22` (2026-07-22): "Infliximab trough (07/08/2026, pre-infusion): <1.0 mcg/mL (undetectable). Antibodies to infliximab: 46 U/mL (reference <10; positive)."
- `PT-0002/gi-note-2026-07-22` (2026-07-22): "- Stop infliximab."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A QuantiFERON-TB Gold Plus dated 2026-10-06, within 12 months of the request, is negative. The mitogen control is adequate, so the result is valid and not indeterminate. (confidence 0.96)

- `PT-0002/labs-2026-10-06` (2026-10-06): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"
- `PT-0002/labs-2026-10-06` (2026-10-06): "(Nil 0.06 | TB1-Nil 0.00 | TB2-Nil 0.03 | Mitogen-Nil 8.42 IU/mL)"

### C7 (policy 3.7): **INSUFFICIENT**
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

An HBsAg result from 2024 is on file and non-reactive, but no total anti-HBc result exists. Anti-HBc was ordered on 10/30/2026, and as of 11/14/2026 the lab had not received a specimen. The surface antibody and vaccination history do not count under the policy. (confidence 0.95)

- `PT-0002/outside-records-2024-08-21` (2024-08-21): "HEPATITIS B SURF AG ............. Non-reactive"
- `PT-0002/gi-note-2026-10-30` (2026-10-30): "- Hepatitis B serologies (HBsAg, total anti-HBc) ordered today to complete pre-biologic screening."
- `PT-0002/nurse-call-2026-11-14` (2026-11-14): "No specimen received by the lab."
- Missing: Total hepatitis B core antibody (anti-HBc) result

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The reconciled medication list states there is no current biologic, JAK inhibitor or S1P receptor modulator. The prior biologic, infliximab, was stopped after the 07/08/2026 infusion. The only other current therapy listed is prednisone, which is not an excluded agent. (confidence 0.94)

- `PT-0002/medication-history-2026-10-30` (2026-10-30): "No current biologic, JAK inhibitor, or S1P receptor modulator. Infliximab discontinued after 07/08/2026 infusion."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 58.2 kg was recorded on 2026-10-30, 19 days before the request. That falls in the >55 to 85 kg band, which matches the 390 mg single IV dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as the label requires. (confidence 0.95)

- `PT-0002/gi-note-2026-10-30` (2026-10-30): "Weight 58.2 kg. BP 108/66. HR 84. Temp 36.8 C."
- `PT-0002/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe (preferred biosimilar): 390 mg IV once (weight 58.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 58.2 kg (2026-10-30) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the GI note name ustekinumab-ttwe, which is a preferred product under the policy. No exception documentation is needed. (confidence 0.97)

- `PT-0002/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe (preferred biosimilar): 390 mg IV once (weight 58.2 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C7**: Resulted total hepatitis B core antibody (anti-HBc) (who: lab)
  > For the ustekinumab-ttwe prior authorization (PA-0002, patient PT-0002), criterion C7 needs both HBsAg and total anti-HBc results on file. HBsAg was non-reactive on 08/21/2024, but the total anti-HBc ordered on 10/30/2026 had no specimen received by the lab as of 11/14/2026. Please arrange the blood draw and send us the resulted total anti-HBc. If it comes back positive, the chart will also need a monitoring or antiviral prophylaxis plan.

## Run cost

3 model calls, 15,117 input and 4,053 output tokens, 35.1 s of model time, $0.183 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: missing_item.

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
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
