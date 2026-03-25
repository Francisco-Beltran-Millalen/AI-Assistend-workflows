# Branch Information

**Branch name:** `web`
**Objective:** Build web application prototypes with REST endpoints and SQL persistence — from idea to deployed working code.
**Workflow path:** `workflow/stages/`
**Agent file:** `AGENTS.md`

## What this branch is for

Use this branch when building a web application with:
- A browser-based UI
- A REST API (JSON over HTTP)
- A SQL database (PostgreSQL)

## How to use

Clone this branch only:

```bash
git clone --branch web --single-branch <repo-url> my-project
cd my-project
claude  # or: gemini, etc.
/start-stage 1-1
```

## Cross-branch decisions

Changes that affect all workflow branches are documented in the `main` branch at `docs/cross-branch-decisions.md`.
