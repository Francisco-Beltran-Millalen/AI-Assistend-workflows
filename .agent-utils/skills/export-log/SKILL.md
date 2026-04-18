# Export Log Skill

Export the current conversation to a log file in `docs/logs/`.

## Arguments

- Stage identifier:
  - `0` for meta-workflow
  - `teacher` for teacher
  - `<phase-name>-<stage-number>` for regular stages (e.g., `graybox-1`, `gdd-2`)
  - `<phase-name>-<stage-number>-<variant>` for variant stages (e.g., `asset-4-2d`, `asset-4-3d`)

## Process

1. Find the current session's transcript file — location is tool-specific, defined in the CLI adapter
2. Run the tool-specific converter script to convert it to readable text
3. Save to `docs/logs/` using the naming convention below

**Naming format:** `stage-<identifier>-<name>-<YYYYMMDD>-<HHMMSS>.txt`

Examples:
- `stage-00-meta-workflow-20260319-091500.txt`
- `stage-teacher-20260319-091500.txt`
- `stage-mechanic-1-mechanic-spec-20260319-143022.txt`
- `stage-graybox-5-code-writer-20260319-143022.txt`

## Stage Names

### On-Demand Stages
- 0 → `00-meta-workflow`
- teacher → `teacher`
- plan-eval → `plan-eval`

### gdd-kickstart: GDD Kickstart
- gdd-1 → `gdd-1-vision-and-references`
- gdd-2 → `gdd-2-gameplay-experience`
- gdd-3 → `gdd-3-systems-design`
- gdd-4 → `gdd-4-aesthetics-and-world`
- gdd-5 → `gdd-5-knowledge-research`
- gdd-6 → `gdd-6-technical-roadmap`
- gdd-7 → `gdd-7-agent-export`

### architecture: System Architecture
- architecture-0 → `architecture-0-system-map`
- architecture-1 → `architecture-1-scope-and-boundaries`
- architecture-2 → `architecture-2-data-flow`
- architecture-3 → `architecture-3-edge-cases`
- architecture-4 → `architecture-4-systems-and-components`
- architecture-5 → `architecture-5-project-scaffold`
- architecture-6 → `architecture-6-interfaces-and-contracts`
- architecture-audit → `architecture-audit-architecture-audit`

### mechanic: Mechanic Analysis
- mechanic-1 → `mechanic-1-mechanic-spec`
- mechanic-2 → `mechanic-2-mechanic-design`

### graybox: Graybox Prototype (Godot)
- graybox-1 → `graybox-1-project-initiator`
- graybox-2 → `graybox-2-plan-generator`
- graybox-4 → `graybox-4-rule-enforcer`
- graybox-5 → `graybox-5-code-writer`
- graybox-6 → `graybox-6-auditor`
- graybox-7 → `graybox-7-debugger`

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

### writing: Game Writing
- writing-1 → `writing-1-story-foundation`
- writing-2 → `writing-2-world-lore`
- writing-3 → `writing-3-character-voices`
- writing-4 → `writing-4-scene-plan`
- writing-5 → `writing-5-writing-loop`

### testing: Unit Testing
- testing-1 → `testing-1-test-scaffold`
- testing-2 → `testing-2-test-loop`

### fusion: Fusion
- fusion-1 → `fusion-1-integration`
