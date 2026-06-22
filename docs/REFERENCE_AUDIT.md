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

## Decisions

### Keep 15 Top-Level Skills

The reference projects show different sizes, but this plugin should stay compact. More skills would make search noisier. Smaller ideas live as subsections in the existing `x-*` skills and in `references/method-catalog.md`.

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
| Host-specific native manifests for Cursor/Gemini/OpenCode/Pi | Only after testing that each host loads the skills correctly. |
| Setup skill | If users need a guided project setup flow for `AGENTS.md`, `docs/reviews/`, or `docs/lessons/`. |
| More examples | When a repeated prompt pattern proves useful. |
| Release automation | When public versioned releases matter more than source installs. |
| Source audit fixture | If the method catalog changes frequently enough to need structured coverage data. |
