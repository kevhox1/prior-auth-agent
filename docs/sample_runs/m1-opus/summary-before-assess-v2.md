# Run m1-opus-v2

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 15 ok, 0 errored
- Packet outcome matches gold: 12/15 exact; 2 more differ only via an acceptable alternate status; 1 wrong
- Criteria correct (gold or acceptable alternate): 163/165
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 1/1
- Model time 740 s; list-price cost $2.93

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-0001](PA-0001/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-0002](PA-0002/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-0003](PA-0003/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-1005](PA-1005/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-1029](PA-1029/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN (alt) | 11/11 | 0 | 0 | 74.7 | 0.276 |
| [PA-1038](PA-1038/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 73.0 | 0.280 |
| [PA-1042](PA-1042/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN ✗ | 9/11 | 0 | 0 | 112.9 | 0.446 |
| [PA-1065](PA-1065/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 53.0 | 0.236 |
| [PA-1082](PA-1082/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 83.6 | 0.294 |
| [PA-1103](PA-1103/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 71.1 | 0.285 |
| [PA-1106](PA-1106/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN (alt) | 11/11 | 0 | 0 | 0 | 0.000 |
| [PA-1121](PA-1121/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 103.5 | 0.373 |
| [PA-1158](PA-1158/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 48.7 | 0.241 |
| [PA-1169](PA-1169/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 64.5 | 0.262 |
| [PA-1197](PA-1197/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 54.9 | 0.242 |
