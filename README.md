# Game Workflow (Prototype)

A structured, AI-collaborative workflow for building game prototypes — from raw idea to playable prototype, one stage at a time.

---

## What This Is

This is not a tool. It is a **process**.

A sequence of stages, each with a defined goal, a persona, concrete input artifacts, and concrete output artifacts. You run it with an LLM CLI (Claude Code, Gemini CLI, or any tool that supports `AGENTS.md`). The AI plays a role in each stage — asking questions, proposing designs, writing code — and you approve, adjust, and steer.

The workflow is specialized for **game development with Bevy/Rust**, producing a graybox prototype using geometric primitives, then replacing them with real assets and sound.

---

## Core Philosophies

### 1. Collaborative by Design — AI Proposes, You Approve

Every significant decision goes through a propose-approve loop. The AI suggests a mechanic implementation, a visual language, an asset pipeline approach. You say yes, no, or adjust. Nothing is implemented without your sign-off.

### 2. Personas Per Stage — Not a Generic Assistant

Each stage has a defined persona with a specific responsibility:
- **Creative Director** — asks questions until the game idea is clear
- **Knowledge Auditor** — maps what you know and what needs research
- **Research Analyst** — fills knowledge gaps with targeted research
- **Game Designer** — identifies mechanics and writes feel contracts
- **Technical Designer** — defines the graybox visual language
- **Senior Rust/Bevy Developer** — implements mechanics and scaffolding
- **Code Mentor** — guides you through implementing mechanics yourself
- **Art Director / Sound Designer** — define and produce assets
- **Workflow Engineer** — fixes the workflow itself

### 3. Artifacts as Context Bridges

Every stage consumes specific input artifacts and produces specific output artifacts. The output of one stage is the input of the next. Sessions can end at any time — the artifacts capture the state.

### 4. Stage 0 — The Workflow Improves Itself

Stage 0 (Meta-Workflow) is a dedicated stage for fixing the workflow itself.

### 5. Prototype Mindset

The workflow produces a **playable graybox prototype** using Bevy primitive meshes (Cuboid, Sphere, Capsule, Cylinder, Plane) before any real assets exist. Mechanics are validated first; polish comes after.

### 6. Logs as Institutional Memory

Every stage session is exported as a human-readable transcript. Auto-export runs every 5 minutes during a session (crash protection). A final export is made at the end of each stage.

### 7. Tool-Agnostic by Design

The canonical workflow instructions live in `AGENTS.md`. Tool-specific configuration (`.claude/`, `.gemini/`) contains only thin wrappers that delegate to the canonical layer in `.agent-utils/`.

---

## The Four Phases

| Phase | Goal | Key Outputs |
|-------|------|-------------|
| **gameconcept** | Clarify the game idea, audit knowledge, fill gaps | `game-brief.md`, `knowledge-audit.md`, `research-findings.md` |
| **graybox** | Spec mechanics, build a Bevy prototype with geometric primitives | `mechanic-spec.md`, `graybox-visual-language.md`, `graybox-prototype/` |
| **asset** | Define art direction, produce 2D/3D assets, integrate into Bevy | `art-direction.md`, `asset-list.md`, sprite sheets / GLTF models |
| **sound** | Define sonic identity, produce SFX, integrate into Bevy | `sound-direction.md`, `sound-event-list.md`, `.ogg` files |

### On-Demand Stages

| Stage | Purpose |
|-------|---------|
| **Stage 0** — Meta-Workflow | Fix the workflow itself |
| **Stage teacher** — Teacher | Socratic learning sessions, rubber duck mode, and knowledge testing |

### What It Produces

- A playable Bevy/Rust prototype with all core mechanics implemented
- Graybox prototype with geometric primitives (validated before asset production)
- 2D sprites, 3D models, or mixed assets — integrated and animating in Bevy
- SFX suite sourced, edited, and integrated into Bevy
- Complete game design documentation (`game-brief.md`, `mechanic-spec.md`, `art-direction.md`, `sound-direction.md`, and more)

---

## Prerequisites

**Required:**
- An LLM CLI that supports `AGENTS.md` (Claude Code recommended)
- Python 3 (workflow scripts)
- bash (hook scripts)
- Rust + Cargo (game engine — see [rustup.rs](https://rustup.rs))
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
echo "Rust:      $(rustc --version 2>/dev/null || echo 'NOT FOUND')"
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
   /start-stage gameconcept-1
   ```

4. **Follow the stage**. The AI will adopt the Creative Director persona and ask about your game idea. Answer, discuss, and at the end of the session, export the log:
   ```bash
   /export-log gameconcept-1
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
├── graybox-prototype/           ← Bevy graybox prototype code
├── docs/
│   ├── logs/                    ← Conversation logs (one per stage session)
│   ├── assets/                  ← Diagrams, concept art, textures
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── stages/
    │   ├── phase-0/             ← On-demand stages (meta-workflow, teacher)
    │   ├── gameconcept/         ← Game Concept stages
    │   ├── graybox/             ← Graybox Prototype stages
    │   ├── asset/               ← Asset Pipeline stages
    │   └── sound/               ← Sound Pipeline stages
    ├── shared/                  ← Shared protocols
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts (log export, auto-export)
```

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/start-stage gameconcept-1` | Start a specific stage |
| `/start-stage 0` | Start the Meta-Workflow (fix workflow issues) |
| `/start-stage teacher` | Start a teaching / knowledge-test session |
| `/export-log gameconcept-1` | Export the current session log |

---

## The Workflow Changelog

Every change to the workflow itself is logged in [`docs/workflow-changelog.md`](docs/workflow-changelog.md). This file is the record of how the workflow evolved — what problems were found, what was fixed, and why.
