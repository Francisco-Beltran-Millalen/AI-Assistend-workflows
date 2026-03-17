# AGENTS.md — Game Workflow (Prototype)

This is the **Game Workflow** — a structured, AI-collaborative process for building playable game prototypes using geometric primitives.

**Branch:** `game` — See `BRANCH-INFORMATION.md` for branch metadata.

**Before doing any work, identify which stage we're in and read the corresponding stage file.**

## Stage Files

### On-Demand Stages

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `workflow-changelog.md` |
| diagram | `workflow/stages/phase-0/01-diagram-assistant.md` | Visual Communicator | `assets/diagrams/*.md` |
| import | `workflow/stages/phase-0/02-import-artifact.md` | Artifact Importer | `imported-artifacts/*-imported.md` |
| knowledge | `workflow/stages/phase-0/03-knowledge-tester.md` | Interview Coach | No artifacts |
| teacher | `workflow/stages/phase-0/04-teacher.md` | Patient Teacher | No artifacts |
| git | `workflow/stages/phase-0/05-git-assistant.md` | Version Control Engineer | No artifacts |

### Phase 1: Discovery + Tech Selection

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 1-1 | `workflow/stages/phase-1/01-project-definition.md` | Project Initiator | `project-brief.md` |
| 1-2 | `workflow/stages/phase-1/02-knowledge-audit.md` | Knowledge Auditor | `knowledge-audit.md` |
| 1-3 | `workflow/stages/phase-1/03-research.md` | Research Analyst | `research-findings.md` |
| 1-4 | `workflow/stages/phase-1/04-mechanic-discovery.md` | Mechanic Analyst | `mechanics.md` |
| 1-5 | `workflow/stages/phase-1/05-tech-selection.md` | Tech Lead | `tech-stack.md`, `adrs/` |
| 1-6 | `workflow/stages/phase-1/06-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-1-consolidation.md`** |

### Phase 2: Game Design

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 2-1 | `workflow/stages/phase-2/01-core-loop-design.md` | Game Designer | `core-loop.md` |
| 2-2 | `workflow/stages/phase-2/02-entity-design.md` | Game Designer + Systems Designer | `entity-design.md` |
| 2-3 | `workflow/stages/phase-2/03-level-design.md` | Level Designer | `level-design.md` *(optional — skip if no levels)* |
| 2-4 | `workflow/stages/phase-2/04-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-2-consolidation.md`** |

### Phase 3: Visual & Audio Design

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 3-1 | `workflow/stages/phase-3/01-visual-design.md` | Visual Designer | `visual-design.md` |
| 3-2 | `workflow/stages/phase-3/02-audio-design.md` | Audio Designer | `audio-design.md` |
| 3-3 | `workflow/stages/phase-3/03-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-3-consolidation.md`** |

### Phase 4: Prototype Implementation

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 4-1 | `workflow/stages/phase-4/01-project-setup.md` | Senior Developer | Architecture pattern, implementation roadmap, `prototype-code/` skeleton, `implementation-decisions.md` |
| 4-2 | `workflow/stages/phase-4/02-implementation-loop.md` | Senior Developer | Working prototype, `implementation-decisions.md` |
| 4-3 | `workflow/stages/phase-4/03-learning-guide.md` | Code Mentor | Working prototype, `implementation-decisions.md` |
| 4-4 | `workflow/stages/phase-4/04-refactor.md` | Senior Architect | Refactored prototype, `implementation-decisions.md` (refactoring section) |

**Stage 4-1** establishes the architecture pattern, its binding rules, and the approved mechanic implementation order — before any code is written.

**Stages 4-2 and 4-3 are alternatives** — use 4-2 (AI implements, you review) or 4-3 (you implement, AI guides) per mechanic. Both repeat until all mechanics are complete, following the architectural rules from Stage 4-1.

**Stage 4-4** runs once after all mechanics are implemented. Audits the codebase, proposes a refactor roadmap (loop purity, input abstraction, constants, entity patterns, state management, audio decoupling), then refactors one area at a time.

### Phase 5: Distribution

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 5-1 | `workflow/stages/phase-5/01-distribution.md` | Deployment Engineer | Distributed prototype |

**Phase 5 is a skeleton** — distribution process will be expanded with real game projects.

---

## Architectural Assumptions

This workflow is scoped to a specific application type:
- **Game** (geometric primitive visuals — rectangles, circles, triangles — for the prototype)
- **Game loop** (update/render cycle, not request/response)
- **No persistent database** for the prototype (game state lives in memory)

