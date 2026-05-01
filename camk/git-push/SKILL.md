---
name: camk-git-push
description: "Git push workflow. Use when: (1) User wants to push code to a branch, (2) Need to commit changes and push to remote, (3) Want to follow a safe workflow: check status → stage → commit → pull rebase → push. Prevents common git mistakes like pushing to wrong branch or overwriting remote changes."
type: flow
---

# Git Push Workflow

Safe workflow for pushing code to a branch.

```mermaid
flowchart TD
    BEGIN([Begin]) --> STATUS

    STATUS[Check git status<br/>- Current branch<br/>- Modified files<br/>- Untracked files<br/>- Ahead/behind remote] --> {Clean working tree?}

    {Clean working tree?} --> |Yes| CHECK_BRANCH
    {Clean working tree?} --> |No| STAGE

    STAGE[Stage changes<br/>- Review what to stage<br/>- git add specific files<br/>- Or git add . if all] --> {Staged correctly?}

    {Staged correctly?} --> |Yes| COMMIT
    {Staged correctly?} --> |No| UNSTAGE

    UNSTAGE[Unstage and re-stage<br/>- git restore --staged<br/>- Re-select files<br/>- Check git status again] --> STAGE

    COMMIT[Write commit<br/>- Follow commit convention<br/>- Meaningful message<br/>- Reference issue if any] --> {Commit OK?}

    {Commit OK?} --> |Yes| PULL
    {Commit OK?} --> |No| AMEND

    AMEND[Amend commit<br/>- git commit --amend<br/>- Fix message<br/>- Or add forgotten files] --> PULL

    CHECK_BRANCH[Verify branch<br/>- Are you on correct branch?<br/>- Should you create new branch?<br/>- Check branch naming convention] --> {Correct branch?}

    {Correct branch?} --> |Yes| PULL
    {Correct branch?} --> |No| SWITCH

    SWITCH[Switch or create branch<br/>- git checkout -b feature/xxx<br/>- Or git switch feature/xxx<br/>- Verify with git branch] --> PULL

    PULL[Pull latest changes<br/>- git pull --rebase origin main<br/>- Resolve conflicts if any<br/>- Verify rebase completed] --> {Conflicts?}

    {Conflicts?} --> |Yes| RESOLVE
    {Conflicts?} --> |No| PUSH

    RESOLVE[Resolve conflicts<br/>- Open conflicted files<br/>- Fix markers <<<<<<<br/>- git add resolved files<br/>- git rebase --continue] --> {Resolved?}

    {Resolved?} --> |Yes| PUSH
    {Resolved?} --> |No| ABORT

    ABORT[Abort rebase<br/>- git rebase --abort<br/>- Investigate conflict cause<br/>- Try different approach] --> END_ABORT

    END_ABORT[Stop and report<br/>- Explain why cannot push<br/>- Suggest next steps] --> END

    PUSH[Push to remote<br/>- git push origin branch-name<br/>- Or git push -u origin branch<br/>- Verify push succeeded] --> VERIFY

    VERIFY[Verify push<br/>- Check git status clean<br/>- Verify on remote (GitHub/GitLab)<br/>- Confirm CI triggered if any] --> {Push OK?}

    {Push OK?} --> |Yes| DONE
    {Push OK?} --> |No| FIX_PUSH

    FIX_PUSH[Fix push issues<br/>- Check remote URL<br/>- Check permissions<br/>- Force push if needed (careful!)<br/>- git push --force-with-lease] --> VERIFY

    DONE[Done<br/>- Branch pushed successfully<br/>- Ready for PR/MR<br/>- Share branch name if needed] --> END([End])
```

## Commit Convention

```
type(scope): subject

body (optional)

footer (optional)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(auth): add OAuth2 login`
- `fix(api): handle null response`
- `docs(readme): update setup instructions`

## Safety Rules

- Always pull before push
- Use `--force-with-lease` instead of `--force`
- Never push directly to `main`/`master`
- Check what you're pushing with `git log origin/main..HEAD`
