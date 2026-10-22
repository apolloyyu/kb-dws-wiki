#!/usr/bin/env python3
"""Offline composition tests against the real index and declaration checker."""
import copy
import csv
import pathlib
import runpy
import shlex
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'bin'))
from command_examples import compose

DOC = runpy.run_path(str(ROOT / 'bin/dwsdoc'))
COMMANDS = DOC['load']('commands.jsonl')
SHORTCUTS = DOC['load']('shortcuts.jsonl')
DETAILS = DOC['contract_details']()
COMMIT = DETAILS['source_commit']


class CommandExamplesTest(unittest.TestCase):
    def compose(self, flags, path='chat +messages-send', **extra):
        payload = {'path': path, 'source_commit': COMMIT, 'flags': flags, **extra}
        return compose(payload, COMMANDS, SHORTCUTS, DETAILS, DOC['check_contract'])

    def assert_pass(self, result):
        self.assertTrue(result['declaration_check_pass'], result['errors'])
        self.assertEqual(shlex.split(result['shell_text']), result['argv'])
        self.assertEqual(result['runtime_validation'], 'not executed')
        self.assertIn('not fully modeled', result['coverage'])
        self.assertTrue(DOC['check_contract'](result['shell_text'])['declaration_check_pass'])

    def assert_rejected(self, result, error):
        self.assertFalse(result['declaration_check_pass'])
        self.assertEqual(result['argv'], [])
        self.assertIsNone(result['shell_text'])
        self.assertTrue(any(error in e for e in result['errors']), result['errors'])

    def test_bot_user_single_and_group_forms(self):
        forms = [
            {'as': 'bot', 'robot-code': '<robotCode>', 'open-dingtalk-ids': ['<openDingTalkId>']},
            {'as': 'bot', 'robot-code': '<robotCode>', 'group': '<conversationId>'},
            {'as': 'user', 'open-dingtalk-id': '<openDingTalkId>'},
            {'as': 'user', 'group': '<conversationId>'},
        ]
        for flags in forms:
            with self.subTest(flags=flags):
                self.assert_pass(self.compose({**flags, 'markdown': '回复内容'}))

    def test_known_bot_singular_target_is_rejected_after_full_check(self):
        for identity in ('as', 'identity'):
            self.assert_rejected(self.compose({identity: 'bot', 'robot-code': 'CODE',
                                              'open-dingtalk-id': 'ID', 'markdown': 'hi'}),
                                 'source declared mode conflict')

    def test_missing_and_empty_conditional_credential(self):
        for extra in ({}, {'robot-code': ''}):
            self.assert_rejected(self.compose({'as': 'bot', 'group': 'GROUP', 'text': 'hi', **extra}),
                                 'source declared mode conflict')

    def test_required_values_must_be_explicit_and_nonempty(self):
        for flags in ({'start': '2026-01-01', 'end': '2026-01-02'},
                      {'users': [], 'start': '2026-01-01', 'end': '2026-01-02'},
                      {'users': ['ID'], 'start': '', 'end': '2026-01-02'}):
            self.assert_rejected(self.compose(flags, 'attendance +check-result'), 'required')
        self.assert_rejected(self.compose({'file': ''}, 'aicard preview'), 'required')

    def test_source_default_identity_does_not_inject_presence(self):
        result = self.compose({'open-dingtalk-id': '<ID>', 'markdown': 'hi'})
        self.assert_pass(result)
        self.assertEqual(result['effective_flags']['identity'], 'user')
        self.assertEqual(result['source_defaults']['identity'], 'user')
        self.assertFalse(any(token.startswith('--identity=') for token in result['argv']))
        self.assertNotIn('timeout', result['source_defaults'])

    def test_root_and_leaf_defaults_use_declared_metadata_with_leaf_precedence(self):
        commands, details = copy.deepcopy(COMMANDS), copy.deepcopy(DETAILS)
        next(f for f in details['root_flags'] if f['name'] == 'token')['default'] = 'root-token'
        next(f for f in details['root_flags'] if f['name'] == 'timeout')['default'] = 30
        leaf = next(r for r in commands if r['cmd'] == 'auth login')
        next(f for f in leaf['flags'] if f['name'] == 'token')['default'] = 'leaf-token'
        result = compose({'path': 'auth login', 'source_commit': COMMIT, 'flags': {}},
                         commands, SHORTCUTS, details, DOC['check_contract'])
        self.assert_pass(result)
        self.assertEqual(result['effective_flags']['token'], 'leaf-token')
        self.assertEqual(result['effective_flags']['timeout'], 30)
        self.assertEqual(result['argv'], ['dws', 'auth', 'login'])

    def test_declared_aliases_normalize_and_equal_values_deduplicate(self):
        result = self.compose({'as': 'user', 'identity': 'user', 'chat-id': '<GROUP>',
                               'group': '<GROUP>', 'markdown': 'hi', 'f': 'json'})
        self.assert_pass(result)
        self.assertEqual(result['argv'].count('--identity=user'), 1)
        self.assertEqual(result['argv'].count('--group=<GROUP>'), 1)
        self.assertIn('--format=json', result['argv'])

    def test_conflicting_aliases_are_not_resolved_by_input_order(self):
        for flags in ({'as': 'bot', 'identity': 'user'}, {'identity': 'user', 'as': 'bot'},
                      {'chat-id': 'A', 'group': 'B'}, {'f': 'json', 'format': 'table'}):
            self.assert_rejected(self.compose({'markdown': 'hi', **flags}), 'conflicting alias/canonical')

    def test_empty_csv_and_one_empty_item_have_distinct_mode_semantics(self):
        base = {'as': 'bot', 'robot-code': 'CODE', 'group': 'GROUP', 'text': 'hi'}
        for value in ([], ''):
            result = self.compose({**base, 'at-mobiles': value})
            self.assert_pass(result)
            self.assertIn('--at-mobiles=', result['argv'])
        for value in ([''], ['', ''], '""', ','):
            self.assert_rejected(self.compose({**base, 'at-mobiles': value}), 'source declared mode conflict')

    def test_csv_list_values_round_trip(self):
        values = ['one,two', '"quote"', '<ID>', 'line\nbreak', '', 'plain']
        result = self.compose({'as': 'bot', 'robot-code': 'CODE', 'open-dingtalk-ids': values, 'text': 'hi'})
        self.assert_pass(result)
        token = next(t for t in result['argv'] if t.startswith('--open-dingtalk-ids='))
        self.assertEqual(next(csv.reader([token.split('=', 1)[1]], strict=True)), values)
        self.assertEqual(result['normalized_flags']['open-dingtalk-ids'], values)

    def test_csv_rejects_records_or_characters_that_cannot_round_trip(self):
        for value in ('one\ntwo', '"unclosed', ['a\r\nb'], [None], [123]):
            self.assert_rejected(self.compose({'as': 'bot', 'robot-code': 'CODE', 'text': 'hi',
                                              'open-dingtalk-ids': value}), '--open-dingtalk-ids')

    def test_shell_metacharacters_are_literal_arguments(self):
        literal = '--flag $(touch /tmp/never) `whoami` ; echo x\n\'single\' "double" <placeholder> \\ end'
        result = self.compose({'open-dingtalk-id': '<ID>', 'markdown': literal})
        self.assert_pass(result)
        self.assertIn('--markdown=' + literal, shlex.split(result['shell_text']))
        self.assertIn("'--markdown=", result['shell_text'])

    def test_full_command_is_checked_once(self):
        seen = []
        def checker(text):
            seen.append(text)
            return DOC['check_contract'](text)
        result = compose({'path': 'chat +messages-send', 'source_commit': COMMIT,
                          'flags': {'open-dingtalk-id': '<ID>', 'text': 'hi'}},
                         COMMANDS, SHORTCUTS, DETAILS, checker)
        self.assert_pass(result)
        self.assertEqual(seen, [result['shell_text']])

    def test_only_declared_numeric_and_bool_types_accept_nonstring_values(self):
        result = self.compose({'open-dingtalk-id': 'ID', 'text': 'hi', 'expires-seconds': 12,
                               'dry-run': True, 'at-all': False, 'timeout': '0x1e'})
        self.assert_pass(result)
        self.assertIn('--at-all=false', result['argv'])
        self.assertIn('--timeout=30', result['argv'])
        for name, value in (('open-dingtalk-id', 123), ('text', True), ('text', None),
                            ('text', {}), ('expires-seconds', True), ('expires-seconds', 1.2),
                            ('expires-seconds', '08'), ('expires-seconds', 2 ** 80),
                            ('dry-run', 'maybe'), ('dry-run', 1)):
            self.assert_rejected(self.compose({'open-dingtalk-id': 'ID', 'text': 'hi', name: value}), '--' + name)

    def test_float_type_accepts_finite_numbers_only(self):
        for value in (0.25, '1e-2'):
            self.assert_pass(self.compose({'limit': value}, 'minutes list mine'))
        for value in (float('nan'), float('inf'), {}, True, 'bad'):
            self.assert_rejected(self.compose({'limit': value}, 'minutes list mine'), '--limit')

    def test_unknown_flags_and_unmodeled_types_are_rejected(self):
        self.assert_rejected(self.compose({'made-up': 'x', 'markdown': 'hi'}), 'unknown indexed flag')
        self.assert_rejected(self.compose({'idle-timeout': '1s'}, 'event _bus'), 'unsupported declared type')
        self.assert_rejected(self.compose({'attachment': ['a', 'b']}, 'mail draft create'), 'unsupported declared type')

    def test_final_checker_retains_declared_enum_and_exclusion_rules(self):
        self.assert_rejected(self.compose({'as': 'invented', 'markdown': 'hi'}), 'enum mismatch')
        self.assert_rejected(self.compose({'open-dingtalk-id': 'ID', 'text': 'one', 'markdown': 'two'}),
                             'constraint mismatch')

    def test_version_mismatch_missing_version_and_mixed_supplement(self):
        self.assert_rejected(self.compose({'markdown': 'hi'}, source_commit='wrong'), 'source version mismatch')
        payload = {'path': 'chat +messages-send', 'flags': {'markdown': 'hi'}}
        self.assert_rejected(compose(payload, COMMANDS, SHORTCUTS, DETAILS, DOC['check_contract']), 'source version mismatch')
        details = copy.deepcopy(DETAILS)
        next(r for r in details['shortcuts'] if r['path'] == payload['path'])['source_commit'] = 'other'
        self.assert_rejected(compose({**payload, 'source_commit': COMMIT}, COMMANDS, SHORTCUTS, details,
                                     DOC['check_contract']), 'selected_contract')

    def test_version_claim_is_scoped_to_actual_metadata(self):
        result = self.compose({'open-dingtalk-id': 'ID', 'markdown': 'hi'})
        self.assert_pass(result)
        self.assertEqual(result['source_commit'], COMMIT)
        self.assertEqual(result['source_versions']['selected_contract'], COMMIT)
        self.assertIsNone(result['source_versions']['selected_index_row'])

    def test_path_requires_exact_leaf_and_positionals_are_explicitly_unsupported(self):
        for path in ('chat', 'chat +messages-sen', 'dws chat +messages-send', 'chat  +messages-send',
                     'chat +messages-send --as bot'):
            self.assertFalse(self.compose({}, path)['declaration_check_pass'])
        self.assert_rejected(self.compose({}, 'event consume', args=['event_key']), 'positional args unsupported')

    def test_invalid_input_shape_and_unrepresentable_arguments(self):
        for payload in (None, [], 'dws chat +messages-send', {'path': 'chat +messages-send', 'flags': []}):
            self.assertFalse(compose(payload, COMMANDS, SHORTCUTS, DETAILS, DOC['check_contract'])['declaration_check_pass'])
        for value in ('bad\x00arg', '\ud800'):
            self.assert_rejected(self.compose({'markdown': value}), 'not representable')
        self.assert_rejected(self.compose({'markdown': 'hi'}, shell='echo unexpected'), 'unknown input fields')

    def test_final_checker_failure_cannot_publish_a_command(self):
        result = compose({'path': 'chat +messages-send', 'source_commit': COMMIT,
                          'flags': {'open-dingtalk-id': 'ID', 'text': 'hi'}},
                         COMMANDS, SHORTCUTS, DETAILS,
                         lambda _: {'declaration_check_pass': False, 'errors': ['injected checker conflict']})
        self.assert_rejected(result, 'injected checker conflict')


if __name__ == '__main__':
    unittest.main()
