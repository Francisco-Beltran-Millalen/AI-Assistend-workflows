# Workflow Changelog

---

## 2026-04-02: Broaden PlayerInput pattern → Godot Composition Pattern

**Problem:** The `PlayerInput` child node rule was introduced as the project's pattern for isolating input, but it was intended as one example of Godot's broader composition principle: any self-contained concern becomes a dedicated child node. Three places named `PlayerInput` specifically, causing future agents to treat it as the only component, missing StaminaComponent, HitboxComponent, AudioComponent, etc.

**Cause:** When the pattern was added (see entry below), only input was on the agenda. The generalization was implicit in the intent but never stated.

**Fix:**
- `AGENTS.md` Architectural Assumptions: replaced "Input pattern" bullet with "Godot Composition Pattern" — states the general principle; lists `PlayerInput` and `StaminaComponent` as concrete examples already in the project.
- `AGENTS.md` Optimization Phase Reference table: renamed row from "`PlayerInput` child node" to "Godot Composition Pattern (child nodes for isolatable concerns)" with both examples cited.
- `gameconcept-9` step 2b: renamed "Input isolation" bullet to "Component isolation pattern" — states general principle; `PlayerInput` is named as example 1.
- `gameconcept-9` output template: updated `Input isolation pattern` field to `Component isolation pattern`.
- `graybox-6` Level 3: after the PlayerInput requirement, added a broader component prompt asking the designer to identify other behaviors in the mechanic that could be isolated into a dedicated child node (stamina, hitboxes, audio cues, physics sensors, timers, state machines). Includes the test: "if the script would need to grow a section that could be described in isolation, that section is a candidate."
- `graybox-6` Level 8b: added a componentization check — for each scripted node, ask whether any behavior grew a clear boundary during design and should become a dedicated child node.

**Files:**
- `AGENTS.md`
- `workflow/stages/gameconcept/09-architecture-consolidation.md`
- `workflow/stages/graybox/06-mechanic-loop.md`
- `docs/workflow-changelog.md`

---

## 2026-04-02: Optimization phase ownership, multiplayer support, asset standards, input contract pattern

**Problem / Motivation:**
- Optimization techniques were all grouped in graybox-5 with no guidance on what carries forward vs. what is graybox-only. Asset phase had no performance guidance.
- No multiplayer support in the workflow — games needing networking had no structured path.
- No enforced asset format standards — each developer could use arbitrary formats.
- Character controllers read directly from `Input`, making them impossible to drive from network or AI without refactoring.
- Godot 4.6 (released Jan 26, 2026) introduced Jolt as the default 3D physics engine, requiring workflow updates.

**Fix — Optimization Phase Ownership:**
- Added a "Phase" column to all Universal Rules in graybox-5, marking which rules are "All phases" vs. "Graybox only".
- Replaced the "Physics Threading" decision with a "Jolt Physics" section (Jolt is now the default in 4.6; no decision needed for new projects).
- Added "Next Phase Preview" table to graybox-5 listing which techniques (LOD, occlusion culling, GI, SSR) are handled in later phases.
- Added "Optimization Phase Reference" table to AGENTS.md: every technique → which phase enforces it.

**Fix — Input Contract Pattern (all games):**
- graybox-6 Level 3 (Composition): all controllable entities must declare a `PlayerInput` child node — character controllers never read `Input` directly.
- graybox-6 Level 9 (Godot Mapping): `player_input.gd` stub added to all controllable entity GDScript stubs.
- graybox-6 Level 10 (Performance): network sync row added to the per-mechanic performance constraints template.
- graybox-6 Node Contracts: `PlayerInput` contract required for every controllable entity.
- graybox-6 Design Sign-Off: two new checklist items for PlayerInput presence and contract definition.
- Added to AGENTS.md Architectural Assumptions: `PlayerInput` child node pattern is a project-wide rule.

**Fix — Multiplayer Support (conditional path, graybox-7):**
- gameconcept-9: added "Multiplayer Architecture Decision" section (step 2b) — decides single/multiplayer, model, transport, rollback stance; gates graybox-7.
- New graybox-7 (`07-multiplayer-scaffold.md`): conditional, one-time stage. Sets up `InputPayload` resource, `PlayerInput` with `MultiplayerSynchronizer`, `GameSession` Autoload, `ENetMultiplayerPeer`, `MultiplayerSpawner`, dual-authority pattern, server-authority verification checklist.
- Stage order: single-player: graybox-4→5→6; multiplayer: graybox-4→5→7→6.
- Detection logic, stage table, project status checklist, and Critical Rules updated in AGENTS.md.

**Fix — Asset Format Standards:**
- asset-1: added "Technical Import Standards" section (step 5) covering: GLTF .glb for 3D, PNG for textures, OGG/WAV for audio, LOD/shadow mesh/lightmap UV import settings, GI stance decision, SSR stance.
- asset-1: output template updated with `## Technical Import Standards` section.
- AGENTS.md Architectural Assumptions: preferred formats added as project-wide defaults.

**Godot 4.6 Updates:**
- graybox-5: Jolt replaces physics threading; 4.6 Mesh→CollisionShape3D auto-generation noted.
- graybox-5: LOD Component Pruning improvement noted in Next Phase Preview.
- asset-1: SSR noted as fully rewritten in 4.6 (half/full resolution modes).

**Files:**
- Created: `workflow/stages/graybox/07-multiplayer-scaffold.md`
- Updated: `workflow/stages/graybox/05-performance-guidelines.md` (Jolt, phase annotations, next phase preview)
- Updated: `workflow/stages/graybox/06-mechanic-loop.md` (PlayerInput in L3/L9/L10, Node Contracts, Sign-Off)
- Updated: `workflow/stages/gameconcept/09-architecture-consolidation.md` (multiplayer architecture section + output template + exit criteria)
- Updated: `workflow/stages/asset/01-art-direction.md` (Technical Import Standards section + output template + exit criteria)
- Updated: `AGENTS.md` (stage table, detection logic, architectural assumptions, critical rules, project status, optimization phase reference table)
- Updated: `.agent-utils/skills/start-stage/SKILL.md` (graybox-7 + stage order note + example)

