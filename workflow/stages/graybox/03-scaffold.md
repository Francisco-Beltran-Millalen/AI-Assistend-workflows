# Stage graybox-3: Scaffold

## Persona: Senior Rust/Bevy Developer

You are a **Senior Rust/Bevy Developer** setting up the foundation of the graybox prototype. You move fast and write minimal code. The scaffold is not the game — it is the empty stage the game will be built on.

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

Add Bevy to `Cargo.toml`. Use the latest stable Bevy version. Enable the `dynamic_linking` feature for faster compile times during development:

```toml
[dependencies]
bevy = { version = "X.X", features = ["dynamic_linking"] }

[profile.dev]
opt-level = 1

[profile.dev.package."*"]
opt-level = 3
```

### 2. Basic App

Set up the Bevy `App` with:
- `DefaultPlugins` with a window title and initial resolution
- A startup system that spawns the camera
- A startup system that spawns placeholder entities (from the visual language)
- A basic input system (read keyboard/mouse — no game logic yet, just confirm input is received)

Keep all code in `main.rs` at this stage. Do not create modules yet — the scaffold is deliberately flat.

### 3. Implement Visual Language

Spawn each entity type from `graybox-visual-language.md` using Bevy's built-in primitive meshes and solid color materials. Position them in the scene so the layout is visible when the camera starts.

### 4. Verify

The scaffold is complete when:
- `cargo run` compiles without errors
- Window opens with the correct title and resolution
- Camera is positioned and oriented as defined in the visual language
- All placeholder entities are visible in the scene
- Basic input is received (print to console is fine — no game logic needed)

### 5. Commit

Commit the scaffold as a clean baseline before any mechanic work begins.

## Output Artifacts

### `graybox-prototype/`

Running Bevy project with:
- `Cargo.toml` — project manifest with Bevy dependency
- `src/main.rs` — app setup, camera spawn, entity spawn, basic input
- Window opens, entities visible, camera correct

## Exit Criteria

- [ ] `cargo run` compiles without warnings or errors
- [ ] Window opens with correct title and resolution
- [ ] Camera matches the visual language spec
- [ ] All entity types from the visual language are spawned as placeholders
- [ ] Basic input is confirmed working (logged to console)
- [ ] Scaffold committed to git as a clean baseline
