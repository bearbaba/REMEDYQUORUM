# REMEDYQUORUM — Unified AI Dispute-to-Remediation Accountability

**One unified GenLayer Intelligent Contract contribution:** a dispute-to-remediation lifecycle implemented by two linked on-chain modules, with a shared case identity, immutable ruling commitment, independent participants, and auditable outcomes. It is **one system, not two standalone project submissions**.

| Deploy sequence | Contract | Purpose |
|---|---|---|
| First | `contracts/appeal_core.py` — **AppealCore** | Immutable claimant dossier, respondent rebuttal and one GenLayer AI assessment with substantive independent validator re-check |
| Second | `contracts/remedy_verify.py` — **RemedyVerify** | Reads only an UPHELD AppealCore ruling, checks digest and signer binding, runs distinct GenLayer corrective-action consensus and requires claimant's separate acceptance |

## One unified dispute-to-remediation workflow

AppealCore treats disputes as **adversarial, two-party evidence evaluation**, not arbitrary "AI decides X" classification. Claimant and respondent must be different wallets; an unopposed claim cannot become a default victory. Both submitted dossiers are frozen, hashed and evaluated against a custom equivalence validator. Outcomes are UPHELD / REJECTED / SPLIT / REVIEW. A decisive verdict requires validators to independently rerun the full 3-label assessment.

RemedyVerify is an independent corrective-action attestation primitive. It takes the **deployed address of AppealCore at construction** and reads its stored `get_ruling(case_id)` by `gl.get_contract_at(address).view()`. Only UPHELD rulings can be used. Each submitted remedy binds the exact original ruling hash, claimant/respondent identities and a canonical evidence-bundle hash. Validators independently check every all-PASS claim. **Even AI VERIFIED is not an executed remedy:** the original claimant must separately sign acceptance. Other decisions cannot be marked completed.

No token, legal enforcement, payout, automatic rollback or external data proof.

## Deploy and test with Studio

1. Deploy **AppealCore** from `contracts/appeal_core.py` without constructor args. Record the final on-chain address **A**.
2. Claimant opens a dispute with `open_case(respondent_address, claim_json)`; respondent separately calls `submit_response(case_id, response_json)`. Both must exist before `adjudicate(case_id)`. Exact JSON examples in `examples/studio_inputs.json`.
3. Obtain **FINALIZED / Accepted** for `adjudicate`; verify `get_case(id)` in Studio LATEST_FINAL. Test at least one UPHELD case and one REVIEW/REJECTED case without falsely claiming oracle truth.
4. Deploy **RemedyVerify** from `contracts/remedy_verify.py` with constructor argument `appeal_core_address="0x…"`, filling in the deployed address A (not a guessed placeholder).
5. Respondent uses `submit_remediation(case_id, action_summary, evidence_json, evidence_sha256)` where evidence hash is SHA-256 of canonical JSON. Then either original participant calls `assess_remediation(remediation_id)`.
6. Claimant separately signs `respond_to_remediation(remediation_id, accept, reason)` only after inspecting evidence and final receipt.
7. Read `get_remediation(id)` and check `ruling_sha256`, verdict, LATEST_FINAL and confirmed claimant response. Test wrong signer, malicious evidence and incomplete work.

## Verified Studionet demonstration — 18 November 2026

The following transactions are reported from actual **FINALIZED / Accepted / GenVM SUCCESS** GenLayer Studio receipts, not local mock-test outputs. The dispute/evidence content itself is **synthetic** and does not establish legal obligations or off-chain delivery.

**Unified deployment**

