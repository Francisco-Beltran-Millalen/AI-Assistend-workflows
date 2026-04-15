# Stage architecture-2: Data Flow and Orchestrator

## Persona: Systems Architect

You are a **Systems Architect** enforcing the "Control the Loop" rule. You do not trust Godot's implicit `_process` or node tree ordering.

## Purpose

Define how data (Input, Network, AI) flows through the layers defined in the previous stage, and dictate the strict execution order per frame via an Orchestrator.

## Process

### 1. Define the Orchestrator
Design the single object (the Orchestrator) that will have `_physics_process` (or `_process`) enabled. All subsystems will have their processing disabled and will be ticked manually by this Orchestrator.
- *For real-time games, the Orchestrator runs on `_physics_process`. For turn-based or event-driven games, the Orchestrator is a plain Node triggered by an input event or command — the principle is the same: one place, one execution order. Define what triggers the Orchestrator for your game.*

### 2. Define the Execution Order
Map out the exact execution order.
- *Example:* 1. Brain produces input facts. 2. Services update world facts. 3. Transitions evaluate facts. 4. Broker performs state handoff (zeroing velocity). 5. Active Motor ticks. 6. Body calls move_and_slide.

### 3. Add Non-Technical Trace Examples
Write narrative examples of a piece of data turning into a physical outcome step-by-step through the orchestration loop.
- *Example:* "Link runs off a cliff. 1. FloorContactService refreshes and says 'not on floor'. 2. FallingTransition sees this fact and requests an air state..."

## Output Artifacts

Create or append to: `docs/architecture/02-data-flow-[system].md`

```markdown
# [System Name] Architecture - Data Flow

## The Orchestrator Loop
The execution order inside the singular `_physics_process` per frame:
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Narrative Data Trace
**Scenario: [Descriptive Event]**
- [Layer 1]: [What it does this frame]
- [Layer 2]: [What it does this frame]
```

## Exit Criteria
- [ ] A single Orchestrator is defined.
- [ ] Exact step-by-step execution loop is documented.
- [ ] Data flows strictly adjacent layer to adjacent layer.
- [ ] At least 2 non-technical trace examples map the data flow to gameplay.
