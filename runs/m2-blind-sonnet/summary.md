# Run m2-blind-sonnet

> **Note (added later):** this is the summary written when the run finished. The 3 false METs below were a scorer error, not agent errors: the scorer compared a merged parent criterion with a failed branch (B39). Re-scored: 0 false METs. See [`docs/MODEL_COMPARISON.md`](../../docs/MODEL_COMPARISON.md).

Model `claude-sonnet-5-5`, backend `claude_code`, effort `default`.

- Cases: 30 ok, 0 errored
- Packet outcome matches gold: 23/30 exact; 1 more differ only via an acceptable alternate status; 6 wrong
- Criteria correct (gold or acceptable alternate): 276/315
- **False MET: 3** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 0/0
- Model time 1077 s; list-price cost $3.43

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

Step 3 extraction for calder-ustekinumab-ibd: 8/10 gold criteria found.
- missing criterion for policy b.5(a)
- missing criterion for policy b.5(b)
- b.5: logic None vs gold ANY
- b.9: lookback 3 vs gold None

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-3004](PA-3004/report.md) | borderline | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 10/11 | 0 | 0 | 37.3 | 0.126 |
| [PA-3006](PA-3006/report.md) | conflicting | NEEDS_PHYSICIAN | GAPS_TO_CLOSE ✗ | 0/11 | 0 | 0 | 31.9 | 0.129 |
| [PA-3007](PA-3007/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/11 | 0 | 0 | 38.7 | 0.121 |
| [PA-3018](PA-3018/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/11 | 0 | 0 | 44.0 | 0.135 |
| [PA-3034](PA-3034/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/11 | 0 | 0 | 34.8 | 0.114 |
| [PA-3040](PA-3040/report.md) | multi_issue | NEEDS_PHYSICIAN | GAPS_TO_CLOSE (alt) | 11/11 | 0 | 0 | 40.1 | 0.130 |
| [PA-3041](PA-3041/report.md) | borderline | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 10/11 | 0 | 0 | 34.5 | 0.113 |
| [PA-3045](PA-3045/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/11 | 0 | 0 | 40.3 | 0.127 |
| [PA-3050](PA-3050/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 34.4 | 0.116 |
| [PA-3080](PA-3080/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 54.9 | 0.184 |
| [PA-3090](PA-3090/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 35.0 | 0.120 |
| [PA-3091](PA-3091/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/11 | 0 | 0 | 35.7 | 0.116 |
| [PA-3092](PA-3092/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/11 | 0 | 0 | 36.0 | 0.114 |
| [PA-3093](PA-3093/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/11 | 0 | 0 | 39.8 | 0.132 |
| [PA-3096](PA-3096/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/11 | 0 | 0 | 40.2 | 0.129 |
| [PA-3504](PA-3504/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 28.4 | 0.091 |
| [PA-3506](PA-3506/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 8/10 | 1 | 0 | 34.9 | 0.105 |
| [PA-3507](PA-3507/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN ✗ | 9/10 | 0 | 0 | 33.3 | 0.100 |
| [PA-3518](PA-3518/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 8/10 | 0 | 0 | 33.6 | 0.102 |
| [PA-3534](PA-3534/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 31.9 | 0.098 |
| [PA-3540](PA-3540/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 38.0 | 0.112 |
| [PA-3541](PA-3541/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 34.0 | 0.101 |
| [PA-3545](PA-3545/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 34.4 | 0.102 |
| [PA-3550](PA-3550/report.md) | clean | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 9/10 | 0 | 0 | 29.6 | 0.095 |
| [PA-3580](PA-3580/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 8/10 | 1 | 0 | 33.1 | 0.100 |
| [PA-3590](PA-3590/report.md) | buried_evidence | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 9/10 | 0 | 0 | 33.9 | 0.106 |
| [PA-3591](PA-3591/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/10 | 0 | 0 | 31.9 | 0.099 |
| [PA-3592](PA-3592/report.md) | multi_issue | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/10 | 0 | 0 | 33.5 | 0.100 |
| [PA-3593](PA-3593/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/10 | 0 | 0 | 34.4 | 0.109 |
| [PA-3596](PA-3596/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 8/10 | 1 | 0 | 34.8 | 0.105 |
