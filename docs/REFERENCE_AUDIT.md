# Reference Audit

This audit records what was reviewed and what changed in this repository.

## Sources Reviewed

| Source | Relevant patterns |
|---|---|
| `https://every.to/guides/compound-engineering` | Philosophy first, main loop, compound step, AGENTS/CLAUDE guidance, project artifact folders, review questions, staged adoption. |
| `EveryInc/compound-engineering-plugin` | Multi-harness README, root AGENTS contract, Codex and Claude plugin metadata, repo-local marketplace metadata, install/update docs, validation discipline. |
| `EveryInc/compound-knowledge-plugin` | Small workflow loop, local knowledge store, progressive disclosure, simple component counts, project context via agent instruction files. |
| `mattpocock/skills` | Skills grouped by invocation role, README as skill index, setup skill mindset, direct skill linking scripts. |
| `steipete/agent-scripts` | Portable local skill homes, concise frontmatter, helper scripts only for repeated commands, shared AGENTS pointer pattern. |

## Gaps Found

| Gap | Why it mattered | Fix |
|---|---|---|
| README opened with awkward independence/plugin wording. | The front page should explain what the skills do before legal context. | Rewrote top section around skill purpose, routes, and examples. |
| No root `AGENTS.md`. | Agent repos need a canonical authoring contract. | Added `AGENTS.md` and `CLAUDE.md` compatibility pointer. |
| Only Codex manifest existed. | Claude-compatible harnesses need their own metadata or direct skill paths. | Added `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`. |
| No repo-local Codex marketplace metadata. | Codex app custom marketplace installs are clearer with repo metadata. | Added `.agents/plugins/marketplace.json`. |
| Install docs were Codex-heavy. | User wanted all harnesses, install, update, and uninstall. | Added `docs/HARNESS_MATRIX.md` and expanded `docs/INSTALL.md`. |
| Plugin manifest was thin. | Marketplace UI needs cleaner description, homepage, repository, keywords, capabilities, and examples. | Expanded `.codex-plugin/plugin.json`. |
| Source-boundary explanation was mixed into the lead. | The top should be useful; legal/source guardrails still matter but belong later. | Kept source boundary and disclaimer lower in README and dedicated docs. |
| No explicit support-level table. | "Works with all harnesses" needs precision. | Added support levels by harness and "does not claim" section. |
| Validation did not require new metadata/docs. | Docs drift silently without tests. | Expanded `scripts/validate_public.py` and tests. |
| No implemented compound memory loop. | Reviews could mention reusable lessons, but no skill actually saved them. | Added `x-compound` and `docs/MEMORY_MODEL.md`. |
| No continuation handoff skill. | Long method reviews need a clean way to resume without copying raw conversation. | Added `x-handoff`. |
| No setup doctor skill. | Users need a direct way to check install, cache, symlink, and prompt-visible state. | Added `x-setup`. |
| No full-loop review skill. | Users wanted one prompt that routes, reviews, compounds, and hands off. | Added `x-review-pack`. |
| No stale-memory cleanup skill. | Once local lessons exist, duplicates and stale notes need a pruning pass. | Added `x-memory-refresh`. |
| No generated skill index. | Hand-maintained tables drift as skills change. | Added `scripts/build_index.py`, `docs/SKILL_INDEX.md`, and per-skill examples. |
| No lightweight native harness bridges. | Direct skill folders are portable, but common harnesses benefit from local rule/context files. | Added Cursor, Continue, Goose, OpenCode, and Gemini bridge files. |
| No changelog. | Reference repos use changelogs or release notes so users can track public changes. | Added `CHANGELOG.md` and `docs/RELEASE.md`. |
| No explicit security/privacy docs. | Public plugin repos should explain vulnerability reporting and data boundaries. | Added `SECURITY.md` and `PRIVACY.md`. |
| No file-backed documentation surface audit. | "All docs exist" should be inspectable against the reference repos, not only implied by README. | Added `docs/DOCUMENTATION_AUDIT.md`. |

## Decisions

### Keep 15 Book-Derived Method Lenses

The reference projects show different sizes, but this plugin should stay compact. More method lenses would make search noisier. Smaller book-derived ideas live as subsections in the existing method skills and in `references/method-catalog.md`.

### Add Only Five Workflow Skills

`x-setup`, `x-review-pack`, `x-compound`, `x-memory-refresh`, and `x-handoff` are not additional book method families. They are operating-layer skills that check installation, run bounded close-the-loop reviews, save approved lessons, refresh local memory, and write redacted continuation notes.

### Do Not Add Default Log Mining

Compound Engineering has powerful history extraction, but this plugin starts with local Markdown memory. Raw transcript or harness-history analysis should remain a later opt-in feature, not default behavior.

### Do Not Add Custom Subagents

Compound Engineering and Compound Knowledge both use agents where workflows need review or research specialists. This plugin is a method lens pack. The current value comes from routing and applying methods, so custom subagents would add install burden without enough benefit.

### Use Direct Skill Symlinks For Broad Harness Support

Not every harness supports the same plugin marketplace format. Direct `SKILL.md` folders are the most portable surface, so `scripts/install_local.py --symlink-skills` remains the broad compatibility path.

### Add Bridge Files, But Do Not Overclaim Marketplace Support

Claude-compatible metadata is useful and low risk. Cursor, Gemini, OpenCode, Continue, and Goose now have lightweight bridge files. They point back to `SKILL.md` folders and do not claim marketplace certification.

### Keep The Disclaimer, Move It Down

The repo still needs to say it is independent and unaffiliated. It should not be the first explanation a user sees.

## Future Improvements

| Idea | When to add |
|---|---|
| Host-specific marketplace validation for Cursor/Gemini/OpenCode/Pi | Only after testing that each host loads the bridge or manifest correctly. |
| Guided project bootstrap skill | If users need a repo-specific setup flow for `AGENTS.md`, `docs/reviews/`, or `docs/lessons/` beyond install diagnostics. |
| Release automation | When public versioned releases matter more than source installs. |
| Source audit fixture | If the method catalog changes frequently enough to need structured coverage data. |

## Documentation Surfaces Now Covered

| Surface | Status |
|---|---|
| README and skill inventory | present |
| AGENTS and CLAUDE compatibility pointer | present |
| Changelog and release checklist | present |
| Security and privacy docs | present |
| Install, update, uninstall, and symlink docs | present |
| Harness matrix and support-level caveats | present |
| Lightweight harness bridge files | present |
| Generated skill index and per-skill examples | present |
| Source-boundary and copyright guardrails | present |
| Reference audit and documentation audit | present |
| Validation and unit-test coverage for docs | present |
