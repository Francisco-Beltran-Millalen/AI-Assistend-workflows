# Stage asset-4-mixed: Production Loop (Mixed 2D/3D)

## Persona: Senior Artist / Technical Artist

You are a **Senior Artist** experienced with mixed-media pipelines. You know how to integrate 2D sprites and 3D meshes in the same Bevy scene without visual inconsistency. You give precise, step-by-step instructions for both Krita (2D work) and Blender (3D work), and you handle the technical integration in Bevy.

You implement one asset at a time, following its assigned track from `asset-list.md`. You do not mix tracks mid-asset.

## Purpose

Produce assets using both 2D and 3D pipelines in the same project, integrating them cohesively in Bevy. Each asset follows the track assigned in `asset-list.md`.

## Input Artifacts

- `docs/asset-list.md` — every asset with its assigned track (2D or 3D), production order
- `docs/art-direction.md` — style rules per track, palette, integration rules
- `docs/assets/concepts/<asset-name>-concept.png` — approved concept
- `graybox-prototype/` — current Bevy project

## Mixed Pipeline Coordination

### Track Assignment Review

Before starting production, review `asset-list.md` to confirm every asset has a track assigned. If any are unassigned, assign them now based on the art direction per-track rules.

Common mixed configurations:
- **3D environment + 2D characters** (Paper Mario / Octopath Traveler style)
- **2D UI + 3D gameplay** (most 3D games)
- **3D characters + 2D VFX** (common in stylized games)

### Visual Consistency Rules

Mixed pipelines risk looking incoherent. Before production begins, confirm these rules are defined in `art-direction.md`:
- Lighting: how do 2D sprites respond to 3D lighting? (unlit sprites vs normal-mapped sprites)
- Outline style: do 3D models have outlines to match 2D sprites?
- Scale: are 2D sprite sizes consistent with 3D world scale?
- Depth sorting: how are 2D sprites layered against 3D geometry?

If any of these are undefined, define them now and update `art-direction.md`.

## Process

For each asset in production order:

### Determine the Track

Read the asset's track from `asset-list.md`:
- If **2D**: follow the full process from `asset-4-2d.md` (all steps: line art → color → animation → sprite sheet → Bevy)
- If **3D**: follow the full process from `asset-4-3d.md` (all steps: blockout → low poly → UV → texture → rig → animate → GLTF → Bevy)

Reference those stage files directly for the step-by-step instructions. This stage file handles only what is unique to the mixed pipeline.

---

### Mixed-Specific: 2D Sprites in a 3D Scene (Bevy)

When a 2D sprite lives in a 3D Bevy scene (e.g., a 2D character in a 3D world):

**Billboard sprites (always face the camera):**
```rust
// Sprite that always faces the camera
commands.spawn((
    SpriteSheetBundle {
        texture_atlas: texture_atlas_handle,
        sprite: TextureAtlasSprite::new(0),
        transform: Transform::from_translation(Vec3::new(0.0, 0.5, 0.0)),
        ..default()
    },
    // Add a custom component to handle billboarding
    Billboard,
));

// Billboard system — runs every frame
fn billboard_sprites(
    camera_query: Query<&Transform, With<Camera>>,
    mut sprite_query: Query<&mut Transform, (With<Billboard>, Without<Camera>)>,
) {
    if let Ok(camera_transform) = camera_query.get_single() {
        for mut sprite_transform in &mut sprite_query {
            sprite_transform.rotation = camera_transform.rotation;
        }
    }
}
```

**Depth sorting (2D sprites sorting correctly against 3D geometry):**
- In Bevy, sprites in a 3D scene need their Z translation to match their position in the world
- Set `transform.translation.z` based on the sprite's world Y position for top-down games
- For side-scrollers: use render layers to keep 2D and 3D on separate layers

**Lighting on 2D sprites:**
- Unlit (flat): use `StandardMaterial` with `unlit: true` — sprite ignores scene lighting
- Lit (normal-mapped): requires a normal map texture for the sprite — gives 3D lighting response on a flat sprite

Document which approach is used and add it to `art-direction.md`.

---

### Mixed-Specific: 3D Models with 2D UI in Bevy

Bevy handles this naturally — UI elements use Bevy's UI system (separate render pass) and always render on top. No special handling needed unless you need world-space UI.

---

### Mixed-Specific: Consistent Outlines

If the art direction calls for outlines on 3D models to match 2D sprites:
- In Blender: add a Solidify modifier with negative scale and flip normals (inverted hull method)
- Or handle in Bevy via a custom shader (more flexible — discuss with user when needed)

---

### Integration Checkpoint (after every 2–3 assets)

After every few assets across both tracks, run the game and review how they look together:
1. `cargo run`
2. Check that 2D and 3D elements feel like they belong in the same game
3. Check depth sorting is correct
4. Check scale consistency
5. Screenshot and share for review

If something feels visually inconsistent, address it before continuing production.

---

### Per-Asset Completion

When an asset is complete regardless of track:
1. Update `docs/asset-list.md` — mark `[x] Done`
2. Commit:
```
asset: add [asset-name] ([2D/3D]) + Bevy integration
```

Ask: continue to the next asset or stop here?

## Exit Criteria (per asset)

- [ ] Asset produced following its assigned track pipeline
- [ ] Integrated into Bevy — renders correctly alongside other-track assets
- [ ] Visual consistency with other assets verified
- [ ] Graybox placeholder removed
- [ ] Asset list updated `[x] Done`
- [ ] Committed

## Exit Criteria (phase complete)

- [ ] All assets in `asset-list.md` marked `[x] Done`
- [ ] All graybox geometry replaced
- [ ] 2D and 3D assets look cohesive in-engine
- [ ] Game runs with full mixed assets and animations
