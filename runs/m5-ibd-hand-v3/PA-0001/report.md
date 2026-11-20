# PA-0001: ustekinumab-aekn for PT-0001

**Outcome: READY_FOR_REVIEW**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 78 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating gastroenterologist documents moderately to severely active ileocolonic Crohn's disease, which matches the requested ICD-10 code K50.80. Severity is described by a Harvey-Bradshaw Index of 11 and by symptom burden. (confidence 0.96)

- `PT-0001/gi-note-2026-10-28` (2026-10-28): "Moderately to severely active ileocolonic Crohn's disease."
- `PT-0001/gi-note-2026-10-28` (2026-10-28): "Harvey-Bradshaw Index today: 11."
- `PT-0001/problem-list-2026-11-03` (2026-11-03): "1. Crohn's disease of both small and large intestine without complications (K50.80)."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The colonoscopy dated 2026-09-15, about 2 months before the request, describes large ileal ulcers. Separately, fecal calprotectin on 2026-09-22 was 820 ug/g against a reference range of <50. Either one alone satisfies the criterion. (confidence 0.96)

- `PT-0001/colonoscopy-2026-09-15` (2026-09-15): "- Terminal ileum: multiple large ulcers (>2 cm) over 15 cm, with surrounding erythema and edema."
- `PT-0001/labs-2026-09-22` (2026-09-22): "Fecal calprotectin                    820 ug/g      <50"

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The prescribing note is signed by Dr. A. Rivera, Gastroenterology, who is also the ordering provider on the request. (confidence 0.97)

- `PT-0001/gi-note-2026-10-28` (2026-10-28): "Electronically signed by Dr. A. Rivera, Gastroenterology, 10/28/2026"

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 04/12/1991, the member is 35 on the request date. The outside records list the same date of birth. (confidence 0.98)

- `PT-0001/demographics-2026-11-03` (2026-11-03): "Date of birth: 04/12/1991"
- Code checks: age 35 on 2026-11-18 from DOB 1991-04-12

### C5 (policy 3.5): MET
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The reconciled medication history gives dates and reasons for stopping prednisone (2022-07 to 2022-10, steroid dependent) and azathioprine (2023-01 to 2024-02, inadequate response). The 2024-02-06 GI note recorded at the time and the 2022 outside plan support this history. Nothing in the chart contradicts it. (confidence 0.93)

- `PT-0001/medication-history-2026-11-03` (2026-11-03): "| Prednisone | 40 mg daily, tapered | 2022-07 | 2022-10 | Steroid dependent: symptoms returned at 15 mg during taper |"
- `PT-0001/medication-history-2026-11-03` (2026-11-03): "| Azathioprine | 150 mg daily (2.0 mg/kg) | 2023-01 | 2024-02 | Inadequate response after 12 months; active disease on colonoscopy 12/2023 |"
- `PT-0001/gi-note-2024-02-06` (2024-02-06): "Crohn's disease, ileocolonic, moderately active, with inadequate response to azathioprine at a therapeutic level. Previously steroid dependent."
- `PT-0001/medication-history-2026-11-03` (2026-11-03): "IBD MEDICATION HISTORY - reconciled against outside records and pharmacy fill history 11/03/2026"

**C5b (policy 3.5(b)): MET**: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

Adalimumab ran from 2024-02 to 2026-08-20 and was stopped for secondary loss of response despite weekly dosing. A low trough level and positive anti-drug antibodies support this. The start and stop are each documented in the GI notes. (confidence 0.95)

- `PT-0001/medication-history-2026-11-03` (2026-11-03): "| Adalimumab | 160 mg / 80 mg induction, then 40 mg every 2 weeks; escalated to 40 mg weekly 2025-11 | 2024-02 | 2026-08-20 | Secondary loss of response despite weekly dosing; trough 1.8 mcg/mL with anti-adalimumab antibodies |"
- `PT-0001/gi-note-2026-08-20` (2026-08-20): "Adalimumab trough (07/30/2026): 1.8 mcg/mL. Anti-adalimumab antibodies: 38 U/mL (reference <10; positive)."
- `PT-0001/gi-note-2026-08-20` (2026-08-20): "- Discontinue adalimumab today."

### C6 (policy 3.6): MET
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

QuantiFERON-TB Gold Plus was negative on 2026-09-22, which is within 12 months of the request. The mitogen control was valid, so the result is not indeterminate. (confidence 0.96)

- `PT-0001/labs-2026-09-22` (2026-09-22): "QuantiFERON-TB Gold Plus              NEGATIVE      Negative"
- `PT-0001/labs-2026-09-22` (2026-09-22): "Mitogen minus Nil                   >10.00 IU/mL"

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Results for both HBsAg and total anti-HBc are on file from 2026-09-22, and both are nonreactive. Because neither is positive, no monitoring or prophylaxis plan is required. (confidence 0.97)

