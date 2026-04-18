# Architecture Principles

The following principles must govern every system designed in the architecture phase. They are not optional. If a design violates these principles, the architecture is invalid.

## 1. SOLID Principles
Apply SOLID class design principles. Components must have a Single Responsibility, be Open for extension/Closed for modification, allow Liskov substitution for decoupled logic, keep Interfaces Segregated, and Depend on abstractions.

## 2. Structure Enforces Rules, Not Discipline
If a contract can be broken accidentally, the architecture is wrong. Do not rely on developers "remembering not to call a method." Use structural constraints (e.g., passing a `Reader` wrapper instead of the mutable source) to make illegal operations impossible to compile.

## 3. Strict Adjacency
Each layer only talks to the layer next to it. No skipping layers. The `Brain` never talks to the `Body`; the `Brain` only talks to the `Broker`. 

## 4. Fail Loud, Fail Early
Instead of writing "safe" code that silently does nothing when it gets bad data, use strict runtime `assert()` statements. A bug should crash the game immediately point-of-origin. Validate data upon entry to critical paths.

## 5. Data is Blind
Data structures (e.g., `InputStruct`, `SaveState`) must contain zero logic. They are just facts. Logic belongs exclusively to the systems that read those facts.

## 6. Single Source of Truth (SSoT)
If a fact about the game world exists, it lives in exactly one place. No component is allowed to make a local copy of that state; they must ask the owner every time. Duplicated state will eventually desync.

## 7. Composition Over Deep Inheritance
Inheritance trees deeper than 2 levels become prisons. If an entity needs a behavior, give it a child Node (service/component/motor) rather than extending its class.

## 8. Rely on Abstractions, Not Concretions (Dependency Inversion)
A transition shouldn't ask "Am I in the ClimbMotor?". It should ask "Is the current motor interruptible?". Systems should care about what things are, not the specific implementation details or concrete node names.

## 9. Control the Loop (Orchestration over Godot Magic)
Never rely on Godot's implicit node tree order or `process_priority` to determine what runs first. Use a single Orchestrator node that disables implicit ticking in its children and calls `tick()` sequentially in a guaranteed, deterministic order.

## 10. Input is Just Another Fact
The game logic shouldn't care if an input came from a human pressing a keyboard, a network packet from a server, or an AI state machine. The `Brain` produces the intent; the body executes. They must share an identical struct interface.

## 11. State Machines over Boolean Flags
A component cannot have `is_jumping`, `is_falling`, and `is_attacking` booleans simultaneously. State is inherently mutually exclusive. Any mutually exclusive state must be implemented via an explicit Enum or State Machine. Boolean flag soup is an anti-pattern.

## 12. Signals Describe the Past, Commands Describe the Future
Signals must only broadcast things that have already happened (e.g., `health_depleted`). You do not emit a signal to request an action (e.g., `take_damage`); actions are explicit method calls downwards.

## 13. Data Flows Down, Events Flow Up
Parents inject dependencies and call methods on children. Children never call `get_parent()` or reach sideways to `$Sibling`. If a child needs to communicate outward, it broadcasts upward via Signals or callbacks.

## 14. No Global State for Game Logic
Godot Autoloads are reserved strictly for stateless utilities and passive observer overlays (like `DebugOverlay`). Game variables and gameplay state (like `PlayerHealth`, `ComboMeter`) cannot be stored in an Autoload.
