# 🌍 5. Navigation & Pathfinding

## 📌 Scope

How entities decide where to go

### Includes:
- NavMesh  
- A* pathfinding  
- Steering behaviors  

---

## 🔍 Typical sub-problems

- Getting stuck  
- Path smoothing  
- Dynamic obstacles  

---

# 🧠 DESIGN PRINCIPLE (IMPORTANT)

Navigation is about choosing feasible movement through space, not directly moving the entity.

That means:
- Pathfinding decides where to go  
- Movement decides how to move there  
- Steering decides how to adjust locally  

---

# 🧱 PROBLEM SET

---

# 1. Graph-based Pathfinding

## 🎯 Goal
Find a traversable route from start to destination

---

## 🛠️ Techniques

### A. A* Search
```pseudo
open_set = [start]

while open_set not empty:
    current = node_with_lowest_f_score(open_set)

    if current == goal:
        return reconstruct_path()

    for neighbor in current.neighbors:
        tentative_g = current.g + cost(current, neighbor)

        if tentative_g < neighbor.g:
            neighbor.parent = current
            neighbor.g = tentative_g
            neighbor.f = neighbor.g + heuristic(neighbor, goal)
```

---

### B. Dijkstra
```pseudo
for each node:
    distance[node] = infinity

distance[start] = 0
```

---

### C. Breadth-First Search (BFS)
```pseudo
queue.push(start)

while queue not empty:
    current = queue.pop()
    visit_neighbors(current)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| A* | Fast, practical, goal-directed | Needs good heuristic |
| Dijkstra | Finds shortest path everywhere | Expensive |
| BFS | Simple | Only good for unweighted graphs |

---

## 💥 Failure Cases

- Poor heuristic → A* behaves like Dijkstra  
- Large graphs → performance spikes  
- No path found → agent stalls  

---

## 🔗 Composability Notes

- A* often feeds:
  - waypoint following  
  - steering  
- Graph quality strongly affects all higher systems  
- Requires good cost definitions for terrain and obstacles  

---

## 🧩 2D vs 3D

- Same logic  
- 3D often uses navigation surfaces or layered graphs  

---

# 2. NavMesh Navigation

## 🎯 Goal
Represent walkable space as connected navigation regions

---

## 🛠️ Techniques

### A. Polygon NavMesh
```pseudo
start_poly = find_nav_polygon(start)
goal_poly = find_nav_polygon(goal)
path = search_connected_polygons(start_poly, goal_poly)
```

---

### B. Portal / Funnel Method
```pseudo
portals = extract_portals(path_polygons)
smoothed_path = funnel(portals)
```

---

### C. Off-mesh Links
```pseudo
if gap_detected:
    use_link(jump_link)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| NavMesh | Natural movement areas | Requires baking / generation |
| Funnel | Smooth paths | Needs clean polygon path |
| Off-mesh Links | Supports jumps/ladders | Manual setup or extra logic |

---

## 💥 Failure Cases

- Agent near mesh border gets stuck  
- Badly baked mesh causes invalid paths  
- Off-mesh links not matched to movement ability  

---

## 🔗 Composability Notes

- NavMesh usually outputs a high-level path  
- Funnel smoothing often comes after polygon search  
- Off-mesh links must integrate with:
  - animation  
  - movement states  
  - controller abilities  

---

## 🧩 2D vs 3D

- 2D may use grids or nav polygons  
- 3D NavMesh is much more common  

---

# 3. Grid-based Navigation

## 🎯 Goal
Navigate discretized space as cells or tiles

---

## 🛠️ Techniques

### A. Uniform Grid
```pseudo
grid[x][y] = walkable or blocked
path = astar(grid_start, grid_goal)
```

---

### B. Weighted Grid
```pseudo
cost = terrain_cost(cell)
```

---

### C. Flow Field
```pseudo
for each cell:
    direction = best_neighbor_toward_goal
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Uniform Grid | Easy to implement | Blocky paths |
| Weighted Grid | Terrain-aware | More tuning |
| Flow Field | Great for crowds | Expensive to generate |

---

## 💥 Failure Cases

- Stair-step paths  
- Resolution too low → poor navigation  
- Resolution too high → expensive  

---

## 🔗 Composability Notes

- Grids pair well with:
  - tactics games  
  - tilemaps  
  - RTS movement  
- Often followed by:
  - path smoothing  
  - local avoidance  

---

## 🧩 2D vs 3D

- 2D grids are common  
- 3D voxel grids are possible but heavier  

---

# 4. Path Smoothing

## 🎯 Goal
Turn raw paths into more natural motion

---

## 🛠️ Techniques

### A. Funnel Algorithm
```pseudo
smoothed_path = funnel(portals)
```

---

### B. Line-of-Sight Shortcutting
```pseudo
if raycast_clear(node_a, node_c):
    remove(node_b)
```

---

### C. Curve Interpolation
```pseudo
smooth_path = spline(path_points)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Funnel | Excellent for navmesh | Requires portals |
| Shortcutting | Simple, effective | Needs visibility checks |
| Curves | Natural look | Can leave traversable area |

---

## 💥 Failure Cases

