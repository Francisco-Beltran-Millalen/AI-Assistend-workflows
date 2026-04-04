# 🧍 4. Character Controller Architecture

## 📌 Scope

How you structure player/NPC movement systems

### Includes:
- Kinematic vs rigidbody controllers  
- State machines (idle/run/jump)  
- Input abstraction  
- Motion composition  

---

## ❗ Why separate

This is design architecture, not a specific mechanic.

You are deciding:
“How do all systems connect and flow together?”

NOT:
“How does jumping work?”

---

## 🔍 Typical sub-problems

- Mixing physics and control  
- State explosion  
- Reusable controllers  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

A character controller is a pipeline of decisions → motion → correction

That means:
- Input → Intent → State → Movement → Collision → Adjustment  
- Systems must be decoupled but coordinated  
- Architecture defines maintainability and scalability  

---

# 🧱 PROBLEM SET

---

# 1. Kinematic vs Rigidbody Controllers

## 🎯 Goal
Choose how movement is fundamentally driven

---

## 🛠️ Techniques

### A. Kinematic Controller
```pseudo
velocity = compute_velocity(input)
position += velocity * delta
resolve_collisions()
```

---

### B. Rigidbody Controller
```pseudo
apply_force(input_force)
physics_engine_simulates()
```

---

### C. Hybrid Controller
```pseudo
velocity = controlled_input + physics_velocity
apply_constraints()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Kinematic | Full control, predictable | Must implement everything |
| Rigidbody | Realistic, built-in physics | Hard to control precisely |
| Hybrid | Flexible | Complex, easy to break |

---

## 💥 Failure Cases

- Rigidbody: uncontrollable bouncing  
- Kinematic: unnatural interactions  
- Hybrid: conflicting forces  

---

## 🔗 Composability Notes

- Kinematic pairs well with:
  - custom collision resolution  
  - game feel systems  
- Rigidbody pairs with:
  - physics-heavy gameplay  
- Hybrid requires strict separation of concerns  

---

## 🧩 2D vs 3D

- Same concepts  
- 3D increases instability in rigidbody systems  

---

# 2. State Machines (Movement States)

## 🎯 Goal
Control behavior based on current state

---

## 🛠️ Techniques

### A. Finite State Machine (FSM)
```pseudo
state = IDLE

if input.move:
    state = RUN
if input.jump:
    state = JUMP
```

---

### B. Hierarchical State Machine
```pseudo
state = GROUND
substate = RUN
```

---

### C. Data-driven States
```pseudo
state = config[current_state]
execute(state.logic)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| FSM | Simple | State explosion |
| Hierarchical | Scalable | More complex |
| Data-driven | Flexible | Harder to debug |

---

## 💥 Failure Cases

- State explosion (too many states)  
- Invalid transitions  
- Hidden coupling between states  

---

## 🔗 Composability Notes

- Drives:
  - animation  
  - movement logic  
- Must remain independent from:
  - physics system  
- Often combined with:
  - event systems  

---

## 🧩 2D vs 3D

- Same structure  

---

# 3. Input Abstraction

## 🎯 Goal
Decouple input source from movement logic

---

## 🛠️ Techniques

### A. Input Mapping
```pseudo
move = get_input("move_axis")
jump = get_input("jump")
```

---

### B. Command Pattern
```pseudo
command = input_to_command(input)
execute(command)
```

---

### C. Intent System
```pseudo
intent.direction = input_vector
intent.jump = pressed
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Mapping | Simple | Limited flexibility |
| Command | Decoupled | More boilerplate |
| Intent | Clean design | Requires structure |

---

## 💥 Failure Cases

- Input tied directly to movement  
- Hardcoded controls  
- Multiplayer input conflicts  

---

## 🔗 Composability Notes

- Feeds:
  - state machine  
  - movement system  
- Enables:
  - AI reuse  
  - network input  

---

## 🧩 2D vs 3D

- Same concept  

---

# 4. Motion Composition

## 🎯 Goal
Combine multiple motion influences into one result

---

## 🛠️ Techniques

### A. Additive Composition
```pseudo
velocity = base + jump + external_forces
```

---

### B. Priority-based Composition
```pseudo
if stunned:
    velocity = stun_motion
else:
    velocity = player_motion
```

---

### C. Layered Motion
```pseudo
velocity = combine_layers([
    input_layer,
    physics_layer,
    animation_layer
])
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Additive | Simple | Can conflict |
| Priority | Clear control | Less flexible |
| Layered | Scalable | Complex |

---

## 💥 Failure Cases

- Forces cancel each other  
- Unexpected overrides  
- Hard-to-debug interactions  

---

## 🔗 Composability Notes

- Central to controller design  
- Must integrate with:
  - physics  
  - animation  
- Needs clear priority rules  

---

## 🧩 2D vs 3D

- Same principle  

---

# 5. Separation of Concerns

## 🎯 Goal
Avoid tightly coupled systems

---

## 🛠️ Techniques

### A. System Separation
```pseudo
input → intent → movement → physics → animation
```

---

### B. Data-oriented Design
```pseudo
components = [position, velocity, state]
systems_update(components)
```

---

### C. Event-driven Architecture
```pseudo
emit("jump_started")
on_event("jump_started", handler)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Separation | Maintainable | More structure |
| Data-oriented | Scalable | Harder to learn |
| Event-driven | Decoupled | Debug complexity |

---

## 💥 Failure Cases

- Spaghetti dependencies  
- Hidden side effects  
- Systems tightly coupled  

---

## 🔗 Composability Notes

- Foundation for:
  - reusable controllers  
  - multiplayer  
- Enables testing and iteration  

---

## 🧩 2D vs 3D

- Same architecture  

---

# 6. Reusable Controller Design

## 🎯 Goal
Create controllers that work across multiple characters

---

## 🛠️ Techniques

### A. Parameterized Controllers
```pseudo
speed = config.speed
jump_force = config.jump_force
```

---

### B. Modular Components
```pseudo
controller = [movement_module, jump_module, climb_module]
```

---

### C. Behavior Composition
```pseudo
abilities = [run, jump, dash]
apply(abilities)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Parameterized | Easy reuse | Limited flexibility |
| Modular | Flexible | Integration complexity |
| Behavior-based | Scalable | Hard to debug |

---

## 💥 Failure Cases

- Over-generalization  
- Too many configuration options  
- Inconsistent behavior across entities  

---

## 🔗 Composability Notes

- Depends on:
  - separation of concerns  
- Interacts with:
  - state machines  
  - motion composition  

---

## 🧩 2D vs 3D

- Same design  

---

# 🧠 FINAL INSIGHT

A character controller is not a single system—it is an architecture:

Input → Intent → State → Motion → Collision → Resolution → Final Transform

Most bugs come from:
- Systems doing too many things  
- Poor separation of concerns  
- Conflicting motion sources  
- State mismanagement  
