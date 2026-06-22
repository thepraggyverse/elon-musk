# Symlinks

This repo supports two kinds of symlinks.

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
python3 scripts/install_local.py --symlink-skills --dry-run
```

Replace intentionally:

```bash
python3 scripts/install_local.py --symlink-skills --force
```

## Remove Symlinks

The installer does not remove skill symlinks automatically. To remove one:

```bash
rm ~/.codex/skills/x-router
```

To remove all `x-*` symlinks from one home:

```bash
find ~/.codex/skills -maxdepth 1 -type l -name 'x-*' -delete
```

Check targets before deleting if you have other `x-*` skills.
