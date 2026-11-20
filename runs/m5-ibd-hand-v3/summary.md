# Run m5-ibd-hand-v3

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 3 ok, 0 errored
- Packet outcome matches gold: 3/3 exact; 0 more differ only via an acceptable alternate status; 0 wrong
- Criteria correct (gold or acceptable alternate): 33/33
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 0/0
- Model time 284 s; list-price cost $1.44

Step 3 extraction for northfield-ustekinumab-ibd: 11/11 gold criteria found.

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-0001](PA-0001/report.md) | clean | READY_FOR_REVIEW | READY_FOR_REVIEW | 11/11 | 0 | 0 | 131.6 | 0.696 |
| [PA-0002](PA-0002/report.md) | missing_item | GAPS_TO_CLOSE | GAPS_TO_CLOSE | 11/11 | 0 | 0 | 73.5 | 0.367 |
| [PA-0003](PA-0003/report.md) | conflicting | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 11/11 | 0 | 0 | 78.4 | 0.375 |
