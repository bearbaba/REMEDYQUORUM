# REMEDYQUORUM — GenLayer Studionet audit ledger

**One project: AppealCore + one active RemedyVerify.** This ledger documents real user-supplied Explorer receipts separately from local mocks and on-chain outcomes that have **not** been achieved. Historical failed contracts are **retired experiments**, not products or named releases.

## Current active deployment — 19 November 2026

| Module | Active address | Evidence |
|---|---|---|
| AppealCore | `0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2` | [Studio](https://studio.genlayer.com/?import-contract=0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2), accepted Case #2 transactions below |
| RemedyVerify | `0x8c65c73187bBf575201d31a1270812e1D4BeD830` | [Studio import](https://studio.genlayer.com/?import-contract=0x8c65c73187bBf575201d31a1270812e1D4BeD830), user-supplied screenshot showing **Deployed at** and **FINALIZED** deploy entry |

**Current verifier source:** [`contracts/remedy_verify.py`](../contracts/remedy_verify.py) — byte-for-byte copied from the source file shown by the user as deployed. Repository uses a single canonical filename. Internal code metadata from that immutable deployed artifact is intentionally unchanged: cosmetic renaming would no longer match its source. **The full new deploy transaction hash, separate `stats()`/`get_core()` readbacks, and independent chain bytecode/source attestation have not yet been furnished.**

**Current live positive-path status:** The current verifier has a real FINALIZED/Accepted/GenVM SUCCESS `assess_remediation(1)` returning **`VERIFIED`** with all three Equivalence Principle criteria **`PASS`** (receipt documented below). Original Claimant independently signed `ACCEPTED`, and a subsequent successful read-only `get_remediation(1)` confirms `ASSESSED / VERIFIED / ACCEPTED` (see final verification below). Do not reuse IDs from retired contracts.

## Active RemedyVerify — real accepted remediation submission (19 November 2026)

- **Transaction:** [`0x67f1879a9b3ddbb68b37953dcf5accfe7c20889844bb5b9b03919ea1f044e413`](https://explorer-studio.genlayer.com/tx/0x67f1879a9b3ddbb68b37953dcf5accfe7c20889844bb5b9b03919ea1f044e413).
- User-supplied GenLayer Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; method `submit_remediation(2, action_summary, evidence_json, evidence_sha256)`, target the one active RemedyVerify at `0x8c65c73187bBf575201d31a1270812e1D4BeD830`. Original Respondent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF` signed, nonce 146, Normal execution, 5 initial validators, 0 GEN.
- Actual return: **Remediation ID `1`** on the *current* contract; this ID is not interchangeable with IDs returned from retired contracts.
- Frozen input is the publicly accessible corrected report plus indexed source archive, each with a full SHA-256 and a 40-character immutable GitHub commit pin `675c2cc5c21bf0ec870155ce2e614bac6907914e`. Report digest `34b5c2767143b3a69dd9db4b0460d4489cc24ca13db9bedbb62862bc5350b741`, archive digest `da1960d26982394dbf08d8ac70ac3b3be1907e0cc9ac0791d8e8a8f9ef0cbca6`, canonical bundle digest `01846f7c006bfe89489d9e7e3625b81c83b5b6dd5a88d6af97b7e1e4ed3ffc87`. The source fixture is [`examples/positive_remediation/studio_inputs.json`](../examples/positive_remediation/studio_inputs.json).
- Source guardrails in `submit_remediation` require the original Respondent signer, a valid bound `UPHELD` AppealCore ruling, two distinct evidence roles, commit-pinned URL structure and canonical evidence-bundle hash. The successful return is evidence those on-chain guardrails passed.
- **Later achieved:** the independent AI `VERIFIED` transaction, original Claimant-signed `ACCEPTED` and a successful final stored-state `get_remediation(1)` are recorded in the sections below. A separate `get_core()` / `stats()` readback, full deploy transaction receipt, and per-validator web execution traces have not been attached.
- **Pre-assessment readback:** user-provided successful `get_remediation(1)` view showed `SUBMITTED`, `claimant_response=NONE`, the expected identities, URLs and frozen digests before the one-time AI assessment. A **later** read after the actual `VERIFIED` and `ACCEPTED` transactions confirmed the corresponding final stored state. These are user-provided Studio views, not independently authenticated RPC attestations.
- This is one active REMEDYQUORUM project and its synthetic digital dispute; no external legal performance is claimed.

## Active RemedyVerify — FINALIZED AI consensus: VERIFIED

- **Transaction:** [accepted GenLayer Explorer TX](https://explorer-studio.genlayer.com/tx/0xeb833645059564627bd042ba47b79d11ce63aff339b6b06f858f151549e5ede3).
- **User-provided receipt:** 19 November 2026, FINALIZED / Accepted / GenVM SUCCESS; original Respondent Agent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF` signed `assess_remediation(1)` to the sole current RemedyVerify `0x8c65c73187bBf575201d31a1270812e1D4BeD830`; nonce 147, 0 GEN, Normal execution, 5 initial validators.
- Actual return value: **`VERIFIED`**.
- Equivalence Principle output: `{"evidence_completeness":"PASS","remaining_violations":"PASS","remedy_match":"PASS"}`.
- In the maintained source, all-PASS classifications trigger the validator's independent semantic and downloaded-byte re-evaluation. The accepted receipt establishes the reported result; per-validator internal traces were not separately provided.
- Scope: verdict applies to a synthetic Case #2 and two actual public content-addressed digital artifacts, not independently attested third-party delivery or legal compliance.
- **Completed:** The original Claimant separately signed `respond_to_remediation(1, true, reason)` and the subsequent `get_remediation(1)` read confirms stored `VERIFIED / ACCEPTED`; see the final verification section below.
## Active RemedyVerify — Claimant acceptance and final stored-state readback

- **Claimant-signed transaction:** [`0x34301026aa6fcd4eda70785afb7e499e6fb9cffdef19fd80e578f5d69c44afae`](https://explorer-studio.genlayer.com/tx/0x34301026aa6fcd4eda70785afb7e499e6fb9cffdef19fd80e578f5d69c44afae). User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS** on 19 November 2026, 0 GEN, 5 initial validators, normal execution.
- Original Claimant/Principal `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb` signed `respond_to_remediation(1, true, reason)` to active RemedyVerify `0x8c65c73187bBf575201d31a1270812e1D4BeD830`, nonce 562. **Actual return: `ACCEPTED`.** The Boolean value was `true` and the signer was distinct from the original Respondent.
- **Exact claimant reason:** "I reviewed the corrected public report and indexed source archive, confirmed the linked digital demonstration deliverables, and accept the synthetic Case #2 correction."
- **Final read-only evidence:** user supplied the successful Studio `get_remediation(1)` response *after* Claimant acceptance. Stored `id=1`, `case_id=2`, `status=ASSESSED`, `verdict=VERIFIED`, `claimant_response=ACCEPTED`, and the same Claimant reason; all three stored labels (`remedy_match`, `evidence_completeness`, `remaining_violations`) are `PASS`.
- Stored `source_contract=0x1f08cd694ac1bdd822f83e593f1ca719236fb5d2`, original Claimant `0x4c7cb73ac8f8999af21cfc9ff4cf2333a9508dcb`, original Respondent `0xd6b8a3a5eb329410d9504784812b8569afa8c2af`, `claim_sha256=eb84170fdd5d8febe7c58b7334ad0ec211b712f17daddadd896c4f7410d6baa9`, and `ruling_sha256=62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0`.
- Stored `evidence_sha256=01846f7c006bfe89489d9e7e3625b81c83b5b6dd5a88d6af97b7e1e4ed3ffc87` with `corrected_report` and `indexed_archive` file digests matching the original submitted bundle. The chat-formatted view rendered the URLs as Markdown links; the prior pre-assessment readback independently displayed plain pinned HTTPS string values.
- Full **positive synthetic-case** proof now includes three actual downstream writes and two readbacks on the same active RemedyVerify: `submit_remediation(2) → remediation ID 1`, `assess_remediation(1) → VERIFIED`, `respond_to_remediation(1,true,reason) → ACCEPTED`, plus final `get_remediation(1) → ASSESSED / VERIFIED / ACCEPTED`. It follows an actual frozen Case #2 `UPHELD` ruling in AppealCore.
- **Assurance boundary:** real accepted GenLayer consensus and independent wallet authorization are demonstrated for a **fictional** dispute and public demonstration artifacts. This does not independently establish an off-chain customer received a deliverable, that a legal contract was performed, or that any remedy was externally enforced. Studio view `Response (Accepted)` means a read succeeded, while the separate stored field `claimant_response=ACCEPTED` represents the original claimant's on-chain decision.

## Reusable upstream proof — original AppealCore

| Stage | Result | Original signer | Real Explorer receipt |
|---|---|---|---|
| Case #2 opens | `2` | Claimant `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb` | [`open_case`](https://explorer-studio.genlayer.com/tx/0x98a6fdf19b227f6a72f0fd211c7900a9495589693160d48a109f1d9a8a7c64e6) |
| Respondent files separate response | `BOTH_SIDES_LOCKED` | Respondent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF` | [`submit_response`](https://explorer-studio.genlayer.com/tx/0x748a8916a95b5c136b100353104acf75e63eef8d21dbcecbf0652abbd7ddb227) |
| Independent AI consensus | `UPHELD` | Respondent | [`adjudicate(2)`](https://explorer-studio.genlayer.com/tx/0xc39ed18ca758922395b0f5d71d538cbc7118061cd873e52242ccec831e2d0d8d) |

All three are **FINALIZED / Accepted / GenVM SUCCESS**. The adjudication Equivalence Principle returned `{"claim_support":"SUPPORTED","counterevidence":"DOES_NOT_REBUT","remedy_basis":"REQUIRED"}`.

**Original `get_ruling(2)` readback:** Claimant `0x4c7cb73ac8f8999af21cfc9ff4cf2333a9508dcb`, Respondent `0xd6b8a3a5eb329410d9504784812b8569afa8c2af`, `claim_sha256=eb84170fdd5d8febe7c58b7334ad0ec211b712f17daddadd896c4f7410d6baa9`, `ruling_sha256=62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0`, required remedy: "Supply the missing indexed evidence archive and a corrected report containing reproducible source references, as expressly required by clause 4.2, at no additional charge." Recomputations from the original fictional claim and ruling match both digests (see [fixture](../examples/case2_upheld_ruling.json) and [test](../tests/test_live_ruling_fixture.py)).

Separate Case #1 [`adjudicate(1)`](https://explorer-studio.genlayer.com/tx/0xcde19030edac6f9dc9bf25b3246308b7d50cf336d9e4221c7138e3d7f9d48880) returned `REVIEW`, so no actionable ruling exists for that case.

## Retired failed implementation trials — audit only

These transactions are genuine historical tests of **discarded implementations**. They are **not** active project deployments or valid evidence of a completed remedy. They remain listed only so a reviewer can distinguish old failures from the new current address. They have not been erased from the blockchain.

| Test | Actual outcome | Explorer receipt |
|---|---|---|
| Initial incomplete synthetic corrective submission | Submitted remediation, ID 1 | [receipt](https://explorer-studio.genlayer.com/tx/0xff05637fb77dea5303fc6ee247b2d4741c5ce631d6d0a1bf0d834ffc13f72389) |
| AI assessment of that incomplete submission | `INSUFFICIENT`, three `REVIEW` | [receipt](https://explorer-studio.genlayer.com/tx/0xf1861eb91518341979c5204f1b26e47840f15fc1341216cc9417cd229cf44684) |
| Original Claimant response to insufficient evidence | `DISPUTED` | [receipt](https://explorer-studio.genlayer.com/tx/0x2c89898ac324dac262e5554d08c56ea426739aa3a55bfc20f1d6b4a353fc87ce) |
| Later external-document submission on a separate, now-retired verifier | Submitted remediation ID 1 | [receipt](https://explorer-studio.genlayer.com/tx/0xc42bf412c23aa271e07035c754fe0488e1504e5019cd3eda11a1c518956ba08e) |
| Subsequent live assessment exposed a web-response field mismatch in its implementation | `INSUFFICIENT`, three `REVIEW` | [receipt](https://explorer-studio.genlayer.com/tx/0x9fb07f5120fb11dbe233f337194c5558c568cbe70fc8f8a9d1cfde8a63e41bf8) |

The retired source incorrectly used `response.status_code` on the GenLayer web response, while the current canonical source uses `response.status`. The former error was hidden by an incorrect local mock and a fail-closed exception handler. This bug was fixed in the current source and regression-tested locally, **but successful HTTP retrieval or positive on-chain consensus on the newly deployed address is not yet demonstrated**.

Do not confuse a successful Studio view response labeled "Accepted" with a Claimant's on-chain corrective-action `ACCEPTED` verdict.

## Prepared source-addressed corrective evidence

Two actual, publicly inspectable files are pinned to GitHub commit `675c2cc5c21bf0ec870155ce2e614bac6907914e`:

- [Corrected report](../examples/positive_remediation/corrected_report.md): SHA-256 `34b5c2767143b3a69dd9db4b0460d4489cc24ca13db9bedbb62862bc5350b741`.
- [Indexed archive](../examples/positive_remediation/indexed_source_archive.json): SHA-256 `da1960d26982394dbf08d8ac70ac3b3be1907e0cc9ac0791d8e8a8f9ef0cbca6`.

Canonical submission bundle SHA-256 `01846f7c006bfe89489d9e7e3625b81c83b5b6dd5a88d6af97b7e1e4ed3ffc87`. [Studio arguments](../examples/positive_remediation/studio_inputs.json).

## Release gate

**Positive synthetic end-to-end workflow completed:** (b) accepted `submit_remediation(2)` returned remediation ID 1, (c) accepted `assess_remediation(1)` returned `VERIFIED` with three PASS labels, (d) original Claimant separately signed `ACCEPTED`, and (e) successful Studio readback confirmed the final `ASSESSED / VERIFIED / ACCEPTED` state. **Remaining independent assurance checks before any claims about deployed source identity:** a standalone `get_core()/stats()` readback, the full current verifier deployment receipt and separate code-identity attestation have not yet been supplied. Do not invent times, hashes or success outcomes. This is a **synthetic digital dispute**, not external legal or delivery attestation.

Local Python CI validates code under controlled shims, not live GenLayer consensus.
