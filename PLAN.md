# Elon Musk Plan

This file tracks the whole Elon Musk project from start to finish, not only v0 or the next slice.
It is the control-room roadmap for the current local-first build.
`VISION.md` remains the north star.
Use `docs/plans/` for detailed Compound Engineering implementation plans for a specific version or slice.

## Current State

- Version: V0 - Project Contract And Roadmap
- Active slice: V0.S1 docs and orchestration contract
- Active worker: none
- Implementation allowed: no
- Next action: run `compound-engineering:ce-brainstorm`

## Rules

- `PLAN.md` tracks project direction, version order, slice status, gates, and next action.
- `docs/brainstorms/` defines product intent.
- `docs/plans/` defines implementation boundaries for confirmed slices.
- Workers execute bounded slices.
- The orchestrator verifies, checkpoints, and starts the next slice.
- Workers are separate Codex project threads in the left sidebar, created with `codex_app.create_thread` when available.
- Do not use the right-side Subagents panel as the project worker-chat model.
- Default to serial worker execution.
- One worker owns one version slice, repo, or file scope at a time unless the owner explicitly approves parallel workers with disjoint ownership.
- Use a fresh worker chat for every new version or new slice.
- Reuse a worker chat only for same-slice follow-ups routed by the orchestrator.
- One worker must complete, block, stop, expire, or explicitly release its lease before the orchestrator may start the next worker.
- Worker ping-back is the primary completion signal.
- Workers must update `docs/handoffs/orchestrator.md` and report back to the main orchestrator chat only after clean final gates or a real blocker.
- The 10 minute watchdog heartbeat is backup inspection for missed ping-backs, stale leases, and blocked workers, and must verify repo state before acting.
- The timer wakes the orchestrator.
- The timer does not directly spawn workers.
- A worker is not complete until the worker thread has finished or reported blocked, handoff and registry are updated, final gates have passed or exact blockers are documented, autoreview is clean or routed, report-back happened when available, and `PLAN.md`, handoff, registry, worker thread status, git state, validation, and autoreview agree.
- Final gates include `npm run verify` when available, repo tests when available, smoke when available, package smoke when package or CLI behavior changed, `git diff --check`, `git diff --cached --check`, owner-doc punctuation scan, local autoreview, and behavior validation when applicable.
- Workers must not mark themselves `completed`, `accepted`, or `released`; they use `active`, `follow-up-needed`, `finalizing`, or `blocked`.
- The orchestrator may mark `reported` after ping-back and `accepted` or `released` after independent verification.
- Treat `finalizing` and `reported` as blocking states.
- Workers must label pending-gate handoff updates `Draft / Finalizing - not complete`.
- Workers must not use `Closeout`, `Final`, `Complete`, or `Completed` headings while gates, autoreview, handoff edits, registry edits, or report-back are pending.
- Worker report-back is one final action after clean final gates on the exact final repo bundle, or after a real blocker is documented.
- Never pair `completed` with final gates pending, autoreview pending, or report-back pending.
- Do not treat `autoreview can run` as `autoreview is clean`.
- Keep heartbeat wakeups active while the project has an active worker, pending verification, pending acceptance, or an approved automation loop.
- Workers do not commit by default.
- Workers may create local checkpoint commits only when their prompt explicitly grants worker commits for that slice.
- The orchestrator may create local checkpoint commits only after `npm run verify` when available, repo tests when available, smoke when available, package smoke when package or CLI behavior changed, `git diff --check`, `git diff --cached --check`, owner-doc punctuation scan, local autoreview, behavior validation when applicable, and handoff update pass.
- No push, PR, merge, close, hosted deployment, public webhook, release, publish, public comment, npm publish, GitHub release, tag push, Homebrew change, package publication, public announcement, paid API, credentials, cloud mutation, live connector mutation, or live-money integration without explicit owner approval for that exact item.
- Security scans can block later public, hosted, connector, package, and release lanes.
- Proof-generating versions or slices should use one canonical typed proof object and render all markdown, HTML, refusal, receipt, and summary views from that object.

## Autocomplete Contract

After the owner confirms an implementation roadmap, the approved project-completion loop should keep going until the roadmap is complete, blocked, or waiting on an explicit owner decision.

The control-room orchestrator should:

- inspect current repo state
- inspect handoff state
- inspect worker registry and lease state
- inspect the active worker thread when needed
- inspect the active worker thread before accepting, releasing, or replacing that worker
- route findings back to the active worker
- create exactly one bounded follow-up fixer when the original worker has reported back, blocked, or become unavailable
- verify worker output against the repo
- run `npm run verify` when available, repo tests when available, smoke when available, package smoke when package or CLI behavior changed, `git diff --check`, `git diff --cached --check`, owner-doc punctuation scan, local autoreview, behavior validation when applicable, and no-mistakes when configured and applicable
- create local checkpoint commits when clean and allowed
- start the next planned worker only when no active worker owns scope