- `PT-0001/labs-2026-09-22` (2026-09-22): "Hepatitis B surface antigen           Nonreactive   Nonreactive"
- `PT-0001/labs-2026-09-22` (2026-09-22): "Hepatitis B core antibody, total      Nonreactive   Nonreactive"

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The reconciled medication list shows no current biologic, JAK inhibitor or S1P receptor modulator. The prior agent, adalimumab, was stopped on 2026-08-20, and the 2026-10-28 note confirms the member is off it. Budesonide is not an excluded agent. (confidence 0.95)

- `PT-0001/medication-history-2026-11-03` (2026-11-03): "No current biologic, JAK inhibitor, or S1P receptor modulator. Adalimumab discontinued 2026-08-20."
- `PT-0001/gi-note-2026-10-28` (2026-10-28): "Off adalimumab since 08/20."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

Weight was 78.0 kg on 2026-10-28, 21 days before the request and so within 30 days. That weight falls in the >55 to 85 kg band, which matches the 390 mg IV induction dose. Maintenance is 90 mg SC every 8 weeks starting 8 weeks after the IV dose, as the label requires. (confidence 0.96)

- `PT-0001/gi-note-2026-10-28` (2026-10-28): "Weight 78.0 kg. BP 118/74. HR 82."
- `PT-0001/gi-note-2026-10-28` (2026-10-28): "- Start ustekinumab-aekn (preferred biosimilar): 390 mg IV once (weight 78 kg, >55 to 85 kg tier), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 78.0 kg (2026-10-28) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request and the prescribing note both name ustekinumab-aekn, which is a preferred product. Because the product is preferred, no exception documentation is needed. (confidence 0.97)

- `PT-0001/gi-note-2026-10-28` (2026-10-28): "- Start ustekinumab-aekn (preferred biosimilar): 390 mg IV once"

## Draft PA form (step 8)

