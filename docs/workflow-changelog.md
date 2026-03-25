# Workflow Changelog

Each entry records a significant design decision — what problem it solved and what changed. Minor fixes (typos, missing prefixes, step numbering) are not recorded here.

---

## 2026-03-25: Full audit — implementation-decisions template + teacher reading order

**Problem:** Two issues found in a thorough audit of all workflow files:
1. `implementation-decisions.md` template referenced `docs/tech-stack.md` (pre-consolidation artifact) instead of `consolidation-artifacts/tech-stack-consolidation.md`. This would cause every Phase 4 project to point the persistence document at the wrong source of truth.
2. `implementation-decisions.md` template was missing the `## Design Changes` section, which is required by `workflow/shared/01-phase-4-artifact-authority.md` (step 5 of the protocol) and explicitly referenced in Stage 4-2 and Stage 4-guided.
3. Teacher Knowledge Test reading order unconditionally listed old `docs/tech-stack.md`, `docs/data-model-physical.md`, and `docs/api-design.md` without fallback logic — contradicting the "Using Project Artifacts" section in the same file which correctly prioritizes consolidation artifacts.
**Cause:** Template and stage file were not updated when the consolidation refactor introduced the authority hierarchy. The teacher's knowledge test section was written before the consolidation artifact pattern was finalized.
**Fix:**
1. Template `## Tech Stack` pointer: `docs/tech-stack.md` → `consolidation-artifacts/tech-stack-consolidation.md`
2. Added `## Design Changes` section to the template with the correct log format from `01-phase-4-artifact-authority.md`
3. Rewrote teacher Knowledge Test reading order to use consolidation artifacts as primary source with `docs/` fallback (consistent with the rest of the file)
**Files:** `workflow/templates/ai/implementation-decisions.md`, `workflow/stages/phase-0/04-teacher.md`

---

## 2026-03-25: Docker replaces native psql as PostgreSQL prerequisite

**Problem:** The workflow assumed a native `psql` install for schema validation and DB setup. The project uses Docker for PostgreSQL, so native psql commands don't apply.
**Fix:** Docker added as a required prerequisite. All `psql` commands updated to show the Docker variant (`docker exec -i <container> psql ...`) as primary, with native psql as a fallback. The old "Planned" Docker comment in PREREQUISITES.md removed.
**Files:** `PREREQUISITES.md`, `README.md`, `workflow/stages/phase-2/02-data-modeling.md`, `workflow/stages/phase-2/04-consolidation.md`

---

## 2026-03-25: Full workflow audit — 5 stale/missing references fixed

**Problem:** Post-consolidation-refactor audit surfaced stale `docs/` references and missing handoff descriptions.
**Cause:** The 2026-03-25 consolidation refactor updated stage instructions but missed a few example strings, a template footer, a handoff summary line, and the teacher's artifact guidance section.
**Fix:** Five targeted edits:
1. Stage 4-2 example code: `[per tech-stack.md]` → `[per tech-stack-consolidation.md]`
2. Teacher "Using Project Artifacts" section: updated to reference consolidation artifacts (with fallback note for early phases)
3. AGENTS.md Phase 2→3 handoff: added missing `docs/view-entity-mapping.md`
4. Template footer (`data-model-physical.md`): `tech-stack.md` → `tech-stack-consolidation.md`
5. README.md quick check script: added missing `git` check (present in PREREQUISITES.md, missing in README)
**Files:** `workflow/stages/phase-4/02-implementation-loop.md`, `workflow/stages/phase-0/04-teacher.md`, `AGENTS.md`, `workflow/templates/ai/data-model-physical.md`, `README.md`

---

## 2026-03-25: Stage 4-guided — domain failures + edge case sweep

**Decision:** Add a structured moment to surface domain-level failures and edge cases before module contracts are locked.

Domain failures (state conflicts, quota limits, time windows, concurrent writes) are a distinct class that falls between validation errors and business logic. Edge cases are hard to think of on the spot without prompting examples. Neither had a dedicated step in the design conversation.

