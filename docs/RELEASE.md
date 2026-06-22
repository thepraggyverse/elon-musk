# Release And Changelog

Use this file when preparing a public update, local install refresh, or release
PR for `elon-musk`.

## Version Source

The package version lives in both manifests:

```text
.codex-plugin/plugin.json
.claude-plugin/plugin.json
```

Keep the versions equal. Do not bump the version for routine local testing.
Only bump when preparing a real public release or when the user asks for it.

## Changelog Rules

`CHANGELOG.md` is the user-facing change history.

- Keep an `## Unreleased` section at the top.
- Include user-visible skill, install, validation, security, privacy, and docs
  changes.
- Exclude typo-only edits and local-only scratch work.
- Group entries under `Added`, `Changed`, `Fixed`, `Removed`, or `Security`.
- Mention skill names and file surfaces when useful.

## Release Checklist

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/check_install.py --plugin --skill-links
```

Optional visibility check for the current Codex profile:

```bash
python3 scripts/check_install.py --prompt-input
```

That command may warn when the user's global skill inventory is too large for
Codex prompt visibility. Treat that as an environment/profile issue if the
plugin cache and symlink checks pass.

## Release Notes Shape

Use concise user-facing bullets:

```markdown
## Unreleased

### Added

- Added `x-compound` for saving approved reusable method lessons.

### Fixed

- Fixed local install checking for direct skill-home symlink installs.
```

## No-Push Default

Do not push, tag, create releases, or publish packages unless the user explicitly
approves that action.
