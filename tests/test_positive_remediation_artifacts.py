"""Validate the new *real public artifacts* for synthetic Case #2.

These documents reference genuine Studionet transactions but do not claim
a real customer delivery or a legally enforceable breach.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
F = ROOT / "examples" / "positive_remediation"

class ConcreteCorrectionArtifacts(unittest.TestCase):
    def test_report_and_archive_are_concrete_and_cross_referenced(self):
        report = (F / "corrected_report.md").read_text("utf-8")
        archive = json.loads((F / "indexed_source_archive.json").read_text("utf-8"))
        self.assertEqual(archive["case_id"], 2)
        self.assertEqual(archive["scope_clause"], "4.2")
        self.assertEqual(archive["additional_charge_usdc"], 0)
        self.assertEqual(archive["additional_charge_gen"], 0)
        self.assertFalse(archive["external_customer_delivery_proven"])
        self.assertEqual(
            archive["ruling_sha256"],
            "62a91466aef08aaca304c4a754e51fe45cce0587f9f12c879ad3c17c7a6594d0"
        )
        entries = archive["entries"]
        self.assertEqual(len(entries), 6)
        self.assertEqual(len(set(e["id"] for e in entries)), len(entries))
        for entry in entries:
            self.assertIn(entry["id"], report)
            self.assertTrue(re.fullmatch(r"0x[a-f0-9]{64}", entry["transaction_hash"]))
            self.assertEqual(
                entry["reference"],
                "https://explorer-studio.genlayer.com/tx/" + entry["transaction_hash"]
            )
        self.assertIn("public", report.lower())
        self.assertIn("no paywall", report.lower())
        self.assertIn("fictional", report.lower())

if __name__ == "__main__":
    unittest.main()
