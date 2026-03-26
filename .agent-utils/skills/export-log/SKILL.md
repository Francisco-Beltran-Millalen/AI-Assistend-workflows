# Export Log Skill

Export the current conversation to a log file in `docs/logs/`.

## Arguments

- Stage identifier:
  - `0` for meta-workflow
  - `teacher` for teacher
  - `<phase-name>-<stage-number>` for regular stages (e.g., `graybox-1`, `gameconcept-2`)
  - `<phase-name>-<stage-number>-<variant>` for variant stages (e.g., `graybox-4-generative`, `asset-4-2d`)

## Process

1. Find the current session's transcript file — location is tool-specific, defined in the CLI adapter
2. Run the tool-specific converter script to convert it to readable text
3. Save to `docs/logs/` using the naming convention below

**Naming format:** `stage-<identifier>-<name>-<YYYYMMDD>-<HHMMSS>.txt`

Examples:
- `stage-00-meta-workflow-20260319-091500.txt`
- `stage-teacher-20260319-091500.txt`
- `stage-gameconcept-1-brief-20260319-143022.txt`
- `stage-graybox-5-generative-mechanic-loop-20260319-143022.txt`

## Stage Names

### On-Demand Stages
- 0 → `00-meta-workflow`
- teacher → `teacher`

### gameconcept: Game Concept
- gameconcept-1 → `gameconcept-1-references-analysis`
- gameconcept-2 → `gameconcept-2-references-art`
- gameconcept-3 → `gameconcept-3-references-feel`
- gameconcept-4 → `gameconcept-4-game-description`
- gameconcept-5 → `gameconcept-5-art-direction`
- gameconcept-6 → `gameconcept-6-feel-direction`
- gameconcept-7 → `gameconcept-7-roadmap`
- gameconcept-8 → `gameconcept-8-knowledge-research`
- gameconcept-9 → `gameconcept-9-architecture-consolidation`

### graybox: Graybox Prototype (Godot)
- graybox-1 → `graybox-1-mechanic-spec`
- graybox-2 → `graybox-2-visual-language`
- graybox-3 → `graybox-3-scaffold`
- graybox-4 → `graybox-4-debug-indicators`
- graybox-5-designed → `graybox-5-designed-mechanic-loop`
- graybox-5-generative → `graybox-5-generative-mechanic-loop`
- graybox-5-assisted → `graybox-5-assisted-mechanic-loop`

### asset: Asset Pipeline
- asset-1 → `asset-1-art-direction`
- asset-2 → `asset-2-asset-list`
- asset-3 → `asset-3-concept`
- asset-4-2d → `asset-4-2d-production`
- asset-4-3d → `asset-4-3d-production`
- asset-4-mixed → `asset-4-mixed-production`

### sound: Sound Pipeline
- sound-1 → `sound-1-sound-direction`
- sound-2 → `sound-2-sound-event-list`
- sound-3 → `sound-3-production-loop`

### feel: Feel & Details
- feel-1 → `feel-1-graybox-feel`
- feel-2 → `feel-2-asset-feel`
- feel-3 → `feel-3-sound-feel`

### fusion: Fusion
- fusion-1 → `fusion-1-integration`
