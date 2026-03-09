# Existing Artifact Protocol

When starting a Phase 1–4 stage, the `start-stage` skill checks whether the stage's output artifacts already exist. This protocol defines what to do when they do.

**Does not apply to on-demand stages (0, diagram, import, knowledge, teacher, git).**

---

## Step 1: Identify Which Artifacts Exist

Look at the stage file's `## Output Artifacts` section. Check if any of the listed files (or folders) already exist.

**Check for special cases first:** Some stages have special behavior when their artifacts already exist — check the stage file's `## Special Cases` section before proceeding. If the stage defines special handling, follow it. It may instruct you to skip this protocol entirely, use a different trigger artifact, or handle partial completion differently.

---

## Step 2: Read and Summarize

For each existing artifact:

1. **Read it**
2. **Show a brief summary** — 2–5 bullet points covering the key content and decisions made

---

## Step 3: Ask Why We're Revisiting

Ask the user why this stage is being run again, and present these options:

> "This stage's output already exists (summary above). Why are we revisiting it?"

- **Iteration** — Refine, expand, or improve the existing work
- **Project direction change** — Goals or scope have shifted; some or all of this may no longer apply
- **Technology stack change** — Different technology choices were made; tech-specific content needs updating
- **Error correction** — Something in the artifact is factually wrong and needs fixing
- **Other** — User describes another reason

---

## Step 4: Proceed Based on the Reason

| Reason | How to Proceed |
|--------|----------------|
| **Iteration** | Load as current state. Build on it. Do not restart from scratch. |
| **Project direction change** | Start fresh. Keep existing artifact as historical reference only — do not be bound by prior decisions. |
| **Technology stack change** | Update in place. Focus changes on tech-specific sections. Structural and domain decisions remain unless the user changes them. |
| **Error correction** | Load the artifact, identify the specific error, fix it. Update in place. |
| **Other** | Ask for more context, then decide together how to proceed. |

---

After completing this protocol, continue with the stage process (Step 5 of `start-stage`).
