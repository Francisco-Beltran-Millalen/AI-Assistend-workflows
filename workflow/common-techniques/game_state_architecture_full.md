# 🧩 11. Game State & Architecture

## 📌 Scope

How all systems are structured, connected, and managed

### Includes:
- Game states (menu, gameplay, pause)  
- Scene/entity architecture  
- System communication  
- Data flow  

---

## 🔍 Typical sub-problems

- Spaghetti code  
- Tight coupling between systems  
- Hard-to-debug interactions  
- Scaling complexity  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

Architecture defines how everything evolves over time

That means:
- Systems must be decoupled but coordinated  
- Data flow must be clear and predictable  
- Structure must support growth and iteration  

---

# 🧱 PROBLEM SET

---

# 1. Game State Management

## 🎯 Goal
Control global game modes

---

## 🛠️ Techniques

### A. Simple State Switch
```pseudo
state = MENU

if start_game:
    state = GAMEPLAY
```

---

### B. State Stack
```pseudo
push_state(PAUSE)
pop_state()
```

---

### C. State Objects
```pseudo
state.update()
state.render()
state.handle_input()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Switch | Simple | Limited |
| Stack | Flexible | More complexity |
| Objects | Scalable | Boilerplate |

---

## 💥 Failure Cases

- State leaks (menu logic in gameplay)  
- Invalid transitions  
- Hidden dependencies  

---

## 🔗 Composability Notes

- Controls:
  - input handling  
  - UI  
  - gameplay systems  
- Must isolate systems per state  

---

## 🧩 2D vs 3D

- Same architecture  

---

# 2. Scene / Entity Architecture

## 🎯 Goal
Organize game objects and their behavior

---

## 🛠️ Techniques

### A. Object-Oriented (OOP)
```pseudo
class Player:
    update()
    move()
```

---

### B. Component-based Architecture
```pseudo
entity = [Transform, Physics, Render]
```

---

### C. Entity Component System (ECS)
```pseudo
systems_update(components)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| OOP | Simple | Tight coupling |
| Component | Flexible | Medium complexity |
| ECS | Scalable | Harder to learn |

---

## 💥 Failure Cases

- God objects  
- Duplicate logic  
- Hard dependencies  

---

## 🔗 Composability Notes

- ECS pairs well with:
  - large-scale systems  
- Component systems integrate with:
  - animation  
  - physics  
  - AI  

---

## 🧩 2D vs 3D

- Same structure  

---

# 3. System Communication

## 🎯 Goal
Allow systems to interact without tight coupling

---

## 🛠️ Techniques

### A. Direct Calls
```pseudo
player.take_damage()
```

---

### B. Event System
```pseudo
emit("damage_taken")
```

---

### C. Message Bus
```pseudo
send_message("enemy_spotted")
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Direct | Simple | Coupled |
| Events | Decoupled | Harder to trace |
| Message Bus | Scalable | Complex |

---

## 💥 Failure Cases

- Hidden dependencies  
- Event spam  
- Hard-to-debug flow  

---

## 🔗 Composability Notes

- Events are key for:
  - UI  
  - animation  
  - AI  
- Must maintain clear ownership of data  

---

## 🧩 2D vs 3D

- Same concept  

---

# 4. Data Flow Architecture

## 🎯 Goal
Control how data moves through systems

---

## 🛠️ Techniques

### A. Push-based Updates
```pseudo
on_event():
    update_system()
```

---

### B. Pull-based Updates
```pseudo
data = query_system()
```

---

### C. Unidirectional Flow
```pseudo
input → simulation → render
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Push | Reactive | Hard to track |
| Pull | Clear | Less efficient |
| Unidirectional | Predictable | Rigid |

---

## 💥 Failure Cases

- Circular dependencies  
- Data inconsistency  
- Update order bugs  

---

## 🔗 Composability Notes

- Must align with:
  - game loop  
- Critical for:
  - debugging  
  - determinism  

---

## 🧩 2D vs 3D

- Same structure  

---

# 5. Update Order & Game Loop

## 🎯 Goal
Ensure systems run in correct sequence

---

## 🛠️ Techniques

### A. Fixed Update Loop
```pseudo
while running:
    update()
    render()
```

---

### B. Fixed + Variable Split
```pseudo
physics_update(fixed_dt)
render_update(variable_dt)
```

---

### C. System Ordering
```pseudo
input → AI → movement → physics → animation → render
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Simple Loop | Easy | Less control |
| Fixed Split | Stable physics | More complexity |
| Ordered Systems | Predictable | Needs discipline |

---

## 💥 Failure Cases

- Order-dependent bugs  
- Jitter  
- Desync between systems  

---

## 🔗 Composability Notes

- One of the MOST critical systems  
- Affects:
  - physics  
  - input  
  - animation  
- Must be consistent  

---

## 🧩 2D vs 3D

- Same principle  

---

# 6. Modularity & Scalability

## 🎯 Goal
Allow the game to grow without breaking

---

## 🛠️ Techniques

### A. Modular Systems
```pseudo
systems = [movement, combat, AI]
```

---

### B. Plugin Architecture
```pseudo
load_module("combat_system")
```

---

### C. Feature Isolation
```pseudo
feature = self-contained_system()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Modular | Clean | Needs discipline |
| Plugin | Flexible | Overhead |
| Isolation | Safe | Duplication risk |

---

## 💥 Failure Cases

- Tight coupling  
- Feature interdependency  
- Hard-to-remove systems  

---

## 🔗 Composability Notes

- Depends on:
  - communication system  
- Enables:
  - rapid iteration  
  - testing  

---

## 🧩 2D vs 3D

- Same concept  

---

# 7. Debugging & Tooling

## 🎯 Goal
Understand and control system behavior

---

## 🛠️ Techniques

### A. Logging
```pseudo
log("state changed")
```

---

### B. Debug UI
```pseudo
draw_debug_panel()
```

---

### C. Visualization Tools
```pseudo
draw_collision()
draw_paths()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Logging | Easy | Noisy |
| Debug UI | Clear | Requires setup |
| Visualization | Powerful | Dev cost |

---

## 💥 Failure Cases

- No visibility into systems  
- Hard-to-reproduce bugs  
- Debugging slows development  

---

## 🔗 Composability Notes

- Must be integrated early  
- Essential for:
  - AI  
  - physics  
  - gameplay  

---

## 🧩 2D vs 3D

- Same tools  

---

# 🧠 FINAL INSIGHT

Game architecture is the foundation of everything:

Input → Systems → Data Flow → Update Loop → Output

Most bugs come from:
- Poor system separation  
- Unclear data flow  
- Hidden dependencies  
- Inconsistent update order  
