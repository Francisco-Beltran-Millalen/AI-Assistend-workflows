# Workflow Changelog

---

## 2026-04-18: Final audit cleanup — architecture import routing and explainer coverage

**Problem:** The last review pass found three small but real workflow mismatches. Stage 0 import detection still skipped `architecture-0`, the `explain-artifact` skill still omitted both `architecture-0` and `architecture-audit`, and `graybox-2` still had duplicated pre-condition numbering.

**Cause:** These were tail-end consistency gaps left after the larger architecture clustering and graybox contract refactors.

**Fix:**
- Added an explicit Stage 0 heuristic row for system maps, architecture grouping, cluster batching, and cross-system coupling so those imports route to `architecture-0`.
- Expanded the `explain-artifact` stage map to include `architecture-0` and `architecture-audit`, keeping the explainer aligned with the current architecture workflow.
- Renumbered the `graybox-2` pre-condition checklist so the plan generator prompt reads as a clean sequential gate again.

**Files:**
- `workflow/stages/phase-0/00-meta-workflow.md`
- `.agent-utils/skills/explain-artifact/SKILL.md`
- `workflow/stages/graybox/02-plan-generator.md`
- `docs/workflow-changelog.md`

---

## 2026-04-18: Re-audit fixes — graybox debug flow aligned with DebugOverlay contracts

**Problem:** A further audit found that the graybox implementation stages still referred to a legacy `DebugManager` pattern, while the architecture phase had already standardized on `DebugOverlay` plus `BaseDebugContext`. This created a direct contract break: graybox setup would build the wrong debug singleton, and later plan/code/audit stages would enforce the wrong integration model.

**Cause:** The architecture debug overlay contract was introduced after the older graybox debug instructions, but the graybox stage files were not fully normalized afterward.

**Fix:**
- Updated `graybox-1` to create the `DebugOverlay` autoload instead of `DebugManager`, wire the `toggle_debug_overlay` input action, and instantiate the required `BaseDebugContext` children for the current `[group]`.
- Updated `graybox-2` so execution plans describe debug hooks in terms of `DebugOverlay.push()` payloads and consuming `BaseDebugContext` nodes.
- Updated `graybox-5` and `graybox-6` so implementation and audit rules enforce the `DebugOverlay` / `BaseDebugContext` contract instead of `DebugManager.debug_enabled`.

**Files:**
- `workflow/stages/graybox/01-project-initiator.md`
- `workflow/stages/graybox/02-plan-generator.md`
- `workflow/stages/graybox/05-code-writer.md`
- `workflow/stages/graybox/06-auditor.md`
- `docs/workflow-changelog.md`

---

## 2026-04-18: Re-audit fixes — downstream mechanic/graybox stages now consume architecture `[group]` artifacts

**Problem:** A second audit found that the architecture phase had already moved to cluster-scoped `[group]` artifacts, but several downstream stages still hardcoded per-system architecture paths. `mechanic-1`, `mechanic-2`, `graybox-1`, `graybox-2`, and `graybox-4` all referenced `docs/architecture/*-[system].md`, which would cause later phases to miss cluster-scoped architecture documents entirely. The new `explain-artifact` skill also still taught users to think in terms of `-[system]` dynamic suffixes.

**Cause:** The architecture refactor landed first, but the mechanic and graybox handoff stages were not fully normalized afterward. The result was a split-brain workflow: architecture produced `[group]` artifacts, while its consumers still looked for `[system]` files.

**Fix:**
- Updated `mechanic-1`, `mechanic-2`, `graybox-1`, `graybox-2`, and `graybox-4` to reference `docs/architecture/*-[group].md`.
- Added explicit guidance in mechanic/graybox stages to identify the owning architecture `[group]` and use per-system sub-sections inside cluster-scoped artifacts when relevant.
- Updated the `explain-artifact` skill text so it refers to dynamic `-[group]` suffixes and multiple architecture groups.

**Files:**
- `workflow/stages/mechanic/01-mechanic-spec.md`
- `workflow/stages/mechanic/02-mechanic-design.md`
- `workflow/stages/graybox/01-project-initiator.md`
- `workflow/stages/graybox/02-plan-generator.md`
- `workflow/stages/graybox/04-rule-enforcer.md`
- `.agent-utils/skills/explain-artifact/SKILL.md`
- `docs/workflow-changelog.md`

