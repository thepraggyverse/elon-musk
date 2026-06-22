# Install

This document covers installing `elon-musk` as a local Codex plugin and optionally exposing every `x-*` skill through local skill homes.

## Requirements

- macOS or Linux shell.
- Python 3.10 or newer.
- Codex CLI/Desktop if installing as a Codex plugin.
- Optional: any other agent that can load `SKILL.md` skill folders.

## Option 1: Install As A Codex Plugin

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

## Option 3: Symlink Skills Directly

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

## Option 4: Marketplace Plus Symlinks

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
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
codex plugin list | grep elon-musk
```

## Updating

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
```

Start a new Codex thread after reinstalling so updated skills load into the active context.
