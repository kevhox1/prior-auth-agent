# Run m5-blind-regress-v3

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 6 ok, 0 errored
- Packet outcome matches gold: 5/6 exact; 1 more differ only via an acceptable alternate status; 0 wrong
- Criteria correct (gold or acceptable alternate): 63/63
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 0/0
- Model time 218 s; list-price cost $1.00

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

Step 3 extraction for calder-ustekinumab-ibd: 10/10 gold criteria found.
- b.9: lookback 3 vs gold None

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-3006](PA-3006/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 33.9 | 0.159 |
| [PA-3018](PA-3018/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 57.3 | 0.247 |
| [PA-3045](PA-3045/report.md) | not_met | NEEDS_PHYSICIAN | GAPS_TO_CLOSE (alt) | 11/11 | 0 | 0 | 31.2 | 0.153 |
| [PA-3506](PA-3506/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 35.2 | 0.152 |
| [PA-3518](PA-3518/report.md) | multi_issue | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 34.0 | 0.152 |
| [PA-3545](PA-3545/report.md) | not_met | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 10/10 | 0 | 0 | 26.8 | 0.135 |
