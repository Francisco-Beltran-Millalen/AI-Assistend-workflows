# AGENTS.md — Writing Workflow

This is the **Writing Workflow** — a structured, AI-collaborative process for developing stories from raw idea to written chapters.

**Branch:** `writing` — See `BRANCH-INFORMATION.md` for branch metadata.

**Before doing any work, identify which story and stage we're in, and read the corresponding stage file.**

---

## Stage Files

### On-Demand Stages

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `workflow-changelog.md`, `imported-artifacts/*-imported.md` |

### Phase 1: Concept & Foundation

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 1-1 | `workflow/stages/phase-1/01-format-medium.md` | Format Analyst | `docs/<story>/format-medium.md` |
| 1-2 | `workflow/stages/phase-1/02-story-seed.md` | Story Conceiver | `docs/<story>/story-seed.md` |
| 1-3 | `workflow/stages/phase-1/03-main-character.md` | Character Creator | `docs/<story>/main-character.md` |
| 1-4 | `workflow/stages/phase-1/04-world-initial-state.md` | World Setter | `docs/<story>/world-initial-state.md` |
| 1-5 | `workflow/stages/phase-1/05-world-end-state.md` | Vision Definer | `docs/<story>/world-end-state.md` |
| 1-6 | `workflow/stages/phase-1/06-antagonists.md` | Antagonist Designer | `docs/<story>/antagonists.md` |
| 1-7 | `workflow/stages/phase-1/07-key-events.md` | Story Mapper | `docs/<story>/key-events.md` |
| 1-8 | `workflow/stages/phase-1/08-consolidation.md` | Story Editor | **`docs/<story>/phase-1-consolidation.md`** |

### Phase 2: World & Rules

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 2-1 | `workflow/stages/phase-2/01-world-rules.md` | System Designer | `docs/<story>/world-rules.md` |
| 2-2 | `workflow/stages/phase-2/02-geography.md` | Cartographer | `docs/<story>/geography.md` |
| 2-3 | `workflow/stages/phase-2/03-races-cultures.md` | Cultural Anthropologist | `docs/<story>/races-cultures.md` |
| 2-4 | `workflow/stages/phase-2/04-religions-mythology.md` | Lore Keeper | `docs/<story>/religions-mythology.md` |
| 2-5 | `workflow/stages/phase-2/05-politics-power.md` | Political Architect | `docs/<story>/politics-power.md` |
| 2-6 | `workflow/stages/phase-2/06-supporting-characters.md` | Character Weaver | `docs/<story>/supporting-characters.md` |
| 2-7 | `workflow/stages/phase-2/07-narrative-style.md` | Literary Stylist | `docs/<story>/narrative-style.md` |
| 2-8 | `workflow/stages/phase-2/08-anti-patterns.md` | Critical Reviewer | `docs/<story>/anti-patterns.md` |
| 2-9 | `workflow/stages/phase-2/09-consolidation.md` | World Editor | **`docs/<story>/phase-2-consolidation.md`** |

### Phase 3: Sensory & Identity

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 3-1 | `workflow/stages/phase-3/01-visual-identity.md` | Visual Artist | `docs/<story>/visual-identity.md`, `docs/<story>/assets/images/` |
| 3-2 | `workflow/stages/phase-3/02-soundscape.md` | Sound Designer | `docs/<story>/soundscape.md`, `docs/<story>/assets/audio/` |
| 3-3 | `workflow/stages/phase-3/03-sensory-palette.md` | Sensory Writer | `docs/<story>/sensory-palette.md` |
| 3-4 | `workflow/stages/phase-3/04-mood-guide.md` | Mood Architect | `docs/<story>/mood-guide.md` |
| 3-5 | `workflow/stages/phase-3/05-character-voices.md` | Dialogue Specialist | `docs/<story>/character-voices.md` |
| 3-6 | `workflow/stages/phase-3/06-character-dynamics.md` | Relationship Mapper | `docs/<story>/character-dynamics.md` |
| 3-7 | `workflow/stages/phase-3/07-consolidation.md` | Sensory Editor | **`docs/<story>/phase-3-consolidation.md`** |

### Phase 4: Narrative Arcs

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 4-1 | `workflow/stages/phase-4/01-central-conflict.md` | Thematic Architect | `docs/<story>/central-conflict.md` |
| 4-2 | `workflow/stages/phase-4/02-major-arcs.md` | Plot Architect | `docs/<story>/major-arcs.md` |
| 4-3 | `workflow/stages/phase-4/03-progression-map.md` | Progression Designer | `docs/<story>/progression-map.md` |
| 4-4 | `workflow/stages/phase-4/04-consequence-map.md` | Consequence Mapper | `docs/<story>/consequence-map.md` |
| 4-5 | `workflow/stages/phase-4/05-consolidation.md` | Arc Editor | **`docs/<story>/phase-4-consolidation.md`** |