- Smoothed path cuts through obstacles  
- Over-smoothing creates unrealistic turns  
- Curves ignore collision constraints  

---

## 🔗 Composability Notes

- Always validate smoothed paths against traversable space  
- Pairs with:
  - waypoint following  
  - steering  
- Must respect agent radius and movement limits  

---

## 🧩 2D vs 3D

- Same idea  
- 3D needs vertical validity checks  

---

# 5. Local Avoidance & Steering

## 🎯 Goal
React to nearby obstacles and moving agents

---

## 🛠️ Techniques

### A. Seek / Arrive / Flee
```pseudo
desired_velocity = normalize(target - position) * speed
steering = desired_velocity - current_velocity
```

---

### B. Obstacle Avoidance
```pseudo
if raycast_ahead_hits():
    steering += avoid_force
```

---

### C. Velocity Obstacles / RVO-like
```pseudo
safe_velocity = choose_velocity_outside_collision_cones()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Seek/Arrive | Simple | Not enough alone |
| Obstacle Avoidance | Reactive | Can jitter |
| RVO-like | Good for crowds | Complex |

---

## 💥 Failure Cases

- Agents oscillate left/right  
- Avoidance fights path following  
- Crowd deadlocks  

---

## 🔗 Composability Notes

- Steering is usually layered on top of path following  
- Must not fully override high-level navigation  
- Needs priority rules between:
  - goal seeking  
  - avoidance  
  - animation constraints  

---

## 🧩 2D vs 3D

- Same logic  
- 3D flying agents are much harder  

---

# 6. Dynamic Obstacles & Replanning

## 🎯 Goal
Handle worlds that change after path computation

---

## 🛠️ Techniques

### A. Periodic Repathing
```pseudo
if time_since_last_path > interval:
    recompute_path()
```

---

### B. Event-driven Replanning
```pseudo
if obstacle_blocks_path:
    recompute_path()
```

---

### C. Partial Path Repair
```pseudo
repair_remaining_path_from(current_position)
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Periodic | Simple | Wasted work |
| Event-driven | Efficient | Needs reliable triggers |
| Repair | Fast | Harder to implement |

---

## 💥 Failure Cases

- Constant repathing loops  
- Agent stuck on moving obstacle  
- Path invalidates every frame  

---

## 🔗 Composability Notes

- Requires coordination between:
  - perception  
  - pathfinding  
  - movement  
- Dynamic updates often need fallback behaviors like waiting or sidestepping  

---

## 🧩 2D vs 3D

- Same concept  
- 3D dynamic nav updates are costlier  

---

# 7. Waypoint Following

## 🎯 Goal
Move along a computed path reliably

---

## 🛠️ Techniques

### A. Sequential Waypoint Traversal
```pseudo
if distance_to(current_waypoint) < threshold:
    waypoint_index += 1
```

---

### B. Look-ahead Following
```pseudo
target = path[waypoint_index + offset]
move_toward(target)
```

---

### C. Predictive Targeting
```pseudo
target = estimate_future_path_point()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Sequential | Simple | Robotic motion |
| Look-ahead | Smoother | Can skip corners badly |
| Predictive | Natural | More tuning |

---

## 💥 Failure Cases

- Agent circles waypoint  
- Agent overshoots corners  
- Waypoint threshold too small or too large  

---

## 🔗 Composability Notes

- Follows output of:
  - A*  
  - navmesh  
  - smoothed path  
- Closely tied to:
  - movement controller  
  - steering system  

---

## 🧩 2D vs 3D

- Same principle  
- 3D requires vertical/path validity awareness  

---

# 8. Getting Stuck & Recovery Behaviors

## 🎯 Goal
Recover when navigation fails in practice

---

## 🛠️ Techniques

### A. Stuck Detection by Progress Check
```pseudo
if distance_to_goal_not_decreasing():
    stuck_timer += delta
```

---

### B. Local Recovery Move
```pseudo
try_side_step()
try_back_up()
```

---

### C. Full Replan / Reset
```pseudo
if stuck_timer > threshold:
    recompute_path()
```

---

## ⚖️ Tradeoffs

| Technique | Pros | Cons |
|----------|------|------|
| Progress Check | Easy | Can false trigger |
| Local Recovery | Cheap | May fail repeatedly |
| Replan | Robust | More expensive |

---

## 💥 Failure Cases

- Agent loops forever  
- Recovery conflicts with steering  
- Constant stuck/un-stuck flicker  

---

## 🔗 Composability Notes

- Essential in real games because perfect pathfinding is not enough  
- Combines with:
  - dynamic replanning  
  - waypoint following  
  - local avoidance  

---

## 🧩 2D vs 3D

- Same problem  
- 3D geometry causes more edge cases  

---

# 🧠 FINAL INSIGHT

Navigation is usually a layered stack:

Path Search → Path Smoothing → Waypoint Following → Local Avoidance → Recovery

Most bugs come from:
- Mixing global navigation with local steering incorrectly  
- Bad navigation representation  
- No recovery behavior when paths fail in practice  
- Pathfinding knowing the map, but movement not being able to execute the path  
