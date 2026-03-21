# Writing Workflow

A structured, AI-collaborative workflow for developing stories — from raw idea to written chapters, one stage at a time.

---

## What This Is

This is not a tool. It is a **process**.

A sequence of stages, each with a defined goal, a persona, concrete input artifacts, and concrete output artifacts. You run it with an LLM CLI (Claude Code, Gemini CLI, or any tool that supports `AGENTS.md`). The AI plays a role in each stage — asking questions, proposing designs, writing alongside you — and you approve, adjust, and steer.

The workflow is designed for **long-form story development**: web novels, traditional novels, manga scripts, screenplays, game narratives. The philosophy is generic and can be adapted to any narrative format.

---

## Core Philosophies

### 1. Collaborative by Design — AI Asks, You Answer, You Write

The AI's primary role is to help you think — not to write for you. In the design phases (1–5), the AI asks questions to help you discover and articulate your story. In the writing phase (6), the AI asks structured questions to help you see a scene clearly before you write it.

You are always in control. The AI keeps you oriented and unstuck.

### 2. Personas Per Stage

Each stage has a defined persona with a specific responsibility:

- **Format Analyst** — determines the target medium and its constraints
- **Story Conceiver** — helps crystallize the emotional core
- **World Builder** — designs the systems and rules of the world
- **Writing Companion** — asks the questions that clarify scenes before you write them
- **Story Editor** — reviews and improves what's already written

The persona frames what the AI pays attention to and what it ignores. An editor does not redesign the world. A world builder does not draft chapters.

### 3. Artifacts as Context Bridges

Every stage consumes specific input artifacts and produces specific output artifacts. The output of one stage is the input of the next.

Sessions can end at any time. New sessions start by reading artifacts. The workflow does not depend on conversation memory — it depends on files.

### 4. General to Specific — The Writing Method

In Phase 6, every chapter starts with a rough description and drills down to scene-level clarity through structured questions. The AI presents a burst of targeted questions drawn from the design artifacts, then continues conversationally if needed. You write once you're clear on the scene.

### 5. Multi-Level Review

Phase 7 operates at three scopes:
- **Chapter** — make this chapter better
- **Book** — does the whole book flow? Are there structural problems?
- **Series** — does the series hold together? Are cross-book arcs satisfying?

Each scope has a distinct persona and process.

### 6. Phase 0 — The Workflow Improves Itself

Stage 0 (Meta-Workflow) is a dedicated stage for fixing the workflow itself. Diagnose, fix, document. Every improvement is logged to `docs/workflow-changelog.md`.

### 7. Tool-Agnostic by Design

Canonical instructions live in `AGENTS.md`. Tool-specific configuration (`.claude/`, `.gemini/`) contains only thin wrappers delegating to `.agent-utils/`.

---

## The Seven Phases

| Phase | Name | Goal | Stages |
|-------|------|------|--------|
| **1** | Concept & Foundation | Define the story's core, protagonist, world states, antagonists, key events | 8 stages |
| **2** | World & Rules | Build the world's systems, cultures, politics, and narrative voice | 9 stages |
| **3** | Sensory & Identity | Define how the world looks, sounds, feels, and how characters speak | 7 stages |
| **4** | Narrative Arcs | Design the thematic conflict, story arcs, progression, and world consequences | 5 stages |
| **5** | Chapter Planning | Define chapter format, outline all chapters, describe scenes, compile the design package | 4 stages |
| **6** | Writing *(cyclical)* | Write chapters one at a time — session setup, scene expansion, writing, close, design sync | 5 stages per chapter |
| **7** | Review *(on-demand)* | Review at chapter, book, or series level | 3 stages |

### On-Demand Stages

| Stage | Purpose |
|-------|---------|
| **Stage 0** — Meta-Workflow | Fix the workflow itself, run git operations, import external artifacts |

---

## Multiple Stories

Each story is its own isolated entity within this project. All story-specific artifacts live under `docs/<story-name>/`. Multiple stories can coexist without interfering.

---

## Prerequisites

See [`PREREQUISITES.md`](PREREQUISITES.md) for the full list.

**Required:** LLM CLI (Claude Code recommended), Python 3, bash, Git

**Quick check:**
```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "git:       $(git --version 2>/dev/null || echo 'NOT FOUND')"
```

---

## Quick Start

1. **Clone this branch** into your new project directory
   ```bash
   git clone --branch writing --single-branch <repo-url> my-story
   cd my-story
   ```

2. **Open the project** in your LLM CLI
   ```bash
   claude  # or: gemini, cursor, etc.
   ```

3. **Start Stage 1-1** to define the format and medium
   ```bash
   /start-stage 1-1
   ```

4. **Follow the stage.** Export the log at the end of each session:
   ```bash
   /export-log 1-1
   ```

5. **Continue stage by stage.**

---

## Project Structure

```
project-root/
├── BRANCH-INFORMATION.md        ← Branch metadata
├── AGENTS.md                    ← Canonical workflow instructions
├── CLAUDE.md                    ← Claude Code redirect → AGENTS.md
├── GEMINI.md                    ← Gemini CLI redirect → AGENTS.md
├── README.md                    ← You are here
├── PREREQUISITES.md             ← Tool installation requirements
├── .claude/
│   ├── settings.json            ← Hook configuration
│   └── skills/                  ← Claude Code slash commands
├── .agent-utils/
│   └── skills/                  ← Canonical, tool-agnostic skill content
├── imported-artifacts/          ← Raw imports + adapted files (Stage 0)
├── docs/
│   ├── logs/                    ← Conversation logs
│   ├── workflow-changelog.md    ← Workflow improvement log
│   └── <story-name>/            ← All artifacts for a specific story
│       ├── format-medium.md
│       ├── story-seed.md
│       ├── main-character.md
│       ├── ... (all phase 1–5 artifacts)
│       ├── phase-N-consolidation.md
│       ├── story-design-package/
│       │   └── ... (final compiled package)
│       ├── assets/
│       │   ├── images/          ← Mood board / visual references
│       │   └── audio/           ← Playlist / audio references
│       └── chapters/
│           ├── chapter-01.md
│           └── chapter-02.md
└── workflow/
    ├── stages/                  ← Stage files organized by phase
    ├── shared/                  ← Shared protocols
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts
```

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/start-stage 1-1` | Start Stage 1-1: Format & Medium |
| `/start-stage 6-2` | Start Stage 6-2: Chapter Expansion |
| `/start-stage 7-1` | Start Stage 7-1: Chapter Review |
| `/start-stage 0` | Start the Meta-Workflow |
| `/export-log 1-1` | Export the session log for Stage 1-1 |
