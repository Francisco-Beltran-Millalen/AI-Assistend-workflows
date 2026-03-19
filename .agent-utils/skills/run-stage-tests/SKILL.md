# Run Stage Tests Skill

Run the tests for the mechanic currently being implemented.

## Process

### 1. Identify the Current Mechanic

Read `docs/mechanic-spec.md`.

Look for the mechanic marked `[~] In progress`, or if none is in-progress, the most recently completed one.

If unclear, ask the user: "Which mechanic should I run tests for?"

### 2. Run the Filtered Test

Derive a keyword from the mechanic name (e.g., "player movement" → `movement` or `player`).

```bash
cd graybox-prototype && cargo test <mechanic_keyword>
```

If the keyword is ambiguous or uncertain, scan `graybox-prototype/src/` for test modules matching the mechanic name and run those files directly.

### 3. Report

Report:
- Which mechanic was tested
- How many tests passed / failed / skipped
- If any failed: show failure names and error messages
- If all passed: confirm clearly
