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
  - `<phase-name>-<stage-number>` for regular stages (e.g., `graybox-1`, `gameconcept-2`)

## Instructions

1. Parse the stage identifier and build the file path using base `workflow/stages/`:
   - If `0`: Read `workflow/stages/phase-0/00-meta-workflow.md`
   - If `diagram`: Read `workflow/stages/phase-0/01-diagram-assistant.md`
   - If `import`: Read `workflow/stages/phase-0/02-import-artifact.md`
   - If `knowledge`: Read `workflow/stages/phase-0/03-knowledge-tester.md`
   - If `teacher`: Read `workflow/stages/phase-0/04-teacher.md`
   - If `git`: Read `workflow/stages/phase-0/05-git-assistant.md`
   - If `<phase-name>-<stage-number>`: Read `workflow/stages/<phase-name>/0<stage-number>-*.md`
   - If `<phase-name>-<stage-number>-<variant>` (e.g., `graybox-4-generative`, `asset-4-2d`): Read `workflow/stages/<phase-name>/0<stage-number>-*-<variant>.md`
2. Adopt the persona defined in the stage file
3. For all named phase stages (not 0, diagram, import, knowledge, teacher, git): check if the stage's output artifacts (listed in `## Output Artifacts`) already exist. If any do, read `workflow/shared/00-existing-artifact-protocol.md` and follow it before proceeding to step 4.
4. Follow the stage process

## Stage Mapping

### On-Demand Stages
- 0: meta-workflow (fix workflow issues)
- diagram: diagram-assistant (visualize artifacts)
- import: import-artifact (import and adapt external artifacts)
- knowledge: knowledge-tester (pre-meeting knowledge check)
- teacher: teacher (Socratic teaching sessions)
- git: git-assistant (version control operations)

### gameconcept: Game Concept
- gameconcept-1: brief (raw concept, genre, tone, references)
- gameconcept-2: knowledge-audit (what you know, what you don't)
- gameconcept-3: research (fill the gaps, reference game analysis, audience)

### graybox: Graybox Prototype
- graybox-1: mechanic-spec (identify mechanics + feel contracts)
- graybox-2: visual-language (geometry/color per entity, camera setup)
- graybox-3: scaffold (Bevy project setup, one-time)
- graybox-4-generative: mechanic-loop-generative (AI implements, user reviews — repeating per mechanic)
- graybox-4-assisted: mechanic-loop-assisted (user implements, AI guides and teaches — repeating per mechanic)

### asset: Asset Pipeline
- asset-1: art-direction (style, palette, 2D/3D/mixed decision)
- asset-2: asset-list (enumerate and prioritize all assets)
- asset-3: concept (concept sketch per asset before production)
- asset-4-2d: production-loop-2d (Krita pipeline, sprite sheets, Bevy integration)
- asset-4-3d: production-loop-3d (Blender pipeline, GLTF, Bevy integration)
- asset-4-mixed: production-loop-mixed (both tracks, cohesion rules, Bevy integration)

### sound: Sound Pipeline
- sound-1: sound-direction (sonic identity, tonal rules, references)
- sound-2: sound-event-list (enumerate every SFX event from mechanics + animations + UI)
- sound-3: production-loop (library → record → synthesize fallback, Audacity edit, Bevy integration)

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
/start-stage graybox-4-generative
```
Starts the Graybox Mechanic Loop (AI implements) with the Senior Rust/Bevy Developer persona.

```
/start-stage graybox-4-assisted
```
Starts the Graybox Mechanic Loop (user implements) with the Code Mentor persona.
