# REMEDYQUORUM — Studio deployment and evidence runbook

**Target:** GenLayer Studionet. **Live status (18 November 2026):** AppealCore and original RemedyVerify V1 are deployed and a real synthetic Case #2 completed its negative outcome `UPHELD → INSUFFICIENT → DISPUTED`. The **positive** `VERIFIED → ACCEPTED` path has **not** been shown. A new V2 source is prepared, **not yet deployed**; use [V2 runbook](REMEDYVERIFY_V2_RUNBOOK.md) for any new positive-path attempt. Instructions below are the original V1 reproduction workflow, not proof of future results.

## Contract A: AppealCore

1. Open [GenLayer Studio](https://studio.genlayer.com/) and paste `contracts/appeal_core.py`. Deploy **AppealCore** without constructor parameters.
2. Record actual **address A** and the finalized deployment receipt. Check `stats()` for `name=APPEALCORE`, `version=1.0.0`.
3. From **Claimant wallet**, call `open_case(respondent_address, claim_json)` with a distinct **Respondent** wallet and editable claim:
```json
{"claim":"The service provider delivered the report without the agreed supporting evidence records in the signed written project scope.","requested_remedy":"Supply the missing verifiable evidence archive and a corrected report that contains reproducible source references.","claim_evidence":"The signed scope explicitly required original supporting records but the delivered file contained no evidence archive."}
```
4. Switch to **Respondent wallet**. Call `submit_response(case_id, response_json)`:
```json
{"response":"We contest the scope interpretation because the completed report was delivered and the source archive was intended as a separate deliverable.","response_evidence":"The signed delivery receipt names a report attachment but contains no specific confirmation of evidence archive delivery."}
```
5. Both claimant and respondent dossiers must exist before `adjudicate(case_id)`. Any party may initiate that method. Use Explorer to verify whether the validator consensus was *Accepted*, *Undetermined*, or *CANCELED*; do not equate a leader's UI answer with a finalized decision.
6. Read `get_case(case_id)` on `LATEST_FINAL`. Only an actual `UPHELD` result makes `get_ruling(case_id)` callable. A `REVIEW`, `REJECTED` or `SPLIT` case **must not** become an actionable ruling.

## Contract B: RemedyVerify

7. Paste `contracts/remedy_verify.py` into Studio. Set required constructor argument `appeal_core_address` to the **real deployed address A**. Deploy B. Check B `get_core()` and `stats()` match A.
8. From original **Respondent**, call `submit_remediation(case_id, action_summary, evidence_json, evidence_sha256)`. The required action summary refers to the exact remedial obligation returned by A; the evidence bundle consists of 1–8 objects of `kind`, `description` and an evidence `sha256`.
9. Save the evidence array as `evidence.json`; run `python scripts/hash_inputs.py evidence.json` to compute the canonical `evidence_sha256` argument. Use actual digests for the retained evidence sources. Evidence descriptions and digests alone do not prove external delivery.
10. Call `assess_remediation(remediation_id)`. Its independent AI criteria are remedy_match, evidence_completeness and remaining_violations, each PASS/FAIL/REVIEW. An all-PASS classification still awaits a separate claimant action.
11. From **Claimant**, call `respond_to_remediation(remediation_id, true, "I have reviewed and accepted the correction.")` **only if** result is `VERIFIED`. Use `false` and a substantive reason to dispute any assessed remedy. The original case ruling at A is not rewritten.

## Mandatory adversarial evidence

| Scenario | Outcome |
|---|---|
| Both parties provided their frozen case facts, decisive AI validator agreement | `UPHELD`, `REJECTED` or `SPLIT` depending on evidence (verify actual result) |
| Claimant alone attempts adjudication before response | Rejected; no default claimant victory |
| Model output ambiguous, missing fields, or injected keys | `REVIEW`; no actionable ruling |
| B attempts to verify an unapproved or non-UPHELD case | Rejected by A's view or B's source checks |
| B uses modified source ruling hash or wrong claimant address | Rejected; binding mismatch |
| Respondent supplies partial or insufficient proof | `INSUFFICIENT` / `FAILED` only after accepted consensus |
| Claimant tries to accept an unverified remediation | Rejected |
| Decisive label disagreement among validators | No accepted on-chain verdict; possible `UNDETERMINED` |

## Collect authentic proof

- A/B deployment and exact contract addresses
- Successful two-role claim and response receipts, plus accepted adjudication
- B read of A's actual ruling, accepted remediation consensus and separate Claimant response
- At least one negative-path proof, explicit outcome and no fabricated hashes
- Tests, declared limitations, deployed-source identity and `LATEST_FINAL` readback

## Submission draft (only AFTER actual verification)

**Title:** REMEDYQUORUM — Two-Sided AI Adjudication + Cross-Contract Remediation Verification

**Notes:** AppealCore requires independently signed claimant and respondent evidence before GenLayer validators can adjudicate a frozen case; decisive UPHELD/REJECTED/SPLIT labels require substantive independent consensus. Only an UPHELD ruling exposes a hashed actionable obligation. RemedyVerify is deployed with the real AppealCore address and verifies the live ruling, claimant/respondent identities, immutable evidence bundle and corrective-action consistency through its own AI consensus. The claimant must separately accept a verified remedy. The pair forms a reusable fail-closed dispute-to-remediation primitive; it does not enforce law, payments or external evidence truth.

**Evidence URL:** https://github.com/bearbaba/REMEDYQUORUM

**Submission:** one `Intelligent Contracts` slot for this paired suite.
