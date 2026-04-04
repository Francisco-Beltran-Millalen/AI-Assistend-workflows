# 🧠 10. AI Decision Systems

## 📌 Scope

How entities decide what to do

### Includes:
- Finite State Machines (FSM)  
- Behavior Trees  
- Utility AI  

---

## 🔍 Typical sub-problems

- Predictable behavior  
- State bugs  
- Performance issues  
- Hard-to-scale logic  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

AI is about decision-making under constraints, not intelligence

That means:
- Simplicity often beats complexity  
- Behavior must be predictable but not trivial  
- Systems must scale with content  

---

# 🧱 PROBLEM SET

---

# 1. Finite State Machines (FSM)

## 🎯 Goal
Define behavior as discrete states with transitions

---

## 🛠️ Techniques

### A. Simple FSM
```pseudo
state = IDLE

if see_enemy:
    state = CHASE
elif health_low:
    state = FLEE
```

---

### B. State with Transitions
```pseudo
if state == CHASE and lost_enemy:
    state = SEARCH
```

---

### C. State Objects
```pseudo
state.update()
state.on_enter()
state.on_exit()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Simple FSM | Easy to implement | Not scalable |
| Transition-based | More control | Complex transitions |
| State objects | Modular | More boilerplate |

---

## 💥 Failure Cases

- State explosion  
- Transition bugs  
- Hard-to-debug behavior  

---

## 🔗 Composability Notes

- Works with:
  - animation  
  - navigation  
- Often combined with:
  - event systems  

---

## 🧩 2D vs 3D

- Same concept  

---

# 2. Behavior Trees

## 🎯 Goal
Structure behavior hierarchically

---

## 🛠️ Techniques

### A. Selector Node
```pseudo
for child in children:
    if child.succeeds():
        return success
```

---

### B. Sequence Node
```pseudo
for child in children:
    if child.fails():
        return failure
```

---

### C. Action Node
```pseudo
move_to(target)
attack()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Behavior Tree | Modular | Harder to debug |
| Selector/Sequence | Structured | Verbose |
| Action Nodes | Flexible | Needs good design |

---

## 💥 Failure Cases

- Infinite loops  
- Poor priority ordering  
- Hard-to-track execution flow  

---

## 🔗 Composability Notes

- Integrates with:
  - navigation  
  - animation  
- Often uses:
  - blackboard system  

---

## 🧩 2D vs 3D

- Same structure  

---

# 3. Utility AI

## 🎯 Goal
Choose actions based on scoring

---

## 🛠️ Techniques

### A. Score-based Decision
```pseudo
score_attack = evaluate_attack()
score_flee = evaluate_flee()

action = max(score_attack, score_flee)
```

---

### B. Weighted Factors
```pseudo
score = health_weight * health + distance_weight * distance
```

---

### C. Curve-based Evaluation
```pseudo
score = curve(distance_to_target)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Utility AI | Dynamic behavior | Hard to tune |
| Weighted | Flexible | Needs balancing |
| Curves | Smooth decisions | Complex setup |

---

## 💥 Failure Cases

- Unstable decisions (flip-flopping)  
- Poor tuning → bad behavior  
- Hard-to-debug scoring  

---

## 🔗 Composability Notes

- Often replaces FSM transitions  
- Works well with:
  - perception systems  
- Needs:
  - cooldowns or hysteresis  

---

## 🧩 2D vs 3D

- Same concept  

---

# 4. Perception Systems

## 🎯 Goal
Provide AI with information about the world

---

## 🛠️ Techniques

### A. Vision Check
```pseudo
if raycast_to_target and within_fov:
    see_enemy = true
```

---

### B. Distance Check
```pseudo
if distance_to(target) < threshold:
    in_range = true
```

---

### C. Event Perception
```pseudo
on_noise_heard():
    investigate()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Vision | Realistic | Expensive |
| Distance | Simple | Less accurate |
| Events | Efficient | Needs triggers |

---

## 💥 Failure Cases

- AI sees through walls  
- Detection too sensitive  
- Missed detections  

---

## 🔗 Composability Notes

- Feeds:
  - FSM  
  - behavior tree  
  - utility AI  
- Uses:
  - collision queries  

---

## 🧩 2D vs 3D

- 3D requires FOV and occlusion  

---

# 5. Decision Timing & Updates

## 🎯 Goal
Control how often AI makes decisions

---

## 🛠️ Techniques

### A. Fixed Interval Updates
```pseudo
if time_since_last_update > interval:
    update_ai()
```

---

### B. Event-driven Updates
```pseudo
on_event():
    update_ai()
```

---

### C. Staggered Updates
```pseudo
update_subset_of_agents()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Fixed | Predictable | Wasteful |
| Event-driven | Efficient | Needs triggers |
| Staggered | Scalable | Less responsive |

---

## 💥 Failure Cases

- AI reacts too slowly  
- Performance spikes  
- Inconsistent behavior  

---

## 🔗 Composability Notes

- Must balance:
  - performance  
  - responsiveness  
- Interacts with:
  - perception  
  - navigation  

---

## 🧩 2D vs 3D

- Same concept  

---

# 6. Coordination & Group Behavior

## 🎯 Goal
Manage multiple agents acting together

---

## 🛠️ Techniques

### A. Shared Targets
```pseudo
group_target = player_position
```

---

### B. Role Assignment
```pseudo
assign_role(agent, ATTACKER)
assign_role(agent, SUPPORT)
```

---

### C. Formation Systems
```pseudo
position = formation.get_slot(agent)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Shared Target | Simple | Predictable |
| Roles | Varied behavior | Needs logic |
| Formation | Organized | Complex |

---

## 💥 Failure Cases

- Agents overlap  
- Group deadlocks  
- Unrealistic coordination  

---

## 🔗 Composability Notes

- Works with:
  - navigation  
  - steering  
- Needs:
  - communication system  

---

## 🧩 2D vs 3D

- Same logic  

---

# 7. Debugging & Visualization

## 🎯 Goal
Understand AI decisions

---

## 🛠️ Techniques

### A. Debug States
```pseudo
print(current_state)
```

---

### B. Visual Debugging
```pseudo
draw_path(path)
draw_fov()
```

---

### C. Decision Logging
```pseudo
log(decision, score)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Logging | Simple | Verbose |
| Visual | Intuitive | Needs tools |
| Debug States | Clear | Limited detail |

---

## 💥 Failure Cases

- Hard-to-reproduce bugs  
- Hidden logic errors  
- Lack of visibility  

---

## 🔗 Composability Notes

- Essential for:
  - complex AI  
- Should be built early  

---

## 🧩 2D vs 3D

- Same tools  

---

# 🧠 FINAL INSIGHT

AI systems are a decision pipeline:

Perception → Evaluation → Decision → Action → Feedback

Most bugs come from:
- Poor state transitions  
- Lack of constraints  
- Overly complex logic  
- Missing debugging tools  
