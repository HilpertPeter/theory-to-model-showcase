# Evidence graphs and focused review agents

**Early development experiments · November 2026**

The research question is whether additional structure and selective checking
improve a useful review enough to justify their complexity and cost.

## Evidence graphs

An evidence graph links document passages, claims and review decisions. Small
prototypes have exercised these links and checked that evidence references stay
within the intended scope. This can support navigation and targeted retrieval.

This is a graph of reported evidence, not a causal model of the world. A graph
can preserve or expose relationships between records; it cannot make an
unsupported scientific assertion true.

## Bounded agent-style review

Development exercises have separated an initial assessment, a focused critique
and a documented revision. A reviewer role can look for missing context or
counterevidence instead of simply asking another model to agree. Unresolved
judgments remain visible for human review.

These are limited prototype exercises on development material. They are not a
deployed autonomous service or a demonstration of continual model training.

## What the experiments have taught me

Complete instructions and consistent definitions are prerequisites for a useful
comparison. An apparent improvement can otherwise come from giving a later pass
better information rather than from using an agent or a graph. A revision must
also remain separate from the original output and from accepted human decisions.

This motivates a measured approach: improve the structured serial baseline,
then test where linked evidence or an additional check adds value.

## What comes next

Compare serial processing, evidence graphs, adaptive review and their combination
on matched inputs. Assess missed evidence, unsupported findings, human-review
effort, cost and latency. Retain extra components only when they show a practical
benefit. No architecture is assumed to be best in advance.

This public note describes the questions and lessons. Internal representations,
prompts, review rules, orchestration code and research cases are not included.
