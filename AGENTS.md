# AGENTS.md — Web Workflow (REST + SQL)

This is the **Web Workflow** — a structured, AI-collaborative process for building web application prototypes with REST endpoints and SQL persistence.

**Branch:** `web` — See `BRANCH-INFORMATION.md` for branch metadata.

**Before doing any work, identify which stage we're in and read the corresponding stage file.**

## Stage Files

### On-Demand Stages

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 0 | `workflow/stages/phase-0/00-meta-workflow.md` | Workflow Engineer | `workflow-changelog.md`, `imported-artifacts/*-imported.md` |
| teacher | `workflow/stages/phase-0/04-teacher.md` | Patient Teacher | `assets/diagrams/*.md` (diagram mode); no artifacts otherwise |

### Phase 1: Discovery + Tech Selection

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 1-1 | `workflow/stages/phase-1/01-project-definition.md` | Project Initiator | `project-brief.md` |
| 1-2 | `workflow/stages/phase-1/02-knowledge-audit.md` | Knowledge Auditor | `knowledge-audit.md` |
| 1-3 | `workflow/stages/phase-1/03-research.md` | Research Analyst | `research-findings.md` |
| 1-4 | `workflow/stages/phase-1/04-use-case-discovery.md` | Use Case Analyst | `use-cases.md` |
| 1-5 | `workflow/stages/phase-1/05-tech-selection.md` | Tech Lead | `tech-stack.md`, `adrs/` |
| 1-6 | `workflow/stages/phase-1/06-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-1-consolidation.md`** |

### Phase 2: Sketching & Data Modeling

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 2-1 | `workflow/stages/phase-2/01-entity-ui-sketching.md` | Domain Modeler + UI Sketcher | `entity-map.md`, `assets/views/*.html`, `view-entity-mapping.md` |
| 2-2 | `workflow/stages/phase-2/02-data-modeling.md` | Data Architect | `data-model-conceptual.md`, `data-model-physical.md`, `assets/schema.sql`, `assets/diagrams/entity-diagram.md` |
| 2-3 | `workflow/stages/phase-2/03-endpoint-design.md` | API Designer | `api-design.md` (with JSON contracts + view-endpoint mapping) |
| 2-4 | `workflow/stages/phase-2/04-consolidation.md` | Technical Writer | **`consolidation-artifacts/phase-2-consolidation.md`**, `assets/` |

### Phase 3: UI Polish

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 3-1 | `workflow/stages/phase-3/01-visual-design.md` | UI Designer | Main view styled, `phase-3-design-decisions.md`, `assets/css/styles.css` |
| 3-2 | `workflow/stages/phase-3/02-core-app-views.md` | UI Designer | Core app views styled |
| 3-3 | `workflow/stages/phase-3/03-user-views.md` | UI Designer | User views styled |
| 3-4 | `workflow/stages/phase-3/04-auth-views.md` | UI Designer | Auth views styled |
| 3-5 | `workflow/stages/phase-3/05-consolidation.md` | Technical Writer | **`consolidation-artifacts/ui-style-guide.md`**, updated `index.html` |

**`phase-3-design-decisions.md`** is a living artifact shared across all Phase 3 stages.

### Phase 4: Prototype Implementation

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 4-1 | `workflow/stages/phase-4/01-project-setup.md` | Senior Developer | Architecture pattern + rules, implementation roadmap, `prototype-code/` (working skeleton), `consolidation-artifacts/implementation-decisions.md` |
| 4-2 | `workflow/stages/phase-4/02-implementation-loop.md` | Senior Developer | Working prototype, `implementation-decisions.md` |
| 4-3 | `workflow/stages/phase-4/03-learning-guide.md` | Code Mentor | Working prototype, `implementation-decisions.md` |
| 4-4 | `workflow/stages/phase-4/04-refactor.md` | Senior Architect | Refactored prototype, `implementation-decisions.md` (refactoring section) |

**Stage 4-1** establishes the architecture pattern (Ports & Adapters, Layered, or Clean Architecture), its binding rules, and the approved use case implementation order — before any code is written.

**Stages 4-2 and 4-3 are alternatives** — use 4-2 (AI writes, you review) or 4-3 (you write, AI guides) per use case. Both repeat until all use cases are complete, following the architectural rules and order established in Stage 4-1. `implementation-decisions.md` is a shared persistence document — read at the start of every session, updated after every completed use case (checkpoint).

**Stage 4-4** runs once after all use cases are implemented. It audits the codebase, proposes a refactor roadmap (error handling, input validation, security basics, layer enforcement), then refactors one area at a time with a plan approved before each change. Ends with a 5-question comprehension check on what was changed and why.

### Phase 5: Deployment

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 5-1 | `workflow/stages/phase-5/01-deployment.md` | Deployment Engineer | Deployed prototype |

