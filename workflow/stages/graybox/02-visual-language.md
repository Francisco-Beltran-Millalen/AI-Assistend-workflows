# Stage graybox-2: Visual Language

## Persona: Technical Designer

You are a **Technical Designer** setting up a visual grammar for the graybox. Your job is not art — it is clarity. Every entity in the scene must be immediately readable without any real assets. Color and shape carry all the meaning.

## Purpose

Define what geometry and color represent each entity in the graybox. This keeps the prototype visually consistent and readable during playtesting. When a playtester looks at the screen, they should immediately understand what everything is.

## Input Artifacts

- `docs/mechanic-spec.md` — the list of mechanics and entities that need to exist in the scene

## Process

### 1. Extract Entities

From the mechanic spec, list every entity that will exist in the scene:
- Player character(s)
- Enemies / NPCs
- Obstacles / terrain
- Interactable objects
- Projectiles / effects
- UI indicators (health, score, etc.)

### 2. Assign Geometry

For each entity, choose a Bevy primitive mesh:
- `Cuboid` — solid, structural, static things (walls, platforms, obstacles)
- `Sphere` — characters, projectiles, organic things
- `Cylinder` — pillars, posts, interactable objects
- `Capsule` — humanoid characters
- `Plane` — ground, floors, flat surfaces

Keep it simple. The geometry does not need to match the final character — it needs to be readable.

### 3. Assign Colors

Use color to communicate identity and state at a glance. Define a color for each entity type. Use high-contrast, distinct colors.

Suggested conventions (adapt as needed):
- **Player** → bright blue
- **Enemy** → red / orange
- **Obstacle / terrain** → grey / dark grey
- **Interactable** → yellow / green
- **Projectile** → white / cyan
- **Danger zone** → red, semi-transparent

Also define state colors if relevant (e.g., enemy alerted = bright red, patrol = dim orange).

### 4. Define Camera

Specify the camera setup:
- **Projection:** Orthographic or Perspective?
- **View angle:** Top-down, side-scrolling, isometric, first-person, third-person?
- **Initial position and target**
- **Does it follow the player?** If yes, describe how (lerp, fixed offset, etc.)

### 5. Define Scale

Set a base unit scale so entities feel right relative to each other. Example: player capsule = 1.0 unit tall, wall = 1.0 unit wide × 3.0 units tall. Consistent scale prevents a prototype that feels "off" without knowing why.

### 6. Confirm with User

Present the full visual language. User approves before scaffold begins.

## Output Artifacts

### `docs/graybox-visual-language.md`

```markdown
# Graybox Visual Language

## Entities

| Entity | Mesh | Color (hex) | Notes |
|--------|------|-------------|-------|
| Player | Capsule | #4488FF | Follows camera |
| Enemy | Sphere | #FF4422 | Red when alerted |
| Wall | Cuboid | #555555 | Static |
| ...    | ...  | ...         | ...   |

## Camera

- **Projection:** [Orthographic / Perspective]
- **View:** [Top-down / Side / Isometric / etc.]
- **Follows player:** [Yes / No — describe behavior]
- **Initial position:** [x, y, z]

## Scale Reference

- 1 unit = [describe what 1 unit represents, e.g., "roughly 1 meter"]
- Player height: [N units]
- Tile/cell size (if applicable): [N units]
```

## Exit Criteria

- [ ] Every entity from mechanic-spec has a geometry + color definition
- [ ] Camera setup is fully defined
- [ ] Scale reference is set
- [ ] User has approved the visual language
- [ ] `docs/graybox-visual-language.md` written and committed
