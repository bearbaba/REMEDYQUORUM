# REMEDYQUORUM — Two-sided AI Disputes + Verified Corrective Action

**One GenLayer Intelligent Contract contribution, containing two interoperable and independently reusable Intelligent Contracts.**

| Deploy sequence | Contract | Purpose |
|---|---|---|
| First | `contracts/appeal_core.py` — **AppealCore** | Immutable claimant dossier, respondent rebuttal and one GenLayer AI assessment with substantive independent validator re-check |
| Second | `contracts/remedy_verify.py` — **RemedyVerify** | Reads only an UPHELD AppealCore ruling, checks digest and signer binding, runs distinct GenLayer corrective-action consensus and requires claimant's separate acceptance |

## Why these belong together

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

**Network status (18 Nov 2026):** AppealCore (first contract) is deployed on GenLayer Studionet at [`0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2`](https://studio.genlayer.com/?import-contract=0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2). A real Claimant-signed [`open_case`](https://explorer-studio.genlayer.com/tx/0x3af6eb6cef490a79c4d1cfb010e1e6816f707c461298988f0b6fa695123506f5) returned **Case ID 1** (FINALIZED / Accepted / GenVM SUCCESS). The separately signed Respondent [`submit_response(1)`](https://explorer-studio.genlayer.com/tx/0x49e5330c7b76cd21e55e87adcfc99ca04ae504e5e265ccf4c269c168bfd277f1) returned **`BOTH_SIDES_LOCKED`** (FINALIZED / Accepted / GenVM SUCCESS). The separately signed and accepted [`adjudicate(1)`](https://explorer-studio.genlayer.com/tx/0xcde19030edac6f9dc9bf25b3246308b7d50cf336d9e4221c7138e3d7f9d48880) returned **`REVIEW`** with `claim_support=SUPPORTED`, `counterevidence=DOES_NOT_REBUT`, `remedy_basis=REVIEW`. This is a genuine **non-actionable**, conservative GenLayer consensus result; no `UPHELD` ruling is available from Case #1. A separate [Claimant-signed Case #2 submission](https://explorer-studio.genlayer.com/tx/0x98a6fdf19b227f6a72f0fd211c7900a9495589693160d48a109f1d9a8a7c64e6) is now FINALIZED / Accepted / GenVM SUCCESS, returning **Case ID 2**. The bound Respondent's separately signed [`submit_response(2)`](https://explorer-studio.genlayer.com/tx/0x748a8916a95b5c136b100353104acf75e63eef8d21dbcecbf0652abbd7ddb227) returned **`BOTH_SIDES_LOCKED`** (FINALIZED / Accepted / GenVM SUCCESS). Its AI adjudication remains **pending**, with no assumed `UPHELD` outcome. RemedyVerify deployment and a full remediation workflow remain **pending**. See [Studionet execution evidence](docs/DEPLOYMENT_EVIDENCE.md). Unit tests are controlled local shims and are not live GenLayer consensus proof.

## Test locally

```bash
python -m unittest discover -s tests -v
python -m py_compile contracts/*.py
```

See [Safety model](docs/SECURITY_MODEL.md), [GenLayer cross-contract views](https://docs.genlayer.com/developers/intelligent-contracts/features/interacting-with-intelligent-contracts), and [custom consensus validators](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle). MIT.
