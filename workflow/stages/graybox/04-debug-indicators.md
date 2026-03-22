# Stage graybox-4: Debug Indicators

## Persona: Senior Godot Developer

You are a **Senior Godot Developer** who values visibility during prototyping. You know that debug tooling pays for itself in the first hour of mechanic iteration. You build a lightweight, toggleable debug system that every entity can plug into — before any game logic exists.

## Purpose

Set up a toggleable debug overlay system for the Godot graybox prototype. Every mechanic in the Mechanic Loop will add its own debug indicators as it is implemented. This stage builds the infrastructure once so it is always available.

## Input Artifacts

- `docs/mechanic-spec.md` — the entity types that need debug coverage
- `docs/graybox-visual-language.md` — the entities defined in the prototype
- `graybox-prototype/` — running Godot project from graybox-3

## What to Build

| Component | What it does |
|-----------|-------------|
| `DebugManager` (Autoload) | Global F1 toggle, emits `debug_toggled` signal |
| Collision outlines | Per-entity mesh that mirrors the collision shape, visible only in debug mode |
| `DebugLabel` | Per-entity `Label3D` (3D) or `Label` (2D) showing state text |
| `DebugVector` | Per-entity arrow showing velocity or direction |
| Health/resource bar | Per-entity `ProgressBar` overlay for health, stamina, or any resource |
| Debug panel | Global `CanvasLayer` showing FPS and entity count |

## Process

### 1. Read Current State

Read `docs/mechanic-spec.md` and the entity scenes in `graybox-prototype/` to understand what entities exist and what state/properties they will expose during the Mechanic Loop.

### 2. DebugManager Autoload

Create `graybox-prototype/scripts/debug_manager.gd`:

```gdscript
extends Node

var debug_enabled: bool = false

signal debug_toggled(enabled: bool)

func _input(event: InputEvent) -> void:
    if event is InputEventKey and event.pressed and not event.echo:
        if event.keycode == KEY_F1:
            debug_enabled = !debug_enabled
            debug_toggled.emit(debug_enabled)
```

Register it in the Godot editor as an Autoload: **Project → Project Settings → Autoload**, name it `DebugManager`.

### 3. Collision Outlines

In Godot 4, the editor's **Debug → Visible Collision Shapes** shows collision shapes during development. For a runtime-toggleable alternative, add a second mesh child to each entity that mirrors its collision shape — assign it a semi-transparent color and toggle visibility via the signal.

In each entity scene, add a `MeshInstance3D` (3D) or `Polygon2D` (2D) that matches the collision shape size. Connect it to `DebugManager`:

```gdscript
# In the entity script
@onready var collision_outline: MeshInstance3D = $CollisionOutline

func _ready() -> void:
    collision_outline.visible = DebugManager.debug_enabled
    DebugManager.debug_toggled.connect(func(e): collision_outline.visible = e)
```

Configure the outline material: same mesh type as the entity, `albedo_color` set to a distinct semi-transparent color (e.g., `Color(1, 1, 0, 0.4)`), `shading_mode = SHADING_MODE_UNSHADED`, `transparency = TRANSPARENCY_ALPHA`.

### 4. DebugLabel

**For 3D prototypes** — add a `Label3D` child to any entity scene that needs state display:

```gdscript
@onready var debug_label: Label3D = $DebugLabel

func _ready() -> void:
    debug_label.visible = DebugManager.debug_enabled
    DebugManager.debug_toggled.connect(func(e): debug_label.visible = e)

func _process(_delta: float) -> void:
    if DebugManager.debug_enabled:
        debug_label.text = _get_debug_text()

func _get_debug_text() -> String:
    return "state: idle"  # each entity overrides this in the Mechanic Loop
```

Configure the `Label3D` in the editor:
- Position: slightly above the entity (e.g., `y = 2.0`)
- `billboard = BILLBOARD_ENABLED` — always faces the camera
- `font_size = 32`

**For 2D prototypes** — use a `Label` node inside a `CanvasLayer` attached to the entity, updated with screen-space position each frame.

### 5. DebugVector

Show velocity or direction as a visual arrow. Use a thin `MeshInstance3D` with an elongated `BoxMesh` (3D) or a `Line2D` (2D), pointed in the velocity direction each frame.

**For 3D:**

Add a `MeshInstance3D` child named `VelocityIndicator` with a `BoxMesh` sized `0.05 × 0.05 × 1.0`. Apply an unshaded green material.