---

## 2026-04-18: Audit fixes — architecture-0 registration, [group] naming, and GDD section numbering

**Problem:** A pre-commit audit found that the new cluster-scoped architecture workflow was only partially wired into the repo. `AGENTS.md` still described architecture artifacts as per-system (`[system]`) and did not mention the new required `architecture-0` system-map stage. The `start-stage` and `export-log` skills also had no explicit handling for `architecture-0`. Separately, `AGENTS.md` still tracked `gdd-2` through `gdd-6` against the wrong Human GDD section numbers.

**Cause:** The stage files and supporting docs were updated at different times. The architecture stage files had already moved to `[group]` semantics and required `00-system-map.md`, but the canonical workflow registry and CLI skill maps still reflected the older per-system model.

**Fix:**
- Updated `AGENTS.md` architecture stage table, stage-detection logic, and project-status checklist to use `architecture-0`, `00-system-map.md`, and `[group]` artifact names.
- Added `architecture-0` explicit path handling to the `start-stage` skill and stage-name mapping to the `export-log` skill.
- Corrected the `gdd-kickstart` status checklist in `AGENTS.md` so gdd-2 through gdd-6 map to Human GDD Sections 4 through 8.

**Files:**
- `AGENTS.md`
- `.agent-utils/skills/start-stage/SKILL.md`
- `.agent-utils/skills/export-log/SKILL.md`
- `docs/workflow-changelog.md`

---

## 2026-04-18: GDD kickstart — practical examples, visual anti-references, and condensed technical framing

**Problem:** After running a first full GDD, the `gdd-kickstart` phase had three weak spots. The stages asked good questions, but lacked concrete examples of strong vs weak answers. The workflow captured positive references, but not explicit image-based anti-references with a rationale. And the `gdd-6` technical section encouraged a broader roadmap dump than the Human GDD actually needs that early.

**Cause:** The phase was optimized for open-ended discovery, but not enough for calibration. Without examples, users can answer too vaguely. Without anti-reference images, the workflow defines only the target, not the forbidden zone. Without tighter `gdd-6` framing, the GDD can start duplicating work meant for later architecture and mechanic phases.

**Fix:**
- Added short strong/weak answer examples directly inside `gdd-1` through `gdd-6` so the coaching happens at the point of use.
- Extended the Human GDD template and `gdd-1` to support Section 1 visual anti-references with explicit rejection rationales.
- Updated `gdd-7` so it strips coaching/examples/placeholders but preserves resolved anti-references in `docs/agent-gdd.xml` as structured negative constraints under `<anti_references>`.
- Tightened `gdd-6` to a compact decision brief plus MVP boundaries and directional milestones instead of a pseudo-architecture deep dive.
- Updated `asset-1` input review notes so the Art Director explicitly reads already-defined anti-references.

**Files:**
- `workflow/templates/human-gdd-template.md`
- `workflow/stages/gdd-kickstart/01-vision-and-references.md`
- `workflow/stages/gdd-kickstart/02-gameplay-experience.md`
- `workflow/stages/gdd-kickstart/03-systems-design.md`
- `workflow/stages/gdd-kickstart/04-aesthetics-and-world.md`
- `workflow/stages/gdd-kickstart/05-knowledge-research.md`
- `workflow/stages/gdd-kickstart/06-technical-roadmap.md`
- `workflow/stages/gdd-kickstart/07-agent-export.md`
- `workflow/stages/asset/01-art-direction.md`
- `docs/workflow-changelog.md`

---

## 2026-04-18: GDD kickstart consistency pass — placeholder replacement, folder names, PDF export docs

**Problem:** The `gdd-kickstart` phase had internal contradictions after the full-template change. gdd-1 now creates the full GDD skeleton up front, but gdd-2 through gdd-6 still instructed the agent to "append" sections, which would encourage duplicated headers instead of filling the existing placeholders. Two stage files also referenced asset subfolders that gdd-1 never creates (`5-systems-design`, `6-aesthetics-and-world`). Separately, gdd-7, `PREREQUISITES.md`, and the exporter script docs still referred to `weasyprint` and `python3`, while the actual implementation uses `xhtml2pdf` and this repo is commonly used on Windows where `python` is the safer default executable name.

