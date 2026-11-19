# Run m1-opus-assess-v2

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 15 ok, 0 errored
- Packet outcome matches gold: 15/15 exact; 0 more differ only via an acceptable alternate status; 0 wrong
- Criteria correct (gold or acceptable alternate): 165/165
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 1/1
- Model time 492 s; list-price cost $2.39

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-0001](PA-0001/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 28.8 | 0.173 |
| [PA-0002](PA-0002/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 35.1 | 0.183 |
| [PA-0003](PA-0003/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 35.4 | 0.182 |
| [PA-1005](PA-1005/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 34.7 | 0.158 |
| [PA-1029](PA-1029/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 51.6 | 0.222 |
| [PA-1038](PA-1038/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 28.8 | 0.151 |
| [PA-1042](PA-1042/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 28.6 | 0.145 |
| [PA-1065](PA-1065/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 24.7 | 0.124 |
| [PA-1082](PA-1082/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 34.1 | 0.161 |
| [PA-1103](PA-1103/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 37.4 | 0.164 |
| [PA-1106](PA-1106/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 32.1 | 0.149 |
| [PA-1121](PA-1121/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 40.8 | 0.173 |
| [PA-1158](PA-1158/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 25.0 | 0.130 |
| [PA-1169](PA-1169/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 30.8 | 0.146 |
| [PA-1197](PA-1197/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 24.2 | 0.128 |
