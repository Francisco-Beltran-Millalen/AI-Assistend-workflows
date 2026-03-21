# Branch Information

**Branch name:** `game-bevy`
**Objective:** Build game prototypes using geometric primitives — from idea to playable distributable prototype, using Bevy/Rust.
**Workflow path:** `workflow/stages/`
**Agent file:** `AGENTS.md`

## What this branch is for

Use this branch when building a game with:
- Geometric primitive visuals (rectangles, circles, meshes) for the prototype
- A game loop (update/render cycle, not request/response)
- No persistent database (game state lives in memory)
- Bevy/Rust as the engine

## How to use

Clone this branch only:

```bash
git clone --branch game-bevy --single-branch <repo-url> my-game
cd my-game
claude  # or: gemini, etc.
/start-stage gameconcept-1
```

## Cross-branch decisions

Changes that affect all workflow branches are documented in the `main` branch at `docs/cross-branch-decisions.md`.