Decided in Stage 1-5 (Tech Selection):
- **Engine** — e.g., Pygame, Godot, Phaser, Unity, Raylib
- **Language** — determined by the engine choice
- **Architecture pattern** — chosen in Stage 4-1: Simple OOP or Entity-Component System (ECS)

These are real decision points. The chosen engine and language are recorded in `docs/tech-stack.md` and shape Phase 4. The architecture pattern is chosen in Stage 4-1 and recorded in `consolidation-artifacts/implementation-decisions.md`.

---

## Phase Handoffs

### Phase 1 → Phase 2

Stage 1-6 produces `consolidation-artifacts/phase-1-consolidation.md` (includes prioritized mechanics list and tech stack summary) — the **primary input** for Phase 2.

### Phase 2 → Phase 3

Stage 2-4 consolidates Phase 2 work into `consolidation-artifacts/phase-2-consolidation.md` — the primary artifact forwarded to Phase 3. Also forwarded: `docs/core-loop.md` (Stage 2-1), `docs/entity-design.md` (Stage 2-2), and optionally `docs/level-design.md` (Stage 2-3, if levels apply).

### Phase 3 → Phase 4

Stage 3-3 consolidates all Phase 3 work into `consolidation-artifacts/phase-3-consolidation.md` — a comprehensive spec for colors, shapes, sizes, canvas dimensions, animation descriptions, and audio events. Phase 4 uses all prior artifacts: the mechanic list, entity specs, and visual/audio specs.

### Phase 4 → Phase 5

Phase 4 produces a refactored working prototype: all mechanics implemented, all tests passing, architecture cleaned up (Stage 4-4). Phase 5 packages and distributes it. The process is a skeleton now and will be expanded with real game projects.

---

## How to Determine Current Stage

Check `docs/` for existing artifacts:

**Phase 1 (Discovery + Tech Selection):**
- No artifacts → Stage 1-1
- `project-brief.md` → Stage 1-2
- `knowledge-audit.md` → Stage 1-3
- `research-findings.md` → Stage 1-4
- `mechanics.md` → Stage 1-5
- `tech-stack.md` → Stage 1-6
- `consolidation-artifacts/phase-1-consolidation.md` → Phase 1 complete

**Phase 2 (Game Design):**
- `consolidation-artifacts/phase-1-consolidation.md` exists but no `core-loop.md` → Stage 2-1
- `core-loop.md` → Stage 2-2
- `entity-design.md` → Stage 2-3 (level design, optional — skip if no levels)
- `level-design.md` or confirmed skip → Stage 2-4
- `consolidation-artifacts/phase-2-consolidation.md` → Phase 2 complete

**Phase 3 (Visual & Audio Design):**
- `consolidation-artifacts/phase-2-consolidation.md` exists but no `visual-design.md` → Stage 3-1
- `visual-design.md` → Stage 3-2
- `audio-design.md` → Stage 3-3
- `consolidation-artifacts/phase-3-consolidation.md` → Phase 3 complete

