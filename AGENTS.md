# Agent Instructions

This repository publishes `elon-musk`, a small skill plugin that packages book-derived Elon Musk method patterns into 15 searchable `x-*` skills.

`AGENTS.md` is the canonical authoring contract for this repo. `CLAUDE.md` exists as a compatibility pointer for harnesses that look for it.

## Quick Start

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

For local Codex plugin testing:

```bash
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
```

For loose skill-home testing:

```bash
python3 scripts/install_local.py --symlink-skills --dry-run
```

## Working Agreement

- Keep the plugin compact: 15 top-level `x-*` skills unless a new method family truly needs its own searchable entry.
- Prefer merging related ideas into an existing skill subsection over adding one-off skills.
- Keep each skill operational: trigger, process, output, and example should be easy for an agent to apply.
- Keep skills self-contained. A `SKILL.md` may point to files inside its own skill directory, but should not depend on sibling skill paths.
- Do not include book text, long quotes, transcripts, EPUB extracts, or copyrighted source passages.
- Keep portable repo files ASCII-only unless there is a specific reason and tests are updated.
- Use `apply_patch` for manual file edits.
- Preserve unrelated user changes in the worktree.

## Source Boundary

The source material is used to extract reusable operating methods. Store only:

- paraphrased method summaries;
- workflow checklists;
- routing guidance;
- examples written for this repository;
- source-level metadata such as section names or method labels.

Do not store:

- full chapters;
- long excerpts;
- copied quote collections;
- EPUB contents;
- transcripts.

## Directory Layout

```text
.codex-plugin/       Native Codex plugin manifest
.claude-plugin/      Claude-compatible plugin metadata
.agents/plugins/     Repo-local Codex marketplace metadata
skills/              Runtime skills, one folder per x-* skill
references/          Book map, method catalog, source notes
examples/            Prompt examples
docs/                Install, harness, usage, audit, and source-boundary docs
scripts/             Installer and public validator
tests/               Unit tests for structure and hygiene
```

## Skill Maintenance

When editing or adding a skill:

1. Update `skills/<name>/SKILL.md`.
2. Update `skills/<name>/agents/openai.yaml`.
3. Update `references/method-catalog.md` if the method family changes.
4. Update `references/book-map.md` if the book-derived mapping changes.
5. Update `README.md` and `docs/USAGE.md` if user-facing behavior changes.
6. Run validation and tests.

Every public skill must:

- live under `skills/x-*`;
- have `SKILL.md`;
- have `agents/openai.yaml`;
- include a rich model-facing description;
- include `## Output` and `## Example` sections;
- be listed in `README.md`.

## Harness Policy

Codex loads the native `.codex-plugin/plugin.json` manifest. Claude-compatible tools use `.claude-plugin/plugin.json` or direct skill symlinks. Other harnesses should use direct `SKILL.md` folders unless they explicitly support one of those plugin formats.

Do not claim native support for a harness unless the repo includes the required manifest or an explicit install path in `docs/HARNESS_MATRIX.md`.

## Verification

Before committing:

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
```

When install behavior changes, also run:

```bash
python3 scripts/install_local.py --marketplace --dry-run
python3 scripts/install_local.py --symlink-skills --dry-run --skill-home /tmp/elon-musk-skills-test
```

## Versioning

The public plugin version lives in `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`.

For routine docs and skill updates, keep the semver version stable unless a user requests a release bump. For local Codex cache refresh, prefer reinstalling from the personal marketplace; do not add public timestamp cachebusters to committed manifests.
