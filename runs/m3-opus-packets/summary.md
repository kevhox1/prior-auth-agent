# Run m3-opus-packets

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 4 ok, 0 errored
- Packet outcome matches gold: 4/4 exact; 0 more differ only via an acceptable alternate status; 0 wrong
- Criteria correct (gold or acceptable alternate): 42/42
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 0/0
- Model time 267 s; list-price cost $1.17

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

Step 3 extraction for calder-ustekinumab-ibd: 10/10 gold criteria found.
- b.9: lookback 3 vs gold None

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-0001](PA-0001/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 87.2 | 0.383 |
| [PA-3004](PA-3004/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 62.3 | 0.272 |
| [PA-3504](PA-3504/report.md) | borderline | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 51.7 | 0.235 |
| [PA-3590](PA-3590/report.md) | buried_evidence | READY_FOR_REVIEW | READY_FOR_REVIEW | 10/10 | 0 | 0 | 65.8 | 0.275 |
