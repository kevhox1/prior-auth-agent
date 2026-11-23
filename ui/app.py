"""Reviewer UI (spec section 8, pipeline step 10).

    .venv/bin/streamlit run ui/app.py

Opens any case from any run under runs/. A reviewer approves, edits or rejects
each criterion; edits need a reason code. Sign-off stays disabled until every
criterion has a decision and the right role is signing (D1). Every action is
written to runs/<run>/<case>/review.jsonl and the case's audit log. Submission is mocked.

The look comes from ui/styles.css (design tokens + a skin for Streamlit's widgets).
Static parts are HTML blocks; anything a reviewer acts on is a Streamlit widget.
"""

from __future__ import annotations

import html
import json
import re
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
CSS = (Path(__file__).parent / "styles.css").read_text()
FONTS = ("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700"
         "&family=Space+Grotesk:wght@500;600;700&display=swap")
DISCLAIMER = "Synthetic data only. Not clinically validated. Not medical advice."
DEFAULT_RUN = "m5-ibd-hand-v3"  # opens on the happy-path demo case (PA-0001)
PAYER_NAMES = {"northfield": "Northfield Health Plan", "calder": "Calder Mutual"}

STATUS_CLASS = {Status.MET: "met", Status.NOT_MET: "notmet", Status.INSUFFICIENT_EVIDENCE: "insuf",
                Status.CONFLICTING: "conf"}
OUTCOME = {  # class, icon, one-line meaning
    PacketOutcome.READY_FOR_REVIEW: ("met", "check", "Every criterion is met"),
    PacketOutcome.GAPS_TO_CLOSE: ("insuf", "pending", "Evidence is missing; see the to-do list"),
    PacketOutcome.NEEDS_PHYSICIAN: ("notmet", "warn", "A physician must resolve this case"),
}

# Icons from the design (24px grid, stroke = currentColor).
_ICONS = {
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6z"/><path d="M12 8.5v4.5"/><path d="M12 16v.01"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5"/><path d="M12 7.5v.01"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.8 2.8L16 9.5"/>',
    "x": '<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
    "pending": '<circle cx="12" cy="12" r="9" stroke-dasharray="3.2 3"/><path d="M12 8v5"/><path d="M12 16.5v.01"/>',
    "swap": '<path d="M4 8h13l-3-3"/><path d="M20 16H7l3 3"/>',
    "warn": '<path d="M12 3.5l9.5 16.5h-19z"/><path d="M12 10v4.5"/><path d="M12 17.5v.01"/>',
    "arrow": '<path d="M4 12h15"/><path d="M14 7l5 5-5 5"/>',
    "chevron": '<path d="M9 6l6 6-6 6"/>',
    "tick": '<path d="M7 12.5l3.3 3.3L17.5 8"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.5l3.5 2"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c1.2-4 4-6 7.5-6s6.3 2 7.5 6"/>',
    "list": '<path d="M9 6.5h11M9 12h11M9 17.5h11"/><path d="M4.5 6.5v.01M4.5 12v.01M4.5 17.5v.01"/>',
    "lock": '<rect x="5" y="11" width="14" height="9.5" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "code": '<path d="M8.5 7l-5 5 5 5"/><path d="M15.5 7l5 5-5 5"/>',
}
STATUS_ICON = {"met": "check", "notmet": "x", "insuf": "pending", "conf": "swap"}


def icon(name: str, size: int = 15, width: float = 2.2) -> str:
    return (f'<svg class="pa-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{_ICONS[name]}</svg>')


def e(s) -> str:
    return html.escape(str(s))


_BLOCK_TAGS = re.compile(r"<(/?)(h1|h2|h3|p|ul|li)\b")


def block(markup: str) -> None:
    """Render an HTML fragment. st.markdown keeps inline SVG and <details>, which st.html strips.
    Headings, paragraphs and lists become divs so Streamlit's markdown styles don't override the design,
    and newlines become entities so a blank line in chart text can't end the HTML block."""
    markup = _BLOCK_TAGS.sub(lambda m: f"<{m.group(1)}div", markup).replace("\n", "&#10;")
    st.markdown(f'<div class="pa-x">{markup}</div>', unsafe_allow_html=True)


