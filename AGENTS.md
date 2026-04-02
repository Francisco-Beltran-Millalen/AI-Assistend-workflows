# AGENTS.md — Game Workflow (Prototype)

This is the **Game Workflow** — a structured, AI-collaborative process for building playable game prototypes.

**Branch:** `game` — See `BRANCH-INFORMATION.md` for branch metadata.

**Before doing any work, identify which stage we're in and read the corresponding stage file.**

## Stage Files

### On-Demand Stages

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `docs/workflow-changelog.md` |
| teacher | `workflow/stages/phase-0/04-teacher.md` | Patient Teacher | No artifacts |

### gameconcept: Game Concept

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| gameconcept-1 | `workflow/stages/gameconcept/01-references-analysis.md` | Game Analyst | `docs/references-analysis.md` |
| gameconcept-2 | `workflow/stages/gameconcept/02-references-art.md` | Art Analyst | `docs/references-art.md` |
| gameconcept-3 | `workflow/stages/gameconcept/03-references-feel.md` | Game Feel Analyst | `docs/references-feel.md` |
| gameconcept-4 | `workflow/stages/gameconcept/04-game-description.md` | Creative Director | `docs/game-description.md` |
| gameconcept-5 | `workflow/stages/gameconcept/05-art-direction.md` | Creative Director / Art Director | `docs/game-art-direction.md` *(concept-level visual identity)* |
| gameconcept-6 | `workflow/stages/gameconcept/06-feel-direction.md` | Creative Director / Game Feel Designer | `docs/game-feel-direction.md` |
| gameconcept-7 | `workflow/stages/gameconcept/07-roadmap.md` | Production Designer | `docs/roadmap.md` |
| gameconcept-8 | `workflow/stages/gameconcept/08-knowledge-research.md` | Research Analyst | `docs/knowledge-research.md` |
| gameconcept-9 | `workflow/stages/gameconcept/09-architecture-consolidation.md` | Systems Architect | `docs/game-architecture.md` |

### graybox: Graybox Prototype (Godot/GDScript)

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| graybox-1 | `workflow/stages/graybox/01-mechanic-spec.md` | Game Designer | `docs/mechanic-spec.md` |
| graybox-2 | `workflow/stages/graybox/02-visual-language.md` | Technical Designer | `docs/graybox-visual-language.md` |
| graybox-3 | `workflow/stages/graybox/03-scaffold.md` | Senior Godot Developer | `graybox-prototype/` |
| graybox-4 | `workflow/stages/graybox/04-debug-indicators.md` | Senior Godot Developer | Debug overlay system in `graybox-prototype/` |
| graybox-5 | `workflow/stages/graybox/05-performance-guidelines.md` | Senior Godot Developer | `docs/performance-guidelines.md` |
| graybox-7 *(conditional)* | `workflow/stages/graybox/07-multiplayer-scaffold.md` | Senior Godot Developer | `graybox-prototype/multiplayer/` + `docs/multiplayer-architecture.md` |
| graybox-6 | `workflow/stages/graybox/06-mechanic-loop.md` | Systems Designer / Senior Godot Developer / Code Mentor | Updated prototype + `docs/mechanic-spec.md` + `docs/mechanic-designs/` |

### asset: Asset Pipeline

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| asset-1 | `workflow/stages/asset/01-art-direction.md` | Art Director | `docs/art-direction.md` *(production-level style guide + 2D/3D/mixed decision)* |
| asset-2 | `workflow/stages/asset/02-asset-list.md` | Production Manager | `docs/asset-list.md` |
| asset-3 | `workflow/stages/asset/03-concept.md` | Concept Artist | `docs/assets/concepts/` |
| asset-4-2d | `workflow/stages/asset/04-production-2d.md` | Senior 2D Artist | Sprite sheets + Godot integration |
| asset-4-3d | `workflow/stages/asset/04-production-3d.md` | Senior 3D Artist | GLTF models + Godot integration |
| asset-4-mixed | `workflow/stages/asset/04-production-mixed.md` | Senior Artist | Mixed assets + Godot integration |

### sound: Sound Pipeline

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| sound-1 | `workflow/stages/sound/01-sound-direction.md` | Sound Designer | `docs/sound-direction.md` |
| sound-2 | `workflow/stages/sound/02-sound-event-list.md` | Sound Designer | `docs/sound-event-list.md` |
| sound-3 | `workflow/stages/sound/03-production-loop.md` | Sound Designer | SFX files + Godot integration |

### feel: Feel & Details (on-demand, complementary)

