# AGENTS.md — Game Workflow (Prototype)

This is the **Game Workflow** — a structured, AI-collaborative process for building playable game prototypes.

**Branch:** `game` — See `BRANCH-INFORMATION.md` for branch metadata.

**Before doing any work, identify which stage we're in and read the corresponding stage file.**

## Stage Files

### On-Demand Stages

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `workflow-changelog.md` |
| diagram | `workflow/stages/phase-0/01-diagram-assistant.md` | Visual Communicator | `docs/assets/diagrams/*.md` |
| import | `workflow/stages/phase-0/02-import-artifact.md` | Artifact Importer | `imported-artifacts/*-imported.md` |
| knowledge | `workflow/stages/phase-0/03-knowledge-tester.md` | Interview Coach | No artifacts |
| teacher | `workflow/stages/phase-0/04-teacher.md` | Patient Teacher | No artifacts |
| git | `workflow/stages/phase-0/05-git-assistant.md` | Version Control Engineer | No artifacts |

### gameconcept: Game Concept

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| gameconcept-1 | `workflow/stages/gameconcept/01-brief.md` | Creative Director | `docs/game-brief.md` |
| gameconcept-2 | `workflow/stages/gameconcept/02-knowledge-audit.md` | Knowledge Auditor | `docs/knowledge-audit.md` |
| gameconcept-3 | `workflow/stages/gameconcept/03-research.md` | Research Analyst | `docs/research-findings.md` |

### graybox: Graybox Prototype

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| graybox-1 | `workflow/stages/graybox/01-mechanic-spec.md` | Game Designer | `docs/mechanic-spec.md` |
| graybox-2 | `workflow/stages/graybox/02-visual-language.md` | Technical Designer | `docs/graybox-visual-language.md` |
| graybox-3 | `workflow/stages/graybox/03-scaffold.md` | Senior Rust/Bevy Developer | `graybox-prototype/` |
| graybox-4-generative | `workflow/stages/graybox/04-mechanic-loop-generative.md` | Senior Rust/Bevy Developer | Updated prototype + `docs/mechanic-spec.md` |
| graybox-4-assisted | `workflow/stages/graybox/04-mechanic-loop-assisted.md` | Code Mentor | Updated prototype + `docs/mechanic-spec.md` |

### asset: Asset Pipeline

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| asset-1 | `workflow/stages/asset/01-art-direction.md` | Art Director | `docs/art-direction.md` |
| asset-2 | `workflow/stages/asset/02-asset-list.md` | Production Manager | `docs/asset-list.md` |
| asset-3 | `workflow/stages/asset/03-concept.md` | Concept Artist | `docs/assets/concepts/` |
| asset-4-2d | `workflow/stages/asset/04-production-2d.md` | Senior 2D Artist | Sprite sheets + Bevy integration |
| asset-4-3d | `workflow/stages/asset/04-production-3d.md` | Senior 3D Artist | GLTF models + Bevy integration |
| asset-4-mixed | `workflow/stages/asset/04-production-mixed.md` | Senior Artist | Mixed assets + Bevy integration |

### sound: Sound Pipeline

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| sound-1 | `workflow/stages/sound/01-sound-direction.md` | Sound Designer | `docs/sound-direction.md` |
| sound-2 | `workflow/stages/sound/02-sound-event-list.md` | Sound Designer | `docs/sound-event-list.md` |
| sound-3 | `workflow/stages/sound/03-production-loop.md` | Sound Designer | SFX files + Bevy integration |

---

## Architectural Assumptions

- **Engine:** Bevy (Rust)
- **Visuals (graybox):** Bevy primitive meshes — Cuboid, Sphere, Cylinder, Capsule, Plane
- **No persistent database** — game state lives in memory
- **Asset tools:** Krita, Blender, Inkscape, Material Maker *(asset phase — TBD)*
- **Audio tools:** Audacity — SFX only (music deferred)

---

## How to Determine Current Stage

Check `docs/` for existing artifacts:

**gameconcept phase:**
- No artifacts → gameconcept-1
- `docs/game-brief.md` exists, no `knowledge-audit.md` → gameconcept-2
- `docs/knowledge-audit.md` exists, no `research-findings.md` → gameconcept-3
- `docs/research-findings.md` exists → gameconcept phase complete → graybox-1

**graybox phase:**
- `docs/mechanic-spec.md` does not exist → graybox-1
- `docs/mechanic-spec.md` exists, `docs/graybox-visual-language.md` does not → graybox-2
- `docs/graybox-visual-language.md` exists, `graybox-prototype/` does not → graybox-3
- `graybox-prototype/` exists, mechanics not all done → graybox-4-generative or graybox-4-assisted (user's choice per mechanic)
- All mechanics in `mechanic-spec.md` marked `[x] Done` → graybox phase complete

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
- **Stage diagram** (`/start-stage diagram`) — Generate diagrams from artifacts
- **Stage import** (`/start-stage import`) — Import external artifacts
- **Stage knowledge** (`/start-stage knowledge`) — Quiz yourself on all decisions
- **Stage teacher** (`/start-stage teacher`) — Socratic teaching sessions
- **Stage git** (`/start-stage git`) — Git and version control operations

---

## Critical Rules

1. **ALWAYS read the stage file** before starting work
2. **ALWAYS adopt the persona** defined in the stage file
3. **ALWAYS use `/start-stage`** to start stages — it runs the Existing Artifact Protocol when artifacts already exist
4. **In graybox-4: ALWAYS read `docs/mechanic-spec.md` first** — it tracks progress across sessions
5. **Follow stage order** within each phase
6. **Complete each phase before starting the next**

---

## Quick Commands

### Slash Commands (Skills)

- `/start-stage <stage-identifier>` → Start a stage (e.g., `/start-stage graybox-1`)
- `/start-stage 0` → Meta-Workflow (fix workflow issues)
- `/start-stage diagram` → Diagram Assistant
- `/start-stage import` → Import an external artifact
- `/start-stage knowledge` → Knowledge Tester
- `/start-stage teacher` → Teacher
- `/start-stage git` → Git Assistant
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
├── graybox-prototype/           ← Bevy graybox prototype code
├── docs/
│   ├── logs/                    ← Conversation logs
│   ├── assets/                  ← Diagrams, design specs
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── stages/
    │   ├── phase-0/             ← On-demand stages
    │   ├── gameconcept/         ← Game Concept stages
    │   ├── graybox/             ← Graybox Prototype stages
    │   ├── asset/               ← Asset Pipeline stages
    │   └── sound/               ← Sound Pipeline stages
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

## Project Status

> Current phase and stage are determined by checking `docs/` for existing artifacts.

### Meta Artifacts
- [ ] `workflow-changelog.md`

### gameconcept phase
- [ ] `docs/game-brief.md` ← gameconcept-1 complete
- [ ] `docs/knowledge-audit.md` ← gameconcept-2 complete
- [ ] `docs/research-findings.md` ← gameconcept-3 complete

### graybox phase
- [ ] `docs/mechanic-spec.md` ← graybox-1 complete
- [ ] `docs/graybox-visual-language.md` ← graybox-2 complete
- [ ] `graybox-prototype/` created ← graybox-3 complete
- [ ] All mechanics `[x] Done` in `mechanic-spec.md` ← graybox-4 complete

### asset phase
- [ ] `docs/art-direction.md` ← asset-1 complete
- [ ] `docs/asset-list.md` ← asset-2 complete
- [ ] `docs/assets/concepts/` populated ← asset-3 complete
- [ ] All assets `[x] Done` in `asset-list.md` ← asset-4 complete

### sound phase
- [ ] `docs/sound-direction.md` ← sound-1 complete
- [ ] `docs/sound-event-list.md` ← sound-2 complete
- [ ] All events `[x] Done` in `sound-event-list.md` ← sound-3 complete
