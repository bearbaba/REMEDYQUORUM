# REMEDYQUORUM — current GenLayer Studio runbook

**One active system, no release-series naming and no redeploy of historical errors.**

| Module | Studionet |
|---|---|
| AppealCore | `0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2` |
| RemedyVerify | `0x8c65c73187bBf575201d31a1270812e1D4BeD830` |

Current verifier source: [`contracts/remedy_verify.py`](../contracts/remedy_verify.py). This is the unchanged source text from the latest deployment screenshot, copied to the canonical filename. The internal class/metadata identifiers reflect the deployed code; they are not additional supported product versions.

## Preflight — read-only (no gas-consuming write)

1. Open the [active RemedyVerify Studio contract](https://studio.genlayer.com/?import-contract=0x8c65c73187bBf575201d31a1270812e1D4BeD830). Confirm the panel displays that exact **Deployed at** address, not a previously deployed instance.
2. Call `get_core()`. It must equal the AppealCore address in the table above (case-insensitive).
3. Call `stats()`. Confirm `appeal_core` matches, `evidence_mode=PINNED_PUBLIC_WEB_CONTENT_SHA256` and note the number of existing `remediations`; do not guess the next remediation ID.
4. Preserve the full deployment TX hash if obtainable, and compare the deployed Python code/source identity with this repository before attributing it to the contract.

## Write sequence — only after readback succeeds

1. Use original **Respondent** wallet `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, Normal (Full Consensus), Simulation Mode off.
2. Open `submit_remediation` and copy **exactly** four input fields from [`examples/positive_remediation/studio_inputs.json`](../examples/positive_remediation/studio_inputs.json). Pass `case_id=2` and the exact strings `action_summary`, `evidence_json` and `evidence_sha256`.
3. Record the actual FINALIZED / Accepted / GenVM SUCCESS transaction and returned remediation ID. If this call fails, do not infer an ID.
4. Before the one-shot AI write, call `get_remediation(actual_id)` and confirm both real HTTPS artifact URLs, hashes, roles, frozen `UPHELD` ruling and `status=SUBMITTED`.
5. Invoke `assess_remediation(actual_id)` **once**. This performs public web retrieval of the two immutable files and semantic validation. Inspect actual Return Value and Equivalence Principle outputs. If `INSUFFICIENT`, `FAILED`, `REVIEW`, or a rejected/failed transaction, stop and diagnose — **do not run it again** for an already assessed remediation.
6. **Only for an actually accepted `VERIFIED` verdict with all PASS criteria**, switch to original **Claimant** wallet `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb`, manually review the published report and archive, and call `respond_to_remediation(actual_id, true, reason)` with an accurate statement of what the claimant checked.
7. Read `get_remediation(actual_id)` again and require `verdict=VERIFIED` with `claimant_response=ACCEPTED` before describing the positive demonstration as complete.

## Limits

The underlying project agreement is fictional. A content-addressed file and public URL do not independently prove legal performance or receipt by any real person. The Claimant's signature is a separate consent action, not a substitute for verifying off-chain facts. Historical failed trials are in [the audit ledger](DEPLOYMENT_EVIDENCE.md), not in the active deployment instructions.
