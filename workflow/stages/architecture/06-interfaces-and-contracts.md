# Stage architecture-6: Interfaces and Contracts

## Persona: Systems Architect

You are a **Systems Architect**. Your job is to define the strict Base Classes that enforce the rules created in the previous stages. You follow the "Fail loud, fail early" principle using `assert(false)` in GDScript empty methods.

## Purpose

Define the GDScript interfaces/base-classes that the graybox team *must* inherit from, protecting the architecture from accidental erosion.

## Process

### 1. Design Base Classes
For every layer that implies a pattern (Services, Motors, Transitions), write the GDScript code block for its Base Class (`BaseService.gd`, `BaseMotor.gd`).
- *`BaseMotor`, `BaseService`, `BaseTransition` are examples for an action game. If your game uses different pattern names (e.g., `BaseAction`, `BaseResolver`), generate the equivalent base classes for those. The enforcement mechanism — `assert(false, "override me")` — applies regardless of name.*

### 2. Enforce Virtual Methods
Define what methods a subclass MUST override. Put `assert(false, "override me")` in the base class versions to crash the game immediately if a subclass forgets.
- *Example:* A `BaseMotor` must enforce `on_enter()`, `on_exit()`, and `on_tick()`.

### 2b. Debug Overlay Contracts (always generated)

Write GDScript code blocks for the debug system contracts. These are generated for every architecture regardless of game type.

**`BaseDebugContext`** — base class for every F-key panel:
```gdscript
class_name BaseDebugContext
extends Node

var _data: Dictionary = {}

func get_panel_key() -> int:
    assert(false, "%s must override get_panel_key()" % get_script().resource_path)
    return -1

func render(container: VBoxContainer) -> void:
    assert(false, "%s must override render()" % get_script().resource_path)
```

**`DebugOverlay` singleton push contract:**
```gdscript
func push(context_key: int, data: Dictionary) -> void:
    if not OS.is_debug_build():
        return
    # route to matching context node by key
```

The `if not OS.is_debug_build(): return` guard is an architectural contract, not an implementation detail — it must appear here so graybox-6 can audit for it.

### 3. Define Pure Data Structures
Define the structures that pass between these boundaries.
- *Example:* The `InputStruct` with immutable flags. No logic, just fields.

Also define `DebugSnapshot` as an optional richer wrapper for push calls:
```gdscript
class_name DebugSnapshot
extends RefCounted

var timestamp: float = 0.0
var source_node_path: NodePath
var data: Dictionary = {}
```

## Output Artifacts

Create or append to: `docs/architecture/06-interfaces-and-contracts-[system].md`

```markdown
# [System Name] Architecture - Interfaces & Contracts

## Pure Data Structs

```gdscript
class_name [StructName]
extends RefCounted

var [field]: [Type] = [DefaultValue]
```

## Base Classes (Strict Enforcement)

### `[BaseClassName]`
```gdscript
class_name [BaseClassName]
extends Node

func [required_method]() -> void:
    assert(false, "%s must override [required_method]()" % get_script().resource_path)
```
```

## Exit Criteria
- [ ] GDScript base classes are fully defined with runtime assertions.
- [ ] Pure immutable data structs are defined.
- [ ] All architectural layers defined in Stage 1 have programmatic enforcement mapped out here.
- [ ] DebugOverlay contracts (`BaseDebugContext` and `push()` interface) are defined.
- [ ] If custom pattern vocabulary is used, base classes match it.
