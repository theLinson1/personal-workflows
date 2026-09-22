---
name: layered-learning-design
description: "Use when designing, auditing, rewriting, or extracting lessons, modules, courses, or interactive learning contracts with learner practice, evidence, feedback, and transfer. Not for simple explanations or requests to directly implement or fix software."
---

# Layered Learning Design

## Core Standard

Design learning around a capability change that can be observed.

Make the learner's entry state, target capability, blocking gap, smallest useful capability increment, performance task, evidence and feedback, and transfer boundary explicit.

Layer only the detail the task needs:

1. Core capability contract.
2. Scope adapter.
3. Domain adapter.
4. Optional interaction, production, or exemplar adapter.

## Route the Task

Classify five dimensions before producing the deliverable.

### Operation

- `audit`: inspect an existing learning artifact and identify evidence-backed gaps.
- `design`: create a new learning artifact.
- `rewrite`: improve an existing artifact while preserving its intended capability goal.
- `extract`: derive reusable instructional structure from one or more examples without copying surface phrasing.

### Scope

- `lesson`: one bounded capability increment.
- `module`: a short sequence with a shared intermediate outcome.
- `course`: a capability map, dependency path, sequence, cumulative assessment, and terminal transfer task.

### Domain

Choose `general`, `algorithms`, `engineering`, `mathematics`, `science`, `humanities`, `language`, `writing-design`, or `mixed`.

For `mixed`, name one primary adapter and any secondary adapter. Do not apply every domain pattern.

### Output Language

Follow the user's requested language. Otherwise follow the user's prompt or the source material. Add bilingual technical terms only when they improve comprehension or terminology transfer.

### Interaction

Choose `artifact` for a standalone deliverable or `interactive` when the learner must perform across turns before the next layer is revealed.

State the inferred operation, scope, domain, topic, and interaction mode in one concise sentence. Honor explicit user choices without reclassifying them.

## Load Resources Conditionally

Load only resources required by the route.

- Read `references/audit-rubric.md` for `audit`.
- Use `assets/lesson-template.md` for lesson-level `design` or `rewrite`.
- Read `references/course-design.md` and use `assets/course-template.md` for module- or course-level work.
- Read `references/domain-adapters.md` when the domain changes the learning sequence, practice, or evidence.
- Read `references/interactive-facilitation.md` for `interactive` work or when the request specifies hint timing, learner-first turns, stage gates, or artifact timing.
- Use `assets/learning-contract-template.md` when producing a reusable interactive Contract.
- Read `references/engineering-production-bridge.md` when an engineering lesson teaches a subsystem, pipeline stage, model call, stateful workflow, evaluation harness, deployment behavior, security boundary, data contract, or operational mechanism.
- Read `references/engineering-incremental-course-example.md` when an engineering progression or exemplar extraction would help.
- Read `references/rag-lesson-08-query-transformation-example.md` for RAG, retrieval, query transformation, Query Rewrite, Multi-Query, HyDE, or the existing Lesson 08.

## Collect or Infer Inputs

Collect or infer:

- Target learner.
- Entry capability and prerequisite evidence.
- Target capability and acceptance evidence.
- Topic, operation, scope, domain, and output language.
- Existing material and source artifacts.
- Time, format, codebase, tools, assessment, accessibility, and production constraints.
- Required artifacts such as code, proof, source text, fixture, dataset, report, metric, trace, diagram, critique, or explanation.
- Interaction mode, disclosure policy, explicit stuck signal, artifact gates, and state source.

State safe assumptions and continue. Ask only when a missing input changes the target capability, core scope, or authorized work.

## Seven-Part Core Contract

Apply these seven parts to every learning artifact. Adapt the labels to the domain instead of forcing identical headings.

### 1. Entry State

State what the learner can already do and which prerequisite is known, evidenced, or assumed.

### 2. Target Capability

State what the learner must be able to do after the learning experience. Define observable acceptance evidence at the same time.

### 3. Blocking Gap

Name the specific problem that prevents the learner from reaching the target. Make it observable through a failure, misconception, incomplete proof, weak interpretation, language error, draft problem, or design limitation.

### 4. Smallest Capability Increment

Introduce the smallest concept, strategy, or mechanism that closes the blocking gap enough for the learner to act.

Allow multiple variants in one lesson only when they:

- Serve the same capability goal.
- Share prerequisites.
- Use one common comparison or verification artifact.
- Do not each require a separate mental model or assessment.

Split the lesson when these conditions do not hold.

### 5. Learner Performance

Require the learner to produce, change, classify, solve, run, explain, critique, or decide something. Do not treat passive reading as sufficient practice.

### 6. Evidence and Feedback

Specify the output, proof step, source comparison, language production, critique, report, metric, trace, or artifact change that demonstrates performance.

Define:

- Passing evidence.
- Failing or partial evidence.
- Feedback or repair when the result differs.

### 7. Boundary and Transfer

State what the exercise proves, what it does not prove, where the capability transfers, and what unresolved problem follows.

Require a next-lesson handoff only for a sequence, module, or course.

## Alignment Gates

Confirm these relationships before returning the deliverable:

- The target capability, learner performance, and acceptance evidence test the same behavior.
- The capability increment directly addresses the blocking gap.
- Required prerequisites are explicit.
- Core concepts map to inspectable artifacts when artifacts exist.
- Feedback tells the learner how to diagnose or repair a weak result.
- Optional sections are included because they serve the target, not because a template contains them.

## Conditional Adapters

### Scope Adapter

For a lesson, produce one core contract and only relevant extensions.

