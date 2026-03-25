# Phase 4: Consolidation Artifact Update Authority

Phase 4 personas have authority — and responsibility — to update consolidation artifacts when implementation reveals the design needs to change.

## Why This Exists

The consolidation artifacts are the source of truth. The `docs/` files from earlier phases are historical. When implementation discovers a discrepancy or necessary change, the consolidation artifact must be updated to reflect reality.

## When to Apply This

When any Phase 4 stage encounters:
- An API contract that doesn't match what implementation requires
- A data model that needs adjustment (new column, changed type, missing table)
- A use case definition that needs clarification or scope change
- A tech stack decision that needs revision

## Protocol

1. **Stop** — do not make the change silently or work around it
2. **Flag** to the user:
   > "The current `[artifact-filename]` says [X]. Implementation reveals we need [Y] because [reason]. Proposing to update the artifact — agree?"
3. **Get explicit approval** before modifying the artifact
4. **Update the consolidation artifact** with the change
5. **Record in `implementation-decisions.md`** under `## Design Changes`:

```
### YYYY-MM-DD — [one-line summary]
Artifact: [filename]
Change: [what changed precisely]
Rationale: [what implementation discovered that required this change]
```

## Scope of Authority

| Change type | Authority |
|-------------|-----------|
| Field rename, type correction, add missing field | Update + record |
| New endpoint or endpoint restructure | Update + record |
| New entity or table | Update + record |
| Remove a use case from scope | User must explicitly agree — flag clearly |
| Change project goals or core constraints | Out of scope for Phase 4 — requires Stage 0 |

## What NOT to Do

- Do not update `docs/` files — they are historical; consolidation artifacts are live
- Do not make silent fixes — every change must be recorded
- Do not invent changes to "improve" the design — only change what implementation genuinely requires
