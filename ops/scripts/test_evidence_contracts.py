"""Cross-product evidence boundaries and static contract checks; no dws execution."""
import importlib.util
import pathlib
import runpy
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'bin'))
import evidence_sections

DOC = runpy.run_path(str(ROOT / 'bin/dwsdoc'), run_name='contract_tests')


class EvidenceTest(unittest.TestCase):
    def test_long_section_retains_late_field_and_balanced_code(self):
        source = '# API\n## 背景\n' + 'background\n' * 120 + '\n## 请求\n```json\n{"lateField": 1}\n```\n'
        text, status = evidence_sections.select(source, 'lateField 的请求', 180)
        self.assertIn('{"lateField": 1}', text)
        self.assertEqual(text.count('```'), 2)
        self.assertEqual(status['coverage'], 'excerpt')

    def test_code_heading_is_not_a_document_heading(self):
        source = '# Contract\n## Example\n```markdown\n# fake section\n```\n## Limits\nlimit 10\n'
        parts = evidence_sections.units(source)
        self.assertEqual(len(parts), 2)
        self.assertIn('# fake section', parts[0]['body'])

    def test_oversized_table_has_header_and_explicit_partial(self):
        source = '# Fields\n| field | type |\n|---|---|\n' + ''.join(f'| item{i} | string |\n' for i in range(100)) + '| targetField | string |\n'
        text, status = evidence_sections.select(source, 'targetField', 300)
        self.assertIn('| field | type |', text)
        self.assertIn('| targetField | string |', text)
        self.assertIn('表格摘录', text)
        self.assertEqual(status['coverage'], 'excerpt')
        self.assertLessEqual(len(text), 350)

    def test_examples_bind_to_their_own_leaf(self):
        check = DOC['check_contract']
        wrong = check('dws chat +messages-send --as bot --robot-code <robotCode> --group <cid> --content hello')
        self.assertFalse(wrong['declaration_check_pass'])
        self.assertIn('content', wrong['unknown_indexed_flags'])
        good = check('dws chat +messages-send --as bot --robot-code <robotCode> --group <cid> --text hello')
        self.assertTrue(good['declaration_check_pass'], good)
        self.assertEqual(good['runtime_validation'], 'not executed')

    def test_profile_is_inherited_and_enum_is_not_free_text(self):
        self.assertTrue(DOC['check_contract']('dws auth login --profile corp:user')['declaration_check_pass'])
        bad = DOC['check_contract']('dws chat +messages-send --as invented --group <cid> --text hello')
        self.assertFalse(bad['declaration_check_pass'])

    def test_exclusive_content_is_rejected(self):
        bad = DOC['check_contract']('dws chat +messages-send --as user --group <cid> --text hello --markdown world')
        self.assertFalse(bad['declaration_check_pass'])

    def test_source_supplement_contains_bot_example_and_required_message(self):
        details = DOC['contract_details']()
        send = next(x for x in details['shortcuts'] if x['path'] == 'chat +messages-send')
        self.assertTrue(any('--as bot --robot-code' in x for x in send['examples']))
        self.assertIn('--identity bot 必须指定 --robot-code', send['validation_messages'])
        self.assertNotIn('content', send['enums'])

    def test_current_product_is_not_replaced_by_prior_assistant_suggestions(self):
        prior = '用户：数字员工可以查询哪些行为记录？\n助理：用 dws aisearch behavior，并创建数字员工。'
        q = '如何做到单聊或者群聊的实时回复'
        subjects = evidence_sections.previous_questions(prior)
        result = DOC['_intent'](q, subjects + '\n' + q)
        self.assertTrue(result['realtime_reply'])
        self.assertFalse(result['behavior_records'])
        self.assertFalse(result['access'])
        self.assertNotIn('aisearch', subjects)

    def test_elliptical_followup_can_inherit_user_subject(self):
        prior = '用户：dws auth status 显示 refresh_token 仍有效。\n助理：使用 --profile。'
        subject = evidence_sections.previous_questions(prior)
        self.assertIn('refresh_token', subject)
        self.assertNotIn('--profile', subject)
        self.assertEqual(evidence_sections.previous_questions('上一问原文'), '上一问原文')

    def test_log_fractional_seconds_are_not_a_software_version(self):
        self.assertFalse(DOC['_intent']('refresh_expires_at=2026-08-28T17:27:47.77788+08:00')['version'])
        self.assertTrue(DOC['_intent']('v1.0.64')['version'])

    def test_nested_table_is_deferred_without_losing_parent_scope(self):
        source = '# Schema\n| field | type |\n|---|---|\n'
        for n in range(25):
            source += f'| parent{n} | Object |\n| notification | Object |\n| notificationOff | Boolean |\n'
        text, status = evidence_sections.select(source, 'notificationOff', 400)
        self.assertIn('含嵌套对象', text)
        self.assertNotIn('| notificationOff |', text)
        self.assertEqual(status['coverage'], 'excerpt')

    def test_global_prefix_and_unknown_subcommand_are_distinct(self):
        check = DOC['check_contract']
        self.assertTrue(check('dws --profile corp:user auth login')['declaration_check_pass'])
        self.assertTrue(check('dws auth --profile corp:user login')['declaration_check_pass'])
        self.assertFalse(check('dws auth definitely-not-a-command')['declaration_check_pass'])

    def test_slice_enum_csv_and_repetition(self):
        check = DOC['check_contract']
        for command in ('dws minutes +detail --id uuid --artifacts basic,summary',
                        'dws minutes +detail --id uuid --artifacts basic --artifacts summary'):
            self.assertTrue(check(command)['declaration_check_pass'], check(command))
        self.assertFalse(check('dws minutes +detail --id uuid --artifacts basic,invented')['declaration_check_pass'])

    def test_shortcut_service_is_canonical_and_mismatch_blocks_build(self):
        sys.path.insert(0, str(ROOT / 'ops/scripts'))
        from build_dws_kb import shortcut_identity
        self.assertEqual(shortcut_identity('', 'Service: "minutes", Command: "+detail", CLIPath: "minutes +detail",'), ('minutes', '+detail'))
        with self.assertRaises(ValueError):
            shortcut_identity('', 'Service: "minutes", Command: "+detail", CLIPath: "smart +detail",')
        details = DOC['contract_details']()
        self.assertTrue(any(r['path'] == 'minutes +detail' for r in details['shortcuts']))
        self.assertFalse(any(r['path'] == 'smart +detail' for r in details['shortcuts']))

    def test_budget_retains_semantics_versions_and_whole_contracts(self):
        entries = ['== 命令契约: dws chat +messages-send ==\n' + 'flag\n' * 100,
                   '== 命令契约: dws chat +chat-messages ==\n' + 'flag\n' * 100,
                   '== 行为语义 ==\nimportant mechanism',
                   '== CHANGELOG ==\nv1.0.64 important release',
                   '== 检索审计 ==\naudit']
        result = DOC['pack_context'](entries, 900)
        self.assertLessEqual(len(result), 900)
        self.assertIn('important mechanism', result)
        self.assertIn('important release', result)
        self.assertIn('未展开完整单元', result)
        self.assertIn('dwsdoc contract', result)
        self.assertNotIn('总量截断', result)


if __name__ == '__main__':
    unittest.main()