**Cause:** gdd-1 and the template were modernized first, but the downstream stage instructions and PDF-export documentation were not fully normalized afterward.

**Fix:**
- Updated gdd-2 through gdd-6 to explicitly replace the existing section placeholders instead of appending new sections.
- Added guidance in gdd-2 through gdd-4 to move image slots from the Image Gallery into the target section before replacing them with actual links.
- Fixed the section-folder examples in gdd-3 and gdd-4 to match the real directories created by gdd-1 and listed in the template (`5-systems`, `6-aesthetics`).
- Updated gdd-7 and `workflow/scripts/gdd_to_pdf.py` usage text to use `python workflow/scripts/gdd_to_pdf.py`.
- Corrected PDF-export dependency references from `weasyprint` to `xhtml2pdf` in the script docs and `PREREQUISITES.md`.

**Files:**
- `workflow/stages/gdd-kickstart/02-gameplay-experience.md`
- `workflow/stages/gdd-kickstart/03-systems-design.md`
- `workflow/stages/gdd-kickstart/04-aesthetics-and-world.md`
- `workflow/stages/gdd-kickstart/05-knowledge-research.md`
- `workflow/stages/gdd-kickstart/06-technical-roadmap.md`
- `workflow/stages/gdd-kickstart/07-agent-export.md`
- `workflow/scripts/gdd_to_pdf.py`
- `PREREQUISITES.md`
- `docs/workflow-changelog.md`

---

## 2026-04-15: Pre-commit audit — stage header naming, artifact references, section consistency

**Problem:** Full workflow audit before commit revealed 4 categories of issues.

**Fix:**
- **export-log SKILL.md:** Fixed incorrect example stage identifier `gameconcept-2` → `gdd-2`.
- **feel-1:** Removed reference to `docs/game-feel-direction.md` (never produced by any stage); replaced with `docs/mechanic-spec.md` which contains the feel contracts.
- **gdd-kickstart stages 1–7:** All 7 stage file headers used `# Stage: Gameconcept-N:` (legacy name). Renamed to `# Stage gdd-N:` to match AGENTS.md identifiers and the naming pattern of all other stage files.
- **gdd-1 and gdd-7:** `## Output Artifact` (singular) → `## Output Artifacts` (plural) to match every other stage file. `gdd-2` through `gdd-6` retain `## Output Update` which is intentionally different (they append to an existing file).

**Files:**
- `.agent-utils/skills/export-log/SKILL.md`
- `workflow/stages/feel/01-graybox-feel.md`
- `workflow/stages/gdd-kickstart/01-vision-and-references.md`
- `workflow/stages/gdd-kickstart/02-gameplay-experience.md`
- `workflow/stages/gdd-kickstart/03-systems-design.md`
- `workflow/stages/gdd-kickstart/04-aesthetics-and-world.md`
- `workflow/stages/gdd-kickstart/05-knowledge-research.md`
- `workflow/stages/gdd-kickstart/06-technical-roadmap.md`
- `workflow/stages/gdd-kickstart/07-agent-export.md`

---

## 2026-04-15: Architecture phase — DebugOverlay + game-type flexibility

**Problem:** (1) No standard in-game debug overlay was part of the architecture design, leading to ad-hoc debug tooling during graybox that breaks composition and data-flow contracts. (2) Architecture stage examples used Motor/Service/Transition vocabulary exclusively, with no signal to the persona that these are action-game illustrations — not prescriptions for every game type.

