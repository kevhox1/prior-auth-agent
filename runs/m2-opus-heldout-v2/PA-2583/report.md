# PA-2583: ustekinumab-ttwe for PT-2583

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 78.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The gastroenterology note of 2026-10-30 records the diagnosis as Crohn's disease and calls it moderately to severely active. The problem list (K50.80) and the Harvey-Bradshaw Index of 10 agree with this. (confidence 0.95)

- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only endoscopy in the chart is a 2019 colonoscopy. That is well outside the 12-month window, and its report is not on file. Calprotectin, CRP and the HBI are lab or clinical markers, and the policy says these do not count on their own. (confidence 0.88)

- `PT-2583/outside-records-2019-11-18` (2019-11-18): "Dx: Crohn's disease, diagnosed 08/2019 by colonoscopy."
- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- His calprotectin from 08/21/2026 came back at 1075 ug/g (lab reference <50)."
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated 2025-11-18 or later documenting active mucosal inflammation

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. Ustekinumab is ordered in the GI follow-up note. (confidence 0.90)

- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 390 mg IV once (weight 78.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

The member was born 04/28/1991, so he is 35 on the 2026-11-18 request date. The outside records give the same date of birth. (confidence 0.98)

- `PT-2583/demographics-2026-09-22` (2026-09-22): "Date of birth: 04/28/1991"
- Code checks: age 35 on 2026-11-18 from DOB 1991-04-28

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Prednisone, a corticosteroid, was used from 09/2019 to 02/2020. It was stopped because of steroid dependence, with flares whenever the dose went below 15 mg, which is an inadequate response. The blank treatment history in the 2019 outside records leaves this out but does not contradict it. (confidence 0.88)

- `PT-2583/gi-note-2026-05-10` (2026-05-10): "- History: Prednisone 40 mg daily, tapered, 09/2019 to 02/2020. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."

**C5b (policy B.5(b)): **NOT MET****: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The prescriber records that the member is biologic-naive, and no TNF-blocker contraindication is documented. Part (b) is therefore not met, though C5 can still be satisfied through C5a. (confidence 0.90)

- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- Biologic-naive; no prior anti-TNF therapy."

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

No IGRA or tuberculin skin test result appears in the retrieved passages. (confidence 0.92)

- Missing: IGRA or TST result dated 2026-05-18 or later

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both required tests have results: HBsAg is nonreactive and total anti-HBc is reactive. Because the core antibody is reactive, a plan is needed, and the prescriber documents monitoring of HBV DNA and liver tests every 3 months. (confidence 0.92)

- `PT-2583/labs-2026-09-25` (2026-09-25): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2583/labs-2026-09-25` (2026-09-25): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The note states there is no current biologic, JAK inhibitor, or S1P receptor modulator. The member is biologic-naive, so he is not switching from another agent. (confidence 0.92)

- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- No current biologic, JAK inhibitor, or S1P receptor modulator."
- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- Biologic-naive; no prior anti-TNF therapy."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 78.7 kg was recorded on 2026-10-30, 19 days before the request. That is in the >55 to 85 kg band, which calls for 390 mg IV. The ordered regimen (390 mg IV once, then 90 mg SC every 8 weeks starting 8 weeks later) matches the labeled regimen. (confidence 0.95)

- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- Weight 78.7 kg."
- `PT-2583/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 390 mg IV once (weight 78.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 78.7 kg (2026-10-30) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy) dated 2025-11-18 or later showing active mucosal inflammation (who: ordering_provider)
  > Dr. Adeyemi, for PA-2583 (ustekinumab-ttwe, PT-2583), Calder policy B.2 requires an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy from 2025-11-18 or later that documents active mucosal inflammation. The only endoscopy we found is the 2019 diagnostic colonoscopy noted in the 2019-11-18 outside records, and that report is not on file. The policy says the calprotectin of 1075 ug/g (08/21/2026), CRP, HBI and imaging do not count on their own. Was an endoscopy done in this window, here or at another facility? If so, please tell us where so we can get the report.
- **C5b**: Provider review of prior biologic/targeted therapy failure or TNF-blocker contraindication (who: ordering_provider)
  > Dr. Adeyemi, for PA-2583 (PT-2583), Calder policy B.5(b) requires either a prior biologic or targeted synthetic agent stopped for inadequate response or intolerance, or a documented contraindication to TNF blockers. Your 2026-10-30 GI note says "Biologic-naive; no prior anti-TNF therapy," and we found no documented TNF-blocker contraindication, so this part is currently not met. Please review and confirm the record is accurate and complete for this criterion.
- **C6**: Negative IGRA or TST result dated 2026-05-18 or later (who: lab)
  > For PA-2583 (PT-2583, ustekinumab-ttwe), Calder policy B.6 requires a negative TB screen (IGRA or tuberculin skin test) dated 2026-05-18 or later. We found no TB screening result in the chart. Please tell us whether one was drawn in this window and send the result, or let us know if the test still needs to be ordered and drawn. Indeterminate or borderline results do not count as negative.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | NOT_MET | NOT_MET | NOT_MET | ok |
| C6 | B.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
