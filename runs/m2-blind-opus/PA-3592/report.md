# PA-3592: ustekinumab-ttwe for PT-3592

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 260 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-10-30 states moderately to severely active ileocolonic Crohn's disease. The HBI of 13 and ongoing symptoms support this. (confidence 0.95)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): **INSUFFICIENT**
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy done within the past 12 months that documents active mucosal inflammation. Lab markers (including fecal calprotectin, C-reactive protein and sedimentation rate) do not meet this requirement on their own. Cross-sectional imaging studies do not meet it either._

The only evidence of activity is lab markers (calprotectin, CRP), and the policy says these do not count on their own. No endoscopy report from the past 12 months is in the passages. (confidence 0.92)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "His calprotectin from 08/23/2026 came back at 1306 ug/g (lab reference <50)."
- `PT-3592/labs-2026-09-21` (2026-09-21): "CRP | 24.1 mg/L | H | <5.0"
- Missing: Ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy report dated 2025-11-18 or later documenting active mucosal inflammation

### C3 (policy B.3): MET
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. M. Chen, Gastroenterology. The ustekinumab plan is written in the GI follow-up note. The quoted line does not name the specialty itself, so the reviewer may want to confirm the note's signature. (confidence 0.85)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request. Members under 18 are not covered by this policy and are reviewed case by case by a Calder Mutual pharmacist._

With a date of birth of 05/12/1990, the member is 36 on the 2026-11-18 request date, which is over 18. (confidence 0.97)

- `PT-3592/demographics-2025-10-15` (2025-10-15): "Date of birth: 05/12/1990"
- Code checks: age 36 on 2026-11-18 from DOB 1990-05-12

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) or (b). One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (an oral or IV corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC only, also an oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

Budesonide is a listed conventional agent. It was used 09/2022 to 12/2022 and stopped for inadequate response, which gives the drug, the dates and the reason. (confidence 0.93)

- `PT-3592/medication-history-2026-10-28` (2026-10-28): "| Budesonide | 9 mg daily | 09/2022 | 12/2022 | Inadequate response after 10 weeks |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, OR there is a documented contraindication to TNF blockers.

The prescriber documents a contraindication to TNF blockers due to multiple sclerosis, which is on the problem list. This satisfies the contraindication branch of part (b). The vedolizumab trial has no documented start date or reason, but that is not needed here. (confidence 0.88)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Anti-TNF agents are contraindicated because of multiple sclerosis (demyelinating disease)."
- `PT-3592/problem-list-2026-10-30` (2026-10-30): "2. Multiple sclerosis, relapsing-remitting (G35)."

### C6 (policy B.6): **INSUFFICIENT**
_Tuberculosis screening with an interferon-gamma release assay or tuberculin skin test gave a negative result within the past 6 months. An indeterminate or borderline result does not count as negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease AND that treatment for latent TB infection has begun._

No IGRA or tuberculin skin test result was found in the passages. A negative result dated within 6 months of the request is required. (confidence 0.93)

- Missing: IGRA or TST result dated 2026-05-18 or later

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody. The results may be of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not enough. Pending orders are not enough._

Both HBsAg and total anti-HBc are resulted as nonreactive on 2026-09-21. No antiviral plan is needed. (confidence 0.95)

- `PT-3592/labs-2026-09-21` (2026-09-21): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3592/labs-2026-09-21` (2026-09-21): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. If the member is switching from one of these agents, the record shows the earlier agent is being stopped._

The member's current biologic is vedolizumab. Both the medication history and the prescriber's note document that it will be stopped when ustekinumab starts. No other biologic, JAK inhibitor or S1P modulator is listed. (confidence 0.90)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "- Stop vedolizumab; ustekinumab induction on the date of the next scheduled vedolizumab infusion."
- `PT-3592/medication-history-2026-10-28` (2026-10-28): "- Vedolizumab 300 mg IV every 8 weeks (last infusion 10/16/2026); to be discontinued when ustekinumab starts."

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based IV induction infusion (260 mg for weight up to and including 55 kg; 390 mg for weight above 55 kg up to and including 85 kg; 520 mg for weight above 85 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the infusion. A body weight recorded within the 90 days before the request must be on file._

A weight of 55.0 kg was recorded on 2026-10-30, within 90 days of the request. That falls in the up-to-and-including-55 kg band, which matches the 260 mg IV dose, and the maintenance dose of 90 mg SC every 8 weeks matches the label. The 58.0 kg weight from 2026-06-01 is outside the window, so it does not decide this criterion. (confidence 0.90)

- `PT-3592/gi-note-2026-10-30` (2026-10-30): "Weight 55.0 kg."
- `PT-3592/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 260 mg IV once (weight 55.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 55.0 kg (2026-10-30) -> label tier 260 mg; requested 260 mg

## To-do list (gap plan)

- **C2**: Endoscopy report (ileocolonoscopy, colonoscopy or flexible sigmoidoscopy) dated 2025-11-18 or later documenting active mucosal inflammation (who: practice_staff)
  > For PA-3592 (PT-3592, ustekinumab-ttwe), criterion B.2 needs disease activity confirmed by direct visualization. The chart has only lab markers: calprotectin 1306 ug/g (08/23/2026, cited in the 2026-10-30 GI note) and CRP 24.1 mg/L (2026-09-21). The policy says lab markers don't count on their own. Please find and file any ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report dated 2025-11-18 or later, including any done at an outside facility, or tell us if none exists.
  - Would satisfy the policy: Policy B.2 accepts an ileocolonoscopy, colonoscopy or flexible sigmoidoscopy report dated on or after 2025-11-18 that documents active mucosal inflammation. Lab markers alone and cross-sectional imaging are not accepted.
- **C6**: Negative IGRA or TST result dated 2026-05-18 or later (who: practice_staff)
  > For PA-3592 (PT-3592, ustekinumab-ttwe), criterion B.6 needs a negative TB screen (IGRA or tuberculin skin test) from the past 6 months. We found no IGRA or TST result in the chart. Please find and file any result dated 2026-05-18 or later, or tell Dr. Chen if none is on file.
  - Would satisfy the policy: Policy B.6 accepts a negative IGRA or TST dated on or after 2026-05-18. An indeterminate or borderline result does not count. If the screen is positive, the policy requires a chest radiograph showing no active disease plus documentation that treatment for latent TB has begun.

## Run cost

3 model calls, 18,825 input and 6,315 output tokens, 57.6 s of model time, $0.235 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome GAPS_TO_CLOSE; agent GAPS_TO_CLOSE. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C3 | B.3 | MET | MET | MET | ok |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
