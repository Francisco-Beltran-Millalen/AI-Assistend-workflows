# AGENTS.md - Project Instructions

## Workflow System

This project uses a structured **Web Workflow** — a specialized workflow for building web applications with REST endpoints and SQL persistence.

### Branching Architecture

**Phase 1 is generic** — it works for any software project (discovery, knowledge audit, research, use cases, tech selection, consolidation).

**At Phase 2, the workflow branches by project type.** Choose the branch that matches what you're building:

| Branch | Status | Path |
|--------|--------|------|
| **Web (REST + SQL)** | Active | `workflow/web/` |
| **Game development** | Active | `workflow/game/` |
| CLI development | Planned | — |
| Mobile development | Planned | — |
| Desktop development | Planned | — |

**After identifying the active branch, read the branch-specific agent file before doing any work:**
- Web branch active → read `WEB-AGENT.md`
- Game branch active → read `GAME-AGENT.md`

### Web Branch Phases

1. **Phase 1: Discovery + Tech Selection** (6 stages) — Understand what to build and pick the stack *(generic — applies to any branch)*
2. **Phase 2: Sketching & Data Modeling** (4 stages) — Design entities, data, endpoints, and UI sketches
3. **Phase 3: UI Polish** (5 stages) — Style the views
4. **Phase 4: Prototype Implementation** (4 stages: setup + alternating implementation loop + refactor) — Build it, use case by use case
5. **Phase 5: Deployment** (skeleton) — Deploy the prototype to a real environment

**This workflow produces a working prototype.** Phase 5 handles deployment; a separate "Correctness Workflow" (future) takes the prototype to production quality.

### Game Branch Phases

1. **Phase 1: Discovery + Tech Selection** (6 stages) — Understand what to build and pick the engine *(largely generic — Stage 1-4 adapted for mechanics)*
2. **Phase 2: Game Design** (4 stages) — Core loop, entities, level design (optional), consolidation
3. **Phase 3: Visual & Audio Design** (3 stages) — Primitive visual specs, audio plan, consolidation
4. **Phase 4: Prototype Implementation** (4 stages: setup + alternating implementation loop) — Build mechanic by mechanic
5. **Phase 5: Distribution** (skeleton) — Package and share the prototype

**This workflow produces a playable game prototype using geometric primitives (rectangles, circles, triangles) for all visual assets.** Real asset production strategy is defined separately.

**Before doing any work, identify which stage we're in and read the corresponding stage file.**

## Conversation Logging

Each stage session should produce one final log file.

### Logging Strategy

- **During session**: Auto-export runs every 5 minutes for crash protection (temporary)
- **On stage completion**: Export the final log using `/export-log <phase>-<stage>`
- **Off-stage conversations**: No logs kept (can be reviewed manually if needed)

### Exporting Logs

At the end of each stage session:

```bash
/export-log 2-1
```

This creates: `docs/logs/stage-2-1-entity-ui-sketching-20260203-143022.txt`

### Log Naming Convention

Format: `stage-<phase>-<stage>-<name>-<YYYYMMDD>-<HHMMSS>.txt`

Examples (Web branch):
- `stage-00-meta-workflow-20260203-091500.txt`
- `stage-1-4-use-case-discovery-20260203-143022.txt`
- `stage-2-1-entity-ui-sketching-20260204-101530.txt`

Examples (Game branch):
- `stage-1-4-mechanic-discovery-20260203-143022.txt`
- `stage-2-1-core-loop-design-20260204-101530.txt`

## On-Demand Stages

**On-demand stages** are not part of the phase cycle. Invoke them anytime:
- **Stage 0** (`/start-stage 0`) — Fix workflow issues
- **Stage diagram** (`/start-stage diagram`) — Generate diagrams and visual aids from artifacts
- **Stage import** (`/start-stage import`) — Import external artifacts and adapt them to workflow format
- **Stage knowledge** (`/start-stage knowledge`) — Pre-meeting knowledge check (quiz yourself on all decisions)
- **Stage teacher** (`/start-stage teacher`) — Socratic teaching sessions (explain concepts, rubber duck mode)
- **Stage git** (`/start-stage git`) — Git and version control operations

On-demand stage files are at `workflow/{branch}/stages/phase-0/` (e.g., `workflow/web/stages/phase-0/` or `workflow/game/stages/phase-0/`).

