# 🎥 9. Camera Systems

## 📌 Scope

How the player sees and perceives the world

### Includes:
- Follow cameras  
- Smoothing and damping  
- Camera collision  
- Framing and composition  

---

## 🔍 Typical sub-problems

- Camera clipping through walls  
- Motion sickness  
- Bad framing / losing the player  
- Camera lag or jitter  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

The camera is not passive—it is an active gameplay system

That means:
- It must prioritize clarity over realism  
- It should anticipate player movement  
- It must never fight player control  

---

# 🧱 PROBLEM SET

---

# 1. Follow Camera

## 🎯 Goal
Keep the player in view consistently

---

## 🛠️ Techniques

### A. Direct Follow
```pseudo
camera.position = target.position
```

---

### B. Offset Follow
```pseudo
camera.position = target.position + offset
```

---

### C. Spring Follow
```pseudo
velocity += (target.position - camera.position) * stiffness
camera.position += velocity * delta
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Direct | Precise | Jittery |
| Offset | Stable | Static feel |
| Spring | Smooth | Can overshoot |

---

## 💥 Failure Cases

- Camera jitter  
- Overshooting target  
- Losing player during fast motion  

---

## 🔗 Composability Notes

- Base system for all camera behavior  
- Works with:
  - smoothing  
  - collision  
- Needs coordination with:
  - movement system  

---

## 🧩 2D vs 3D

- 2D: simpler tracking  
- 3D: requires rotation and distance control  

---

# 2. Camera Smoothing & Damping

## 🎯 Goal
Reduce jitter and create smooth motion

---

## 🛠️ Techniques

### A. Linear Interpolation
```pseudo
camera.position = lerp(camera.position, target, smooth_factor)
```

---

### B. Exponential Smoothing
```pseudo
camera.position += (target - camera.position) * (1 - exp(-k * delta))
```

---

### C. Critically Damped Spring
```pseudo
apply_spring_damper(camera, target)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Lerp | Simple | Frame-rate dependent |
| Exponential | Stable | Less intuitive |
| Spring | Natural | Needs tuning |

---

## 💥 Failure Cases

- Camera lag  
- Oversmoothing  
- Input feels delayed  

---

## 🔗 Composability Notes

- Must balance:
  - responsiveness  
  - smoothness  
- Interacts with:
  - input feel  
  - game speed  

---

## 🧩 2D vs 3D

- Same principle  

---

# 3. Camera Collision

## 🎯 Goal
Prevent camera from clipping through geometry

---

## 🛠️ Techniques

### A. Raycast Clamp
```pseudo
hit = raycast(target, camera_position)
if hit:
    camera.position = hit.point
```

---

### B. Sphere Cast
```pseudo
hit = shapecast(sphere, target, camera_position)
```

---

### C. Camera Push Forward
```pseudo
if obstacle_detected:
    move_camera_closer()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Raycast | Simple | Can clip edges |
| Sphere Cast | Robust | More expensive |
| Push | Smooth | May distort framing |

---

## 💥 Failure Cases

- Camera pops  
- Sudden zoom changes  
- Losing intended framing  

---

## 🔗 Composability Notes

- Must integrate with:
  - follow system  
- Needs:
  - collision layers  
- Must not break:
  - player visibility  

---

## 🧩 2D vs 3D

- Mostly a 3D problem  

---

# 4. Camera Framing & Composition

## 🎯 Goal
Keep important elements visible and readable

---

## 🛠️ Techniques

### A. Dead Zone
```pseudo
if target outside zone:
    move_camera()
```

---

### B. Look-ahead Framing
```pseudo
camera.offset = velocity * factor
```

---

### C. Multi-target Framing
```pseudo
center = average(targets)
camera.position = center
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Dead Zone | Stable | Less reactive |
| Look-ahead | Predictive | Can overshoot |
| Multi-target | Good for multiplayer | Hard to tune |

---

## 💥 Failure Cases

- Player near screen edge  
- Camera oscillation  
- Important objects off-screen  

---

## 🔗 Composability Notes

- Works with:
  - navigation  
  - combat systems  
- Must adapt to:
  - gameplay context  

---

## 🧩 2D vs 3D

- 2D: common technique  
- 3D: harder due to perspective  

---

# 5. Camera Modes & Context Switching

## 🎯 Goal
Adapt camera behavior to different situations

---

## 🛠️ Techniques

### A. Mode Switching
```pseudo
if in_combat:
    camera_mode = COMBAT
```

---

### B. Blend Between Modes
```pseudo
camera = blend(mode_a, mode_b, t)
```

---

### C. State-driven Camera
```pseudo
camera.update(state)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Switching | Clear behavior | Abrupt changes |
| Blending | Smooth | Needs tuning |
| State-driven | Flexible | Complex |

---

## 💥 Failure Cases

- Abrupt transitions  
- Conflicting camera logic  
- Player disorientation  

---

## 🔗 Composability Notes

- Driven by:
  - gameplay state  
- Must sync with:
  - animation  
  - input  
- Needs priority system  

---

## 🧩 2D vs 3D

- Same concept  

---

# 6. Camera Rotation & Control

## 🎯 Goal
Control how the camera rotates around the player

---

## 🛠️ Techniques

### A. Fixed Angle
```pseudo
camera.rotation = fixed_value
```

---

### B. Player-controlled Camera
```pseudo
camera.rotation += input * sensitivity
```

---

### C. Auto-alignment
```pseudo
camera.rotation = lerp(camera.rotation, target_direction)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Fixed | Stable | Limited control |
| Player-controlled | Freedom | Harder to manage |
| Auto-align | Guided | Can fight player |

---

## 💥 Failure Cases

- Camera fighting player input  
- Sudden rotation snaps  
- Disorientation  

---

## 🔗 Composability Notes

- Must integrate with:
  - input system  
- Interacts with:
  - movement direction  
- Needs smoothing  

---

## 🧩 2D vs 3D

- Mostly 3D  
- Rare in 2D  

---

# 7. Camera Jitter & Stability Fixes

## 🎯 Goal
Eliminate visual instability

---

## 🛠️ Techniques

### A. Fixed Update Sync
```pseudo
update_camera_after_physics()
```

---

### B. Position Interpolation
```pseudo
camera.position = interpolate(previous, current)
```

---

### C. Velocity Compensation
```pseudo
camera += target.velocity * delta
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Fixed Sync | Stable | Less flexible |
| Interpolation | Smooth | Adds delay |
| Compensation | Predictive | Can overshoot |

---

## 💥 Failure Cases

- Micro jitter  
- Camera lag  
- Desync with movement  

---

## 🔗 Composability Notes

- Must align with:
  - physics timestep  
  - rendering update  
- Critical for:
  - fast-paced games  

---

## 🧩 2D vs 3D

- Same issue  

---

# 🧠 FINAL INSIGHT

The camera is a perception pipeline:

Target → Framing → Smoothing → Collision → Final View

Most bugs come from:
- Camera reacting too late or too aggressively  
- Systems fighting each other (input vs auto-align)  
- Poor prioritization of player visibility  
- Treating camera as passive instead of active  
