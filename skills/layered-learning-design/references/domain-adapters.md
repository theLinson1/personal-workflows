# Domain Adapters

Select one primary adapter after applying the seven-part core contract. Use a secondary adapter only for a genuinely mixed task.

## Contents

1. Adapter interface
2. General conceptual or procedural learning
3. Algorithmic problem solving
4. Engineering
5. Mathematics
6. Science
7. Humanities and social science
8. Language learning
9. Writing and design
10. Mixed domains

## Adapter Interface

For the selected domain, define:

- The form of the blocking gap.
- The smallest useful learning move.
- The learner performance.
- The strongest observable evidence.
- The important boundary or transfer condition.

## General Conceptual or Procedural Learning

Use this fallback when no specialized adapter fits.

- Gap: incorrect distinction, missing procedure, weak decision rule, or inability to apply a concept.
- Learning move: definition, model, worked example, contrast case, decision rule, or guided procedure.
- Performance: classify, explain, execute, compare, diagnose, or choose.
- Evidence: correct application in a new but bounded case plus explanation of the decision.
- Boundary: cases where the concept or procedure no longer applies.

## Algorithmic Problem Solving

Use this adapter for data structures, algorithms, competitive programming, and coding interview preparation.

- Gap: inability to recognize a problem pattern, choose a representation, state an invariant, justify an optimization, or transfer a known method to an unlabeled problem.
- Learning move: brute-force baseline, structural cues, representation, invariant or recurrence, optimized implementation, correctness argument, complexity analysis, and contrast case.
- Performance: classify an unlabeled problem, justify the selected pattern, implement it, test boundaries, analyze complexity, and diagnose an incorrect solution.
- Evidence: a correct unseen solution, explicit invariant or state definition, justified complexity, minimal counterexample, error repair, and delayed cold retry.
- Boundary: tag leakage, memorized templates, language-specific implementation gaps, non-monotonic cases, and problem families where the selected pattern does not apply.

Require the learner to distinguish visually similar patterns through contrast cases. For example, distinguish two pointers from sliding window by continuity, maintained state, and movement monotonicity rather than by counting pointer variables.

Treat online-judge acceptance as implementation evidence, not complete mastery evidence. When the goal includes interview transfer, also require pattern selection without labels, explanation of the invariant or recurrence, complexity justification, and an unseen problem.

Use an error taxonomy appropriate to the task, such as recognition, representation, state, invariant, transition, boundary, complexity, or language implementation. Tie feedback and retry work to the observed category.

For interactive work, require the learner's initial attempt to include a brute-force solution, time and extra-space complexity, repeated work, and an initial optimization direction. Until those are present, return `wait` or diagnose the missing item without naming the optimized representation or implementation. After an explicit stuck signal, reveal one minimal layer and wait for a new attempt. When no hint level is specified, the first layer is exactly one question that compares two concrete candidates from the learner's own brute-force process and asks them to identify already-stated repeated operations. Use only concepts already present in the problem or learner attempt. Do not introduce a new computed quantity, suggest what to save, or name or describe the target algorithm, representation, state formula, symbols, update rule, or implementation. Gate implementation artifacts on a complete representation plus invariant, state, recurrence, or recursive contract. Treat boundary analysis and interview explanation as learner performance after executed code evidence when the Contract calls for them.

## Engineering

- Gap: reproducible failure, system limitation, missing mechanism, or non-inspectable behavior.
- Learning move: add one capability increment while preserving most of the working system.
- Performance: modify or run code, inspect artifacts, diagnose output, and explain the mechanism.
- Evidence: command output, test, report, metric, trace, state change, or code-to-concept mapping.
- Boundary: teaching fixture versus production behavior, operational limits, and adjacent component responsibilities.

Prefer failure-driven progression when a real or constructed bad case can expose the need for the increment.

For interactive work, require an initial reproducible limitation with expected behavior, actual behavior, input, command, and the smallest available log, metric, trace, or artifact. Do not require an algorithmic brute-force baseline unless the engineering target contains an algorithmic subproblem. After an explicit stuck signal, reveal one observation point, boundary-narrowing question, or falsifiable experiment. Gate production changes on a reproducible case and a stated mechanism hypothesis.

## Mathematics

- Gap: inability to solve a problem, misuse of a definition, missing proof move, or overgeneralization.
- Learning move: problem, definition, representation, theorem or claim, proof, and counterexample.
- Performance: solve, derive, prove, construct a counterexample, or transfer the method.
- Evidence: valid reasoning steps, justified transformations, boundary cases, and a new problem.
- Boundary: assumptions under which the claim fails or changes.

Make definitions pay for a proof, computation, or counterexample.

## Science

- Gap: mismatch between observation and current model, weak causal explanation, or inability to interpret evidence.
- Learning move: phenomenon, model, prediction, observation or dataset, analysis, and model revision.
- Performance: predict, design an investigation, analyze data, compare models, or explain uncertainty.
- Evidence: prediction quality, data interpretation, experimental reasoning, uncertainty statement, or revised model.
- Boundary: measurement limits, confounding, model assumptions, and difference between correlation and causation.

Label simulated data or constructed experiments clearly.

## Humanities and Social Science

- Gap: decontextualized claim, unsupported causal story, source misreading, or inability to compare interpretations.
- Learning move: source, context, claim, competing interpretation, evidence limits, and argument.
- Performance: analyze a source, compare interpretations, build an evidence-backed argument, or revise a claim.
- Evidence: accurate source use, contextual reasoning, explicit warrants, counterevidence, and bounded conclusions.
- Boundary: source reliability, missing perspectives, presentism, causal uncertainty, and interpretation versus fact.

Separate primary-source claims, secondary interpretation, and the learner's inference.

## Language Learning

- Gap: failure to notice, comprehend, select, or produce a target form in context.
- Learning move: comprehensible input, noticing, controlled practice, meaningful output, feedback, and transfer.
- Performance: identify, transform, respond, speak, write, or negotiate meaning.
- Evidence: accurate and appropriate use in increasingly less controlled contexts.
- Boundary: register, dialect, pragmatics, fluency versus accuracy, and transfer beyond memorized sentences.

Provide input before requiring unsupported output.

## Writing and Design

- Gap: weak artifact, invisible craft decision, mismatch with audience, or inability to revise from critique.
- Learning move: exemplar, decomposition, constrained imitation, critique, revision, and new brief.
- Performance: create, annotate, critique, revise, and justify an artifact.
- Evidence: visible artifact change tied to a criterion and successful transfer to a different brief.
- Boundary: taste versus rubric, audience and context dependence, originality, and limits of one exemplar.

Map each craft or design move to a visible artifact decision.

## Mixed Domains

Name one primary adapter that determines the learning sequence and evidence.

Use a secondary adapter only for a specific subtask. For example:

- Algorithms primary plus engineering secondary when implementing the algorithm inside a real service or system.
- Engineering primary plus writing-design secondary for an API design review.
- Science primary plus mathematics secondary for quantitative modeling.
- Language primary plus humanities secondary for source-based discussion.

Do not concatenate every adapter's checklist.
