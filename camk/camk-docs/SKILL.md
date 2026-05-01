---
name: camk-docs
description: "Documentation and writing workflow. Use when: (1) User needs to write technical documentation, README, API docs, or changelogs, (2) Need to structure and organize documentation, (3) Want to ensure docs are clear, complete, and consistent with the codebase."
type: flow
---

# Documentation Workflow

Structured workflow for creating and maintaining technical documentation.

```mermaid
flowchart TD
    BEGIN([Begin]) --> IDENTIFY

    IDENTIFY{What type of docs?} --> |README| README
    IDENTIFY --> |API docs| API_DOCS
    IDENTIFY --> |Architecture| ARCH
    IDENTIFY --> |Changelog| CHANGELOG
    IDENTIFY --> |User guide| USER_GUIDE

    README[Write README<br/>- Project overview<br/>- Quick start<br/>- Installation<br/>- Usage examples<br/>- Contributing] --> REVIEW

    API_DOCS[Write API docs<br/>- Endpoint list<br/>- Request/response schemas<br/>- Auth requirements<br/>- Error codes] --> REVIEW

    ARCH[Write architecture doc<br/>- System overview<br/>- Component diagram<br/>- Data flow<br/>- Tech stack<br/>- Decisions] --> REVIEW

    CHANGELOG[Write changelog<br/>- Version sections<br/>- Breaking changes<br/>- New features<br/>- Bug fixes<br/>- Deprecations] --> REVIEW

    USER_GUIDE[Write user guide<br/>- Step-by-step instructions<br/>- Screenshots/diagrams<br/>- Troubleshooting<br/>- FAQ] --> REVIEW

    REVIEW[Review docs<br/>- Check completeness<br/>- Verify accuracy<br/>- Check formatting<br/>- Test code examples] --> {Ready?}

    {Ready?} --> |Yes| PUBLISH
    {Ready?} --> |Needs edit| IDENTIFY

    PUBLISH[Publish / Update<br/>- Commit to repo<br/>- Update links<br/>- Notify team] --> END([End])
```
