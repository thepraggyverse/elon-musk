# Changelog

All notable changes to this project are documented here.

This project uses a lightweight Keep a Changelog style. The source of truth for
the package version is `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`.

## Unreleased

### Added

- Added `x-setup` for plugin install checks, direct skill-home verification,
  Codex cache inspection, and prompt-visibility diagnosis.
- Added `examples/all-skills.md` as a compact example index covering every
  public skill.
- Added a README compatibility quick scan showing output artifact, write
  behavior, and safe-default status for every skill.
- Added `x-compound` for saving one to three approved local Markdown reviews or
  lessons after useful method work.
- Added `x-handoff` for writing compact redacted continuation notes.
- Added `docs/MEMORY_MODEL.md` to document local review, lesson, and handoff
  storage boundaries.
- Added `scripts/check_install.py` to verify Codex plugin cache installs,
  direct skill-home symlinks, and prompt-input visibility.
- Added expanded harness, install, usage, and reference-audit documentation for
  the 18-skill package.
- Added public security, privacy, release, and documentation-audit docs.

### Changed

- Updated Codex and Claude-compatible manifests from 15 to 18 `x-*` skills.
- Updated `README.md`, `CONCEPTS.md`, `AGENTS.md`, `docs/USAGE.md`, and
  references so workflow skills are described separately from book-derived
  method lenses.
- Tightened public validation and unit tests to cover the new docs, memory
  model, install checker, and Codex default-prompt limit.
- Scoped hygiene validation to tracked and untracked non-ignored public files so
  local scaffold artifacts do not break package validation.

### Fixed

- Fixed Codex manifest default prompts to stay within Codex's three-prompt
  limit.
- Fixed install checking so marketplace-only, direct-symlink-only, and combined
  installs can be validated independently.

## 0.1.0 - Initial public package

### Added

- Published the initial compact skill plugin with 15 book-derived `x-*` method
  lenses.
- Added Codex and Claude-compatible plugin metadata.
- Added install, harness, usage, source-boundary, reference, example, and
  validation docs.