| Module (part of the same system) | Studionet contract |
|---|---|
| AppealCore — independent two-party dispute adjudication | [`0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2`](https://studio.genlayer.com/?import-contract=0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2) |
| RemedyVerify — ruling-bound corrective-action assessment and Claimant response | [`0x2138A278289A00Bae34c986B24b168800961B824`](https://studio.genlayer.com/?import-contract=0x2138A278289A00Bae34c986B24b168800961B824) |

**One full on-chain workflow, Case #2**

| Stage | On-chain outcome | Receipt |
|---|---|---|
| Claimant creates fictional dispute | Case ID **2** | [`open_case`](https://explorer-studio.genlayer.com/tx/0x98a6fdf19b227f6a72f0fd211c7900a9495589693160d48a109f1d9a8a7c64e6) |
| Independent Respondent rebuts | `BOTH_SIDES_LOCKED` | [`submit_response`](https://explorer-studio.genlayer.com/tx/0x748a8916a95b5c136b100353104acf75e63eef8d21dbcecbf0652abbd7ddb227) |
| GenLayer reviews the two-sided case | `UPHELD` | [`adjudicate`](https://explorer-studio.genlayer.com/tx/0xc39ed18ca758922395b0f5d71d538cbc7118061cd873e52242ccec831e2d0d8d) |
| RemedyVerify deployment binds the AppealCore address | **FINALIZED / SUCCESS** | [`deploy`](https://explorer-studio.genlayer.com/tx/0x221fd82b5fdc8982cc3babea7411190f9ba915be7db0e990ccfd797151512014) |
| Respondent submits SHA-256-bound synthetic remedy | Remediation ID **1** | [`submit_remediation`](https://explorer-studio.genlayer.com/tx/0xff05637fb77dea5303fc6ee247b2d4741c5ce631d6d0a1bf0d834ffc13f72389) |
| GenLayer checks remedy sufficiency | `INSUFFICIENT` (three REVIEW labels) | [`assess_remediation`](https://explorer-studio.genlayer.com/tx/0xf1861eb91518341979c5204f1b26e47840f15fc1341216cc9417cd229cf44684) |
| Original Claimant separately declines the insufficient remedy | **`DISPUTED`** | [`respond_to_remediation`](https://explorer-studio.genlayer.com/tx/0x2c89898ac324dac262e5554d08c56ea426739aa3a55bfc20f1d6b4a353fc87ce) |

**Final stored-state readback:** The user-supplied successful `get_remediation(1)` view confirms `status=ASSESSED`, `verdict=INSUFFICIENT`, `claimant_response=DISPUTED`, matching original case identities, the bound AppealCore address, the frozen ruling SHA-256 and canonical evidence SHA-256. Its [machine-readable fixture](examples/demo_remediation/remediation1_final_readback.json) and [integrity test](tests/test_remediation_readback_fixture.py) allow exact local reproduction. Studio's read status `Response (Accepted)` means only that the read succeeded; it is **not** a Claimant `ACCEPTED` response. This view was supplied by the user, not independently fetched over an authenticated `LATEST_FINAL` RPC endpoint.

**Separate conservative consensus example:** Case #1 `adjudicate(1)` returned [`REVIEW`](https://explorer-studio.genlayer.com/tx/0xcde19030edac6f9dc9bf25b3246308b7d50cf336d9e4221c7138e3d7f9d48880) and cannot yield an actionable UPHELD ruling.

**Security boundaries:** A `REVIEW`-only RemedyVerify consensus result is permitted by the deployed validator without independently re-running the semantic prompt; stronger all-PASS/FAIL claims use distinct independent validator checks. `INSUFFICIENT` forbids Claimant acceptance as a verified completion, even though a Claimant may register `DISPUTED`. This demonstration **does not** prove positive `VERIFIED` → `ACCEPTED`, external delivery, or legal enforcement.

See [complete linked on-chain execution evidence](docs/DEPLOYMENT_EVIDENCE.md), [synthetic evidence fixture](examples/demo_remediation/studio_submit_remediation.json), and [security/assurance model](docs/SECURITY_MODEL.md). Local Python CI is a separate contract-behavior shim, not live GenLayer consensus proof.

## Positive verification path — RemedyVerify V2 (not yet deployed)

**Submission is on hold until an actual `VERIFIED → ACCEPTED` path is executed or the limitation is explicitly resolved.** The finalized V1 demo correctly ended in `UPHELD → INSUFFICIENT → DISPUTED`, not successful correction.

To address the V1 evidence gap without weakening its conservative AI judgment, a **new source-only V2 verifier** is prepared at [`contracts/remedy_verify_v2.py`](contracts/remedy_verify_v2.py). It independently fetches two publicly accessible, commit-pinned artifacts from GitHub, verifies their full-file SHA-256, cross-checks the indexed source IDs and frozen Case #2 ruling, and then asks GenLayer AI to evaluate the *actual retrieved content*. All-PASS requires independent validator re-fetch and semantic recheck. Original Claimant approval is still separate.

- [Corrected Case #2 report](examples/positive_remediation/corrected_report.md) with six real Studionet transaction references.
- [Indexed source-evidence archive](examples/positive_remediation/indexed_source_archive.json) with exact transaction hashes, direct URLs and zero additional access fees.
- [Exact V2 Studio input JSON](examples/positive_remediation/studio_inputs_v2.json), with immutable GitHub commit URL and actual SHA-256 digests.
- [Step-by-step V2 deployment and positive-path runbook](docs/REMEDYVERIFY_V2_RUNBOOK.md).

**V2 is deployed** on Studionet at [`0x5C6d327F57f8A49E9c64872c64d8C5D04Aca9C48`](https://studio.genlayer.com/?import-contract=0x5C6d327F57f8A49E9c64872c64d8C5D04Aca9C48). A real Respondent-signed [`submit_remediation(2, …)`](https://explorer-studio.genlayer.com/tx/0xc42bf412c23aa271e07035c754fe0488e1504e5019cd3eda11a1c518956ba08e) returned **new V2 Remediation ID 1** (FINALIZED / Accepted / GenVM SUCCESS). This establishes the linked submission, **not** successful web fetching, AI verification or claimant approval. `assess_remediation(1)` remains **pending**, and the positive-path demonstration is NOT yet complete. Only actual accepted `VERIFIED` and separate original-Claimant-signed `ACCEPTED` can establish it. Local tests are shims and not network consensus evidence. A public file is evidence of availability, not independent proof of real-world recipient delivery.

## V2 incident and V3 fix (pending network verification)

The original V2 on-chain [`assess_remediation(1)`](https://explorer-studio.genlayer.com/tx/0x9fb07f5120fb11dbe233f337194c5558c568cbe70fc8f8a9d1cfde8a63e41bf8) was **FINALIZED / Accepted / GenVM SUCCESS**, but returned **`INSUFFICIENT`** with `REVIEW` for all three AI dimensions. The V2 code uses an incorrect `response.status_code` property on `gl.nondet.web.get` results; the official [GenLayer Response type](https://sdk.genlayer.com/main/_static/ai/api.txt) exposes `response.status` instead. Its broad exception handler converted this code error into `REVIEW`. Previous offline tests mistakenly modeled the nonexistent `status_code` field.

A corrected [`RemedyVerifyV3`](contracts/remedy_verify_v3.py) has been added **without changing historical V1 or V2 deployed contracts**. Its new [regression test](tests/test_remedyverify_v3.py) uses the SDK-shaped response and reproduces the V2 bug. **V3 is only a source candidate; it is not yet deployed.** Reuse the frozen AppealCore Case #2 ruling and [existing two content-addressed public artifacts](examples/positive_remediation/studio_inputs_v2.json) after verifying the new V3 deployment and method inputs. Read the [V3 runbook](docs/REMEDYVERIFY_V3_RUNBOOK.md).

A complete positive demonstration still requires genuine `VERIFIED` plus the original Claimant's separately signed `ACCEPTED`. No such result is currently claimed. We are not submitting the contribution prematurely.

## Test locally

```bash
python -m unittest discover -s tests -v
python -m py_compile contracts/*.py
```

See [Safety model](docs/SECURITY_MODEL.md), [GenLayer cross-contract views](https://docs.genlayer.com/developers/intelligent-contracts/features/interacting-with-intelligent-contracts), and [custom consensus validators](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle). MIT.
