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

### 5. Docker

Used to run the PostgreSQL database (no native PostgreSQL install needed). Also used in Phase 4 to run the prototype in a consistent environment.

| OS | Status | Install |
|----|--------|---------|
| Linux | Not always included | https://docs.docker.com/engine/install/ |
| macOS | Not included | https://docs.docker.com/desktop/install/mac-install/ |
| Windows | Not included | https://docs.docker.com/desktop/install/windows-install/ |

Verify:
```bash
docker --version
docker compose version
```

**PostgreSQL via Docker:** All `psql` commands in the workflow are run inside the Docker container:
```bash
docker exec -i <container_name> psql -U <db_user> -d <db_name> < schema.sql
```
The container name, user, and database are defined in the project's `docker-compose.yml`, set up during Stage 4-1.

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


---

## Quick verification

Run this to check all required tools at once:

```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "docker:    $(docker --version 2>/dev/null || echo 'NOT FOUND')"
echo "git:       $(git --version 2>/dev/null || echo 'NOT FOUND')"
```
