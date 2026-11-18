"""Contract-independent Python test shim; NOT a live GenLayer consensus proof."""
import importlib.util
import hashlib
import json
import sys
import types
import unittest
from pathlib import Path

class UserError(Exception):pass
class Address:
    def __init__(self, s): self.as_hex=s.lower()
class TreeMap(dict):
    def __class_getitem__(cls, x):return cls
class UInt(int):pass
class Return:
    def __init__(self,x):self.calldata=x
class VM:
    Return=Return
    UserError=UserError
    def run_nondet_unsafe(self, leader, validator):
        x=leader()
        if not validator(Return(x)):raise RuntimeError("validator disagreement")
        return x
class Stub:pass
gl=Stub()
gl.Contract=type("Contract",(),{})
gl.public=Stub()
gl.public.write=lambda f:f
gl.public.view=lambda f:f
gl.vm=VM()
gl.message=Stub()
gl.message.sender_address=Address("0x"+"1"*40)
gl.nondet=Stub()
package=types.ModuleType("genlayer")
package.gl=gl;package.Address=Address;package.u256=UInt;package.TreeMap=TreeMap
sys.modules["genlayer"]=package
ROOT=Path(__file__).resolve().parents[1]
def load(name, path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
a=load("appeal_core","contracts/appeal_core.py")
b=load("remedy_verify","contracts/remedy_verify.py")
CLAIMANT="0x"+"1"*40
RESPONDENT="0x"+"2"*40
OUTSIDER="0x"+"3"*40
REGISTRY="0x"+"4"*40
CLAIM={"claim":"The service provider delivered a report without the supporting evidence promised under the accepted written project agreement.",
"requested_remedy":"Submit a corrected report with reproducible source references and the missing supporting evidence bundle.",
"claim_evidence":"The frozen project brief explicitly required supporting references, while the delivered report omitted the promised evidence archive."}
RESPONSE={"response":"The report was delivered under the original agreement but its source references might be incomplete.",
"response_evidence":"The upload receipt confirms one report attachment, while the source evidence archive was not recorded."}
def actor(x):gl.message.sender_address=Address(x)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def pass_case():
    return {"claim_support":"SUPPORTED","counterevidence":"DOES_NOT_REBUT","remedy_basis":"REQUIRED"}
def dismiss_case():
    return {"claim_support":"UNSUPPORTED","counterevidence":"REBUTS","remedy_basis":"NOT_REQUIRED"}
def proof():
    return [{"kind":"artifact","description":"A corrected report contains the previously omitted source references and indexed evidence archive.","sha256":"a"*64},
            {"kind":"receipt","description":"A proof receipt lists the delivered bundle and a timestamped claimant-facing transfer record.","sha256":"b"*64}]
class Linked:
    def __init__(self, registry):self.registry=registry
    def view(self):return self
    def get_ruling(self,id):return self.registry.get_ruling(id)
class Tests(unittest.TestCase):
    def setUp(self):
        actor(CLAIMANT)
        self.a=a.AppealCore();self.a.cases=TreeMap()
        self.id=self.a.open_case(RESPONDENT,canon(CLAIM))
        self.b=b.RemedyVerify(REGISTRY);self.b.remediations=TreeMap()
        gl.get_contract_at=lambda addr:Linked(self.a)
        self.answers=[]
        def ask(q,response_format=None):
            self.assertEqual(response_format,"json")
            self.assertTrue(self.answers,"unexpected additional LLM call")
            return self.answers.pop(0)
        gl.nondet.exec_prompt=ask
    def respond(self):
        actor(RESPONDENT)
        return self.a.submit_response(self.id,canon(RESPONSE))
    def upheld(self):
        self.respond()
        self.answers=[pass_case(),pass_case()]
        self.assertEqual(self.a.adjudicate(self.id),"UPHELD")
    def test_claim_opened_immutable_hash(self):
        record=json.loads(self.a.get_case(self.id))
        self.assertEqual(record["claim_sha256"],a.sha(a.canon(record["claim"])))
        self.assertEqual(record["status"],"OPEN")
    def test_response_requires_counterparty(self):
        with self.assertRaises(UserError):self.a.submit_response(self.id,canon(RESPONSE))
        self.respond()
        with self.assertRaises(UserError):self.a.submit_response(self.id,canon(RESPONSE))
    def test_no_automatic_one_sided_ruling(self):
        with self.assertRaises(UserError):self.a.adjudicate(self.id)
        with self.assertRaises(UserError):self.a.get_ruling(self.id)
    def test_upheld_decisive_requires_independent_agreement(self):
        self.upheld()
        ruling=json.loads(self.a.get_ruling(self.id))
        payload={k:ruling[k] for k in ("case_id","verdict","claimant","respondent","claim_sha256","required_remedy")}
        self.assertEqual(ruling["ruling_sha256"],a.sha(a.canon(payload)))
    def test_validator_disagreement_does_not_store_decision(self):
        self.respond();self.answers=[pass_case(),dismiss_case()]
        with self.assertRaises(RuntimeError):self.a.adjudicate(self.id)
        self.assertEqual(json.loads(self.a.get_case(self.id))["status"],"BOTH_SIDES_LOCKED")
    def test_bad_model_format_means_review_and_not_actionable(self):
        self.respond();self.answers=[{"wrong":"UPHELD"}]
        self.assertEqual(self.a.adjudicate(self.id),"REVIEW")
        with self.assertRaises(UserError):self.a.get_ruling(self.id)
    def test_rejected_ruling_cannot_be_used_for_remediation(self):
        self.respond();self.answers=[dismiss_case(),dismiss_case()]
        self.assertEqual(self.a.adjudicate(self.id),"REJECTED")
        actor(RESPONDENT)
        p=proof()
        with self.assertRaises(UserError):self.b.submit_remediation(self.id,"We have prepared all requested reference files and delivered a corrected report.",canon(p),b.sha(canon(p)))
    def test_remedy_pass_and_claimant_separate_acceptance(self):
        self.upheld();actor(RESPONDENT)
        p=proof();rid=self.b.submit_remediation(self.id,"We corrected the report and supplied the missing evidence archive with reproducible source references.",canon(p),b.sha(canon(p)))
        gl.nondet.exec_prompt=lambda *_a,**_kw:canon({k:"PASS" for k in b.CRITERIA})
        self.assertEqual(self.b.assess_remediation(rid),"VERIFIED")
        with self.assertRaises(UserError):self.b.respond_to_remediation(rid,True,"Thank you, agreed and verified.")
        actor(CLAIMANT)
        self.assertEqual(self.b.respond_to_remediation(rid,True,"The corrected report and evidence are satisfactory."),"ACCEPTED")
        with self.assertRaises(UserError):self.b.respond_to_remediation(rid,True,"Cannot approve twice.")
    def test_review_and_incomplete_evidence_cannot_be_accepted(self):
        self.upheld();actor(RESPONDENT);p=proof()
        rid=self.b.submit_remediation(self.id,"We may have updated the report but the supporting evidence archive is not available yet.",canon(p),b.sha(canon(p)))
        gl.nondet.exec_prompt=lambda *_a,**_kw:canon({k:"REVIEW" for k in b.CRITERIA})
        self.assertEqual(self.b.assess_remediation(rid),"INSUFFICIENT")
        actor(CLAIMANT)
        with self.assertRaises(UserError):self.b.respond_to_remediation(rid,True,"We accept incomplete evidence for now.")
        self.assertEqual(self.b.respond_to_remediation(rid,False,"Supporting documentation has not been provided."),"DISPUTED")
    def test_fake_ruling_hash_is_rejected(self):
        self.upheld();actor(RESPONDENT);p=proof()
        gl.get_contract_at=lambda addr:types.SimpleNamespace(view=lambda:types.SimpleNamespace(
         get_ruling=lambda id:canon(json.loads(self.a.get_ruling(id))|{"ruling_sha256":"0"*64})))
        with self.assertRaises(UserError):self.b.submit_remediation(self.id,"This is a detailed corrective action summary containing the latest references.",canon(p),b.sha(canon(p)))
    def test_wrong_evidence_bundle_hash_rejected(self):
        self.upheld();actor(RESPONDENT);p=proof()
        with self.assertRaises(UserError):self.b.submit_remediation(self.id,"We prepared the reference archive and updated the report for claimant review.",canon(p),"0"*64)
    def test_validator_disagreement_blocks_remedy_without_record_mutation(self):
        self.upheld();actor(RESPONDENT);p=proof()
        rid=self.b.submit_remediation(self.id,"We provided all missing files and a complete corrected project report to the claimant.",canon(p),b.sha(canon(p)))
        self.answers=[{k:"PASS" for k in b.CRITERIA},{k:"REVIEW" for k in b.CRITERIA}]
        with self.assertRaises(RuntimeError):self.b.assess_remediation(rid)
        self.assertEqual(json.loads(self.b.get_remediation(rid))["status"],"SUBMITTED")
    def test_unconfirmed_adverse_ai_fail_does_not_commit(self):
        self.upheld();actor(RESPONDENT);p=proof()
        rid=self.b.submit_remediation(self.id,"We provided the complete corrected report and supporting evidence archive.",canon(p),b.sha(canon(p)))
        failure={"remedy_match":"FAIL","evidence_completeness":"PASS","remaining_violations":"PASS"}
        success={k:"PASS" for k in b.CRITERIA}
        self.answers=[failure,success]
        with self.assertRaisesRegex(RuntimeError,"validator disagreement"):
            self.b.assess_remediation(rid)
        self.assertEqual(json.loads(self.b.get_remediation(rid))["status"],"SUBMITTED")
    def test_confirmed_negative_ai_can_record_failed(self):
        self.upheld();actor(RESPONDENT);p=proof()
        rid=self.b.submit_remediation(self.id,"An incomplete report was returned and the supporting evidence has not been delivered.",canon(p),b.sha(canon(p)))
        failure={"remedy_match":"FAIL","evidence_completeness":"PASS","remaining_violations":"PASS"}
        self.answers=[failure,failure]
        self.assertEqual(self.b.assess_remediation(rid),"FAILED")
        actor(CLAIMANT)
        with self.assertRaises(UserError):self.b.respond_to_remediation(rid,True,"We want to approve anyway.")
    def test_split_case_is_not_an_actionable_ruling(self):
        self.respond()
        split={"claim_support":"SUPPORTED","counterevidence":"REBUTS","remedy_basis":"REQUIRED"}
        self.answers=[split,split]
        self.assertEqual(self.a.adjudicate(self.id),"SPLIT")
        with self.assertRaises(UserError):self.a.get_ruling(self.id)
    def test_wrong_parties_cannot_adjudicate_or_submit_remedy(self):
        self.respond();actor(OUTSIDER)
        with self.assertRaises(UserError):self.a.adjudicate(self.id)
        actor(CLAIMANT);self.answers=[pass_case(),pass_case()]
        self.a.adjudicate(self.id)
        p=proof()
        with self.assertRaises(UserError):self.b.submit_remediation(self.id,"A completed correction and all evidence references were submitted for review.",canon(p),b.sha(canon(p)))
    def test_second_case_independent_from_first(self):
        actor(CLAIMANT)
        other=self.a.open_case(OUTSIDER,canon(CLAIM))
        self.assertNotEqual(other,self.id)
        self.assertEqual(json.loads(self.a.get_case(other))["status"],"OPEN")
if __name__=="__main__": unittest.main()
