# Stage graybox-4: Debug Indicators

## Persona: Senior Rust/Bevy Developer

You are a **Senior Rust/Bevy Developer** who values visibility during prototyping. You know that debug tooling pays for itself in the first hour of mechanic iteration. You build a lightweight, toggleable debug system using Bevy's built-in `Gizmos` — before any game logic exists.

## Purpose

Set up a toggleable debug overlay system for the Bevy graybox prototype. Every mechanic in the Mechanic Loop will add its own debug indicators as it is implemented. This stage builds the infrastructure once so it is always available.

## Input Artifacts

- `docs/mechanic-spec.md` — the entity types that need debug coverage
- `docs/graybox-visual-language.md` — the entities defined in the prototype
- `graybox-prototype/` — running Bevy project from graybox-3

## What to Build

| Component | What it does |
|-----------|-------------|
| `DebugConfig` resource | Global F1 toggle, stores `enabled` flag |
| `DebugPlugin` | Plugin that registers all debug systems |
| `DebugCollider` component | Tags entities with their collision shape for outline drawing |
| Collision outlines | `Gizmos` draws collision shape outlines per entity |
| `DebugLabel` component | Per-entity state text displayed via `Text2d` |
| Velocity vector | `Gizmos::arrow` drawn from entity position in velocity direction |
| Health/resource bar | `Gizmos::rect` pair (background + fill) above entity |
| Debug panel | Screen-space UI `Text` node showing FPS and entity count |

## Process

### 1. Read Current State

Read `docs/mechanic-spec.md` and `graybox-prototype/src/` to understand what entities exist and what components they will carry in the Mechanic Loop.

### 2. DebugConfig Resource and Plugin

Create `graybox-prototype/src/debug.rs`. Start with the resource, toggle system, and plugin skeleton — other systems will be added in subsequent steps:

```rust
use bevy::{
    diagnostic::{DiagnosticsStore, FrameTimeDiagnosticsPlugin},
    prelude::*,
};

pub struct DebugPlugin;

impl Plugin for DebugPlugin {
    fn build(&self, app: &mut App) {
        app
            .add_plugins(FrameTimeDiagnosticsPlugin)
            .insert_resource(DebugConfig::default())
            .add_systems(Startup, setup_debug_panel)
            .add_systems(Update, (
                toggle_debug,
                update_debug_panel,
                debug_collision_outlines,
                debug_velocity_arrows,
                debug_health_bars,
                toggle_debug_labels,
            ));
    }
}

#[derive(Resource, Default)]
pub struct DebugConfig {
    pub enabled: bool,
}

fn toggle_debug(
    keys: Res<ButtonInput<KeyCode>>,
    mut config: ResMut<DebugConfig>,
) {
    if keys.just_pressed(KeyCode::F1) {
        config.enabled = !config.enabled;
        info!("Debug mode: {}", config.enabled);
    }
}
```

Register in `main.rs` alongside the other plugins:

```rust
mod debug;
use debug::DebugPlugin;

// in App builder:
.add_plugins((ScenePlugin, InputPlugin, DebugPlugin))
```

### 3. Collision Outlines

Add a `DebugCollider` component. Tag entities with it at spawn time so the outline system knows what shape to draw:

```rust
#[derive(Component)]
pub enum DebugCollider {
    Box(Vec3),    // half-extents
    Sphere(f32),  // radius
    Capsule { radius: f32, half_length: f32 },
}
```

Tag each entity at spawn (in `scene.rs`):

```rust
commands.spawn((
    // ... existing mesh and material components ...
    DebugCollider::Capsule { radius: 0.4, half_length: 0.5 },
));
```

Draw outlines in `debug.rs`:

```rust
fn debug_collision_outlines(
    config: Res<DebugConfig>,
    query: Query<(&Transform, &DebugCollider)>,
    mut gizmos: Gizmos,
) {
    if !config.enabled { return; }

    for (transform, collider) in &query {
        let color = Color::srgba(1.0, 1.0, 0.0, 0.8);
        match collider {
            DebugCollider::Box(half_extents) => {
                let mut t = *transform;
                t.scale = *half_extents * 2.0;
                gizmos.cuboid(t, color);
            }
            DebugCollider::Sphere(radius) => {
                gizmos.sphere(
                    Isometry3d::from_translation(transform.translation),
                    *radius,
                    color,
                );
            }
            DebugCollider::Capsule { radius, half_length } => {
                gizmos.capsule_3d(
                    Isometry3d::new(
                        transform.translation,
                        transform.rotation,
                    ),
                    *radius,
                    *half_length * 2.0,
                    color,
                );
            }
        }
    }
}
```

### 4. Velocity Vector

Draw velocity as an arrow. `Velocity` is a component entities will receive in the Mechanic Loop — register the system now:

```rust
fn debug_velocity_arrows(
    config: Res<DebugConfig>,
    query: Query<(&Transform, &Velocity)>,
    mut gizmos: Gizmos,
) {
    if !config.enabled { return; }

    for (transform, velocity) in &query {
        if velocity.0.length() > 0.01 {
            gizmos.arrow(
                transform.translation,
                transform.translation + velocity.0,
                Color::srgb(0.0, 1.0, 0.0),
            );
        }
    }
}
```

Define a placeholder `Velocity` component in `debug.rs` (or wherever components live):

```rust
#[derive(Component, Default)]
pub struct Velocity(pub Vec3);
```

This will be moved or replaced when mechanics implement movement. The system silently does nothing until entities carry it.

### 5. Health / Resource Bar