**Changes:**
- Level 5 now generates 3–5 contextual domain failure examples from the actual use case (using entity names from the data model) and asks which apply. Result documented under "Domain failures" with error codes.
- Edge Case Sweep section added between Level 9 and Module Contracts: 2–3 contextual edge cases per module drawn from standard patterns (null/not-found, empty collection, concurrent modification, FK violation). Unhandled cases are added to the relevant level before contracts are locked.
- Test coverage and exit criteria updated to include both.

**Files:** `workflow/stages/phase-4/programming-loop-guided.md`

---

## 2026-03-25: Stage 4-guided — 9-level design conversation + design journal

**Decision:** Expand the design conversation from 6 coarse levels to 9 structured levels, and produce a self-contained design document that any agent can implement from without conversation context.

The former "Business Rules" level mixed validations, authorization, business logic, and side effects — each of which warrants its own conversation and produces different artifacts. The sign-off also lived only in conversation, with no persistent artifact.

**Changes:**
- Expanded to 9 levels: Inputs/Outputs → Happy Path → Validation Rules → Authorization → Business Logic → Side Effects → Data Operations → Module Map → Tech Mapping
- Concrete examples added on Levels 1–4 (example scenario, example JSON, example validation failure, example auth failure)
- ASCII call-flow diagrams on Level 8; typed code stubs on Level 9
- Design journal: `consolidation-artifacts/designs/[use-case-slug].md` created at start of each use case, filled in section by section as levels are confirmed, marked Approved at Green Light and Implemented at checkpoint
- Green Light includes a self-containment check before approval

**Files:** `workflow/stages/phase-4/programming-loop-guided.md`

---

## 2026-03-25: Consolidation artifact refactor + stage 4-guided rename

**Decision:** Make consolidation artifacts the sole source of truth for Phase 4, split them into meaningful granular files, and establish an explicit authority protocol for Phase 4 to update them.

Phase 4 stages were reading 7+ scattered `docs/` files. Consolidation stages existed but were not treated as authoritative. When implementation revealed design changes, there was no mechanism to update the consolidation documents.

**Changes:**
- Stage 1-6 now produces three files: `project-summary.md`, `use-cases-consolidation.md`, `tech-stack-consolidation.md`
- Stage 2-4 now produces two files: `data-model-consolidation.md`, `api-design-consolidation.md`
- All Phase 4 stages reference only `consolidation-artifacts/` — no `docs/` files
- New shared protocol `workflow/shared/01-phase-4-artifact-authority.md` defines when/how Phase 4 updates consolidation artifacts
- `implementation-decisions.md` gains a `## Design Changes` section to record updates with rationale
- Stage 4-2b (Design-First Implementation) renamed to Stage 4-guided (Guided Implementation); file renamed to `programming-loop-guided.md`

**Files:** `workflow/shared/01-phase-4-artifact-authority.md` (new), `workflow/stages/phase-1/06-consolidation.md`, `workflow/stages/phase-2/04-consolidation.md`, `workflow/stages/phase-3/05-consolidation.md`, `workflow/stages/phase-4/programming-loop-guided.md`, all Phase 4 stages, `AGENTS.md`, `.agent-utils/skills/start-stage/SKILL.md`

---

## 2026-03-21: Always use latest stable versions

**Decision:** Add an explicit rule to always use the latest stable version of any tool, library, or framework unless the user specifies otherwise.

No instruction existed about version selection — leaving it ambiguous whether to prefer stability, familiarity, or recency.

**Files:** `AGENTS.md` (Critical Rules), `workflow/stages/phase-1/05-tech-selection.md`

---

## 2026-03-20: Stage 4-guided (formerly 4-2b) — design-first implementation mode

**Decision:** Add a third implementation mode where the user owns the design but not the typing.

The workflow offered two extremes: full AI authorship (Stage 4-2) or full user authorship (Stage 4-3). Users who wanted to control architecture without writing every line had no path.

