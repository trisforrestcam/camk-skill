# Spec Skills

Spec-driven development skills for Kimi Code CLI. Think, spec, plan, then build.

## Quick Start

```bash
# Copy into your project
cp -r .kimi/ ~/your-project/.kimi/

# Add to .gitignore
echo ".kimi/openspec/" >> ~/your-project/.gitignore

# Start Kimi Code
cd ~/your-project && kimi
```

## Skills

| Skill | Type | Command | Description |
|-------|------|---------|-------------|
| spec-propose | flow | `/flow:spec-propose "your idea"` | Explore, spec, plan |
| spec-apply | flow | `/flow:spec-apply` | Implement with parallel agents |
| spec-archive | standard | `/skill:spec-archive` | Archive completed change |
| spec-review | standard | `/skill:spec-review` | Review active and archived changes |

## Workflow

```
/flow:spec-propose "add user auth"
  → AI explores codebase, asks questions
  → Creates specs with requirements + scenarios
  → Creates proposal.md + tasks.md
  → You edit files directly if needed

/flow:spec-apply
  → AI reads specs as contract
  → Implements tasks (parallel agents if phased)
  → Marks tasks done

/skill:spec-archive
  → Moves change to archive/
  → Updates capabilities manifest

/skill:spec-review
  → Shows active changes, progress, archived history
```

## File Structure

```
.kimi/
├── skills/
│   ├── spec-propose/SKILL.md
│   ├── spec-apply/SKILL.md
│   ├── spec-archive/SKILL.md
│   └── spec-review/SKILL.md
│
└── openspec/                    ← not committed to git
    ├── capabilities.yaml        ← manifest of archived capabilities
    └── changes/
        ├── <name>/              ← active change
        │   ├── specs/
        │   │   └── <capability>/spec.md
        │   ├── proposal.md
        │   └── tasks.md
        └── archive/             ← completed changes
            └── YYYY-MM-DD-<name>/
                ├── specs/
                ├── proposal.md
                └── tasks.md
```

## Spec Format

```markdown
# Capability: user-auth

### Requirement: User can log in
The system SHALL allow users to authenticate with email and password.

#### Scenario: Valid credentials
- WHEN user submits valid email and password
- THEN system creates a new session
- AND returns JWT token

#### Scenario: Invalid password
- WHEN user submits wrong password
- THEN system returns 401 Unauthorized
```

## Tasks Format

Simple (1 agent):
```markdown
- [ ] 1.1 Task description
- [ ] 1.2 Task description
```

Parallel (up to 3 agents):
```markdown
## Streams Overview
| Stream | Scope | Files | Specs |
|--------|-------|-------|-------|
| data   | DB    | src/db/* | user-model |

## Phase 1 (parallel: 3 agents)

### Stream: data
- [ ] B1 Create user model
      files: src/db/user.model.ts
      spec: user-model → "User schema"

### Stream: auth
- [ ] A1 Create session manager
      files: src/auth/session.ts

### Stream: api
- [ ] C1 Error handling
      files: src/api/middleware/error.ts
```

## Requirements

- Kimi Code CLI
- No other dependencies
