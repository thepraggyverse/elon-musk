# Contributing

Contributions are welcome if they preserve the purpose of the repository: compact, practical, book-derived method skills without reproducing copyrighted source material.

## Ground Rules

- Keep every callable skill prefixed with `x-`.
- Keep each `SKILL.md` small, procedural, and directly useful.
- Put broader context in `references/`, not inside every skill.
- Do not add full book text, long quotes, transcripts, or copyrighted source dumps.
- Add or update tests when changing skill inventory, references, scripts, or install behavior.
- Keep `README.md`, `docs/HARNESS_MATRIX.md`, and plugin manifests in sync with supported install paths.
- Update `CHANGELOG.md` for user-visible changes.
- Keep `SECURITY.md`, `PRIVACY.md`, and `docs/RELEASE.md` aligned when security, data-handling, or release behavior changes.

## Validate Before Opening A PR

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

If you have Codex's local skill/plugin creator helpers installed, the public validator will use them too.

## Adding A Skill

1. Pick a lowercase hyphenated `x-` name.
2. Add `skills/<name>/SKILL.md`.
3. Add `skills/<name>/agents/openai.yaml`.
4. Add the skill to:
   - `README.md`
   - `CHANGELOG.md`
   - `references/book-map.md`
   - `references/method-catalog.md`
   - `.claude-plugin/plugin.json`
   - `tests/test_plugin_structure.py`
5. Run validation.

## Promoting A Subsection

Most ideas should remain subsections in an existing top-level skill. Promote a subsection into its own skill only when it has a distinct repeated use case and clear invocation pattern.
