# PA-2588: ustekinumab-aekn for PT-2588

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 520 mg IV once (weight 104.3 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

In the 2026-10-26 GI note, the prescriber states the patient has moderately to severely active ulcerative pancolitis. This covers both the diagnosis and the severity. (confidence 0.95)

- `PT-2588/gi-note-2026-10-26` (2026-10-26): "- Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

A flexible sigmoidoscopy on 2026-09-28, within 12 months of the request, found continuous inflammation with friability and erosions (Mayo endoscopic subscore 3). Pathology confirmed chronic active inflammation. (confidence 0.95)

- `PT-2588/flexible-sigmoidoscopy-2026-09-28` (2026-09-28): "- Rectum to 27 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-2588/flexible-sigmoidoscopy-2026-09-28` (2026-09-28): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. The ustekinumab order appears in a GI follow-up note. The quoted passage does not itself state the specialty, so the reviewer may want to confirm the note's author header. (confidence 0.88)

- `PT-2588/gi-note-2026-10-26` (2026-10-26): "- Start ustekinumab-aekn: 520 mg IV once (weight 104.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The date of birth is 05/02/1964, which makes the member 62 on the request date of 2026-11-18. The outside records show the same date of birth. (confidence 0.97)

- `PT-2588/demographics-2026-08-03` (2026-08-03): "Date of birth: 05/02/1964"
- Code checks: age 62 on 2026-11-18 from DOB 1964-05-02

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The outside records show budesonide from 08/2023 to 11/2023, stopped for inadequate response. The 2026 medication history says 'no prior IBD therapy documented', but that is missing documentation, not a statement that budesonide was never taken, so it is not a conflict. (confidence 0.80)

- `PT-2588/outside-records-2024-06-18` (2024-06-18): "- Budesonide 9 mg daily, 08/2023 to 11/2023. Reason stopped: inadequate response after 10 weeks."

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The outside records show infliximab from 01/2024 to 05/2024, stopped for primary non-response. The 'no prior IBD therapy documented' line in the medication history is missing documentation, not a contradiction. (confidence 0.80)

- `PT-2588/outside-records-2024-06-18` (2024-06-18): "- Infliximab 5 mg/kg IV every 8 weeks, 01/2024 to 05/2024. Reason stopped: primary non-response: no clinical improvement after induction and 8 weeks of maintenance."

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

The IGRA on 2026-09-12, within 6 months, was positive. The policy's exception for a positive screen applies: the 2026-09-15 chest radiograph shows no active TB, and rifampin for latent TB started 09/22/2026. (confidence 0.90)

- `PT-2588/labs-2026-09-12` (2026-09-12): "QUANTIFERON TB GOLD PLUS .......... POSITIVE  (Negative)"
- `PT-2588/chest-xray-2026-09-15` (2026-09-15): "IMPRESSION: No evidence of active pulmonary tuberculosis."
- `PT-2588/gi-note-2026-10-26` (2026-10-26): "- Latent TB infection: rifampin daily for 4 months, started 09/22/2026."

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both required results are on file: HBsAg is nonreactive and total anti-HBc is reactive. Because anti-HBc is reactive, a plan is required, and the 2026-10-26 note documents monitoring of HBV DNA and liver tests every 3 months. (confidence 0.93)

- `PT-2588/labs-2026-09-12` (2026-09-12): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2588/labs-2026-09-12` (2026-09-12): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-2588/gi-note-2026-10-26` (2026-10-26): "- Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): **NOT MET**
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The prescriber's plan says to continue upadacitinib, a JAK inhibitor, and add ustekinumab. That is combined use, which the policy excludes. The chart does not show upadacitinib being stopped. (confidence 0.95)

- `PT-2588/gi-note-2026-10-26` (2026-10-26): "- Continue upadacitinib 15 mg daily and add ustekinumab."
- `PT-2588/medication-history-2026-10-26` (2026-10-26): "- Upadacitinib 15 mg daily"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

The weight of 104.3 kg was recorded on 2026-10-26, within 90 days of the request. That is above 85 kg, so the matching induction dose is 520 mg IV. The requested 520 mg IV, then 90 mg SC every 8 weeks starting 8 weeks after the infusion, is the labeled regimen. (confidence 0.94)

- `PT-2588/gi-note-2026-10-26` (2026-10-26): "- Weight 104.3 kg."
- `PT-2588/gi-note-2026-10-26` (2026-10-26): "- Start ustekinumab-aekn: 520 mg IV once (weight 104.3 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 104.3 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C8**: Prescriber review of the plan to combine ustekinumab with upadacitinib (JAK inhibitor), and updated documentation if the plan changes (who: ordering_provider)
  > Dr. Adeyemi, PA-2588 (PT-2588, ustekinumab-aekn for K51.00) does not meet Calder policy criterion B.8. That criterion does not allow ustekinumab to be combined with a JAK inhibitor, and if the patient is switching, the chart must show the earlier agent is being stopped. Your GI note dated 2026-10-26 says "Continue upadacitinib 15 mg daily and add ustekinumab," and the medication history from the same date lists upadacitinib 15 mg daily as current. Please review this criterion and tell us how you want to proceed. If the treatment plan is different from what the 2026-10-26 note says, please document the plan as it actually stands.

## Run cost

3 model calls, 19,709 input and 6,869 output tokens, 55.6 s of model time, $0.256 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: not_met.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | NOT_MET | NOT_MET | NOT_MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