## Skill Policy

Use skills deliberately, as gates or design aids, not as permission to sprawl.

- `no-mistakes`: use only after a real implementation checkpoint exists, the repo has been initialized for it, the work is committed, the branch is eligible, and the owner-approved validation path calls for it.
- Matt Pocock `domain-modeling`: use when durable domain vocabulary, ubiquitous language, or glossary terms change.
- Matt Pocock `codebase-design`: use when designing module interfaces, adapters, persistence, registries, or other deep codebase structure.
- Matt Pocock `prototype`: use for throwaway spikes that answer one question, then delete or absorb the answer.
- Matt Pocock `tdd`: use for behavior-first implementation of persistence, export, generation, state transitions, and other non-trivial behavior.
- Compound Engineering `ce-brainstorm`, `ce-plan`, and `ce-work`: keep the sequence requirements, plan, owner confirmation, implementation.
- Matt Pocock skills live at `/Users/praggy/Developer/agent-tools/mattpocock-skills/skills/engineering/<skill>/SKILL.md` when they are not installed in the active skill list.
- `behavior-validator`: use after autoreview when runnable user-visible or operator-visible behavior changed in UI, CLI, API, generated artifacts, or workflows.
- `define-goal`: use before large autonomous loops or fuzzy objectives when success evidence, stop condition, or owner-help condition is unclear.
- `handoff`: use for paste-ready continuation prompts, worker prompts, fresh-chat prompts, and cross-chat summaries.
- `agent-transcript`: use only for approved, redacted PR or issue body provenance from agent work.
- `security-threat-model`: recommend when auth, credentials, public APIs, hosted deployment, webhooks, payments, live connectors, multi-user state, or sensitive data enter scope, but run it only after explicit owner request.
- `security-best-practices`: use for explicit security review/report work or secure-by-default JS/TS, Python, or Go implementation work.
- `gh-fix-ci`: use for GitHub Actions PR failures after GitHub access and owner approval.
- `gh-address-comments`: use for GitHub PR comment follow-up after GitHub access is approved and the owner selects comments.

Do not claim a skill or gate ran unless the exact skill instructions were read and the exact command or artifact exists.

## Integration And Refactor Hygiene

- Every implementation slice must either wire into an existing user-visible path, operator command, API, or documented module interface, or explicitly mark itself as an isolated prototype.
- Do not leave parallel systems, orphan adapters, unused schemas, duplicate state stores, or dead prototype paths without recording a follow-up slice.
- After each accepted version, run a small integration review before starting the next version: entrypoints wired, types and tests aligned, docs updated, stale code removed or tracked, and architecture drift noted.
- Keep refactors scoped to the slice unless the refactor is the slice.
- If a cleanup crosses module ownership, changes public behavior, changes persistence shape, or affects multiple slices, promote it to a planned refactor slice with its own gates.
- Update `ARCHITECTURE.md` when module boundaries, data flow, runtime topology, persistence, or external integrations change.

## Optional Memory Capture

- Repo docs are the source of truth for current plan and execution state.
- GBrain may be used for optional cross-project recall and curated accepted-slice memory when `gbrain` is installed and healthy.
- Do not require GBrain to execute this plan.
- Do not import raw chats by default.
- After an accepted version or slice, capture only durable learning when safe and approved: phase or slice id, changed files, decisions, proof, failures, follow-ups, and reusable lesson.
- Never capture secrets, credentials, raw private data, sensitive user data, or public/private mutation logs without explicit approval.

## Integration Reflection Gate

Before accepting a completed slice, checkpointing, or expanding the next version, answer:

- Could this be better with a larger refactor?
- Now that this slice exists, what would we have done differently?
- What is the better long-term shape?
- Do we have enough tests?
- What documentation should be written or updated, and where should it live?
- What errors, warnings, or confusing source-code paths are visible now?
- What questions remain for Praggy?

Classify each answer as one of:

- Accept now
- Small cleanup
- Future refactor slice
- Needs owner decision
- Real blocker

If the answers reveal small cleanup inside the current worker scope, route it back before acceptance.
If the answers reveal larger cleanup, create a planned refactor slice instead of doing it opportunistically.
If the answers require product direction, credentials, public mutation, or expanded scope, ask Praggy.

## Version And Slice Execution Template

Use this structure for every executable version or implementation slice:

- Dependencies
- May start when
- Must not start when
- Ordered steps
- Worker goal
- Owned scope
- Forbidden scope
- Validation gates
- Checkpoint name
- Exit condition

