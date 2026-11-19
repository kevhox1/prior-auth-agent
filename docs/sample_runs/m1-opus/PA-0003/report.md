# PA-0003: ustekinumab-aekn for PT-0003

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 520 mg IV once (weight 92.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.00). The treating GI's 2026-10-28 note calls it moderately to severely active and records a Harvey-Bradshaw Index of 10. The January 2026 note describing mild symptoms is older and reflects an earlier disease state, so it does not conflict with the current description. (confidence 0.95)

- `PT-0003/problem-list-2026-10-28` (2026-10-28): "Crohn's disease of small intestine without complications (K50.00). Diagnosed 2022. Ileal, inflammatory phenotype."
- `PT-0003/gi-note-2026-10-28` (2026-10-28): "Moderately to severely active ileal Crohn's disease."
- `PT-0003/gi-note-2026-10-28` (2026-10-28): "Harvey-Bradshaw Index today: 10."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-10-20, within 12 months of the request, shows ulcers in the terminal ileum. A fecal calprotectin of 410 ug/g (reference <50) from 2026-10-14 also qualifies by itself. (confidence 0.96)

- `PT-0003/colonoscopy-2026-10-20` (2026-10-20): "- Terminal ileum: multiple ulcers 0.5 to 2 cm over the distal 20 cm, with nodularity and erythema. Ileocecal valve ulcerated but passable."
- `PT-0003/labs-2026-10-14` (2026-10-14): "Fecal calprotectin                    410 ug/g      <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The order is written in a GI follow-up note. The request names the ordering provider as Dr. A. Rivera, Gastroenterology. The quoted passage itself does not state the specialty, so the reviewer should confirm it from the note header. (confidence 0.85)

- `PT-0003/gi-note-2026-10-28` (2026-10-28): "- Start ustekinumab-aekn (preferred biosimilar): 520 mg IV once (weight 92.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

A date of birth of 07/30/1979 makes the member 47 on the 2026-11-18 request date, which is 18 or older. (confidence 0.98)

- `PT-0003/demographics-2025-10-14` (2025-10-14): "Date of birth: 07/30/1979"
- Code checks: age 47 on 2026-11-18 from DOB 1979-07-30

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Prednisone (11/2022 to 02/2023, steroid dependent) and methotrexate (04/2023 to 11/2023, stopped for transaminitis) each have dates and a reason for stopping. Both are backed by the prior GI's outside records, which agree with the intake history. The outside records conflict only on the adalimumab history (see C5b), not on these conventional therapies. (confidence 0.88)

- `PT-0003/outside-records-2025-09-12` (2025-09-12): "- Prednisone 11/2022-02/2023, steroid-dependent."
- `PT-0003/medication-history-2025-10-14` (2025-10-14): "| Prednisone | 40 mg taper | 2022-11 | 2023-02 | Steroid dependent: symptoms returned below 20 mg |"
- `PT-0003/outside-records-2025-09-12` (2025-09-12): "- Methotrexate SC 25mg/wk 04/2023-11/2023, d/c'd for
   transaminitis (ALT 168; ref <40)."

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The intake history, which is based on patient report, and the current GI note say adalimumab was used from 01/2024 to 06/2025 and stopped for loss of response. The prior GI's records say the patient is biologic-naive and declined adalimumab. Nothing in the chart resolves this. Under the policy, records that conflict with the reported history require clinical review. (confidence 0.92)

- `PT-0003/medication-history-2025-10-14` (2025-10-14): "| Adalimumab | 40 mg every 2 weeks (per patient) | 2024-01 | 2025-06 | Per patient: worked at first, then symptoms came back; stopped by prior GI |"
- `PT-0003/gi-note-2026-10-28` (2026-10-28): "Moderately to severely active ileal Crohn's disease. Steroid dependent, methotrexate intolerance, prior adalimumab with loss of response."
- `PT-0003/outside-records-2025-09-12` (2025-09-12): "- Biologic-naive. Adalimumab recommended 01/2024; pt
   declined at that time (cost concerns, needle aversion).
   Re-discussed 06/2025, pt still undecided."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

The QuantiFERON-TB Gold Plus IGRA dated 2026-10-14 is negative. That is within 12 months of the request. (confidence 0.96)

- `PT-0003/labs-2026-10-14` (2026-10-14): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

HBsAg and total anti-HBc were both resulted as nonreactive on 2026-10-14. Because neither is positive, no monitoring or prophylaxis plan is required. (confidence 0.96)

- `PT-0003/labs-2026-10-14` (2026-10-14): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-0003/labs-2026-10-14` (2026-10-14): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication list (2026-10-28) shows only budesonide and lisinopril. It explicitly states the patient is not on any biologic, JAK inhibitor or S1P receptor modulator. (confidence 0.93)

- `PT-0003/gi-note-2026-10-28` (2026-10-28): "Budesonide 9 mg daily, lisinopril 10 mg daily. Not on any biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 92.4 kg was recorded on 2026-10-28, 21 days before the request. That is above 85 kg, so the 520 mg IV band applies, and 520 mg is what was requested. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, which matches the label. (confidence 0.95)

- `PT-0003/gi-note-2026-10-28` (2026-10-28): "Weight 92.4 kg. Height 175 cm. BMI 30.2. BP 132/84. HR 76."
- `PT-0003/gi-note-2026-10-28` (2026-10-28): "- Start ustekinumab-aekn (preferred biosimilar): 520 mg IV once (weight 92.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 92.4 kg (2026-10-28) -> label tier 520 mg; requested 520 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

Both the request and the chart order name ustekinumab-aekn specifically, and it is a preferred product, so no exception is needed. (confidence 0.97)

- `PT-0003/gi-note-2026-10-28` (2026-10-28): "- Start ustekinumab-aekn (preferred biosimilar): 520 mg IV once (weight 92.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Ordering provider review and documentation resolving conflicting adalimumab history (drug, start/stop dates, reason stopped) (who: ordering_provider)
  > Dr. Rivera, for PT-0003's ustekinumab PA (Northfield policy 3.5(b), prior TNF blocker), the records disagree. The medication history (2025-10-14, per patient) and your GI note (2026-10-28) list adalimumab 01/2024–06/2025, stopped for loss of response. The prior GI's outside records (2025-09-12) say the patient is "biologic-naive" and declined adalimumab in 01/2024 and was still undecided in 06/2025. Please review and document which history is accurate, including drug, approximate start/stop dates and reason for stopping, with any claims, prescription records or attestation that support it.

## Run cost

3 model calls, 15,130 input and 3,983 output tokens, 35.4 s of model time, $0.182 at list price (1 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: conflicting.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