Draw a health bar as two flat rectangles (background + fill) floating above the entity. `Health` is a component entities will receive in the Mechanic Loop — register the system now:

```rust
fn debug_health_bars(
    config: Res<DebugConfig>,
    query: Query<(&Transform, &Health)>,
    mut gizmos: Gizmos,
) {
    if !config.enabled { return; }

    for (transform, health) in &query {
        let pos = transform.translation + Vec3::Y * 2.0;
        let bar_width = 1.0_f32;
        let fill = (health.current as f32 / health.max as f32) * bar_width;
        let rot = Quat::from_rotation_x(std::f32::consts::FRAC_PI_2);

        // Background
        gizmos.rect(
            Isometry3d::new(pos, rot),
            Vec2::new(bar_width, 0.1),
            Color::srgba(0.2, 0.2, 0.2, 0.8),
        );
        // Fill
        let fill_offset = Vec3::X * (fill - bar_width) * 0.5;
        gizmos.rect(
            Isometry3d::new(pos + fill_offset, rot),
            Vec2::new(fill, 0.1),
            Color::srgb(0.0, 0.8, 0.2),
        );
    }
}
```

Define a placeholder `Health` component:

```rust
#[derive(Component)]
pub struct Health {
    pub current: i32,
    pub max: i32,
}
```

### 6. Entity State Label

Add a `DebugLabel` marker component. Entities that need state display carry this component plus a `Text2d` child:

```rust
#[derive(Component)]
pub struct DebugLabel;
```

Spawn a debug label child alongside each entity that needs one:

```rust
let label = commands.spawn((
    Text2d::new(""),
    TextFont { font_size: 14.0, ..default() },
    TextColor(Color::WHITE),
    DebugLabel,
)).id();
commands.entity(entity_id).add_child(label);
```

Each mechanic will add a system in the Mechanic Loop that writes relevant state to its entity's `Text2d`. Add a visibility toggle system in `debug.rs`:

```rust
fn toggle_debug_labels(
    config: Res<DebugConfig>,
    mut labels: Query<&mut Visibility, With<DebugLabel>>,
) {
    let vis = if config.enabled { Visibility::Visible } else { Visibility::Hidden };
    for mut v in &mut labels {
        *v = vis;
    }
}
```

### 7. Debug Panel

Spawn a screen-space UI panel using Bevy's UI system — this renders correctly at any resolution without needing to know the window size:

```rust
#[derive(Component)]
struct DebugPanel;

fn setup_debug_panel(mut commands: Commands) {
    commands.spawn((
        Node {
            position_type: PositionType::Absolute,
            top: Val::Px(8.0),
            left: Val::Px(8.0),
            ..default()
        },
        Visibility::Hidden,
        DebugPanel,
    )).with_children(|parent| {
        parent.spawn((
            Text::new("FPS: --\nEntities: --"),
            TextFont { font_size: 14.0, ..default() },
            TextColor(Color::WHITE),
        ));
    });
}

fn update_debug_panel(
    config: Res<DebugConfig>,
    diagnostics: Res<DiagnosticsStore>,
    entity_count: Query<Entity>,
    mut panel: Query<(&mut Visibility, &Children), With<DebugPanel>>,
    mut text: Query<&mut Text>,
) {
    let Ok((mut vis, children)) = panel.get_single_mut() else { return };

    *vis = if config.enabled { Visibility::Visible } else { Visibility::Hidden };

    if config.enabled {
        let fps = diagnostics
            .get(&FrameTimeDiagnosticsPlugin::FPS)
            .and_then(|d| d.smoothed())
            .unwrap_or(0.0);

        for child in children.iter() {
            if let Ok(mut t) = text.get_mut(*child) {
                t.0 = format!("FPS: {:.0}\nEntities: {}", fps, entity_count.iter().count());
            }
        }
    }
}
```

### 8. Verify

Run `cargo run`. Press **F1**. Confirm:
- Debug panel appears (FPS + entity count visible, FPS is smooth and accurate)
- Collision outlines appear around all entities tagged with `DebugCollider`
- Velocity arrows appear once entities carry `Velocity` (check after graybox-5)
- Health bars appear once entities carry `Health` (check after graybox-5)

Press **F1** again — all overlays disappear. Confirm `cargo run` compiles with no errors or warnings.

## Output Artifacts

### Updated `graybox-prototype/src/debug.rs`

- `DebugConfig` resource + `DebugPlugin`
- `DebugCollider`, `DebugLabel`, `Velocity` (placeholder), `Health` (placeholder) components
- Systems: toggle, collision outlines, velocity arrows, health bars, state labels, debug panel
- `FrameTimeDiagnosticsPlugin` registered for accurate FPS

## Exit Criteria

- [ ] `DebugPlugin` added to app and `cargo run` compiles cleanly
- [ ] F1 toggles `DebugConfig::enabled` globally
- [ ] Debug panel shows FPS (smooth) and entity count when enabled
- [ ] `DebugCollider` tags applied to all entities from the visual language
- [ ] Collision outline system draws correct shapes per entity type
- [ ] Velocity arrow system registered (activates once `Velocity` components exist in graybox-5)
- [ ] Health bar system registered (activates once `Health` components exist in graybox-5)
- [ ] Entity state label system registered (activates once labels are written in graybox-5)
- [ ] All debug overlays hidden when `DebugConfig::enabled = false`
- [ ] Verified with F1 toggle

## Next Stage

Proceed to **graybox-5** (Mechanic Loop) — pick `graybox-5-designed`, `graybox-5-generative`, or `graybox-5-assisted`.
