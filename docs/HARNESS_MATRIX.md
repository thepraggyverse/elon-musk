# Harness Matrix

This plugin is intentionally small: 17 `SKILL.md` folders plus plugin metadata. It does not ship MCP servers, custom subagents, or host-specific commands.

## Support Levels

| Harness | Support level | Install path | Update path |
|---|---|---|---|
| Codex app | Native plugin marketplace | Add `thepraggyverse/elon-musk` as a custom marketplace, install `elon-musk`, restart Codex | Update marketplace/plugin in the app, restart Codex |
| Codex CLI local | Personal marketplace | `python3 scripts/install_local.py --marketplace` then `codex plugin add elon-musk@personal` | `git pull --ff-only`, rerun installer, rerun `codex plugin add` |
| Codex loose skills | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.codex/skills` | `git pull --ff-only`; symlinks keep pointing at the checkout |
| Claude Code plugin | Claude-compatible plugin metadata | `/plugin marketplace add thepraggyverse/elon-musk` then `/plugin install elon-musk` | `/plugin marketplace update elon-musk-methods` then `/plugin update elon-musk` |
| Claude Code local dev | Plugin directory | `claude --plugin-dir "$PWD"` | Restart Claude Code after edits |
| Claude Code loose skills | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.claude/skills` | `git pull --ff-only`; restart session |
| OpenClaw | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.openclaw/skills` | `git pull --ff-only`; restart session |
| Shared `.agents` home | Direct `SKILL.md` folders | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.agents/skills` | `git pull --ff-only`; restart session |
| Cursor | Not native yet | Use direct skill folders only if your Cursor setup imports `SKILL.md` directories | Pull the repo and refresh that import |
| Gemini CLI | Not native yet | Use direct skill folders only if your Gemini setup imports `SKILL.md` directories | Pull the repo and refresh that import |
| OpenCode | Not native yet | Use direct skill folders only if your OpenCode setup imports `SKILL.md` directories | Pull the repo and refresh that import |
| Pi | Not native yet | Use direct skill folders only if your Pi setup imports `SKILL.md` directories | Pull the repo and refresh that import |
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
python3 scripts/install_local.py --symlink-skills
```

Default homes:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
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
python3 scripts/install_local.py --symlink-skills --dry-run
```

Verify direct skill links:

```bash
python3 scripts/check_install.py --skill-links
```

## Update Checklist

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 scripts/check_install.py --plugin --skill-links
```

Start a new session in the target harness after updating.

## Codex Skill Budget Check

On machines with many skill roots, Codex can install the plugin but omit late
skills from the model-visible prompt when the global skill inventory exceeds
the skill context budget. After installing, check:

```bash
python3 scripts/check_install.py --prompt-input
codex debug prompt-input | rg 'x-compound|x-handoff'
```

If nothing appears, the plugin cache can still be valid while automatic skill
invocation is unreliable. Disable unused plugins/skill roots or use a slim
Codex profile for this plugin.

## Uninstall Checklist

Codex local plugin:

```bash
codex plugin remove elon-musk@personal
```

Loose skill symlinks:

```bash
find ~/.codex/skills -maxdepth 1 -type l -name 'x-*' -delete
find ~/.claude/skills -maxdepth 1 -type l -name 'x-*' -delete
find ~/.agents/skills -maxdepth 1 -type l -name 'x-*' -delete
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
- Cursor, Gemini CLI, OpenCode, and Pi rows are intentionally conservative until native manifests are added and validated.
