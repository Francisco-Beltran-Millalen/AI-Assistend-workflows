# 🎮 7. Input Systems

## 📌 Scope

How player input is captured and interpreted

### Includes:
- Input buffering  
- Action mapping  
- Device abstraction  

---

## 🔍 Typical sub-problems

- Missed inputs  
- Input lag  
- Conflicting actions  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

Input systems should capture intent, not raw hardware state.

That means:
- Separate input reading from game logic  
- Convert inputs into actions or intents  
- Make input time-aware (not just frame-based)  

---

# 🧱 PROBLEM SET

---

# 1. Input Sampling

## 🎯 Goal
Capture input from devices reliably

---

## 🛠️ Techniques

### A. Polling (Per Frame)
```pseudo
input = read_device_state()
```

---

### B. Event-based Input
```pseudo
on_key_pressed(key):
    handle_input(key)
```

---

### C. Hybrid Sampling
```pseudo
events = collect_events()
state = current_device_state()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Polling | Simple | Can miss short inputs |
| Events | Precise | More complex |
| Hybrid | Robust | More systems to manage |

---

## 💥 Failure Cases

- Input missed between frames  
- Multiple inputs in one frame lost  
- Event flooding  

---

## 🔗 Composability Notes

- Feeds:
  - input buffering  
  - intent system  
- Must align with:
  - game loop timing  

---

## 🧩 2D vs 3D

- Same system  

---

# 2. Input Mapping (Action System)

## 🎯 Goal
Map raw input to game actions

---

## 🛠️ Techniques

### A. Direct Mapping
```pseudo
if key == SPACE:
    jump()
```

---

### B. Action Mapping
```pseudo
if action_pressed("jump"):
    jump()
```

---

### C. Contextual Input Mapping
```pseudo
if context == MENU:
    handle_menu_input()
elif context == GAMEPLAY:
    handle_game_input()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Direct | Simple | Not flexible |
| Action Mapping | Rebindable | Needs setup |
| Contextual | Scalable | More complexity |

---

## 💥 Failure Cases

- Hardcoded inputs  
- Conflicting bindings  
- Wrong context handling  

---

## 🔗 Composability Notes

- Feeds:
  - intent system  
  - state machines  
- Must integrate with:
  - UI systems  
  - gameplay modes  

---

## 🧩 2D vs 3D

- Same concept  

---

# 3. Input Buffering

## 🎯 Goal
Store inputs for a short time to improve responsiveness

---

## 🛠️ Techniques

### A. Simple Buffer
```pseudo
if input_pressed:
    buffer.add(input, time)
```

---

### B. Time-window Execution
```pseudo
if buffered_input and within_time_window:
    execute_action()
```

---

### C. Queue-based Input
```pseudo
queue.push(input)
process_next_input()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Buffer | Prevents missed inputs | Adds hidden logic |
| Time-window | Controlled | Needs tuning |
| Queue | Structured | Can feel delayed |

---

## 💥 Failure Cases

- Inputs triggering too late  
- Multiple buffered inputs firing unexpectedly  
- Buffer interfering with timing-based gameplay  

---

## 🔗 Composability Notes

- Works with:
  - state machines  
  - animation timing  
- Essential for:
  - platformers  
  - combat systems  

---

## 🧩 2D vs 3D

- Same system  

---

# 4. Input Priority & Conflict Resolution

## 🎯 Goal
Resolve multiple simultaneous inputs

---

## 🛠️ Techniques

### A. Priority Rules
```pseudo
if jump and crouch:
    execute(jump)
```

---

### B. State-based Filtering
```pseudo
if state == JUMP:
    ignore(crouch)
```

---

### C. Input Locking
```pseudo
if action_in_progress:
    ignore_new_inputs()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Priority | Predictable | Hardcoded rules |
| State-based | Context-aware | More logic |
| Locking | Prevents conflicts | Can feel unresponsive |

---

## 💥 Failure Cases

- Input feels ignored  
- Conflicting actions triggering  
- Player loses control  

---

## 🔗 Composability Notes

- Must align with:
  - state machine  
  - animation system  
- Critical for:
  - combat  
  - complex movement  

---

## 🧩 2D vs 3D

- Same logic  

---

# 5. Input Smoothing & Filtering

## 🎯 Goal
Reduce noise and create smoother input behavior

---

## 🛠️ Techniques

### A. Deadzone
```pseudo
if abs(input) < threshold:
    input = 0
```

---

### B. Smoothing / Interpolation
```pseudo
smoothed = lerp(previous_input, current_input, factor)
```

---

### C. Accumulated Input
```pseudo
input_sum += input * delta
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Deadzone | Removes noise | Reduces sensitivity |
| Smoothing | Stable input | Adds latency |
| Accumulation | Precise control | Complex |

---

## 💥 Failure Cases

- Input lag  
- Over-smoothed controls  
- Loss of responsiveness  

---

## 🔗 Composability Notes

- Used before:
  - intent system  
- Must balance:
  - responsiveness vs stability  

---

## 🧩 2D vs 3D

- Same concept  

---

# 6. Input Timing & Responsiveness

## 🎯 Goal
Ensure input feels immediate and reliable

---

## 🛠️ Techniques

### A. Frame-perfect Input
```pseudo
if input_pressed_this_frame:
    execute()
```

---

### B. Input Windowing
```pseudo
if input within allowed_window:
    execute()
```

---

### C. Latency Compensation
```pseudo
predicted_input = estimate_next_input()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Frame-perfect | Precise | Unforgiving |
| Windowing | Player-friendly | Less strict |
| Compensation | Smooth feel | Can be inaccurate |

---

## 💥 Failure Cases

- Missed inputs  
- Delayed response  
- Inconsistent timing  

---

## 🔗 Composability Notes

- Strongly tied to:
  - game loop timing  
  - animation timing  
- Works with:
  - buffering  
  - state machines  

---

## 🧩 2D vs 3D

- Same principle  

---

# 7. Device Abstraction

## 🎯 Goal
Support multiple input devices uniformly

---

## 🛠️ Techniques

### A. Unified Input Layer
```pseudo
move = get_action("move")
```

---

### B. Device-specific Mapping
```pseudo
if device == GAMEPAD:
    use_gamepad_mapping()
```

---

### C. Dynamic Rebinding
```pseudo
bind_key(action, new_key)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Unified | Clean | Abstract layer needed |
| Device-specific | Optimized | More complexity |
| Rebinding | User-friendly | Needs UI + storage |

---

## 💥 Failure Cases

- Inconsistent behavior across devices  
- Broken bindings  
- Device detection issues  

---

## 🔗 Composability Notes

- Must integrate with:
  - input mapping  
  - UI system  
- Enables:
  - accessibility  
  - cross-platform support  

---

## 🧩 2D vs 3D

- Same system  

---

# 🧠 FINAL INSIGHT

Input systems are a pipeline:

Device → Raw Input → Mapping → Buffer → Intent → Action

Most bugs come from:
- Mixing input with gameplay logic  
- Not accounting for timing  
- Conflicting input rules  
- Lack of buffering or over-buffering  
