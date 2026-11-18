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
- This transaction proves the original claim was accepted and stored. The Respondent's separately signed response is documented below. No adjudication, UPHELD result or remediation has yet been established.

## Case #1 — authentic Respondent-signed rebuttal

- **TX:** [`0x49e5330c7b76cd21e55e87adcfc99ca04ae504e5e265ccf4c269c168bfd277f1`](https://explorer-studio.genlayer.com/tx/0x49e5330c7b76cd21e55e87adcfc99ca04ae504e5e265ccf4c269c168bfd277f1).
- User-provided Explorer receipt: **FINALIZED / Accepted / GenVM SUCCESS**; value 0 GEN; nonce 138.
- The independent Respondent/Agent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF` called `submit_response(1, response_json)` on the deployed AppealCore. Return value: **`BOTH_SIDES_LOCKED`**.
- Submitted rebuttal: `We contest the scope interpretation because the completed report was delivered and the source archive was intended as a separate deliverable.`
- Submitted `response_evidence`: `The signed delivery receipt names a report attachment but contains no specific confirmation of evidence archive delivery.`
- This establishes that distinct claimant and respondent wallets committed their respective synthetic narratives in the same on-chain case. It **does not** prove either narrative true, and **does not** imply an AI ruling.

## Next live test

1. Have an original participant call `adjudicate(1)` from AppealCore using **Normal (Full Consensus)**. Record the actual return value, accepted execution, and Equivalence Principle outputs.
2. Read `get_case(1)` at `LATEST_FINAL` and confirm state `DECIDED`, exact verdict and three labels.
3. Only a real `UPHELD` ruling makes `get_ruling(1)` actionable; then deploy and bind RemedyVerify to the **exact** AppealCore address above. For any other outcome, do not falsely claim actionable remediation.
4. Eventually verify both deployed sources against GitHub and test authentic cross-contract remediation and Claimant acknowledgment.

Local [CI](https://github.com/bearbaba/REMEDYQUORUM/actions) validates code with controlled GenLayer shims, not real remote consensus.