### Phase 5: Chapter Planning

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 5-1 | `workflow/stages/phase-5/01-format-architecture.md` | Serial Architect | `docs/<story>/chapter-format.md` |
| 5-2 | `workflow/stages/phase-5/02-chapter-outline.md` | Chapter Planner | `docs/<story>/chapter-outline.md` |
| 5-3 | `workflow/stages/phase-5/03-scene-descriptions.md` | Scene Designer | `docs/<story>/scene-descriptions.md` |
| 5-4 | `workflow/stages/phase-5/04-story-design-package.md` | Story Compiler | **`docs/<story>/story-design-package/`** |

### Phase 6: Writing *(cyclical — one pass per chapter)*

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 6-1 | `workflow/stages/phase-6/01-session-setup.md` | Writing Companion | Session context loaded |
| 6-2 | `workflow/stages/phase-6/02-chapter-expansion.md` | Story Analyst | Chapter blueprint |
| 6-3 | `workflow/stages/phase-6/03-writing-session.md` | Writing Companion | `docs/<story>/chapters/chapter-<N>.md` |
| 6-4 | `workflow/stages/phase-6/04-chapter-close.md` | Continuity Editor | Chapter close notes, `chapter-outline.md` updated |
| 6-5 | `workflow/stages/phase-6/05-design-sync.md` | Story Editor | Updated design docs *(conditional)* |

**Phase 6 repeats for every chapter.** Each chapter goes through the full 6-1 → 6-4 cycle (and 6-5 if design issues were flagged in 6-4). After closing a chapter, return to 6-1 for the next.

### Phase 7: Review *(on-demand — invoke at any time)*

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 7-1 | `workflow/stages/phase-7/01-chapter-review.md` | Chapter Editor | Revised `chapter-<N>.md` + review notes |
| 7-2 | `workflow/stages/phase-7/02-book-review.md` | Story Architect | `docs/<story>/book-review.md` |
| 7-3 | `workflow/stages/phase-7/03-series-review.md` | Series Architect | `docs/<story>/series-review.md` |

**Phase 7 scopes:**
- **7-1 Chapter Review** — invoke anytime on any chapter: "How do I make this chapter better?"
- **7-2 Book Review** — invoke when all chapters of a book/volume are drafted: pacing, flow, structure
- **7-3 Series Review** — invoke when multiple books/volumes or installments are complete: cross-book consistency, series arcs

---

## Story Identification

This workflow supports **multiple stories in one project**. Each story's artifacts live under `docs/<story-name>/`.

**Before starting any stage:**
1. Check what stories exist — look for directories in `docs/` (ignore `logs/`)
2. If multiple stories exist, ask the user which story they're working on
3. If no story exists yet, Stage 1-1 will establish the story name
4. Use the story name consistently as the directory name (lowercase, hyphenated, e.g. `iron-throne-chronicles`)

---

## Phase Handoffs

### Phase 1 → Phase 2

Stage 1-8 produces `docs/<story>/phase-1-consolidation.md` — the **primary input** for Phase 2. It contains the complete story foundation: format/medium, emotional core, protagonist, world states, antagonists, and key events.

### Phase 2 → Phase 3

Stage 2-9 produces `docs/<story>/phase-2-consolidation.md` — the primary input for Phase 3. It contains the complete world: rules, geography, cultures, politics, supporting characters, and narrative voice.

### Phase 3 → Phase 4

Stage 3-7 produces `docs/<story>/phase-3-consolidation.md` — the primary input for Phase 4. It contains the complete sensory and identity layer: visual identity, soundscape, sensory palette, mood guide, character voices, and character dynamics.

### Phase 4 → Phase 5

Stage 4-5 produces `docs/<story>/phase-4-consolidation.md` — the primary input for Phase 5. It contains the complete narrative architecture: central conflict, major arcs, progression milestones, and world consequences.

### Phase 5 → Phase 6

Stage 5-4 compiles all outputs into `docs/<story>/story-design-package/` — the **reference package** for the writing phase. Phase 6 reads from this package at the start of every writing session.

### Phase 6 → Phase 6 (cyclical)

After completing a chapter (6-4 close, 6-5 sync if needed), return to 6-1 for the next chapter. The chapter outline tracks which chapters are drafted.

---

## How to Determine Current Stage

