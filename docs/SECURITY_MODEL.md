# REMEDYQUORUM — Threat model and assurance boundary

1. **Two distinct participant wallets**: a claimant opens a case against another respondent. The respondent alone submits counterevidence. No default ruling on unopposed evidence; both submissions are required.
2. **Frozen commitments**: all claim evidence and response evidence are byte-bound by canonical SHA-256, independent of later AI reasoning. Model text never controls signers or source address.
3. **Decisive GenLayer consensus**: custom validator independently reruns three semantic criteria; exact match required for any UPHELD/REJECTED/SPLIT outcome. Invalid format normalizes to REVIEW. Leader-only verdict never becomes binding.
4. **Separate extension contract**: RemedyVerify stores AppealCore address at deployment, reads UPHELD rulings through deterministic view calls, verifies stable source marker, ruling digest and claimant/respondent. It cannot be repointed to another case registry by a caller.
5. **Independent remediation consensus**: three dimensions assess whether described actions match the frozen remedy, have sufficient evidence and leave unresolved violations. All-PASS requires validator independently reproducing all-PASS, even if explanatory prose differs.
6. **Human confirmation**: claimant must accept after VERIFIED. A respondent cannot declare its own remedy complete; no failed or insufficient remedy is marked accepted. Acceptance is an on-chain statement of claimant consent, not external proof of performance.
7. **Safe failure paths**: wrong signers, malformed evidence, forged ruling hashes, extra AI keys, missing response, ambiguous remedy, non-UPHELD ruling and repeat submission fail closed.
8. **Scope limits**: no legal arbitration force, personal identification, automated enforcement or real-world completeness proof. Claims/evidence may be false, selective or injected; digest only freezes submitted bytes. Production needs external identity and telemetry/oracle checks.
