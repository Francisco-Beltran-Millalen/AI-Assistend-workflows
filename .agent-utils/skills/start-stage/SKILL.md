# Start Stage Skill

Start the specified workflow stage.

## Arguments

- Stage identifier:
  - `0` for meta-workflow
  - `teacher` for teacher
  - `<phase-name>-<stage-number>` for regular stages (e.g., `graybox-1`, `gameconcept-2`)

## Instructions

1. Parse the stage identifier and build the file path using base `workflow/stages/`:
   - If `0`: Read `workflow/stages/phase-0/00-meta-workflow.md`
   - If `teacher`: Read `workflow/stages/phase-0/04-teacher.md`
   - If `<phase-name>-<stage-number>`: Read `workflow/stages/<phase-name>/<NN>-*.md`
     where `<NN>` is the stage number zero-padded to 2 digits (1 → `01`, 9 → `09`, 10 → `10`)
   - If `<phase-name>-<stage-number>-<variant>` (e.g., `graybox-4-generative`, `asset-4-2d`): Read `workflow/stages/<phase-name>/<NN>-*-<variant>.md`
     (same zero-padding rule applies)
2. Adopt the persona defined in the stage file
3. For all named phase stages (not 0 or teacher): check if the stage's output artifacts (listed in `## Output Artifacts`) already exist. If any do, read `workflow/shared/00-existing-artifact-protocol.md` and follow it before proceeding to step 4.
4. Follow the stage process

## Stage Mapping

### On-Demand Stages
- 0: meta-workflow (fix workflow issues)
- teacher: teacher (Socratic teaching sessions)

### gameconcept: Game Concept
- gameconcept-1: references-analysis (main loop + mechanics of each reference game)
- gameconcept-2: references-art (visual style of each reference game)
- gameconcept-3: references-feel (how each reference game feels to play)
- gameconcept-4: game-description (our game's main loop + core mechanics)
- gameconcept-5: art-direction (our game's visual identity)
- gameconcept-6: feel-direction (how our game should feel)
- gameconcept-7: roadmap (collaborative ping-pong — all deliverables tagged by phase)
- gameconcept-8: knowledge-research (identify and fill gaps from the roadmap)
- gameconcept-9: architecture-consolidation (frame for all execution phases)
- gameconcept-10: gdd-consolidation (master GDD — markdown + styled HTML)

### graybox: Graybox Prototype (Godot/GDScript)
- graybox-1: mechanic-spec (identify mechanics + feel contracts)
- graybox-2: visual-language (Godot node types, 2D/3D decision, color per entity, camera setup)
- graybox-3: scaffold (Godot project setup, one-time)
- graybox-4: debug-indicators (debug overlay system — one-time setup)
- graybox-5: performance-guidelines (establish Godot performance rules and game-specific decisions — one-time)
- graybox-7: multiplayer-scaffold (ENet peer, GameSession, PlayerInput+MultiplayerSynchronizer, dual-authority pattern — conditional, one-time, multiplayer games only)
- graybox-6: mechanic-loop (12-level design conversation then generative or assisted implementation — repeating per mechanic)

Stage order:
- Single-player: graybox-4 → graybox-5 → graybox-6 (loop)
- Multiplayer: graybox-4 → graybox-5 → graybox-7 → graybox-6 (loop)

### asset: Asset Pipeline
- asset-1: art-direction (style, palette, 2D/3D/mixed decision)
- asset-2: asset-list (enumerate and prioritize all assets)
- asset-3: concept (concept sketch per asset before production)
- asset-4-2d: production-loop-2d (Krita pipeline, sprite sheets, Godot integration)
- asset-4-3d: production-loop-3d (Blender pipeline, GLTF, Godot integration)
- asset-4-mixed: production-loop-mixed (both tracks, cohesion rules, Godot integration)

### sound: Sound Pipeline
- sound-1: sound-direction (sonic identity, tonal rules, references)
- sound-2: sound-event-list (enumerate every SFX event from mechanics + animations + UI)
- sound-3: production-loop (library → record → synthesize fallback, Audacity edit, Godot integration)

### writing: Game Writing (conditional — narrative/dialogue games)
- writing-1: story-foundation (narrative spine, protagonist/antagonist arc, key story events, mechanic–narrative bridges)
- writing-2: world-lore (world systems with costs/limits, factions, history, lore reveal map)
- writing-3: character-voices (per-character dialogue patterns, evasion methods, sample lines, dynamic pairs)
- writing-4: scene-plan (full writing inventory: cutscenes, NPC dialogue trees, quest text, items, environmental)
- writing-5: writing-loop (per scene: brief → draft → voice check → integration check — repeating)

### testing: Unit Testing
- testing-1: test-scaffold (GUT 9.6.0 installation, test directory structure, verify setup — one-time, after graybox-3)
- testing-2: test-loop (per mechanic: identify testable units, write GUT tests, run, update design doc — repeating)

### feel: Feel & Details (on-demand)
- feel-1: graybox-feel (engine effects per interaction — particles, tween, shaders, camera shake)
- feel-2: asset-feel (upgrade placeholder effects with real art per effect)
- feel-3: sound-feel (audio variation and detail per sound event)

### fusion: Fusion (final phase)
- fusion-1: integration-loop (per mechanic — wire up all components, replace placeholders, verify everything plays together)

## Example Usage

```
/start-stage 0
```
Starts Stage 0 (Meta-Workflow) with the Workflow Engineer persona.

```
/start-stage graybox-1
```
Starts the Graybox Mechanic Spec stage with the Game Designer persona.

```
/start-stage graybox-5
```
Starts the Graybox Performance Guidelines stage with the Senior Godot Developer persona.

```
/start-stage graybox-7
```
Starts the Multiplayer Scaffold stage (conditional — only if multiplayer confirmed in gameconcept-9).

```
/start-stage graybox-6
```
Starts the Graybox Mechanic Loop — 12-level design conversation then generative or assisted implementation.
