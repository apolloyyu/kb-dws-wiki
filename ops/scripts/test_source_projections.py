#!/usr/bin/env python3
"""Offline tests for source envelope extraction; no model or network."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from build_note_sources import functions
class GoSourceEnvelopeTest(unittest.TestCase):
 def test_quoted_braces_comments_and_runes(self):
  source='''package example
func (x *Thing) Run() error {
 _ = "}"
 _ = '{'
 _ = `{}`
 /* } { */
 // }
 return nil
}
func Next() { _ = 1 }
'''
  rows=functions(source);self.assertEqual(len(rows),2)
  self.assertIn('return nil',rows[0]['source']);self.assertTrue(rows[0]['source'].endswith('}'))
  self.assertEqual(rows[1]['source'],'func Next() { _ = 1 }')
 def test_anonymous_types_are_not_function_bodies(self):
  source='func Make(x struct{ A int }) struct{ B int } { return struct{ B int }{x.A} }'
  self.assertEqual(functions("package example\n"+source)[0]['source'],source)
 def test_incomplete_source_does_not_claim_complete_function(self):
  self.assertEqual(functions('package example\nfunc Broken() { if true { return }'),[])
 def test_comment_between_signature_and_body_and_fake_declaration(self):
  source='package example\nvar text = `\nfunc Fake() {}\n`\n/*\nfunc AlsoFake() {}\n*/\nfunc Real() /* {} */ {}\n'
  rows=functions(source);self.assertEqual(len(rows),1);self.assertEqual(rows[0]['source'],'func Real() /* {} */ {}')
if __name__=='__main__':unittest.main()