**Phase 4 (Prototype Implementation):**
- `consolidation-artifacts/phase-3-consolidation.md` exists but no `consolidation-artifacts/implementation-decisions.md` → Stage 4-1
- `consolidation-artifacts/implementation-decisions.md` exists (mechanics not all complete) → Stage 4-2 or 4-3 (user's choice per mechanic)
- `consolidation-artifacts/implementation-decisions.md` with all mechanics complete but no `## Refactoring` section → Stage 4-4
- `consolidation-artifacts/implementation-decisions.md` with `## Refactoring` section and refactoring incomplete → Stage 4-4 (resume)
- `consolidation-artifacts/implementation-decisions.md` with all refactor areas complete → **Prototype refactored → Stage 5-1**

---

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

This creates: `docs/logs/stage-2-1-core-loop-design-20260203-143022.txt`

### Log Naming Convention

Format: `stage-<phase>-<stage>-<name>-<YYYYMMDD>-<HHMMSS>.txt`

Examples:
- `stage-00-meta-workflow-20260203-091500.txt`
- `stage-1-4-mechanic-discovery-20260203-143022.txt`
- `stage-2-1-core-loop-design-20260204-101530.txt`

---

## On-Demand Stages

**On-demand stages** are not part of the phase cycle. Invoke them anytime:
- **Stage 0** (`/start-stage 0`) — Fix workflow issues
- **Stage diagram** (`/start-stage diagram`) — Generate diagrams and visual aids from artifacts
- **Stage import** (`/start-stage import`) — Import external artifacts and adapt them to workflow format
- **Stage knowledge** (`/start-stage knowledge`) — Pre-meeting knowledge check (quiz yourself on all decisions)
- **Stage teacher** (`/start-stage teacher`) — Socratic teaching sessions (explain concepts, rubber duck mode)
- **Stage git** (`/start-stage git`) — Git and version control operations

---

## Critical Rules

1. **ALWAYS read the stage file** before starting work
2. **ALWAYS adopt the persona** defined in the stage file
3. **ALWAYS use `/start-stage`** to start stages — it automatically runs the Existing Artifact Protocol, which detects prior runs and asks how to proceed before any work begins
4. **In Phase 4: ALWAYS read `implementation-decisions.md` first** — it tracks progress and decisions across sessions
5. **Follow stage order** within each phase
6. **Complete each phase before starting the next**

---

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

- "Start stage 2-1" → Core Loop Design
- "What stage are we in?" → Check docs/ for artifacts
- "Export the log" → Save conversation

### Built-in Claude Code Commands

- `/export <file>` → Export conversation
- `/compact` → Compress long conversations
- `/context` → See context usage
- `/cost` → See token usage

---

## Project Structure

```
project-root/
├── BRANCH-INFORMATION.md        ← Branch metadata (name, objective, path)
├── AGENTS.md                    ← You are here (canonical workflow instructions)
├── CLAUDE.md                    ← Claude Code redirect to AGENTS.md
├── GEMINI.md                    ← Gemini redirect to AGENTS.md
├── .claude/
│   ├── settings.json            ← Hooks configuration
│   └── skills/                  ← Custom slash commands
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
│   ├── logs/                    ← Conversation logs
│   ├── assets/                  ← Diagrams, design specs
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── stages/                  ← Stage files organized by phase
    │   ├── phase-0/             ← On-demand stages
    │   ├── phase-1/             ← Discovery + Tech Selection
    │   ├── phase-2/             ← Game Design
    │   ├── phase-3/             ← Visual & Audio Design
    │   ├── phase-4/             ← Prototype Implementation
    │   └── phase-5/             ← Distribution (skeleton)
    ├── shared/                  ← Shared protocols (Existing Artifact Protocol)
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts
```

---

## Artifact Storage

- Phase milestone documents: `consolidation-artifacts/`
- Working prototype code: `prototype-code/`
- Working design artifacts: `docs/`
- Design specs: `docs/assets/`
- Architecture decisions: `docs/adrs/`
- Conversation logs: `docs/logs/`
- Workflow changelog: `docs/workflow-changelog.md`

---

## Project Status

> Current phase and stage are determined by checking `docs/` for existing artifacts — see "How to Determine Current Stage" above.

### Meta Artifacts
- [ ] `workflow-changelog.md` ← Workflow fixes log

### Phase 1: Discovery + Tech Selection
- [ ] `project-brief.md`
- [ ] `knowledge-audit.md`
- [ ] `research-findings.md`
- [ ] `mechanics.md`
- [ ] `tech-stack.md`
- [ ] `adrs/` (decision records)
- [ ] **`consolidation-artifacts/phase-1-consolidation.md`** ← Phase 1 complete

### Phase 2: Game Design
- [ ] `core-loop.md`
- [ ] `entity-design.md`
- [ ] `level-design.md` *(optional — skip if no distinct levels)*
- [ ] **`consolidation-artifacts/phase-2-consolidation.md`** ← Phase 2 complete

### Phase 3: Visual & Audio Design
- [ ] `visual-design.md`
- [ ] `audio-design.md`
- [ ] **`consolidation-artifacts/phase-3-consolidation.md`** ← Phase 3 complete

### Phase 4: Prototype Implementation
- [ ] `prototype-code/` created ← Stage 4-1 complete
- [ ] `consolidation-artifacts/implementation-decisions.md` initialized ← Stage 4-1 complete
- [ ] All mechanics implemented + tested (per Implementation Roadmap order)
- [ ] **All tests passing** ← Prototype complete (4-2/4-3 done)
- [ ] Refactor roadmap approved ← Stage 4-4 started
- [ ] All refactor areas complete + comprehension check passed ← Stage 4-4 complete

### Phase 5: Distribution
- [ ] Prototype packaged and distributed ← Phase 5 complete

---

## Final Output

The **Game Workflow** produces a **distributable playable prototype** with:
- All mechanics implemented using geometric primitives
- Tests for logic functions (where applicable)
- Architecturally clean codebase (loop purity, input abstraction, constants, entity patterns)
- Complete game design documentation
- Packaged for distribution