The orchestrator may start only the next eligible version slice or step.
If `PLAN.md`, the worker registry, and `docs/handoffs/orchestrator.md` disagree, reconcile from actual repo state before spawning, checkpointing, or rotating.
If validation or autoreview finds an issue inside the current worker slice, route the exact finding back to that worker or one bounded follow-up fixer before starting the next version slice.

## Version Map

| Version | Goal | Input | Output | Gate | Status |
| --- | --- | --- | --- | --- | --- |
| V0 | Project contract and whole-roadmap planning | Project idea | Root docs, requirements, version map, orchestration policy | Owner accepts roadmap shape | In progress |
| V1 | Local useful MVP | V0 docs and owner confirmation | Smallest working product loop | Local smoke passes | Not started |
| V2 | Domain model and structured state | V1 prototype | Durable domain objects, schema, and round-trip tests | Model tests pass | Not started |
| V3 | Core interaction and UX workflow | V2 model | Main screens, workflows, and user-facing behavior | E2E or smoke proof passes | Not started |
| V4 | Worker prompt and proof engine | V3 workflow | Requirements, plan, QA, proof, and worker prompt exports | Generated brief can drive a bounded worker | Not started |
| V5 | Persistence, import, export, and recovery | V4 engine | Local files, import/export, backup or restore | File proof and migration checks pass | Not started |
| V6 | QA, security, and regression cockpit | V5 persistence | QA ledgers, security scan loop, visual or runtime checks | No critical workflow or security gaps | Not started |
| V7 | Supervised automation mode | V6 proof | 10 minute watchdog, worker registry, checkpoint loop | Dry-run automation proof passes | Not started |
| V8 | Optional ecosystem bridges | Stable local model | Approved connector or import/export candidates | New requirements and exact approval | Deferred |
| V9 | Personal daily-use or release candidate | V7 proven loop | Hardened private or release-ready tool and operating docs | Owner accepts daily use or release readiness | Deferred |

## Slice Backlog

| Slice | Goal | Owner | Dependencies | Files / Scope | Proof Required | Status |
| --- | --- | --- | --- | --- | --- | --- |
| V0.S1 | Finish docs-first scaffold and whole-roadmap planning | Orchestrator | None | Root docs, requirements, first plan, loop docs, templates | Docs present and owner decision requested | In progress |
| V1.S1 | Spike or scaffold first local MVP | Worker after owner confirmation | V0 | Isolated proof or app scaffold | Runnable prototype and answer captured | Not started |
| V1.S2 | First usable local workflow | Worker after V1.S1 | V1.S1 | App loop, state, smoke proof | Local smoke and `git diff --check` | Not started |
| V2.S1 | Domain model and schema | Worker after V1 | V1 accepted | Domain glossary, schema, round-trip tests | Tests and schema docs | Not started |

## Active Worker

- Worker thread: none
- Slice: none
- Lease expires: none
- State: none
- Last heartbeat: none

## Validation Gates

- Requirements exist before implementation planning.
- Active plan exists before implementation.
- Owner confirms the plan before `ce-work`.
- Worker handoff is updated before orchestrator review.
- Repo tests pass or exact blocker is documented.
- Smoke test passes or exact blocker is documented.
- Package smoke passes when package, CLI, or distribution behavior changed.
- `git diff --check` passes.
- `git diff --cached --check` passes.
- Owner-doc em dash and en dash scan passes over touched docs.
- Autoreview is clean or findings are routed back to the owning worker.
- Behavior validation passes when runnable behavior changed or exact blocker is documented.
- Security findings that block later public or release lanes are fixed, waived, or explicitly deferred by the owner.
- `no-mistakes` runs only after its preconditions are true: initialized repo, committed work, eligible feature branch, and owner-approved validation path.

## Stop Conditions

- Owner approval is required.
- Public mutation is required.
- Credentials, paid API, cloud mutation, or live-money scope is required.
- The same worker fails repeatedly.
- The active worker is stale and cannot be inspected.
- Ownership is ambiguous.
- Validation cannot be trusted.
- No approved next version slice exists.

## End Of Roadmap

If no approved next version slice exists, stop heartbeat wakeups instead of continuing to wake the thread.
Do not invent new versions or slices.
Add a new version or slice only after `PLAN.md` is updated with owner approval.

## Next

Use `docs/templates/fresh-control-room-prompt.md` to start or resume the control-room chat.
Use `docs/templates/worker-prompt.md` only when the orchestrator starts a bounded worker.
Use `docs/templates/periodic-heartbeat-prompt.md` for the 10 minute watchdog heartbeat.
Use the 10 minute heartbeat only as orchestrator inspection, not as direct worker execution.
