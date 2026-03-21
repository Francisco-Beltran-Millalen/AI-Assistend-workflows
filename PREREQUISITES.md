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

### 4. Git

Required to clone the workflow, version control your project, and push to GitHub.

| OS | Status | Install |
|----|--------|---------|
| Linux (Debian/Ubuntu) | Usually pre-installed | `sudo apt install git` if missing |
| macOS | Usually pre-installed | `brew install git` if missing |
| Windows | Not included | https://git-scm.com (Git Bash included) |

Verify: `git --version`

---

## Optional

### Image viewer / browser

Useful for reviewing mood board images referenced in Phase 3 (Visual Identity) and Phase 6 (Session Setup). Any image viewer works; a browser handles HTML-embedded references.

### Music player

Phase 3 (Soundscape) and Phase 6 (Session Setup) produce playlist and audio references for scene moods. Any music player or streaming service works.

---

## Quick verification

Run this to check required tools:

```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "git:       $(git --version 2>/dev/null || echo 'NOT FOUND')"
```