**Fix:**
- `01-scope-and-boundaries.md`: Added Step 2b ("Declare the Debug Overlay Layer") — always assigns F1–F12 debug context names; added `## Debug Overlay Contexts` table to the output artifact template and exit criteria. Added one-line framing note after Step 2 example clarifying that layer names are domain-specific.
- `02-data-flow.md`: Added one-line clarification after the Orchestrator definition noting that turn-based/event-driven games use a command-triggered Orchestrator instead of `_physics_process`.
- `04-systems-and-components.md`: Added one-line framing note after inventory examples clarifying Motor/Service/Transition are action-game names. Added Step 3b ("Autoloads") with mandatory DebugOverlay entry, performance rules, and artifact template section. Updated exit criteria.
- `05-project-scaffold.md`: Added instruction in Step 2 to show DebugOverlay in a separate `## Autoloads` section (not scene-tree child). Extended scaffold diagram template with Autoloads section and DebugOverlay rationale. Updated exit criteria.
- `06-interfaces-and-contracts.md`: Added one-line framing note in Step 1 for custom vocabulary. Added Step 2b ("Debug Overlay Contracts") with `BaseDebugContext` and `push()` GDScript code blocks. Added `DebugSnapshot` struct to Step 3. Updated exit criteria.

**Files:**
- `workflow/stages/architecture/01-scope-and-boundaries.md`
- `workflow/stages/architecture/02-data-flow.md`
- `workflow/stages/architecture/04-systems-and-components.md`
- `workflow/stages/architecture/05-project-scaffold.md`
- `workflow/stages/architecture/06-interfaces-and-contracts.md`

---

## 2026-04-15: GDD skeleton, image gallery, asset folders, and PDF export

**Problem:** gdd-1 only initialized Section 1 of `docs/human-gdd.md`, with no full document skeleton visible up-front. There was no standard image folder structure, no gallery of image slots for the user to organize, and no way to export the completed GDD to PDF.

**Fix:**
- Created `workflow/templates/human-gdd-template.md`: a full 8-section GDD skeleton with an Image Gallery header listing all image slots across all sections. Users cut-and-paste slots from the gallery to the section where the image belongs.
- Updated gdd-1 to initialize the document by copying the template verbatim (instead of writing only Section 1 inline), and to create the standard `docs/assets/GDD/<section>/` subdirectories on disk.
- Updated gdd-1 image population step: only Section 1 slots are resolved during gdd-1; all others remain in the gallery for subsequent stages.
- Created `workflow/scripts/gdd_to_pdf.py`: a Python script that pre-processes Mermaid blocks with `mmdc` (renders diagrams to PNGs), converts the markdown to HTML via the `markdown` library, and exports `docs/human-gdd.pdf` via `weasyprint`.
- Created `requirements.txt` at project root with `markdown` and `weasyprint` as explicit dependencies.
- Updated gdd-7 (the true last stage of gdd-kickstart) to run the PDF export after the XML is generated, ensuring the PDF reflects any final clarifications made during Agent Export.
- Updated `PREREQUISITES.md` with weasyprint and mermaid-cli install instructions for gdd-7.

**Files modified:**
- `workflow/templates/human-gdd-template.md` (new)
- `workflow/scripts/gdd_to_pdf.py` (new)
- `requirements.txt` (new)
- `workflow/stages/gdd-kickstart/01-vision-and-references.md`
- `workflow/stages/gdd-kickstart/07-agent-export.md`
- `PREREQUISITES.md`

---

## 2026-04-14: Audit sweep, stale reference purge, and legacy folder archiving

**Problem:** After transitioning from the old monolithic graybox structure to the new multi-agent `graybox` execution pipeline (initiator, generator, rule-enforcer, code-writer, auditor, debugger) and the new `gdd-kickstart`, `architecture`, and `mechanic` phases, the repository was littered with stale cross-references. Many stage files, CLI skills, and documentation artifacts still pointed to old paths, old pipeline phases (`gameconcept`), obsolete target files (`game-brief.md`, `graybox-visual-language`, `performance-guidelines.md`), and old `graybox-6` implementation logic.

**Fix:** Conducted a comprehensive, repository-wide search-and-replace sweep.
- Updated all stage input files to point to correct, modern outputs (e.g. `docs/human-gdd.md`, `docs/architecture/*.md`).
- Scrubbed `mechanic-2`, `plan-eval`, `testing-2`, `phase-0`, and `asset` phase files of any stale graybox stage dependencies.
- Updated the CLI `.agent-utils/skills/git-commit/SKILL.md` to reflect the new pipeline stages instead of the old terminology.
- Prevented git clutter by expressly adding the newly created archived folders (`legacy/` and `workflow/stages/legacy/`) into the `.gitignore`.
- Finalized a clean Git commit of the total workflow overhaul, ensuring the multi-agent framework is pristine and ready for Godot 4.6 game development.

