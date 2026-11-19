"""Step 4: evidence retrieval. Model reads every document, returns candidate passages.

One call per case covers all criteria (batched to keep call count low on a
subscription; per-criterion calls are a config change if isolation matters
more than cost). Code then drops any passage whose quote is not verbatim in its
document, so step 5 only ever sees real text.
"""

from __future__ import annotations

from agent.checks import quote_in_text
from agent.llm import CallRecord, LLMConfig, structured_call
from agent.prompts import load_prompt
from agent.render import chart_block, criteria_block, request_block
from agent.schemas import CaseRetrievalDraft, Chart, InjectionFlag, PARequest, PolicyChecklist, RetrievalResult

PROMPT = "retrieve@v1"


def retrieve(req: PARequest, chart: Chart, checklist: PolicyChecklist, cfg: LLMConfig | None = None
             ) -> tuple[list[RetrievalResult], list[InjectionFlag], CallRecord, list[str]]:
    p = load_prompt(PROMPT)
    user = "\n\n".join([request_block(req), criteria_block(checklist), chart_block(chart)])
    draft, rec = structured_call(step="retrieve", prompt_id=p.ref, system=p.text, user=user,
                                 schema=CaseRetrievalDraft, cfg=cfg)
    notes: list[str] = []
    all_docs = [d.doc_id for d in chart.documents]
    by_id = {r.criterion_id: r for r in draft.criteria}
    results = []
    for leaf in checklist.leaves():
        r = by_id.get(leaf.id)
        if r is None:
            notes.append(f"retrieval returned nothing for {leaf.id}")
            results.append(RetrievalResult(criterion_id=leaf.id, passages=[], docs_searched=all_docs))
            continue
        kept = []
        for ps in r.passages:
            doc = chart.get(ps.doc_id)
            if doc is None or not quote_in_text(ps.quote, doc.text):
                notes.append(f"{leaf.id}: dropped non-verbatim passage from {ps.doc_id}: {ps.quote[:60]!r}")
                continue
            kept.append(ps.model_copy(update={"doc_date": doc.date}))
        results.append(RetrievalResult(criterion_id=leaf.id, passages=kept, docs_searched=all_docs,
                                       injection_flags=r.injection_flags))
    flags = list(draft.injection_flags) + [f for r in draft.criteria for f in r.injection_flags]
    return results, flags, rec, notes