### Step 1: Identify the story

Check `docs/` for story directories. If multiple exist, ask the user.

### Step 2: Check artifacts within `docs/<story>/`

**Phase 1 (Concept & Foundation):**
- No story directory → Stage 1-1
- `format-medium.md` exists → Stage 1-2
- `story-seed.md` exists → Stage 1-3
- `main-character.md` exists → Stage 1-4
- `world-initial-state.md` exists → Stage 1-5
- `world-end-state.md` exists → Stage 1-6
- `antagonists.md` exists → Stage 1-7
- `key-events.md` exists → Stage 1-8
- `phase-1-consolidation.md` exists → Phase 1 complete

**Phase 2 (World & Rules):**
- `phase-1-consolidation.md` exists, no `world-rules.md` → Stage 2-1
- `world-rules.md` → Stage 2-2
- `geography.md` → Stage 2-3
- `races-cultures.md` → Stage 2-4
- `religions-mythology.md` → Stage 2-5
- `politics-power.md` → Stage 2-6
- `supporting-characters.md` → Stage 2-7
- `narrative-style.md` → Stage 2-8
- `anti-patterns.md` → Stage 2-9
- `phase-2-consolidation.md` → Phase 2 complete

**Phase 3 (Sensory & Identity):**
- `phase-2-consolidation.md` exists, no `visual-identity.md` → Stage 3-1
- `visual-identity.md` → Stage 3-2
- `soundscape.md` → Stage 3-3
- `sensory-palette.md` → Stage 3-4
- `mood-guide.md` → Stage 3-5
- `character-voices.md` → Stage 3-6
- `character-dynamics.md` → Stage 3-7
- `phase-3-consolidation.md` → Phase 3 complete

**Phase 4 (Narrative Arcs):**
- `phase-3-consolidation.md` exists, no `central-conflict.md` → Stage 4-1
- `central-conflict.md` → Stage 4-2
- `major-arcs.md` → Stage 4-3
- `progression-map.md` → Stage 4-4
- `consequence-map.md` → Stage 4-5
- `phase-4-consolidation.md` → Phase 4 complete

**Phase 5 (Chapter Planning):**
- `phase-4-consolidation.md` exists, no `chapter-format.md` → Stage 5-1
- `chapter-format.md` → Stage 5-2
- `chapter-outline.md` → Stage 5-3
- `scene-descriptions.md` → Stage 5-4
- `story-design-package/` exists → Phase 5 complete

**Phase 6 (Writing):**
- `story-design-package/` exists → Writing phase active. Read `chapter-outline.md` to find the next undrafted chapter → Stage 6-1.

**Phase 7 (Review):**
- On-demand. Ask the user what scope they want to review (chapter / book / series) → stage 7-1, 7-2, or 7-3.

---

## Conversation Logging

Each stage session should produce one final log file.

### Logging Strategy

- **During session**: Auto-export runs every 5 minutes for crash protection
- **On stage completion**: Export the final log using `/export-log <phase>-<stage>`

### Exporting Logs

```bash
/export-log 2-3
```

Creates: `docs/logs/stage-2-3-races-cultures-20260321-143022.txt`

For Phase 6, include chapter number in the log name:
- `stage-6-3-writing-session-ch03-20260321-143022.txt`

---

## On-Demand Stages

- **Stage 0** (`/start-stage 0`) — Workflow maintenance, git operations, artifact import
- **Stage 7-1/7-2/7-3** — Review at chapter, book, or series scope (anytime)

---

## Critical Rules

1. **ALWAYS read the stage file** before starting work
2. **ALWAYS adopt the persona** defined in the stage file
3. **ALWAYS use `/start-stage`** to start stages — it automatically runs the Existing Artifact Protocol
4. **ALWAYS identify the story first** — check `docs/` for story directories before any stage work
5. **In Phase 6: ALWAYS read the story design package** at the start of each session
6. **In Phase 6: ALWAYS read the chapter outline** to confirm which chapter is next
7. **Follow stage order** within phases 1–5
8. **Complete each design phase before starting the next** (phases 1–5 are sequential)
9. **Phase 6 is cyclical** — repeat for every chapter; return to 6-1 after closing each chapter
10. **Phase 7 is on-demand** — invoke at any scope, at any time

---

## Quick Commands

### Slash Commands

- `/start-stage <phase>-<stage>` → Start a specific stage (e.g., `/start-stage 2-1`)
- `/start-stage 0` → Workflow Engineer
- `/export-log <phase>-<stage>` → Export conversation log

### Natural Language

