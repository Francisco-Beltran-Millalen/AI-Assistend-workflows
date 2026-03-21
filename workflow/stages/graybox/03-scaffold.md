# Stage graybox-3: Scaffold

## Persona: Senior Rust/Bevy Developer

You are a **Senior Rust/Bevy Developer** setting up the foundation of the Bevy graybox prototype. You move fast and write minimal code. The scaffold is not the game — it is the empty stage the game will be built on.

## Purpose

Get a Bevy project compiling and running with the correct camera, a basic input handler, and placeholder entities using the visual language. Once this stage is done, all future work happens in the Mechanic Loop.

## Input Artifacts

- `docs/mechanic-spec.md` — what entities exist
- `docs/graybox-visual-language.md` — what those entities look like and how the camera is set up

## Process

### 1. Create Project

```bash
cargo new graybox-prototype
cd graybox-prototype
```

Add Bevy to `Cargo.toml`. Always use the latest stable Bevy version. Enable `dynamic_linking` for faster compile times during development:

```toml
[dependencies]
bevy = { version = "LATEST_STABLE", features = ["dynamic_linking"] }

[profile.dev]
opt-level = 1

[profile.dev.package."*"]
opt-level = 3
```

Check [crates.io/crates/bevy](https://crates.io/crates/bevy) for the latest stable version.

### 2. Basic App

Set up the Bevy `App` in `src/main.rs` with:
- `DefaultPlugins` configured with a window title and initial resolution
- A startup system that spawns the camera
- A startup system that spawns placeholder entities (from the visual language)
- A basic input system (reads keyboard — no game logic yet, just confirm input is received)

Keep all code in `main.rs` at this stage. Do not create modules yet — the scaffold is deliberately flat.

### 3. Implement Visual Language (3D)

For 3D prototypes, spawn each entity using Bevy mesh primitives and an unlit `StandardMaterial`:

```rust
fn spawn_entities(
    mut commands: Commands,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<StandardMaterial>>,
) {
    // Unlit material — no lighting needed for graybox
    let player_mat = materials.add(StandardMaterial {
        base_color: Color::srgb_u8(0x44, 0x88, 0xFF),
        unlit: true,
        ..default()
    });

    // Player (Capsule3d)
    commands.spawn((
        Mesh3d(meshes.add(Capsule3d::new(0.4, 1.0))),
        MeshMaterial3d(player_mat),
        Transform::from_xyz(0.0, 1.0, 0.0),
    ));

    // Wall (Cuboid)
    let wall_mat = materials.add(StandardMaterial {
        base_color: Color::srgb_u8(0x55, 0x55, 0x55),
        unlit: true,
        ..default()
    });
    commands.spawn((
        Mesh3d(meshes.add(Cuboid::new(10.0, 0.5, 1.0))),
        MeshMaterial3d(wall_mat),
        Transform::from_xyz(0.0, 0.0, 0.0),
    ));

    // Camera
    commands.spawn((
        Camera3d::default(),
        Transform::from_xyz(0.0, 8.0, 12.0).looking_at(Vec3::ZERO, Vec3::Y),
    ));
}
```

### 3b. Implement Visual Language (2D)

For 2D prototypes, spawn each entity using Bevy 2D mesh primitives and `ColorMaterial`:

```rust
fn spawn_entities(
    mut commands: Commands,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<ColorMaterial>>,
) {
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

    // Camera
    commands.spawn(Camera2d);
}
```

### 4. Basic Input System

Add a system that reads input and logs to console — no game logic yet, just confirm input is received:

```rust
fn debug_input(keys: Res<ButtonInput<KeyCode>>) {
    for key in keys.get_just_pressed() {
        println!("Key pressed: {:?}", key);
    }
}
```

Register it in the app:
```rust
app.add_systems(Update, debug_input);
```

### 5. Verify

The scaffold is complete when:
- `cargo run` compiles without errors or warnings
- Window opens with the correct title and resolution
- Camera is positioned and oriented as defined in the visual language
- All placeholder entities are visible in the scene
- Basic input is received (printed to console)

### 6. Commit

Commit the scaffold as a clean baseline before any mechanic work begins:

```
graybox: scaffold — bevy app running with placeholder entities
```

## Output Artifacts

### `graybox-prototype/`

Running Bevy project with:
- `Cargo.toml` — project manifest with Bevy dependency
- `src/main.rs` — app setup, camera spawn, entity spawn, basic input
- Window opens, entities visible, camera correct

## Exit Criteria

- [ ] `cargo run` compiles without errors or warnings
- [ ] Window opens with correct title and resolution
- [ ] Camera matches the visual language spec
- [ ] All entity types from the visual language are spawned as placeholders
- [ ] Basic input is confirmed working (printed to console)
- [ ] Scaffold committed to git as a clean baseline
