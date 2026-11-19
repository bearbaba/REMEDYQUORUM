# REMEDYQUORUM — GenLayer Studionet audit ledger

**One project: AppealCore + one active RemedyVerify.** This ledger documents real user-supplied Explorer receipts separately from local mocks and on-chain outcomes that have **not** been achieved. Historical failed contracts are **retired experiments**, not products or named releases.

## Current active deployment — 19 November 2026

| Module | Active address | Evidence |
|---|---|---|
| AppealCore | `0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2` | [Studio](https://studio.genlayer.com/?import-contract=0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2), accepted Case #2 transactions below |
| RemedyVerify | `0x8c65c73187bBf575201d31a1270812e1D4BeD830` | [Studio import](https://studio.genlayer.com/?import-contract=0x8c65c73187bBf575201d31a1270812e1D4BeD830), user-supplied screenshot showing **Deployed at** and **FINALIZED** deploy entry |

**Current verifier source:** [`contracts/remedy_verify.py`](../contracts/remedy_verify.py) — byte-for-byte copied from the source file shown by the user as deployed. Repository uses a single canonical filename. Internal code metadata from that immutable deployed artifact is intentionally unchanged: cosmetic renaming would no longer match its source. **The full new deploy transaction hash, separate `stats()`/`get_core()` readbacks, and independent chain bytecode/source attestation have not yet been furnished.**

**Current live positive-path status:** a real finalized `submit_remediation` for Case #2 **has** now been supplied (see below), but no subsequent `assess_remediation`, `VERIFIED` or Claimant `ACCEPTED` transaction has been supplied. Do not reuse remediation IDs from retired contract addresses.

## Active RemedyVerify — real accepted remediation submission (19 November 2026)

- **Transaction:** [`0x67f1879a9b3ddbb68b37953dcf5accfe7c20889844bb5b9b03919ea1f044e413`](https://explorer-studio.genlayer.com/tx/0x67f1879a9b3ddbb68b37953dcf5accfe7c20889844bb5b9b03919ea1f044e413).
- User-supplied GenLayer Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; method `submit_remediation(2, action_summary, evidence_json, evidence_sha256)`, target the one active RemedyVerify at `0x8c65c73187bBf575201d31a1270812e1D4BeD830`. Original Respondent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF` signed, nonce 146, Normal execution, 5 initial validators, 0 GEN.
- Actual return: **Remediation ID `1`** on the *current* contract; this ID is not interchangeable with IDs returned from retired contracts.
- Frozen input is the publicly accessible corrected report plus indexed source archive, each with a full SHA-256 and a 40-character immutable GitHub commit pin `675c2cc5c21bf0ec870155ce2e614bac6907914e`. Report digest `34b5c2767143b3a69dd9db4b0460d4489cc24ca13db9bedbb62862bc5350b741`, archive digest `da1960d26982394dbf08d8ac70ac3b3be1907e0cc9ac0791d8e8a8f9ef0cbca6`, canonical bundle digest `01846f7c006bfe89489d9e7e3625b81c83b5b6dd5a88d6af97b7e1e4ed3ffc87`. The source fixture is [`examples/positive_remediation/studio_inputs.json`](../examples/positive_remediation/studio_inputs.json).
- Source guardrails in `submit_remediation` require the original Respondent signer, a valid bound `UPHELD` AppealCore ruling, two distinct evidence roles, commit-pinned URL structure and canonical evidence-bundle hash. The successful return is evidence those on-chain guardrails passed.
- **Not yet evidenced:** a separate `get_core()` / `stats()` readback of the current verifier, stored `get_remediation(1)`, actual HTTP content fetching, GenLayer `assess_remediation(1)` consensus, `VERIFIED` verdict, or independent Claimant `ACCEPTED`.
- **Safest next action:** call **read-only `get_remediation(1)`** on the current address. Confirm `status=SUBMITTED`, `claimant_response=NONE`, `case_id=2`, the original parties, exact source contract, two *plain* HTTPS URL values and both pinned SHA-256 commitments. The Explorer input display may render plain URL text as Markdown links; the stored readback is the authoritative string value. Once confirmed, run `assess_remediation(1)` only once.
- This is one active REMEDYQUORUM project and its synthetic digital dispute; no external legal performance is claimed.

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

Keep the contribution **unsubmitted** until (a) read-only `get_core()/stats()` confirm the current deployed verifier's source link, (b) **completed**: accepted `submit_remediation(2)` returned Remediation ID 1 at the current address, (c) an actually accepted `assess_remediation` returns `VERIFIED` with all three PASS labels, (d) the original Claimant independently signs `ACCEPTED`, and (e) final read-only state agrees. Do not invent times, hashes or success outcomes. This is a **synthetic digital dispute**, not external legal or delivery attestation.

Local Python CI validates code under controlled shims, not live GenLayer consensus.
