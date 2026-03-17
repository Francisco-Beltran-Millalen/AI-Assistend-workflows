# Start Stage Skill

Start the specified workflow stage.

## Arguments

- Stage identifier:
  - `0` for meta-workflow
  - `diagram` for diagram-assistant
  - `import` for import-artifact
  - `knowledge` for knowledge-tester
  - `teacher` for teacher
  - `git` for git-assistant
  - `<phase>-<stage>` for regular stages (e.g., `2-1` for Phase 2 Stage 1)

## Instructions

1. Parse the stage identifier and build the file path using base `workflow/stages/`:
   - If `0`: Read `workflow/stages/phase-0/00-meta-workflow.md`
   - If `diagram`: Read `workflow/stages/phase-0/01-diagram-assistant.md`
   - If `import`: Read `workflow/stages/phase-0/02-import-artifact.md`
   - If `knowledge`: Read `workflow/stages/phase-0/03-knowledge-tester.md`
   - If `teacher`: Read `workflow/stages/phase-0/04-teacher.md`
   - If `git`: Read `workflow/stages/phase-0/05-git-assistant.md`
   - If `<phase>-<stage>`: Read `workflow/stages/phase-<phase>/0<stage>-*.md`
2. Adopt the persona defined in the stage file
3. For Phase 1–4 stages only (not 0, diagram, import, knowledge, teacher, git): check if the stage's output artifacts (listed in `## Output Artifacts`) already exist. If any do, read `workflow/shared/00-existing-artifact-protocol.md` and follow it before proceeding to step 4.
4. Follow the stage process

## Stage Mapping

### On-Demand Stages
- 0: meta-workflow (fix workflow issues)
- diagram: diagram-assistant (visualize artifacts)
- import: import-artifact (import and adapt external artifacts)
- knowledge: knowledge-tester (pre-meeting knowledge check)
- teacher: teacher (Socratic teaching sessions)
- git: git-assistant (version control operations)

### Phase 1: Discovery + Tech Selection
- 1-1: project-definition
- 1-2: knowledge-audit
- 1-3: research
- 1-4: mechanic-discovery
- 1-5: tech-selection
- 1-6: consolidation

### Phase 2: Game Design
- 2-1: core-loop-design
- 2-2: entity-design
- 2-3: level-design (optional — skip if no distinct levels)
- 2-4: consolidation

### Phase 3: Visual & Audio Design
- 3-1: visual-design (primitives: shapes, colors, sizes, HUD, menus)
- 3-2: audio-design (SFX list, music plan — skeleton)
- 3-3: consolidation

### Phase 4: Prototype Implementation
- 4-1: project-setup
- 4-2: implementation-loop (repeats per mechanic; AI implements, user reviews)
- 4-3: learning-guide (repeats per mechanic; user implements, AI guides)
- 4-4: refactor (once, after all mechanics done; plan-first, comprehension check at end)

### Phase 5: Distribution
- 5-1: distribution (skeleton — process defined per project)

## Example Usage

```
/start-stage 0
```
Starts Stage 0 (Meta-Workflow) with the Workflow Engineer persona.

```
/start-stage 2-1
```
Starts Phase 2, Stage 1 (Core Loop Design) with the Game Designer persona.

```
/start-stage 4-2
```
Starts Phase 4, Stage 2 (Implementation Loop) with the Senior Developer persona.
