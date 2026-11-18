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

**Separate conservative consensus example:** Case #1 `adjudicate(1)` returned [`REVIEW`](https://explorer-studio.genlayer.com/tx/0xcde19030edac6f9dc9bf25b3246308b7d50cf336d9e4221c7138e3d7f9d48880) and cannot yield an actionable UPHELD ruling.

**Security boundaries:** A `REVIEW`-only RemedyVerify consensus result is permitted by the deployed validator without independently re-running the semantic prompt; stronger all-PASS/FAIL claims use distinct independent validator checks. `INSUFFICIENT` forbids Claimant acceptance as a verified completion, even though a Claimant may register `DISPUTED`. This demonstration **does not** prove positive `VERIFIED` → `ACCEPTED`, external delivery, or legal enforcement.

See [complete linked on-chain execution evidence](docs/DEPLOYMENT_EVIDENCE.md), [synthetic evidence fixture](examples/demo_remediation/studio_submit_remediation.json), and [security/assurance model](docs/SECURITY_MODEL.md). Local Python CI is a separate contract-behavior shim, not live GenLayer consensus proof.

## Test locally

```bash
python -m unittest discover -s tests -v
python -m py_compile contracts/*.py
```

See [Safety model](docs/SECURITY_MODEL.md), [GenLayer cross-contract views](https://docs.genlayer.com/developers/intelligent-contracts/features/interacting-with-intelligent-contracts), and [custom consensus validators](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle). MIT.
