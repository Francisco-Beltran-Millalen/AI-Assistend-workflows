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
| 1-1 | `workflow/stages/phase-1/01-project-brief-y-casos-de-uso.md` | Project Analyst | `project-brief.md`, `use-cases.md` |
| 1-2 | `workflow/stages/phase-1/02-stack-tecnico-y-arquitectura.md` | Software Architect | `tech-stack.md` (with Architecture Rules), `adrs/` |
| 1-3 | `workflow/stages/phase-1/03-consolidacion.md` | Technical Writer | **`consolidation-artifacts/project-summary.md`**, **`consolidation-artifacts/use-cases-consolidation.md`**, **`consolidation-artifacts/tech-stack-consolidation.md`** |

### Phase 2: Sketching & Data Modeling

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 2-1 | `workflow/stages/phase-2/01-sketching-de-interfaz.md` | Diseñador Visual de Sistemas | `assets/views/*.html` (con CSS) |
| 2-2 | `workflow/stages/phase-2/02-modelado-de-dominio-y-datos.md` | Arquitecto de Datos | `data-model-conceptual.md`, `data-model-physical.md`, `assets/schema.sql`, `assets/diagrams/entity-diagram.md` |
| 2-3 | `workflow/stages/phase-2/03-diseno-de-api-y-rutas.md` | Diseñador de Contratos | `api-design.md` |
| 2-4 | `workflow/stages/phase-2/04-consolidacion.md` | Redactor Técnico | **`consolidation-artifacts/data-model-consolidation.md`**, **`consolidation-artifacts/api-design-consolidation.md`** |

### Phase 3: UI Polish & Frontend Architecture

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 3-1 | `workflow/stages/phase-3/01-arquitectura-frontend-y-css.md` | Arquitecto UI | Layout base, `docs/phase-3-design-decisions.md`, `docs/assets/css/styles.css` |
| 3-2 | `workflow/stages/phase-3/02-componentes-e-interactividad.md` | Arquitecto de Componentes | Componentes listados e interactividad JS definida |
| 3-3 | `workflow/stages/phase-3/03-ensamblaje-de-vistas.md` | Desarrollador UI | Vistas en calidad de producción |
| 3-4 | `workflow/stages/phase-3/04-consolidacion.md` | Redactor Técnico | **`consolidation-artifacts/ui-style-guide.md`** |

**`phase-3-design-decisions.md`** is a living artifact shared across all Phase 3 stages.

### Phase 4: Prototype Implementation

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 4-1 | `workflow/stages/phase-4/01-setup-y-arquitectura-base.md` | Arquitecto Principal | Skeleton, layers, visibility rules |
| 4-2 | `workflow/stages/phase-4/02-planificacion-por-caso-de-uso.md` | Diseñador Técnico | `consolidation-artifacts/designs/*.md` (Specs and Rust Contracts) |
| 4-3 | `workflow/stages/phase-4/03-implementacion-mecanica.md` | Light Coder | Working code based on specs |
| 4-4 | `workflow/stages/phase-4/04-auditoria-y-refactor.md` | Auditor de Sistemas | Refactored prototype, final QA |

**Stage 4-1** establishes the architecture pattern and boundary rules (e.g. visibility and dependency injection).

**Stage 4-2** isolates design planning for each use case, generating rigid technical specs and explicit empty Rust definitions.

**Stage 4-3** mechanically implements code and tests matching the specs strictly.

**Stage 4-4** runs a global audit on security and layer enforcement once implementation is completed.

### Phase 5: Deployment

| Stage | File | Persona | Output |
|-------|------|---------|--------|
| 5-1 | `workflow/stages/phase-5/01-build-optimizado-y-contenedor.md` | Ingeniero de Contenedores | `Dockerfile`, `docker-compose.yml`, `.env.example`, build release validado localmente |
| 5-2 | `workflow/stages/phase-5/02-entorno-de-produccion.md` | Ingeniero de Infraestructura | Entorno de producción activo, `docs/deployment.md` |
| 5-3 | `workflow/stages/phase-5/03-pipeline-cicd.md` | Ingeniero de Automatización | `.github/workflows/deploy.yml`, pipeline CI/CD funcional |

---

## Architectural Assumptions

This workflow is scoped to a specific application type:
- **Web application** (browser-based UI)
- **REST API** (JSON over HTTP)
- **SQL database** (relational persistence)

Decided in Stage 1-2 (Stack Técnico y Arquitectura):
- **Frontend rendering approach** — SPA, SSR, hybrid, or MPA
- **Authentication mechanism** — JWT, sessions, OAuth, or hybrid

