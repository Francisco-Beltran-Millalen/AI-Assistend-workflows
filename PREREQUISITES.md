# Prerequisites

Everything you need installed before using this workflow.

---

## Required

### 1. LLM CLI (Claude Code recommended)

The interface you use to run the workflow stages.

- **Claude Code**: https://claude.ai/code
- Any compatible LLM CLI that supports project instructions and slash commands

### 2. Python 3

Used by the workflow scripts (log export, transcript conversion).

| OS | Status | Install |
|----|--------|---------|
| Linux (Debian/Ubuntu) | Pre-installed | `sudo apt install python3` if missing |
| macOS | Pre-installed | `brew install python3` if missing |
| Windows | Not included | Install from https://python.org or use WSL |

Verify: `python3 --version`

### 3. bash

Required to run the workflow hook scripts.

| OS | Status | Notes |
|----|--------|-------|
| Linux | Pre-installed | Default shell |
| macOS | Available | Not the default (zsh is), but present. Scripts run fine via `#!/bin/bash` shebang. |
| Windows | Not included | Use WSL (recommended) or Git Bash |

- **WSL**: https://learn.microsoft.com/en-us/windows/wsl/install
- **Git Bash**: ships with Git for Windows — https://git-scm.com

Verify: `bash --version`

### 4. Web browser

Used to review HTML views produced in Phase 2 (UI Sketching) and Phase 3 (UI Polish).

Any modern browser works (Chrome, Firefox, Safari, Edge).

### 5. SQLite CLI

Used in Stage 2-2 to validate the database schema and mock data by running the generated `schema.sql` script.

| OS | Status | Install |
|----|--------|---------|
| Linux (Debian/Ubuntu) | Not always included | `sudo apt install sqlite3` |
| macOS | Pre-installed | Available via `sqlite3` |
| Windows | Not included | https://sqlite.org/download.html or use WSL |

Verify: `sqlite3 --version`

### 6. Git

Required to clone the workflow, version control your project, and push to GitHub.

| OS | Status | Install |
|----|--------|---------|
| Linux (Debian/Ubuntu) | Usually pre-installed | `sudo apt install git` if missing |
| macOS | Usually pre-installed | `brew install git` if missing |
| Windows | Not included | https://git-scm.com (Git Bash included) |

Verify: `git --version`

---

## Planned (not yet required)

<!--
  - Docker: planned for standardizing the development and deployment environment
    in Phase 4 (Prototype Implementation), so the project runs consistently
    across machines without manual dependency setup.
    Install: https://docs.docker.com/get-docker/
-->

---

## Quick verification

Run this to check all required tools at once:

```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "sqlite3:   $(sqlite3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "git:       $(git --version 2>/dev/null || echo 'NOT FOUND')"
```
