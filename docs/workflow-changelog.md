# Workflow Changelog

---

## 2026-03-26: graybox-5-designed — 9-level conversation, design journal, architecture enforcement

**Problem:** The 6-level design conversation was too coarse — Behavior mixed logic, edge cases, and signals into one level. No persistent design artifact existed. No architecture enforcement during code generation. No evaluation of user understanding.

**Fix:**
- Expanded to 9 levels: Player Experience → Entity List → Composition → State → Behavior Logic → Edge Behaviors → Signals & Interactions → Scene Map → Godot Mapping
- Level 6 (Edge Behaviors): contextual state conflicts/boundary conditions surfaced with standard Godot solutions, user confirms which apply
- Level 7 (Signals & Interactions): explicit signal contracts with typed params and intended listeners
- Level 8 (Scene Map): ASCII scene tree + call flow diagram
- Level 8b (Architecture Review): verifies scene map against Godot composition rules before code
- Level 9 (Godot Mapping): typed GDScript stubs (not full code)
- Industry standard approach stated at every question and design choice
- Design journal (`docs/mechanic-designs/[mechanic-slug].md`): created at session start, updated section-by-section after each confirmed level — self-contained handoff for future agents
- Edge Case Sweep + Node Contracts before Green Light sign-off
- Code generation: flags architecture violations (sideways/upward node references) before writing
- Comprehension Check (Step 11): user narrates mechanic in natural language from memory — up to 3 attempts with precise corrections

**Files:** `workflow/stages/graybox/05-mechanic-loop-designed.md`

---

## 2026-03-20: Add feel + fusion phases; Bevy → Godot; redesign gameconcept; add graybox-5-designed

**feel phase (on-demand):** 3 independently invocable stages — engine effects per mechanic (`feel-1`), asset feel upgrades (`feel-2`), audio detail per event (`feel-3`). No sequential dependency.

**fusion phase (final):** 1 integration loop stage (`fusion-1`) — wire up code + assets + feel + sound per mechanic. A mechanic is complete when all components work together.

**gameconcept redesigned:** 4 old stages → 9 new stages in 4 blocks:
- Block 1 (1–3): Reference study — analyze reference games by mechanics, art, and feel
- Block 2 (4–6): Our game — mirror of reference study for our own design
- Block 3 (7): Roadmap — collaborative discovery, all deliverables tagged by phase
- Block 4 (8–9): Knowledge research + architecture consolidation

**graybox-5-designed added:** 6-level design-first mechanic loop (user designs in natural language, AI generates all code at once after confirmation). Later upgraded to 9 levels (see 2026-03-26 entry).

**Bevy → Godot:** User tested both engines, chose Godot. All graybox, asset, sound, and skill files rewritten for Godot/GDScript. `graybox-godot/` parallel track deleted.

**Files:** All `workflow/stages/` directories; `AGENTS.md`; all `.agent-utils/skills/`

---

## 2026-03-19: Game branch migration — full audit, web references purged (5 passes)

Migrated the game branch from a shared web+game AGENTS.md structure to a self-contained game-only workflow. Purged all web-workflow content across all files.

**Key changes:**
- Deleted legacy `phase-1/`–`phase-5/` directories; removed all web artifact references
- Rewrote `00-meta-workflow.md` Mode 3 heuristics table for game context
- Rewrote teacher, export-log, git-commit, run-all-tests, run-stage-tests for Godot/game context
- Rewrote `README.md`, `PREREQUISITES.md`, `BRANCH-INFORMATION.md` for game workflow
- Added: latest-tools assumption in AGENTS.md; no-auto-commits rule across all stages

**Files:** All `workflow/stages/`; `AGENTS.md`; all `.agent-utils/skills/`; `README.md`; `PREREQUISITES.md`; `BRANCH-INFORMATION.md`

---

## 2026-03-09 and earlier: Initial design and audits

- **2026-03-06:** Game branch designed from scratch — 25 files across 6 phases (`workflow/game/stages/`)
- **2026-03-09:** Web workflow generalized (SPA/SSR/hybrid/MPA, flexible auth); AGENTS.md split into WEB-AGENT.md + GAME-AGENT.md (later consolidated back); ~25 bugs fixed across web and game branches over 10+ audit passes
