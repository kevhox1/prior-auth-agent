# PA-3580: ustekinumab-aekn for PT-3580

**Outcome: NEEDS_PHYSICIAN**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **expedited**
- Decision clock: URGENT review. Decision within 24 hours of receiving all required information (policy section E). Prescriber attestation of urgency is required. Work this case first.
- Ordered dose: 520 mg IV once (weight 104.9 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI prescriber's 2026-10-26 note states a UC diagnosis (pancolitis) and calls it moderately to severely active. The problem list also documents UC (K51.00). (confidence 0.95)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Moderately to severely active ulcerative pancolitis."

### C2 (policy B.2): **NOT MET**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy on file is a flexible sigmoidoscopy from 2023-07-18. That is more than 12 months before the 2026-11-18 request. Recent calprotectin, CRP and the partial Mayo score are lab or clinical markers, and the policy says these do not count. (confidence 0.70)

- `PT-3580/flexible-sigmoidoscopy-2023-07-18` (2023-07-18): "- Rectum to 31 cm: continuous inflammation with friability and erosions; Mayo endoscopic subscore 3."
- `PT-3580/labs-2026-09-10` (2026-09-10): "CALPROTECTIN FECAL ................ 64 ug/g  (<50)"

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The ordering provider is Dr. S. Adeyemi, Gastroenterology. Ustekinumab was ordered in a GI follow-up note. (confidence 0.90)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The member was born 2000-10-17, so they are 26 on the 2026-11-18 request date. (confidence 0.98)

- `PT-3580/demographics-2025-11-27` (2025-11-27): "Date of birth: 2000-10-17"
- Code checks: age 26 on 2026-11-18 from DOB 2000-10-17

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): **INSUFFICIENT****: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The notes describe inadequate response to an unnamed 'current therapy' but do not name a conventional agent or give its dates. The medication history says there are no steroids at present, and no conventional agent trial appears in the passages. (confidence 0.75)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Symptoms not controlled on current therapy; missing work."
- `PT-3580/medication-history-2026-10-24` (2026-10-24): "- No steroids at present"
- Missing: Documentation naming the conventional agent tried (corticosteroid, budesonide, thiopurine, methotrexate, or oral 5-ASA), with approximate dates of use and the reason it was stopped or found insufficient

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

Adalimumab was used from 2023-07 to 2026-05. It was stopped for intolerance (drug-induced lupus), which satisfies part (b). (confidence 0.92)

- `PT-3580/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

A negative QuantiFERON (an IGRA) resulted on 2026-09-10, within 6 months of the 2026-11-18 request. The older 2023 screen is not needed. (confidence 0.93)

- `PT-3580/labs-2026-09-10` (2026-09-10): "QUANTIFERON TB GOLD PLUS .......... NEGATIVE  (Negative)"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg and total anti-HBc resulted nonreactive on 2026-09-10. Because neither is reactive, no prophylaxis or monitoring plan is required. (confidence 0.95)

- `PT-3580/labs-2026-09-10` (2026-09-10): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-3580/labs-2026-09-10` (2026-09-10): "HEP B CORE AB TOTAL ............... Nonreactive  (Nonreactive)"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The medication history shows no current biologic or small-molecule advanced therapy. The prior adalimumab was stopped in 2026-05. (confidence 0.90)

- `PT-3580/medication-history-2026-10-24` (2026-10-24): "- No biologic or small-molecule advanced therapy at present."
- `PT-3580/medication-history-2026-10-24` (2026-10-24): "| Adalimumab | 40 mg every 2 weeks | 2023-07 | 2026-05 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 104.9 kg was recorded 2026-10-26, within 90 days of the request. That is above 85 kg, so the 520 mg IV dose is correct, and the 90 mg SC every 8 weeks maintenance matches the label. (confidence 0.93)

- `PT-3580/gi-note-2026-10-26` (2026-10-26): "Weight 104.9 kg."
- `PT-3580/gi-note-2026-10-26` (2026-10-26): "1. Start ustekinumab-aekn: 520 mg IV once (weight 104.9 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 104.9 kg (2026-10-26) -> label tier 520 mg; requested 520 mg

## To-do list (gap plan)

- **C2**: Endoscopy report from the past 12 months showing active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, for PA-3580 (ustekinumab-aekn, UC), Calder policy B.2 requires an endoscopy from the past 12 months that shows active inflammation. The only endoscopy on file is the flexible sigmoidoscopy from 2023-07-18 (Mayo subscore 3). The 2026-09-10 calprotectin (64 ug/g), CRP and partial Mayo score don't count under this policy. Please check whether a more recent endoscopy exists, or tell us how you'd like to proceed.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers and cross-sectional imaging are not accepted.
- **C5a**: Name, dates and outcome of the conventional agent tried (who: ordering_provider)
  > Dr. Adeyemi, for PA-3580, Calder policy B.5(a) requires a named conventional agent that was stopped or didn't work well enough. Your 2026-10-26 GI note says "Symptoms not controlled on current therapy" but doesn't name the agent. The request's expedited reason says the patient is "on steroids," but the 2026-10-24 medication history says "No steroids at present." Please document which agent(s) were used, roughly when, and why each was stopped or found insufficient.
  - Would satisfy the policy: Policy B.5(a) accepts documentation naming an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, methotrexate, or (for UC) an oral 5-aminosalicylate. It must give approximate dates of use and say whether the agent was stopped or found insufficient for inadequate response, intolerance, or contraindication.

## Run cost

3 model calls, 39,737 input and 11,968 output tokens, 105.5 s of model time, $0.427 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | NOT_MET | NOT_MET | NOT_MET | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
