# Development

Use this document when editing the plugin, adding skills, changing harness support, or preparing a release.

Read `AGENTS.md` first. It is the canonical authoring contract for this repository.

## Local Checks

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

If Codex's local creator helpers are installed, `validate_public.py` also runs:

- `plugin-creator/scripts/validate_plugin.py`
- `skill-creator/scripts/quick_validate.py` for every `x-*` skill

## Install And Smoke Test Locally

```bash
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
python3 scripts/check_install.py
codex plugin list | grep elon-musk
```

Expected:

```text
elon-musk@personal   installed, enabled  0.2.0
```

## Editing A Skill

Each skill must include:

```text
skills/<skill-name>/
  SKILL.md
  agents/openai.yaml
```

Rules:

- Folder name and frontmatter `name` must match.
- Skill name must start with `x-`.
- Frontmatter must include `name` and `description` only.
- Description should include when to use the skill.
- `agents/openai.yaml` default prompt must mention `$<skill-name>`.
- Keep the skill body procedural and compact.
- Keep the README, catalog, and harness docs aligned with behavior users can actually run.

## Adding A New Skill

1. Create `skills/x-new-skill/SKILL.md`.
2. Create `skills/x-new-skill/agents/openai.yaml`.
3. Add it to `README.md`.
4. Add it to `references/method-catalog.md`.
5. Add it to `references/book-map.md`.
6. Add its metadata to `references/skill-catalog.json`.
7. Run `python3 scripts/build_index.py`.
8. Run validation.

## Updating Install Behavior

Update `scripts/install_local.py`, then test:

```bash
python3 scripts/install_local.py --marketplace --dry-run
python3 scripts/install_local.py --symlink-skills --profile codex --dry-run
python3 scripts/uninstall_local.py --skill-links --profile codex --dry-run
python3 scripts/validate_public.py
```

If install support changes, also update:

- `docs/HARNESS_MATRIX.md`
- `docs/INSTALL.md`
- `docs/SYMLINKS.md`
- `docs/DOCUMENTATION_AUDIT.md`
- `CHANGELOG.md`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json` when Claude-compatible behavior changes
- `.agents/plugins/marketplace.json` when repo-local marketplace behavior changes

## Public Release Checklist

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
python3 scripts/check_install.py
codex plugin list | grep elon-musk
```

Then commit and push.

Do not push, tag, or publish unless the user explicitly approves that release action.