---

## 2026-04-02: Add graybox-5 (Performance Guidelines) + unify mechanic loop into graybox-6

**Problem / Motivation:**
- No performance discipline established before mechanic implementation — techniques like `_process` discipline, object pooling, and `MultiMeshInstance3D` were never discussed until problems appeared.
- Three separate mechanic loop variants (designed/generative/assisted) required choosing a mode before entering the stage, but the 11-level design conversation is always desirable regardless of who writes the code.

**Fix — graybox-5 (Performance Guidelines):**
- New one-time stage between debug-indicators and the mechanic loop.
- Senior Godot Developer persona leads a session to establish universal rules (`_process` discipline, signal-only cross-node communication, no group iteration in hot paths, simple collision shapes, profiling cadence) and game-specific decisions (pooling thresholds, `MultiMeshInstance3D` thresholds, rendering stance, physics threading, large population threshold).
- Output: `docs/performance-guidelines.md` — a contract every mechanic checks against at Level 10 of the design conversation.

**Fix — graybox-6 (Unified Mechanic Loop):**
- Merged `05-mechanic-loop-designed.md`, `05-mechanic-loop-generative.md`, `05-mechanic-loop-assisted.md` into a single `06-mechanic-loop.md`.
- Design conversation is now mandatory for every mechanic (not a mode choice). Extended from 9 to 11 levels:
  - Level 10 (Performance Review): check design against `docs/performance-guidelines.md`, produce concrete per-mechanic constraints.
  - Level 11 (Debug Indicators): design exactly what debug info each node exposes, referencing the `DebugManager` infrastructure from graybox-4.
- Mode selection (generative or assisted) happens after design sign-off, per mechanic.
- Stage identifier simplified to `graybox-6` (no suffix variants).

**Files:**
- Created: `workflow/stages/graybox/05-performance-guidelines.md`
- Created: `workflow/stages/graybox/06-mechanic-loop.md`
- Deleted: `workflow/stages/graybox/05-mechanic-loop-designed.md`
- Deleted: `workflow/stages/graybox/05-mechanic-loop-generative.md`
- Deleted: `workflow/stages/graybox/05-mechanic-loop-assisted.md`
- Updated: `workflow/stages/graybox/04-debug-indicators.md` (Next Stage pointer + graybox-5→6 references)
- Updated: `AGENTS.md` (stage table, detection logic, project status checklist, mechanic-designs folder reference)
- Updated: `.agent-utils/skills/start-stage/SKILL.md` (stage mapping + examples)

---

## 2026-03-26: AGENTS.md — workflow-changelog.md path missing docs/ prefix

**Problem:** AGENTS.md listed the stage-0 output as `workflow-changelog.md` (project root) in two places — the stage table and the project status checklist. The actual file lives at `docs/workflow-changelog.md`.

**Cause:** Oversight — the path was never given a `docs/` prefix in the stage registry.

**Fix:** Updated both references in AGENTS.md to `docs/workflow-changelog.md`.

**Files:** `AGENTS.md`

---

## 2026-03-26: Full workflow audit — broken artifact references and medium design gaps

**Problem:** Full audit revealed 7 stages referencing non-existent artifact names (`docs/game-brief.md`, `docs/game-concept-foundation.md`, `docs/research-findings.md`, `docs/knowledge-audit.md`). These names predated the gameconcept redesign into a 9-stage structure and were never updated in downstream stages. Additionally: asset-1 didn't explain how the 2D/3D/mixed decision gates asset-4 variant selection; AGENTS.md had two "Art Direction" stages with confusingly similar names but different outputs and purposes.

**Cause:** gameconcept phase was redesigned (split into 9 stages, new artifact names) but the update wasn't propagated to graybox-1, asset-1/2/3, sound-1/2, and the teacher stage.

**Fix:**
- Updated `graybox/01-mechanic-spec.md` input: `game-concept-foundation.md` → `game-description.md` + `game-architecture.md`
- Updated `asset/01-art-direction.md` inputs: `game-brief.md` → `game-description.md`, `research-findings.md` → `references-art.md`; added `game-art-direction.md` as explicit input; added asset-4 track selection gating note
- Updated `asset/02-asset-list.md` input: `game-brief.md` → `game-description.md`
- Updated `asset/03-concept.md` input: `game-brief.md` → `game-description.md`
- Updated `sound/01-sound-direction.md` input: `game-brief.md` → `game-description.md`
- Updated `sound/02-sound-event-list.md` input: `game-brief.md` → `game-description.md`
- Updated `phase-0/04-teacher.md` knowledge test mode reading list: `game-brief.md` → `game-description.md`, `knowledge-audit.md` → `knowledge-research.md`, `research-findings.md` → `references-analysis.md`
- Updated `AGENTS.md` stage table to distinguish `docs/game-art-direction.md` (concept-level, gameconcept-5) from `docs/art-direction.md` (production-level, asset-1)

**Files:**
- `workflow/stages/graybox/01-mechanic-spec.md`
- `workflow/stages/asset/01-art-direction.md`
- `workflow/stages/asset/02-asset-list.md`
- `workflow/stages/asset/03-concept.md`
- `workflow/stages/sound/01-sound-direction.md`
- `workflow/stages/sound/02-sound-event-list.md`
- `workflow/stages/phase-0/04-teacher.md`
- `AGENTS.md`

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
