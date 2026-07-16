# Elon Musk Methods

[![Validate](https://github.com/thepraggyverse/elon-musk/actions/workflows/validate.yml/badge.svg)](https://github.com/thepraggyverse/elon-musk/actions/workflows/validate.yml)

`elon-musk` is a skill plugin for applying book-derived Elon Musk method patterns to strategy, engineering, teams, risk, company building, execution, and reusable learning.

It ships 20 searchable `x-*` skills: 14 book-derived method lenses, 1 router, and 5 workflow skills for setup, review packs, compounding lessons, memory refresh, and writing handoffs. Use `x-setup` when checking installation, `x-review-pack` when you want the whole loop, the router when you are unsure which method fits, or a specific skill when you already know the lens.

```text
Use $x-setup to check whether the plugin is installed and visible.
Use $x-review-pack to review this launch plan and close the loop.
Use $x-router on this project idea.
Use $x-5-step-algo on this feature plan.
Use $x-org and $x-teams on this blocked team workflow.
Use $x-risk on this AI launch plan.
Use $x-compound to save the reusable lesson from this review.
```

The skills are paraphrased operating methods. They are not a quote archive and they do not include the book text.
Direct, near-primary, book-derived, and original plugin material are separated in `docs/SOURCES.md`.

## Skill Loop

For broad work, start here:

```text
x-router -> selected method -> concrete review -> reusable lesson
x-review-pack -> route -> review -> compound candidate -> handoff decision
```

Common routes:

| Situation | Useful sequence |
|---|---|
| Check install or skill visibility | `x-setup` |
| Full close-the-loop review | `x-review-pack` |
| New product or startup idea | `x-purpose -> x-thinking -> x-company-building` |
| Feature or workflow before building | `x-5-step-algo -> x-engineering -> x-urgency` |
| Slow organization or blocked project | `x-org -> x-teams -> x-urgency` |
| Production or delivery bottleneck | `x-manufacturing -> x-engineering -> x-5-step-algo` |
| Risky AI or infrastructure launch | `x-risk -> x-thinking -> x-company-building` |
| Moonshot or long-horizon mission | `x-multiplanetary -> x-risk -> x-company-building` |
| Save what a review taught you | `x-compound` |
| Refresh stale or duplicate saved lessons | `x-memory-refresh` |
| Continue a long review later | `x-handoff` |

## Quick Examples

### Feature Before Building

```text
Use $x-5-step-algo on this feature plan:
We want a team dashboard with daily KPIs, Slack alerts, CSV export, role-based permissions, and scheduled email digests.
```

Expected lens:

| Step | Question |
|---|---|
| Question | Which requirements have named owners and evidence? |
| Delete | Which alerts, exports, permissions, or digests can be removed? |
| Simplify | What is the smallest useful dashboard? |
| Accelerate | What can be tested this week? |
| Automate | What should stay manual until the process is proven? |

### Startup Idea

```text
Use $x-router on this startup idea:
A local-first AI research assistant for founders that keeps private notes, runs weekly reviews, and suggests next bets.
```

Likely route:

| Role | Skill | Why |
|---|---|---|
| Primary | `x-purpose` | Decide whether the work is useful and worth pain. |
| Support | `x-thinking` | Separate real constraints from copied assumptions. |
| Support | `x-company-building` | Turn the mission into prototype, sequence, and survival path. |

### Stuck Team

```text
Use $x-org and $x-teams on this blocked project:
Engineering waits for Product, Product waits for Legal, Legal waits for Security, and nobody can name the final owner.
```

Expected lens:

| Area | What to inspect |
|---|---|
| Ownership | Who can actually decide? |
| Communication | Which handoffs can become direct owner-to-owner loops? |
| Risk | Which approvals prevent real harm? |
| Culture | Is the team building, waiting, hiding, or debating reality? |

## Skill Inventory

| Skill | What it does | Use when |
|---|---|---|
| `x-setup` | Checks plugin install state, cache, symlinks, and prompt visibility. | Setup, update, or skill discoverability looks wrong. |
| `x-router` | Chooses the best method or workflow skill. | The request is broad, messy, or spans several method families. |
| `x-review-pack` | Runs routing, method review, compound candidates, and handoff closeout. | A plan needs a complete close-the-loop review. |
| `x-purpose` | Tests usefulness, ambition, originality, and sustained effort. | Choosing projects, missions, product bets, or career bets. |
| `x-thinking` | Improves reasoning through facts, direct sources, first principles, limits, and updates. | Strategy, architecture, impossible claims, expensive claims, or inherited assumptions. |
| `x-engineering` | Finds engineering leverage using ideal limits, cost structure, integration, and product taste. | Technical strategy, build-vs-buy, architecture, cost, design, or engineering leadership. |
| `x-5-step-algo` | Questions, deletes, simplifies, accelerates, then automates. | Feature specs, workflows, migrations, refactors, automations. |
| `x-teams` | Reviews talent, ownership, builder culture, feedback, and fair people-process boundaries. | Hiring, founding teams, performance, team health, or consequential people decisions. |
| `x-org` | Removes organizational drag while preserving controls that protect real risks. | Meetings, approvals, cross-team work, communication, or unclear ownership. |
| `x-urgency` | Shortens timelines and feedback loops after direction and safety boundaries are valid. | Launches, blocked projects, roadmaps, migrations, or crisis work. |
| `x-manufacturing` | Treats production and delivery as the product and attacks the throughput constraint. | Operations, CI/CD, support, fulfillment, data pipelines, or physical production. |
| `x-founder` | Tests conviction, responsibility, runway, protected constraints, and commitment level. | Startup commitment, pivots, runway, leadership, or hard personal bets. |
| `x-company-building` | Turns mission into prototype, proof, survival, sequence, trust, and scale. | Startup roadmaps, product strategy, capital allocation, launches, or customer trust. |
| `x-future` | Applies abundance, emerging possibility, AI, robotics, autonomy, interfaces, and energy lenses. | Long-term technology bets, future-state planning, automation, robotics, or energy ideas. |
| `x-risk` | Reviews systemic downside, affected parties, controls, release gates, and stop conditions. | AI systems, safety, infrastructure, policy, compliance, or plans with broad downside. |
| `x-multiplanetary` | Turns moonshots into staged milestones. | Deep-tech, resilience, infrastructure, long-horizon missions. |
| `x-reading` | Builds source-labeled reading paths by problem type and learning goal. | Learning engineering, rockets, history, AI, strategy, science, economics, or worldview. |
| `x-compound` | Saves explicitly authorized lessons and reviews as local Markdown memory. | A completed method session produced learning that should guide future work. |
| `x-memory-refresh` | Audits local lessons and reviews for stale, duplicate, unsafe, or weakly retrievable memory. | Saved method memory has accumulated and needs pruning or reconciliation. |
| `x-handoff` | Writes a redacted continuation handoff. | Long reviews, context transitions, or next-session briefs. |

The generated long-form index lives in `docs/SKILL_INDEX.md`; run `python3 scripts/build_index.py` after changing skill metadata.

## Merged Method Map

| Top-level skill | Merged methods |
|---|---|
| `x-purpose` | be useful, fight for the future, start before ready, create more than consume, work like hell, fear |
| `x-thinking` | truth calibration, first principles, thinking in limits, less wrong, direct source |
| `x-engineering` | engineering creates value, engineering magic, engineering wins, chief engineer mindset, good taste |
| `x-5-step-algo` | question, delete, simplify, accelerate, automate, overdelete/addback |
| `x-teams` | exceptional ability, special forces, builder culture, feedback over feelings |
| `x-org` | direct communication, remove boundaries, simple language, permission to fail, legacy rule expiry |
| `x-urgency` | do not waste time, parallel work, impossible breakdown, aggressive timelines, one key scoreboard |
| `x-manufacturing` | make stuff, factory as product, attack constraint, supplier bottlenecks, manufacturing moat |
| `x-founder` | all-in conviction, adversity, eat glass, courage under uncertainty, runway |
| `x-company-building` | prototypes, sequencing, public reality, more for less, survival runway, anchor trust |
| `x-future` | abundance, AI, robotics, sustainable energy, human-machine upgrades, autonomy transition |
| `x-risk` | AI risk, population, regulation drag, war, energy, asteroids |
| `x-multiplanetary` | Mars roadmap, civilization backup, gateway milestones, long-horizon execution |
| `x-reading` | fiction, science, engineering, history, AI, business |

## Workflow Skill Map

| Workflow skill | What it adds |
|---|---|
| `x-setup` | Checks installed-state, direct skill homes, Codex cache, and prompt-visible workflow sentinels. |
| `x-review-pack` | Runs the bounded full loop: route, primary review, support checks, compound candidates, and handoff decision. |
| `x-compound` | Turns a finished method session into 1-3 approved local Markdown notes under `docs/reviews/` or `docs/lessons/`. |
| `x-memory-refresh` | Audits accumulated local notes for duplicates, stale claims, missing retrieval triggers, and unsafe saved content. |
| `x-handoff` | Writes a compact redacted handoff to OS temp by default, with suggested next skills and exact next actions. |

## Compatibility Quick Scan

| Skill | Output artifact | Writes files? | Safe default? |
|---|---|---|---|
| `x-setup` | Install and visibility diagnosis | No | Yes |
| `x-router` | Skill route and prompt | No | Yes |
| `x-review-pack` | Route, review, compound candidates, and handoff decision | Only with explicit write authorization | Yes |
| `x-purpose` | Project or mission review | No | Yes |
| `x-thinking` | Assumption and reasoning review | No | Yes |
| `x-engineering` | Engineering leverage review | No | Yes |
| `x-5-step-algo` | Requirement deletion and simplification plan | No | Yes |
| `x-teams` | Team capability and ownership review | No | Yes |
| `x-org` | Organization drag review | No | Yes |
| `x-urgency` | Timeline compression plan | No | Yes |
| `x-manufacturing` | Production path and bottleneck review | No | Yes |
| `x-founder` | Founder commitment review | No | Yes |
| `x-company-building` | Prototype, sequence, and survival plan | No | Yes |
| `x-future` | Future-state opportunity review | No | Yes |
| `x-risk` | Risk map and release gates | No | Yes |
| `x-multiplanetary` | Moonshot milestone plan | No | Yes |
| `x-reading` | Reading path by problem type | No | Yes |
| `x-compound` | Authorized Markdown lesson or review | Only with explicit write authorization | Yes |
| `x-memory-refresh` | Memory audit with proposed or authorized edits | Only with explicit write authorization | Yes |
| `x-handoff` | Redacted continuation note | Temp by default | Yes |

## Install

### Codex, Local Personal Plugin

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/elon-musk.git ~/plugins/elon-musk
cd ~/plugins/elon-musk
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
```

### Codex App, Custom Marketplace

In the Codex app, add this repository as a plugin marketplace:

| Field | Value |
|---|---|
| Source | `thepraggyverse/elon-musk` |
| Git ref | `main` |
| Sparse paths | leave blank |

Install `elon-musk`, then restart Codex so the skills reload.

### Claude Code

Use the Claude-compatible plugin metadata:

```text
/plugin marketplace add thepraggyverse/elon-musk
/plugin install elon-musk
```

For local development from a checkout:

```bash
claude --plugin-dir "$PWD"
```

### Loose Skill Homes

For harnesses that read `SKILL.md` folders directly:

```bash
python3 scripts/install_local.py --symlink-skills --profile openclaw
```

Other profiles:

```text
agents, codex, claude, openclaw-codex
```

Use `--profile all` only when every supported skill home is intentional.

See `docs/HARNESS_MATRIX.md`, `docs/INSTALL.md`, and `docs/SYMLINKS.md`.

## Updating

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
```

Start a new Codex or Claude thread after reinstalling so the updated skills are loaded.

## Repository Layout

```text
elon-musk/
  AGENTS.md                   authoring rules for this repo
  CLAUDE.md                   Claude-compatible pointer to AGENTS.md
  CHANGELOG.md                user-facing change history
  .codex-plugin/plugin.json   native Codex plugin manifest
  .claude-plugin/             Claude-compatible plugin metadata
  .agents/plugins/            repo-local Codex marketplace metadata
  skills/                     20 x-prefixed skills
  references/                 book map, method catalog, source notes
  examples/                   practical prompt examples, including all-skills.md
  docs/                       install, harness, usage, audit, source boundaries
  docs/SKILL_INDEX.md         generated skill index and compatibility table
  scripts/build_index.py      generator for skill index and examples
  scripts/check_install.py    installed-state checker for cache and symlinks
  scripts/run_behavior_smoke.py source-blind fixture validator and optional live runner
  scripts/install_local.py    marketplace and skill symlink installer
  scripts/uninstall_local.py  targeted safe removal of this checkout's links
  scripts/validate_public.py  public repository validator
  tests/                      unit tests for structure and install assumptions
```

## Documentation

| File | Purpose |
|---|---|
| `AGENTS.md` | Maintainer and agent instructions for this repo. |
| `CHANGELOG.md` | User-facing change history and unreleased notes. |
| `CONCEPTS.md` | Plugin philosophy, workflow, and method families. |
| `docs/MEMORY_MODEL.md` | Local Markdown memory model for reviews, lessons, and handoffs. |
| `docs/NATIVE_HARNESS_BRIDGES.md` | Lightweight bridge files for Cursor, Continue, Goose, OpenCode, and Gemini. |
| `docs/DOCUMENTATION_AUDIT.md` | Documentation-surface comparison against the reference repos. |
| `docs/HARNESS_MATRIX.md` | Harness Matrix for install, update, uninstall, and compatibility notes. |
| `docs/REFERENCE_AUDIT.md` | What was audited from the reference projects and what changed here. |
| `docs/COMPOUND_ENGINEERING.md` | How Compound Engineering ideas shaped the plugin packaging. |
| `docs/INSTALL.md` | Detailed local install and update paths. |
| `docs/RELEASE.md` | Version, changelog, release, and no-push checklist. |
| `docs/SKILL_INDEX.md` | Generated skill inventory, workflow map, and compatibility table. |
| `docs/SYMLINKS.md` | How plugin and skill symlinks work. |
| `docs/USAGE.md` | More examples and prompt recipes. |
| `docs/DEVELOPMENT.md` | Maintainer workflow. |
| `docs/SOURCE_BOUNDARIES.md` | Copyright and source-use boundaries. |
| `docs/SOURCES.md` | Public source bibliography and attribution-strength ledger. |
| `SECURITY.md` | Private vulnerability reporting and security scope. |
| `PRIVACY.md` | Local data-handling and memory boundaries. |
| `references/book-map.md` | Maps book sections to skills. |
| `references/method-catalog.md` | Full merged method catalog. |
| `references/CORE_METHODS.md` | Generated human-readable map of all 69 paraphrased core methods. |
| `references/source-notes.md` | Source-use guardrails. |

## Validate

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 scripts/run_behavior_smoke.py
```

The public validator checks:

| Area | Check |
|---|---|
| Plugin manifests | Codex, Claude-compatible, and repo-local marketplace metadata exist and parse. |
| Skills | Exactly 20 `x-*` skills with matching frontmatter and UI metadata. |
| Docs | README, changelog, security, privacy, AGENTS, install, usage, harness, generated index, audit, symlink, source-boundary, and CI files exist. |
| References | Canonical taxonomy, book map, all 69 core-method anchors, and bundled reading bibliography are validated. |
| Hygiene | Placeholder text and non-ASCII drift are rejected. |
| Behavior contracts | Source-blind fixtures cover routing, review, algorithm order, people decisions, founder constraints, stop-worthy risk, and attribution. |

Optional live smoke tests run selected fixtures in fresh harness processes:

```bash
python3 scripts/run_behavior_smoke.py --harness codex --fixture team-decision-fair-process
python3 scripts/run_behavior_smoke.py --harness claude --fixture risk-do-not-proceed
python3 scripts/run_behavior_smoke.py --harness codex --invoke-mode named --fixture review-pack-stop-check
```

Path mode validates skill behavior even in crowded harness profiles.
Named mode separately validates whether the harness can discover `$x-*` by name.

## Loaded Skill Check

After install, a fresh Codex process should be able to see the plugin cache:

```bash
python3 scripts/check_install.py
codex plugin list | grep 'elon-musk@personal'
find ~/.codex/plugins/cache/personal/elon-musk/0.2.0/skills -maxdepth 2 -name SKILL.md | wc -l
```

To also check model-visible skill loading:

```bash
python3 scripts/check_install.py --prompt-input
```

If you also installed loose skill symlinks:

```bash
python3 scripts/check_install.py --plugin --skill-links --profile all
```

If the prompt-input check warns that `x-setup`, `x-compound`, or `x-handoff`
are not visible, your global skill inventory may be over the Codex skill prompt budget.
The installed cache can still be valid, but automatic `x-*` invocation is
unreliable until unused plugins/skill roots are disabled or a slim Codex profile
is used.

## Design References

This repo follows the broad plugin-as-product pattern from:

- https://every.to/guides/compound-engineering
- https://github.com/EveryInc/compound-engineering-plugin
- https://github.com/EveryInc/compound-knowledge-plugin
- https://github.com/mattpocock/skills
- https://github.com/steipete/agent-scripts/tree/main/skills

See `docs/REFERENCE_AUDIT.md` for the detailed gap list and decisions.

## Source Boundaries

This repository contains paraphrased operating methods, workflows, and metadata. It does not contain the full text of *The Book of Elon*, long excerpts, transcripts, EPUB files, or extracted chapters.

See `docs/SOURCE_BOUNDARIES.md` and `docs/SOURCES.md`.

## Disclaimer

This is an independent educational and productivity project. It is not affiliated with, endorsed by, sponsored by, or connected to Elon Musk, Eric Jorgenson, ElonMuskBook.org, Tesla, SpaceX, X, xAI, Neuralink, The Boring Company, or any publisher/rightsholder.

"Elon Musk" is used descriptively to identify the inspiration for the operating patterns.

## License

MIT. See `LICENSE`.

<!-- BEGIN PRAGGY PROJECT DOCS -->
## Project Docs

This repo uses a docs-first agent contract:

- `README.md` explains the current project, commands, and how to run it.
- `AGENTS.md` defines the rules future agents must obey.
- `VISION.md` captures long-term direction, not implementation permission.
- `PLAN.md` tracks the full project roadmap from start to end as versions, slices, gates, active worker state, and next action.
- `OPINIONS.md` captures durable project taste, vocabulary, and tradeoffs.
- `MEMORY.md` captures stable project facts agents should not rediscover.
- `VOICE.md` captures communication defaults and owner-voice rules.
- `DESIGN.md` guides UI and UX decisions when the project has user-facing surfaces.
- `docs/handoffs/orchestrator.md` is the control-room state for continuation.
- `docs/handoffs/worker-brief.md` is the bounded scout/ship worker brief.
- `docs/brainstorms/` stores requirements and product-shape decisions.
- `docs/plans/` stores implementation plans.
- `docs/loops/` stores repeatable agent procedures.
- `docs/templates/` stores reusable control-room, worker, heartbeat, and template-builder prompts.
- `docs/qa/` stores feature, test case, defect, and regression ledgers.

Use a V0...Vn version map in `PLAN.md`.
Expand only the next eligible version or slice before starting a worker.
The default approved watchdog cadence is 10 minutes.
The timer wakes the orchestrator; it does not directly spawn workers.

GStack and GBrain are optional local helpers, not required project dependencies.
Use gstack as workflow and skill guidance when installed.
Use GBrain as searchable long-term memory when gbrain is installed and healthy.
Repo docs remain the source of truth for current project state.
Do not import raw chats by default.
Prefer curated GBrain captures after accepted slices, owner decisions, failure postmortems, major handoffs, and release/readiness milestones.
Never sync secrets, credentials, raw private data, public mutation logs, or sensitive runtime data without explicit approval.

Vision ideas must become requirements, then a plan, then receive owner confirmation before implementation.
<!-- END PRAGGY PROJECT DOCS -->
