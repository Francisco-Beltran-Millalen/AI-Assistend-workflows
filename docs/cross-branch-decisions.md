# Cross-Branch Decisions

This document logs decisions that affect all workflow branches, or decisions that apply to a stage that exists across multiple branches (e.g., Phase 0 personas, Phase 1 stages).

When you change a shared concept in one branch, document it here so you know to apply the same change to other branches and remember why it was made.

---

## Format

```markdown
## YYYY-MM-DD: Brief Description

**Scope:** Which branches are affected (`web`, `game`, or `all`)
**Stage(s):** Which stages are affected (e.g., `phase-0/00-meta-workflow`, `phase-1/01-project-definition`, or `all`)
**Change:** What was changed
**Reason:** Why it was changed
**Applied to:** Which branches have already been updated
```

---

## 2026-03-21: New branch — game-bevy (Bevy/Rust variant of game)

**Scope:** `game-bevy` (new branch)
**Stage(s):** all
**Change:** Created `game-bevy` branch from `game`. All engine-specific stage files adapted from Godot/GDScript to Bevy/Rust: graybox-2 (visual language), graybox-3 (scaffold), graybox-4 (all three mechanic loop variants), feel-1/2/3, asset-4-2d/3d/mixed, sound-3, fusion-1. Retained 2D support via Bevy 2D mesh primitives. Stable tool choices: `bevy_hanabi` (particles), `bevy_tweening` (tweens), built-in `bevy_audio` (audio). Engine-agnostic stages (gameconcept 1–9, asset 1–3, sound 1–2, phase-0) kept as-is.
**Reason:** Users who prefer Bevy/Rust over Godot/GDScript needed a dedicated branch. The `game` branch now targets Godot; `game-bevy` targets Bevy.
**Applied to:** `game-bevy`, `main` (README updated with new branch row)

---

## 2026-03-20: Game — Bevy/Rust → Godot/GDScript migration; gameconcept phase expanded; feel + fusion phases added

**Scope:** `game`
**Stage(s):** all
**Change:** Engine migrated from Bevy/Rust to Godot/GDScript throughout all stage files and AGENTS.md. `gameconcept` phase expanded from 4 to 9 stages: references-analysis, references-art, references-feel, game-description, art-direction, feel-direction, roadmap, knowledge-research, architecture-consolidation. Two new complementary on-demand phases added: `feel` (game feel polish on graybox) and `fusion` (art + feel integration).
**Reason:** Switched engine based on project needs. gameconcept expanded to produce richer pre-production artifacts before graybox work begins.
**Applied to:** `game`

---

## 2026-03-20: Web — Stage 4-2b (design-first implementation) added

**Scope:** `web`
**Stage(s):** Phase 4
**Change:** Added `4-2b` (`workflow/stages/phase-4/02b-design-first.md`) as an alternative to `4-2`. Persona: Design-First Developer. It front-loads design decisions before writing implementation code, as opposed to the standard implementation loop.
**Reason:** Some projects benefit from designing the full approach before touching code.
**Applied to:** `web`

---

## 2026-03-19: Game — redesigned to 4 named phases with full stage files

**Scope:** `game`
**Stage(s):** all
**Change:** Game branch restructured from numbered phases (1–4) to 4 domain-named phases: `gameconcept`, `graybox`, `asset`, `sound`. Each phase has a dedicated `workflow/stages/<phase>/` directory with full stage files. On-demand stages reduced to `0` (meta-workflow) and `teacher`.
**Reason:** Named phases are more intuitive for game development than generic phase numbers. The structure better reflects the natural sequence of game production.
**Applied to:** `game`

---

## 2026-03-17: Web — Phase-0 persona fusion

**Scope:** `web`
**Stage(s):** Phase 0 (on-demand stages)
**Change:** Phase-0 stage personas updated to use fused/combined personas rather than single-role personas.
**Reason:** Fused personas allow on-demand stages to handle broader scope without switching contexts.
**Applied to:** `web`

---

## 2026-03-17: Repository restructured to per-branch architecture

**Scope:** all
**Stage(s):** all
**Change:** Each workflow (web, game) moved to its own isolated git branch. Paths simplified from `workflow/<branch>/stages/` to `workflow/stages/`. `WEB-AGENT.md` and `GAME-AGENT.md` merged into `AGENTS.md` per branch. `BRANCH-INFORMATION.md` added to each branch. `start-stage` skill simplified (no branch detection). `main` branch stripped to meta-only (README + this file + shared sources of truth).
**Reason:** Web and game contexts are too different to share a branch. Cloning the full repo for a web project would pollute the agent context with game workflow files and terminology, and vice versa.
**Applied to:** `web`, `game`, `main`

---

## 2026-03-21: Writing branch created

**Scope:** `writing` (new branch)
**Stage(s):** all
**Change:** New `writing` branch created from `web` base. Full 7-phase story development workflow replacing all web-specific stages:
- Phase 1 (8 stages): Format & Medium, Story Seed, Main Character, World Initial/End State, Antagonists, Key Events, Consolidation
- Phase 2 (9 stages): World Rules, Geography, Races & Cultures, Religions, Politics, Supporting Characters, Narrative Style, Anti-Patterns, Consolidation
- Phase 3 (7 stages): Visual Identity, Soundscape, Sensory Palette, Mood Guide, Character Voices, Character Dynamics, Consolidation
- Phase 4 (5 stages): Central Conflict, Major Arcs, Progression Map, Consequence Map, Consolidation
- Phase 5 (4 stages): Format Architecture, Chapter Outline, Scene Descriptions, Story Design Package
- Phase 6 (5 stages, cyclical per chapter): Session Setup, Chapter Expansion, Writing Session, Chapter Close, Design Sync
- Phase 7 (3 stages, on-demand): Chapter Review, Book Review, Series Review
**Reason:** Long-form fiction development requires a fundamentally different process: no code, no tech stack, instead deep story design (sensory palettes, mood recipes, character voices) followed by cooperative writing (user writes, AI clarifies with structured question bursts) and multi-scope review (chapter / book / series).
**Key design decisions:** Multiple stories per project (docs/<story-name>/), Phases 1–5 sequential, Phase 6 cyclical (repeats per chapter), Phase 7 on-demand at any scope. Multimedia references (images, audio) supported in Phase 3 and Phase 6. Supports novels, web novels, manga, screenplays, game narratives, multibook/multi-game series.
**Applied to:** `writing`, `main`
