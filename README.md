# Game Workflow (Prototype)

A structured, AI-collaborative workflow for building game prototypes — from raw idea to playable prototype, one stage at a time.

---

## What This Is

This is not a tool. It is a **process**.

A sequence of stages, each with a defined goal, a persona, concrete input artifacts, and concrete output artifacts. You run it with an LLM CLI (Claude Code, Gemini CLI, or any tool that supports `AGENTS.md`). The AI plays a role in each stage — asking questions, proposing designs, writing code — and you approve, adjust, and steer.

The workflow is specialized for **game development with geometric primitive visuals** (rectangles, circles, triangles). The underlying philosophy is generic and can be adapted to any domain.

---

## Core Philosophies

### 1. Collaborative by Design — AI Proposes, You Approve

Every significant decision goes through a propose-approve loop. The AI suggests a core loop, an entity structure, a mechanic implementation. You say yes, no, or adjust. Nothing is implemented without your sign-off.

### 2. Personas Per Stage — Not a Generic Assistant

Each stage has a defined persona with a specific responsibility:
- **Project Initiator** — asks questions until the idea is clear
- **Mechanic Analyst** — surfaces and prioritizes core game mechanics
- **Game Designer** — designs the core loop and entity system
- **Senior Developer** — implements one mechanic at a time
- **Workflow Engineer** — fixes the workflow itself

### 3. Artifacts as Context Bridges

Every stage consumes specific input artifacts and produces specific output artifacts. The output of one stage is the input of the next. Sessions can end at any time — the artifacts capture the state.

### 4. Phase 0 — The Workflow Improves Itself

Stage 0 (Meta-Workflow) is a dedicated stage for fixing the workflow itself.

### 5. Prototype Mindset

The workflow produces a **playable prototype** using geometric primitives — not a finished game. The goal is to validate mechanics by building something real.

### 6. Logs as Institutional Memory

Every stage session is exported as a human-readable transcript. Auto-export runs every 5 minutes during a session (crash protection). A final export is made at the end of each stage.

### 7. Tool-Agnostic by Design

The canonical workflow instructions live in `AGENTS.md`. Tool-specific configuration (`.claude/`, `.gemini/`) contains only thin wrappers that delegate to the canonical layer in `.agent-utils/`.

---

## This Workflow: Game (Prototype)

The `game` workflow is a specialization for building game prototypes with:
- **Geometric primitive visuals** (rectangles, circles, triangles — no external assets in the prototype)
- **A game loop** (update/render cycle)
- **No persistent database** (game state in memory)

**Engine and language** are chosen in Stage 1-5 (Tech Selection).
**Architecture pattern** (Simple OOP or ECS) is chosen in Stage 4-1.

### The Five Phases

| Phase | Goal | Stages |
|-------|------|--------|
| **Phase 1: Discovery + Tech Selection** | Understand what to build and pick the engine | 6 stages |
| **Phase 2: Game Design** | Design core loop, entities, and level structure | 4 stages |
| **Phase 3: Visual & Audio Design** | Spec primitive shapes, colors, canvas, audio events | 3 stages |
| **Phase 4: Prototype Implementation** | Build it, mechanic by mechanic, then refactor | 4 stages |
| **Phase 5: Distribution** | Package and share the prototype | 1 stage (skeleton) |

### On-Demand Stages

| Stage | Purpose |
|-------|---------|
| **Stage 0** — Meta-Workflow | Fix the workflow itself |
| **Stage diagram** — Diagram Assistant | Visualize any artifact as a Mermaid diagram |
| **Stage import** — Artifact Importer | Bring in an external artifact and adapt it to the workflow's format |
| **Stage knowledge** — Knowledge Tester | Pre-meeting quiz on all decisions made so far |
| **Stage teacher** — Teacher | Socratic learning sessions and rubber duck debugging |
| **Stage git** — Git Assistant | Version control operations |

### What It Produces

- A playable prototype with all mechanics implemented using geometric primitives
- Tests for logic functions (where applicable)
- Architecturally clean codebase
- Complete game design documentation (`project-brief.md`, `mechanics.md`, `core-loop.md`, `entity-design.md`, and more)
- Packaged for distribution

---

## Prerequisites

**Required:**
- An LLM CLI that supports `AGENTS.md` (Claude Code recommended)
- Python 3 (workflow scripts)
- bash (hook scripts)
- Your chosen game engine/framework

**Quick check:**
```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
```

---

## Quick Start

1. **Clone this branch** into your new project directory
   ```bash
   git clone --branch game --single-branch <repo-url> my-game
   cd my-game
   ```

2. **Open the project** in your LLM CLI
   ```bash
   claude  # or: gemini, etc.
   ```

3. **Start Stage 1-1** to begin Discovery
   ```bash
   /start-stage 1-1
   ```

4. **Follow the stage**. The AI will adopt the Project Initiator persona and ask about your game idea. Answer, discuss, and at the end of the session, export the log:
   ```bash
   /export-log 1-1
   ```

5. **Continue stage by stage.** Each stage reads the outputs of the previous one. The workflow guides you.

---

## Project Structure

```
project-root/
├── BRANCH-INFORMATION.md        ← Branch metadata (name, objective, path)
├── AGENTS.md                    ← Canonical workflow instructions (read by all LLM tools)
├── CLAUDE.md                    ← Claude Code redirect → AGENTS.md
├── GEMINI.md                    ← Gemini CLI redirect → AGENTS.md
├── README.md                    ← You are here
├── .claude/
│   ├── settings.json            ← Hook configuration (auto-export, session start)
│   └── skills/                  ← Claude Code slash commands (thin wrappers)
│       ├── start-stage/
│       └── export-log/
├── .agent-utils/
│   └── skills/                  ← Canonical, tool-agnostic skill content
│       ├── start-stage/
│       └── export-log/
├── imported-artifacts/          ← Raw imports + adapted *-imported.md files (Stage I)
├── consolidation-artifacts/     ← Phase milestone documents (committed to git)
├── prototype-code/              ← Working prototype code (committed to git)
├── docs/
│   ├── logs/                    ← Conversation logs (one per stage session)
│   ├── assets/                  ← Diagrams, design specs
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── stages/                  ← Stage files (one per stage, organized by phase)
    ├── shared/                  ← Shared protocols (Existing Artifact Protocol)
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts (log export, auto-export)
```

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/start-stage 1-1` | Start a specific stage (Phase 1, Stage 1) |
| `/start-stage 0` | Start the Meta-Workflow (fix workflow issues) |
| `/start-stage diagram` | Start the Diagram Assistant |
| `/start-stage import` | Start the Artifact Importer |
| `/export-log 1-1` | Export the current session log for Stage 1-1 |

---

## The Workflow Changelog

Every change to the workflow itself is logged in [`docs/workflow-changelog.md`](docs/workflow-changelog.md). This file is the record of how the workflow evolved — what problems were found, what was fixed, and why.
