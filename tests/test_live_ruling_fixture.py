"""Offline SHA-256 reproduction of user-supplied synthetic GenLayer Case #2 ruling.
This does not attest to independent LATEST_FINAL RPC or real-world facts.
"""
import hashlib
import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "case2_upheld_ruling.json"

def digest(value):
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

class Case2OnChainRulingFixture(unittest.TestCase):
    def test_claim_and_ruling_sha256(self):
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        claim = data["claim"]
        ruling = data["ruling"]
        self.assertEqual(set(claim), {"claim", "claim_evidence", "requested_remedy"})
        self.assertEqual(ruling["contract"], "APPEALCORE")
        self.assertEqual(ruling["case_id"], 2)
        self.assertEqual(ruling["verdict"], "UPHELD")
        self.assertNotEqual(ruling["claimant"], ruling["respondent"])
        self.assertEqual(ruling["required_remedy"], claim["requested_remedy"])
        self.assertEqual(
            digest(claim),
            "eb84170fdd5d8febe7c58b7334ad0ec211b712f17daddadd896c4f7410d6baa9",
        )
        self.assertEqual(digest(claim), ruling["claim_sha256"])
        six_fields = (
            "case_id", "verdict", "claimant", "respondent",
            "claim_sha256", "required_remedy",
        )
        self.assertEqual(
            set(ruling), set(six_fields) | {"contract", "ruling_sha256"}
        )
        payload = {key: ruling[key] for key in six_fields}
        self.assertEqual(
            digest(payload),
            "62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0",
        )
        self.assertEqual(digest(payload), ruling["ruling_sha256"])

if __name__ == "__main__":
    unittest.main()
