# REMEDYQUORUM — security and assurance model

REMEDYQUORUM is **one GenLayer workflow** composed of AppealCore and the **single active** RemedyVerify deployment, not a family of product releases.

- **Separate participants:** Claimant and Respondent must use different wallets. Only the named Respondent may respond or file a remedy; the original Claimant alone may accept or dispute.
- **Frozen record:** canonical SHA-256 binds the original claim and ruling, and separately binds the corrective evidence bundle and source file bytes.
- **Actionable upstream ruling:** only a frozen AppealCore `UPHELD` verdict can be used by RemedyVerify. Other judgments have no downstream remediation authorization.
- **Immutable source addresses:** corrective evidence consists of commit-pinned raw GitHub file URLs, not mutable branches or user-supplied summary text alone.
- **Actual content checks:** on `assess_remediation`, the verifier requests the full artifact bytes via GenLayer nondeterministic web access, checks response status and SHA-256, validates archive semantics and source IDs, and asks AI to inspect the fetched content.
- **Independent decisive consensus:** all-PASS or flagged FAIL claims require independent validator re-evaluation. REVIEW-only decisions are conservative but may be accepted without a second semantic run; REVIEW is never a completed remedy.
- **Final human gate:** AI `VERIFIED` is not claimant `ACCEPTED`. Only the original Claimant can submit acceptance; failure/insufficient verdicts cannot be accepted.
- **Honest boundaries:** file hashes prove integrity of submitted/public bytes, not external delivery, identity or legal compliance. The demo's clause 4.2 dispute is fictional.
- **Historical failed implementations:** not active, not recommended, not releases. Their on-chain effects cannot be erased; failure receipts remain in the audit ledger solely for traceability.
- **Deployed source identity:** the canonical repository verifier file preserves the actual deployment source content, including its internal class identifier. Cosmetic renaming would create a different artifact and cannot modify an already deployed on-chain contract.

Further evidence: [Studionet ledger](DEPLOYMENT_EVIDENCE.md), [live runbook](STUDIO_RUNBOOK.md).