## Critical Rules

1. **ALWAYS read the stage file** before starting work
2. **ALWAYS adopt the persona** defined in the stage file
3. **ALWAYS use `/start-stage`** to start stages — it automatically runs the Existing Artifact Protocol, which detects prior runs and asks how to proceed before any work begins
4. **In Phase 4: ALWAYS read `implementation-decisions.md` first** — it tracks progress and decisions across sessions *(Web branch: also applies to Phase 3 via `phase-3-design-decisions.md` — see WEB-AGENT.md)*
5. **Follow stage order** within each phase
6. **Complete each phase before starting the next**

## Quick Commands

### Slash Commands (Skills)

- `/start-stage <phase>-<stage>` → Start a specific stage (e.g., `/start-stage 2-1`)
- `/start-stage 0` → Meta-Workflow (fix workflow issues)
- `/start-stage diagram` → Diagram Assistant (visualize artifacts)
- `/start-stage import` → Import an external artifact into workflow format
- `/start-stage knowledge` → Knowledge Tester (pre-meeting quiz)
- `/start-stage teacher` → Teacher (Socratic learning sessions)
- `/start-stage git` → Git Assistant (version control operations)
- `/export-log <phase>-<stage>` → Export conversation to docs/logs/

### Natural Language

- "Start stage 0" → Meta-Workflow (fix workflow issues)
- "Start stage 2-1" → Entity & UI Sketching
- "What stage are we in?" → Check docs/ for artifacts
- "Export the log" → Save conversation

### Built-in Claude Code Commands

- `/export <file>` → Export conversation
- `/compact` → Compress long conversations
- `/context` → See context usage
- `/cost` → See token usage

## Project Structure

```
project-root/
├── AGENTS.md                    ← You are here (shared entry point — canonical)
├── WEB-AGENT.md                 ← Full web branch context
├── GAME-AGENT.md                ← Full game branch context
├── CLAUDE.md                    ← Claude Code redirect to AGENTS.md
├── GEMINI.md                    ← Gemini redirect to AGENTS.md
├── .claude/
│   ├── settings.json            ← Hooks configuration
│   └── skills/                  ← Custom slash commands
│       ├── start-stage/         ← /start-stage <phase>-<stage>
│       └── export-log/          ← /export-log <phase>-<stage>
├── .agent-utils/
│   └── skills/                  ← Canonical, tool-agnostic skill content
│       ├── start-stage/
│       └── export-log/
├── imported-artifacts/          ← Raw imports + adapted *-imported.md files (Stage I)
├── consolidation-artifacts/     ← Phase milestone documents (committed to git)
├── prototype-code/              ← Working prototype code (committed to git)
├── docs/
│   ├── logs/                    ← Conversation logs
│   ├── assets/                  ← Views, CSS, SQL, diagrams
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── web/                     ← ACTIVE WORKFLOW (Web: REST + SQL)
    │   └── stages/
    │       ├── phase-0/         ← Meta-workflow (on-demand)
    │       ├── phase-1/         ← Discovery + Tech Selection (generic)
    │       ├── phase-2/         ← Sketching & Data Modeling
    │       ├── phase-3/         ← UI Polish
    │       ├── phase-4/         ← Prototype Implementation
    │       └── phase-5/         ← Deployment (skeleton)
    ├── game/                    ← ACTIVE WORKFLOW (Game development)
    │   └── stages/
    │       ├── phase-0/         ← Meta-workflow (on-demand)
    │       ├── phase-1/         ← Discovery + Tech Selection (generic)
    │       ├── phase-2/         ← Game Design
    │       ├── phase-3/         ← Visual & Audio Design
    │       ├── phase-4/         ← Prototype Implementation
    │       └── phase-5/         ← Distribution (skeleton)
    ├── shared/                  ← Shared protocols (Existing Artifact Protocol)
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts
```

## Artifact Storage

- Phase milestone documents: `consolidation-artifacts/`
- Working prototype code: `prototype-code/`
- Working design artifacts: `docs/`
- Assets (views, CSS, SQL): `docs/assets/`
- Architecture decisions: `docs/adrs/`
- Conversation logs: `docs/logs/`
- Workflow changelog: `docs/workflow-changelog.md`