**Files modified:**
- Almost every active stage file inside `workflow/stages/*`
- `AGENTS.md` and `README.md`
- `.agent-utils/skills/git-commit/SKILL.md`
- `workflow/common-techniques/INDEX.md`
- `.gitignore` (added legacy folders)

---

## 2026-04-14: Add `architecture` phase

**Problem:** The gameconcept phase historically culminated in a single stage (gameconcept-9) for "architecture consolidation," which failed to bridge the gap between abstract game design concepts and strict Godot-specific code implementation. This led to AI agents going straight from broad designs to unstructured code generation in the graybox phase.

**Fix:** Created an entirely new `architecture` phase spanning 6 distinct stages, placed between `gameconcept-2` and `graybox`. This phase produces six source-of-truth technical documents that define the systemic bedrock using clean architecture patterns adapted for Godot (e.g. strict Base Class contracts, explicitly separated layers, single-orchestrator flows).

**Files created:**
- `workflow/stages/architecture/01-scope-and-boundaries.md`
- `workflow/stages/architecture/02-data-flow.md`
- `workflow/stages/architecture/03-edge-cases.md`
- `workflow/stages/architecture/04-systems-and-components.md`
- `workflow/stages/architecture/05-project-scaffold.md`
- `workflow/stages/architecture/06-interfaces-and-contracts.md`

**Files modified:**
- `AGENTS.md` — inserted the architecture phase stages, adjusted the "Current Stage" checks, and updated the project completion checklist.

---
## 2026-04-09: Add `plan-eval` — Plan Evaluator stage

**Problem:** The graybox-6 mechanic loop has no external validation of design documents before implementation. The designer who wrote the plan evaluates their own work — a known failure mode: models confidently praise plans even when they will fail in implementation.

**Cause:** No GAN-style separation between generator and evaluator in the graybox phase. Phase 4 of graybox-6 relied on self-evaluation against the feel contract.

**Fix:** Added `plan-eval` as a Phase 0 on-demand stage. Inspired by the Anthropic engineering article on harness design for long-running applications. Key design decisions informed by the article:
- Evaluator always runs in a new session (cold context — never saw the design conversation)
- Five criteria weighted toward model weaknesses: feel fit and logic completeness are high-weight (areas generators get wrong silently)
- Hard thresholds: binary PASS/FAIL/PARTIAL per criterion — no partial credit
- Active probing method per criterion (not static checklist)
- Explicit anti-leniency instruction in persona — "looks reasonable" is not a verdict
- Calibration rule: uncertain items must be flagged, not silently resolved in the plan's favor
- REVISE verdict includes specific issue location, consequence, and required fix

Flexible invocation: can be called mid-graybox-6 design conversation (partial design) or after Green Light (complete design). Partial designs receive a partial evaluation plus forward-risk flags for upcoming levels.

**Files created:**
- `workflow/stages/phase-0/05-plan-eval.md`

**Files modified:**
- `AGENTS.md` — added plan-eval to On-Demand Stages table
- `.agent-utils/skills/start-stage/SKILL.md` — added plan-eval to stage mapping and path resolution
- `.agent-utils/skills/export-log/SKILL.md` — added plan-eval to stage names

---

## 2026-04-04: Fix gameconcept-10 missing from export-log stage name map

**Problem:** `gameconcept-10` was absent from the `## Stage Names` section of `.agent-utils/skills/export-log/SKILL.md`. Running `/export-log gameconcept-10` would produce a log file without the correct stage name slug.

**Cause:** Oversight when gameconcept-10 was added to the workflow — the start-stage skill was updated but export-log was not.

**Fix:** Added `- gameconcept-10 → \`gameconcept-10-gdd-consolidation\`` to the gameconcept section of the export-log skill.

**Files:** `.agent-utils/skills/export-log/SKILL.md`

---

## 2026-04-04: Fix misleading variant examples and stale asset-4 labels in skill files