**Process:** User describes architecture map → AI reviews dependency directions → User defines module contracts (name, path, input, output, errors) → Green light sign-off → AI writes code module by module.

**Files:** `workflow/stages/phase-4/programming-loop-guided.md` (new at the time), `AGENTS.md`, `.agent-utils/skills/start-stage/SKILL.md`

---

## 2026-03-17: Phase-0 persona fusion — 6 on-demand stages collapsed to 2

**Decision:** Merge 6 on-demand stages into 2 multi-mode stages to reduce friction and make related capabilities available in the same session.

Switching between workflow maintenance, git operations, and artifact import required separate stage invocations even though they share context. Teaching, knowledge testing, and diagrams had the same problem.

**Changes:**
- Stage 0 (Meta-Workflow) absorbs git operations and artifact import. Now has three modes: workflow maintenance, git operations, artifact import.
- Stage teacher absorbs knowledge tester and diagram assistant. Now has four modes: teaching, rubber duck, knowledge test, diagram.
- Deleted: `01-diagram-assistant.md`, `02-import-artifact.md`, `03-knowledge-tester.md`, `05-git-assistant.md`

**Files:** `workflow/stages/phase-0/00-meta-workflow.md`, `workflow/stages/phase-0/04-teacher.md`, `AGENTS.md`, skill files

---

## 2026-03-15: CWD-independent hook scripts

**Decision:** Anchor hook script paths to the git root instead of the current working directory.

Hooks failed when Claude Code's working directory changed (e.g., `cd prototype-code/` during Phase 4). Relative paths in `.claude/settings.json` broke whenever CWD wasn't the project root.

**Fix:** Both hook commands now use `git rev-parse --show-toplevel` to resolve the script path regardless of CWD.

**Files:** `.claude/settings.json`

---

## 2026-03-09: AGENTS.md split into branch-specific files

**Decision:** Extract web-specific content from `AGENTS.md` into `WEB-AGENT.md` (and `GAME-AGENT.md`), keeping `AGENTS.md` as a thin shared entry point that delegates to the branch-specific file.

`AGENTS.md` had grown to 575 lines with both web and game context loaded in every session regardless of the active branch. A web project session loaded game-specific stage tables and checklists unnecessarily.

**Note:** Later consolidated back into a single `AGENTS.md` on the web branch when the repository was restructured as a single-branch template.

**Files:** `AGENTS.md`, `WEB-AGENT.md` (created), `.agent-utils/skills/start-stage/SKILL.md`

---

## 2026-03-09: Web workflow generalized — flexible frontend and auth

**Decision:** Remove SPA-only and JWT-only constraints. Frontend rendering approach and authentication mechanism are now real decision points in Stage 1-5.

The workflow hardcoded SPA as the only frontend rendering approach and JWT as the only auth mechanism. Projects using SSR, hybrid rendering, MPA (HTMX), session-based auth, or OAuth could not use the workflow correctly.

**Changes:** Frontend rendering (SPA / SSR / Hybrid / MPA) and auth mechanism (JWT / Sessions / OAuth / Hybrid) added as explicit decision tables in Stage 1-5. Downstream stages reference `tech-stack.md` rather than hardcoding assumptions.

**Files:** `workflow/stages/phase-1/05-tech-selection.md`, `workflow/stages/phase-1/06-consolidation.md`, `workflow/stages/phase-2/03-endpoint-design.md`, `workflow/stages/phase-3/05-consolidation.md`, Phase 4 stages, `AGENTS.md`

---

## 2026-03-06: Stage 4-4: Refactor — structured cleanup before deployment

**Decision:** Add a dedicated refactor stage after all use cases are implemented, to address architecture drift before deployment.

After Phase 4 implementation, prototypes accumulate inconsistent error handling, missing input validation, security basics not enforced, and layer rule violations. No structured stage addressed this.

**Process:** Audit across 5 dimensions (error handling, validation, security, layer rules, config) → propose refactor roadmap → user approves → implement one area at a time → verify tests pass → 5-question comprehension check.

