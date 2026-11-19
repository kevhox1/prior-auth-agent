# Production plan

What would change between this demo and a pilot with a real practice. The demo runs on synthetic files, mocks submission and has no real patient data. Each section below says what the demo does today and what a pilot needs.

## 1. Getting the chart: EHR integration

**Today:** each chart is a folder of text files with a small header (document id, type, date, author).

**Pilot:**
- **Read from the EHR through its standard interface (FHIR).** That means the patient, conditions, medications, lab observations, procedures and clinical notes. Map each to the agent's existing document types. The document types were kept specialty-neutral for this reason (B4).
- **Outside records arrive as scanned faxes.** They need OCR before the agent sees them, and the OCR text must keep a link to the page image, so a reviewer can check a quote against the original. Synthetic "fax" charts are already in the test set, but real OCR errors will be worse.
- **Pull only what the policy needs.** The window is the policy's longest lookback plus prior-therapy history, not the whole record. This is the minimum-necessary rule for patient data, and it also keeps retrieval to one model call per case.
- **Write back to the EHR.** Pilot sites usually want three things written back: the signed letter as a document, a note that PA was submitted, and the payer's decision when it arrives.
- **Order entry.** Ideally the agent starts when a doctor orders a drug that the lookup table says needs PA, not when staff remember to start it.

## 2. Two submission rails

The agent already decides, per phase of therapy, which benefit pays. It writes one mock submission file per benefit.

| | Pharmacy benefit | Medical benefit |
|---|---|---|
| Typical drug | Self-injected (SC maintenance, PCSK9 inhibitors) | Clinic-given, buy and bill (IV induction) |
| Rail | Electronic prior authorization (ePA) on the NCPDP SCRIPT standard, through an ePA network the practice's prescribing system already uses | Payer web portal today. Electronic requests (X12 278, or the newer FHIR-based prior authorization APIs payers are building under CMS-0057-F) where the payer supports them |
| What comes back | Payer questions, which often arrive as a structured questionnaire | Usually a portal status, sometimes a fax |

**Pilot:**
- **Pharmacy benefit:** connect to the practice's existing ePA network first. It covers most payers through one integration, and payer questions arrive in a structured form the agent can answer from its checklist.
- **Medical benefit:** start with a human submitting through the portal from the agent's packet. Portal automation is brittle and payer-specific, so build it only for the highest-volume payers, and only after the packet quality is proven.
- **Keep the submission step outside the agent.** Under D2 the agent never submits. A separate service submits only after a recorded physician or nurse sign-off. The rules for that live in code today (`agent/submit.py`).
- **Do not quote CMS-0057-F decision deadlines for drugs.** They cover medical items and services, not drugs. Drug decision clocks come from the payer's policy or plan documents, which is what the lookup table holds.

## 3. Patient data (PHI) handling

**Today:** there is no real patient data. Every model call goes through a local Claude Code session.

**Pilot:**
- **Model access.** Use a model endpoint covered by a business associate agreement with the provider, with zero data retention where available. Use a separate account per client.
- **Treat the logs as patient data.** The audit log stores chart quotes and model reasoning for every case. In production, encrypt it at rest, restrict access by role, and set retention to the practice's record-retention policy. The model response cache must be off, or encrypted and scoped to one client.
- **Evaluation data.** Real cases enter the eval set only after de-identification. Synthetic cases stay the default for prompt development, so no engineer needs patient data to iterate.
- **Least privilege.** The agent's service account can read the chart sections it needs and write drafts. It cannot submit, sign or change orders.
- **Injection.** Chart text is data. The two-layer defense (model flag plus code scan, B23) stays. In production, flagged text also raises an alert to the practice, since it means someone edited a record.

## 4. Catching payer policy changes

A stale policy is the quietest way to fail. The agent would assemble a correct packet against rules that no longer apply.

**Today:** the policy version is pinned in three places: the policy file, the lookup table and the rules table. Intake refuses to run if they disagree.

**Pilot:**
- **Watch for changes.** A scheduled job fetches each payer's published policy page and drug lists, hashes them, and opens a review task when anything changes. This is cheap and needs no model.
- **Extract and compare.** On a change, the strongest model re-extracts the checklist (B39), and code diffs it against the approved version: criteria added or removed, lookbacks, logic, product lists.
- **Human approval.** A PA specialist approves the new checklist and the updated rules table. Until then, cases under the old version keep running and are tagged, and new cases are held only if the change is material.
- **Use denials as a signal.** A rise in denials for one payer and one criterion often means the payer changed its rules, or its reviewers changed their practice, before the document did.

## 5. What to monitor every week

| Metric | Why it matters | Where it comes from |
|---|---|---|
| **First-pass approval rate** (approved without additional information requests or appeal), by payer and drug | The outcome the practice pays for | Payer decisions written back |
| **Denial reasons mapped to criteria** | Tells you whether a denial was a criterion the agent called MET (the worst case, a false MET found in production), one it flagged but staff sent anyway, or a rule the checklist does not have | Denial letter reason, mapped to policy section |
| **Reviewer edit rate by reason code** (wrong evidence, missed evidence, wrong status, wording) | The main leading indicator of agent quality. Rising "missed evidence" usually means a new chart format; rising "wrong status" means a prompt or policy problem | `review.jsonl` |
| **Turnaround time** (order to submission, submission to decision) | Patient experience. A correct packet that takes three days is still a failure | Audit log timestamps plus decisions |
| **Escalation mix** (READY vs gaps vs physician) and **physician minutes per case** | Checks whether D1's split saves the time it promised | Outcomes and sign-off logs |
| **Code-check downgrades and verifier flags** | Each is a model error caught before a human saw it. A rise is an early warning | Audit log |
| **Cost and latency per case** | Model choice (`MODEL_COMPARISON.md`) | Audit log |

Any production false MET (a criterion the agent called MET that the payer denied on, and a reviewer confirms was wrong) is treated as an incident. It gets a root cause, a regression case added to the eval set, and a fix before the next prompt release.

## 6. Rolling out to a second practice

The reuse test (`DECISIONS.md` B41) showed that a new drug, payer and specialty is mostly data and configuration: a policy file, a gold checklist for evaluation, a lookup row and a rules row. It also showed where it is not:
- **Code checks that encode one specialty's habits.** The copy-forward date check needed a fix, and the weight-based dose check exists only for ustekinumab.
- **Prompt wording.** One gap prompt still says "gastroenterologist".

A second practice needs:
1. **Its payer mix.** Build the lookup and rules rows for its top payers and drugs, then have someone who works that practice's PA queue approve the extracted checklists.
2. **A local evaluation set.** 30 to 50 of its own recent PA cases, de-identified, with outcomes known from the payer's decisions. Run the agent offline and compare with what actually happened, before any reviewer sees live output.
3. **Its chart formats.** Templates, outside-record sources and fax quality differ. Expect retrieval misses at first. Watch the "missed evidence" edit rate in week one.
4. **Its staffing model.** Who signs what (D1) is a practice decision. Some practices let a nurse sign routine letters under a standing protocol; the sign-off rules are code and can be configured per practice.
5. **A shadow period.** For two to four weeks, the agent drafts and staff work as usual. Compare packets side by side, then switch to agent-first with human review.
6. **Clinician review of the open questions** in the README before go-live.
