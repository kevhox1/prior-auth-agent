# Run m5-reuse-opus-v3

Model `claude-opus-5-5`, backend `claude_code`, effort `default`.

- Cases: 3 ok, 0 errored
- Packet outcome matches gold: 2/3 exact; 1 more differ only via an acceptable alternate status; 0 wrong
- Criteria correct (gold or acceptable alternate): 27/27
- **False MET: 0** (release gate: 0)
- MET claims downgraded by step 6 code checks: 0
- Injection cases flagged: 0/0
- Model time 21 s; list-price cost $0.07

Step 3 extraction for calder-evolocumab-lipids: 9/9 gold criteria found.
- benefit channels {'self_administered_sc': 'pharmacy'} vs gold {'sc_injection': 'pharmacy'}

| Case | Type | Gold outcome | Agent outcome | Criteria ok | False MET | Downgrades | s | $ |
|---|---|---|---|---|---|---|---|---|
| [PA-0101](PA-0101/report.md) | reuse | READY_FOR_REVIEW | READY_FOR_REVIEW | 9/9 | 0 | 0 | 0 | 0.000 |
| [PA-0102](PA-0102/report.md) | reuse | GAPS_TO_CLOSE | NEEDS_PHYSICIAN (alt) | 9/9 | 0 | 0 | 20.7 | 0.067 |
| [PA-0103](PA-0103/report.md) | reuse | NEEDS_PHYSICIAN | NEEDS_PHYSICIAN | 9/9 | 0 | 0 | 0 | 0.000 |
