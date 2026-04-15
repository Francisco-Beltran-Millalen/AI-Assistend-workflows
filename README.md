# Game Workflow (Prototype)

A structured, AI-collaborative workflow for building game prototypes — from raw idea to playable prototype, one stage at a time.

---

## What This Is

This is not a tool. It is a **process**.

A sequence of stages, each with a defined goal, a persona, concrete input artifacts, and concrete output artifacts. You run it with an LLM CLI (Claude Code, Gemini CLI, or any tool that supports `AGENTS.md`). The AI plays a role in each stage — asking questions, proposing designs, writing code — and you approve, adjust, and steer.

The workflow is specialized for **game development with Godot/GDScript**, producing a graybox prototype using geometric primitives, then replacing them with real assets and sound.

---

## Core Philosophies

### 1. Collaborative by Design — AI Proposes, You Approve

Every significant decision goes through a propose-approve loop. The AI suggests a mechanic implementation, a visual language, an asset pipeline approach. You say yes, no, or adjust. Nothing is implemented without your sign-off.

### 2. Personas Per Stage — Not a Generic Assistant

Each stage has a defined persona with a specific responsibility:
- **Creative Director** — asks questions until the game idea is clear
- **Systems Architect** — establishes system boundaries and constraints
- **Game Designer** — identifies mechanics and writes feel contracts
- **Systems Designer** — matches mechanics to architecture to create execution blueprints
- **Plan Generator** — translates blueprints into file-by-file execution plans
- **Code Writer** — executes plans by writing Godot code
- **Auditor** — strictly reviews written code against architectural constraints

### 3. Artifacts as Context Bridges

Every stage consumes specific input artifacts and produces specific output artifacts. The output of one stage is the input of the next. Sessions can end at any time — the artifacts capture the state.

### 4. Stage 0 — The Workflow Improves Itself

Stage 0 (Meta-Workflow) is a dedicated stage for fixing the workflow itself.

### 5. Prototype Mindset

The workflow produces a **playable graybox prototype** using Godot primitive meshes (BoxMesh, SphereMesh, CapsuleMesh, CylinderMesh, PlaneMesh) before any real assets exist. Mechanics are validated first; polish comes after.

### 6. Logs as Institutional Memory

Every stage session is exported as a human-readable transcript. Auto-export runs every 5 minutes during a session (crash protection). A final export is made at the end of each stage.

### 7. Tool-Agnostic by Design

The canonical workflow instructions live in `AGENTS.md`. Tool-specific configuration (`.claude/`, `.gemini/`) contains only thin wrappers that delegate to the canonical layer in `.agent-utils/`.

---

## The Four Phases

| Phase | Goal | Key Outputs |
|-------|------|-------------|
| **gdd-kickstart** | Clarify the game idea, audit knowledge, fill gaps | `human-gdd.md`, `agent-gdd.xml` |
| **architecture** | Define system boundaries, data flow, and components | `docs/architecture/*.md` |
| **mechanic** | Spec mechanics, create isolated mechanic blueprints | `mechanic-spec.md`, `mechanic-designs/*.md` |
| **graybox** | Execute blueprints using a multi-agent pipeline in Godot | `execution-plans/*.md`, `graybox-prototype/` |
| **asset** | Define art direction, produce 2D/3D assets, integrate into Godot | `art-direction.md`, `asset-list.md`, sprite sheets / GLTF models |
| **sound** | Define sonic identity, produce SFX, integrate into Godot | `sound-direction.md`, `sound-event-list.md`, `.ogg files / .wav files` |

### On-Demand Stages

| Stage | Purpose |
|-------|---------|
| **Stage 0** — Meta-Workflow | Fix the workflow itself |
| **Stage teacher** — Teacher | Socratic learning sessions, rubber duck mode, and knowledge testing |

### What It Produces

- A playable Godot/GDScript prototype with all core mechanics implemented
- Graybox prototype with geometric primitives (validated before asset production)
- 2D sprites, 3D models, or mixed assets — integrated and animating in Godot
- SFX suite sourced, edited, and integrated into Godot
- Complete set of design blueprints (`human-gdd.md`, `mechanic-spec.md`, `art-direction.md`, `sound-direction.md`, architecture docs, etc.)

---

## Prerequisites

**Required:**
- An LLM CLI that supports `AGENTS.md` (Claude Code recommended)
- Python 3 (workflow scripts)
- bash (hook scripts)
- Godot Engine 4.6+ (executable in PATH recommended)
- Git

**Required for asset phase:**
- Krita (2D art) — [krita.org](https://krita.org)
- Blender (3D modeling) — [blender.org](https://blender.org) *(3D/mixed track only)*
- Material Maker (procedural textures) *(optional)*

**Required for sound phase:**
- Audacity (audio editing) — [audacityteam.org](https://www.audacityteam.org)

**Quick check:**
```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "Godot:     $(godot --version 2>/dev/null || echo 'NOT FOUND')"
echo "git:       $(git --version 2>/dev/null || echo 'NOT FOUND')"
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

3. **Start the first stage** to begin the game concept phase
   ```bash
   /start-stage gdd-1
   ```

4. **Follow the stage**. The AI will adopt the Creative Director persona and ask about your game idea. Answer, discuss, and at the end of the session, export the log:
   ```bash
   /export-log gdd-1
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
├── .agent-utils/
│   └── skills/                  ← Canonical, tool-agnostic skill content
├── imported-artifacts/          ← Raw imports + adapted *-imported.md files
├── graybox-prototype/           ← Godot graybox prototype code
├── docs/
│   ├── logs/                    ← Conversation logs (one per stage session)
│   ├── assets/                  ← Diagrams, concept art, textures
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── stages/
    │   ├── phase-0/             ← On-demand stages (meta-workflow, teacher)
    │   ├── gdd-kickstart/       ← GDD Kickstart stages
    │   ├── architecture/        ← System Architecture stages
    │   ├── mechanic/            ← Mechanic Analysis stages
    │   ├── graybox/             ← Graybox Prototype stages
    │   ├── asset/               ← Asset Pipeline stages
    │   ├── sound/               ← Sound Pipeline stages
    │   ├── writing/             ← Game Writing stages
    │   ├── testing/             ← Unit Testing stages
    │   ├── feel/                ← Feel & Details stages
    │   ├── fusion/              ← Fusion stages
    │   └── legacy/              ← Archived stages
    ├── shared/                  ← Shared protocols
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts (log export, auto-export)
```

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/start-stage gdd-1` | Start a specific stage |
| `/start-stage 0` | Start the Meta-Workflow (fix workflow issues) |
| `/start-stage teacher` | Start a teaching / knowledge-test session |
| `/export-log gdd-1` | Export the current session log |

---

## The Workflow Changelog

Every change to the workflow itself is logged in [`docs/workflow-changelog.md`](docs/workflow-changelog.md). This file is the record of how the workflow evolved — what problems were found, what was fixed, and why.
