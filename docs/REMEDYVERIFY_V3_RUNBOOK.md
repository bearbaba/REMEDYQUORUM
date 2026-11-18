# REMEDYQUORUM — RemedyVerify V3 (SDK web status fix)

## Current verified facts and goal

- Case #2 has an authentic AppealCore UPHELD ruling. AppealCore address: `0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2`.
- V1 RemedyVerify accepted the synthetic submission but conservatively assessed `INSUFFICIENT`; original Claimant then signed `DISPUTED`. Historical V1 records remain unchanged.
- V2 RemedyVerify address `0x5C6d327F57f8A49E9c64872c64d8C5D04Aca9C48` accepted new Remediation ID 1, then a [FINALIZED accepted assessment](https://explorer-studio.genlayer.com/tx/0x9fb07f5120fb11dbe233f337194c5558c568cbe70fc8f8a9d1cfde8a63e41bf8) returned `INSUFFICIENT` with all three labels `REVIEW`.
- V2 had a **confirmed code defect**: it read `response.status_code`, but GenLayer's authoritative `nondet.web.Response` has `response.status` (and `response.body`) according to [official SDK API](https://sdk.genlayer.com/main/_static/ai/api.txt). This `AttributeError` is swallowed by its fail-closed handler, producing `REVIEW`. Tests unintentionally used the same incorrect mock property.
- V3 is corrected **source code and offline tests only**. **No V3 deploy transaction or on-chain VERIFIED/ACCEPTED receipt has been supplied yet.** The objective is to obtain actual consensus for a new content-verified remediation and then a separate Claimant signature if the evidence merits acceptance.

## What changed

- New source: [`contracts/remedy_verify_v3.py`](../contracts/remedy_verify_v3.py). The only functional change from V2 is `response.status` instead of `response.status_code`; class and metadata identify `RemedyVerifyV3` / version `3.0.0`.
- New regression tests: [`tests/test_remedyverify_v3.py`](../tests/test_remedyverify_v3.py), using a mock with `.status` **and deliberately without `.status_code`**. A test reproduces the old V2's `INSUFFICIENT` caused by the bad property, and the V3 all-PASS branch checks both leader and validator independently fetch exact bytes and hashes.
- Same immutable, public evidence files and canonical SHA-256 hashes: [corrected report](../examples/positive_remediation/corrected_report.md) and [indexed archive](../examples/positive_remediation/indexed_source_archive.json) pinned to Git commit `675c2cc5c21bf0ec870155ce2e614bac6907914e`.
- Exact V3 studio arguments: [`examples/positive_remediation/studio_inputs_v3.json`](../examples/positive_remediation/studio_inputs_v3.json). No fabricated hashes or altered original Case #2 evidence.

## Minimal new on-chain sequence

1. Use the original AppealCore **without redeploying**, without re-adjudicating and without creating a new Case. Never call V2 `assess_remediation(1)` again because its stored status is already ASSESSED.
2. After the corrected V3 PR CI is PASS, open GenLayer Studio, paste **exact** `contracts/remedy_verify_v3.py` and deploy **new V3 verifier instance** on the same Studionet, constructor `appeal_core_address = 0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2`. Record actual address and FINALIZED / Accepted / GenVM SUCCESS deployment receipt. Do not silently upgrade/rewrite V1/V2 historical contract state.
3. From V3 read `stats()` and confirm `name=REMEDYVERIFY_V3`, `version=3.0.0`, `evidence_mode=PINNED_PUBLIC_WEB_CONTENT_SHA256`; read `get_core()` to confirm exact frozen AppealCore address above.
4. Switch to original Respondent Agent wallet `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`. On **V3 only**, call `submit_remediation(2, action_summary, evidence_json, evidence_sha256)` with the unchanged contents in `studio_inputs_v3.json`, Normal/Full Consensus and Simulation Mode OFF. The new V3 return value is its own remediation ID (normally `1`, but use actual returned ID).
5. Optionally view `get_remediation(new_id)` before any irreversible AI assessment to inspect the full stored raw URLs, hashes and original source-bound ruling.
6. From the original Respondent/Claimant, call `assess_remediation(new_id)` **once**. V3 fetches the two commit-pinned raw files, compares full response bytes against SHA-256, checks the index, and asks GenLayer AI about the actual document content. The original Claimant must not pre-approve. Capture the accepted Return Value and EP labels.
7. **Only after actual `VERIFIED`** with all three PASS labels and after inspecting the corrected report and archive, switch to original Claimant `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb` and call `respond_to_remediation(new_id, true, "I reviewed the corrected public report and indexed source archive, confirmed the linked digital demonstration deliverables, and accept the synthetic Case #2 correction.")`. The reason is limited to the synthetic demonstration and does not claim real-world delivery.
8. Verify the final `get_remediation(new_id)` readback says `status=ASSESSED`, `verdict=VERIFIED` and `claimant_response=ACCEPTED` before advertising a completed positive demo. Preserve the previous V1/V2 rejection transactions as distinct auditable outcomes.

## Failure handling and limits

- A response of `INSUFFICIENT` or `FAILED` remains a real non-success and is not grounds for Claimant approval. Investigate web access/HTTP status, exact hashes, archive checks and AI EP outputs before preparing any *new* record.
- The public [Web Access guide](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access) contains some examples using `status_code`, but the authoritative [SDK type reference](https://sdk.genlayer.com/main/_static/ai/api.txt) declares the Response field `status`; our tests model the SDK type, not the inconsistent guide examples.
- This source/test fix is evidence of a detected root cause, **not** yet proof of V3 web availability or positive on-chain consensus. The underlying clause 4.2 agreement is fictional; no completed legal or external customer remedy is asserted.
