# Stage graybox-3: Scaffold

## Persona: Senior Rust/Bevy Developer

You are a **Senior Rust/Bevy Developer** setting up the foundation of the Bevy graybox prototype. You move fast and write minimal code. The scaffold is not the game — it is the empty stage the game will be built on.

## Purpose

Get a Bevy project compiling and running with the correct camera, placeholder entities from the visual language, and a basic input handler. Structure the project with Bevy's Plugin pattern from the start so every future mechanic has a clean home. Once this stage is done, all future work happens in the Mechanic Loop.

## Input Artifacts

- `docs/mechanic-spec.md` — what entities exist
- `docs/graybox-visual-language.md` — what those entities look like and how the camera is set up

## Process

### 1. Create Project

```bash
cargo new graybox-prototype
cd graybox-prototype
```

### 2. Configure Cargo.toml

Use Bevy 0.18. Enable `dynamic_linking` for faster compile times during development:

```toml
[dependencies]
bevy = { version = "0.18", features = ["dynamic_linking"] }

[profile.dev]
opt-level = 1

[profile.dev.package."*"]
opt-level = 3
```

### 3. Project Structure

Use Bevy's **Plugin pattern** from day one. Each file owns one concern and registers its own systems:

```
graybox-prototype/
└── src/
    ├── main.rs      ← App setup only: add_plugins, window config
    ├── scene.rs     ← ScenePlugin: spawn_camera + spawn_entities
    └── input.rs     ← InputPlugin: debug_input system
```

`debug.rs` will be added in graybox-4.

### 4. main.rs — App Setup

`main.rs` contains only the `App` builder. No systems, no logic:

```rust
mod scene;
mod input;

use bevy::prelude::*;
use scene::ScenePlugin;
use input::InputPlugin;

fn main() {
    App::new()
        .add_plugins(DefaultPlugins.set(WindowPlugin {
            primary_window: Some(Window {
                title: "[Game Title] — Graybox".into(),
                resolution: (1280.0, 720.0).into(),
                ..default()
            }),
            ..default()
        }))
        .add_plugins((ScenePlugin, InputPlugin))
        .run();
}
```

### 5. scene.rs — Camera and Entities

`ScenePlugin` owns the startup system that spawns the camera and all placeholder entities from the visual language.

**For 3D prototypes:**

```rust
use bevy::prelude::*;

pub struct ScenePlugin;

impl Plugin for ScenePlugin {
    fn build(&self, app: &mut App) {
        app.add_systems(Startup, spawn_scene);
    }
}

fn spawn_scene(
    mut commands: Commands,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<StandardMaterial>>,
) {
    // Camera
    commands.spawn((
        Camera3d::default(),
        Transform::from_xyz(0.0, 8.0, 12.0).looking_at(Vec3::ZERO, Vec3::Y),
    ));

    // Player (Capsule3d) — unlit material, no lighting needed for graybox
    commands.spawn((
        Mesh3d(meshes.add(Capsule3d::new(0.4, 1.0))),
        MeshMaterial3d(materials.add(StandardMaterial {
            base_color: Color::srgb_u8(0x44, 0x88, 0xFF),
            unlit: true,
            ..default()
        })),
        Transform::from_xyz(0.0, 1.0, 0.0),
    ));

    // Wall (Cuboid)
    commands.spawn((
        Mesh3d(meshes.add(Cuboid::new(10.0, 0.5, 1.0))),
        MeshMaterial3d(materials.add(StandardMaterial {
            base_color: Color::srgb_u8(0x55, 0x55, 0x55),
            unlit: true,
            ..default()
        })),
        Transform::from_xyz(0.0, 0.0, 0.0),
    ));

    // Spawn all other entities from graybox-visual-language.md here
}
```

**For 2D prototypes:**

```rust
fn spawn_scene(
    mut commands: Commands,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<ColorMaterial>>,
) {
    // Camera
    commands.spawn(Camera2d);

    // Player (Capsule2d)
    commands.spawn((
        Mesh2d(meshes.add(Capsule2d::new(16.0, 32.0))),
        MeshMaterial2d(materials.add(Color::srgb_u8(0x44, 0x88, 0xFF))),
        Transform::from_xyz(0.0, 0.0, 0.0),
    ));

    // Platform (Rectangle)
    commands.spawn((
        Mesh2d(meshes.add(Rectangle::new(200.0, 20.0))),
        MeshMaterial2d(materials.add(Color::srgb_u8(0x55, 0x55, 0x55))),
        Transform::from_xyz(0.0, -100.0, 0.0),
    ));

    // Spawn all other entities from graybox-visual-language.md here
}
```

Spawn every entity type from `graybox-visual-language.md`. Use the exact mesh, color, and position defined there.

### 6. input.rs — Basic Input

`InputPlugin` owns a system that reads keyboard input and prints to the console — no game logic, just confirm input is wired up:

```rust
use bevy::prelude::*;

pub struct InputPlugin;

impl Plugin for InputPlugin {
    fn build(&self, app: &mut App) {
        app.add_systems(Update, debug_input);
    }
}

fn debug_input(keys: Res<ButtonInput<KeyCode>>) {
    for key in keys.get_just_pressed() {
        println!("Key pressed: {:?}", key);
    }
}
```

### 7. Verify

The scaffold is complete when:
- `cargo run` compiles without errors or warnings
- Window opens with the correct title and resolution
- Camera is positioned and oriented as defined in the visual language
- All placeholder entities are visible in the scene
- Key presses print to the console

### 8. Commit

Commit the scaffold as a clean baseline before any mechanic work begins:

```
graybox: scaffold — bevy app running with placeholder entities
```

## Output Artifacts

### `graybox-prototype/`

Running Bevy 0.18 project with:
- `Cargo.toml` — Bevy 0.18 dependency, dev profile
- `src/main.rs` — App setup + plugin registration
- `src/scene.rs` — ScenePlugin: camera + placeholder entities
- `src/input.rs` — InputPlugin: basic input logging
- Window opens, entities visible, camera correct

## Exit Criteria

- [ ] `cargo run` compiles without errors or warnings
- [ ] Window opens with correct title and resolution
- [ ] Camera matches the visual language spec
- [ ] All entity types from the visual language are spawned as placeholders
- [ ] Basic input is confirmed working (printed to console)
- [ ] Scaffold committed to git as a clean baseline
