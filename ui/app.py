"""Reviewer UI (spec section 8, pipeline step 10).

    .venv/bin/streamlit run ui/app.py

Opens any case from any run under runs/. A reviewer approves, edits or rejects
each criterion; edits need a reason code. Sign-off stays disabled until every
criterion has a decision and the right role is signing (D1). Every action is
written to runs/<run>/<case>/review.jsonl and the case's audit log. Submission is mocked.
"""

from __future__ import annotations

import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from agent import intake as I  # noqa: E402
from agent.checks import normalize_ws  # noqa: E402
from agent.schemas import (  # noqa: E402
    EditReason, PacketOutcome, PipelineResult, ReviewAction, ReviewDecision, SignOff, Status,
)
from agent.submit import SignOffBlocked, blockers, mock_submit, required_role, save_review  # noqa: E402
from evals.metrics import find_case  # noqa: E402

RUNS = ROOT / "runs"
COLOR = {Status.MET: "green", Status.NOT_MET: "red", Status.INSUFFICIENT_EVIDENCE: "orange",
         Status.CONFLICTING: "violet"}
OUTCOME_COLOR = {PacketOutcome.READY_FOR_REVIEW: "green", PacketOutcome.GAPS_TO_CLOSE: "orange",
                 PacketOutcome.NEEDS_PHYSICIAN: "red"}


def badge(status: Status) -> str:
    return f":{COLOR[status]}-background[{status.value}]"


def highlight(text: str, quotes: list[str]) -> str:
    """Escape the document and mark each quote. Whitespace-tolerant, like the quote check."""
    out = html.escape(text)
    for q in quotes:
        q_esc = html.escape(normalize_ws(q))
        if q_esc and q_esc in out:
            out = out.replace(q_esc, f"<mark>{q_esc}</mark>")
        else:  # quote spans irregular whitespace: mark line by line
            for part in q.splitlines():
                p = html.escape(part.strip())
                if p and p in out:
                    out = out.replace(p, f"<mark>{p}</mark>")
    return f"<pre style='white-space:pre-wrap;font-size:0.85em'>{out}</pre>"


@st.cache_data
def list_results() -> dict[str, list[str]]:
    out = {}
    for run in sorted(RUNS.iterdir(), reverse=True) if RUNS.exists() else []:
        cases = sorted(p.parent.name for p in run.glob("PA-*/result.json"))
        if cases:
            out[run.name] = cases
    return out


def load(run: str, case: str):
    res = PipelineResult.model_validate_json((RUNS / run / case / "result.json").read_text())
    _, charts_dir = find_case(case)
    return res, I.load_chart(res.request.patient_id, charts_dir)


def audit_append(case_dir: Path, step: str, payload: dict) -> None:
    ev = {"timestamp": datetime.now(timezone.utc).isoformat(), "request_id": case_dir.name, "step": step,
          "payload": payload}
    with (case_dir / "audit.jsonl").open("a") as f:
        f.write(json.dumps(ev, default=str) + "\n")


