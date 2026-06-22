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
| No changelog. | Reference repos use changelogs or release notes so users can track public changes. | Added `CHANGELOG.md` and `docs/RELEASE.md`. |
| No explicit security/privacy docs. | Public plugin repos should explain vulnerability reporting and data boundaries. | Added `SECURITY.md` and `PRIVACY.md`. |
| No file-backed documentation surface audit. | "All docs exist" should be inspectable against the reference repos, not only implied by README. | Added `docs/DOCUMENTATION_AUDIT.md`. |

## Decisions

### Keep 15 Book-Derived Method Lenses

The reference projects show different sizes, but this plugin should stay compact. More method lenses would make search noisier. Smaller book-derived ideas live as subsections in the existing method skills and in `references/method-catalog.md`.

### Add Only Two Workflow Skills

`x-compound` and `x-handoff` are not additional book method families. They are operating-layer skills that close the loop: save approved lessons and write redacted continuation notes.

### Do Not Add Default Log Mining

Compound Engineering has powerful history extraction, but this plugin starts with local Markdown memory. Raw transcript or harness-history analysis should remain a later opt-in feature, not default behavior.

### Do Not Add Custom Subagents

Compound Engineering and Compound Knowledge both use agents where workflows need review or research specialists. This plugin is a method lens pack. The current value comes from routing and applying methods, so custom subagents would add install burden without enough benefit.

### Use Direct Skill Symlinks For Broad Harness Support

Not every harness supports the same plugin marketplace format. Direct `SKILL.md` folders are the most portable surface, so `scripts/install_local.py --symlink-skills` remains the broad compatibility path.

### Add Claude Metadata, But Do Not Pretend Every Host Is Native

Claude-compatible metadata is useful and low risk. For Cursor, Gemini, OpenCode, Pi, and other hosts, this repo documents direct skill-folder usage unless a native manifest is added and validated later.

### Keep The Disclaimer, Move It Down

The repo still needs to say it is independent and unaffiliated. It should not be the first explanation a user sees.

## Future Improvements

| Idea | When to add |
|---|---|
| `x-memory-refresh` | After users have enough `docs/reviews/` and `docs/lessons/` files to make stale-note auditing valuable. |
| Host-specific native manifests for Cursor/Gemini/OpenCode/Pi | Only after testing that each host loads the skills correctly. |
| Setup skill | If users need a guided project setup flow for `AGENTS.md`, `docs/reviews/`, or `docs/lessons/`. |
| More examples | When a repeated prompt pattern proves useful. |
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
| Source-boundary and copyright guardrails | present |
| Reference audit and documentation audit | present |
| Validation and unit-test coverage for docs | present |