def pill(status: Status) -> str:
    c = STATUS_CLASS[status]
    return f'<span class="pa-pill is-{c}">{icon(STATUS_ICON[c], 13, 2.4)}{e(status.value)}</span>'


def tag(doc_id: str) -> str:
    return f'<span class="pa-tag" title="{e(doc_id)}">{e(doc_id.split("/")[-1])}</span>'


def section_head(title: str, hint: str = "") -> None:
    block(f'<div class="pa-section-head"><h2 class="pa-section-title">{e(title)}</h2>'
          f'<span class="pa-section-hint">{e(hint)}</span></div>')


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
    return f'<div class="pa-doc">{out}</div>'


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


# --------------------------------------------------------------------------------------------
# Sections
# --------------------------------------------------------------------------------------------

def sidebar(runs: dict[str, list[str]]):
    with st.sidebar:
        block(f'<div class="pa-brand"><div class="pa-brand-mark">{icon("shield", 22, 2)}</div><div>'
              '<div class="pa-brand-name">Prior Auth Agent</div><div class="pa-brand-sub">Reviewer console</div>'
              '</div></div>')
        block('<span class="pa-eyebrow">Case</span>')
        names = list(runs)
        run = st.selectbox("Run", names, index=names.index(DEFAULT_RUN) if DEFAULT_RUN in names else 0)
        case = st.selectbox("Case", runs[run])
        block('<div class="pa-sidebar-rule"></div>')
        block('<span class="pa-eyebrow">Reviewer</span>')
        reviewer = st.text_input("Reviewer name", "R. Patel, RN")
        role = st.selectbox("Role", ["nurse", "pa_specialist", "physician"])
        block('<div class="pa-sidebar-rule"></div>')
        block(f'<div class="pa-disclaimer">{icon("info")}<span>{DISCLAIMER}</span></div>')
    return run, case, reviewer, role


def hero(res: PipelineResult) -> None:
    r = res.request
    oc, oi, osub = OUTCOME[res.outcome]
    with st.container(key="hero"):
        left, right = st.columns([3, 2], vertical_alignment="top")
        with left:
            st.title(f"{r.request_id} · {r.product}", anchor=False)
            block(f'<p class="pa-hero-practice">{e(r.ordering_provider)} · Request date {e(r.request_date)}</p>')
        with right:
            block(f'<div class="pa-outcome is-{oc}">{icon(oi, 28, 2)}<div><div class="pa-outcome-label">'
                  f'{e(res.outcome.value)}</div><div class="pa-outcome-sub">{e(osub)}</div></div></div>')
        payer = PAYER_NAMES.get(r.payer, r.payer.title())
        urgent = r.urgency.value == "expedited"
        chips = (f'<span class="pa-chip"><span class="pa-chip-key">Patient</span>'
                 f'<span class="pa-chip-val pa-mono">{e(r.patient_id)}</span></span>'
                 f'<span class="pa-chip"><span class="pa-chip-key">Payer</span>'
                 f'<span class="pa-chip-val">{e(payer)} ({e(r.plan_type.value)})</span></span>'
                 f'<span class="pa-chip{" pa-chip--expedited" if urgent else ""}"><span class="pa-chip-key">Urgency'
                 f'</span><span class="pa-chip-val">{e(r.urgency.value.upper())}</span></span>'
                 f'<span class="pa-chip"><span class="pa-chip-key">Diagnosis</span>'
                 f'<span class="pa-chip-val pa-mono">{e(r.indication_icd10)}</span></span>')
        routes = "".join(
            f'<span class="pa-route">{e(phase.replace("_", " ").replace("iv ", "IV ").replace("sc ", "SC "))}'
            f'<span class="pa-route-arrow">{icon("arrow", 16)}</span>'
            f'<span class="pa-route-benefit">{e(ch.value)} benefit</span></span>'
            for phase, ch in res.routing.channels.items())
        n_sub = len(set(res.routing.channels.values()))
        if n_sub > 1:
            routes += f'<span class="pa-chip pa-chip--accent">{n_sub} submissions</span>'
        block(f'<div class="pa-chip-row">{chips}</div>')
        block(f'<div class="pa-routing"><span class="pa-eyebrow">Benefit routing</span>{routes}</div>')
        block(f'<p class="pa-hero-policy">Policy <span class="pa-mono">{e(res.policy_id)} v{e(res.policy_version)}'
              f'</span> · {e(res.intake.decision_clock)}</p>')


