# Engineering Production Transfer Bridge

Use this reference after the teaching mechanism works and only when the learner needs to place it in a larger production system.

Select the smallest applicable tier.

## Selection Rule

Use no bridge for a local syntax lesson, isolated language feature, or explicitly non-production exercise unless the user asks for production context.

Use Tier A when the lesson teaches a component, data contract, pipeline stage, state transition, model call, deployment behavior, or security boundary.

Add Tier B when learners must choose among strategies or compose the mechanism with adjacent components.

Add Tier C when the target includes production readiness, evaluation, observability, rollout, reliability, cost, privacy, or operations.

## Tier A: System Placement and Contract

Answer:

- Where does the mechanism sit in the system?
- What consumes its input?
- What does it emit?
- What consumes its output?
- What does this mechanism own?
- What remains the responsibility of upstream, downstream, or peer components?
- Which part is real code, pseudocode, or a teaching fixture?

Tier A is the default production bridge for a production-relevant engineering mechanism.

## Tier B: Strategy and Composition

Add only when alternatives or composition matter.

Answer:

- When should this strategy be used?
- When should it not be used?
- When should it run alone, in parallel, in sequence, or as a fallback?
- How are results merged, deduplicated, ranked, validated, or handed off?
- Which implementation options exist, such as rules, templates, parsers, metadata, ontology, small model, specialist model, LLM, service, or human review?
- What quality, latency, cost, controllability, and maintenance trade-offs drive selection?

## Tier C: Evaluation and Operations

Add only when production operation is part of the target.

Answer:

- Which schemas, prompts, examples, glossaries, metadata, eval sets, logs, reports, metrics, or traces are required?
- Which trace fields permit replay, debugging, and decision attribution?
- What does the teaching metric prove?
- What must offline and online production evaluation still measure?
- What are the latency, token, throughput, caching, fallback, rollback, permission, privacy, monitoring, and incident-response concerns?
- Who owns the artifact and what triggers refresh or rollback?

## Output Discipline

Do not write all three tiers automatically.

Prefer a compact table or short architecture description when it answers the selected tier.

Use `pseudocode` for production-shaped code unless real production code exists.

Preserve raw inputs, decisions, and relevant outputs in traces when replay or attribution is part of the target.

State what the local exercise cannot establish about production quality.

## Audit Checks

- Is the selected tier justified by the learner goal?
- Does the bridge connect to the lesson's actual artifacts?
- Are responsibilities separated across components?
- Are strategy rules actionable rather than a list of options?
- Are teaching evidence and production evidence separated?
- Does operational detail remain proportional to the lesson scope?
