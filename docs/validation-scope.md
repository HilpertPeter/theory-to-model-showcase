# Validation evidence and its limits

**Updated November 2026.** This page distinguishes a functioning research
prototype from independently demonstrated scientific performance.

## What has been exercised

| Evidence | What it supports | What it does not establish |
|---|---|---|
| Local coding and review workflows | Source inspection, separate human decisions and an operational supervised process | A hosted, production-ready multiuser service |
| September technical handoff: 46 synthetic pipeline tests, with additional interface and persistence checks | Behavior on documented document-processing and storage failure cases | Accuracy of scientific classifications on unseen papers |
| November technical handoff: 25 synthetic checks for evidence contracts and a coherence-to-report demo | Evidence integrity, scope handling and behavior on explicit contrast scenarios | General causal validity or autonomous paper-review accuracy |
| Iterative expert review of development material | Identification of ambiguous cases and improvements to rules and presentation | Independent human–AI or human–human reliability |
| Small evidence-graph and agent-style review experiments | Feasibility of linked retrieval, critique and recorded revision | Superiority over a simpler serial workflow |

The September and November counts refer to different, dated test runs. They are
not a combined performance score. The private implementation and its test suites
are not distributed in this portfolio.

## What the public examples demonstrate

The screenshots show a working local interface using invented material. The
[review example](review-example.md) is a handwritten illustration of useful
feedback. It is not a model prediction, an annotation from a real study, or an
independent reference judgment. The diagrams summarize product behavior without
publishing the internal decision procedure.

## Next evaluation milestones

- Freeze a compatible rule and software version before testing on new material.
- Obtain independent annotations with adequate source context and retain the
  first answers separately from adjudication.
- Measure missed evidence and false findings, not just agreement on selected cases.
- Compare serial processing, graphs and bounded adaptive checking with matched
  inputs and explicit resource budgets.
- Measure cost, elapsed time and human-review minutes alongside quality.
- Test whether reviewers understand the findings and find the suggested revisions useful.

Human discussion has been valuable for development. Agreement after that
conversation cannot be treated as an independent accuracy estimate. Confidence
signals also require calibration before they can justify unattended acceptance.
