"""Offline integrity checks against user-supplied Studio get_remediation(1) output.

This is a fixture of a user-provided contract view, not an independently executed
GenLayer LATEST_FINAL query or proof of external delivery.
"""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "examples" / "demo_remediation"

def digest_canonical(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")).hexdigest()

class FinalizedRemediationReadbackFixture(unittest.TestCase):
    def test_saved_onchain_view_links_to_immutable_inputs(self):
        item = json.loads((DEMO / "remediation1_final_readback.json").read_text(encoding="utf-8"))
        submitted = json.loads((DEMO / "studio_submit_remediation.json").read_text(encoding="utf-8"))
        ruling = json.loads((ROOT / "examples" / "case2_upheld_ruling.json").read_text(encoding="utf-8"))["ruling"]
        self.assertEqual(item["id"], 1)
        self.assertEqual(item["case_id"], 2)
        self.assertEqual(item["status"], "ASSESSED")
        self.assertEqual(item["verdict"], "INSUFFICIENT")
        self.assertEqual(item["claimant_response"], "DISPUTED")
        self.assertEqual(item["labels"], {
            "remedy_match": "REVIEW",
            "evidence_completeness": "REVIEW",
            "remaining_violations": "REVIEW",
        })
        self.assertEqual(item["claimant_reason"], (
            "The submitted synthetic artifacts do not establish independently confirmed "
            "delivery or complete fulfillment of clause 4.2. Additional verifiable "
            "evidence is required."
        ))
        self.assertEqual(item["source_contract"], "0x1f08cd694ac1bdd822f83e593f1ca719236fb5d2")
        self.assertEqual(item["claimant"], ruling["claimant"])
        self.assertEqual(item["respondent"], ruling["respondent"])
        self.assertEqual(item["claim_sha256"], ruling["claim_sha256"])
        self.assertEqual(item["ruling_sha256"], ruling["ruling_sha256"])
        self.assertEqual(item["required_remedy"], ruling["required_remedy"])
        self.assertEqual(item["action_summary"], submitted["action_summary"])
        self.assertEqual(item["evidence"], json.loads(submitted["evidence_json"]))
        self.assertEqual(item["evidence_sha256"], submitted["evidence_sha256"])
        self.assertEqual(item["evidence_sha256"], digest_canonical(item["evidence"]))

if __name__ == "__main__":
    unittest.main()