**Problem:** Two issues in `.agent-utils/skills/start-stage/SKILL.md`:
1. Example variant `graybox-4-generative` was used to illustrate the variant syntax, but no such file exists — only `asset-4-2d/3d/mixed` have real variant files. A user running `/start-stage graybox-4-generative` would get a silent glob failure.
2. asset-4 description labels read "production-loop-2d/3d/mixed" but actual filenames are `04-production-2d.md` etc. (no `-loop`). Same misleading label appeared in `export-log/SKILL.md`.

**Cause:** Stale names from an earlier iteration of the stage files; the generative/assisted split in graybox-6 was later collapsed into a single file with an internal mode-select rather than separate variant files.

**Fix:**
- Replaced `graybox-4-generative` with `asset-4-2d` (real example) in both skill files
- Dropped `-loop` from asset-4 description labels in `start-stage/SKILL.md`

**Files:** `.agent-utils/skills/start-stage/SKILL.md`, `.agent-utils/skills/export-log/SKILL.md`

---

## 2026-04-04: Common Techniques — log cleanup, web review, Nintendo references, Godot 4.x sections

**Task 1 — Log cleanup:**
Summarized all 12 session log files (2026-03-19 to 2026-04-04) into a permanent `docs/logs/session-history.md` table (date, session, work done, outcome). Deleted all 12 individual `.txt` log files from `docs/logs/`.

**Task 2 — Web review for correctness:**
Searched for factual errors across the 11 technique files. Two fixes applied:
- `character_controller_architecture_full.md`: Added explicit warning that `RigidBody3D` is not recommended for player characters in Godot 4 — use `CharacterBody3D` (kinematic). Prior text was ambiguous.
- `animation_systems_full.md`: Fixed oversimplification in 2D vs 3D section — modern 2D games also use skeletal animation via `Skeleton2D`, not just sprite switching.

**Task 3 — Nintendo references (all 11 files):**
Added a `## 🎮 Reference Games` table to each file listing relevant Nintendo games. Per each problem area, added `### 🎮 Nintendo Reference` with 2–3 sentences on how a specific shipped game solved that problem. Reference games: Zelda BotW/TotK (3D), Metroid Dread (2D), Fire Emblem: Three Houses (strategy/AI).

**Task 4 — Godot 4.x sections (all 11 files):**
Per each problem area, added `### 🟦 Godot 4.x` with: primary node/API, typed GDScript snippet (5–15 lines, full static typing), and 2 pitfall bullets. All snippets use Godot 4.6 APIs (Jolt physics default, `CharacterBody3D`, `NavigationAgent3D`, `AStarGrid2D`, `AnimationTree`, `SpringArm3D`, `FastNoiseLite`, etc.).

**Files modified:**
- `docs/logs/session-history.md` (created)
- `docs/logs/*.txt` (12 files deleted)
- All 11 `workflow/common-techniques/*_full.md` files
- `workflow/common-techniques/INDEX.md`

---

## 2026-04-04: Common Techniques index, static typing enforcement, no hardcoded values, gameconcept-10 skill fix

**Problem 1:** Technique reference files in `imported-artifacts/` were unindexed and misplaced — they are workflow-level reference material, not project-specific imports, and had no navigation aid.
**Cause:** Files were added to `imported-artifacts/` during an earlier session without being integrated into the workflow structure.
**Fix:** Moved all 11 technique files to `workflow/common-techniques/`. Created `workflow/common-techniques/INDEX.md` with a quick-lookup table, per-file descriptions, and cross-references to graybox-6 design levels. Added `common-techniques/` to the Project Structure in `AGENTS.md`. Added a reference to the index in graybox-6's Input Artifacts section.
**Files:** `workflow/common-techniques/` (new), `AGENTS.md`, `workflow/stages/graybox/06-mechanic-loop.md`