| Field | Value | Source |
|---|---|---|
| Member name | Okafor, Daniel E. | `PT-0001/demographics-2026-11-03` |
| Member date of birth | 04/12/1991 | `PT-0001/demographics-2026-11-03` |
| Member ID | NHP-448-201-77 | `PT-0001/demographics-2026-11-03` |
| Requested product | ustekinumab-aekn | `request` |
| Requested regimen | 390 mg IV once (weight 78 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose | `request` |
| Diagnosis code (ICD-10) | K50.80 | `request`; `PT-0001/problem-list-2026-11-03` |
| Ordering provider | Dr. A. Rivera, Gastroenterology | `request` |
| Requested start date | 2026-12-01 | `request` |
| Review type | Standard | `request` |
| C1 (policy 3.1) | Met. Moderately to severely active ileocolonic Crohn's disease (K50.80); Harvey-Bradshaw Index 11 on 2026-10-28. | `PT-0001/gi-note-2026-10-28`; `PT-0001/gi-note-2026-10-28`; `PT-0001/problem-list-2026-11-03` |
| C2 (policy 3.2) | Met. (a) Colonoscopy 2026-09-15: multiple large terminal ileal ulcers (>2 cm) over 15 cm. (b) Fecal calprotectin 820 ug/g (reference <50) on 2026-09-22. Both are within 12 months of the 2026-11-18 request. | `PT-0001/colonoscopy-2026-09-15`; `PT-0001/labs-2026-09-22`; `request` |
| C3 (policy 3.3) | Met. Prescribed by Dr. A. Rivera, Gastroenterology. | `PT-0001/gi-note-2026-10-28`; `request` |
| C4 (policy 3.4) | Met. DOB 04/12/1991; age 35 on the request date 2026-11-18. | `PT-0001/demographics-2026-11-03`; `request` |
| C5a (policy 3.5(a)) | Met. Prednisone 2022-07 to 2022-10: steroid dependent. Azathioprine 150 mg daily (2.0 mg/kg) 2023-01 to 2024-02: inadequate response after 12 months. | `PT-0001/medication-history-2026-11-03`; `PT-0001/medication-history-2026-11-03`; `PT-0001/gi-note-2024-02-06` |
| C5b (policy 3.5(b)) | Met. Adalimumab 2024-02 to 2026-08-20, escalated to 40 mg weekly 2025-11: secondary loss of response; trough 1.8 mcg/mL with positive anti-adalimumab antibodies (38 U/mL) on 07/30/2026; discontinued 2026-08-20. | `PT-0001/medication-history-2026-11-03`; `PT-0001/gi-note-2026-08-20`; `PT-0001/gi-note-2026-08-20` |
| C6 (policy 3.6) | Met. QuantiFERON-TB Gold Plus negative on 2026-09-22, within 12 months of the request. | `PT-0001/labs-2026-09-22`; `request` |
| C7 (policy 3.7) | Met. HBsAg nonreactive and total anti-HBc nonreactive, 2026-09-22. | `PT-0001/labs-2026-09-22`; `PT-0001/labs-2026-09-22` |
| C8 (policy 3.8) | Met. No current biologic, JAK inhibitor, or S1P receptor modulator; adalimumab discontinued 2026-08-20. | `PT-0001/medication-history-2026-11-03`; `PT-0001/gi-note-2026-10-28` |
| C9 (policy 3.9) | Met. Weight 78.0 kg; 390 mg IV once (>55 to 85 kg tier), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose. | `PT-0001/gi-note-2026-10-28`; `PT-0001/gi-note-2026-10-28`; `request` |
| C10 (policy 3.10) | Met. Product named: ustekinumab-aekn. | `request`; `PT-0001/gi-note-2026-10-28` |

## Draft letter of medical necessity (step 8)

To the Northfield Health Plan Prior Authorization Review Team:  
Re: Daniel E. Okafor, date of birth 04/12/1991, Member ID NHP-448-201-77. [`PT-0001/demographics-2026-11-03`] [`PT-0001/demographics-2026-11-03`] [`PT-0001/demographics-2026-11-03`]  
I am requesting authorization of ustekinumab-aekn for this member. [`request`]  
The requested regimen is 390 mg IV once (weight 78 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose. [`request`]  
The requested start date is 2026-12-01. [`request`]  
The record shows the following for each policy criterion.  
Policy 3.1: The member has moderately to severely active ileocolonic Crohn's disease. [`PT-0001/gi-note-2026-10-28`]  
His Harvey-Bradshaw Index was 11 on 2026-10-28. [`PT-0001/gi-note-2026-10-28`]  
The problem list records Crohn's disease of both small and large intestine (K50.80). [`PT-0001/problem-list-2026-11-03`]  
Policy 3.2: Colonoscopy on 2026-09-15 showed multiple large ulcers (>2 cm) over 15 cm of the terminal ileum, with surrounding erythema and edema. [`PT-0001/colonoscopy-2026-09-15`]  
Fecal calprotectin on 2026-09-22 was 820 ug/g, against a reference range of <50. [`PT-0001/labs-2026-09-22`]  
Both results fall within the 12 months before the request date of 2026-11-18. [`request`] [`PT-0001/colonoscopy-2026-09-15`] [`PT-0001/labs-2026-09-22`]  
Policy 3.3: The medication is prescribed by me, Dr. A. Rivera, Gastroenterology. [`request`] [`PT-0001/gi-note-2026-10-28`]  
Policy 3.4: The member's date of birth is 04/12/1991, so he was 35 years old on the request date of 2026-11-18. [`PT-0001/demographics-2026-11-03`] [`request`]  
Policy 3.5(a): He took prednisone 40 mg daily, tapered, from 2022-07 to 2022-10, and was steroid dependent, with symptoms returning at 15 mg during the taper. [`PT-0001/medication-history-2026-11-03`]  
He took azathioprine 150 mg daily (2.0 mg/kg) from 2023-01 to 2024-02 and had an inadequate response after 12 months, with active disease on colonoscopy in 12/2023. [`PT-0001/medication-history-2026-11-03`] [`PT-0001/gi-note-2024-02-06`]  
Policy 3.5(b): He took adalimumab from 2024-02 to 2026-08-20, with dosing escalated to 40 mg weekly in 2025-11, and had a secondary loss of response despite weekly dosing. [`PT-0001/medication-history-2026-11-03`]  
On 07/30/2026 his adalimumab trough was 1.8 mcg/mL and anti-adalimumab antibodies were positive at 38 U/mL (reference <10). [`PT-0001/gi-note-2026-08-20`]  
Adalimumab was discontinued on 2026-08-20. [`PT-0001/gi-note-2026-08-20`] [`PT-0001/medication-history-2026-11-03`]  
Policy 3.6: QuantiFERON-TB Gold Plus on 2026-09-22 was negative, within the 12 months before the request. [`PT-0001/labs-2026-09-22`] [`request`]  
Policy 3.7: On 2026-09-22, hepatitis B surface antigen was nonreactive. [`PT-0001/labs-2026-09-22`]  
On the same date, total hepatitis B core antibody was nonreactive. [`PT-0001/labs-2026-09-22`]  
Policy 3.8: The member is on no current biologic, JAK inhibitor, or S1P receptor modulator. [`PT-0001/medication-history-2026-11-03`] [`PT-0001/gi-note-2026-10-28`]  
Policy 3.9: The member weighed 78.0 kg on 2026-10-28. [`PT-0001/gi-note-2026-10-28`]  
The plan is a single 390 mg IV dose for the >55 to 85 kg weight tier, then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose. [`PT-0001/gi-note-2026-10-28`]  
Policy 3.10: The request names the specific product, ustekinumab-aekn. [`request`] [`PT-0001/gi-note-2026-10-28`]  
Thank you for reviewing this request.  
Sincerely,  
[Signature pending review by Dr. A. Rivera, Gastroenterology]  

## Independent verification (step 9)

All claims supported. (44 claims checked.)

## Run cost

4 model calls, 44,406 input and 17,943 output tokens, 131.6 s of model time, $0.696 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent READY_FOR_REVIEW. Case type: clean.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | MET | MET | MET | ok |
| C6 | 3.6 | MET | MET | MET | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