**Files:** `workflow/stages/phase-4/04-refactor.md` (new), Phase 4 stages, `AGENTS.md`

---

## 2026-03-06: Web workflow restructuring — branching architecture

**Decision:** Rename `workflow/spa-rest-sql/` to `workflow/web/` and establish a branching architecture where Phase 1 is generic and Phase 2+ branches by project type.

The workflow had no branching concept. All content was in a single linear path named for a specific technology stack. The generalization allows other specializations (game, CLI, mobile) to share Phase 1.

**Files:** `workflow/web/` (renamed from `workflow/spa-rest-sql/`), `AGENTS.md`, skill files, `workflow/stages/phase-5/01-deployment.md` (new skeleton)

---

## 2026-03-01: Comprehension check after each use case

**Decision:** Add a mandatory comprehension verification step after each use case is implemented, before moving to the next one.

Users were moving to the next use case without narrating what was just built. No mechanism ensured understanding between sessions.

**Changes:**
- Stage 4-2: 5-question check after tests pass (functions written, inputs/outputs, purpose, layer, data flow). Up to 3 attempts before proceeding.
- Stage 4-3: Full end-to-end narration (HTTP request through all layers to response). Same 3-attempt rule.

**Files:** `workflow/stages/phase-4/02-implementation-loop.md`, `workflow/stages/phase-4/03-learning-guide.md`

---

## 2026-02-28: Stage 4-1 — architecture selection + implementation roadmap

**Decision:** Add an upfront architectural decision and an approved implementation order before any code is written.

Phase 4 had no architecture decision. The implementation loop improvised structure per use case with no agreed rules. Implementation order was also deferred to the first Stage 4-2 session — meaning no approval before code started.

**Changes:**
- Part 2 added to Stage 4-1: architecture pattern selection (Ports & Adapters, Layered, Clean Architecture) with pattern-specific rules; folder structure proposal; implementation roadmap (approved use-case order based on dependencies)
- `implementation-decisions.md` template updated to include Architecture and Implementation Roadmap sections

**Files:** `workflow/stages/phase-4/01-project-setup.md`, `workflow/stages/phase-4/02-implementation-loop.md`, `workflow/stages/phase-4/03-learning-guide.md`

---

## 2026-02-28: Existing Artifact Protocol — handle stage re-runs

**Decision:** Standardize behavior when a stage's output artifacts already exist (re-runs, iterations, direction changes).

The workflow was originally designed as a linear sequence (each stage runs once). Re-runs were not designed for — the AI would improvise, sometimes overwriting, sometimes ignoring existing work.

**Fix:** Created `workflow/shared/00-existing-artifact-protocol.md`. When output artifacts exist: read them, show a summary, ask why (iteration / direction change / tech change / error correction / other), proceed per reason. Special cases: Stages 3-2/3-3/3-4 and Stage 2-4 skip the protocol because they update shared artifacts that pre-exist by design.

**Files:** `workflow/shared/00-existing-artifact-protocol.md` (new), `.agent-utils/skills/start-stage/SKILL.md`, `workflow/stages/phase-3/01-visual-design.md`

---

## 2026-02-27: Stage 4-3 Learning Guide — user-authored implementation mode

**Decision:** Add a second implementation mode where the Code Mentor guides the user to write the code themselves.

Stage 4-2 (AI writes, user reviews) was good for shipping but not for learning. Users with weaker technical skills didn't build understanding by approving code they didn't write.

**Process:** AI asks what the code should do → corrects misunderstandings → user writes → AI reviews. Shares the same `implementation-decisions.md` persistence document with Stage 4-2 so both modes can be used on the same project.

**Files:** `workflow/stages/phase-4/03-learning-guide.md` (new)

---

## 2026-02-27: Test design step + git-commit skill

**Decision:** Add a test design approval step before tests are written, and a stage-aware git-commit skill.

In Stage 4-2, the AI wrote tests and the user just ran them — no engagement with what the tests should cover. Commit messages were also manual with no stage context.

