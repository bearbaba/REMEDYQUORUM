# REMEDYQUORUM

**One GenLayer Intelligent Contract project. One active dispute-to-remediation system.**

REMEDYQUORUM uses two linked Intelligent Contracts to resolve a two-sided synthetic dispute and evaluate a corrective-action submission. The workflow is governed by separately signed claimant and respondent actions, immutable SHA-256 commitments, GenLayer AI consensus and an explicit claimant confirmation gate.

| Active module | GenLayer Studionet deployment | Maintained source |
|---|---|---|
| **AppealCore** | [`0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2`](https://studio.genlayer.com/?import-contract=0x1f08cd694aC1bDd822F83e593f1ca719236FB5D2) | [`contracts/appeal_core.py`](contracts/appeal_core.py) |
| **RemedyVerify** | [`0x8c65c73187bBf575201d31a1270812e1D4BeD830`](https://studio.genlayer.com/?import-contract=0x8c65c73187bBf575201d31a1270812e1D4BeD830) | [`contracts/remedy_verify.py`](contracts/remedy_verify.py) |

**Important status (19 November 2026):** The active RemedyVerify deployment is shown as **Deployed** in the user's GenLayer Studio screenshot. A real [FINALIZED / Accepted / GenVM SUCCESS `submit_remediation(2, …)` transaction](https://explorer-studio.genlayer.com/tx/0x67f1879a9b3ddbb68b37953dcf5accfe7c20889844bb5b9b03919ea1f044e413) signed by the original Respondent returned **Remediation ID 1** on the active address. Its full deployment receipt, current read-only `get_core()` / `stats()` / `get_remediation(1)` output and AI assessment have not yet been supplied. **Do not claim `VERIFIED` or `ACCEPTED` yet.**

## How the single system works

1. Claimant calls `AppealCore.open_case(respondent, claim_json)`. Respondent must be a different wallet and independently provide `submit_response`.
2. GenLayer assesses the frozen two-sided dossier. Only a successful `UPHELD` outcome exposes the exact action request and ruling commitment to the downstream contract.
3. Respondent sends a corrected report and indexed evidence archive through `RemedyVerify.submit_remediation`, using pinned public URLs and SHA-256 values derived from the actual artifact bytes.
4. `RemedyVerify.assess_remediation` retrieves and hashes the commit-pinned documents and evaluates their content with GenLayer AI. `VERIFIED` is allowed only after the validator's independent all-PASS recheck.
5. Even a `VERIFIED` report is not a claimant approval. Only the original claimant can call `respond_to_remediation(id, true, reason)`, producing `ACCEPTED`. Inadequate evidence cannot be accepted.

### Existing live evidence

On the original AppealCore, synthetic **Case #2** is a genuine [FINALIZED, Accepted `UPHELD` ruling](https://explorer-studio.genlayer.com/tx/0xc39ed18ca758922395b0f5d71d538cbc7118061cd873e52242ccec831e2d0d8d). The accepted `get_ruling(2)` readback binds Claimant `0x4C7cb73aC8F8999af21cfc9fF4cF2333a9508Dcb`, Respondent `0xD6b8A3A5eB329410D9504784812b8569afA8C2aF` and ruling SHA-256 `62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0`.

The earlier unsuccessful corrective-action trials have been retired and are **not products, releases, recommended deployments or proof of successful correction**. Their actual negative receipts are retained only in [audit evidence](docs/DEPLOYMENT_EVIDENCE.md), so the historical record remains transparent.

## Current correction data

- [Corrected report](examples/positive_remediation/corrected_report.md) — real public file referring to six Studionet transactions.
- [Indexed evidence archive](examples/positive_remediation/indexed_source_archive.json) — numbered source IDs, full source links and explicit zero additional access fees.
- [Studio inputs](examples/positive_remediation/studio_inputs.json) — exact `case_id`, `action_summary`, `evidence_json` and `evidence_sha256` for the **current** verifier.
- [Studio runbook](docs/STUDIO_RUNBOOK.md) — read-only configuration checks first, then single-use live writes.

The underlying clause 4.2 agreement and delivery dispute are synthetic. Public documents and matching hashes prove content availability/integrity in this demo, **not** external delivery, legal enforcement or off-chain customer consent.

## Quality and verification

Run locally:

```bash
python -m unittest discover -s tests -v
python -m py_compile contracts/*.py
```

The tests use local GenLayer shims and are **not** an actual Studionet consensus receipt. Full state and security boundaries are in [security model](docs/SECURITY_MODEL.md) and [audit receipts](docs/DEPLOYMENT_EVIDENCE.md).

**Contribution status:** One unified Intelligent Contracts submission, **on hold until the real active RemedyVerify yields an auditable positive `VERIFIED → ACCEPTED` flow** or the remaining limitation is resolved.

*Repository file naming is canonical: one AppealCore, one RemedyVerify. A legacy internal class/metadata identifier retained inside the byte-identical deployed verifier source is not a product version or an invitation to deploy another module. Changing that identifier on-chain would require a separate signed deployment or upgrade.*
