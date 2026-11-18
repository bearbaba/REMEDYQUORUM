# RemedyVerify V2 — evidence-verified positive-path runbook

## Goal and status

- **Goal:** demonstrate a real GenLayer Studionet flow ending in `VERIFIED` and a separate original-Claimant-signed `ACCEPTED`, not merely `UPHELD / INSUFFICIENT / DISPUTED`.
- **Current status:** SOURCE AND OFFLINE TESTS ONLY. This V2 contract has **not yet been deployed** and no V2 on-chain success is claimed.
- **Single system:** V2 replaces the RemedyVerify module **within REMEDYQUORUM**. AppealCore at `0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2` and the accepted synthetic Case #2 `UPHELD` ruling remain unchanged. V1 state, including Remediation #1 DISPUTED, is preserved as historical evidence.

## Why V1 could not substantiate completion

V1 reads only `description` and `sha256` supplied by the Respondent. Those hashes bind claimed bytes but the AI never receives the bytes. A conservative AI rightfully returned `INSUFFICIENT / REVIEW` when external delivery facts and source evidence could not be verified. Merely changing prompt wording or pretending a receipt exists is not a solution.

## What V2 actually checks

1. Two mandatory evidence roles: `corrected_report` and `indexed_archive`, with content-addressed SHA-256 and **immutable commit-pinned raw GitHub URLs**. The two artifacts must share the same 40-character commit pin.
2. In a GenLayer nondeterministic block, leader fetches the actual published report and archive with `gl.nondet.web.get`, verifies HTTP 200, bounds bytes, and checks each complete file's SHA-256 against frozen submitted evidence.
3. Deterministic consistency checks require the archive's Case #2 ID, exact frozen ruling digest, a source index, source IDs appearing in the report, and zero additional USDC/GEN access charge.
4. Only after those checks, AI assesses the actual fetched document text against the required remedy. A decisive all-PASS outcome requires an independent validator to refetch both files and independently obtain all PASS labels.
5. `VERIFIED` establishes successful review of accessible **synthetic digital deliverables**, not real-world legal liability or third-party delivery. The original Claimant must still sign `respond_to_remediation(id,true,reason)` after reviewing the report and archive. Without that step there is no `ACCEPTED`.
6. Any bad URL/hash, HTTP failure, malformed archive, ambiguous requirement, or missing documentation must result in REVIEW / INSUFFICIENT (or an unsuccessful transaction), never a claimed successful correction.

## Immutable public evidence fixtures

- [Corrected report](../examples/positive_remediation/corrected_report.md): full SHA-256 `34b5c2767143b3a69dd9db4b0460d4489cc24ca13db9bedbb62862bc5350b741`.
- [Indexed source archive](../examples/positive_remediation/indexed_source_archive.json): full SHA-256 `da1960d26982394dbf08d8ac70ac3b3be1907e0cc9ac0791d8e8a8f9ef0cbca6`.
- Both artifacts are pinned to merged GitHub commit `675c2cc5c21bf0ec870155ce2e614bac6907914e`; the URL fields in [Studio V2 inputs](../examples/positive_remediation/studio_inputs_v2.json) use this immutable commit.
- Canonical JSON evidence-bundle SHA-256: `01846f7c006bfe89489d9e7e3625b81c83b5b6dd5a88d6af97b7e1e4ed3ffc87`.

## Studio sequence — do not skip source checks

1. First inspect [the V2 source](../contracts/remedy_verify_v2.py) and confirm GitHub Python CI PASSES. Do not import or redeploy the original V1 file.
2. Deploy **RemedyVerifyV2** as a new contract on GenLayer Studionet, with constructor `appeal_core_address` equal to the unchanged AppealCore address above. Record the new contract address and true FINALIZED / Accepted / GenVM SUCCESS receipt.
3. Use the V2 `get_core()` view to confirm the exact stored AppealCore address. New V2 `get_remediation` state starts empty and its first accepted ID will normally be 1; never assume until the real return value is seen.
4. From original Respondent wallet `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, call V2 `submit_remediation` with the four arguments `case_id`, `action_summary`, `evidence_json`, `evidence_sha256` copied *exactly* from `studio_inputs_v2.json`.
5. Read back `get_remediation(new_id)` to confirm stored evidence commitments; use Normal / Full Consensus for `assess_remediation(new_id)` **once**, recording the Return Value and EP labels.
6. **Only if** accepted consensus actually returns `VERIFIED` with all PASS criteria, switch to original Claimant wallet `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb`, inspect the public files, then call `respond_to_remediation(new_id,true,reason)`. Record actual `ACCEPTED` return and final `get_remediation(new_id)` view.
7. If the actual outcome is `INSUFFICIENT`, `FAILED`, `UNDETERMINED` or execution ERROR, stop and inspect logs. Do not claim success, mark Claimant acceptance, or repeat a one-shot assessment. Investigate web access and evidence rather than modifying an already-frozen decision.

**Note:** V2 is new source requiring a separate deployment by the authorized wallet. No wallet deployment/signature is initiated by preparing these files. The previous negative V1 path is already completed on-chain and remains valid.
