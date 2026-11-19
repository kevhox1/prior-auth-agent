# Run m2-blind-opus

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 30 ok, 0 errored
- Packet outcome matches gold: 25/30 exact; 4 more differ only via an acceptable alternate status; 1 wrong
- Criteria correct (gold or acceptable alternate): 314/315
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 0/0
- Model time 1942 s; list-price cost $8.54

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

Step 3 extraction for calder-ustekinumab-ibd: 10/10 gold criteria found.
- b.9: lookback 3 vs gold None

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-3004](PA-3004/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 52.8 | 0.255 |
| [PA-3006](PA-3006/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 65.1 | 0.293 |
| [PA-3007](PA-3007/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 56.9 | 0.262 |
| [PA-3018](PA-3018/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 69.9 | 0.305 |
| [PA-3034](PA-3034/report.md) | not_met | NEEDS_PHYSICIAN | GAPS_TO_CLOSE (alt) | 11/11 | 0 | 0 | 80.7 | 0.380 |
| [PA-3040](PA-3040/report.md) | multi_issue | NEEDS_PHYSICIAN | GAPS_TO_CLOSE (alt) | 11/11 | 0 | 0 | 62.2 | 0.285 |
| [PA-3041](PA-3041/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 47.4 | 0.229 |
| [PA-3045](PA-3045/report.md) | not_met | NEEDS_PHYSICIAN | GAPS_TO_CLOSE (alt) | 11/11 | 0 | 0 | 61.0 | 0.277 |
| [PA-3050](PA-3050/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 45.3 | 0.233 |
| [PA-3080](PA-3080/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 135.2 | 0.561 |
| [PA-3090](PA-3090/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 54.6 | 0.261 |
| [PA-3091](PA-3091/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN ✗ | 10/11 | 0 | 0 | 66.4 | 0.291 |
| [PA-3092](PA-3092/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 98.3 | 0.437 |
| [PA-3093](PA-3093/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 62.3 | 0.287 |
| [PA-3096](PA-3096/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 65.5 | 0.296 |
| [PA-3504](PA-3504/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 46.9 | 0.216 |
| [PA-3506](PA-3506/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 65.6 | 0.274 |
| [PA-3507](PA-3507/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN (alt) | 10/10 | 0 | 0 | 49.9 | 0.226 |
| [PA-3518](PA-3518/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 82.2 | 0.332 |
| [PA-3534](PA-3534/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 51.1 | 0.224 |
| [PA-3540](PA-3540/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 62.9 | 0.263 |
| [PA-3541](PA-3541/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 53.0 | 0.226 |
| [PA-3545](PA-3545/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 59.6 | 0.251 |
| [PA-3550](PA-3550/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 43.9 | 0.208 |
| [PA-3580](PA-3580/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 105.5 | 0.427 |
| [PA-3590](PA-3590/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 49.5 | 0.229 |
| [PA-3591](PA-3591/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 61.1 | 0.250 |
| [PA-3592](PA-3592/report.md) | multi_issue | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 57.6 | 0.235 |
| [PA-3593](PA-3593/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/10 | 0 | 0 | 65.9 | 0.266 |
| [PA-3596](PA-3596/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 63.4 | 0.260 |
