# Verifier report (step 9 seeded errors)

Run `m3-opus-packets`, verifier model `claude-opus-5-5`. Each seeded error changes one claim in a real drafted packet. Its citation stays valid and verbatim, so the step 8 code check cannot catch it; only the independent verifier can.

**Caught 10 of 10 seeded errors** (the exact claim flagged). Packets blocked from sign-off: 10 of 10.

| Case | Error | Claim | Seeded text | Caught | Verifier's reason | Other claims flagged |
|---|---|---|---|---|---|---|
| PA-0001 | changed number | letter:2 | The requested regimen is 427 mg IV once (weight 78 kg), then 90 mg SC every 8 weeks starting 8 weeks after the | yes | The letter gives the IV induction dose as 427 mg, but the request and the 10/28/2026 GI note both say 390 mg IV once. | - |
| PA-0001 | shifted date | letter:3 | The requested start date is 2024-12-01. | yes | The letter gives the start date as 2024-12-01, but the request and the cited quote say 2026-12-01. | - |
| PA-0001 | flipped result | letter:21 | Policy 3.6: The QuantiFERON-TB Gold Plus test on 09/22/2026 was positive. | yes | The letter says the 09/22/2026 QuantiFERON-TB Gold Plus was positive, but the cited lab result and the 10/28/2026 GI note both say NEGATIVE. | - |
| PA-0001 | wrong drug | letter:15 | Methotrexate 150 mg daily (2.0 mg/kg) was used from 2023-01 to 2024-02, with inadequate response after 12 mont | yes | The letter names methotrexate, but the cited medication history row, the 02/06/2024 GI note and the 10/28/2026 note all say azathioprine 150 | - |
| PA-0001 | unsupported claim | letter:2 | The member also completed a 6-month trial of vedolizumab, stopped for loss of response. | yes | The letter says the member completed a 6-month vedolizumab trial stopped for loss of response, but vedolizumab appears nowhere in the chart  | - |
| PA-3004 | changed number | letter:3 | The requested regimen is 297 mg IV once (weight 55.0 kg), then 90 mg SC every 8 weeks starting 8 weeks after t | yes | The letter gives the IV induction dose as 297 mg, but the request and the 2026-10-31 GI note both say 260 mg IV once. | - |
| PA-3004 | shifted date | letter:2 | Her member ID is NHP-672-659-23 and her date of birth is 1998-04-27. | yes | The letter gives the date of birth as 1998-04-27, but the cited demographics quote and the outside records both say 2000-04-27. | - |
| PA-3004 | flipped result | letter:15 | Policy 3.6: Her QuantiFERON-TB Gold Plus on 2026-09-20 was positive. | yes | Letter says the QuantiFERON-TB Gold Plus was positive, but the cited 2026-09-20 lab result is NEGATIVE. | - |
| PA-3004 | wrong drug | letter:14 | Policy 3.5(b): She received adalimumab 5 mg/kg IV every 8 weeks from 2024-03 to 2026-09, which was stopped for | yes | The letter says adalimumab, but the cited quote and the medication history say infliximab 5 mg/kg IV every 8 weeks. | - |
| PA-3004 | unsupported claim | letter:2 | The member also completed a 6-month trial of vedolizumab, stopped for loss of response. | yes | The letter says she had a 6-month vedolizumab trial stopped for loss of response, but vedolizumab appears nowhere in the chart (the medicati | - |

Flags the verifier raised on the unmodified packets (false-alarm baseline): PA-0001: none; PA-3004: none.