**Changes:**
- Stage 4-2: Step "Design Tests" added before writing. AI proposes Scenario / Input / Expected Output for each test; user approves before code is written.
- Stage 4-3: Guided test design loop — AI asks what scenarios to cover, corrects omissions with questions (not answers).
- `/git-commit` skill: stage-aware commit messages (feat/chore/design/docs/workflow prefix); walks through each command one at a time with approval.
- `/run-all-tests` and `/run-stage-tests` skills created.

**Files:** `workflow/stages/phase-4/02-implementation-loop.md`, `workflow/stages/phase-4/03-learning-guide.md`, skill files

---

## 2026-02-27: SPA+JWT specialization (later reversed)

**Decision:** Specialize the workflow exclusively to SPA + stateless JWT. Renamed `workflow/web-rest-sql/` to `workflow/spa-rest-sql/`.

Every project run at the time used SPA+JWT. Server-rendered paths added noise and conditional complexity throughout every Phase 4 stage.

**Note:** This decision was reversed in 2026-03-09 when the workflow was re-generalized to support all frontend/auth approaches.

---

## 2026-02-19: consolidation-artifacts/ and prototype-code/ folders

**Decision:** Add a clear separation between committed project artifacts (`consolidation-artifacts/`) and working/intermediate files (`docs/`), and designate `prototype-code/` as the home for all application code.

All artifacts lived in `docs/`, which was gitignored. No clean answer existed for "what gets committed?" and no specified location existed for the Phase 4 application code.

**Files:** `consolidation-artifacts/` (new), `prototype-code/` (new), all stage files referencing consolidation docs, `AGENTS.md`, `README.md`

---

## 2026-02-19: Published to GitHub + README + .gitignore

**Decision:** Version-control the workflow and write a README explaining its philosophy.

The workflow had no README, no `.gitignore`, and was not version controlled — impossible to share, back up, or reuse.

**`.gitignore` strategy:** Ignore project-generated artifacts (`docs/*.md` except `workflow-changelog.md`, session logs, `imported-artifacts/` content). Preserve folder structure via `.gitkeep` files.

**README covers:** What this is (a process, not a tool), the 7 core philosophies, the web specialization, prerequisites, quick start, project structure, slash commands, and how to build other workflow specializations.

**Files:** `README.md` (new), `.gitignore` (new)

---

## 2026-02-18: .agent-utils/ — multi-tool canonical layer

**Decision:** Create a tool-agnostic canonical skill layer in `.agent-utils/`, with `.claude/` as a thin wrapper. `AGENTS.md` becomes the canonical workflow entry point; `CLAUDE.md` and `GEMINI.md` redirect to it.

The workflow was Claude Code-specific. `AGENTS.md` is the Linux Foundation / Agentic AI Foundation standard (December 2025) adopted by Claude Code, Gemini CLI, GitHub Copilot, and others. Adding support for a new tool should require only: a converter script + two thin skill wrappers.

**Changes:**
- `workflow/scripts/convert_transcript_generic.py` — abstract base class
- `workflow/scripts/convert_transcript_claude.py` — Claude implementation
- `.agent-utils/skills/start-stage/SKILL.md` — canonical skill instructions
- `.agent-utils/skills/export-log/SKILL.md` — canonical naming convention
- `.claude/skills/` — thin wrappers delegating to `.agent-utils/`
- `AGENTS.md` becomes the canonical file; `CLAUDE.md` and `GEMINI.md` redirect to it

**Files:** `workflow/scripts/` (2 new, 1 deleted), `.agent-utils/skills/` (new), `.claude/skills/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`

---

## 2026-02-18: Python 3 replaces jq in workflow scripts

**Decision:** Rewrite `convert-transcript.sh` and `session-start.sh` to use Python 3 (standard library only) instead of `jq`.

`jq` is not pre-installed on Debian or macOS, causing silent failures on any new machine. Python 3 is a documented prerequisite; `jq` was not.

**Files:** `workflow/scripts/convert-transcript.sh`, `workflow/scripts/session-start.sh`, `PREREQUISITES.md` (new)
