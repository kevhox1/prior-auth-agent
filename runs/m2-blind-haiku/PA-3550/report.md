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

The GI prescriber's note dated 2026-11-04 states moderately to severely active ileocolonic Crohn's disease. The Harvey-Bradshaw Index of 14 on the same date supports that statement. No passage contradicts it. (confidence 0.93)

- `PT-3550/gi-note-2026-11-04` (2026-11-04): "Moderately to severely active ileocolonic Crohn's disease."

### C2 (policy B.2): MET
_Disease activity is confirmed by direct visualization: an ileocolonoscopy, colonoscopy, or flexible sigmoidoscopy performed within the past 12 months that documents active mucosal inflammation. Laboratory markers (including fecal calprotectin, C-reactive protein, and sedimentation rate) do not meet this requirement on their own, and neither do cross-sectional imaging studies._

A colonoscopy dated 2026-10-11 falls within the 12-month lookback from the 2026-11-18 request date. The report documents ulcers, erythema and edema in the terminal ileum, which is direct visualization of active mucosal inflammation. Calprotectin and CRP are not relied on for this finding. (confidence 0.90)

- `PT-3550/colonoscopy-2026-10-11` (2026-10-11): "PROCEDURE: Colonoscopy with biopsies"
- `PT-3550/colonoscopy-2026-10-11` (2026-10-11): "- Terminal ileum: multiple ulcers 0.3-1.5 cm with surrounding erythema and edema."

### C3 (policy B.3): **INSUFFICIENT**
_The prescriber is a gastroenterologist, or the prescriber has consulted with a gastroenterologist about this treatment._

The request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology, but no chart passage documents the prescriber's specialty or a consultation with a gastroenterologist. The request header alone is not chart documentation. (confidence 0.60)

- Missing: Chart documentation of the prescriber's specialty (for example, a signature block or credentials on the GI note), or a documented consultation with a gastroenterologist about ustekinumab

### C4 (policy B.4): MET
_The member is at least 18 years old on the date of the request._

The date of birth of 1996-02-13 makes the member 30 years old on the 2026-11-18 request date, which is over 18. (confidence 0.97)

- `PT-3550/demographics-2026-10-23` (2026-10-23): "Date of birth: 1996-02-13"
- Code checks: age 30 on 2026-11-18 from DOB 1996-02-13

### C5 (policy B.5): MET
_The member has tried at least one prior therapy for CD or UC, shown by either sub-criterion (a) or (b); one is enough. The record identifies the drug, roughly when it was used, and why it was stopped. A trial of a TNF blocker before ustekinumab is not required._

**C5a (policy B.5(a)): MET**: A conventional agent (oral or intravenous corticosteroid, budesonide, azathioprine, mercaptopurine, or methotrexate; for UC, oral 5-aminosalicylate) was stopped or found insufficient because of inadequate response, intolerance, or contraindication.

The medication history lists mercaptopurine used 2022-08 to 2023-03 and stopped for inadequate response. It also lists budesonide used 2023-04 to 2023-07 and stopped for inadequate response. Either one satisfies the conventional-agent step. (confidence 0.92)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Mercaptopurine | 1.5 mg/kg daily | 2022-08 | 2023-03 | Inadequate response after 6 months at a therapeutic metabolite level |"
- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Budesonide | 9 mg daily | 2023-04 | 2023-07 | Inadequate response after 10 weeks |"

**C5b (policy B.5(b)): MET**: A biologic or targeted synthetic agent for CD or UC (for example adalimumab, infliximab, vedolizumab, certolizumab, risankizumab, tofacitinib, upadacitinib, ozanimod) was stopped or found insufficient because of inadequate response or intolerance, or there is a documented contraindication to TNF blockers.

The medication history records adalimumab, a TNF blocker, used 2023-09 to 2026-07 and stopped for intolerance. That satisfies the biologic step with a dated trial and a stated reason. (confidence 0.90)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C6 (policy B.6): MET
_Tuberculosis has been screened for with an interferon-gamma release assay or tuberculin skin test with a negative result within the past 6 months. An indeterminate or borderline result is not negative. A member with a positive screen qualifies only if the record shows a chest radiograph without active disease and that treatment for latent infection has begun._

A QuantiFERON-TB Gold Plus dated 2026-09-12 is reported as negative. That is within the 6-month window before the 2026-11-18 request date, and no indeterminate result is recorded. (confidence 0.93)

