---
name: x-setup
description: "Check and explain an elon-musk plugin installation across Codex cache, marketplace metadata, direct skill-home symlinks, prompt visibility, and validation commands. Use when a user asks whether the plugin is installed, whether x-prefixed skills are discoverable, or how to fix a local harness setup."
---

# X Setup

Use this skill when the user wants to verify, repair, or understand an
`elon-musk` plugin installation.

## When To Use

- The user says "check install", "is it loaded?", "why is the skill missing?", or "setup doctor".
- A new skill was added and the user needs to know whether Codex, Claude, or a loose skill home can see it.
- The install appears correct on disk but automatic `$x-*` invocation is unreliable.
- The user wants exact reinstall, update, or symlink commands.

## Workflow

1. Locate the plugin checkout. Prefer the current repository if it contains `.codex-plugin/plugin.json`.
2. When this skill is inside the complete plugin, read `README.md`, `docs/INSTALL.md`, and `docs/HARNESS_MATRIX.md` only as needed. If those files are unavailable, continue with this contract and report that plugin-level docs were not loaded.
3. Run the local checker when available:

```bash
python3 scripts/check_install.py --plugin
```

4. If the user asks about model-visible skill loading, also run:

```bash
python3 scripts/check_install.py --prompt-input
```

5. Explain results in three buckets:
   - Installed state: marketplace, plugin link, cache, direct skill homes.
   - Prompt visibility: whether Codex injected the skill into prompt context.
   - Next action: reinstall, refresh cache, restart harness, reduce skill roots, or use direct skill invocation.
6. For direct skill links, require an explicit profile such as `--profile codex`, `--profile claude`, or `--profile openclaw`; never assume all homes.
7. Do not delete plugins, edit global config, or remove skill roots unless the user explicitly asks.

## Output

```text
X Setup:
Installed state:
Prompt visibility:
Issues:
Recommended command:
What this means:
```

## Completion Gate

Complete only when installed-on-disk state, prompt-visible state, the exact issue, and one targeted next command are distinguished explicitly.

## Example

User: "Use x-setup to check whether the new skills are loaded."

Answer: run `scripts/check_install.py --plugin`, optionally run
`scripts/check_install.py --prompt-input`, then explain whether the plugin cache
and direct symlinks are correct and whether the current Codex profile can see
the skills in prompt context.