**On-demand phase** — invoke at any point during or after implementation phases. Each stage is independent.

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| feel-1 | `workflow/stages/feel/01-graybox-feel.md` | Game Feel Artist | Updated `graybox-prototype/` |
| feel-2 | `workflow/stages/feel/02-asset-feel.md` | Technical Artist | Updated `graybox-prototype/` |
| feel-3 | `workflow/stages/feel/03-sound-feel.md` | Sound Designer | Updated `graybox-prototype/` |

### fusion: Fusion (final phase)

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| fusion-1 | `workflow/stages/fusion/01-integration-loop.md` | Integration Engineer | Production-ready mechanics + updated `docs/mechanic-spec.md` |

---

## Architectural Assumptions

- **Tool versions:** Always use the latest stable version of all tools, libraries, and engines unless the project explicitly specifies otherwise.
- **Engine:** Godot 4.6+ (GDScript)
- **Visuals (graybox):** Godot primitive meshes — BoxMesh, SphereMesh, CylinderMesh, CapsuleMesh, PlaneMesh
- **No persistent database** — game state lives in memory
- **Asset tools:** Krita, Blender, Inkscape, Material Maker *(asset phase — TBD)*
- **Audio tools:** Audacity — SFX only (music deferred)
- **3D models:** GLTF 2.0 `.glb` (binary) — established in asset-1; apply transforms before export
- **2D textures:** PNG — world: VRAM compressed + mipmaps ON; UI: lossless + mipmaps OFF
- **Audio:** OGG Vorbis for music/long ambient; WAV for short SFX (< 3s)
- **Import standards (3D):** LOD generation ON, shadow meshes ON, lightmap UV ON — set in asset-1
- **Physics engine:** Jolt (default since Godot 4.6) — verify in Project Settings if migrating from older version
- **Godot Composition Pattern (all phases):** Any self-contained concern becomes a dedicated child node, Resource, or Autoload — not inlined into the parent script. The question to ask at every composition design: "Does this behavior have a clear boundary and could it be swapped, reused, or driven externally?" If yes, make it a child node. Examples already in the project: `PlayerInput` (isolates input source from controller), `StaminaComponent` (isolates stamina logic from controller). The pattern applies to: hitboxes, audio cues, physics sensors, state machines, timers — anything with a clear interface.

---

## How to Determine Current Stage

Check `docs/` for existing artifacts:

**gameconcept phase:**
- No artifacts → gameconcept-1
- `docs/references-analysis.md` exists → gameconcept-2
- `docs/references-art.md` exists → gameconcept-3
- `docs/references-feel.md` exists → gameconcept-4
- `docs/game-description.md` exists → gameconcept-5
- `docs/game-art-direction.md` exists → gameconcept-6
- `docs/game-feel-direction.md` exists → gameconcept-7
- `docs/roadmap.md` exists → gameconcept-8
- `docs/knowledge-research.md` exists → gameconcept-9
- `docs/game-architecture.md` exists → gameconcept phase complete → graybox-1

**graybox phase (Godot):**
- `docs/mechanic-spec.md` does not exist → graybox-1
- `docs/mechanic-spec.md` exists, `docs/graybox-visual-language.md` does not → graybox-2
- `docs/graybox-visual-language.md` exists, `graybox-prototype/` does not → graybox-3
- `graybox-prototype/` exists, `graybox-prototype/scripts/debug_manager.gd` does not → graybox-4
- `graybox-prototype/scripts/debug_manager.gd` exists, `docs/performance-guidelines.md` does not → graybox-5
- `docs/performance-guidelines.md` exists, `game-architecture.md` has multiplayer confirmed, `docs/multiplayer-architecture.md` does not exist → graybox-7
- `docs/performance-guidelines.md` exists, (single-player OR `docs/multiplayer-architecture.md` exists), mechanics not all done → graybox-6 (repeating per mechanic)
- All mechanics in `mechanic-spec.md` marked `[x] Done` → graybox phase complete

> **Stage order:**
> - Single-player: graybox-4 → graybox-5 → graybox-6 (loop)
> - Multiplayer: graybox-4 → graybox-5 → graybox-7 → graybox-6 (loop)

**asset phase:**
- `docs/art-direction.md` does not exist → asset-1
- `docs/art-direction.md` exists, no `asset-list.md` → asset-2
- `docs/asset-list.md` exists, concepts not done → asset-3
- Concepts done, assets not all complete → asset-4-2d / asset-4-3d / asset-4-mixed (per art-direction.md track decision)
- All assets `[x] Done` → asset phase complete

