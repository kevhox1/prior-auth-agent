# PA-3550: ustekinumab-ttwe for PT-3550

**Outcome: GAPS_TO_CLOSE**

- Payer: calder (commercial); policy calder-ustekinumab-ibd version 2026-07
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy benefit: 72 hours; medical benefit: 7 calendar days, from receipt of all required information (policy section E).
- Ordered dose: 390 mg IV once (weight 66.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy B.1): MET
_The member has moderately to severely active Crohn's disease or ulcerative colitis, as stated by the prescriber in the clinical record._

The GI note from 2026-11-04 states moderately to severely active ileocolonic Crohn's disease. This is the prescriber's statement in the clinical record. (confidence 0.96)

- `PT-3550/gi-note-2026-11-04` (2026-11-04): "A:
- Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity has been confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy dated 2026-10-11, within 12 months of the request, documents terminal ileal ulcers with erythema and edema. Biopsy confirms chronic active inflammation. This is direct visualization, not a lab marker. (confidence 0.97)

- `PT-3550/colonoscopy-2026-10-11` (2026-10-11): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."
- `PT-3550/colonoscopy-2026-10-11` (2026-10-11): "PATHOLOGY: Chronic active inflammation. No dysplasia."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

No chart passage retrieved documents the prescriber's specialty or a gastroenterology consultation. The specialty appears only in the request form, not in a quoted chart document. (confidence 0.70)

- Missing: Chart documentation of the prescriber's specialty (gastroenterologist), such as a signed GI note identifying Dr. Adeyemi's specialty, or a documented GI consultation

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

Date of birth 1996-02-13 makes the member 30 on the request date 2026-11-18. This is over 18. (confidence 0.98)

- `PT-3550/demographics-2026-10-23` (2026-10-23): "Date of birth: 1996-02-13"
- Code checks: age 30 on 2026-11-18 from DOB 1996-02-13

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either (a) a conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, an oral 5-aminosalicylate) that was stopped or found insufficient because of inadequate response, intolerance, or contraindication; or (b) a biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) that was stopped or found insufficient because of inadequate response or intolerance, or a documented contraindication to TNF blockers. One is enough. The record should identify the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker is not required before ustekinumab._

Adalimumab was used 2023-09 to 2026-07 and stopped for intolerance. Mercaptopurine (2022-08 to 2023-03) was also stopped for inadequate response. Each entry gives the drug, dates and reason. (confidence 0.96)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"
- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Mercaptopurine | 1.5 mg/kg daily | 2022-08 | 2023-03 | Inadequate response after 6 months at a therapeutic metabolite level |"

### C6 (policy B.6): MET
_Tuberculosis has been screened with an interferon-gamma release assay or tuberculin skin test with a negative result in the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A negative QuantiFERON-TB Gold Plus dated 2026-09-12 is within 6 months of the 2026-11-18 request. (confidence 0.95)

- `PT-3550/labs-2026-09-12` (2026-09-12): "QuantiFERON-TB Gold Plus | NEGATIVE | - | Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for both hepatitis B surface antigen and total hepatitis B core antibody (results may be of any age). A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both HBsAg and total core antibody results are documented and nonreactive. No prophylaxis plan is needed because neither is reactive. (confidence 0.96)

- `PT-3550/labs-2026-09-12` (2026-09-12): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3550/labs-2026-09-12` (2026-09-12): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these, the record shows the earlier agent is stopping._

The medication history states the member is on no biologic, JAK inhibitor or S1P modulator. Adalimumab ended 2026-07, so there is no concurrent use. (confidence 0.93)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "- Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

Weight 66.0 kg was recorded 2026-11-04, within 90 days of the request. It falls in the 390 mg tier (above 55 kg up to 85 kg). The maintenance of 90 mg SC every 8 weeks starting 8 weeks after the infusion matches the label. (confidence 0.95)

- `PT-3550/gi-note-2026-11-04` (2026-11-04): "- Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- `PT-3550/gi-note-2026-11-04` (2026-11-04): "- Weight 66.0 kg."
- Code checks: weight 66.0 kg (2026-11-04) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C3**: Chart documentation of prescriber's gastroenterology specialty or GI consultation (who: practice_staff)
  > For PA-3550 (PT-3550, ustekinumab-ttwe), criterion C3 (Policy B.3) needs chart documentation that the prescriber is a gastroenterologist. Could you locate and file a signed GI note identifying Dr. Adeyemi's specialty, or a documented GI consultation about this treatment? The specialty currently appears only on the request form.
  - Would satisfy the policy: Policy B.3 accepts chart documentation, such as a signed note from Dr. Adeyemi identifying the specialty as gastroenterology, or a documented consultation with a gastroenterologist about this treatment.

## Run cost

3 model calls, 17,019 input and 4,782 output tokens, 29.6 s of model time, $0.095 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: clean.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | - | ok |
| C5b | B.5(b) | MET | MET | - | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
