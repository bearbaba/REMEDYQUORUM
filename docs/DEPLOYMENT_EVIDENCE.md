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
- **Next:** RemedyVerify is deployed with the correct constructor address; its successful cross-contract `submit_remediation(2, ...)` transaction is documented below. A standalone `get_core()` view readback is still pending.

## RemedyVerify — finalized linked deployment (18 November 2026)

- **Deployment TX:** [`0x221fd82b5fdc8982cc3babea7411190f9ba915be7db0e990ccfd797151512014`](https://explorer-studio.genlayer.com/tx/0x221fd82b5fdc8982cc3babea7411190f9ba915be7db0e990ccfd797151512014).
- User-provided full Explorer deploy receipt: **FINALIZED / Accepted / GenVM SUCCESS**, deployment method, from Principal `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb`, nonce 558, value 0 GEN, initial validators 5.
- **New deployed address:** `0x2138A278289A00Bae34c986B24b168800961B824`. [Import RemedyVerify in Studio](https://studio.genlayer.com/?import-contract=0x2138A278289A00Bae34c986B24b168800961B824).
- Receipt contains the deployed `contract_code` (Python `RemedyVerify`) and constructor `calldata`. Decoding the Base64 calldata gives the expected constructor `appeal_core_address=0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2` (same exact deployed AppealCore address from Case #2).
- Contract implementation fixes `self.core` at deployment; `submit_remediation` and `assess_remediation` read `get_ruling(case_id)` from that stored source address and check the complete ruling hash, original participants, `UPHELD` verdict, and requested remedy.
- **Evidence boundary:** this receipt proves an accepted deployment with the correct constructor argument. A subsequently accepted `submit_remediation(2,...)` provides additional **cross-contract read/validation evidence** (see next section), but a standalone live `get_core()` view, AI `VERIFIED` result and Claimant acknowledgment are **not yet** documented.
- Demo case and potential evidence submissions are **synthetic**; file digests bind bytes, not external delivery or performance. Claimant's separate signature is required for any acceptance.

## Case #2 — finalized cross-contract remediation submission

- **TX:** [`0xff05637fb77dea5303fc6ee247b2d4741c5ce631d6d0a1bf0d834ffc13f72389`](https://explorer-studio.genlayer.com/tx/0xff05637fb77dea5303fc6ee247b2d4741c5ce631d6d0a1bf0d834ffc13f72389).
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; method `submit_remediation`, `case_id=2`, target RemedyVerify `0x2138A278289A00Bae34c986B24b168800961B824`, original Respondent/Agent signer `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, nonce 142, value 0 GEN.
- Actual return value: **Remediation ID `1`**. Contract code stores this item as `SUBMITTED`; a separate `get_remediation(1)` storage readback has not yet been attached.
- Input `action_summary` states synthetic fixture report and indexed archive were prepared at no extra cost, while explicitly disclaiming any external delivery or Claimant receipt.
- `evidence_json` contains two actual synthetic repository artifacts: [corrected_report.md](../examples/demo_remediation/corrected_report.md) (`e609fd0b96ea65c21781db4f93817c72691e89642519f99c5e3d679a60a396e4`) and [source_archive.json](../examples/demo_remediation/source_archive.json) (`1cbe9e5cda4fc30209f85c0312b9e719ca6b15310cdace635894fe295a4e7bee`).
- Canonical JSON evidence-bundle SHA-256 submitted: `e4cc82d7c0418b16ef1c4561764772e3e6296bcbd792b93f5fe90a0a5ce9ee66`. These digests are checked against exact source fixture bytes and canonical bundle with [reproducible Python test](../tests/test_demo_remediation_fixture.py).
- `RemedyVerify.submit_remediation` calls `gl.get_contract_at(self.core).view().get_ruling(case_id)` and validates `UPHELD`, case/ruling hash, participant binding, signer authorization and canonical evidence bundle digest. **The accepted result is substantive evidence that these on-chain cross-contract gates succeeded** for this input; a failed guard would not successfully return Remediation ID 1.
- **Subsequent AI assessment and Claimant response:** actual `assess_remediation(1)` returned `INSUFFICIENT`, followed by an independently Claimant-signed `respond_to_remediation(1,false,...)` returning `DISPUTED` (both FINALIZED / Accepted / GenVM SUCCESS), documented below. `VERIFIED`, a completed remedy, and external proof of delivery have **not** been established.

## Case #2 — real GenLayer remediation assessment: INSUFFICIENT

- **TX:** [`0xf1861eb91518341979c5204f1b26e47840f15fc1341216cc9417cd229cf44684`](https://explorer-studio.genlayer.com/tx/0xf1861eb91518341979c5204f1b26e47840f15fc1341216cc9417cd229cf44684).
- User-provided Explorer receipt (18 November 2026): **FINALIZED / Accepted / GenVM SUCCESS**. Signed by bound Respondent/Agent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, method `assess_remediation(1)`, to RemedyVerify `0x2138A278289A00Bae34c986B24b168800961B824`, nonce 143, value 0 GEN, initial validators 5.
- Actual return value: **`INSUFFICIENT`**. Equivalence Principle output: `{"evidence_completeness":"REVIEW","remaining_violations":"REVIEW","remedy_match":"REVIEW"}`.
- The deterministic verdict mapping returns `INSUFFICIENT` for any `REVIEW` criterion without a confirmed `FAIL`. The successful transaction records an assessed remediation but **does not establish delivery, compliance, `VERIFIED`, or Claimant acceptance**.
- Important consensus nuance: under the deployed validator, a `REVIEW`-only decision is admissible without an independent validator rerun of the underlying AI prompt; independent all-PASS re-evaluation is required for `VERIFIED` and separately flagged FAIL re-evaluation is required for a `FAILED` classification. The receipt supports accepted GenLayer execution and the three actual REVIEW labels, not a claim that validators independently rejudged each REVIEW criterion.
- Because `assess_remediation(1)` has succeeded, it must **not be called again**: the contract guards against duplicate assessment (`status != SUBMITTED`). An optional read-only `get_remediation(1)` call can show stored `ASSESSED`, `INSUFFICIENT`, `claimant_response=NONE` and exact ruling/digest bindings (the readback is still pending).
- **Subsequent Claimant safety demonstration:** the original Claimant has now signed `respond_to_remediation(1, false, reason)` with result `DISPUTED` as recorded below. Under the deployed contract, `accept=true` is forbidden when verdict is `INSUFFICIENT`. A later remedial attempt would require a separate new remediation record; the old assessment must not be overwritten.

## Case #2 — FINALIZED independent Claimant response: DISPUTED

- **TX:** [`0x2c89898ac324dac262e5554d08c56ea426739aa3a55bfc20f1d6b4a353fc87ce`](https://explorer-studio.genlayer.com/tx/0x2c89898ac324dac262e5554d08c56ea426739aa3a55bfc20f1d6b4a353fc87ce).
- User-provided Studio Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**, Normal execution, 5 initial validators, 0 GEN; Claimant/Principal **`0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb`**, nonce **559**, target RemedyVerify **`0x2138A278289A00Bae34c986B24b168800961B824`**.
- Method: `respond_to_remediation(1, false, reason)`. The `accept` argument was genuine Boolean `false`, not the string `"false"`.
- Reason (exact): "The submitted synthetic artifacts do not establish independently confirmed delivery or complete fulfillment of clause 4.2. Additional verifiable evidence is required."
- Actual return value: **`DISPUTED`**. The caller was the **original Claimant**, distinct from the Respondent who filed the remediation and requested AI assessment.
- This finalizes the **negative/insufficient-evidence branch** of the single, connected REMEDYQUORUM workflow: `open_case(2)` → `submit_response(2)` → `adjudicate(2): UPHELD` → `submit_remediation(2): ID 1` → `assess_remediation(1): INSUFFICIENT` → `respond_to_remediation(1,false): DISPUTED`.
- `DISPUTED` is a genuine on-chain **refusal to accept** the submitted synthetic corrective evidence. It is **not** `ACCEPTED`, **not** `VERIFIED`, and does not show any off-chain corrective action or legal enforcement.
- Under deployed source, `respond_to_remediation` permits only the stored Claimant, requires `status=ASSESSED` and `claimant_response=NONE`, and prevents `accept=true` unless `verdict=VERIFIED`. Successful `DISPUTED` confirms an authorized one-time response; no need to spend test GEN on an intentional rollback.
- A **user-supplied, successful read-only `get_remediation(1)` view result** now confirms the stored `claimant_response=DISPUTED`, `verdict=INSUFFICIENT`, original identities, source contract, canonical evidence digest, claim digest and ruling digest. See the final view fixture section below. The view was copied from Studio; its `LATEST_FINAL` selector and an independent RPC read were not separately attested.

## Case #2 — final read-only RemedyVerify storage confirmation

- **Source:** user-pasted `get_remediation(1)` Contract Call response marked `Response (Accepted)`. This denotes the **successful read**, not acceptance of a correction. No new transaction hash is associated with this read-only evidence.
- Stored `id=1`, `case_id=2`, `status=ASSESSED`, `verdict=INSUFFICIENT`, `claimant_response=DISPUTED`, with `claimant_reason` exactly matching the separately signed Claimant refusal transaction above.
- All three stored labels are `REVIEW`: `evidence_completeness`, `remaining_violations`, `remedy_match`. **Neither `VERIFIED` nor `ACCEPTED` appears in the finalized state.**
- `source_contract=0x1f08cd694ac1bdd822f83e593f1ca719236fb5d2` matches the deployed AppealCore. Original Claimant `0x4c7cb73ac8f8999af21cfc9ff4cf2333a9508dcb` and Respondent `0xd6b8a3a5eb329410d9504784812b8569afa8c2af` match the on-chain ruling.
- `claim_sha256=eb84170fdd5d8febe7c58b7334ad0ec211b712f17daddadd896c4f7410d6baa9` and `ruling_sha256=62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0` match Case #2's saved `UPHELD` ruling fixture.
- `evidence_sha256=e4cc82d7c0418b16ef1c4561764772e3e6296bcbd792b93f5fe90a0a5ce9ee66` matches the content-addressed synthetic evidence bundle submitted for Remediation ID 1.
- The exact [user-supplied storage view fixture](../examples/demo_remediation/remediation1_final_readback.json) is retained as machine-readable evidence; [offline tests](../tests/test_remediation_readback_fixture.py) verify its fields against the saved `UPHELD` ruling, submitted evidence JSON and canonical SHA-256. These comparisons establish **internal consistency**, not an independently executed RPC read or proof of off-chain delivery.
- **Assurance boundary:** read request's "Accepted" status is unrelated to business-state `claimant_response=DISPUTED`. This is a verified negative branch of the synthetic workflow; the separate positive `VERIFIED → ACCEPTED` branch is not demonstrated.

## Next live steps

1. Optionally read `get_case(1)` at `LATEST_FINAL` and document its actual persisted verdict and three labels.
2. Case #2's separately signed `adjudicate(2)` is **FINALIZED / Accepted / SUCCESS**, with return `UPHELD`. A user-provided `get_ruling(2)` output has matching recomputed claim/ruling hashes; independently read `get_case(2)` at `LATEST_FINAL` when available. The existing ruling readback is sufficient to begin the downstream source-address-bound deployment but does not replace independent RPC attestation.
3. **Completed:** RemedyVerify at `0x2138A278289A00Bae34c986B24b168800961B824` accepted the Respondent's linked `submit_remediation(2, ...)` and returned Remediation ID 1. A later successful Studio `get_remediation(1)` readback was supplied and cross-checked against the ruling and evidence fixture. A separate `get_core()` view and independently authenticated `LATEST_FINAL` RPC read remain optional checks.
4. **Completed:** Respondent `assess_remediation(1)` returned `INSUFFICIENT` with three `REVIEW` labels; original Claimant separately recorded `respond_to_remediation(1, false, reason): DISPUTED` in a FINALIZED transaction. The successful fail-closed negative branch is complete. No repeat writes are needed for this case. For additional assurance before submission, use independent read-only `LATEST_FINAL` / `get_core()` checks and verify deployed-source identity; the user-pasted `get_remediation(1)` readback is already preserved. The positive `VERIFIED`/`ACCEPTED` path is **not** evidenced.

Local [CI](https://github.com/bearbaba/REMEDYQUORUM/actions) validates code with controlled GenLayer shims, not real remote consensus.


## RemedyVerify V2 — content-addressed remediation submission (18 November 2026)

- **New verifier address:** [`0x5C6d327F57f8A49E9c64872c64d8C5D04Aca9C48`](https://studio.genlayer.com/?import-contract=0x5C6d327F57f8A49E9c64872c64d8C5D04Aca9C48). User-provided Studio screenshot shows a deployed contract, transaction entry FINALIZED, and the expected get_core, get_remediation, stats, submit_remediation, assess_remediation and respond_to_remediation methods. A full separate V2 deploy transaction hash and independent source-byte attestation have not yet been attached.
- **Live submission TX:** [`0xc42bf412c23aa271e07035c754fe0488e1504e5019cd3eda11a1c518956ba08e`](https://explorer-studio.genlayer.com/tx/0xc42bf412c23aa271e07035c754fe0488e1504e5019cd3eda11a1c518956ba08e), user-provided Explorer receipt **FINALIZED / Accepted / GenVM SUCCESS**, Normal execution, five initial validators, signed by original Respondent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, nonce 144, 0 GEN.
- Called `submit_remediation(2, action_summary, evidence_json, evidence_sha256)` on the V2 address. **Actual return: Remediation ID `1` in the new V2 instance.** This is distinct from RemedyVerify V1's old Remediation ID 1, which remains `INSUFFICIENT / DISPUTED`.
- Input evidence has two roles `corrected_report` and `indexed_archive`, with immutable GitHub commit `675c2cc5c21bf0ec870155ce2e614bac6907914e`, pinned public artifact URLs and SHA-256 `34b5c2767143b3a69dd9db4b0460d4489cc24ca13db9bedbb62862bc5350b741` (corrected report) and `da1960d26982394dbf08d8ac70ac3b3be1907e0cc9ac0791d8e8a8f9ef0cbca6` (indexed archive). Canonical bundle digest: `01846f7c006bfe89489d9e7e3625b81c83b5b6dd5a88d6af97b7e1e4ed3ffc87`. Exact submitted-input fixture: [`studio_inputs_v2.json`](../examples/positive_remediation/studio_inputs_v2.json).
- **Validation boundary:** the accepted `submit_remediation` executes the source-ruling, role/URL-shape, signer and canonical hash checks and stores the remediation. It does **not** fetch external artifact bytes or run the AI assessment: these steps occur only in the separate, **not-yet-executed** `assess_remediation(1)` call. The user-pasted Explorer table Markdown-formats the two URLs as clickable links, so the actual stored `get_remediation(1)` response is preferable for examining the URL string bytes.
- **Next stage:** optionally read `get_remediation(1)` and `stats()` from V2, then from the original Claimant or Respondent invoke `assess_remediation(1)` **once** in Normal/Full Consensus. Record the true verdict and equivalence labels. Only actual accepted `VERIFIED` plus a separately signed original Claimant `respond_to_remediation(1, true, reason)` can demonstrate a positive `ACCEPTED` result. No such success is claimed yet.
- **Single-project assurance:** AppealCore Case #2 remains `UPHELD`; V1's negative branch is intact. V2 is a new on-chain module inside the same REMEDYQUORUM project, not a separate contribution.

## RemedyVerify V2 — real on-chain consensus: INSUFFICIENT (API compatibility defect)

- **Transaction:** [`0x9fb07f5120fb11dbe233f337194c5558c568cbe70fc8f8a9d1cfde8a63e41bf8`](https://explorer-studio.genlayer.com/tx/0x9fb07f5120fb11dbe233f337194c5558c568cbe70fc8f8a9d1cfde8a63e41bf8).
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS** (18 November 2026), original Respondent Agent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF`, nonce 145, calling `assess_remediation(1)` on V2 address `0x5C6d327F57f8A49E9c64872c64d8C5D04Aca9C48`; return **`INSUFFICIENT`**.
- Equivalence Principle labels: `{"evidence_completeness":"REVIEW","remaining_violations":"REVIEW","remedy_match":"REVIEW"}`. No `VERIFIED` or Claimant `ACCEPTED` result exists for V2; the assessed Remediation ID 1 must not be re-run.
- **Confirmed source defect:** V2 `judge()` accesses `response.status_code` after `gl.nondet.web.get(url)`. The authoritative [GenLayer SDK Response API](https://sdk.genlayer.com/main/_static/ai/api.txt) defines a `status: int` field and a `body: bytes | None` field, **not** `status_code`. The invalid attribute raises `AttributeError`, which V2's broad caught exception maps to the three `REVIEW` labels without surfacing the reason. This is a strong code-level explanation of the observed response; the real execution's internal trace has not yet been independently inspected.
- **Why local CI previously passed:** the original test fake `FakeWebResponse` incorrectly provided `status_code=200`, matching the faulty contract, whereas the real SDK Response has `status`. The V2 tests therefore did not detect this environment mismatch.
- **Fix:** new source-only [`contracts/remedy_verify_v3.py`](../contracts/remedy_verify_v3.py) reads `response.status`, and [`tests/test_remedyverify_v3.py`](../tests/test_remedyverify_v3.py) uses only `status`, reproduces the V2 bug and tests the repaired all-PASS path. V3 is a separate fresh verifier instance to preserve unchangeable V2's accepted `INSUFFICIENT` state and the original V1 negative path.
- **Do not submit as a completed positive remediation yet.** A V3 on-chain deployment and real `submit_remediation → assess_remediation: VERIFIED → original Claimant ACCEPTED` transaction sequence have not yet occurred. The underlying fictional dispute is always marked synthetic.