def main() -> None:
    st.set_page_config(page_title="PA review", layout="wide")
    runs = list_results()
    if not runs:
        st.error("No runs yet. Run `python -m agent.pipeline PA-0001` first.")
        return
    with st.sidebar:
        st.caption("Synthetic data only. Not clinically validated. Not medical advice.")
        run = st.selectbox("Run", list(runs))
        case = st.selectbox("Case", runs[run])
        reviewer = st.text_input("Reviewer name", "R. Patel, RN")
        role = st.selectbox("Role", ["nurse", "pa_specialist", "physician"])
    res, chart = load(run, case)
    case_dir = RUNS / run / case
    key = f"{run}/{case}"
    decisions: dict[str, ReviewDecision] = st.session_state.setdefault(key, {})

    # 1. Header ---------------------------------------------------------------
    r = res.request
    st.title(f"{r.request_id}: {r.product}")
    c = st.columns(5)
    c[0].metric("Patient", r.patient_id)
    c[1].metric("Payer", f"{r.payer} ({r.plan_type.value})")
    c[2].metric("Urgency", r.urgency.value.upper())
    c[3].metric("Channels", ", ".join(f"{k.split('_')[0].upper()}: {v.value}" for k, v in res.routing.channels.items()))
    c[4].markdown(f"**Outcome**  \n:{OUTCOME_COLOR[res.outcome]}-background[{res.outcome.value}]")
    st.caption(f"Policy {res.policy_id} v{res.policy_version}. {res.intake.decision_clock}")
    for n in res.routing.notes:
        st.info(n)
    if res.injection_flags:
        with st.container(border=True):
            st.error("Text in the chart addressed to an automated reviewer. The agent ignored it. Check where it came from.")
            for f in res.injection_flags:
                st.markdown(f"- `{f.doc_id}`: _{html.escape(f.quote)}_")

    # 2. Checklist with decisions ------------------------------------------------
    st.header("Checklist")
    a_by_id = {a.criterion_id: a for a in res.assessments}
    for crit in res.checklist.criteria:
        leaves = crit.sub_criteria or [crit]
        st.subheader(f"{crit.id} (policy {crit.policy_ref}) {badge(res.rolled_up[crit.id])}")
        if crit.sub_criteria:
            st.caption(f"{crit.logic.value} of the parts below. {crit.text}")
        for leaf in leaves:
            a = a_by_id[leaf.id]
            with st.container(border=True):
                left, right = st.columns([3, 2])
                with left:
                    st.markdown(f"**{leaf.id}** {badge(a.status)}  confidence {a.confidence:.2f}")
                    st.caption(leaf.text)
                    if a.status_before_checks:
                        st.warning(f"Code check changed the model's {a.status_before_checks.value} to {a.status.value}.")
                    st.write(a.reasoning)
                    for e in a.evidence:
                        doc = chart.get(e.doc_id)
                        with st.expander(f"“{e.quote.strip()[:110]}” - {e.doc_id} ({e.doc_date})"):
                            if doc:
                                st.markdown(highlight(doc.text, [x.quote for x in a.evidence if x.doc_id == doc.doc_id]),
                                            unsafe_allow_html=True)
                    for m in a.missing_items:
                        st.markdown(f"- Missing: **{m}**")
                    if a.deterministic_checks.notes:
                        st.caption("Code checks: " + "; ".join(a.deterministic_checks.notes))
                with right:
                    action = st.radio("Decision", ["approve", "edit", "reject"], horizontal=True,
                                      key=f"{key}/{leaf.id}/action", index=None)
                    reason = new_status = note = None
                    if action == "edit":
                        reason = st.selectbox("Reason (required)", [e.value for e in EditReason], key=f"{key}/{leaf.id}/reason")
                        new_status = st.selectbox("Corrected status", ["(unchanged)"] + [s.value for s in Status],
                                                  key=f"{key}/{leaf.id}/new")
                    if action in ("edit", "reject"):
                        note = st.text_input("Note", key=f"{key}/{leaf.id}/note")
                    if action:
                        d = ReviewDecision(
                            criterion_id=leaf.id, action=ReviewAction(action),
                            reason_code=EditReason(reason) if reason else None,
                            new_status=Status(new_status) if new_status and new_status != "(unchanged)" else None,
                            reviewer=reviewer, reviewer_role=role, note=note or None,
                            timestamp=datetime.now(timezone.utc))
                        if decisions.get(leaf.id, None) is None or decisions[leaf.id].model_dump(exclude={"timestamp"}) \
                                != d.model_dump(exclude={"timestamp"}):
                            decisions[leaf.id] = d
                            save_review(case_dir, [d])
                            audit_append(case_dir, "10_review_decision", d.model_dump(mode="json"))

    # 3. Gap list -------------------------------------------------------------------
    if res.gaps:
        st.header("To-do list")
        for g in res.gaps:
            with st.container(border=True):
                st.markdown(f"**{g.criterion_id}**: {g.missing_item}  \nWho can supply it: `{g.who_can_supply.value}`")
                st.text_area("Drafted message", g.clinician_query, key=f"{key}/gap/{g.criterion_id}")
                if g.would_satisfy:
                    st.caption(f"Would satisfy the policy: {g.would_satisfy}")

    # 4 and 5. Packet and verification ----------------------------------------------
    if res.packet:
        bad = {c.claim_ref: c.issue for c in res.verification.checks if not c.supported} if res.verification else {}
        st.header("Draft PA form")
        for f in res.packet.form_fields:
            flag = bad.get(f"form:{f.name}")
            line = f"**{f.name}:** {f.value}  " + " ".join(f"`{c.doc_id}`" for c in f.citations)
            st.markdown(f":red[{line} - verifier: {flag}]" if flag else line)
        st.header("Draft letter of medical necessity")
        cites = []
        for i, s in enumerate(res.packet.letter):
            nums = []
            for c in s.citations:
                cites.append(c)
                nums.append(str(len(cites)))
            text = s.text + (f" [{', '.join(nums)}]" if nums else "")
            flag = bad.get(f"letter:{i}")
            st.markdown(f":red[{text}] - **verifier: {flag}**" if flag else text)
        with st.expander("Citations"):
            for n, c in enumerate(cites, 1):
                st.markdown(f"[{n}] `{c.doc_id}`: “{c.quote.strip()}”")
        st.header("Independent verification")
        if res.packet_code_issues:
            st.error("Code citation check: " + "; ".join(res.packet_code_issues))
        if res.verification and res.verification.overall_pass:
            st.success(f"All {len(res.verification.checks)} claims supported.")
        elif res.verification:
            st.error(f"{len(bad)} claim(s) flagged by the verifier (shown in red above).")

    # 6 and 7. Sign-off ----------------------------------------------------------------
    st.header("Sign-off")
    need = required_role(res)
    st.caption(f"Required signer: {'physician' if need == 'physician' else 'nurse or PA specialist'} (D1).")
    options = ["submit", "return_to_staff"] if res.packet else ["reviewed_no_submission", "return_to_staff"]
    decision = st.radio("Decision", options, horizontal=True, key=f"{key}/signoff")
    note = st.text_input("Sign-off note (to override a verifier flag, start with 'Override:' and say why)",
                         key=f"{key}/signoff_note")
    so = SignOff(reviewer=reviewer, reviewer_role=role, decision=decision, note=note or None,
                 timestamp=datetime.now(timezone.utc))
    problems = blockers(res, list(decisions.values()), so)
    for p in problems:
        st.warning(p)
    if st.button("Sign off", type="primary", disabled=bool(problems)):
        save_review(case_dir, [], so)
        audit_append(case_dir, "10_signoff", so.model_dump(mode="json"))
        if decision == "submit":
            try:
                sub = mock_submit(res, list(decisions.values()), so, case_dir)
            except SignOffBlocked as e:
                st.error(str(e))
            else:
                audit_append(case_dir, "11_mock_submission", {"dir": str(sub.relative_to(ROOT))})
                st.success(f"Mock submission written to {sub.relative_to(ROOT)}")
        else:
            st.success("Recorded.")


main()
