---
name: spec-review
description: Review active and archived spec changes. Shows progress, specs, and history. Use /skill:spec-review.
---

Review spec changes - active and archived.

## Usage

User can ask:
- "show active changes" - list current work
- "show archived" - list completed work
- "show <name>" - display details of a specific change
- "show progress" - task completion status
- "show specs <name>" - display spec requirements and scenarios
- Or just invoke without args for a full overview

## Steps

### Step 1: Gather Data

Scan both active and archived changes:

```bash
# Active changes
ls -d .kimi/openspec/changes/*/ 2>/dev/null | grep -v archive

# Archived changes
ls .kimi/openspec/changes/archive/ 2>/dev/null
```

Read capabilities manifest if it exists:

```bash
cat .kimi/openspec/capabilities.yaml 2>/dev/null
```

### Step 2: Present Overview

#### Active Changes

For each active change, read `tasks.md` and count progress:

```bash
DONE=$(grep -c '\[x\]' tasks.md 2>/dev/null || echo 0)
TOTAL=$(grep -c '\[.\]' tasks.md 2>/dev/null || echo 0)
```

Present as table:

```
ACTIVE CHANGES
─────────────────────────────────────────────────────
Change          Progress    Status
add-auth        3/7         applying (Phase 2/3)
fix-pagination  0/4         planned
─────────────────────────────────────────────────────
```

#### Archived Changes

```
ARCHIVED
─────────────────────────────────────────────────────
Date        Change              Tasks
2026-05-01  add-logging         5/5 ✓
2026-05-02  fix-cors            3/3 ✓
─────────────────────────────────────────────────────
```

#### Capabilities

Read and display capabilities.yaml:

```
CAPABILITIES
─────────────────────────────────────────────────────
user-auth (archived 2026-05-03, from add-user-auth)
  - User can log in
  - User can log out
  - Session auto-expires

password-policy (archived 2026-05-03, from add-user-auth)
  - Password must be hashed
  - Password validation
─────────────────────────────────────────────────────
```

### Step 3: Answer Questions

User may ask follow-up questions:
- "What specs does add-auth have?" → read and show spec files
- "Which tasks are still pending?" → filter `- [ ]` lines
- "Compare proposal of X and Y" → read both proposals, side by side
- "Show me the archived specs for X" → read from archive/

## Bash Commands Reference

```bash
# List active changes
ls -d .kimi/openspec/changes/*/ | grep -v archive

# List archived changes
ls .kimi/openspec/changes/archive/

# Count task progress
grep -c '\[x\]' .kimi/openspec/changes/<name>/tasks.md
grep -c '\[ \]' .kimi/openspec/changes/<name>/tasks.md

# Show pending tasks
grep '\[ \]' .kimi/openspec/changes/<name>/tasks.md

# Show completed tasks
grep '\[x\]' .kimi/openspec/changes/<name>/tasks.md

# Find all spec files for a change
find .kimi/openspec/changes/<name>/specs -name "*.md"

# Read capabilities
cat .kimi/openspec/capabilities.yaml

# Read archived proposal
cat .kimi/openspec/changes/archive/<folder>/proposal.md

# Read archived specs
find .kimi/openspec/changes/archive/<folder>/specs -name "*.md"
```

## Guardrails

- Always scan before presenting, data may have changed
- Handle gracefully if no changes exist yet
- Handle gracefully if no archive exists yet
- Handle gracefully if capabilities.yaml does not exist yet
