---
name: spec-archive
description: Archive a completed change. Moves the change folder to archive and updates capabilities manifest. Use /skill:spec-archive.
---

Archive a completed spec change.

## Steps

### Step 1: Select Change

Scan active changes:

```bash
ls -d .kimi/openspec/changes/*/ 2>/dev/null | grep -v archive
```

- If only one: auto-select
- If multiple: ask user which one to archive
- If none: report and exit

### Step 2: Verify Completion

Check that all tasks are done:

```bash
grep -c '\[ \]' .kimi/openspec/changes/<name>/tasks.md
```

- If pending tasks remain (count > 0): warn user, ask to confirm anyway
- If all done: proceed

### Step 3: Move to Archive

```bash
mkdir -p .kimi/openspec/changes/archive
DATE=$(date +%Y-%m-%d)
mv .kimi/openspec/changes/<name> .kimi/openspec/changes/archive/${DATE}-<name>
```

### Step 4: Update Capabilities Manifest

Read the specs from the archived change and update `.kimi/openspec/capabilities.yaml`.

If the file does not exist, create it.

Read each `specs/<capability>/spec.md` in the archived change. Extract:
- Capability name (from directory name)
- All requirement names (from `### Requirement:` headers)

Append to capabilities.yaml:

```yaml
# Updated: <date>
capabilities:
  <existing-capability>:
    archived: <date>
    source: <change-name>
    requirements:
      - <requirement 1>
      - <requirement 2>
  <new-capability>:
    archived: <date>
    source: <change-name>
    requirements:
      - <requirement 1>
      - <requirement 2>
```

If a capability already exists in the manifest, update it with the new requirements from this change.

### Step 5: Confirm

```
Archived: <name> → archive/<date>-<name>
Updated: capabilities.yaml (<N> capabilities total)
```

## Paths

```
.kimi/openspec/
├── capabilities.yaml
└── changes/
    └── archive/
        └── <date>-<name>/
            ├── specs/
            ├── proposal.md
            └── tasks.md
```

## Guardrails

- Always verify task completion before archiving
- Keep all files intact when moving (specs, proposal, tasks)
- Always update capabilities.yaml after archive
- If capabilities.yaml is malformed, recreate it