For a module or course, apply the core contract internally and output a compact capability map, prerequisite dependencies, progressive sequence, pacing, cumulative retrieval or practice, assessment architecture, and terminal transfer task. Do not emit a full seven-part lesson contract for every topic unless the user asks.

Default to at most 12 module rows and 1,500 words for a course. When the source contains more topics, cluster them into capability families and preserve topic coverage in the map. Prefer a complete compact map over expanded prose.

### Domain Adapter

Use the selected pattern from `references/domain-adapters.md`. Keep the seven-part core contract stable while changing the learning moves and evidence.

### Engineering Adapter

Prefer a reproducible bad case or concrete limitation. Map core concepts to real files, functions, classes, fields, commands, reports, metrics, traces, and data structures when they exist.

Label invented code `pseudocode`.

Label constructed cases `teaching fixture` and state:

- What the fixture proves.
- What it cannot prove.
- Which production reality it simplifies.

### Algorithms Adapter

Use `algorithms` as the primary domain for data-structure and algorithm exercises, competitive programming, and coding interview preparation. Do not route these tasks through the engineering production adapter unless the learner goal includes building or operating a real system.

Use the algorithmic problem-solving pattern in `references/domain-adapters.md`. Require unlabeled transfer problems when the target includes pattern recognition.

### Production Transfer Adapter

Use the smallest applicable tier from `references/engineering-production-bridge.md`.

Do not force a full production architecture into a syntax lesson, isolated concept, or non-production exercise. If a bridge would normally be expected but is omitted, state why.

### Exemplar Extraction Adapter

For `extract`, identify:

- Capability progression.
- Knowledge delivery pattern.
- Practice pattern.
- Evidence and feedback pattern.
- Chapter or module handoff pattern.
- Boundary and transfer pattern.

Cite the source location for each extracted pattern. Separate reusable structure from topic-specific content and avoid copying surface wording.

### Teach-Back Adapter

Add an interview answer, oral explanation, teach-back, or concise explanation only when the learner goal, assessment format, or user request calls for it.

### Interactive Facilitation Adapter

Apply the stage interface from `references/interactive-facilitation.md`. Require learner performance before later disclosure, select only `wait`, `advance`, or `repair` after a learner turn, and create artifacts only after the matching gate passes.

Generating a Contract does not authorize creating or modifying `AGENTS.md`. Require an explicit request to configure a persistent learning workspace.

## Operation Workflows

### Audit

1. Read `references/audit-rubric.md`.
2. Identify the intended capability and scope before checking headings.
3. Evaluate the core learning loop with direct evidence.
4. Apply only relevant scope and domain checks.
5. Report all P0 and P1 findings, then the highest-value P2 and P3 findings.
6. Provide a missing-artifact map and the smallest ordered repair plan.

Do not report the absence of an optional adapter as a defect.

### Design

1. Define target capability and acceptance evidence.
2. Infer the entry state and blocking gap.
3. Choose the smallest capability increment.
4. Create or select a concrete task.
5. Define evidence, feedback, boundary, and transfer.
6. Add only the matching scope and domain adapters.
7. For `interactive`, define stage permissions, minimal-hint behavior, artifact gates, and the state source.

### Rewrite

1. Recover the intended target capability.
2. Preserve valid content and source meaning.
3. Remove, defer, or split unrelated increments.
4. Repair the target-task-evidence alignment.
5. Add missing feedback, boundary, and transfer information.
6. Mark assumptions, teaching fixtures, pseudocode, and production limits.

Do not invent production code or evidence and present it as real.

### Extract

1. Identify the source artifact and its intended learner progression.
2. Extract recurring instructional decisions with source evidence.
3. Separate stable structure from domain-specific choices.
4. State where the pattern transfers and where it should not be generalized.
5. Return reusable rules or a compact pattern template.

## Style Rules

Use direct declarative sentences and concrete nouns.

Use one primary language. Translate a full title once when bilingual terminology is useful; do not translate word by word inside a sentence or title.

Prefer `entry state` over an invented previous lesson when the material is standalone.

Prefer `capability increment` over `new mechanism` outside engineering.

Make judgments auditable. Include evidence for critiques and acceptance conditions for designs.

Separate real artifacts from pseudocode and teaching fixtures.

Avoid generic encouragement, stance packaging, and claims such as "students will understand" without observable evidence.

## Output Shapes

For `audit`, output:

- Route and topic.
- Overall health and highest severity.
- Findings with location, evidence, learning impact, repair, affected artifact, and confidence.
- Missing-artifact map.
- Minimal ordered repair plan.

For lesson-level `design` or `rewrite`, output:

- Route, learner, target capability, and assumptions.
- Seven-part core contract.
- Only relevant scope, domain, production, or teach-back extensions.
- Remaining evidence or artifact gaps.

For module- or course-level `design` or `rewrite`, output:

- Route, learner, terminal capability, and assumptions.
- Entry profile and compact capability or dependency map.
- One sequence row per module or capability family.
- Cumulative practice, feedback, assessment, pacing, and terminal transfer.
- Boundaries and remaining evidence gaps.

Do not repeat the seven-part contract for each lesson or topic unless explicitly requested.

For `extract`, output:

- Source and extraction scope.
- Evidence-backed structural patterns.
- Reusable rules or template.
- Transfer limits and unresolved assumptions.

For an interactive Contract, fill `assets/learning-contract-template.md` and include the state source, stage permissions, minimal-hint rule, artifact gates, feedback repair, and transfer evidence. Generate a capability-specific Contract rather than a generic topic persona.
