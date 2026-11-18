"""Verify real bytes of synthetic demo remedy fixtures and Studio calldata hash.

These files are illustrative and do not prove external delivery or claimant consent.
"""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "examples" / "demo_remediation"

def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)

class Case2RemediationDemo(unittest.TestCase):
    def test_fixture_and_bundle_digests(self):
        inputs = json.loads((DIR / "studio_submit_remediation.json").read_text("utf-8"))
        self.assertEqual(inputs["case_id"], 2)
        self.assertTrue(inputs["action_summary"].startswith("For the synthetic Case #2"))
        evidence = json.loads(inputs["evidence_json"])
        self.assertEqual(len(evidence), 2)
        self.assertTrue(all(item["kind"] == "artifact" for item in evidence))
        self.assertEqual(
            sha_bytes((DIR / "corrected_report.md").read_bytes()),
            "e609fd0b96ea65c21781db4f93817c72691e89642519f99c5e3d679a60a396e4"
        )
        self.assertEqual(evidence[0]["sha256"], sha_bytes((DIR / "corrected_report.md").read_bytes()))
        self.assertEqual(
            sha_bytes((DIR / "source_archive.json").read_bytes()),
            "1cbe9e5cda4fc30209f85c0312b9e719ca6b15310cdace635894fe295a4e7bee"
        )
        self.assertEqual(evidence[1]["sha256"], sha_bytes((DIR / "source_archive.json").read_bytes()))
        self.assertEqual(
            sha_bytes(canonical(evidence).encode("utf-8")),
            "e4cc82d7c0418b16ef1c4561764772e3e6296bcbd792b93f5fe90a0a5ce9ee66"
        )
        self.assertEqual(inputs["evidence_sha256"], sha_bytes(canonical(evidence).encode("utf-8")))

if __name__ == "__main__":
    unittest.main()
