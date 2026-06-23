# Agent Instructions

This repository publishes `elon-musk`, a small skill plugin that packages book-derived Elon Musk method patterns into 18 searchable `x-*` skills: 15 method lenses and 3 workflow skills.

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

- Keep the plugin compact: 15 book-derived method lenses plus focused workflow skills only when they make future work easier.
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
CHANGELOG.md         User-facing change history
SECURITY.md          Vulnerability reporting and scope notes
PRIVACY.md           Data-handling and local memory boundaries
```

## Skill Maintenance

When editing or adding a skill:

1. Update `skills/<name>/SKILL.md`.
2. Update `skills/<name>/agents/openai.yaml`.
3. Update `references/method-catalog.md` if the method family changes.
4. Update `references/book-map.md` if the book-derived mapping changes or if adding a non-book workflow skill that needs an explicit boundary note.
5. Update `docs/MEMORY_MODEL.md` if memory, review, lesson, or handoff behavior changes.
6. Update `README.md` and `docs/USAGE.md` if user-facing behavior changes.
7. Update `CHANGELOG.md` when the change is user-visible.
8. Run validation and tests.

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

## Changelog And Release Notes

- Keep `CHANGELOG.md` in a lightweight Keep a Changelog style with an `Unreleased` section at the top.
- Include user-visible skill, install, validation, security, privacy, and docs changes.
- Exclude local-only scratch files, typo-only edits, and generated evidence.
- Follow `docs/RELEASE.md` before any public release, tag, push, or package publication.
- Do not push, tag, create GitHub Releases, or publish packages unless the user explicitly asks for that action.

<!-- BEGIN PRAGGY LOOP GUARDRAILS -->
## Praggy Loop Guardrails

- Treat `VISION.md` as direction, not implementation permission.
- Treat requirements as product intent and plans as implementation boundaries.
- Do not implement vision-only ideas until they become requirements, then a plan, then receive user confirmation.
- Classify agent automation as a goal, loop, or routine before running it.
- Every loop must have a verifier, budget or iteration cap, no-progress stop, and owner-help condition.
- Prefer independent verification over letting the worker grade its own work.
- Use scout passes for unclear work: inspect, classify, reproduce, estimate, and recommend before editing.
- Use ship passes for confirmed work: implement the scoped slice, verify it, and report proof.
- Workers execute. Orchestrators coordinate, verify, and ask owner-level questions. Workers should not recursively spawn more workers.
- Batch reads and tool calls where possible. Prefer evidence over long narration.
- Treat lint failures, flaky tests, unrelated broken checks, visual regressions, layout overlap, and accessibility regressions as real signals. Report scope clearly instead of ignoring them.
- Do not manually edit generated files, generated changelogs, lockfile output, or build artifacts unless this repo explicitly expects that edit.
- Do not add coauthor trailers, attribution, or public-facing metadata unless the owner asks.
- In long-form markdown, prefer one complete sentence per physical line so review diffs stay clean.
- Autoreview, browser proof, lavish artifacts, and no-mistakes gates are evidence, not permission to push, PR, merge, release, publish, or comment publicly.
<!-- END PRAGGY LOOP GUARDRAILS -->

<!-- BEGIN COMPOUND CODEX TOOL MAP -->
## Compound Codex Tool Mapping (Claude Compatibility)

This section maps Claude Code plugin tool references to Codex behavior.
Only this block is managed automatically.

Tool mapping:
- Read: use shell reads such as `cat` or `sed`, or use `rg`.
- Write: create files with `apply_patch` for manual edits.
- Edit/MultiEdit: use `apply_patch`.
- Bash: use the available shell command tool.
- Grep: use `rg`, fallback to `grep`.
- Glob: use `rg --files` or `find`.
- LS: use `ls` through the shell command tool.
- WebFetch/WebSearch: use available web tools, `curl`, or configured documentation tools.
- AskUserQuestion/Question: present choices as a numbered list in chat and wait for a reply number. For multi-select, accept comma-separated numbers. Never skip or auto-configure.
- Task/Subagent/Parallel: run sequentially in the main thread unless a real multi-agent tool is available; use `multi_tool_use.parallel` only for parallel tool calls.
- TaskCreate/TaskUpdate/TaskList/TaskGet/TaskStop/TaskOutput: use `update_plan`.
- TodoWrite/TodoRead: use `update_plan`.
- Skill: open the referenced `SKILL.md` and follow it.
- ExitPlanMode: ignore.
<!-- END COMPOUND CODEX TOOL MAP -->
