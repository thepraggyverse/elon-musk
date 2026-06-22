# Install

This document covers installing `elon-musk` as a Codex plugin, a Claude-compatible plugin, or a direct `SKILL.md` skill pack for other local harnesses.

## Requirements

- macOS or Linux shell.
- Python 3.10 or newer.
- Codex CLI/Desktop if installing as a Codex plugin.
- Claude Code if installing through `.claude-plugin/`.
- Optional: any other agent that can load `SKILL.md` skill folders.

## Option 1: Codex Local Personal Plugin

Clone into the conventional local plugin directory:

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/elon-musk.git ~/plugins/elon-musk
cd ~/plugins/elon-musk
```

Register the plugin in the default personal marketplace:

```bash
python3 scripts/install_local.py --marketplace
```

Install it into Codex:

```bash
codex plugin add elon-musk@personal
```

Verify:

```bash
codex plugin list | grep elon-musk
```

Expected status:

```text
elon-musk@personal   installed, enabled  0.1.0    /Users/<you>/plugins/elon-musk
```

## Why The `~/plugins/elon-musk` Path Matters

The personal marketplace file lives at:

```text
~/.agents/plugins/marketplace.json
```

Codex resolves this marketplace entry:

```json
{
  "name": "elon-musk",
  "source": {
    "source": "local",
    "path": "./plugins/elon-musk"
  }
}
```

relative to your home directory. That means Codex expects:

```text
~/plugins/elon-musk
```

If you cloned the repo elsewhere, the installer creates a symlink:

```text
~/plugins/elon-musk -> /actual/path/to/elon-musk
```

## Option 2: Install From Any Local Path

```bash
git clone https://github.com/thepraggyverse/elon-musk.git ~/Developer/elon-musk
cd ~/Developer/elon-musk
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
```

The installer will create `~/plugins/elon-musk` as a symlink to the current clone.

## Option 3: Codex App Custom Marketplace

In the Codex app, add this repo as a plugin marketplace:

| Field | Value |
|---|---|
| Source | `thepraggyverse/elon-musk` |
| Git ref | `main` |
| Sparse paths | leave blank |

Then install `elon-musk` from the marketplace UI and restart Codex.

For local development against the current checkout, use the local folder path as the marketplace source instead of the GitHub repo:

```text
/Users/<you>/Developer/elon-musk
```

## Option 4: Claude Code Plugin

Inside Claude Code:

```text
/plugin marketplace add thepraggyverse/elon-musk
/plugin install elon-musk
```

For local development from this checkout:

```bash
claude --plugin-dir "$PWD"
```

Claude-compatible metadata lives in:

```text
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
```

## Option 5: Symlink Skills Directly

```bash
python3 scripts/install_local.py --symlink-skills
```

Default targets:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

The script skips existing destinations unless `--force` is passed.

Use this path for OpenClaw, shared `.agents` homes, and any other harness that can read plain `SKILL.md` folders. Cursor, Gemini CLI, OpenCode, and Pi are not claimed as native integrations in this repo yet.

The direct skill pack includes 15 book-derived method lenses plus `x-compound`
for approved local memory and `x-handoff` for redacted continuation notes.

Verify direct skill links:

```bash
python3 scripts/check_install.py --skill-links
```

## Option 6: Marketplace Plus Symlinks

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/check_install.py --plugin --skill-links
```

Use this when you want both:

- Codex plugin management.
- Loose `x-*` skills visible to other local harnesses.

## Dry Run

Preview writes:

```bash
python3 scripts/install_local.py --marketplace --symlink-skills --dry-run
```

## Custom Marketplace Path

```bash
python3 scripts/install_local.py \
  --marketplace \
  --marketplace-path /path/to/marketplace.json
```

## Custom Skill Homes

```bash
python3 scripts/install_local.py \
  --symlink-skills \
  --skill-home ~/.codex/skills \
  --skill-home ~/.agents/skills
```

## Validate After Install

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 scripts/check_install.py
codex plugin list | grep elon-musk
```

Check that the installed Codex cache contains all 17 skills:

```bash
find ~/.codex/plugins/cache/personal/elon-musk/0.1.0/skills \
  -maxdepth 2 \
  -name SKILL.md | wc -l
```

If a fresh Codex process warns that the skills context budget is exceeded, the
plugin may be installed but hidden from the model-visible skill list by other
enabled skill roots. Confirm with either command:

```bash
python3 scripts/check_install.py --prompt-input
codex debug prompt-input | rg 'x-compound|x-handoff'
```

If that returns nothing, reduce the active global skill inventory or run with a
slim Codex profile before relying on automatic `x-*` skill invocation.

## Updating

### Codex Local Personal Plugin

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
```

Start a new Codex thread after reinstalling so updated skills load into the active context.

### Claude Code

```text
/plugin marketplace update elon-musk-methods
/plugin update elon-musk
```

Restart Claude Code after plugin updates so the skill loader reads the current copy.

### Direct Skill Symlinks

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --symlink-skills
```

Symlinked skill homes read the updated checkout once the harness starts a new session.

## Uninstall

Codex local personal plugin:

```bash
codex plugin remove elon-musk@personal
```

Remove local loose-skill symlinks from one skill home:

```bash
find ~/.codex/skills -maxdepth 1 -type l -name 'x-*' -delete
```

Claude Code:

```text
/plugin uninstall elon-musk
```

Then remove the checkout if you no longer need it:

```bash
rm -rf ~/plugins/elon-musk
```