These are real decision points, not fixed constraints. The chosen approach is recorded in `docs/tech-stack.md` and shapes Phase 3 and Phase 4.

---

## Phase Handoffs

### Phase 1 → Phase 2

Stage 1-3 produces three consolidation artifacts:
- `consolidation-artifacts/project-summary.md` — project overview and scope (summarized)
- `consolidation-artifacts/use-cases-consolidation.md` — complete use case list (full)
- `consolidation-artifacts/tech-stack-consolidation.md` — complete stack + ADR decisions (full)

Phase 2 reads only these three files.

### Phase 2 → Phase 3

Stage 2-4 produces two consolidation artifacts:
- `consolidation-artifacts/data-model-consolidation.md` — physical data model + embedded SQL (full)
- `consolidation-artifacts/api-design-consolidation.md` — all endpoint contracts with JSON (full)

Phase 3 reads these plus `docs/assets/views/` (HTML sketches). CSS is created during Stage 3-1.

### Phase 3 → Phase 4

Stage 3-4 consolidates all Phase 3 work into `consolidation-artifacts/ui-style-guide.md` — a comprehensive style guide whose Decision Log captures everything from `phase-3-design-decisions.md` (the Phase 3 working document, which is not forwarded to Phase 4).

Phase 4 reads only consolidation artifacts:
- `consolidation-artifacts/project-summary.md`
- `consolidation-artifacts/use-cases-consolidation.md`
- `consolidation-artifacts/tech-stack-consolidation.md`
- `consolidation-artifacts/data-model-consolidation.md`
- `consolidation-artifacts/api-design-consolidation.md`
- `consolidation-artifacts/ui-style-guide.md`
- `consolidation-artifacts/designs/` (specs generated in Stage 4-2, one per use case)

The `docs/assets/views/` and `docs/assets/css/` folders are also used as design references for frontend development.

The styled HTML views from Phase 3 are **design references** for frontend development in Phase 4. For SPA/hybrid projects: no template conversion needed — backend is a pure JSON API. For SSR/MPA projects: views serve as templates for server-side rendering.

### Phase 4 → Phase 5

Phase 4 produces a refactored working prototype: heavily spec-driven use cases fully implemented and audited. Phase 5 deploys it to a real environment. The process is minimal now and will be expanded as deployment experience grows.

---

## How to Determine Current Stage

Check `docs/` for existing artifacts:

**Phase 1 (Discovery + Tech Selection):**
- No artifacts → Stage 1-1
- `docs/project-brief.md` and `docs/use-cases.md` present but no `docs/tech-stack.md` → Stage 1-2
- `docs/tech-stack.md` exists but no `consolidation-artifacts/tech-stack-consolidation.md` → Stage 1-3
- `consolidation-artifacts/tech-stack-consolidation.md` → Phase 1 complete

**Phase 2 (Sketching & Data Modeling):**
- `consolidation-artifacts/tech-stack-consolidation.md` exists but no `docs/assets/views/` HTML sketches → Stage 2-1
- `docs/assets/views/` exist but no `docs/data-model-physical.md` → Stage 2-2
- `docs/data-model-physical.md` exists but no `docs/api-design.md` → Stage 2-3
- `docs/api-design.md` exists but no `consolidation-artifacts/api-design-consolidation.md` → Stage 2-4
- `consolidation-artifacts/api-design-consolidation.md` → Phase 2 complete

**Phase 3 (UI Polish & Frontend Architecture):**
- `consolidation-artifacts/api-design-consolidation.md` exists but no `docs/phase-3-design-decisions.md` → Stage 3-1
- `docs/phase-3-design-decisions.md` exists but missing components rules → Stage 3-2
- Components defined but not all final views are assembled → Stage 3-3
- All views completed but no `consolidation-artifacts/ui-style-guide.md` → Stage 3-4
- `consolidation-artifacts/ui-style-guide.md` → Phase 3 complete

> To detect Phase 3 progress: read `docs/phase-3-design-decisions.md`. If global CSS and layout are defined, move to 3-2. If JS interaction rules and base components are established there, move to 3-3 to assemble screens. Once all screens from 2-1 and contracts from 2-3 are implemented with high-fidelity polish, run 3-4 to consolidate.

