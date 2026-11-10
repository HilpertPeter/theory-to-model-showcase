# Theory-to-Model — Evidence-Linked AI Review

**Peter Hilpert · Applied AI project lead & domain architect**

**Research prototype · November 2026**

![Theory-to-Model: turning research documents into reviewable reasoning](assets/overview.svg)

I turn a complex scientific-review problem into a working AI-assisted workflow:
organize research documents, connect claims to their sources, support expert
judgment, and present findings that a reviewer can act on.

**My role:** problem formulation, domain modeling, workflow architecture,
human-review experience, error analysis and validation design. I use AI-assisted
implementation to build and refine the prototype, with explicit tests and human
checks at the points where judgment matters.

[See a review example](docs/review-example.md) ·
[Explore the architecture work](docs/architecture-exploration.md) ·
[Check the evidence and limits](docs/validation-scope.md)

## The problem

A paper's argument is distributed across its introduction, methods, analyses and
conclusions. A useful review must connect those pieces: what was intended, what
was actually examined, and what the findings can support. An isolated comment
or a fluent summary can miss the gap between them.

Theory-to-Model addresses that gap within the broader **Internal Coherence
Framework (ICF)** research programme. The initial application is observational
psychology, with a longer-term interest in other empirical research domains.

## From document processing to useful feedback

| Capability | What the prototype makes possible |
|---|---|
| Document intelligence | Organize publications and recover structured evidence with source locations. |
| Evidence-linked analysis | Inspect the passage and context behind a proposed judgment. |
| Human review | Confirm or correct decisions while retaining the original suggestion. |
| Cross-section reasoning | Follow a claim through the study and identify where its support becomes incomplete. |
| Reviewer communication | Present a short finding, its consequence and a practical revision suggestion, with evidence available on demand. |

The supervised research workflow has been exercised end to end. Recent work
extends the initial extraction and coding tools into linked assessments and
reviewer-facing explanations. A portable, fully integrated production service
is the next engineering milestone.

## What the output should help a reviewer do

![Invented review example: separate an observed association from an intervention claim](assets/review-example.svg)

*Illustrative output design using entirely invented content. It shows the
communication goal, not a measured model result or the full internal rubric.*

[Read the short example and its proposed author feedback →](docs/review-example.md)

## Working prototype

![Local review interface with invented content](assets/synthetic-review.png)

*Screenshot from the working local review interface. The content is invented;
this earlier screen illustrates the interaction design, not a benchmark result.*

<details>
<summary><strong>Inspect source context and a separate human decision</strong></summary>

![Source context and human review](assets/source-review.png)

The reviewer sees the surrounding passage and records a separate decision.
The original suggestion remains available for comparison and audit.

</details>

<details>
<summary><strong>Inspect an evidence-linked evaluation screen</strong></summary>

![Evaluation screen using invented content](assets/evaluation-review.png)

This demonstration leaves a judgment unresolved until the necessary evidence
has been checked. The entries are illustrative, not research annotations.

</details>

## Early graph and agent experiments

I have explored **evidence graphs** and **bounded agent-style review loops** in
small development experiments. The questions are practical: can linked evidence
help retrieve the right context, and can a focused second review find support
or counterevidence that an initial pass missed?

The experiments include source/claim linking, targeted critique and documented
revision. One recurring lesson is that complete, consistent instructions and
well-scoped evidence matter before additional architectural complexity.

These are early research prototypes. A controlled comparison with a matched
serial baseline, including cost and human-review effort, is still needed.
[Read the public architecture note →](docs/architecture-exploration.md)

## Evidence of progress

- **Working interaction:** local source inspection, separate corrections, saving
  and reloading have been exercised in the prototype.
- **Documented iteration:** source reconstruction, missing context, duplicated
  review work and persistence problems led to targeted changes and checks.
- **Technical verification:** the November handoff passed 25 synthetic checks
  covering scoped evidence contracts and a coherence-to-report demonstration.
- **Evaluation discipline:** original suggestions, human answers and jointly
  resolved decisions are kept distinct; development agreement is not reported
  as independent accuracy.

[Validation scope](docs/validation-scope.md) ·
[What development uncovered](docs/observed-errors.md)

## Capabilities I bring to a team

| Area | Contribution demonstrated by this project |
|---|---|
| Applied AI product development | Translate a specialist problem into a usable workflow and concrete deliverables. |
| Domain and knowledge modeling | Represent evidence, claims, context and decisions so they can be inspected together. |
| Human–AI interaction | Design review tasks around the information a person needs to make a sound decision. |
| Evaluation and quality assurance | Build contrast cases, analyze errors and separate technical checks from scientific validation. |
| Technical collaboration | Prepare versioned documentation, demonstrations and an integration roadmap for an engineering team. |

**Implementation context:** Python, document conversion, LLM-assisted processing,
structured data, local web interfaces and automated checks. The portfolio
emphasizes my ownership of the problem, system design and evaluation; implementation
has been developed with AI assistance.

For a guided demonstration or a discussion of applied AI, research intelligence
or human-review workflows, contact me through my [GitHub profile](https://github.com/HilpertPeter)
or the application accompanying this portfolio.

## Public showcase scope

The current showcase contains documentation and static visual examples. The
implementation, prompts, detailed coding rules, internal schemas and research
data remain private. No Python scripts are included in the current version.
Earlier commits contain a small illustrative artifact verifier; removing it from
the current version does not remove the existing Git history.

The [MIT License](LICENSE) applies to the material distributed in this showcase.
It does not cover the undistributed research implementation, prompts or datasets.
