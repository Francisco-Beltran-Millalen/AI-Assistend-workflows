# ⚖️ 3. Collision Resolution & Physics Response

## 📌 Scope

What happens AFTER a collision is detected

### Includes:
- Sliding along walls  
- Bounce, friction  
- Penetration correction  
- Rigidbody physics  

---

## ❗ Key distinction

- Detection = “did we hit?”  
- Resolution = “what do we do about it?”  

---

## 🔍 Typical sub-problems

- Jittering  
- Sticking to walls  
- Tunneling fixes (CCD)  
- Stable stacking  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

Resolution is about producing stable, believable motion under constraints

That means:
- No interpenetration (or minimal)  
- Stable over time (no jitter/explosions)  
- Predictable and controllable  

---

# 🧱 PROBLEM SET

---

# 1. Penetration Resolution (Depenetration)

## 🎯 Goal
Resolve overlapping objects by pushing them apart

---

## 🛠️ Techniques

### A. Minimum Translation Vector (MTV)
```pseudo
mtv = compute_penetration_vector(a, b)
position += mtv
```

---

### B. Iterative Depenetration
```pseudo
for i in range(iterations):
    if overlapping:
        position += compute_mtv()
```

---

### C. Position Projection
```pseudo
position = project_out_of_collision(position)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| MTV | Direct, fast | Can cause jitter |
| Iterative | More stable | More expensive |
| Projection | Clean result | Requires robust math |

---

## 💥 Failure Cases

- Oscillation between surfaces  
- Deep penetration → large correction → “teleport”  
- Stacked objects exploding  

---

## 🔗 Composability Notes

- Must run before velocity resolution  
- Works with:
  - sliding  
  - stacking  
- Too aggressive correction breaks movement feel  

---

## 🧩 2D vs 3D

- Same concept  
- 3D introduces more axes → more instability  

---

# 2. Sliding Response

## 🎯 Goal
Allow movement along surfaces instead of stopping

---

## 🛠️ Techniques

### A. Velocity Projection
```pseudo
velocity = project_on_plane(velocity, collision_normal)
```

---

### B. Remove Normal Component
```pseudo
velocity -= dot(velocity, normal) * normal
```

---

### C. Sequential Collision Resolution
```pseudo
for collision in collisions:
    velocity = adjust_velocity(velocity, collision.normal)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Projection | Smooth | Needs stable normals |
| Remove Component | Precise | Can feel rigid |
| Sequential | Handles multiple hits | Order-dependent bugs |

---

## 💥 Failure Cases

- Corner trapping (multiple normals)  
- Infinite sliding loops  
- Loss of speed  

---

## 🔗 Composability Notes

- Depends on detection normals  
- Must follow depenetration  
- Interacts with:
  - slope handling  
  - step offset  

---

## 🧩 2D vs 3D

- Same principle  
- 3D has more multi-surface cases  

---

# 3. Bounce & Restitution

## 🎯 Goal
Simulate bouncing behavior after collision

---

## 🛠️ Techniques

### A. Reflection Vector
```pseudo
velocity = reflect(velocity, normal) * restitution
```

---

### B. Restitution Coefficient
```pseudo
velocity *= bounce_factor
```

---

### C. Conditional Bounce
```pseudo
if impact_speed > threshold:
    apply_bounce()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Reflection | Realistic | Needs correct normals |
| Restitution | Simple | Less accurate |
| Conditional | Controlled | Less physical |

---

## 💥 Failure Cases

- Infinite bouncing  
- Energy gain due to numeric error  
- Micro-bounces on flat surfaces  

---

## 🔗 Composability Notes

- Interacts with:
  - friction  
  - velocity clamping  
- Often disabled for character controllers  

---

## 🧩 2D vs 3D

- Same math  
- 3D adds angular effects  

---

# 4. Friction & Damping

## 🎯 Goal
Reduce motion over time or on contact

---

## 🛠️ Techniques

### A. Linear Damping
```pseudo
velocity *= (1 - damping * delta)
```

---

### B. Surface Friction
```pseudo
velocity -= friction * normal_component
```

---

### C. Coulomb Friction Approximation
```pseudo
friction_force = clamp(force, max_friction)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Damping | Simple | Not physically accurate |
| Surface Friction | Context-aware | Needs tuning |
| Coulomb | Realistic | More complex |

---

## 💥 Failure Cases

- Objects never fully stop  
- Overdamping → sticky movement  
- Sliding on flat surfaces  

---

## 🔗 Composability Notes

- Works with:
  - sliding  
  - stacking  
- Must be applied after collision resolution  

---

## 🧩 2D vs 3D

- Same principles  

---

# 5. Continuous Collision Detection (CCD)

## 🎯 Goal
Prevent fast objects from passing through surfaces

---

## 🛠️ Techniques

### A. Swept Collision
```pseudo
hit = sweep(shape, previous_pos, next_pos)
```

---

### B. Substepping
```pseudo
for step in steps:
    simulate_small_step()
```

---

### C. Time of Impact (TOI)
```pseudo
toi = compute_time_of_impact(a, b)
position = interpolate_to(toi)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Sweep | Accurate | Expensive |
| Substep | Simple | Cost increases fast |
| TOI | Precise | Complex |

---

## 💥 Failure Cases

- Missed collisions at extreme speeds  
- Performance spikes  
- Numerical instability  

---

## 🔗 Composability Notes

- Requires:
  - detection system  
- Interacts with:
  - physics timestep  
  - resolution order  

---

## 🧩 2D vs 3D

- Same approach  
- 3D more expensive  

---

# 6. Stable Stacking

## 🎯 Goal
Keep objects resting on each other without jitter

---

## 🛠️ Techniques

### A. Constraint Solvers
```pseudo
solve_constraints(bodies)
```

---

### B. Iterative Solver (Gauss-Seidel)
```pseudo
for i in iterations:
    resolve_contacts()
```

---

### C. Sleep States
```pseudo
if velocity < threshold:
    set_sleeping()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Solver | Stable | Complex |
| Iterative | Practical | Needs tuning |
| Sleep | Performance boost | Can freeze incorrectly |

---

## 💥 Failure Cases

- Jittering stacks  
- Objects sinking  
- Exploding stacks  

---

## 🔗 Composability Notes

- Requires:
  - penetration resolution  
  - friction  
- Highly dependent on:
  - timestep consistency  

---

## 🧩 2D vs 3D

- 3D significantly harder  

---

# 7. Jittering & Stability Fixes

## 🎯 Goal
Eliminate unstable micro-movements

---

## 🛠️ Techniques

### A. Velocity Threshold Clamp
```pseudo
if abs(velocity) < epsilon:
    velocity = 0
```

---

### B. Positional Correction Bias
```pseudo
position += correction * bias
```

---

### C. Fixed Timestep
```pseudo
simulate(dt_fixed)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Clamp | Simple | Can hide real issues |
| Bias | Stabilizes | Can drift |
| Fixed Timestep | Consistent | Less flexible |

---

## 💥 Failure Cases

- Visible snapping  
- Energy loss  
- Hidden bugs masked  

---

## 🔗 Composability Notes

- Works across ALL physics systems  
- Essential for:
  - stacking  
  - resting contacts  

---

## 🧩 2D vs 3D

- Same idea  
- 3D amplifies instability  

---

# 🧠 FINAL INSIGHT

Collision resolution is a pipeline of corrections:

Detect → Depenetrate → Adjust Velocity → Apply Forces → Stabilize

Most bugs come from:
- Wrong order of operations  
- Missing iterations  
- Systems fighting each other  
- Numerical instability  