**Phase 5 is a skeleton** — the process is minimal and will be expanded as deployment experience grows.

---

## Architectural Assumptions

This workflow is scoped to a specific application type:
- **Web application** (browser-based UI)
- **REST API** (JSON over HTTP)
- **SQL database** (relational persistence)
- **SQLite for prototyping** (always, regardless of production DB)

Decided in Stage 1-5 (Tech Selection):
- **Frontend rendering approach** — SPA, SSR, hybrid, or MPA
- **Authentication mechanism** — JWT, sessions, OAuth, or hybrid

These are real decision points, not fixed constraints. The chosen approach is recorded in `docs/tech-stack.md` and shapes Phase 3 and Phase 4.

---

## Phase Handoffs

### Phase 1 → Phase 2

Stage 1-6 produces `consolidation-artifacts/phase-1-consolidation.md` (includes tech stack summary) — the **primary input** for Phase 2.

### Phase 2 → Phase 3

Stage 2-4 consolidates Phase 2 work into `consolidation-artifacts/phase-2-consolidation.md` — the primary artifact forwarded to Phase 3. Also forwarded: `docs/view-entity-mapping.md` (Stage 2-1), `docs/api-design.md` (Stage 2-3, includes view-endpoint mapping with JSON contracts), and the `docs/assets/` folder.

### Phase 3 → Phase 4

Stage 3-5 consolidates all Phase 3 work into `consolidation-artifacts/ui-style-guide.md` — a comprehensive style guide whose Decision Log captures everything from `phase-3-design-decisions.md` (the Phase 3 working document, which is not forwarded to Phase 4). Phase 4 uses all prior artifacts: styled views, endpoint contracts, SQLite schema, and tech stack.

The styled HTML views from Phase 3 are **design references** for frontend development in Phase 4. For SPA/hybrid projects: no template conversion needed — backend is a pure JSON API. For SSR/MPA projects: views serve as templates for server-side rendering.

### Phase 4 → Phase 5

Phase 4 produces a refactored working prototype: all use cases implemented, all tests passing, architecture cleaned up (Stage 4-4). Phase 5 deploys it to a real environment. The process is minimal now and will be expanded as deployment experience grows.

---

## How to Determine Current Stage

Check `docs/` for existing artifacts:

**Phase 1 (Discovery + Tech Selection):**
- No artifacts → Stage 1-1
- `project-brief.md` → Stage 1-2
- `knowledge-audit.md` → Stage 1-3
- `research-findings.md` → Stage 1-4
- `use-cases.md` → Stage 1-5
- `tech-stack.md` → Stage 1-6
- `consolidation-artifacts/phase-1-consolidation.md` → Phase 1 complete

**Phase 2 (Sketching & Data Modeling):**
- `consolidation-artifacts/phase-1-consolidation.md` exists but no `entity-map.md` → Stage 2-1
- `entity-map.md` → Stage 2-2
- `data-model-physical.md` → Stage 2-3
- `api-design.md` → Stage 2-4
- `consolidation-artifacts/phase-2-consolidation.md` → Phase 2 complete

**Phase 3 (UI Polish):**
- `consolidation-artifacts/phase-2-consolidation.md` exists but no `phase-3-design-decisions.md` → Stage 3-1
- `phase-3-design-decisions.md` + styled main view → Stage 3-2
- Core app views styled → Stage 3-3
- User views styled → Stage 3-4
- Auth views styled → Stage 3-5
- `consolidation-artifacts/ui-style-guide.md` → Phase 3 complete

> To detect Phase 3 sub-stages: read `docs/phase-3-design-decisions.md` → View Decisions section. First check the **Main View (reference implementation)** entry — if it is still plain HTML, Stage 3-1 is incomplete; continue Stage 3-1. Otherwise, views marked INCLUDE that still have plain HTML (no CSS framework classes applied) indicate the current unfinished stage based on their category: core app views → still in 3-2, user views → still in 3-3, auth views → still in 3-4.

