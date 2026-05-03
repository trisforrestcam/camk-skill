---
name: spec-apply
description: Implement tasks from a spec change. Supports parallel execution with up to 3 agents. Use /skill:spec-apply to start.
---

# Spec Apply

Implement all pending tasks from an active spec change. This skill handles both simple sequential changes and complex phased parallel changes.

## Workflow Overview

```
Select Change → Read Context → Detect Mode → Execute → Complete
```

- **Sequential mode**: Loop through tasks one by one, implement, mark done
- **Parallel mode**: Execute by phases, spawn up to 3 subagents per phase for different streams

## Input

Optionally specify a change name. If omitted:
- Infer from conversation context
- Auto-select if only one active change exists
- If ambiguous, scan and ask user to select

## Paths

```
.kimi/openspec/changes/<name>/
├── specs/<capability>/spec.md
├── proposal.md
└── tasks.md
```

## Steps

### Step 1: Select Change

Scan active changes:

```bash
ls -d .kimi/openspec/changes/*/ 2>/dev/null | grep -v archive
```

- If only one: auto-select
- If multiple: ask user which one
- Announce: "Using change: <name>"

### Step 2: Read Context

Read ALL context files for the selected change:

1. All spec files: find and read every `specs/*/spec.md`
2. `proposal.md`
3. `tasks.md`

Show summary:
- Which specs and how many requirements/scenarios
- Progress: count `- [x]` vs total `- [ ]` + `- [x]`

### Step 3: Detect Execution Mode

Parse `tasks.md`:

- If it contains `## Phase` headers with `(parallel: N agents)`: **parallel mode**
- If tasks are flat with no phases: **sequential mode**

### Step 4A: Sequential Execution (simple changes)

Loop through each pending task (`- [ ]`):
1. Show which task is being worked on
2. Read relevant spec requirement (from task's `spec:` annotation)

   Task format with spec annotation:
   ```
   - [ ] A1 Implement login with email
         files: src/auth/login.ts
         spec: auth → "REQ-01 User shall login with email and password"
   ```

3. Implement the code change
4. Mark task complete: use `StrReplaceFile` to change `- [ ]` → `- [x]` for that task in tasks.md
5. Continue to next task

**Pause if:**
- Task is unclear → ask user for clarification, then resume from this task
- Implementation reveals design issue → suggest updating specs/proposal, wait for user decision, then resume
- Error or blocker → report the error/blocker with details, wait for user input, then resume

**Do NOT skip tasks.** Always resume from the paused task and continue through remaining tasks in order.

### Step 4B: Parallel Execution (phased changes)

For each phase in order:

1. **Identify streams in this phase**
   Parse all `### Stream:` sections under the current `## Phase N` header.

2. **Spawn subagents** (max 3)

   For each stream, spawn a subagent using the `Agent` tool with `run_in_background=true`:

   ```
   Agent(
     description="<stream-name> implementation",
     prompt="<complete context for this stream>",
     run_in_background=true
   )
   ```

   **Subagent context (include in prompt):**
   - Stream name and scope
   - ONLY the specs relevant to this stream (from the **Streams Overview** table in `tasks.md`)
   - ONLY the tasks for this stream in this phase
   - File boundary (which files the agent may modify, from the Streams Overview table)
   - Relevant spec requirements and scenarios

   **Subagent rules (include in prompt):**
   - ONLY modify files within the stream's file boundary
   - Do NOT modify files outside scope
   - Do NOT modify tasks.md (main agent handles that)
   - Implement each task to satisfy its referenced spec scenario
   - If blocked, report back with clear description

   **When a subagent reports blocked:**
   - Pause the entire phase
   - Report the blocker to the user with full context (which stream, which task, what the issue is)
   - Ask user for guidance on how to proceed
   - Do NOT proceed to next phase until all blockers are resolved

3. **Wait for all subagents**

   After spawning all subagents, use `TaskOutput` with `block=true` to wait for each one:

   ```
   TaskOutput(task_id="<agent-id>", block=true, timeout=<reasonable>)
   ```

   Collect results from all subagents before proceeding.

4. **Check results**
   - If all succeeded (subagents completed without errors and reported success): use `StrReplaceFile` to mark their tasks `[x]` in tasks.md
   - If any failed (subagent reported failure, threw error, or returned incomplete work): report the failure, do NOT proceed to next phase
   - Show progress: "Phase N complete. N/M tasks done overall."

5. **Move to next phase**

### Step 5: Completion

When all tasks are done:

```
## Implementation Complete

**Change:** <name>
**Progress:** <N>/<N> tasks complete

All tasks complete! Ready to archive.
Run /skill:spec-archive
```

## Parallel Execution Rules

These rules govern how subagents work:

1. **Max 3 agents** running in parallel, never more
2. **File isolation**: each agent only touches files in its stream scope
3. **Context isolation**: each agent only sees specs relevant to its stream
4. **No cross-stream writes**: agents must NOT modify files outside their boundary
5. **Main agent owns tasks.md**: only the main agent marks tasks as done
6. **Phase ordering**: next phase starts only after current phase fully completes
7. **Failure handling**: if any agent fails in a phase, stop and report. Do not continue.

## Spec Verification

When implementing a task, verify against its spec:

- Read the `spec:` annotation on the task
- Find the requirement and scenarios in the spec file
- Implement to satisfy all WHEN/THEN scenarios
- A task is NOT done until its spec scenarios would pass

## Guardrails

- Always read all context files before starting
- Respect file boundaries per stream
- Mark tasks `[x]` immediately after completing each
- Pause on errors, blockers, or unclear requirements
- If implementation reveals spec issues, pause and suggest updating specs
- Keep code changes minimal and scoped to each task
- Specs are the contract: if code does not satisfy spec, task is not done
