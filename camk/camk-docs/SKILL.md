---
name: camk-docs
description: Technical documentation workflow. Use when the user needs to create, update, or review documentation such as README, API docs, architecture docs, changelogs, or user guides. Trigger on phrases like "write docs", "update README", "document this", "create API documentation", "write changelog", or when documentation tasks arise alongside code changes.
type: flow
---

# Documentation Workflow

Structured workflow for creating and maintaining technical documentation.

```d2
BEGIN -> IDENTIFY

IDENTIFY: What type of docs?
IDENTIFY -> README: README
IDENTIFY -> API_DOCS: API docs
IDENTIFY -> ARCH: Architecture
IDENTIFY -> CHANGELOG: Changelog
IDENTIFY -> USER_GUIDE: User guide

README: |md
  Write README
  - Project overview
  - Quick start
  - Installation
  - Usage examples
  - Contributing
|
README -> REVIEW

API_DOCS: |md
  Write API docs
  - Endpoint list
  - Request/response schemas
  - Auth requirements
  - Error codes
|
API_DOCS -> REVIEW

ARCH: |md
  Write architecture doc
  - System overview
  - Component diagram
  - Data flow
  - Tech stack
  - Decisions
|
ARCH -> REVIEW

CHANGELOG: |md
  Write changelog
  - Version sections
  - Breaking changes
  - New features
  - Bug fixes
  - Deprecations
|
CHANGELOG -> REVIEW

USER_GUIDE: |md
  Write user guide
  - Step-by-step instructions
  - Screenshots/diagrams
  - Troubleshooting
  - FAQ
|
USER_GUIDE -> REVIEW

REVIEW: |md
  Review docs
  - Check completeness
  - Verify accuracy
  - Check formatting
  - Test code examples
|
REVIEW -> READY

READY: Ready?
READY -> PUBLISH: Yes
READY -> IDENTIFY: Needs edit

PUBLISH: |md
  Publish / Update
  - Commit to repo
  - Update links
  - Notify team
|
PUBLISH -> END
```

## References

- **Documentation templates**: See `references/doc-templates.md`
- **Style guide**: See `references/style-guide.md`