def summary(res: PipelineResult, key: str) -> None:
    counts = {s: sum(a.status == s for a in res.assessments) for s in Status}
    labels = {Status.INSUFFICIENT_EVIDENCE: "INSUFFICIENT"}
    stats = "".join(
        f'<div class="pa-card pa-stat is-{STATUS_CLASS[s]}{" is-zero" if not n else ""}"><div class="pa-stat-top">'
        f'{icon(STATUS_ICON[STATUS_CLASS[s]], 15, 2.4)}{labels.get(s, s.value)}</div>'
        f'<div class="pa-stat-num">{n}</div></div>' for s, n in counts.items())
    total = len(res.assessments)
    done = sum(st.session_state.get(f"{key}/{a.criterion_id}/action") is not None for a in res.assessments)
    pct = round(100 * done / total) if total else 0
    block(f'<section class="pa-summary">{stats}<div class="pa-card pa-progress-card">'
          f'<span class="pa-eyebrow">Review progress</span><p class="pa-progress-text"><strong>{done} of {total}'
          f'</strong> criteria reviewed</p><div class="pa-progress"><div class="pa-progress-fill" '
          f'style="width:{pct}%"></div></div></div></section>')


def injection_alert(res: PipelineResult, chart) -> None:
    for f in res.injection_flags:
        doc = chart.get(f.doc_id)
        when = f" · dated {e(doc.date)}" if doc is not None and getattr(doc, "date", None) else ""
        block(f'<section class="pa-alert"><div class="pa-alert-icon">{icon("lock", 22, 2)}</div>'
              '<div class="pa-alert-body"><h2 class="pa-alert-title">Text in the chart addressed to an automated '
              'reviewer was ignored.</h2><p class="pa-alert-text">The agent treated the passage as untrusted chart '
              'content and did not change any criterion because of it. Check where it came from.</p>'
              f'<div class="pa-alert-quote">{e(f.quote)}</div><div class="pa-alert-meta"><span>Source</span>'
              f'{tag(f.doc_id)}<span>{e(f.doc_id)}{when}</span></div></div></section>')


def criterion_body(leaf, a, chart) -> str:
    c = STATUS_CLASS[a.status]
    parts = [
        f'<div class="pa-crit-head"><span class="pa-crit-id">{e(leaf.id)}</span>'
        f'<span class="pa-crit-section">Policy {e(leaf.policy_ref)}</span>{pill(a.status)}'
        f'<div class="pa-conf-meter is-{c}"><span>Confidence</span><div class="pa-conf-track">'
        f'<div class="pa-conf-fill" style="width:{round(a.confidence * 100)}%"></div></div>'
        f'<span class="pa-conf-value">{a.confidence:.2f}</span></div></div>',
        f'<p class="pa-crit-text">{e(leaf.text)}</p>',
        f'<p class="pa-reasoning">{e(a.reasoning)}</p>',
    ]
    if a.evidence:
        rows = []
        for ev in a.evidence:
            doc = chart.get(ev.doc_id)
            body = (highlight(doc.text, [x.quote for x in a.evidence if x.doc_id == ev.doc_id]) if doc
                    else '<div class="pa-hint">Source document not found in this chart.</div>')
            rows.append(f'<details class="pa-expander"><summary><span class="pa-expander-chevron">'
                        f'{icon("chevron", 14, 2.4)}</span><span class="pa-ev-quote">“{e(ev.quote.strip())}”</span>'
                        f'{tag(ev.doc_id)}<span class="pa-ev-date">{e(ev.doc_date)}</span></summary>'
                        f'<div class="pa-expander-body">{body}</div></details>')
        parts.append(f'<div class="pa-evidence"><span class="pa-eyebrow">Evidence</span>{"".join(rows)}</div>')
    if a.missing_items:
        chips = "".join(f'<span class="pa-chip pa-chip--missing">{e(m)}</span>' for m in a.missing_items)
        parts.append(f'<div class="pa-missing"><span>Missing:</span>{chips}</div>')
    if a.status_before_checks:
        parts.append(f'<div class="pa-note">{icon("code", 16)}<span>Code check changed the model\'s '
                     f'{e(a.status_before_checks.value)} to {e(a.status.value)}.</span></div>')
    if a.deterministic_checks.notes:
        parts.append(f'<p class="pa-hint">Code checks: {e("; ".join(a.deterministic_checks.notes))}</p>')
    return f'<div style="display:flex;flex-direction:column;gap:12px">{"".join(parts)}</div>'