**Problem 2:** GDScript static typing was not explicitly required anywhere in the workflow. Code produced during graybox sessions could use bare `var` and untyped functions without any prompt to type them.
**Cause:** Missing code style rule in the workflow.
**Fix:** Added a "Code Style Rules" section to `workflow/stages/graybox/05-performance-guidelines.md` (process + output template) requiring full static typing for all vars, `@onready` vars, signal parameters, function parameters, and return types. Added explicit enforcement at Level 10 (Godot Mapping), the Green Light checklist, and the Generative mode implementation rules in graybox-6. Fixed lambda type annotations in graybox-4 code samples.
**Files:** `workflow/stages/graybox/05-performance-guidelines.md`, `workflow/stages/graybox/06-mechanic-loop.md`, `workflow/stages/graybox/03-scaffold.md`, `workflow/stages/graybox/04-debug-indicators.md`

**Problem 3:** No rule existed to prevent hardcoded magic numbers, positions, and inline formula results. Mechanics accumulated untunable magic values during prototyping.
**Cause:** Missing code style rule in the workflow.
**Fix:** Added no-hardcoded-values rule to the Code Style Rules section in graybox-5 (requiring `@export var` for tunables, `const` for fixed values, and derived calculations over hardcoded coordinates). Added the rule at Level 4 (State), the Green Light checklist, and Generative mode in graybox-6.
**Files:** `workflow/stages/graybox/05-performance-guidelines.md`, `workflow/stages/graybox/06-mechanic-loop.md`

**Problem 4:** `gameconcept-10` was present in `AGENTS.md` and as a stage file, but missing from the Stage Mapping in `.agent-utils/skills/start-stage/SKILL.md`. Additionally, the path mapping rule `0<stage-number>-*.md` would produce `010-*` for stage 10 (double-digit), which is incorrect.
**Cause:** Stage was added to AGENTS.md and the stage file was created, but the skill was not updated. The path rule was written assuming single-digit stages only.
**Fix:** Added `gameconcept-10: gdd-consolidation` to the Stage Mapping in SKILL.md. Fixed the path rule to use zero-padded 2-digit stage numbers (`<NN>`), which correctly handles both single-digit (01–09) and double-digit (10+) stages.
**Files:** `.agent-utils/skills/start-stage/SKILL.md`

---

## 2026-04-03: Add `gameconcept-10` GDD Consolidation stage

**Problem:** The `gameconcept` phase lacked a final consolidation step to compile the 9 scattered artifacts into a single cohesive Game Design Document (GDD).

**Cause:** The redesign of the gameconcept phase generated multiple individual documents without a master file for human readability and production reference.

**Fix:** Added `gameconcept-10` (Lead Game Designer) as the final step of the `gameconcept` phase. This stage aggregates exact contents of prior artifacts into `.md` and HTML formats, explicitly handling duplications and adding multimedia placeholders.

**Files created:**
- `workflow/stages/gameconcept/10-gdd-consolidation.md`

**Files modified:**
- `AGENTS.md` — added gameconcept-10 to the stage table, detection logic, and project status.

---

## 2026-04-03: Add `writing` and `testing` phases

**Problem:** The workflow had no support for game narrative/dialogue or for automated unit testing of game logic.

**Cause:** The original workflow focused on prototyping mechanics. Writing and testing are commonly needed but were absent.

**Fix:** Added two new workflow phases:

- **writing** (5 stages): story-foundation → world-lore → character-voices → scene-plan → writing-loop. Conditional — for games with narrative/dialogue. Can run in parallel with graybox. Adapted from the AI-assisted writing workflow reference (`C:\Users\francisco\Programming\AI-Assisted-workflow-writing`).
- **testing** (2 stages): test-scaffold (GUT 9.6.0 installation, one-time after graybox-3) + test-loop (per mechanic, after each graybox-6 implementation). Uses GUT 9.6.0 for Godot 4.6.

**Files created:**
- `workflow/stages/writing/01-story-foundation.md`
- `workflow/stages/writing/02-world-lore.md`
- `workflow/stages/writing/03-character-voices.md`
- `workflow/stages/writing/04-scene-plan.md`
- `workflow/stages/writing/05-writing-loop.md`
- `workflow/stages/testing/01-test-scaffold.md`
- `workflow/stages/testing/02-test-loop.md`

**Files modified:**
- `AGENTS.md` — added writing + testing to stage table, detection logic, project status, critical rules, artifact storage, project structure
- `.agent-utils/skills/start-stage/SKILL.md` — added writing + testing stage mappings

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
