# Cross-Branch Decisions

This document logs decisions that affect all workflow branches, or decisions that apply to a stage that exists across multiple branches (e.g., Phase 0 personas, Phase 1 stages).

When you change a shared concept in one branch, document it here so you know to apply the same change to other branches and remember why it was made.

---

## Format

```markdown
## YYYY-MM-DD: Brief Description

**Scope:** Which branches are affected (`web`, `game`, or `all`)
**Stage(s):** Which stages are affected (e.g., `phase-0/00-meta-workflow`, `phase-1/01-project-definition`, or `all`)
**Change:** What was changed
**Reason:** Why it was changed
**Applied to:** Which branches have already been updated
```

---

## 2026-03-17: Repository restructured to per-branch architecture

**Scope:** all
**Stage(s):** all
**Change:** Each workflow (web, game) moved to its own isolated git branch. Paths simplified from `workflow/<branch>/stages/` to `workflow/stages/`. `WEB-AGENT.md` and `GAME-AGENT.md` merged into `AGENTS.md` per branch. `BRANCH-INFORMATION.md` added to each branch. `start-stage` skill simplified (no branch detection). `main` branch stripped to meta-only (README + this file + shared sources of truth).
**Reason:** Web and game contexts are too different to share a branch. Cloning the full repo for a web project would pollute the agent context with game workflow files and terminology, and vice versa.
**Applied to:** `web`, `game`, `main`
