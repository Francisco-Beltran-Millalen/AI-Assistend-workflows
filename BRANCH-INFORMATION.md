# Branch Information

**Branch name:** `game`
**Objective:** Build game prototypes using geometric primitives — from idea to playable distributable prototype.
**Workflow path:** `workflow/stages/`
**Agent file:** `AGENTS.md`

## What this branch is for

Use this branch when building a game with:
- Geometric primitive visuals (rectangles, circles, triangles) for the prototype
- A game loop (update/render cycle, not request/response)
- No persistent database (game state lives in memory)

## How to use

Clone this branch only:

```bash
git clone --branch game --single-branch <repo-url> my-game
cd my-game
claude  # or: gemini, etc.
/start-stage gameconcept-1
```

## Cross-branch decisions

Changes that affect all workflow branches are documented in the `main` branch at `docs/cross-branch-decisions.md`.
