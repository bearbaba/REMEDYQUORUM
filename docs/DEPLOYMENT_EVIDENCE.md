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
- The receipt verifies **the submission**, not the truth of the fictional clause or missing archive. The distinct Respondent's successful signed response and accepted `UPHELD` adjudication are documented immediately below; the verdict is a conclusion about fictional submitted statements, not verified real-world conduct.

## Case #2 — authentic Respondent-signed response

- **TX:** [`0x748a8916a95b5c136b100353104acf75e63eef8d21dbcecbf0652abbd7ddb227`](https://explorer-studio.genlayer.com/tx/0x748a8916a95b5c136b100353104acf75e63eef8d21dbcecbf0652abbd7ddb227).
- User-provided GenLayer Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**. Respondent/Agent wallet `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, nonce 140, value 0 GEN, method `submit_response(2, response_json)`, returned **`BOTH_SIDES_LOCKED`**.
- Filed fictional response: "We acknowledge that the fictional delivery manifest lists only the final report and does not record the indexed evidence archive. We believed the archive could be supplied separately, but it has not yet been delivered."
- Filed fictional response evidence: "The fictional delivery manifest lists final_report.pdf without an accompanying archive entry. Clause 4.2 requires both the final report and the indexed source-evidence archive for complete delivery."
- **Status:** both independent parties signed their statements and they were locked before the subsequent accepted `adjudicate(2)` transaction. This alone does not establish real-world truth; see the accepted adjudication receipt below.

## Case #2 — genuine GenLayer AI consensus: UPHELD

- **TX:** [`0xc39ed18ca758922395b0f5d71d538cbc7118061cd873e52242ccec831e2d0d8d`](https://explorer-studio.genlayer.com/tx/0xc39ed18ca758922395b0f5d71d538cbc7118061cd873e52242ccec831e2d0d8d).
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; function `adjudicate(2)`; Respondent/Agent signer `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, nonce 141, value 0 GEN.
- Actual return value: **`UPHELD`**. GenLayer Equivalence Principle output: `{"claim_support":"SUPPORTED","counterevidence":"DOES_NOT_REBUT","remedy_basis":"REQUIRED"}`.
- The deterministic mapping of all three accepted labels now provides a **positive, actionable ruling on submitted synthetic facts**, in contrast with Case #1 `REVIEW`. GenLayer did not verify external contract execution, deliverables, or real-world legal liability.
- **Do not repeat `adjudicate(2)`**; AppealCore allows exactly one adjudication per case.
- **User-provided `get_ruling(2)` view result (read-only):** `contract=APPEALCORE`, `case_id=2`, `verdict=UPHELD`, `claimant=0x4c7cb73ac8f8999af21cfc9ff4cf2333a9508dcb`, `respondent=0xd6b8a3a5eb329410d9504784812b8569afa8c2af`, `claim_sha256=eb84170fdd5d8febe7c58b7334ad0ec211b712f17daddadd896c4f7410d6baa9`, `ruling_sha256=62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0`.
- **Frozen required remedy (exact):** "Supply the missing indexed evidence archive and a corrected report containing reproducible source references, as expressly required by clause 4.2, at no additional charge."
- Independently recomputed SHA-256 of the **canonical frozen Case #2 claim**: `eb84170fdd5d8febe7c58b7334ad0ec211b712f17daddadd896c4f7410d6baa9` — **exact match**.
- Independently recomputed SHA-256 of the **canonical six-field ruling payload**: `62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0` — **exact match**. Reproducible local fixture tests are provided in `tests/test_live_ruling_fixture.py`.
- Source of view data: copied user-supplied Studio output. Hash verification validates the reported fields' internal consistency; this is **not yet an independently executed LATEST_FINAL RPC read** and is not external proof of the fictional contract's performance.
- **Next:** deploy `RemedyVerify` from the unchanged repository source, passing `appeal_core_address="0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2"` as constructor argument. Then capture the real RemedyVerify deployment address and inspect `get_core()` before making remediation claims.

## Next live steps

1. Optionally read `get_case(1)` at `LATEST_FINAL` and document its actual persisted verdict and three labels.
2. Case #2's separately signed `adjudicate(2)` is **FINALIZED / Accepted / SUCCESS**, with return `UPHELD`. A user-provided `get_ruling(2)` output has matching recomputed claim/ruling hashes; independently read `get_case(2)` at `LATEST_FINAL` when available. The existing ruling readback is sufficient to begin the downstream source-address-bound deployment but does not replace independent RPC attestation.
3. Deploy the existing `contracts/remedy_verify.py` with constructor `appeal_core_address="0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2"`. Record the real deployment address; check its `get_core()` and `stats()` before submitting remediation. No RemedyVerify deployment or corrective-action evidence is claimed yet.
4. Independently attest deployed source and state before submission.

Local [CI](https://github.com/bearbaba/REMEDYQUORUM/actions) validates code with controlled GenLayer shims, not real remote consensus.
