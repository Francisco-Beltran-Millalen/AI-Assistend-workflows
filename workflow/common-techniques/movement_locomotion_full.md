# 🧱 1. Movement & Locomotion

## 📌 Scope

Anything related to how entities move through space.

### Includes:
- Walking, running, jumping  
- Stairs, slopes, ledges  
- Air control  
- Acceleration / deceleration  
- Root motion vs code-driven motion  

---

## ❗ Why it's its own category

Movement is not physics—it's player-facing behavior design.  
You are not simulating reality; you are designing control + feel.

---

## 🔍 Typical sub-problems

- Stair stepping  
- Slope handling  
- Momentum vs responsiveness  
- Ground detection  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

Movement systems are usually kinematic + assisted by queries.

That means:
- You decide the velocity  
- You query the world  
- You adjust the result  

---

# 🧱 PROBLEM SET

---

# 1. Ground Detection

## 🎯 Goal
Determine if the character is “grounded” and what the ground is.

---

## 🛠️ Techniques

### A. Single Raycast
```pseudo
is_grounded = raycast(origin, down, distance)
ground_normal = hit.normal
```

### B. Multi-ray / Foot Probes
```pseudo
hits = [
  raycast(left_foot),
  raycast(center),
  raycast(right_foot)
]
is_grounded = any(hits)
```

### C. Shape Cast (Capsule / Box)
```pseudo
is_grounded = shapecast(collider, down)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Single Ray | Fast, simple | Fails on edges |
| Multi-ray | More stable | More complexity |
| Shape Cast | Most accurate | Expensive |

---

## 💥 Failure Cases

- Edge of platform → ray misses → “fake falling”  
- Fast movement → ground skipped  
- Uneven terrain → jittering normals  

---

## 🔗 Composability Notes

- Combine with slope handling (uses ground normal)  
- Combine with coyote time for better feel  
- Must run before movement resolution  

---

## 🧩 2D vs 3D

- 2D: Usually 1–3 rays downward  
- 3D: Capsule or multi-ray is strongly preferred  

---

# 2. Stair Stepping

## 🎯 Goal
Allow smooth traversal over small vertical obstacles

---

## 🛠️ Techniques

### A. Step Offset (Lift + Forward)
```pseudo
if collide_forward():
    if obstacle_height < step_height:
        position.y += step_height
        move_forward()
```

---

### B. Invisible Ramp Approximation
- Replace stairs with slope collider

---

### C. Raycast Snap to Ground
```pseudo
target_y = raycast(down)
position.y = lerp(position.y, target_y, snap_speed)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Step Offset | Accurate | Complex, edge cases |
| Ramp | Stable, cheap | Not physically correct |
| Snap | Smooth | Can feel floaty |

---

## 💥 Failure Cases

- Step too high → character “blocks”  
- Rapid step sequences → jitter  
- Snap → causes foot sliding illusion  
- Offset → can clip into ceilings  

---

## 🔗 Composability Notes

- Must integrate with collision resolution  
- Strong interaction with ground detection  
- Often combined with slope logic  
- Snap + gravity can conflict (fighting forces)  

---

## 🧩 2D vs 3D

- 2D: Often unnecessary (tilemaps handle it)  
- 3D: Critical problem (stairs are everywhere)  

---

# 3. Slope Handling

## 🎯 Goal
Move smoothly across inclined surfaces

---

## 🛠️ Techniques

### A. Velocity Projection
```pseudo
velocity = project_on_plane(velocity, ground_normal)
```

---

### B. Max Slope Angle Clamp
```pseudo
if angle_between(normal, up) > max_slope:
    block_or_slide()
```

---

### C. Stick-to-Ground Force
```pseudo
velocity += ground_normal * stick_force
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Projection | Natural | Depends on stable normals |
| Angle Clamp | Simple | Hard cutoff, feels artificial |
| Stick Force | Prevents bouncing | Can feel “magnetic” |

---

## 💥 Failure Cases

- Crest of slope → character becomes airborne  
- Sharp edges → unstable normals  
- Downhill acceleration bugs  

---

## 🔗 Composability Notes

- Requires ground detection normals  
- Conflicts with jump logic if not gated  
- Works with friction / acceleration tuning  

---

## 🧩 2D vs 3D

- 2D: Usually angle-based logic  
- 3D: Requires vector projection  

---

# 4. Jumping & Gravity

## 🎯 Goal
Control vertical movement and responsiveness

---

## 🛠️ Techniques

### A. Basic Gravity
```pseudo
velocity.y -= gravity * delta
```

---

### B. Coyote Time
```pseudo
if time_since_ground < threshold:
    allow_jump()
