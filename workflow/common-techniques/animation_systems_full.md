# 🎞️ 6. Animation Systems

## 📌 Scope

How movement and actions are visually represented

### Includes:
- Animation blending  
- State machines / animation graphs  
- Root motion vs in-place animation  
- Inverse kinematics (IK)  

---

## 🔍 Typical sub-problems

- Foot sliding  
- Snapping transitions  
- Mismatch with physics  
- Animation desync  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

Animation is not just visual—it is part of the control system.

That means:
- Animation must match gameplay state  
- Motion must feel consistent with visuals  
- Systems must coordinate timing and motion  

---

# 🧱 PROBLEM SET

---

# 1. Animation State Machines / Graphs

## 🎯 Goal
Control which animation plays based on state

---

## 🛠️ Techniques

### A. Finite Animation State Machine
```pseudo
if state == IDLE:
    play("idle")
elif state == RUN:
    play("run")
elif state == JUMP:
    play("jump")
```

---

### B. Blend Trees
```pseudo
blend_value = speed / max_speed
animation = blend(idle, run, blend_value)
```

---

### C. Animation Graphs
```pseudo
node = graph.evaluate(parameters)
play(node.animation)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| FSM | Simple | Hard transitions |
| Blend Tree | Smooth transitions | Limited logic |
| Graph | Flexible | Complex setup |

---

## 💥 Failure Cases

- State mismatch (running animation while idle)  
- Transition spam  
- Hard snapping between states  

---

## 🔗 Composability Notes

- Driven by:
  - character state machine  
- Must stay synchronized with:
  - movement  
  - physics  
- Often combined with:
  - event systems  

---

## 🧩 2D vs 3D

- Same logic  
- 3D requires more blending dimensions  

---

# 2. Animation Blending

## 🎯 Goal
Smooth transitions between animations

---

## 🛠️ Techniques

### A. Linear Interpolation
```pseudo
pose = lerp(pose_a, pose_b, t)
```

---

### B. Crossfade
```pseudo
crossfade(current_anim, next_anim, duration)
```

---

### C. Additive Blending
```pseudo
final_pose = base_pose + additive_pose
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Lerp | Simple | Limited realism |
| Crossfade | Smooth | Timing-sensitive |
| Additive | Flexible | Requires correct setup |

---

## 💥 Failure Cases

- Blending incompatible poses  
- Foot sliding  
- Over-blending → mushy motion  

---

## 🔗 Composability Notes

- Works with:
  - state machines  
  - IK systems  
- Must respect:
  - timing  
  - animation phase  

---

## 🧩 2D vs 3D

- 2D: sprite blending or switching  
- 3D: skeletal blending  

---

# 3. Root Motion vs In-place Animation

## 🎯 Goal
Determine where motion comes from

---

## 🛠️ Techniques

### A. In-place Animation
```pseudo
position += velocity * delta
animation = play("run_in_place")
```

---

### B. Root Motion
```pseudo
delta_motion = animation.root_delta
position += delta_motion
```

---

### C. Hybrid Approach
```pseudo
position += blend(root_motion, velocity_motion)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| In-place | Full control | Requires syncing |
| Root Motion | Natural movement | Hard to control |
| Hybrid | Flexible | Complex |

---

## 💥 Failure Cases

- Foot sliding (in-place mismatch)  
- Loss of control (root motion)  
- Desync with physics  

---

## 🔗 Composability Notes

- Root motion must integrate with:
  - collision system  
  - navigation  
- In-place relies heavily on:
  - movement controller  

---

## 🧩 2D vs 3D

- 2D: mostly in-place  
- 3D: both approaches common  

---

# 4. Inverse Kinematics (IK)

## 🎯 Goal
Adjust bones dynamically to match environment

---

## 🛠️ Techniques

### A. Two-bone IK
```pseudo
solve_ik(shoulder, elbow, hand, target)
```

---

### B. Foot Placement IK
```pseudo
foot_target = raycast_to_ground()
apply_ik(foot, foot_target)
```

---

### C. Look-at IK
```pseudo
head.rotation = look_at(target)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Two-bone | Simple, fast | Limited flexibility |
| Foot IK | Ground alignment | Needs stable ground data |
| Look-at | Expressive | Can look unnatural |

---

## 💥 Failure Cases

- Jitter on uneven terrain  
- Foot snapping  
- Overextension of limbs  

---

## 🔗 Composability Notes

- Depends on:
  - collision queries (for ground)  
- Applied after:
  - animation blending  
- Must not fight:
  - root motion  

---

## 🧩 2D vs 3D

- Mostly 3D  
- Rare in 2D  

---

# 5. Animation Timing & Events

## 🎯 Goal
Synchronize gameplay with animation

---

## 🛠️ Techniques

### A. Animation Events
```pseudo
on_frame("attack_hit"):
    apply_damage()
```

---

### B. Time-based Triggers
```pseudo
if animation_time > threshold:
    trigger_event()
```

---

### C. State Sync
```pseudo
if animation_finished:
    change_state()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Events | Precise | Hard to maintain |
| Time-based | Simple | Less accurate |
| Sync | Clean | Needs coordination |

---

## 💥 Failure Cases

- Desync between animation and gameplay  
- Missed events  
- Double-trigger bugs  

---

## 🔗 Composability Notes

- Must align with:
  - state machine  
  - hit detection  
- Critical for:
  - combat systems  

---

## 🧩 2D vs 3D

- Same principle  

---

# 6. Animation Layering

## 🎯 Goal
Combine multiple animations (e.g., run + shoot)

---

## 🛠️ Techniques

### A. Upper/Lower Body Split
```pseudo
lower_body = run_animation
upper_body = shoot_animation
```

---

### B. Masked Blending
```pseudo
apply_mask(animation, body_parts)
```

---

### C. Additive Layers
```pseudo
final_pose += recoil_animation
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Split | Simple | Limited flexibility |
| Masking | Flexible | Setup complexity |
| Additive | Powerful | Needs careful tuning |

---

## 💥 Failure Cases

- Conflicting poses  
- Broken animations  
- Visual artifacts  

---

## 🔗 Composability Notes

- Works with:
  - blending  
  - state machines  
- Requires consistent rig setup  

---

## 🧩 2D vs 3D

- Mostly 3D  
- 2D uses sprite layering  

---

# 7. Animation & Movement Synchronization

## 🎯 Goal
Ensure visuals match actual movement

---

## 🛠️ Techniques

### A. Speed Matching
```pseudo
animation_speed = velocity.length / max_speed
```

---

### B. Stride Warping
```pseudo
adjust_stride(animation, target_speed)
```

---

### C. Motion Warping
```pseudo
warp_animation_to_target(position)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Speed Match | Simple | Limited accuracy |
| Stride Warp | Natural | Complex |
| Motion Warp | Precise | Expensive |

---

## 💥 Failure Cases

- Foot sliding  
- Overstretching animations  
- Desync during fast motion  

---

## 🔗 Composability Notes

- Critical for:
  - root motion systems  
- Interacts with:
  - navigation  
  - physics  

---

## 🧩 2D vs 3D

- Mostly 3D problem  

---

# 🧠 FINAL INSIGHT

Animation is a layer between logic and perception:

State → Animation → Blending → IK → Final Pose

Most bugs come from:
- Animation not matching gameplay state  
- Systems running out of sync  
- Mixing root motion and code-driven motion incorrectly  
- Lack of coordination between animation and physics  