def decision_panel(leaf, key, decisions, reviewer, role, case_dir) -> None:
    block('<span class="pa-eyebrow">Reviewer decision</span>')
    action = st.radio("Decision", ["approve", "edit", "reject"], horizontal=True,
                      key=f"{key}/{leaf.id}/action", index=None, label_visibility="collapsed")
    reason = new_status = note = None
    if action == "edit":
        reason = st.selectbox("Reason (required)", [r.value for r in EditReason], key=f"{key}/{leaf.id}/reason")
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
        block(f'<span class="pa-decision-state is-done">{icon("tick", 14, 2.6)}Decision recorded</span>')
    else:
        block(f'<span class="pa-decision-state">{icon("clock", 14, 2)}No decision yet</span>')


def checklist(res, chart, key, decisions, reviewer, role, case_dir) -> None:
    n_leaves = len(res.assessments)
    section_head("Checklist", f"{n_leaves} criteria · approve = this criterion passes · reject = it does not")
    a_by_id = {a.criterion_id: a for a in res.assessments}

    def leaf_card(leaf, card_key):
        a = a_by_id[leaf.id]
        with st.container(key=card_key.format(STATUS_CLASS[a.status])):
            left, right = st.columns([1, 0.4])
            with left:
                block(criterion_body(leaf, a, chart))
            with right:
                decision_panel(leaf, key, decisions, reviewer, role, case_dir)

    for i, crit in enumerate(res.checklist.criteria):
        if not crit.sub_criteria:
            leaf_card(crit, "crit-{}-" + str(i))
            continue
        rolled = res.rolled_up[crit.id]
        with st.container(key=f"group-{i}"):
            block(f'<div class="pa-card pa-crit-parent is-{STATUS_CLASS[rolled]}"><span class="pa-crit-id">'
                  f'{e(crit.id)}</span><span class="pa-crit-section">Policy {e(crit.policy_ref)}</span>'
                  f'<span class="pa-crit-parent-rule">{e(crit.logic.value)} of the parts below</span>'
                  f'{pill(rolled)}<span class="pa-crit-text">{e(crit.text)}</span></div>')
            with st.container(key=f"children-{i}"):
                for j, leaf in enumerate(crit.sub_criteria):
                    leaf_card(leaf, "leaf-{}-" + f"{i}-{j}")


def todo(res, key) -> None:
    if not res.gaps:
        return
    section_head("To-do list", f"{len(res.gaps)} item(s) to close before this can be submitted")
    for i, g in enumerate(res.gaps):
        with st.container(key=f"todo-{i}"):
            block(f'<div class="pa-todo-head"><h3 class="pa-todo-title"><b>{e(g.criterion_id)}</b> · '
                  f'{e(g.missing_item)}</h3><span class="pa-chip"><span class="pa-chip-key">{icon("user", 14)}</span>'
                  f'<span class="pa-chip-key">Who can supply it</span><span class="pa-chip-val">'
                  f'{e(g.who_can_supply.value.replace("_", " "))}</span></span></div>')
            st.text_area("Drafted message (editable)", g.clinician_query, key=f"{key}/gap/{g.criterion_id}")
            if g.would_satisfy:
                block(f'<div class="pa-todo-accepts">{icon("info")}<span><strong>What the policy accepts:</strong> '
                      f'{e(g.would_satisfy)}</span></div>')