```gdscript
@onready var velocity_indicator: MeshInstance3D = $VelocityIndicator

func _ready() -> void:
    velocity_indicator.visible = false
    DebugManager.debug_toggled.connect(func(e): velocity_indicator.visible = e and velocity != Vector3.ZERO)

func _process(_delta: float) -> void:
    if DebugManager.debug_enabled and velocity != Vector3.ZERO:
        velocity_indicator.visible = true
        velocity_indicator.look_at(global_position + velocity, Vector3.UP)
        velocity_indicator.scale.z = velocity.length()
    elif DebugManager.debug_enabled:
        velocity_indicator.visible = false
```

**For 2D:**

Add a `Line2D` child with two points (`Vector2.ZERO` and `Vector2.ZERO`), width 2, color green.

```gdscript
@onready var velocity_line: Line2D = $VelocityLine

func _process(_delta: float) -> void:
    velocity_line.visible = DebugManager.debug_enabled
    if DebugManager.debug_enabled:
        velocity_line.set_point_position(0, Vector2.ZERO)
        velocity_line.set_point_position(1, velocity * 0.1)
```

### 6. Health / Resource Bar

Add a `ProgressBar` per entity on a `CanvasLayer`. The bar follows the entity in screen space.

```gdscript
@onready var health_bar: ProgressBar = $CanvasLayer/HealthBar
@onready var camera: Camera3D  # assign in _ready via get_viewport().get_camera_3d()

func _ready() -> void:
    health_bar.visible = DebugManager.debug_enabled
    DebugManager.debug_toggled.connect(func(e): health_bar.visible = e)
    camera = get_viewport().get_camera_3d()

func _process(_delta: float) -> void:
    if DebugManager.debug_enabled:
        health_bar.value = health  # your health variable, added in the Mechanic Loop
        var screen_pos = camera.unproject_position(global_position + Vector3(0, 1.5, 0))
        health_bar.position = screen_pos - Vector2(health_bar.size.x / 2, 0)
```

Configure the `ProgressBar`: width 60, height 8, `min_value = 0`, `max_value = 100`.

> Register the health bar system now. It will silently do nothing until entities have a `health` variable — that comes in the Mechanic Loop.

### 7. Debug Panel

Create `graybox-prototype/scenes/debug_panel.tscn`:

- Root: `CanvasLayer` (layer 100, always on top)
- Child: `VBoxContainer` anchored top-left, margin 8px
  - `Label` id `FPS`
  - `Label` id `Entities`

```gdscript
# debug_panel.gd
extends CanvasLayer

@onready var fps_label: Label = $VBoxContainer/FPS
@onready var entity_label: Label = $VBoxContainer/Entities

func _ready() -> void:
    visible = DebugManager.debug_enabled
    DebugManager.debug_toggled.connect(func(e): visible = e)

func _process(_delta: float) -> void:
    if visible:
        fps_label.text = "FPS: %d" % Engine.get_frames_per_second()
        entity_label.text = "Entities: %d" % get_tree().get_node_count()
```

Instance `debug_panel.tscn` inside `main.tscn`, or register it as an Autoload.

### 8. Verify

Run the project (F5). Press **F1**. Confirm:
- Debug panel appears (FPS + entity count visible)
- Collision outlines appear on each entity
- Debug labels appear on each entity
- Velocity indicators appear (once entities have velocity — check after graybox-5)
- Health bars appear (once entities have health — check after graybox-5)

Press **F1** again — all overlays disappear.

## Output Artifacts

### Updated `graybox-prototype/`

- `scripts/debug_manager.gd` — Autoload singleton with toggle signal
- `scenes/debug_panel.tscn` + `scripts/debug_panel.gd` — global stats overlay
- Each entity scene updated with: `CollisionOutline`, `DebugLabel`, `VelocityIndicator`, `HealthBar` (where applicable)

## Exit Criteria

- [ ] `DebugManager` registered as Autoload
- [ ] F1 toggles debug mode globally
- [ ] Collision outlines visible per entity in debug mode
- [ ] Debug labels visible per entity in debug mode
- [ ] Velocity indicators set up per entity (activate once velocity exists in graybox-5)
- [ ] Health bars set up per entity (activate once health exists in graybox-5)
- [ ] Debug panel shows FPS and entity count in debug mode
- [ ] All debug overlays hidden when debug mode is off
- [ ] Verified with F1 toggle

## Next Stage

Proceed to **graybox-5** (Mechanic Loop) — pick `graybox-5-designed`, `graybox-5-generative`, or `graybox-5-assisted`.
