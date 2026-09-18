# Validation evidence and its limits

Status: September 2026 development handoff. No independent scientific benchmark
is claimed in this showcase.

## Technical checks completed in the private implementation

| Area | Evidence | What it supports |
|---|---|---|
| Document and inventory pipeline | 46 synthetic pytest cases passed | Regression checks for structural and contract-level failure modes |
| Human-review persistence | Unit tests for revision conflicts, source identity, record separation and save/read behavior | Correct behavior on the tested storage scenarios |
| Browser interactions | JavaScript checks and browser exercises for page changes, shared evidence, category-specific controls and reload | Behavior of the exercised interface flows |
| Portable synthetic demonstration | Startup without research files or API keys; real HTTP save/reload | A working local demonstration, not just a visual design |
| Scientific coding workflow | Iterative human inspection of development publications | Discovery of ambiguous definitions and workflow problems |

The private test suite is not distributed here. The evidence example below is
intentionally small enough to inspect directly and independent of that suite.

## What you can verify in this public repository

Read `examples/source.txt` and `examples/evidence.json`. Then run:

```bash
python3 examples/verify_evidence.py
```

You can also run the four public artifact tests:

```bash
python3 -m unittest discover -s examples -p 'test_*.py'
```

They check the valid example and rejection of altered source bytes, a wrong span
and a broken review link. These four tests are separate from the 46 private
pipeline tests; they do not reproduce that suite.

The script checks the source's actual SHA-256 hash, an exact half-open Unicode
character span and the link between an unchanged suggestion and a separate
correction. The suggestion is deliberately wrong and both decisions are
handwritten for the demonstration. The object is an illustrative public format,
not the internal schema. The verifier uses Python's standard library and makes
no network or LLM calls.

These checks can reject a modified source file, invalid span or broken review
link. They do not validate the scientific correctness of the chosen labels.

## Still to establish

- Independent precision/recall and completeness across unseen publications.
- Interrater reliability and adjudication under a frozen coding protocol.
- Scientific validity of automated coherence judgments.
- Measured reviewer time savings and production-scale cost/reliability.
- Authenticated multiuser deployment and institutional operational safeguards.

Software regression tests, manual development review and scientific benchmarking
answer different questions. They should not be combined into an accuracy claim.
