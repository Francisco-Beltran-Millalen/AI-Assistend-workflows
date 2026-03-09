# GAME-AGENT.md — Game Branch Context

This file contains the full context for the **Game development** branch.
Read this after identifying the active branch in `AGENTS.md`.

---

## Stage Files

### On-Demand Stages

Same on-demand stages as Web. All on-demand stage files exist under `workflow/game/stages/phase-0/`. Most are identical to the Web versions — `00-meta-workflow.md` and `01-diagram-assistant.md` are domain-adapted (e.g., Game references state diagrams and mechanic flowcharts instead of ER diagrams and use case flows).

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/game/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `workflow-changelog.md` |
| diagram | `workflow/game/stages/phase-0/01-diagram-assistant.md` | Visual Communicator | `assets/diagrams/*.md` |
| import | `workflow/game/stages/phase-0/02-import-artifact.md` | Artifact Importer | `imported-artifacts/*-imported.md` |
| knowledge | `workflow/game/stages/phase-0/03-knowledge-tester.md` | Interview Coach | No artifacts |
| teacher | `workflow/game/stages/phase-0/04-teacher.md` | Patient Teacher | No artifacts |
| git | `workflow/game/stages/phase-0/05-git-assistant.md` | Version Control Engineer | No artifacts |

### Phase 1: Discovery + Tech Selection

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 1-1 | `workflow/game/stages/phase-1/01-project-definition.md` | Project Initiator | `project-brief.md` |
| 1-2 | `workflow/game/stages/phase-1/02-knowledge-audit.md` | Knowledge Auditor | `knowledge-audit.md` |
| 1-3 | `workflow/game/stages/phase-1/03-research.md` | Research Analyst | `research-findings.md` |
| 1-4 | `workflow/game/stages/phase-1/04-mechanic-discovery.md` | Mechanic Analyst | `mechanics.md` |
| 1-5 | `workflow/game/stages/phase-1/05-tech-selection.md` | Tech Lead | `tech-stack.md`, `adrs/` |
| 1-6 | `workflow/game/stages/phase-1/06-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-1-consolidation.md`** |

### Phase 2: Game Design

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 2-1 | `workflow/game/stages/phase-2/01-core-loop-design.md` | Game Designer | `core-loop.md` |
| 2-2 | `workflow/game/stages/phase-2/02-entity-design.md` | Game Designer + Systems Designer | `entity-design.md` |
| 2-3 | `workflow/game/stages/phase-2/03-level-design.md` | Level Designer | `level-design.md` *(optional — skip if no levels)* |
| 2-4 | `workflow/game/stages/phase-2/04-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-2-consolidation.md`** |

### Phase 3: Visual & Audio Design

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 3-1 | `workflow/game/stages/phase-3/01-visual-design.md` | Visual Designer | `visual-design.md` |
| 3-2 | `workflow/game/stages/phase-3/02-audio-design.md` | Audio Designer | `audio-design.md` |
| 3-3 | `workflow/game/stages/phase-3/03-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-3-consolidation.md`** |

### Phase 4: Prototype Implementation

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 4-1 | `workflow/game/stages/phase-4/01-project-setup.md` | Senior Developer | Architecture pattern, implementation roadmap, `prototype-code/` skeleton, `implementation-decisions.md` |
| 4-2 | `workflow/game/stages/phase-4/02-implementation-loop.md` | Senior Developer | Working prototype, `implementation-decisions.md` |
| 4-3 | `workflow/game/stages/phase-4/03-learning-guide.md` | Code Mentor | Working prototype, `implementation-decisions.md` |
| 4-4 | `workflow/game/stages/phase-4/04-refactor.md` | Senior Architect | Refactored prototype, `implementation-decisions.md` (refactoring section) |

**Stage 4-1** establishes the architecture pattern, its binding rules, and the approved mechanic implementation order — before any code is written.

**Stages 4-2 and 4-3 are alternatives** — use 4-2 (AI implements, you review) or 4-3 (you implement, AI guides) per mechanic. Both repeat until all mechanics are complete, following the architectural rules from Stage 4-1.

**Stage 4-4** runs once after all mechanics are implemented. Audits the codebase, proposes a refactor roadmap (loop purity, input abstraction, constants, entity patterns, state management, audio decoupling), then refactors one area at a time.

### Phase 5: Distribution

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 5-1 | `workflow/game/stages/phase-5/01-distribution.md` | Deployment Engineer | Distributed prototype |

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

### Phase 4 → Phase 5: Distribution

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

## Artifact Storage

- Stage files: `workflow/game/stages/phase-N/`

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
