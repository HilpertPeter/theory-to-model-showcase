"""Tests of the public illustration only, not the private research pipeline."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from verify_evidence import verify


class PublicArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)
        for name in ('source.txt', 'evidence.json'):
            shutil.copy2(Path(__file__).parent / name, self.folder / name)

    def tearDown(self):
        self.temp.cleanup()

    def change(self, edit):
        path = self.folder / 'evidence.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        edit(data)
        path.write_text(json.dumps(data), encoding='utf-8')

    def test_valid_example(self):
        verify(self.folder)

    def test_changed_source_rejected(self):
        (self.folder / 'source.txt').write_bytes(b'Changed source\n')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            verify(self.folder)

    def test_wrong_span_rejected(self):
        self.change(lambda d: d['evidence']['span'].update(start=0))
        with self.assertRaisesRegex(ValueError, 'span mismatch'):
            verify(self.folder)

    def test_broken_review_link_rejected(self):
        self.change(lambda d: d['review'].update(suggestion_id='unknown'))
        with self.assertRaisesRegex(ValueError, 'review link'):
            verify(self.folder)


if __name__ == '__main__':
    unittest.main()