**sound phase:**
- `docs/sound-direction.md` does not exist → sound-1
- `docs/sound-direction.md` exists, no `sound-event-list.md` → sound-2
- `docs/sound-event-list.md` exists, events not all done → sound-3
- All events `[x] Done` → sound phase complete

**feel phase (on-demand):**
- Invoke `feel-1` anytime after a mechanic is implemented — add engine feel effects
- Invoke `feel-2` anytime after real art is ready for an effect — upgrade placeholder visuals
- Invoke `feel-3` anytime after sound files exist for an event — add audio variation/detail
- No sequential dependency — each stage is independently invocable

**fusion phase:**
- Invoke `fusion-1` when a mechanic has code + assets + sounds in place
- Loop per mechanic until all target mechanics are marked `[x] Integrated`

---

## Conversation Logging

Each stage session should produce one final log file.

### Logging Strategy

- **During session**: Auto-export runs every 5 minutes for crash protection
- **On stage completion**: Export the final log using `/export-log <stage-identifier>`
- **Off-stage conversations**: No logs kept

### Exporting Logs

At the end of each stage session:

```bash
/export-log graybox-1
```

This creates: `docs/logs/stage-graybox-1-mechanic-spec-20260319-143022.txt`

---

## On-Demand Stages

**On-demand stages** are not part of the phase cycle. Invoke them anytime:
- **Stage 0** (`/start-stage 0`) — Fix workflow issues
- **Stage teacher** (`/start-stage teacher`) — Socratic teaching sessions
- **feel-1 / feel-2 / feel-3** — Add feel effects to any mechanic, anytime during implementation

---

## Critical Rules

1. **ALWAYS read the stage file** before starting work
2. **ALWAYS adopt the persona** defined in the stage file
3. **ALWAYS use `/start-stage`** to start stages — it runs the Existing Artifact Protocol when artifacts already exist
4. **In graybox-6: ALWAYS read `docs/mechanic-spec.md`, `docs/performance-guidelines.md`, AND (if multiplayer) `docs/multiplayer-architecture.md` first** — they track progress and constraints across sessions
5. **Follow stage order** within each phase (gameconcept is strictly sequential; graybox/asset/sound are loosely ordered)
6. **feel is on-demand** — invoke anytime, in any order, per mechanic or per interaction
7. **fusion is final** — invoke when a mechanic is ready for integration

---

## Quick Commands

### Slash Commands (Skills)

- `/start-stage <stage-identifier>` → Start a stage (e.g., `/start-stage graybox-1`)
- `/start-stage 0` → Meta-Workflow (fix workflow issues)
- `/start-stage teacher` → Teacher
- `/export-log <stage-identifier>` → Export conversation to `docs/logs/`

### Natural Language

- "Start graybox-1" → Mechanic Spec
- "What stage are we in?" → Check `docs/` for artifacts
- "Export the log" → Save conversation

---

## Project Structure

```
project-root/
├── BRANCH-INFORMATION.md        ← Branch metadata
├── AGENTS.md                    ← Canonical workflow instructions
├── CLAUDE.md                    ← Claude Code redirect to AGENTS.md
├── GEMINI.md                    ← Gemini redirect to AGENTS.md
├── .claude/
│   ├── settings.json            ← Hooks configuration
│   └── skills/                  ← Custom slash commands (thin wrappers)
├── .agent-utils/
│   └── skills/                  ← Canonical, tool-agnostic skill content
├── imported-artifacts/          ← Raw imports + adapted files
├── graybox-prototype/           ← Godot graybox prototype code
├── docs/
│   ├── logs/                    ← Conversation logs
│   ├── assets/                  ← Diagrams, design specs
│   ├── adrs/                    ← Architecture Decision Records
│   ├── mechanic-designs/        ← Per-mechanic design journals (graybox-6)
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── stages/
    │   ├── phase-0/             ← On-demand stages
    │   ├── gameconcept/         ← Game Concept stages
    │   ├── graybox/             ← Graybox Prototype stages (Godot)
    │   ├── asset/               ← Asset Pipeline stages
    │   ├── sound/               ← Sound Pipeline stages
    │   ├── feel/                ← Feel & Details stages (on-demand)
    │   └── fusion/              ← Fusion / Integration stages (final)
    ├── shared/                  ← Shared protocols
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts
```

---

## Artifact Storage

- Working design artifacts: `docs/`
- Graybox prototype code: `graybox-prototype/`
- Architecture decisions: `docs/adrs/`
- Conversation logs: `docs/logs/`
- Workflow changelog: `docs/workflow-changelog.md`

