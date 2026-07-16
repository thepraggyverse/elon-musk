# Harness Matrix

This plugin is intentionally small: 20 `SKILL.md` folders plus plugin metadata and lightweight harness bridge files. It does not ship MCP servers, custom subagents, or paid-service integrations.

## Support Levels

| Harness | Support level | Install path | Update path |
|---|---|---|---|
| Codex app | Native plugin marketplace | Add `thepraggyverse/elon-musk` as a custom marketplace, install `elon-musk`, restart Codex | Update marketplace/plugin in the app, restart Codex |
| Codex CLI local | Personal marketplace | `python3 scripts/install_local.py --marketplace` then `codex plugin add elon-musk@personal` | `git pull --ff-only`, rerun installer, rerun `codex plugin add` |
| Codex loose skills | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --profile codex` | `git pull --ff-only`; symlinks keep pointing at the checkout |
| Claude Code plugin | Claude-compatible plugin metadata | `/plugin marketplace add thepraggyverse/elon-musk` then `/plugin install elon-musk` | `/plugin marketplace update elon-musk-methods` then `/plugin update elon-musk` |
| Claude Code local dev | Plugin directory | `claude --plugin-dir "$PWD"` | Restart Claude Code after edits |
| Claude Code loose skills | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --profile claude` | `git pull --ff-only`; restart session |
| OpenClaw | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --profile openclaw` | `git pull --ff-only`; restart session |
| Shared `.agents` home | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --profile agents` | `git pull --ff-only`; restart session |
| Cursor | Bridge file | Use `.cursor/rules/elon-musk-methods.mdc` plus direct skill folders | Pull the repo and refresh Cursor rules |
| Gemini | Bridge file | Use `GEMINI.md` and `gemini-extension.json` plus direct skill folders | Pull the repo and restart Gemini context |
| OpenCode | Bridge file | Use `.opencode/AGENTS.md` plus direct skill folders | Pull the repo and restart session |
| Continue | Bridge file | Use `.continue/rules/elon-musk-methods.md` plus direct skill folders | Pull the repo and refresh Continue rules |
| Goose | Bridge file | Use `.goosehints` plus direct skill folders | Pull the repo and restart session |
| Pi | Direct skill folders | Use direct skill folders only if your Pi setup imports `SKILL.md` directories | Pull the repo and refresh that import |
| Other SKILL.md harnesses | Direct folder import | Point the harness at `skills/` or symlink individual `x-*` folders | Pull the repo and restart the harness |

## Codex App

Use this when you want the plugin visible in the Codex plugin UI.

| Field | Value |
|---|---|
| Source | `thepraggyverse/elon-musk` |
| Git ref | `main` |
| Sparse paths | leave blank |

After installation, restart Codex. Existing chats do not automatically reload plugin skills.

## Codex CLI Local

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/elon-musk.git ~/plugins/elon-musk
cd ~/plugins/elon-musk
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
```

Verify:

```bash
codex plugin list | grep elon-musk
```

## Claude Code

Remote marketplace:

```text
/plugin marketplace add thepraggyverse/elon-musk
/plugin install elon-musk
```

Local checkout:

```bash
claude --plugin-dir "$PWD"
```

The Claude-compatible manifest is `.claude-plugin/plugin.json`.

## Loose Skill Homes

Use loose skill symlinks when a harness reads `SKILL.md` folders directly or when plugin marketplace support is unavailable.

```bash
python3 scripts/install_local.py --symlink-skills --profile openclaw
```

Named profiles:

```text
agents, codex, claude, openclaw, openclaw-codex, all
```

Custom homes:

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home ~/.codex/skills \
  --skill-home ~/.claude/skills
```

Preview first:

```bash
python3 scripts/install_local.py --symlink-skills --profile openclaw --dry-run
```

Verify direct skill links:

```bash
python3 scripts/check_install.py --skill-links --profile openclaw
```

## Update Checklist

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills --profile openclaw
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 scripts/check_install.py --plugin --skill-links --profile openclaw
```

Start a new session in the target harness after updating.

## Codex Skill Budget Check

On machines with many skill roots, Codex can install the plugin but omit late
skills from the model-visible prompt when the global skill inventory exceeds
the skill context budget. After installing, check:

```bash
python3 scripts/check_install.py --prompt-input
codex debug prompt-input | rg 'x-setup|x-review-pack|x-compound|x-memory-refresh|x-handoff'
```

If nothing appears, the plugin cache can still be valid while automatic skill
invocation is unreliable. Disable unused plugins/skill roots or use a slim
Codex profile for this plugin.

## Uninstall Checklist

Codex local plugin:

```bash
codex plugin remove elon-musk@personal
```

Loose skill symlinks owned by this checkout:

```bash
python3 scripts/uninstall_local.py --skill-links --profile codex
python3 scripts/uninstall_local.py --skill-links --profile claude
python3 scripts/uninstall_local.py --skill-links --profile agents
```

Claude Code plugin:

```text
/plugin uninstall elon-musk
```

## What This Repo Does Not Claim

- It does not ship custom subagents.
- It does not ship MCP servers.
- It does not install paid services.
- It does not include book text.
- It does not claim a native host integration unless this file names one.
- Cursor, Gemini, OpenCode, Continue, and Goose bridge files are lightweight adapters. Host-specific marketplace validation should be added only when each host is available locally.
