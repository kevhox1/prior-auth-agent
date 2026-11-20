# Run m2-opus-heldout-v2

> **Note (added later):** this is the summary written when the run finished. Two gold-label fixes made after this run (B32, B34) turn one outcome from alternate to exact: 29/30 exact. See [`docs/EVAL_REPORT.md`](../../docs/EVAL_REPORT.md).

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 30 ok, 0 errored
- Packet outcome matches gold: 28/30 exact; 2 more differ only via an acceptable alternate status; 0 wrong
- Criteria correct (gold or acceptable alternate): 315/315
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 2/2
- Model time 554 s; list-price cost $2.64

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

Step 3 extraction for calder-ustekinumab-ibd: 10/10 gold criteria found.
- b.9: lookback 3 vs gold None

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-2003](PA-2003/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2010](PA-2010/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2029](PA-2029/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2048](PA-2048/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2050](PA-2050/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2052](PA-2052/report.md) | multi_issue | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2054](PA-2054/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 54.4 | 0.260 |
| [PA-2055](PA-2055/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 54.9 | 0.275 |
| [PA-2059](PA-2059/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2063](PA-2063/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 59.0 | 0.283 |
| [PA-2070](PA-2070/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 49.9 | 0.265 |
| [PA-2073](PA-2073/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2082](PA-2082/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2083](PA-2083/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-2088](PA-2088/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 66.1 | 0.303 |
| [PA-2503](PA-2503/report.md) | multi_issue | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2510](PA-2510/report.md) | conflicting | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2529](PA-2529/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2548](PA-2548/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2550](PA-2550/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2552](PA-2552/report.md) | multi_issue | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2554](PA-2554/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 49.9 | 0.231 |
| [PA-2555](PA-2555/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 61.6 | 0.281 |
| [PA-2559](PA-2559/report.md) | multi_issue | GAPS_TO_CLOSE | NEEDS_PHYSICIAN (alt) | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2563](PA-2563/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN (alt) | 10/10 | 0 | 0 | 54.5 | 0.248 |
| [PA-2570](PA-2570/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 48.4 | 0.237 |
| [PA-2573](PA-2573/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2582](PA-2582/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2583](PA-2583/report.md) | multi_issue | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 0 | 0.000 |
| [PA-2588](PA-2588/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 55.6 | 0.256 |