def packet(res) -> None:
    if not res.packet:
        why = ("This run predates packet drafting, so no form or letter is shown."
               if res.outcome == PacketOutcome.READY_FOR_REVIEW else
               "The PA form and letter are drafted only when every criterion is MET. Nothing has been written "
               "for this case yet.")
        block(f'<div class="pa-empty">{icon("info", 16)}<span>{why}</span></div>')
        return
    r = res.request
    bad = {c.claim_ref: c.issue for c in res.verification.checks if not c.supported} if res.verification else {}

    # Draft PA form
    rows = []
    for f in res.packet.form_fields:
        flag = bad.get(f"form:{f.name}")
        cites = "".join(tag(c.doc_id) for c in f.citations)
        reason = f'<div class="pa-form-reason">{icon("warn", 14)}verifier: {e(flag)}</div>' if flag else ""
        rows.append(f'<div class="pa-form-row{" is-flagged" if flag else ""}"><span class="pa-form-label">'
                    f'{e(f.name)}</span><span class="pa-form-value">{e(f.value)}</span>'
                    f'<span class="pa-form-cites">{cites}</span>{reason}</div>')
    section_head("Draft PA form", f"{len(rows)} fields · every value cites its source document")
    block(f'<div class="pa-card pa-form">{"".join(rows)}</div>')

    # Draft letter
    cites, paras, cur = [], [], []
    for i, s in enumerate(res.packet.letter):
        nums = []
        for c in s.citations:
            cites.append(c)
            nums.append(str(len(cites)))
        flag = bad.get(f"letter:{i}")
        sup = f'<sup class="pa-cite">[{", ".join(nums)}]</sup>' if nums else ""
        vt = f'<span class="pa-verifier-tag">verifier: {e(flag)}</span>' if flag else ""
        span = f'<span class="pa-sent{" is-flagged" if flag else ""}">{e(s.text)}{sup}</span>{vt}'
        if s.is_factual:
            if cur and (re.match(r"Policy \d", s.text) or len(cur) >= 4):  # one paragraph per criterion
                paras.append(" ".join(cur))
                cur = []
            cur.append(span)
        else:  # salutation, transitions, closing: their own line
            if cur:
                paras.append(" ".join(cur))
                cur = []
            paras.append(span)
    if cur:
        paras.append(" ".join(cur))
    payer = PAYER_NAMES.get(r.payer, r.payer.title())
    cite_rows = "".join(f'<div class="pa-citation"><span class="pa-citation-n">[{n}]</span>{tag(c.doc_id)}'
                        f'<span class="pa-citation-quote">“{e(c.quote.strip())}”</span></div>'
                        for n, c in enumerate(cites, 1))
    section_head("Draft letter of medical necessity", "Each sentence carries its citations")
    block(f'<article class="pa-card pa-letter"><div class="pa-letter-meta"><div>{e(r.ordering_provider)}<br>'
          f'{e(r.request_date)}</div><div>{e(payer)}<br>Utilization management</div></div>'
          f'<h3 class="pa-letter-subject">Letter of medical necessity: {e(r.product)}</h3>'
          f'<div class="pa-letter-body">{"".join(f"<p>{p}</p>" for p in paras)}</div>'
          f'<details class="pa-expander"><summary><span class="pa-expander-chevron">{icon("chevron", 14, 2.4)}'
          f'</span><strong>Citations</strong><span class="pa-hint">{len(cites)} sources · doc ID and exact quote'
          f'</span></summary><div class="pa-expander-body"><div class="pa-citations">{cite_rows}</div></div>'
          f'</details></article>')

    # Verification
    if res.packet_code_issues:
        block(f'<section class="pa-verify is-notmet">{icon("warn", 20)}<span class="pa-verify-title">'
              f'Code citation check: {e("; ".join(res.packet_code_issues))}</span></section>')
    if res.verification:
        n = len(res.verification.checks)
        ok = res.verification.overall_pass
        title = f"All {n} claims supported" if ok else f"{len(bad)} claim(s) flagged (shown in red above)"
        block(f'<section class="pa-verify is-{"met" if ok else "notmet"}">{icon("check" if ok else "warn", 20)}'
              f'<span class="pa-verify-title">{e(title)}</span><span class="pa-verify-sub">Independent '
              'verification · form and letter checked against source quotes</span></section>')


