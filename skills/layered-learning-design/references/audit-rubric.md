# Layered Learning Audit Rubric

Use this rubric for `audit` at lesson, module, or course scope.

Audit the intended capability and evidence before auditing headings or prose.

## Contents

1. Status and severity
2. Core learning loop
3. Alignment
4. Scope checks
5. Domain and artifact checks
6. Evidence rules
7. Finding and output format

## Status Scale

- `PASS`: direct evidence satisfies the criterion.
- `PARTIAL`: some evidence exists, but the learning loop is incomplete or ambiguous.
- `MISSING`: required evidence is absent.
- `N/A`: the criterion does not apply to this scope, domain, or learner goal.

Do not convert `N/A` into a finding.

## Severity Scale

- `P0`: the stated capability cannot be practiced or validated, or the material creates a serious safety, factual, or representational failure.
- `P1`: a target-task-evidence loop, essential prerequisite, or major scope contract is missing.
- `P2`: the artifact is usable but has a material sequencing, feedback, domain, boundary, or transfer gap.
- `P3`: wording, ordering, consistency, or efficiency can improve without breaking the learning loop.

Use the highest severity justified by learner impact. Do not inflate severity because many low-impact checks fail.

## Pass 1: Core Learning Loop

### Entry State

Check whether the artifact:

- States or safely infers prerequisite capability.
- Distinguishes evidence from assumptions.
- Avoids hidden prerequisites that block the task.

### Target Capability

Check whether the target:

- Describes observable learner performance.
- Fits the stated learner and available time.
- Defines acceptance evidence.

### Blocking Gap

Check whether the artifact:

- Names a specific obstacle between entry and target.
- Makes the obstacle observable.
- Uses the obstacle to justify the capability increment.

### Smallest Capability Increment

Check whether the artifact:

- Introduces one primary capability increment.
- Defers unrelated concepts.
- Keeps multiple variants together only when they share the same goal, prerequisites, and verification artifact.

### Learner Performance

Check whether the learner must:

- Produce, change, classify, solve, run, explain, critique, or decide something.
- Work with clear inputs, constraints, and outputs.
- Use the target capability rather than bypass it.

### Evidence and Feedback

Check whether the artifact:

- Defines observable pass, partial, and fail evidence.
- Verifies the target rather than a proxy or author assertion.
- Provides diagnosis, feedback, or repair.
- Uses repeatable checks when repeatability is possible.

### Boundary and Transfer

Check whether the artifact:

- States what the exercise proves and does not prove.
- Provides a transfer context.
- Adds a next-gap handoff only when part of a sequence.

## Pass 2: Alignment

Check these relationships explicitly:

- Target capability ↔ learner performance.
- Learner performance ↔ acceptance evidence.
- Blocking gap ↔ capability increment.
- Feedback ↔ observed failure mode.
- Transfer task ↔ learned capability.

Treat a broken target-task-evidence relationship as at least P1.

## Pass 3: Scope Checks

For a lesson, check one bounded increment and a manageable task.

For a module or course, also check:

- Terminal capability and authentic terminal evidence.
- Capability or knowledge map.
- Prerequisite dependencies and sequence rationale.
- Cumulative retrieval, practice, and scaffold fading.
- Diagnostic, formative, cumulative, and terminal assessment roles.
- Pacing, workload, and learner variation.
- Terminal transfer task and maintenance boundary.

Do not require every lesson to be fully expanded during a course-level audit.

## Pass 4: Domain and Artifact Checks

Read `domain-adapters.md` and apply only the selected domain's checks.

For engineering material, check:

- A reproducible bad case or concrete limitation when appropriate.
- Concept-to-artifact mapping for real files, functions, classes, fields, commands, reports, metrics, traces, and data structures that exist.
- Runnable or inspectable verification.
- `pseudocode` labels for invented structures.
- `teaching fixture` labels plus what the fixture proves, cannot prove, and simplifies.
- The smallest applicable production bridge tier when the lesson teaches a production-relevant mechanism.

Check language against the user's requested language and source context. Do not require Chinese-English bilingual headings by default.

## Evidence Rules

For every finding:

- Cite a section, path, line, artifact, or direct observation.
- Separate observed evidence from inference.
- State confidence as `high`, `medium`, or `low`.
- Describe learner impact, not only formatting inconsistency.
- Propose the smallest concrete repair.

When evidence is unavailable, mark the check `PARTIAL` or state the assumption. Do not fabricate missing artifacts.

## Finding Template

```text
[Severity] [Short title]
Location: [section, path, line, or artifact]
Status: [PARTIAL | MISSING]
Evidence: [direct evidence]
Problem: [specific gap]
Why it matters: [learner or assessment impact]
Repair: [smallest concrete edit]
Artifact affected: [lesson, task, code, proof, source, fixture, report, rubric, or template]
Confidence: [high | medium | low]
```

## Output Discipline

- Report every P0 and P1 finding.
- Report only the highest-value P2 findings, normally no more than five.
- Combine repetitive P3 findings into one pattern when possible.
- Preserve valid design decisions and acknowledge strong evidence.
- End with a missing-artifact map and ordered minimal repair plan.

## Final Summary

- Overall health: `strong | usable with gaps | structurally weak | incomplete`.
- Highest severity.
- Main broken or missing learning loop.
- Main missing evidence or artifact.
- Minimal ordered repair plan.
