"""Offline tests for the deployed canonical RemedyVerify pinned-public-artifact evidence gates.

The test stubs actual GenLayer web/consensus execution and does NOT count as
a real Studionet VERIFIED or Claimant ACCEPTED receipt.
"""
import hashlib
import json
import unittest
from pathlib import Path

import test_remedyquorum as t

ROOT = Path(__file__).resolve().parents[1]
CORRECTED = ROOT / "examples" / "positive_remediation" / "corrected_report.md"
ARCHIVE = ROOT / "examples" / "positive_remediation" / "indexed_source_archive.json"
INPUTS = ROOT / "examples" / "positive_remediation" / "studio_inputs.json"
CASE_FIXTURE = ROOT / "examples" / "case2_upheld_ruling.json"
CLAIMANT = "0x4c7cb73ac8f8999af21cfc9ff4cf2333a9508dcb"
RESPONDENT = "0xd6b8a3a5eb329410d9504784812b8569afa8c2af"
CORE = "0x1f08cd694ac1bdd822f83e593f1ca719236fb5d2"
active = t.load("remedy_verify", "contracts/remedy_verify.py")

class FakeWebResponse:
    def __init__(self, content):
        self.status = 200
        self.body = content

class RemedyVerifyTests(unittest.TestCase):
    def setUp(self):
        self.inputs = json.loads(INPUTS.read_text(encoding="utf-8"))
        self.report = CORRECTED.read_bytes()
        self.archive = ARCHIVE.read_bytes()
        self.evidence = json.loads(self.inputs["evidence_json"])
        t.actor(CLAIMANT)
        self.a = t.a.AppealCore()
        self.a.cases = t.TreeMap()
        c = json.loads(CASE_FIXTURE.read_text(encoding="utf-8"))["claim"]
        # Seed a first case so the actual frozen synthetic case has Case ID 2.
        self.a.open_case(RESPONDENT, t.canon(t.CLAIM))
        self.case_id = self.a.open_case(RESPONDENT, t.canon(c))
        self.assertEqual(self.case_id, 2)
        t.actor(RESPONDENT)
        self.a.submit_response(self.case_id, t.canon(t.RESPONSE))
        t.gl.nondet.exec_prompt = lambda prompt, response_format=None: (
            t.canon(t.pass_case()) if "claim_support" in prompt else
            t.canon({k: "PASS" for k in active.CRITERIA})
        )
        self.assertEqual(self.a.adjudicate(self.case_id), "UPHELD")
        t.gl.get_contract_at = lambda address: t.Linked(self.a)
        self.b = active.RemedyVerifyV3(CORE)
        self.b.remediations = t.TreeMap()
        class Web:
            def __init__(webself):
                webself.overrides = {}
                webself.urls_called = []
            def get(webself, url):
                webself.urls_called.append(url)
                content = webself.overrides.get(url)
                if content is None:
                    content = self.report if url.endswith("/corrected_report.md") else self.archive
                return FakeWebResponse(content)
        self.web = Web()
        t.gl.nondet.web = self.web

    def submit(self, evidence=None):
        docs = self.evidence if evidence is None else evidence
        bundle = t.canon(docs)
        return self.b.submit_remediation(
            self.case_id, self.inputs["action_summary"],
            bundle, hashlib.sha256(bundle.encode("utf-8")).hexdigest()
        )

    def test_mock_matches_official_response_api(self):
        response = FakeWebResponse(self.report)
        self.assertEqual(response.status, 200)
        self.assertFalse(hasattr(response, "status_code"))

    def test_real_fixture_digest_and_pinned_urls(self):
        self.assertEqual(
            hashlib.sha256(self.report).hexdigest(),
            "34b5c2767143b3a69dd9db4b0460d4489cc24ca13db9bedbb62862bc5350b741"
        )
        self.assertEqual(
            hashlib.sha256(self.archive).hexdigest(),
            "da1960d26982394dbf08d8ac70ac3b3be1907e0cc9ac0791d8e8a8f9ef0cbca6"
        )
        self.assertEqual(self.inputs["evidence_sha256"], hashlib.sha256(
            self.inputs["evidence_json"].encode("utf-8")
        ).hexdigest())
        self.assertTrue(all(
            self.inputs["positive_artifact_commit"] in e["url"] for e in self.evidence
        ))

    def test_complete_artifacts_can_pass_twice_and_claimant_accept(self):
        rid = self.submit()
        self.assertEqual(rid, 1)
        self.assertEqual(self.b.assess_remediation(rid), "VERIFIED")
        self.assertEqual(len(self.web.urls_called), 4)  # Leader and validator independently fetch both.
        with self.assertRaises(t.UserError):
            self.b.respond_to_remediation(rid, True, "Respondent self-approval must fail")
        t.actor(CLAIMANT)
        self.assertEqual(
            self.b.respond_to_remediation(
                rid, True, "I inspected the publicly available corrected report and indexed archive."
            ), "ACCEPTED"
        )

    def test_changed_remote_artifact_fails_closed(self):
        rid = self.submit()
        self.web.overrides[self.evidence[0]["url"]] = b"tampered report bytes"
        self.assertEqual(self.b.assess_remediation(rid), "INSUFFICIENT")
        t.actor(CLAIMANT)
        with self.assertRaises(t.UserError):
            self.b.respond_to_remediation(
                rid, True, "I am attempting to accept a non-verified remedy."
            )

    def test_mutable_url_or_duplicate_roles_rejected(self):
        docs = [dict(x) for x in self.evidence]
        docs[0]["url"] = docs[0]["url"].replace(
            self.inputs["positive_artifact_commit"], "main"
        )
        with self.assertRaises(t.UserError):
            self.submit(docs)
        docs = [dict(x) for x in self.evidence]
        docs[1]["role"] = "corrected_report"
        with self.assertRaises(t.UserError):
            self.submit(docs)

if __name__ == "__main__":
    unittest.main()
