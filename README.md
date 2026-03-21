# Workflow Repository

This repository contains structured, AI-collaborative workflows for building software prototypes — from raw idea to working code.

---

## Why Branches?

Each workflow branch is **self-contained and isolated** from the others.

**The reason:** Different software domains require fundamentally different processes. A web workflow (REST endpoints, data modeling, UI polish, SQL persistence) does not translate to a game workflow (core loop design, mechanic discovery, geometric primitive visuals, update/render cycle). Sharing these contexts in one branch would pollute the AI's working context with irrelevant stage files, artifacts, and terminology — and vice versa.

**The rule:** One branch = one workflow. When you start a new project, clone only the branch for your domain.

---

## Available Workflow Branches

| Branch | Domain | Clone command |
|--------|--------|---------------|
| `web` | Web applications (REST + SQL) | `git clone --branch web --single-branch <url> my-project` |
| `game` | Game development (Godot/GDScript) | `git clone --branch game --single-branch <url> my-game` |
| `game-bevy` | Game development (Bevy/Rust) | `git clone --branch game-bevy --single-branch <url> my-game` |

Each branch contains its own `BRANCH-INFORMATION.md` with the branch name, objective, and workflow path.

---

## This Branch (main)

`main` is **not** a workflow branch. Do not work from `main`. Clone the branch for your domain instead.

`main` contains:
- This README
- `docs/cross-branch-decisions.md` — decisions that affect all branches
- `workflow/shared/` — shared protocols (source of truth; duplicated into each branch)
- `workflow/scripts/` — automation scripts (source of truth; duplicated into each branch)
- `workflow/templates/` — output templates (source of truth; duplicated into each branch)

---

## Cross-Branch Decisions

When a change affects multiple branches (e.g., a shared persona is updated, a Stage 0 process changes, a new Phase 1 stage is added), document it in [`docs/cross-branch-decisions.md`](docs/cross-branch-decisions.md) **before** applying it to each branch.

This prevents forgetting to apply the same change everywhere and explains *why* decisions were made when you revisit them months later.

---

## Shared Resources

The `workflow/shared/`, `workflow/scripts/`, and `workflow/templates/` directories in `main` are the **source of truth** for content that is duplicated into each workflow branch. Each branch has its own copy of these files (required for self-contained cloning). When you update a shared file, update it here first, then apply the change to each branch, and log it in `docs/cross-branch-decisions.md`.

---

## Adding a New Workflow Branch

1. Create a new branch from the existing branch closest in structure to your new domain
2. Strip out irrelevant content and adapt stage files to the new domain
3. Add a `BRANCH-INFORMATION.md` to the new branch
4. Add a row to the table in this README
5. Log the addition in `docs/cross-branch-decisions.md`
