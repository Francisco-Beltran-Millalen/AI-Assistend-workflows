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

### 4. Rust + Cargo

Used to build and run the Bevy graybox prototype (graybox phase onward).

Install via **rustup** (manages Rust versions and toolchains):

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

| OS | Notes |
|----|-------|
| Linux / macOS | Install via rustup (above) |
| Windows | Use rustup-init.exe from https://rustup.rs |

Verify: `rustc --version && cargo --version`

### 5. Git

Required to clone the workflow, version control your project, and push to GitHub.

| OS | Status | Install |
|----|--------|---------|
| Linux (Debian/Ubuntu) | Usually pre-installed | `sudo apt install git` if missing |
| macOS | Usually pre-installed | `brew install git` if missing |
| Windows | Not included | https://git-scm.com (Git Bash included) |

Verify: `git --version`

---

## Required for Asset Phase

Install these when you reach the asset phase. Not needed before then.

### Krita (2D art)

Used for concept sketching, line art, coloring, and sprite sheet production.

- Download: https://krita.org/en/download/
- Available on Linux, macOS, Windows

### Blender (3D modeling)

Required only if your art direction decision is 3D or Mixed pipeline.

- Download: https://www.blender.org/download/
- Available on Linux, macOS, Windows

### Material Maker (procedural textures)

Optional. Used for generating PBR texture maps procedurally (metal, fabric, stone, etc.).

- Download: https://www.materialmaker.org

---

## Required for Sound Phase

Install when you reach the sound phase.

### Audacity

Used for trimming, normalizing, pitch-shifting, EQ, and layering SFX recordings.

- Download: https://www.audacityteam.org/download/
- Available on Linux, macOS, Windows

---

## Quick verification

Run this to check all required tools at once:

```bash
echo "Python 3:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "bash:      $(bash --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "Rust:      $(rustc --version 2>/dev/null || echo 'NOT FOUND')"
echo "Cargo:     $(cargo --version 2>/dev/null || echo 'NOT FOUND')"
echo "git:       $(git --version 2>/dev/null || echo 'NOT FOUND')"
```