- "Start stage 3-4" → Mood Guide
- "What stage are we in?" → Check `docs/<story>/` for artifacts
- "Review chapter 5" → Stage 7-1

### Built-in Commands

- `/export <file>` → Export conversation
- `/compact` → Compress long conversations

---

## Project Structure

```
project-root/
├── AGENTS.md                    ← You are here
├── BRANCH-INFORMATION.md
├── CLAUDE.md
├── GEMINI.md
├── .claude/
│   ├── settings.json
│   └── skills/
│       ├── start-stage/
│       └── export-log/
├── .agent-utils/
│   └── skills/
│       ├── start-stage/
│       └── export-log/
├── imported-artifacts/
├── docs/
│   ├── logs/
│   ├── workflow-changelog.md
│   └── <story-name>/
│       ├── format-medium.md
│       ├── story-seed.md
│       ├── main-character.md
│       ├── world-initial-state.md
│       ├── world-end-state.md
│       ├── antagonists.md
│       ├── key-events.md
│       ├── phase-1-consolidation.md
│       ├── world-rules.md
│       ├── geography.md
│       ├── races-cultures.md
│       ├── religions-mythology.md
│       ├── politics-power.md
│       ├── supporting-characters.md
│       ├── narrative-style.md
│       ├── anti-patterns.md
│       ├── phase-2-consolidation.md
│       ├── visual-identity.md
│       ├── soundscape.md
│       ├── sensory-palette.md
│       ├── mood-guide.md
│       ├── character-voices.md
│       ├── character-dynamics.md
│       ├── phase-3-consolidation.md
│       ├── central-conflict.md
│       ├── major-arcs.md
│       ├── progression-map.md
│       ├── consequence-map.md
│       ├── phase-4-consolidation.md
│       ├── chapter-format.md
│       ├── chapter-outline.md
│       ├── scene-descriptions.md
│       ├── story-design-package/
│       ├── assets/
│       │   ├── images/
│       │   └── audio/
│       └── chapters/
│           ├── chapter-01.md
│           └── chapter-02.md
└── workflow/
    ├── stages/
    │   ├── phase-0/
    │   ├── phase-1/
    │   ├── phase-2/
    │   ├── phase-3/
    │   ├── phase-4/
    │   ├── phase-5/
    │   ├── phase-6/
    │   └── phase-7/
    ├── shared/
    ├── templates/
    └── scripts/
```

---

## Project Status

> Identify the story first. Check `docs/<story-name>/` for existing artifacts.

### Meta Artifacts
- [ ] `workflow-changelog.md`

### Phase 1: Concept & Foundation
- [ ] `format-medium.md`
- [ ] `story-seed.md`
- [ ] `main-character.md`
- [ ] `world-initial-state.md`
- [ ] `world-end-state.md`
- [ ] `antagonists.md`
- [ ] `key-events.md`
- [ ] **`phase-1-consolidation.md`** ← Phase 1 complete

### Phase 2: World & Rules
- [ ] `world-rules.md`
- [ ] `geography.md`
- [ ] `races-cultures.md`
- [ ] `religions-mythology.md`
- [ ] `politics-power.md`
- [ ] `supporting-characters.md`
- [ ] `narrative-style.md`
- [ ] `anti-patterns.md`
- [ ] **`phase-2-consolidation.md`** ← Phase 2 complete

### Phase 3: Sensory & Identity
- [ ] `visual-identity.md`
- [ ] `soundscape.md`
- [ ] `sensory-palette.md`
- [ ] `mood-guide.md`
- [ ] `character-voices.md`
- [ ] `character-dynamics.md`
- [ ] **`phase-3-consolidation.md`** ← Phase 3 complete

### Phase 4: Narrative Arcs
- [ ] `central-conflict.md`
- [ ] `major-arcs.md`
- [ ] `progression-map.md`
- [ ] `consequence-map.md`
- [ ] **`phase-4-consolidation.md`** ← Phase 4 complete

### Phase 5: Chapter Planning
- [ ] `chapter-format.md`
- [ ] `chapter-outline.md`
- [ ] `scene-descriptions.md`
- [ ] **`story-design-package/`** ← Phase 5 complete

### Phase 6: Writing
- [ ] Chapter 01 drafted
- [ ] *(add rows as chapters are planned in Stage 5-2)*

### Phase 7: Review *(on-demand)*
- [ ] Book review complete
- [ ] Series review complete *(if applicable)*

---

## Final Output

The **Writing Workflow** produces **written chapters** — the actual story text — grounded in a comprehensive design package. Each chapter is developed through a structured cooperative process: design first, scene clarity second, writing third, review on-demand.
