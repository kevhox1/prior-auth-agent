# PA-2083: ustekinumab-ttwe for PT-2083

**Outcome: NEEDS_PHYSICIAN**

- Payer: northfield (commercial); policy northfield-ustekinumab-ibd version 2026-10
- Request date 2026-11-18; requested start 2026-12-01; urgency **standard**
- Decision clock: Standard review. Pharmacy-benefit phase: decision within 72 hours of a complete request (policy section 7). Medical-benefit phase: per plan documents.
- Ordered dose: 390 mg IV once (weight 78.7 kg), then 90 mg SC every 8 weeks starting 8 weeks after the IV dose
- Benefit routing: iv_induction -> medical, sc_maintenance -> pharmacy
  - Two submissions: iv induction via the medical benefit; sc maintenance via the pharmacy benefit

## Checklist

### C1 (policy 3.1): MET
_The member has a diagnosis of moderately to severely active Crohn's disease or moderately to severely active ulcerative colitis. The treating provider must describe disease severity (for example, by symptom burden, a validated disease activity index, or endoscopic severity)._

The treating GI note documents moderately to severely active ileocolonic Crohn's disease and gives a Harvey-Bradshaw Index of 10. The problem list confirms the Crohn's diagnosis (K50.80). (confidence 0.95)

- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Moderately to severely active ileocolonic Crohn's disease."
- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Harvey-Bradshaw Index today: 10."
- `PT-2083/problem-list-2026-10-30` (2026-10-30): "1. Crohn's disease of both small and large intestine without complications (K50.80). Diagnosed 2019."

### C2 (policy 3.2): MET
_Objective evidence of active disease dated within the 12 months before the request: either (a) an endoscopy, colonoscopy, or flexible sigmoidoscopy report describing active inflammation (such as ulceration, erosions, or friability), or (b) a fecal calprotectin result above the upper limit of the performing laboratory's reference range. An elevated C-reactive protein or erythrocyte sedimentation rate alone does not satisfy this criterion. Imaging alone does not satisfy this criterion._

The fecal calprotectin of 1075 ug/g, dated 08/21/2026, is about 3 months before the request and well above the lab reference of <50. The result is reported in the provider note with its date and reference range, but the lab report itself is not in the chart, so the reviewer may want the source report. CRP alone and the 2019 colonoscopy do not count. (confidence 0.72)

- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- His calprotectin from 08/21/2026 came back at 1075 ug/g (lab reference <50)."

### C3 (policy 3.3): MET
_The medication is prescribed by, or in consultation with, a gastroenterologist._

The prescription is in the GI follow-up note, and the request lists the ordering provider as Dr. S. Adeyemi, Gastroenterology. (confidence 0.90)

- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 390 mg IV once (weight 78.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

### C4 (policy 3.4): MET
_The member is 18 years of age or older. Requests for members under 18 fall under policy NHP-CCP-RX-0413 and are outside this policy._

With a date of birth of 04/28/1991, the member is 35 on the request date. The outside record shows the same date of birth. (confidence 0.98)

- `PT-2083/demographics-2026-09-22` (2026-09-22): "Date of birth: 04/28/1991"
- Code checks: age 35 on 2026-11-18 from DOB 1991-04-28

### C5 (policy 3.5): **NOT MET**
_Both conventional therapy and anti-TNF therapy history are documented. For each prior therapy, the record must name the drug, give approximate start and stop dates, and state why it was stopped. Prior therapy must be supported by pharmacy or medical claims, prescription records, or treating-provider chart notes; a treating-provider history without supporting records may be accepted on prescriber attestation. If claims or other records on file are inconsistent with the reported history, the request is referred for clinical review and is not approved on the reported history alone._

**C5a (policy 3.5(a)): MET**: Inadequate response to, intolerance of, or contraindication to at least one conventional therapy. Conventional therapies are systemic corticosteroids (budesonide counts as a corticosteroid), azathioprine, 6-mercaptopurine, and methotrexate; for ulcerative colitis only, oral aminosalicylates (such as mesalamine) also count. Inadequate response to corticosteroids includes steroid dependence (relapse during taper or within 3 months of stopping) and steroid-refractory disease. Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

A treating-provider chart note names prednisone, gives dates (09/2019 to 02/2020) and gives the reason stopped: steroid dependence, which the policy counts as inadequate response. The blank treatment history in the 2019 outside record is missing information, not a conflict. No claims are on file to back this up. (confidence 0.80)

- `PT-2083/gi-note-2026-05-10` (2026-05-10): "- History: Prednisone 40 mg daily, tapered, 09/2019 to 02/2020. Reason stopped: steroid dependent (flared each time the dose went below 15 mg)."

**C5b (policy 3.5(b)): **NOT MET****: Inadequate response to, intolerance of, or contraindication to at least one TNF blocker: adalimumab or infliximab, including any biosimilar of either. Primary non-response, secondary loss of response, and intolerance each qualify. A contraindication must be specifically documented (for example, demyelinating disease or moderate to severe heart failure). Drug name, approximate start/stop dates, and reason for stopping must be documented and supported by claims, prescription records, chart notes, or prescriber attestation.

The treating GI note states outright that the member has had no prior anti-TNF therapy. No specific contraindication to adalimumab or infliximab is documented. (confidence 0.93)

- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Biologic-naive; no prior anti-TNF therapy."

### C6 (policy 3.6): **INSUFFICIENT**
_Negative tuberculosis screening test (interferon-gamma release assay or tuberculin skin test) dated within the 12 months before the request. An indeterminate IGRA is not a negative result. A test ordered but not resulted does not satisfy this criterion (per 2026-10 revision history). If the screening test is positive, the record must show active tuberculosis was excluded by chest imaging and that treatment for latent tuberculosis has been started._

None of the retrieved passages contains a TB screening result. The 09/2026 labs do not include an IGRA or TST. (confidence 0.90)

- Missing: Resulted tuberculosis screening test (IGRA or tuberculin skin test) dated within 12 months before 2026-11-18, showing a negative result

### C7 (policy 3.7): MET
_Results of both hepatitis B surface antigen (HBsAg) and total hepatitis B core antibody (anti-HBc) are on file. No lookback limit applies. If either result is positive, the record must include a plan for monitoring or antiviral prophylaxis. Hepatitis B vaccination history, or a hepatitis B surface antibody (anti-HBs) result alone, does not satisfy this criterion. A test that has been ordered but not resulted does not satisfy this criterion._

Both HBsAg (nonreactive) and total anti-HBc (reactive) have results on file. Because anti-HBc is positive, a plan is required, and the GI note documents HBV DNA and liver test monitoring every 3 months. (confidence 0.92)

- `PT-2083/labs-2026-09-25` (2026-09-25): "HEP B SURFACE AG .................. Nonreactive  (Nonreactive)"
- `PT-2083/labs-2026-09-25` (2026-09-25): "HEP B CORE AB TOTAL ............... Reactive  (Nonreactive)"
- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Resolved prior hepatitis B infection (HBsAg negative, anti-HBc positive, HBV DNA undetectable): monitor HBV DNA and liver tests every 3 months on therapy."

### C8 (policy 3.8): MET
_Ustekinumab will not be used together with another biologic agent, a Janus kinase (JAK) inhibitor (such as tofacitinib or upadacitinib), or a sphingosine 1-phosphate (S1P) receptor modulator (such as ozanimod or etrasimod). If the member is switching from one of these agents, the record must show that the prior agent has been or will be stopped._

The current GI note states the member is not taking a biologic, JAK inhibitor, or S1P receptor modulator. The member is biologic-naive, so no switch applies. (confidence 0.88)

- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- No current biologic, JAK inhibitor, or S1P receptor modulator."

### C9 (policy 3.9): MET
_Requested dose follows FDA-approved adult labeling. Induction: a single IV dose by body weight — 260 mg for 55 kg or less; 390 mg for more than 55 kg up to 85 kg; 520 mg for more than 85 kg. A current body weight dated within 30 days of the request must be documented for the induction dose. Maintenance: 90 mg subcutaneously every 8 weeks, starting 8 weeks after the IV dose. Maintenance intervals shorter than every 8 weeks are not approved on initial authorization._

The weight of 78.7 kg is dated 19 days before the request and falls in the >55 to 85 kg band, which calls for 390 mg IV. Maintenance of 90 mg SC every 8 weeks, starting 8 weeks after the IV dose, matches the label. (confidence 0.93)

- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Weight 78.7 kg."
- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 390 mg IV once (weight 78.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."
- Code checks: weight 78.7 kg (2026-10-30) -> label tier 390 mg; requested 390 mg

### C10 (policy 3.10): MET
_The request must name the specific ustekinumab product; a request for 'ustekinumab' without a product is incomplete. Preferred products are ustekinumab-aekn and ustekinumab-ttwe (IV and SC). All other ustekinumab products, including the reference (originator) product, are non-preferred and are covered only if the record documents either (a) an inadequate response to, or intolerance of, both preferred products (intolerance of only one preferred product does not satisfy this), or (b) a contraindication or documented hypersensitivity to an inactive ingredient present in both preferred products and absent from the requested product._

The request names the specific product ustekinumab-ttwe, which is one of the preferred products. (confidence 0.95)

- `PT-2083/gi-note-2026-10-30` (2026-10-30): "- Start ustekinumab-ttwe: 390 mg IV once (weight 78.7 kg), then 90 mg subcutaneously every 8 weeks starting 8 weeks after the IV dose."

## To-do list (gap plan)

- **C5b**: Provider review of prior TNF blocker history or a documented contraindication to adalimumab/infliximab (who: ordering_provider)
  > Dr. Adeyemi, for PA-2083 (PT-2083, ustekinumab-ttwe), Northfield policy 3.5(b) requires an inadequate response to, intolerance of, or contraindication to adalimumab or infliximab. Your GI note dated 2026-10-30 says "Biologic-naive; no prior anti-TNF therapy," and no contraindication to either drug is documented. Please review and tell us whether any prior TNF blocker trial or specifically documented contraindication exists that the chart does not show.
- **C6**: Negative IGRA or TST result dated 2025-11-18 or later (who: lab)
  > For PA-2083 (PT-2083, ustekinumab-ttwe), Northfield policy 3.6 requires a negative TB screening result (IGRA or tuberculin skin test) dated within 12 months before 2026-11-18. The 09/2026 labs do not include an IGRA or TST, and the chart has no TB screening result. Please send a resulted test if one exists. If not, a test needs to be drawn and resulted, because an ordered or indeterminate test does not count.

## Run cost

3 model calls, 0 input and 0 output tokens, 0 s of model time, $0.000 at list price (3 served from cache).

## Compared with gold (evaluation only; a reviewer would not see this)

Gold outcome NEEDS_PHYSICIAN; agent NEEDS_PHYSICIAN. Case type: multi_issue.

| Gold id | Policy | Gold | Agent | Model before checks | Result |
|---|---|---|---|---|---|
| C1 | 3.1 | MET | MET | MET | ok |
| C2 | 3.2 | MET | MET | MET | ok |
| C3 | 3.3 | MET | MET | MET | ok |
| C4 | 3.4 | MET | MET | MET | ok |
| C5a | 3.5(a) | MET | MET | MET | ok |
| C5b | 3.5(b) | NOT_MET | NOT_MET | NOT_MET | ok |
| C6 | 3.6 | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | INSUFFICIENT_EVIDENCE | ok |
| C7 | 3.7 | MET | MET | MET | ok |
| C8 | 3.8 | MET | MET | MET | ok |
| C9 | 3.9 | MET | MET | MET | ok |
| C10 | 3.10 | MET | MET | MET | ok |
