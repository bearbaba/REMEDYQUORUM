"""Verify user-supplied final Studionet state against submitted synthetic artifacts.

Does not independently query GenLayer, assert real-world delivery, or override
the separately signed ACCEPTED record.
"""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "examples" / "positive_remediation"

class PositiveLiveReadbackIntegrityTest(unittest.TestCase):
    def test_final_state_matches_pinned_inputs_and_ruling(self):
        state = json.loads((BASE / "final_accepted_state.json").read_text("utf-8"))
        inputs = json.loads((BASE / "studio_inputs.json").read_text("utf-8"))
        ruling = json.loads((ROOT / "examples" / "case2_upheld_ruling.json").read_text("utf-8"))["ruling"]
        self.assertEqual(state["source_contract_instance"], inputs["remedy_contract_address"].lower())
        self.assertEqual(state["original_appeal_core"], inputs["appeal_core_address"].lower())
        self.assertEqual(state["status"], "ASSESSED")
        self.assertEqual(state["verdict"], "VERIFIED")
        self.assertEqual(state["claimant_response"], "ACCEPTED")
        self.assertEqual(state["id"], 1)
        self.assertEqual(state["case_id"], inputs["case_id"])
        self.assertEqual(state["labels"], {
            "remedy_match": "PASS",
            "evidence_completeness": "PASS",
            "remaining_violations": "PASS",
        })
        self.assertEqual(state["claimant"], ruling["claimant"])
        self.assertEqual(state["respondent"], ruling["respondent"])
        self.assertEqual(state["claim_sha256"], ruling["claim_sha256"])
        self.assertEqual(state["ruling_sha256"], ruling["ruling_sha256"])
        self.assertEqual(state["evidence_sha256"], inputs["evidence_sha256"])
        evidence = json.loads(inputs["evidence_json"])
        canonical = json.dumps(evidence, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        self.assertEqual(hashlib.sha256(canonical.encode()).hexdigest(), state["evidence_sha256"])
        self.assertEqual(
            state["claimant_reason"],
            "I reviewed the corrected public report and indexed source archive, "
            "confirmed the linked digital demonstration deliverables, "
            "and accept the synthetic Case #2 correction."
        )
        for tx in state["transaction_hashes"].values():
            self.assertRegex(tx, r"^0x[0-9a-f]{64}$")

if __name__ == "__main__":
    unittest.main()
