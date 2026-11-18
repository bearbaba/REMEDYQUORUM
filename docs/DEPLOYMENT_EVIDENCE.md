# REMEDYQUORUM — Studionet Execution Evidence

Network: GenLayer Studionet. Date: 18 November 2026. This document distinguishes deployed contract receipts from local tests and unverified future results.

## Live first component: AppealCore

- Source: [`contracts/appeal_core.py`](../contracts/appeal_core.py)
- User-supplied deployed address: `0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2`
- [Import the deployed contract into GenLayer Studio](https://studio.genlayer.com/?import-contract=0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2)
- User's Studio screenshot reported **Deployed** and a **FINALIZED** deployment; **the full deployment TX hash is not yet provided**, so independent byte-for-byte source attestation is not yet claimed.
- Bound test roles: Claimant/Principal `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb`; Respondent/Agent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`.

## Case #1 — authentic Claimant-signed submission

- **TX:** [`0x3af6eb6cef490a79c4d1cfb010e1e6816f707c461298988f0b6fa695123506f5`](https://explorer-studio.genlayer.com/tx/0x3af6eb6cef490a79c4d1cfb010e1e6816f707c461298988f0b6fa695123506f5)
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; nonce 556; value 0 GEN.
- Function: `open_case(respondent_address, claim_json)` from Claimant. Returned **Case ID = 1**.
- Respondent address: `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`.
- Frozen fictional claim states that a service provider delivered a report without mandatory supporting evidence; requested remedy is to provide supporting files and a corrected report with reproducible references. This is a **synthetic demonstration dispute**, not independent proof of delivery or contract breach.
- This transaction proves the original claim was accepted and stored. The separately signed response and accepted adjudication are documented below; the **REVIEW** decision is not an actionable UPHELD ruling.

## Case #1 — authentic Respondent-signed rebuttal

- **TX:** [`0x49e5330c7b76cd21e55e87adcfc99ca04ae504e5e265ccf4c269c168bfd277f1`](https://explorer-studio.genlayer.com/tx/0x49e5330c7b76cd21e55e87adcfc99ca04ae504e5e265ccf4c269c168bfd277f1).
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; value 0 GEN; nonce 138.
- The independent Respondent/Agent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF` called `submit_response(1, response_json)` on the deployed AppealCore. Return value: **`BOTH_SIDES_LOCKED`**.
- Submitted rebuttal: `We contest the scope interpretation because the completed report was delivered and the source archive was intended as a separate deliverable.`
- Submitted `response_evidence`: `The signed delivery receipt names a report attachment but contains no specific confirmation of evidence archive delivery.`
- This establishes that distinct claimant and respondent wallets committed their respective synthetic narratives in the same on-chain case. It **does not** prove either narrative true, and **does not** imply an AI ruling.

## Case #1 — genuine GenLayer AI consensus: REVIEW (fail-closed)

- **TX:** [`0xcde19030edac6f9dc9bf25b3246308b7d50cf336d9e4221c7138e3d7f9d48880`](https://explorer-studio.genlayer.com/tx/0xcde19030edac6f9dc9bf25b3246308b7d50cf336d9e4221c7138e3d7f9d48880).
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; method `adjudicate(1)`; Respondent/Agent signer `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`; nonce 139, value 0 GEN.
- Actual return value: **`REVIEW`**. GenLayer Equivalence Principle output: `{"claim_support":"SUPPORTED","counterevidence":"DOES_NOT_REBUT","remedy_basis":"REVIEW"}`.
- Interpreting this narrowly: the assessment labels support the claim and find the rebuttal insufficient, but the requested remedy's factual basis remains inconclusive. Because `remedy_basis=REVIEW`, the contract's deterministic verdict mapping conservatively returns `REVIEW`, not `UPHELD`. No executable ruling can be obtained through `get_ruling(1)`.
- **Do not rerun `adjudicate(1)`**. Case #1 has already undergone its one on-chain review. Its synthetic inputs do not independently prove any real-world breach, delivery or obligation.
- A `LATEST_FINAL` `get_case(1)` readback has not yet been independently attached; the accepted transaction receipt proves the returned verdict and EP labels but is not a substitute for a separately checked storage snapshot.

## Case #2 — authentic Claimant-signed submission (18 November 2026)

- **TX:** [`0x98a6fdf19b227f6a72f0fd211c7900a9495589693160d48a109f1d9a8a7c64e6`](https://explorer-studio.genlayer.com/tx/0x98a6fdf19b227f6a72f0fd211c7900a9495589693160d48a109f1d9a8a7c64e6).
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**, Claimant/Principal `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb` signed `open_case`, nonce 557, value 0 GEN, returned **Case ID = 2**.
- Respondent bound to `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, distinct from the Claimant.
- Fictional claim: synthetic project clause 4.2 requires both a final report and indexed source-evidence archive; fictional delivery manifest names only `final_report.pdf`. Requested remedy is an indexed archive and corrected report with reproducible references, at no additional charge.
- The receipt verifies **the submission**, not the truth of the fictional clause or missing archive. The distinct Respondent's successful signed response is documented immediately below; no AI adjudication for Case #2 has yet occurred.

## Case #2 — authentic Respondent-signed response

- **TX:** [`0x748a8916a95b5c136b100353104acf75e63eef8d21dbcecbf0652abbd7ddb227`](https://explorer-studio.genlayer.com/tx/0x748a8916a95b5c136b100353104acf75e63eef8d21dbcecbf0652abbd7ddb227).
- User-provided GenLayer Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**. Respondent/Agent wallet `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, nonce 140, value 0 GEN, method `submit_response(2, response_json)`, returned **`BOTH_SIDES_LOCKED`**.
- Filed fictional response: "We acknowledge that the fictional delivery manifest lists only the final report and does not record the indexed evidence archive. We believed the archive could be supplied separately, but it has not yet been delivered."
- Filed fictional response evidence: "The fictional delivery manifest lists final_report.pdf without an accompanying archive entry. Clause 4.2 requires both the final report and the indexed source-evidence archive for complete delivery."
- **Status:** both independent parties have signed their statements, now locked for an adjudication. This does not establish the real-world truth of the synthetic facts, nor an `UPHELD` or any other verdict. `adjudicate(2)` must be assessed by real GenLayer consensus **once**.

## Next live steps

1. Optionally read `get_case(1)` at `LATEST_FINAL` and document its actual persisted verdict and three labels.
2. Case #2 has a finalized Claimant claim and a separate finalized Respondent rebuttal, returning `BOTH_SIDES_LOCKED`. An original party may now call `adjudicate(2)` **once**, using Normal/Full Consensus. Record its actual FINALIZED/Accepted/SUCCESS status, Equivalence Principle fields and verdict rather than presuming `UPHELD`.
3. Only an accepted **`UPHELD`** ruling makes `get_ruling(case_id)` actionable. Deploy RemedyVerify with AppealCore's exact address and test its real cross-contract binding; otherwise, keep the remediation gate closed.
4. Independently attest deployed source and state before submission.

Local [CI](https://github.com/bearbaba/REMEDYQUORUM/actions) validates code with controlled GenLayer shims, not real remote consensus.
