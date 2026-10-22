"""CLI serialization failures preserve a machine-readable result; no dws calls."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]


class ComposeCLITest(unittest.TestCase):
    def rejected(self, raw):
        proc = subprocess.run([sys.executable, '-B', str(ROOT / 'bin/dwsdoc'),
                               'compose', '--input', '-'], input=raw,
                              text=True, capture_output=True, check=False)
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(proc.stderr, '')
        data = json.loads(proc.stdout)
        self.assertFalse(data['declaration_check_pass'])
        self.assertIsNone(data['shell_text'])
        self.assertEqual(data['argv'], [])
        self.assertTrue(data['errors'])

    def test_unpaired_surrogates_remain_structured_errors(self):
        for payload in [
            {'path': '\ud800', 'flags': {}, 'source_commit': 'x'},
            {'path': 'chat +messages-send', 'flags': {'\ud800': 'x'}, 'source_commit': 'x'},
            {'path': 'chat +messages-send', 'flags': {}, 'source_commit': 'x', '\ud800': 'x'},
        ]:
            with self.subTest(payload=ascii(payload)):
                self.rejected(json.dumps(payload))

    def test_duplicate_json_keys_are_not_silently_replaced(self):
        self.rejected('{"path":"one","path":"two","flags":{}}')
        self.rejected('{"path":"chat +messages-send","flags":{"as":"user","as":"bot"}}')

    def test_malformed_json_is_a_structured_error(self):
        self.rejected('{"path":')

    def test_deeply_nested_input_is_a_structured_error(self):
        self.rejected('[' * 30000 + '0' + ']' * 30000)


if __name__ == '__main__':
    unittest.main()