def signoff(res, key, decisions, reviewer, role, case_dir) -> None:
    section_head("Sign-off", "Nothing is sent to the insurer until a permitted signer signs off")
    need = required_role(res)
    with st.container(key="signoff"):
        left, right = st.columns([3, 2])
        with left:
            options = ["submit", "return_to_staff"] if res.packet else ["reviewed_no_submission", "return_to_staff"]
            decision = st.radio("Action", options, horizontal=True, key=f"{key}/signoff")
        with right:
            who = "physician" if need == "physician" else "nurse or PA specialist"
            block(f'<div style="display:flex;justify-content:flex-end"><span class="pa-chip pa-chip--accent">'
                  f'{icon("user", 14)}Required signer: {who} (D1)</span></div>')
        note = st.text_input("Note", key=f"{key}/signoff_note", placeholder="Optional note for the audit log",
                             help="To override a verifier flag, start the note with 'Override:' and say why.")
        so = SignOff(reviewer=reviewer, reviewer_role=role, decision=decision, note=note or None,
                     timestamp=datetime.now(timezone.utc))
        problems = blockers(res, list(decisions.values()), so)
        if problems:
            items = "".join(f'<li class="pa-blocker">{icon("list" if "decision" in p else "user", 16)}'
                            f'{e(p[0].upper() + p[1:])}</li>' for p in problems)
            block(f'<div class="pa-blockers"><span class="pa-eyebrow">Sign-off is blocked</span>'
                  f'<ul style="display:flex;flex-direction:column;gap:8px">{items}</ul></div>')
        clicked = st.button("Sign off", type="primary", disabled=bool(problems), icon=":material/send:")
        if not clicked:
            return
        save_review(case_dir, [], so)
        audit_append(case_dir, "10_signoff", so.model_dump(mode="json"))
        if decision != "submit":
            block(f'<div class="pa-success"><div class="pa-success-icon">{icon("tick", 22, 2.6)}</div><div>'
                  f'<div class="pa-success-title">Recorded: {e(decision)}</div><div>Signed by {e(reviewer)} '
                  f'({e(role)}). Nothing was sent.</div></div></div>')
            return
        try:
            sub = mock_submit(res, list(decisions.values()), so, case_dir)
        except SignOffBlocked as err:
            st.error(str(err))
            return
        audit_append(case_dir, "11_mock_submission", {"dir": str(sub.relative_to(ROOT))})
        files = sorted(p.name for p in sub.iterdir())
        benefits = ", ".join(sorted({ch.value for ch in res.routing.channels.values()}))
        tags = "".join(f'<span class="pa-tag">{e(f)}</span>' for f in files)
        block(f'<div class="pa-success"><div class="pa-success-icon">{icon("tick", 22, 2.6)}</div><div>'
              f'<div class="pa-success-title">Mock submission written ({e(benefits)})</div>'
              f'<div>Signed by {e(reviewer)} ({e(role)}). Written to <span class="pa-mono">'
              f'{e(sub.relative_to(ROOT))}</span>. Nothing was sent to a real insurer.</div>'
              f'<div class="pa-success-files">{tags}</div></div></div>')
        st.toast("Signed off. Mock submission written.", icon=":material/check_circle:")


def main() -> None:
    st.set_page_config(page_title="Prior Auth Agent · Reviewer console", page_icon=":material/shield:",
                       layout="wide")
    css = "\n".join(line for line in CSS.splitlines() if line.strip())  # no blank lines inside markdown HTML
    st.markdown(f"<style>@import url('{FONTS}');\n{css}</style>", unsafe_allow_html=True)
    runs = list_results()
    if not runs:
        st.error("No runs yet. Run `python -m agent.pipeline PA-0001` first.")
        return
    run, case, reviewer, role = sidebar(runs)
    res, chart = load(run, case)
    case_dir = RUNS / run / case
    key = f"{run}/{case}"
    decisions: dict[str, ReviewDecision] = st.session_state.setdefault(key, {})

    hero(res)
    summary(res, key)
    injection_alert(res, chart)
    for n in res.routing.notes:
        if len(set(res.routing.channels.values())) < 2:  # two-rail note is already shown in the header
            block(f'<div class="pa-todo-accepts">{icon("info")}<span>{e(n)}</span></div>')
    checklist(res, chart, key, decisions, reviewer, role, case_dir)
    todo(res, key)
    packet(res)
    signoff(res, key, decisions, reviewer, role, case_dir)
    block(f'<div class="pa-disclaimer pa-disclaimer--footer">{icon("info")}<span>{DISCLAIMER}</span></div>')


main()