**Phase 4 (Prototype Implementation):**
- `consolidation-artifacts/ui-style-guide.md` exists but no `prototype-code/` folder → Stage 4-1
- Base architecture exists but no specs defined in `consolidation-artifacts/designs/` → Stage 4-2
- Specs exist but cases are not fully coded/tested → Stage 4-3
- Code implemented but not fully audited/refactored → Stage 4-4
- All refactor areas complete → **Prototype refactored → Stage 5-1**

**Phase 5 (Deployment):**
- Phase 4 complete but no `Dockerfile` → Stage 5-1
- `Dockerfile` and `docker-compose.yml` exist and validated locally but no production environment → Stage 5-2
- Production environment live but no `.github/workflows/deploy.yml` → Stage 5-3
- Pipeline passing and deploy automated → **Phase 5 complete**

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
5. **In Phase 4: ALWAYS read `consolidation-artifacts/designs/` first** — contains the active spec files for each use case and tracks implementation progress
6. **Follow stage order** within each phase
7. **Complete each phase before starting the next**
8. **ALWAYS use the latest stable version of any tool, library, or framework** unless the user explicitly specifies otherwise

---

## Quick Commands

### Slash Commands (Skills)

- `/start-stage <phase>-<stage>` → Start a specific stage (e.g., `/start-stage 2-1`)
- `/start-stage 0` → Workflow Engineer (workflow fixes, git ops, artifact import)
- `/start-stage teacher` → Teacher (teaching, rubber duck, knowledge test, diagrams)
- `/export-log <phase>-<stage>` → Export conversation to docs/logs/

### Natural Language

- "Start stage 2-1" → Sketching de Interfaz
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
├── .agents/
│   └── skills/                  ← Canonical, tool-agnostic skill content
│       ├── start-stage/
│       └── export-log/
├── imported-artifacts/          ← Raw imports + adapted *-imported.md files (Stage 0)
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
- Per-use-case design specs (Etapa 4-2, one per use case): `consolidation-artifacts/designs/`
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
- [ ] `docs/project-brief.md`
- [ ] `docs/use-cases.md`
- [ ] `docs/tech-stack.md`
- [ ] `docs/adrs/` (decision records)
- [ ] **`consolidation-artifacts/project-summary.md`**
- [ ] **`consolidation-artifacts/use-cases-consolidation.md`**
- [ ] **`consolidation-artifacts/tech-stack-consolidation.md`** ← Phase 1 complete

### Phase 2: Sketching & Data Modeling
- [ ] `docs/assets/views/` (HTML + CSS sketches)
- [ ] `docs/data-model-conceptual.md` (agnostic)
- [ ] `docs/data-model-physical.md` (PostgreSQL)
- [ ] `docs/assets/schema.sql` (PostgreSQL with mock data)
- [ ] `docs/assets/diagrams/entity-diagram.md`
- [ ] `docs/api-design.md` (contracts + routing)
- [ ] **`consolidation-artifacts/data-model-consolidation.md`**
- [ ] **`consolidation-artifacts/api-design-consolidation.md`** ← Phase 2 complete

### Phase 3: UI Polish & Frontend Architecture
- [ ] `docs/phase-3-design-decisions.md` ← Living decisions file (all stages read/update)
- [ ] `docs/assets/css/styles.css`
- [ ] Layout base and CSS rules established ← Stage 3-1 complete
- [ ] Component inventory and JS interactivity defined ← Stage 3-2 complete
- [ ] All views assembled and production-ready ← Stage 3-3 complete
- [ ] **`consolidation-artifacts/ui-style-guide.md`** ← Phase 3 complete

### Phase 4: Prototype Implementation
- [ ] `prototype-code/` with structure, DB, boundaries established ← Stage 4-1 complete
- [ ] `consolidation-artifacts/designs/` containing strict specs for use cases ← Stage 4-2 complete
- [ ] All code implemented blindly conforming to specs and tested ← Stage 4-3 complete
- [ ] Security and pattern audit performed ← Stage 4-4 complete

### Phase 5: Deployment
- [ ] `Dockerfile` (multi-stage) + `docker-compose.yml` validados localmente ← Stage 5-1 complete
- [ ] Entorno de producción activo + `docs/deployment.md` ← Stage 5-2 complete
- [ ] Pipeline CI/CD `.github/workflows/deploy.yml` funcional ← Phase 5 complete

---

## Final Output

The **Web Workflow** produces a **deployed working prototype** with:
- Implemented REST endpoints for all use cases
- PostgreSQL database with mock data
- Automated tests (unit + integration)
- Styled HTML views
- Complete design documentation
- Deployment to a real environment
