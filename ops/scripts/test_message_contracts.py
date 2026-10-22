#!/usr/bin/env python3
"""Source-declared mode contracts; no dws process or runtime validation."""
import importlib.machinery,importlib.util,json,pathlib,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from build_contracts import project_message_constraints
loader=importlib.machinery.SourceFileLoader('dwsdoc',str(ROOT/'bin/dwsdoc'));spec=importlib.util.spec_from_loader('dwsdoc',loader);doc=importlib.util.module_from_spec(spec);loader.exec_module(doc)
class MessageContractTest(unittest.TestCase):
 def check(self,tail):return doc.check_contract('dws chat +messages-send '+tail)
 def test_bot_singular_target_rejected_for_canonical_and_declared_alias(self):
  for flag in ['--as','--identity']:
   x=self.check(flag+' bot --robot-code CODE --open-dingtalk-id ID --markdown hi');self.assertFalse(x['declaration_check_pass']);self.assertTrue(any('source declared mode conflict' in e for e in x['errors']))
 def test_bot_required_credential_from_source(self):
  for missing in ['', '--robot-code ""']:
   self.assertFalse(self.check('--as bot --group GROUP --markdown hi '+missing)['declaration_check_pass'])
 def test_positive_source_forms_not_overblocked(self):
  for args in ['--as bot --robot-code CODE --group GROUP --markdown hi','--as bot --robot-code CODE --open-dingtalk-ids ID --markdown hi','--as user --open-dingtalk-id ID --markdown hi','--open-dingtalk-id ID --markdown hi']:
   self.assertTrue(self.check(args)['declaration_check_pass'],args)
 def test_slice_presence_matches_source_length_check(self):
  base='--as bot --robot-code CODE --group GROUP --markdown hi'
  # CSV [] is absent; [''] and ['', ''] still have a forbidden element.
  self.assertTrue(self.check(base+' --at-mobiles ""')['declaration_check_pass'])
  for value in ["'\"\"'", "','"]:
   x=self.check(base+' --at-mobiles '+value)
   self.assertFalse(x['declaration_check_pass'],value)
   self.assertTrue(any('不接受 --at-mobiles' in e for e in x['errors']))
 def test_partial_coverage_stays_explicit(self):
  x=self.check('--as user --group GROUP --markdown hi');self.assertEqual(x['runtime_validation'],'not executed');self.assertIn('not fully modeled',x['coverage'])
 def test_ambiguous_or_qualified_messages_stay_raw(self):
  source=['--mode sync 不接受 --danger','--mode sync 当离线时不接受 --danger','--mode other 不接受 --danger','--mode sync 不接受 特殊凭据','--mode sync 必须指定 --missing']
  out=project_message_constraints(source,{'mode':['sync']},{'mode','danger'});self.assertEqual(len(out),1);self.assertEqual(out[0]['source_message'],source[0])
if __name__=='__main__':unittest.main()