---

## Optimization Phase Reference

Which technique is enforced in which phase. Rules marked **All phases** are never relaxed.

| Technique | Phase | Notes |
|-----------|-------|-------|
| `_process`/`_physics_process` disabled by default | graybox-5 → **all phases** | Universal rule, never relaxed |
| Signal-only cross-node communication | graybox-5 → **all phases** | Universal rule |
| No group iteration in hot paths | graybox-5 → **all phases** | Universal rule |
| Godot Composition Pattern (child nodes for isolatable concerns) | graybox-6 → **all phases** | Universal rule; `PlayerInput` and `StaminaComponent` are examples; enables network/AI input swapping and reuse |
| Simple collision shapes (gameplay nodes) | graybox-5 | Graybox only — static env may use mesh collision in asset phase |
| Object pooling thresholds | graybox-5 | Counts may be revised in asset phase once real asset costs are known |
| MultiMeshInstance3D thresholds | graybox-5 | Same — threshold may be revised in asset phase |
| Jolt physics (default, Godot 4.6) | graybox-5 (verify) | No action for new 4.6 projects; verify if migrating |
| Unshaded rendering / no GI | graybox only | Replaced at asset-1 with GI decision |
| Asset import format standards | **asset-1** | GLTF .glb, PNG, OGG/WAV — defined in `docs/art-direction.md` |
| LOD auto-generation (import setting) | **asset-1** | ON for all 3D meshes; Godot 4.6 LOD pruning improved for multi-part meshes |
| Occlusion culling plan | **asset-1** | Bake after level geometry finalized |
| GI stance (LightmapGI / VoxelGI / SDFGI) | **asset-1** | Decided before any lighting is baked |
| Texture compression per use case | **asset-1** | VRAM for world; lossless for UI |
| SSR configuration | **feel phase** | After real geometry exists; Godot 4.6 SSR fully rewritten — half vs full resolution |
| Particle budgets | **feel phase** | Max particles per effect type |
| Full profiler pass | **fusion phase** | Before any mechanic marked ship-ready |
| Network bandwidth profiling | **fusion phase** | Bytes/sec per player under full load (multiplayer only) |

---

## Project Status

> Current phase and stage are determined by checking `docs/` for existing artifacts.

### Meta Artifacts
- [ ] `docs/workflow-changelog.md`

### gameconcept phase
- [ ] `docs/references-analysis.md` ← gameconcept-1 complete
- [ ] `docs/references-art.md` ← gameconcept-2 complete
- [ ] `docs/references-feel.md` ← gameconcept-3 complete
- [ ] `docs/game-description.md` ← gameconcept-4 complete
- [ ] `docs/game-art-direction.md` ← gameconcept-5 complete
- [ ] `docs/game-feel-direction.md` ← gameconcept-6 complete
- [ ] `docs/roadmap.md` ← gameconcept-7 complete
- [ ] `docs/knowledge-research.md` ← gameconcept-8 complete
- [ ] `docs/game-architecture.md` ← gameconcept-9 complete

### graybox phase (Godot)
- [ ] `docs/mechanic-spec.md` ← graybox-1 complete
- [ ] `docs/graybox-visual-language.md` ← graybox-2 complete
- [ ] `graybox-prototype/` created ← graybox-3 complete
- [ ] Debug overlay system set up ← graybox-4 complete
- [ ] `docs/performance-guidelines.md` ← graybox-5 complete
- [ ] `docs/multiplayer-architecture.md` ← graybox-7 complete *(multiplayer games only)*
- [ ] All mechanics `[x] Done` in `mechanic-spec.md` ← graybox-6 complete

### asset phase
- [ ] `docs/art-direction.md` ← asset-1 complete
- [ ] `docs/asset-list.md` ← asset-2 complete
- [ ] `docs/assets/concepts/` populated ← asset-3 complete
- [ ] All assets `[x] Done` in `asset-list.md` ← asset-4 complete

### sound phase
- [ ] `docs/sound-direction.md` ← sound-1 complete
- [ ] `docs/sound-event-list.md` ← sound-2 complete
- [ ] All events `[x] Done` in `sound-event-list.md` ← sound-3 complete

### feel phase (on-demand — no completion gate)
- feel-1: engine feel effects per mechanic (invoke per mechanic, multiple times)
- feel-2: asset feel upgrades per effect (invoke when art is ready)
- feel-3: sound feel detail per event (invoke when audio is ready)

### fusion phase
- [ ] All target mechanics `[x] Integrated` in `docs/mechanic-spec.md` ← fusion complete
