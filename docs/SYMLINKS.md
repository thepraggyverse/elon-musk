# Symlinks

This repo supports two kinds of symlinks: one for the local Codex plugin source, and one set for direct `SKILL.md` skill homes.

## Plugin Source Symlink

Codex's personal marketplace expects:

```text
~/plugins/elon-musk
```

If the repo lives somewhere else, run:

```bash
python3 scripts/install_local.py --marketplace
```

The script creates:

```text
~/plugins/elon-musk -> /actual/path/to/elon-musk
```

This keeps the source of truth wherever you cloned it while satisfying Codex marketplace resolution.

## Skill Home Symlinks

For tools that scan loose skill folders, run:

```bash
python3 scripts/install_local.py --symlink-skills --profile codex
```

Available profiles:

```text
agents, codex, claude, openclaw, openclaw-codex, all
```

Select only the harnesses you intend to modify.
The installer refuses `--symlink-skills` without a named profile or explicit `--skill-home`.

Example result:

```text
~/.codex/skills/x-router -> ~/plugins/elon-musk/skills/x-router
~/.codex/skills/x-purpose -> ~/plugins/elon-musk/skills/x-purpose
~/.codex/skills/x-5-step-algo -> ~/plugins/elon-musk/skills/x-5-step-algo
```

## Existing Destinations

The installer is conservative:

- Existing correct symlink: keep it.
- Existing different file/dir/link: skip it.
- `--force`: replace it.

Preview before replacing:

```bash
python3 scripts/install_local.py --symlink-skills --profile codex --dry-run
```

Replace intentionally:

```bash
python3 scripts/install_local.py --symlink-skills --profile codex --force
```

## Remove Symlinks

Use the targeted uninstaller to remove only links owned by this checkout:

```bash
python3 scripts/uninstall_local.py --skill-links --profile codex --dry-run
python3 scripts/uninstall_local.py --skill-links --profile codex
```

Foreign links, regular files, and directories are skipped.

## Update Symlinks

Symlinks point at this checkout. Updating is usually just:

```bash
cd ~/plugins/elon-musk
git pull --ff-only
```

If you added a new skill home or want to repair missing links:

```bash
python3 scripts/install_local.py --symlink-skills --profile codex
```
