"""Check only this public illustration's bytes, span and review linkage.

This is not an extraction algorithm, scientific evaluator or benchmark.
Python standard library only. Run from any directory.
"""
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(folder):
    folder = Path(folder)
    example = json.loads((folder / 'evidence.json').read_text(encoding='utf-8'))
    require(example['synthetic'] is True, 'Example must be explicitly synthetic')
    source_path = (folder / example['document']['text_file']).resolve()
    require(source_path.parent == folder.resolve(), 'Source must be in this example folder')
    raw = source_path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == example['document']['sha256'], 'Source hash mismatch')
    text = raw.decode('utf-8')
    span = example['evidence']['span']
    require(span['unit'] == 'Unicode code points' and span['end_exclusive'] is True, 'Unsupported span convention')
    require(0 <= span['start'] < span['end'] <= len(text), 'Invalid span bounds')
    require(text[span['start']:span['end']] == example['evidence']['quote'], 'Source span mismatch')
    require(example['review']['suggestion_id'] == example['suggestion']['id'], 'Broken review link')
    require(example['review']['decision'] == 'corrected', 'Expected an illustrative correction')
    require(example['suggestion']['label'] != example['review']['label'], 'Correction should leave the original different label intact')


if __name__ == '__main__':
    verify(Path(__file__).resolve().parent)
    print('PASS: source hash, exact span and separate suggestion/review linkage.')
    print('Synthetic illustration only: no extraction accuracy or scientific validity claim.')
