# Run m2-blind-haiku

Model `claude-haiku-5-5`, backend `claude_code`, effort `default`.

- Cases: 30 ok, 0 errored
- Packet outcome matches gold: 20/30 exact; 0 more differ only via an acceptable alternate status; 10 wrong
- Criteria correct (gold or acceptable alternate): 274/315
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 0/0
- Model time 1933 s; list-price cost $0.34

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.
- extra criterion for policy 3.10(a)
- extra criterion for policy 3.10(b)
- 3.10: logic ANY vs gold None

Step 3 extraction for calder-ustekinumab-ibd: 10/10 gold criteria found.
- b.9: lookback 3 vs gold None

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-3004](PA-3004/report.md) | borderline | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 8/11 | 0 | 0 | 83.3 | 0.015 |
| [PA-3006](PA-3006/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/11 | 0 | 0 | 72.9 | 0.014 |
| [PA-3007](PA-3007/report.md) | missing_item | GAPS_TO_CLOSE | NEEDS_PHYSICIAN ✗ | 10/11 | 0 | 0 | 64.0 | 0.011 |
| [PA-3018](PA-3018/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/11 | 0 | 0 | 63.5 | 0.012 |
| [PA-3034](PA-3034/report.md) | not_met | NEEDS_PHYSICIAN | GAPS_TO_CLOSE ✗ | 8/11 | 0 | 0 | 74.7 | 0.013 |
| [PA-3040](PA-3040/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/11 | 0 | 0 | 69.8 | 0.013 |
| [PA-3041](PA-3041/report.md) | borderline | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 10/11 | 0 | 0 | 62.0 | 0.011 |
| [PA-3045](PA-3045/report.md) | not_met | NEEDS_PHYSICIAN | GAPS_TO_CLOSE ✗ | 9/11 | 0 | 0 | 84.7 | 0.014 |
| [PA-3050](PA-3050/report.md) | clean | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 10/11 | 0 | 0 | 56.1 | 0.011 |
| [PA-3080](PA-3080/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 8/11 | 0 | 0 | 90.7 | 0.015 |
| [PA-3090](PA-3090/report.md) | buried_evidence | READY_FOR_REVIEW | NEEDS_PHYSICIAN ✗ | 8/11 | 0 | 0 | 63.6 | 0.012 |
| [PA-3091](PA-3091/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/11 | 0 | 0 | 70.3 | 0.012 |
| [PA-3092](PA-3092/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/11 | 0 | 0 | 79.8 | 0.013 |
| [PA-3093](PA-3093/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 10/11 | 0 | 0 | 84.9 | 0.015 |
| [PA-3096](PA-3096/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/11 | 0 | 0 | 69.0 | 0.013 |
| [PA-3504](PA-3504/report.md) | borderline | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 9/10 | 0 | 0 | 40.3 | 0.008 |
| [PA-3506](PA-3506/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 56.3 | 0.010 |
| [PA-3507](PA-3507/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/10 | 0 | 0 | 49.3 | 0.009 |
| [PA-3518](PA-3518/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 81.4 | 0.014 |
| [PA-3534](PA-3534/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 47.0 | 0.008 |
| [PA-3540](PA-3540/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 68.8 | 0.012 |
| [PA-3541](PA-3541/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 45.1 | 0.008 |
| [PA-3545](PA-3545/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 72.2 | 0.013 |
| [PA-3550](PA-3550/report.md) | clean | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 9/10 | 0 | 0 | 40.0 | 0.008 |
| [PA-3580](PA-3580/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 50.9 | 0.009 |
| [PA-3590](PA-3590/report.md) | buried_evidence | READY_FOR_REVIEW | GAPS_TO_CLOSE ✗ | 9/10 | 0 | 0 | 61.8 | 0.012 |
| [PA-3591](PA-3591/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/10 | 0 | 0 | 52.6 | 0.009 |
| [PA-3592](PA-3592/report.md) | multi_issue | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/10 | 0 | 0 | 51.1 | 0.009 |
| [PA-3593](PA-3593/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 9/10 | 0 | 0 | 70.6 | 0.012 |
| [PA-3596](PA-3596/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/10 | 0 | 0 | 56.0 | 0.010 |