**Phase 4 (Prototype Implementation):**
- `consolidation-artifacts/ui-style-guide.md` exists but no `consolidation-artifacts/implementation-decisions.md` → Stage 4-1
- `consolidation-artifacts/implementation-decisions.md` exists (use cases not all complete) → Stage 4-2 or 4-3 (user's choice per use case)
- `consolidation-artifacts/implementation-decisions.md` with all use cases complete but no `## Refactoring` section → Stage 4-4
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

This creates: `docs/logs/stage-2-1-entity-ui-sketching-20260203-143022.txt`

### Log Naming Convention

Format: `stage-<phase>-<stage>-<name>-<YYYYMMDD>-<HHMMSS>.txt`

Examples:
- `stage-00-meta-workflow-20260203-091500.txt`
- `stage-1-4-use-case-discovery-20260203-143022.txt`
- `stage-2-1-entity-ui-sketching-20260204-101530.txt`

---

## On-Demand Stages

**On-demand stages** are not part of the phase cycle. Invoke them anytime:
- **Stage 0** (`/start-stage 0`) — Workflow maintenance, git operations, and artifact import
- **Stage teacher** (`/start-stage teacher`) — Teaching (Socratic), rubber duck mode, pre-meeting knowledge test, diagrams

---

## Critical Rules

1. **ALWAYS read the stage file** before starting work
2. **ALWAYS adopt the persona** defined in the stage file
3. **ALWAYS use `/start-stage`** to start stages — it automatically runs the Existing Artifact Protocol, which detects prior runs and asks how to proceed before any work begins
4. **In Phase 3: ALWAYS read `docs/phase-3-design-decisions.md` first** — it persists decisions across sessions
5. **In Phase 4: ALWAYS read `implementation-decisions.md` first** — it tracks progress and decisions across sessions
6. **Follow stage order** within each phase
7. **Complete each phase before starting the next**

---

## Quick Commands

### Slash Commands (Skills)

- `/start-stage <phase>-<stage>` → Start a specific stage (e.g., `/start-stage 2-1`)
- `/start-stage 0` → Workflow Engineer (workflow fixes, git ops, artifact import)
- `/start-stage teacher` → Teacher (teaching, rubber duck, knowledge test, diagrams)
- `/export-log <phase>-<stage>` → Export conversation to docs/logs/

### Natural Language

- "Start stage 2-1" → Entity & UI Sketching
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
│   ├── assets/                  ← Views, CSS, SQL, diagrams
│   ├── adrs/                    ← Architecture Decision Records
│   └── *.md                     ← Working design artifacts
└── workflow/
    ├── stages/                  ← Stage files organized by phase
    │   ├── phase-0/             ← On-demand stages
    │   ├── phase-1/             ← Discovery + Tech Selection
    │   ├── phase-2/             ← Sketching & Data Modeling
    │   ├── phase-3/             ← UI Polish
    │   ├── phase-4/             ← Prototype Implementation
    │   └── phase-5/             ← Deployment (skeleton)
    ├── shared/                  ← Shared protocols (Existing Artifact Protocol)
    ├── templates/               ← Output templates
    └── scripts/                 ← Automation scripts
```

---

## Artifact Storage

- Phase milestone documents: `consolidation-artifacts/`
- Working prototype code: `prototype-code/`
- Working design artifacts: `docs/`
- Assets (views, CSS, SQL): `docs/assets/`
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
- [ ] `use-cases.md`
- [ ] `tech-stack.md`
- [ ] `adrs/` (decision records)
- [ ] **`consolidation-artifacts/phase-1-consolidation.md`** ← Phase 1 complete

### Phase 2: Sketching & Data Modeling
- [ ] `entity-map.md`
- [ ] `assets/views/` (plain HTML)
- [ ] `view-entity-mapping.md`
- [ ] `data-model-conceptual.md` (agnostic)
- [ ] `data-model-physical.md` (SQLite)
- [ ] `assets/schema.sql` (SQLite with mock data)
- [ ] `assets/diagrams/entity-diagram.md`
- [ ] `api-design.md` (with JSON contracts + view-endpoint mapping)
- [ ] **`consolidation-artifacts/phase-2-consolidation.md`** ← Phase 2 complete

### Phase 3: UI Polish
- [ ] `phase-3-design-decisions.md` ← Living decisions file (all stages read/update)
- [ ] `assets/css/styles.css`
- [ ] Styled main view ← Stage 3-1 complete
- [ ] Styled core app views ← Stage 3-2 complete
- [ ] Styled user views ← Stage 3-3 complete
- [ ] Styled auth views ← Stage 3-4 complete
- [ ] **`consolidation-artifacts/ui-style-guide.md`** ← Phase 3 complete

### Phase 4: Prototype Implementation
- [ ] `prototype-code/` created ← Stage 4-1 complete
- [ ] `consolidation-artifacts/implementation-decisions.md` initialized ← Stage 4-1 complete
- [ ] All use cases implemented + tested (per Implementation Roadmap order)
- [ ] **All tests passing** ← Prototype complete (4-2/4-3 done)
- [ ] Refactor roadmap approved ← Stage 4-4 started
- [ ] All refactor areas complete + comprehension check passed ← Stage 4-4 complete

### Phase 5: Deployment
- [ ] Prototype deployed to a real environment ← Phase 5 complete

---

## Final Output

The **Web Workflow** produces a **deployed working prototype** with:
- Implemented REST endpoints for all use cases
- SQLite database with mock data
- Automated tests (unit + integration)
- Styled HTML views
- Complete design documentation
- Deployment to a real environment
