# Native Harness Bridges

This repo's canonical runtime surface is still the portable `SKILL.md` folder
layout plus Codex and Claude-compatible plugin manifests.

The bridge files below make the same instructions easier for other harnesses to
discover. They are lightweight context/rule files, not a claim that every host
has accepted this repo as a marketplace-native package.

| Harness | Bridge file | Purpose |
|---|---|---|
| Cursor | `.cursor/rules/elon-musk-methods.mdc` | Rule file pointing Cursor agents at the skill folders. |
| Continue | `.continue/rules/elon-musk-methods.md` | Rule file for direct skill-folder usage. |
| Goose | `.goosehints` | Short repository hints for Goose-style agents. |
| OpenCode | `.opencode/AGENTS.md` | Harness-local pointer back to `AGENTS.md` and `skills/`. |
| Gemini | `GEMINI.md`, `gemini-extension.json` | Gemini context and lightweight extension metadata. |

## Validation

The public validator checks that these bridge files exist and stay ASCII/UTF-8
clean. Functional host-specific validation should be added only when that host
is available locally.
