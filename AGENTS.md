# Agent Instructions

This repository publishes `elon-musk`, a small skill plugin that packages book-derived Elon Musk method patterns into 20 searchable `x-*` skills: 14 method lenses, 1 router, and 5 workflow skills.

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
python3 scripts/install_local.py --symlink-skills --profile codex --dry-run
```

## Working Agreement

- Keep the plugin compact: 14 book-derived method lenses, 1 router, and 5 focused workflow skills.
- Prefer merging related ideas into an existing skill subsection over adding one-off skills.
- Keep each skill operational: trigger, process, output, and example should be easy for an agent to apply.
- Keep method skills and `x-router` standalone. They may reference files inside their own skill directory but must not depend on repo-parent or sibling paths.
- `x-setup` is plugin-integrated and may use root docs and scripts with a graceful fallback when installed alone.
- `x-review-pack` may load selected sibling skills when available, but it must report and safely handle a standalone fallback.
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
3. Update `references/skill-catalog.json` when inventory metadata or taxonomy changes, then regenerate derived docs.
4. Update `references/core-methods.json` and the relevant runtime anchors when 69-method coverage changes.
5. Update `references/method-catalog.md` if the method family changes.
6. Update `references/book-map.md` if the book-derived mapping changes or if adding a non-book workflow skill that needs an explicit boundary note.
7. Update `docs/MEMORY_MODEL.md` if memory, review, lesson, or handoff behavior changes.
8. Update `README.md` and `docs/USAGE.md` if user-facing behavior changes.
9. Update `CHANGELOG.md` when the change is user-visible.
10. Run validation and tests.

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
python3 scripts/install_local.py --symlink-skills --profile codex --dry-run
python3 scripts/uninstall_local.py --skill-links --profile codex --dry-run
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
- Treat `PLAN.md` as the project roadmap and execution-state source, not permission to skip requirements or owner confirmation.
- Treat requirements as product intent and plans as implementation boundaries.
- Do not implement vision-only ideas until they become requirements, then a plan, then receive user confirmation.
- The marginal cost of completeness is near zero with AI. Do the whole thing.
- Do it right. Do it with tests. Do it with documentation.
- Do it so well that Praggy is genuinely impressed, not politely satisfied, actually impressed.
- Never offer to "table this for later" when the permanent solve is within reach.
- Never leave a dangling thread when tying it off takes five more minutes.
- Never present a workaround when the real fix exists.
- The standard is not "good enough" it is "holy shit, that's done."
- Search before building.
- Test before shipping.
- Ship the complete thing.
- When Praggy asks for something, the answer is the finished product, not a plan to build it.
- Time is not an excuse. Fatigue is not an excuse. Complexity is not an excuse.
- Boil the ocean.
- The Praggy standard is the finished scoped product, not a plan to build it.
- Do the confirmed slice right, with tests, documentation, and source-grounded investigation.
- Search and inspect existing source before building new systems.
- Test before shipping or checkpointing.
- Do not offer a workaround when the real fix is within the owned scope and reachable.
- Do not leave a dangling thread when tying it off is small and safe.
- If the complete fix is outside the confirmed scope, record the better fix as a future slice instead of silently expanding scope.
- Default to one active worker per repo, task, slice, and file scope.
- If validation or autoreview finds an issue in an active worker slice, route a bounded follow-up to that same worker instead of spawning a duplicate.
- Heartbeats may inspect state, verify evidence, create local checkpoint commits after all gates pass, and start exactly one next worker when the next slice is clear.
- Worker ping-back is the primary completion signal. Heartbeat inspection is backup, not proof by itself.
- Default watchdog cadence is 10 minutes when the owner approves automated heartbeats.
- The timer wakes the orchestrator. It does not directly spawn workers.
- A worker is not complete until the worker thread has finished or reported blocked, handoff and registry are updated, final gates have passed or exact blockers are documented, autoreview is clean or routed, report-back happened when available, and PLAN.md, handoff, registry, worker thread status, git state, validation, and autoreview agree.
- Final gates include npm run verify when available, repo tests when available, smoke when available, package smoke when package or CLI behavior changed, git diff --check, git diff --cached --check, owner-doc punctuation scan, local autoreview, and behavior validation when applicable.
- Do not treat autoreview can run as autoreview is clean.
- Keep heartbeat wakeups active while there is an active worker, pending verification, pending acceptance, or an approved automation loop.
- If docs and worker thread state disagree, live worker thread state wins until reconciled.
- Use a V0...Vn version map in PLAN.md for whole-project visibility.
- Keep later versions sketched, expand only the next eligible version or slice before starting a worker, and lock completed versions as history except for factual drift.
- Workers do not commit by default.
- Workers may create local checkpoint commits only when their prompt explicitly grants worker commits for that slice.
- Worker commits are local only and must never push, PR, post, publish, release, or mutate public surfaces.
- The orchestrator may create local checkpoint commits or accept worker-created local checkpoints only after npm run verify when available, repo tests when available, smoke when available, package smoke when package or CLI behavior changed, git diff --check, git diff --cached --check, owner-doc punctuation scan, local autoreview, behavior validation when applicable, and handoff update pass.
- Default to main.
- Praggy-owned private repos work directly on main unless Praggy explicitly asks for a feature branch.
- Do not create feature branches by default.
- If the repo has an approved GitHub push lane and configured account and remote details, the orchestrator may push accepted main checkpoints to the approved remote without repeated pushback.
- Use the already configured GitHub account and remote details.
- Ask again only if the remote, account, repo visibility, branch, or push target is unclear or has changed.
- For open-source, forked, shared, external, or upstream-tracking repos, do not assume direct push.
- Follow the repo contribution policy unless Praggy explicitly approves direct-main push for that repo.
- Never push to an unknown remote, force-push, push secrets, create tags/releases, publish packages, or mutate public surfaces unless explicitly approved for that exact action.
- Security scans can block later public, hosted, connector, package, and release lanes until findings are fixed, waived, or explicitly deferred by the owner.
- Fix one accepted security finding per bounded worker.
- Prefer one canonical typed proof object per proof-generating version or slice and render all proof views from it.
- Keep local proof manifests separate from exact-approved live approval manifests.
- Use Matt Pocock domain-modeling when durable product vocabulary changes.
- Use Matt Pocock codebase-design when designing module interfaces, adapters, persistence, registries, or deep structure.
- Use Matt Pocock prototype for throwaway spikes that answer one question.
- Use Matt Pocock tdd for behavior-first implementation of state, persistence, export, generation, or non-trivial behavior.
- Use no-mistakes only after a real implementation checkpoint exists, the repo has been initialized for it, the work is committed, and the branch is eligible.
- Matt Pocock skills live at /Users/praggy/Developer/agent-tools/mattpocock-skills/skills/engineering/<skill>/SKILL.md when they are not installed in the active skill list.
- Use behavior-validator after autoreview when runnable user-visible or operator-visible behavior changed in UI, CLI, API, generated artifacts, or workflows.
- Use define-goal before large autonomous loops or fuzzy objectives when success evidence, stop condition, or owner-help condition is unclear.
- Use handoff for paste-ready continuation prompts, worker prompts, fresh-chat prompts, and cross-chat summaries.
- Use agent-transcript only for approved, redacted PR or issue body provenance from agent work.
- Recommend security-threat-model when auth, credentials, public APIs, hosted deployment, webhooks, payments, live connectors, multi-user state, or sensitive data enter scope, but run it only after explicit owner request.
- Use security-best-practices for explicit security review/report work or secure-by-default JS/TS, Python, or Go implementation work.
- Use gh-fix-ci for GitHub Actions PR failures after GitHub access and owner approval.
- Use gh-address-comments for GitHub PR comment follow-up after GitHub access is approved and the owner selects comments.
- Do not claim a skill or gate ran unless the exact skill instructions were read and the exact command or artifact exists.
- Use gstack as the optional workflow and skill layer when it is installed and relevant.
- Use GBrain as optional long-term searchable memory when gbrain is installed and healthy.
- Repo docs remain the source of truth for current project state.
- GBrain is recall, not authority.
- Do not make project execution depend on GBrain unless the owner explicitly makes that part of the project.
- Before using GBrain for a project decision, prefer gbrain doctor --fast plus a focused gbrain search, gbrain ask, or gbrain get check when available.
- Use GBrain for cross-project recall, prior lessons, similar failures, reusable prompts, architecture decisions, release/readiness reports, and accepted slice summaries.
- Do not import raw chats, secrets, credentials, tokens, private personal data, runtime logs, generated noise, or public/private mutation logs by default.
- Prefer curated GBrain captures after accepted slices, owner decisions, architecture decisions, failure postmortems, reusable template changes, final handoffs, and release/readiness milestones.
- Each curated capture should name the project, repo path, phase or slice, changed files, decisions, proof, failures, follow-ups, and reusable lesson.
- Raw transcripts may be imported only when explicitly useful and approved; tag them as raw or noisy so they do not masquerade as curated memory.
- Never use GBrain sync, import, publish, integrations, or watch modes to move secrets, private repos, public mutation records, or sensitive user data without explicit owner approval.
- If GBrain is unavailable, continue from repo docs and mention that cross-project memory lookup was skipped.
- Every implementation slice must wire into an existing user-visible path, operator command, API, or documented module interface, or explicitly mark itself as an isolated prototype.
- Do not leave parallel systems, orphan adapters, unused schemas, duplicate state stores, or dead prototype paths without recording a follow-up slice.
- After each accepted version, run an integration review before starting the next version: entrypoints wired, types and tests aligned, docs updated, stale code removed or tracked, and architecture drift noted.
- Keep refactors scoped to the slice unless the refactor is the slice.
- If cleanup crosses module ownership, changes public behavior, changes persistence shape, or affects multiple slices, promote it to a planned refactor slice with its own gates.
- Update ARCHITECTURE.md when module boundaries, data flow, runtime topology, persistence, or external integrations change.
- Run the Integration Reflection Gate before accepting a completed slice, checkpointing, or expanding the next version.
- Integration Reflection asks whether a larger refactor would be better, what we would do differently, the better long-term shape, whether tests are enough, what docs should be written and where, what source errors or confusing paths are visible, and what questions remain for Praggy.
- Classify each reflection answer as Accept now, Small cleanup, Future refactor slice, Needs owner decision, or Real blocker.
- If reflection reveals small cleanup inside the current worker scope, route it back before acceptance.
- If reflection reveals larger cleanup, create a planned refactor slice instead of doing it opportunistically.
- If reflection requires product direction, credentials, public mutation, or expanded scope, ask Praggy.
- No PR, merge, close, hosted deployment, public webhook, release, publish, public comment, npm publish, GitHub release, tag push, Homebrew change, package publication, public announcement, paid API, credentials, cloud mutation, live Slack/GitHub/connector mutation, broker integration, or live-money integration without explicit owner approval for that exact item.
- If no approved next version slice exists, stop heartbeat wakeups and ask before extending PLAN.md.
- Classify agent automation as a goal, loop, or routine before running it.
- Every loop must have a verifier, budget or iteration cap, no-progress stop, and owner-help condition.
- Prefer independent verification over letting the worker grade its own work.
- Use scout passes for unclear work: inspect, classify, reproduce, estimate, and recommend before editing.
- Use ship passes for confirmed work: implement the scoped slice, verify it, and report proof.
- Workers execute. Orchestrators coordinate, verify, and ask owner-level questions. Workers should not recursively spawn more workers.
- Tool-level subagents or sidecar helpers may be used for bounded review, source inspection, test diagnosis, and verification when useful.
- Tool-level subagents or sidecar helpers must not own project scope, hold registry leases, create project worker chats, mutate public surfaces, push, post, deploy, or cross the worker forbidden scope.
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
