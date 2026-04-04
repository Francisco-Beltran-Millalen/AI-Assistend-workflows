# 🧲 2. Collision Detection & Queries

## 📌 Scope

Detecting if/when things touch or overlap

### Includes:
- Raycasts, shapecasts  
- Overlaps  
- Hit detection  
- Line of sight  

---

## ❗ Why separate from physics

This is about querying the world, not resolving it.

You are asking:
“What is there?”
NOT:
“What should happen?”

---

## 🔍 Typical sub-problems

- Ground checks  
- Wall detection  
- Hitboxes vs hurtboxes  
- Visibility checks  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

Detection should be stateless, deterministic, and query-based

That means:
- No side effects  
- Same input → same result  
- Independent from movement logic  

---

# 🧱 PROBLEM SET

---

# 1. Raycasting (Line Queries)

## 🎯 Goal
Detect intersections along a line

---

## 🛠️ Techniques

### A. Single Raycast
```pseudo
hit = raycast(origin, direction, max_distance)
if hit:
    point = hit.position
    normal = hit.normal
```

---

### B. Multi-ray Sampling
```pseudo
hits = []
for dir in directions:
    hits.append(raycast(origin, dir))

result = aggregate(hits)
```

---

### C. Layer / Mask Filtering
```pseudo
hit = raycast(origin, dir, mask=GROUND_LAYER)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Single Ray | Fast, simple | Limited coverage |
| Multi-ray | More robust | More expensive |
| Layer Mask | Precise filtering | Requires setup discipline |

---

## 💥 Failure Cases

- Thin objects missed (tunneling-like effect)  
- Starting inside collider → no hit  
- Precision errors at long distances  
- Missing fast-moving targets  

---

## 🔗 Composability Notes

- Used by:
  - ground detection  
  - line of sight  
  - aiming systems  
- Often combined with shape casts for robustness  
- Must be consistent with collision layers used in physics  

---

## 🧩 2D vs 3D

- 2D: simpler, fewer rays needed  
- 3D: often requires multiple rays or spread  

---

# 2. Shape Casting (Swept Volumes)

## 🎯 Goal
Detect collisions over a volume along a path

---

## 🛠️ Techniques

### A. Capsule Cast
```pseudo
hit = shapecast(capsule, direction, distance)
```

---

### B. Box Cast
```pseudo
hit = shapecast(box, direction, distance)
```

---

### C. Continuous Sweep
```pseudo
hit = sweep_shape(shape, from, to)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Capsule | Good for characters | Limited shapes |
| Box | Predictable | Can snag on edges |
| Sweep | Accurate | Expensive |

---

## 💥 Failure Cases

- Starting inside geometry → undefined results  
- Edge grazing → unstable normals  
- Performance spikes with many casts  

---

## 🔗 Composability Notes

- Often replaces multiple raycasts  
- Works closely with movement prediction  
- Required for:
  - robust grounding  
  - ledge detection  

---

## 🧩 2D vs 3D

- 2D: box/circle casts  
- 3D: capsule is dominant  

---

# 3. Overlap Queries (Volume Checks)

## 🎯 Goal
Detect what is inside a region

---

## 🛠️ Techniques

### A. Sphere / Circle Overlap
```pseudo
colliders = overlap_sphere(center, radius)
```

---

### B. Box Overlap
```pseudo
colliders = overlap_box(center, size)
```

---

### C. Trigger Volumes
```pseudo
on_enter(collider):
    handle_event()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Sphere | Cheap | Imprecise |
| Box | Flexible | Orientation issues |
| Triggers | Event-driven | Less control |

---

## 💥 Failure Cases

- Missing fast objects between frames  
- Multiple triggers firing unexpectedly  
- Large volumes causing performance issues  

---

## 🔗 Composability Notes

- Used for:
  - area detection  
  - combat hitboxes  
  - pickups  
- Often combined with state machines  

---

## 🧩 2D vs 3D

- Same concept  
- 3D requires rotation handling  

---

# 4. Hit Detection (Combat / Interaction)

## 🎯 Goal
Determine if an attack or interaction hits a target

---

## 🛠️ Techniques

### A. Hitbox vs Hurtbox
```pseudo
if overlap(hitbox, hurtbox):
    apply_damage()
```

---

### B. Frame-based Activation
```pseudo
if animation_frame in active_frames:
    enable_hitbox()
```

---

### C. Swept Hit Detection
```pseudo
hit = sweep(hitbox, previous_pos, current_pos)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Overlap | Simple | Can miss fast hits |
| Frame-based | Precise timing | Animation dependent |
| Sweep | Accurate | Expensive |

---

## 💥 Failure Cases

- Missed hits due to low framerate  
- Double hits in one frame  
- Desync with animation  

---

## 🔗 Composability Notes

- Requires:
  - overlap queries  
  - animation system  
- Interacts with:
  - networking  
  - state machines  

---

## 🧩 2D vs 3D

- Same logic  
- 3D adds directional complexity  

---

# 5. Line of Sight (Visibility)

## 🎯 Goal
Determine if one entity can “see” another

---

## 🛠️ Techniques

### A. Direct Raycast
```pseudo
hit = raycast(eye, target)
visible = (hit == target)
```

---

### B. Multi-point Visibility
```pseudo
points = target.get_visibility_points()
visible = any(raycast(eye, p) for p in points)
```

---

### C. Cone Check + Raycast
```pseudo
if angle_to_target < fov:
    visible = raycast_clear()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Single Ray | Fast | Easily blocked |
| Multi-point | Robust | Expensive |
| Cone + Ray | Realistic | More logic |

---

## 💥 Failure Cases

- Partial occlusion issues  
- Thin obstacles not detected  
- Flickering visibility  

---

## 🔗 Composability Notes

- Combines:
  - raycasting  
  - angle checks  
- Used by:
  - AI systems  
  - stealth mechanics  

---

## 🧩 2D vs 3D

- 2D: simpler geometry  
- 3D: occlusion is more complex  

---

# 6. Spatial Filtering & Layers

## 🎯 Goal
Limit what queries can detect

---

## 🛠️ Techniques

### A. Collision Layers
```pseudo
raycast(mask=ENEMY_LAYER)
```

---

### B. Tag Filtering
```pseudo
if collider.tag == "enemy":
```

---

### C. Query Groups
```pseudo
overlap(group="interactable")
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Layers | Fast, engine-level | Limited slots |
| Tags | Flexible | String-based errors |
| Groups | Organized | Requires discipline |

---

## 💥 Failure Cases

- Incorrect filtering → missing hits  
- Overlapping layers → unintended interactions  
- Hard-to-debug filtering logic  

---

## 🔗 Composability Notes

- Critical for ALL queries  
- Must align with:
  - physics system  
  - gameplay logic  

---

## 🧩 2D vs 3D

- Same system  

---

# 🧠 FINAL INSIGHT

Collision detection is not one tool—it is a toolkit of queries:

Raycast → ShapeCast → Overlap → Filter → Interpret

Most bugs come from:
- Wrong query type used  
- Missing edge cases (thin objects, fast movement)  
- Inconsistent filtering  
- Mixing detection with resolution  