```

---

### C. Jump Buffering
```pseudo
if jump_pressed_recently:
    queue_jump()
```

---

### D. Variable Jump Height
```pseudo
if jump_released_early:
    velocity.y *= 0.5
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Gravity | Simple | Feels stiff alone |
| Coyote | Forgiving | Less realistic |
| Buffer | Responsive | Hidden complexity |
| Variable Jump | Expressive | Needs tuning |

---

## 💥 Failure Cases

- Double jump bugs from bad state tracking  
- Jump during slope transitions  
- Gravity fighting ground snapping  

---

## 🔗 Composability Notes

- Strong interaction with ground detection  
- Must override stick-to-ground forces  
- Buffer + coyote together = best feel combo  

---

## 🧩 2D vs 3D

- Same concepts  
- 3D adds directional jump influence  

---

# 5. Air Control

## 🎯 Goal
Control movement while airborne

---

## 🛠️ Techniques

### A. Reduced Acceleration
```pseudo
velocity += input * air_control_factor
```

---

### B. Directional Influence Clamp
```pseudo
velocity = clamp_direction_change(velocity, max_angle)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Reduced Control | Predictable | Can feel stiff |
| Full Control | Responsive | Unrealistic |

---

## 💥 Failure Cases

- Mid-air direction snapping  
- Overpowered air strafing  

---

## 🔗 Composability Notes

- Uses same system as ground movement  
- Must ignore friction models  
- Interacts with jump arcs  

---

## 🧩 2D vs 3D

- 2D: Horizontal only  
- 3D: Full vector control  

---

# 6. Wall Sliding & Collision Response (Movement-side)

## 🎯 Goal
Prevent hard stops when hitting walls

---

## 🛠️ Techniques

### A. Slide Along Surface
```pseudo
velocity = project_on_plane(velocity, wall_normal)
```

---

### B. Cancel Into Wall
```pseudo
velocity = remove_component(velocity, wall_normal)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Sliding | Smooth | Can feel slippery |
| Cancel | Precise | Feels rigid |

---

## 💥 Failure Cases

- Corner trapping  
- Oscillation between surfaces  
- Loss of control in tight spaces  

---

## 🔗 Composability Notes

- Depends on collision detection normals  
- Must run after movement intent  
- Interacts with step offset logic  

---

## 🧩 2D vs 3D

- Same concept  
- 3D has more edge cases (corners, edges)  

---

# 7. Momentum vs Responsiveness

## 🎯 Goal
Balance realism vs control

---

## 🛠️ Techniques

### A. Acceleration Model
```pseudo
velocity = lerp(current_velocity, target_velocity, accel * delta)
```

---

### B. Instant Velocity (Arcade)
```pseudo
velocity = input_direction * max_speed
```

---

### C. Hybrid Model
- Instant direction change  
- Gradual speed change  

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Acceleration | Realistic | Sluggish |
| Instant | Responsive | Unrealistic |
| Hybrid | Balanced | More tuning |

---

## 💥 Failure Cases

- Input feels laggy  
- Over-snappy movement  
- Inconsistent speed on slopes  

---

## 🔗 Composability Notes

- Affects ALL movement systems  
- Interacts with:
  - slope handling  
  - air control  
  - animation  

---

## 🧩 2D vs 3D

- Same logic  
- 3D requires direction smoothing  

---

# 8. Moving Platforms

## 🎯 Goal
Keep character stable on moving surfaces

---

## 🛠️ Techniques

### A. Add Platform Velocity
```pseudo
velocity += platform.velocity
```

---

### B. Parent to Platform
```pseudo
character.parent = platform
```

---

### C. Relative Motion Tracking
```pseudo
position += platform.delta_movement
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Velocity Add | Flexible | Drift issues |
| Parenting | Simple | Breaks physics |
| Relative Motion | Accurate | Complex |

---

## 💥 Failure Cases

- Sliding off platform  
- Desync on fast platforms  
- Jump inherits wrong velocity  

---

## 🔗 Composability Notes

- Requires ground detection  
- Interacts with:
  - jumping  
  - slope handling  
- Parenting conflicts with physics systems  

---

## 🧩 2D vs 3D

- Same concept  
- 3D rotation adds complexity  

---

# 🧠 FINAL INSIGHT

Movement is not one system—it is a composition of systems:

Input → Intent → Velocity → Collision Query → Adjustment → Final Motion

Most bugs come from:
- Systems running in wrong order  
- Systems fighting each other  
- Missing state transitions  
