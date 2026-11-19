# PA-2050: ustekinumab-aekn for PT-2050

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 71.4 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The problem list documents Crohn's disease (K50.80). The treating GI note says the disease is moderately to severely active and gives a Harvey-Bradshaw Index of 9, which describes severity. (confidence 0.93)

- `PT-2050/gi-note-2026-11-08` (2026-11-08): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-2050/gi-note-2026-11-08` (2026-11-08): "- Harvey-Bradshaw Index today: 9."
- `PT-2050/problem-list-2026-11-08` (2026-11-08): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2023."

### C2 (policy 3.2): **INSUFFICIENT**
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The only colonoscopy showing ulcers is dated 2025-03-18, which is before the 12-month cutoff of 2025-11-18. The CRP from 2026-09-07 is high, but the policy says CRP alone does not count. No fecal calprotectin is on file. (confidence 0.88)

- `PT-2050/colonoscopy-2025-03-18` (2025-03-18): "- Terminal ileum: multiple ulcers 0.5-2 cm with surrounding erythema and edema."
- `PT-2050/labs-2026-09-07` (2026-09-07): "C-reactive protein                    12.2 mg/L     <5.0"
- Missing: Endoscopy, colonoscopy, or flexible sigmoidoscopy report showing active inflammation dated on or after 2025-11-18
- Missing: Fecal calprotectin result above the lab's upper reference limit (with reference range) dated on or after 2025-11-18

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The ustekinumab-aekn order appears in a GI follow-up note. The request lists the ordering provider as Dr. M. Chen, Gastroenterology. (confidence 0.85)

- `PT-2050/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 390 mg IV once (weight 71.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 1989-08-06, the member is 37 on the 2026-11-18 request date. The outside records show the same DOB. (confidence 0.97)

- `PT-2050/demographics-2026-02-20` (2026-02-20): "Date of birth: 1989-08-06"
- Code checks: age 37 on 2026-11-18 from DOB 1989-08-06

### C5 (policy 3.5): **CONFLICTING**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history lists budesonide (2023-12 to 2024-03, inadequate response) and prednisone (2024-04 to 2024-12, steroid dependent), each with dates and a reason for stopping. No passage contradicts this steroid history. (confidence 0.85)

- `PT-2050/medication-history-2026-11-06` (2026-11-06): "Budesonide 9 mg daily, 2023-12 to 2024-03. Reason stopped: inadequate response after 10 weeks."
- `PT-2050/medication-history-2026-11-06` (2026-11-06): "Prednisone 40 mg daily, tapered, 2024-04 to 2024-12. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."

**C5b (policy 3.5(b)): **CONFLICTING****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The medication history, based on patient report, says adalimumab ran from 2025-02 to 2026-05 and was stopped for loss of response. Outside records dated 2025-06-18, which falls inside that reported course, say the patient was biologic-naive and declined adalimumab in 2025-02. Per policy, records that are inconsistent with the reported history require clinical review. (confidence 0.85)

- `PT-2050/medication-history-2026-11-06` (2026-11-06): "Adalimumab 40 mg every 2 weeks, 2025-02 to 2026-05. Reason stopped: per patient report, worked at first and then stopped working; outside records requested."
- `PT-2050/outside-records-2025-06-18` (2025-06-18): "- Biologic-naive. Adalimumab was recommended 2025-02 but the patient declined."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

A negative QuantiFERON-TB Gold Plus result is dated 2026-09-07, which is within 12 months of the request. (confidence 0.95)

- `PT-2050/labs-2026-09-07` (2026-09-07): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg and total anti-HBc have results on file and both are nonreactive, so no monitoring plan is needed. (confidence 0.96)

- `PT-2050/labs-2026-09-07` (2026-09-07): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-2050/labs-2026-09-07` (2026-09-07): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current medication history shows no biologic, JAK inhibitor, or S1P modulator. Whether or not the patient ever took adalimumab (see C5b), the chart does not show it being used now. (confidence 0.88)

- `PT-2050/medication-history-2026-11-06` (2026-11-06): "- No biologic or small-molecule advanced therapy at present."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The 71.4 kg weight is from 10 days before the request and falls in the >55 to 85 kg band, which calls for 390 mg IV. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as the label requires. (confidence 0.94)

- `PT-2050/gi-note-2026-11-08` (2026-11-08): "- Weight 71.4 kg."
- `PT-2050/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 390 mg IV once (weight 71.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 71.4 kg (2026-11-08) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the order both name ustekinumab-aekn, which is a preferred product, so no exception is needed. (confidence 0.96)

- `PT-2050/gi-note-2026-11-08` (2026-11-08): "- Start ustekinumab-aekn: 390 mg IV once (weight 71.4 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C2**: Fecal calprotectin result above the lab's upper reference limit, with the reference range, dated on or after 2025-11-18. A colonoscopy, endoscopy or sigmoidoscopy report showing active inflammation from the same window would also work. (who: lab)
  > For PT-2050 (ustekinumab-aekn PA-2050), criterion C2 needs objective evidence of active disease dated on or after 2025-11-18. The only colonoscopy on file showing ulcers is from 2025-03-18, which is too old, and the CRP of 12.2 mg/L from 2026-09-07 does not count on its own under the policy. Is there a fecal calprotectin result, or a colonoscopy, endoscopy or sigmoidoscopy report, from 2025-11-18 onward? If not, please collect and report a fecal calprotectin with the lab's reference range.
- **C5b**: Ordering provider's review of the conflicting adalimumab history, plus documentation of the actual TNF-blocker history (drug, start and stop dates, reason stopped) backed by claims, prescription records, chart notes or attestation (who: ordering_provider)
  > Dr. Chen, for PT-2050 (PA-2050), criterion C5b has conflicting records on prior TNF-blocker use. The medication history dated 2026-11-06 records adalimumab 40 mg every 2 weeks from 2025-02 to 2026-05, stopped for loss of response. That history is based on patient report. The outside records dated 2025-06-18 say the patient was 'Biologic-naive' and declined adalimumab in 2025-02. Please review these records and document the patient's actual adalimumab history, including dates and the reason it was stopped, with supporting records or your attestation.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | NOT_MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok (alternate) |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | CONFLICTING | CONFLICTING | CONFLICTING | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