- `PT-3550/labs-2026-09-12` (2026-09-12): "QuantiFERON-TB Gold Plus | NEGATIVE | - | Negative"

### C7 (policy B.7): MET
_Hepatitis B status is documented with results for hepatitis B surface antigen and total hepatitis B core antibody, of any age. A reactive result requires a documented plan for antiviral prophylaxis or monitoring. Surface antibody results and vaccination records are not sufficient. Pending orders are not sufficient._

Both hepatitis B surface antigen and total core antibody are reported as nonreactive on 2026-09-12. Because neither is reactive, no antiviral plan is required. (confidence 0.95)

- `PT-3550/labs-2026-09-12` (2026-09-12): "HBsAg | Nonreactive | - | Nonreactive"
- `PT-3550/labs-2026-09-12` (2026-09-12): "Anti-HBc (total) | Nonreactive | - | Nonreactive"

### C8 (policy B.8): MET
_Ustekinumab will not be combined with any other biologic, JAK inhibitor, or S1P receptor modulator for CD or UC. When the member is switching from one of these agents, the record shows the earlier agent is stopping._

The 2026-10-31 medication reconciliation states the member is not on any advanced therapy. The prior adalimumab has a documented stop date of 2026-07, so the earlier agent is recorded as stopped before ustekinumab. (confidence 0.85)

- `PT-3550/medication-history-2026-10-31` (2026-10-31): "Not currently on any advanced therapy (biologic, JAK inhibitor, or S1P receptor modulator)."
- `PT-3550/medication-history-2026-10-31` (2026-10-31): "| Adalimumab | 40 mg every 2 weeks | 2023-09 | 2026-07 | Intolerance (drug-induced lupus with positive anti-histone antibodies and arthralgias) |"

### C9 (policy B.9): MET
_The requested regimen is the labeled adult regimen: one weight-based intravenous induction infusion (260 mg up to and including 55 kg; 390 mg above 55 kg up to and including 85 kg; 520 mg above 85 kg), then 90 mg subcutaneously every 8 weeks beginning 8 weeks after the infusion. A body weight recorded in the 90 days before the request must be on file._

A weight of 66.0 kg recorded on 2026-11-04 is within 90 days of the request. That weight falls in the 390 mg band (above 55 kg up to 85 kg), and the requested 390 mg IV then 90 mg SC every 8 weeks matches the labeled regimen. (confidence 0.93)

- `PT-3550/gi-note-2026-11-04` (2026-11-04): "Weight 66.0 kg."
- `PT-3550/gi-note-2026-11-04` (2026-11-04): "Start ustekinumab-ttwe: 390 mg IV once (weight 66.0 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 66.0 kg (2026-11-04) -> label tier 390 mg; requested 390 mg

## To-do list (gap plan)

- **C3**: Chart documentation of the prescriber's specialty (signature block or credentials on a GI note), or a documented consultation with a gastroenterologist about ustekinumab (who: practice_staff)
  > Criterion C3 (prescriber is a gastroenterologist or consulted one) is open for PA-3550. The request lists Dr. S. Adeyemi, Gastroenterology, but no chart document shows the prescriber's specialty or a GI consultation about ustekinumab. Please locate a signed GI note, signature block, or consult documentation for Dr. Adeyemi and file it with the request.
  - Would satisfy the policy: Policy B.3 accepts chart documentation of the prescriber's gastroenterology specialty, or a documented consultation with a gastroenterologist about ustekinumab, dated on or before the request date 2026-11-18.

## Run cost

3 model calls, 19,049 input and 9,843 output tokens, 40.0 s of model time, $0.008 at list price (0 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome READY_FOR_REVIEW; agent GAPS_TO_CLOSE. Case type: clean.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | B.1 | MET | MET | MET | ok |
| C2 | B.2 | MET | MET | MET | ok |
| C3 | B.3 | MET | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | wrong |
| C4 | B.4 | MET | MET | MET | ok |
| C5a | B.5(a) | MET | MET | MET | ok |
| C5b | B.5(b) | MET | MET | MET | ok |
| C6 | B.6 | MET | MET | MET | ok |
| C7 | B.7 | MET | MET | MET | ok |
| C8 | B.8 | MET | MET | MET | ok |
| C9 | B.9 | MET | MET | MET | ok |
