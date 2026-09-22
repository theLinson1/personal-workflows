# Layered Lesson Template

Use this output scaffold for lesson-level `design` or `rewrite`.

Replace bracketed text. Remove every conditional section that does not serve the target capability.

## Route and Metadata

- Operation: [design | rewrite]
- Scope: lesson
- Domain: [general | engineering | mathematics | science | humanities | language | writing-design | mixed]
- Topic: [topic]
- Output language: [language]
- Target learner: [learner profile]
- Duration or size: [time or artifact limit]
- Assumptions: [only assumptions that affect the design]

## 1. Entry State

The learner can already:

- [Observable prerequisite capability.]

Evidence or assumption:

- [Prior lesson, artifact, assessment, or explicitly labeled assumption.]

## 2. Target Capability

After this lesson, the learner can:

- [Observable performance.]

Acceptance evidence:

- [Artifact, action, explanation, proof, decision, output, or metric that demonstrates the capability.]

## 3. Blocking Gap

Current problem:

- [Specific obstacle between entry state and target capability.]

Observable symptom:

- [Failure, misconception, incomplete proof, source conflict, language error, weak draft, design limitation, or bad result.]

Why the current approach is insufficient:

- [Mechanism-level or reasoning-level explanation.]

## 4. Smallest Capability Increment

Introduce:

- [One concept, strategy, or mechanism that addresses the blocking gap.]

Defer:

- [Related concept that is not required yet.]

If comparing variants, confirm:

- Shared capability goal: [goal].
- Shared prerequisites: [prerequisites].
- Common verification artifact: [artifact].
- Reason they belong in one lesson: [reason].

## 5. Learner Performance

Concrete material:

- Type: [real artifact | teaching fixture | pseudocode | source | problem | sample | prompt]
- Location or content: [path, URL, excerpt, dataset, code, proof problem, or brief]

The learner must:

1. [Produce, change, classify, solve, run, explain, critique, or decide something.]
2. [Inspect or compare a concrete result.]
3. [Explain the result when explanation is part of the target.]

Expected output:

- [Learner-created artifact or action.]

## 6. Evidence and Feedback

Verification method:

- [Command, test, rubric, report field, proof check, source comparison, critique, or performance observation.]

| Result status | Observable evidence | Feedback or repair |
| --- | --- | --- |
| Pass | [Evidence] | [Reinforcement or next challenge] |
| Partial | [Evidence] | [Targeted repair] |
| Fail | [Evidence] | [Diagnostic step and retry] |

Common mistakes:

- Mistake: [Likely mistake].
  - Symptom: [Observable symptom].
  - Repair: [Concrete repair].

## 7. Boundary and Transfer

This lesson proves:

- [Supported claim.]

This lesson does not prove:

- [Unsupported claim or remaining uncertainty.]

Transfer scenario:

- [A different context where the learner should apply the capability.]

Unresolved problem:

- [Remaining bottleneck, if this lesson belongs to a sequence.]

## Alignment Check

| Element | Definition | Alignment evidence |
| --- | --- | --- |
| Target capability | [Target] | [Why it is observable] |
| Learner performance | [Task] | [Why it exercises the target] |
| Acceptance evidence | [Evidence] | [Why it verifies the same behavior] |

## Engineering Extension

Include only for an engineering lesson.

### Reproducible Bad Case or Concrete Limitation

- Setup: [Command, input, state, or fixture.]
- Current result: [Observable failure or limitation.]
- Why it fails: [Mechanism-level explanation.]

### Concept-to-Artifact Map

| Concept | Artifact | Location | Learner action | Evidence |
| --- | --- | --- | --- | --- |
| [Concept] | [File, function, class, field, command, report, metric, trace, or data structure] | [Path or symbol] | [Action] | [Observation] |

### Runnable Verification

```powershell
[command]
```

Expected output:

- [Output, report, metric, trace, or artifact change.]

### Artifact Integrity

- Real code exists: [yes | no].
- Pseudocode used: [yes | no; label every invented structure].
- Teaching fixture used: [yes | no].
- Fixture proves: [claim].
- Fixture cannot prove: [limit].
- Production reality simplified: [limit].

## Production Transfer Extension

Include only when `references/engineering-production-bridge.md` selects a tier.

- Selected tier: [A | B | C].
- System position and I/O: [Tier A].
- Strategy selection or composition: [Tier B, when relevant].
- Evaluation, trace, and operations: [Tier C, when relevant].
- Omission reason: [State only when a bridge would normally be expected but is out of scope.]

## Sequence Handoff

Include only when the lesson belongs to a sequence.

- Capability now available: [capability].
- Next unresolved gap: [gap].
- Next lesson: [title or topic].

## Teach-Back or Interview Version

Include only when required by the learner goal or assessment.

- Prompt: [oral, interview, review, or teach-back prompt].
- Concise response standard: [what a strong response must preserve].
