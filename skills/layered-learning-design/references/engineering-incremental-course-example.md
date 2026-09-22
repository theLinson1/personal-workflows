# Engineering Incremental Course Example

> Portable handoff note (2026-09-22): This is a historical teaching example. The external course files, scripts, reports, commands, and observations described below are not bundled here and were not rerun during packaging. Use its instructional structure; verify or obtain the original artifacts before claiming the commands run or results hold in the current workspace.

This reference extracts the course structure from `learn-claude-code` s06_subagent and s07_skill_loading.

It extracts structure. It does not copy surface wording.

## Contents

1. Source role
2. Shared chapter skeleton
3. s06_subagent structure
4. s07_skill_loading structure
5. Extracted design rules
6. Anti-patterns

## Source Role

Use these chapters as a good example for engineering lessons that teach agent harness mechanisms.

The reusable pattern is:

1. Start from a working previous chapter.
2. Expose one capability bottleneck.
3. Add one smallest capability increment.
4. Keep the main loop or surrounding architecture stable.
5. Show the concrete code diff from the previous chapter.
6. Give a run command.
7. Tell the learner what to observe.
8. Explain the boundary of the teaching implementation.
9. End with the next bottleneck.

## Shared Chapter Skeleton

Both chapters follow the same learning design.

- Previous capability: the learner already has a minimal agent harness with tool dispatch and hooks.
- New bottleneck: the previous harness works, but a new scaling problem appears.
- Capability increment: one new tool and the small support functions needed by that tool.
- Concrete artifact: a runnable `code.py`.
- Exercise: run the chapter script and send targeted prompts.
- Observation: inspect terminal markers and tool behavior.
- Boundary: compare the teaching implementation with production Claude Code behavior.
- Transition: show the next bottleneck that the current mechanism creates or leaves unresolved.

## s06_subagent Structure

### Previous Capability

The learner already understands:

- Basic tool definitions.
- Tool dispatch through `TOOL_HANDLERS`.
- Hook points such as `PreToolUse` and `PostToolUse`.
- `todo_write` as a stateful tool in the main loop.

### Current Bottleneck

The main agent can trace a complex problem, but intermediate investigation fills the main `messages` list.

The bottleneck is context pollution. The main task loses attention because subtask exploration stays in the same conversation state.

### Capability Increment

s06 introduces one primary capability increment:

- `task` tool.

The supporting implementation is:

- `spawn_subagent(description: str) -> str`.
- A fresh `messages` list for the subagent.
- A restricted `SUB_TOOLS` list.
- A `SUB_SYSTEM` prompt.
- A safety loop limit.
- Summary-only return through `extract_text`.

### Concept-To-Code Mapping

- Concept: context isolation.
  Artifact: `messages = [{"role": "user", "content": description}]` inside `spawn_subagent`.
- Concept: subagent delegation.
  Artifact: `TOOLS.append({"name": "task", ...})`.
- Concept: summary-only return.
  Artifact: `return result` from `spawn_subagent`.
- Concept: recursion prevention.
  Artifact: `SUB_TOOLS` excludes `task`.
- Concept: permission continuity.
  Artifact: subagent tool calls still run `trigger_hooks("PreToolUse", block)`.
- Concept: unchanged main dispatch.
  Artifact: `TOOL_HANDLERS["task"] = spawn_subagent`.

### Hands-On Task

The learner runs:

```sh
cd learn-claude-code
python s06_subagent/code.py
```

The learner tries prompts that ask the agent to delegate file reading, project inspection, or small file creation.

### Observation Target

The learner observes:

- A subagent spawn marker.
- A subagent completion marker.
- Subagent tool calls shown separately.
- The parent agent receives a conclusion instead of the full subagent message history.

### Boundary

The chapter states that the implementation is a teaching model.

It simplifies production behavior:

- It shows synchronous subagents.
- It focuses on fresh message isolation.
- It omits forked prompt-cache behavior.
- It simplifies recursive delegation prevention.
- It simplifies permission propagation details.

### Next Transition

After subagents exist, tasks can be delegated. The next bottleneck is knowledge loading.

Different tasks need different rules. Putting all rules into the system prompt wastes context.

This leads to s07 Skill Loading.

## s07_skill_loading Structure

### Previous Capability

The learner already understands:

- The minimal agent loop.
- Hooks.
- `todo_write`.
- Subagent delegation through `task`.

### Current Bottleneck

The agent needs task-specific knowledge such as coding rules, SQL style, or API design guidance.

Putting every document into the system prompt makes every model call carry mostly irrelevant text.

The bottleneck is knowledge bloat.

### Capability Increment

s07 introduces one primary capability increment:

- `load_skill` tool.

The supporting implementation is:

- `SKILLS_DIR`.
- `_parse_frontmatter`.
- `_scan_skills`.
- `SKILL_REGISTRY`.
- `list_skills`.
- `build_system`.
- `load_skill(name: str) -> str`.

### Concept-To-Code Mapping

- Concept: cheap catalog.
  Artifact: `list_skills()` formats skill names and descriptions.
- Concept: startup registry.
  Artifact: `_scan_skills()` fills `SKILL_REGISTRY`.
- Concept: skill metadata.
  Artifact: YAML frontmatter fields `name` and `description`.
- Concept: on-demand full content.
  Artifact: `load_skill` returns stored `SKILL.md` content.
- Concept: safe lookup.
  Artifact: registry lookup by skill name instead of arbitrary path reads.
- Concept: unchanged dispatch.
  Artifact: `TOOL_HANDLERS["load_skill"] = load_skill`.

### Hands-On Task

The learner runs:

```sh
cd learn-claude-code
python s07_skill_loading/code.py
```

The learner asks what skills are available, then asks the agent to load and follow a specific skill.

### Observation Target

The learner observes:

- The agent can see available skill names from the system prompt catalog.
- Full skill content loads only after `load_skill`.
- The answer changes after the relevant skill is loaded.
- The main loop stays structurally unchanged.

### Boundary

The chapter states that the implementation is a teaching model.

It simplifies production behavior:

- It assumes one local `skills/` directory.
- It parses only core metadata.
- It treats skill content loading as a simple tool result.
- It omits bundled, managed, dynamic, remote, and conditional skill sources.
- It omits forked skill execution.

### Next Transition

On-demand loading solves early context bloat. It does not solve context growth during long sessions.

Long work still fills `messages` with old tool results and stale file content.

This leads to context compaction.

## Extracted Design Rules

Use these rules when designing engineering lessons.

- Preserve most of the previous working system.
- Add one primary capability increment per lesson.
- Name the exact bottleneck that forced the mechanism.
- Make the code diff visible.
- Keep runnable code minimal.
- Use terminal output as feedback.
- Tell the learner what to inspect.
- State what the teaching model simplifies.
- End with a bottleneck that the next lesson solves.

## Anti-Patterns

Avoid these when adapting the example.

- Adding unrelated capability increments that require separate mental models or assessments.
- Explaining a mechanism without a run command.
- Providing code without observation targets.
- Treating a teaching simplification as production behavior.
- Ending a chapter without a next problem.
- Copying the chapter's surface phrasing instead of extracting its progression method.
