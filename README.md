# Elon Musk Methods

[![Validate](https://github.com/thepraggyverse/elon-musk/actions/workflows/validate.yml/badge.svg)](https://github.com/thepraggyverse/elon-musk/actions/workflows/validate.yml)

`elon-musk` is a skill plugin for applying book-derived Elon Musk method patterns to strategy, engineering, teams, risk, company building, and execution.

It ships 15 searchable `x-*` skills. Use the router when you are unsure which method fits, or call a specific skill when you already know the lens.

```text
Use $x-router on this project idea.
Use $x-5-step-algo on this feature plan.
Use $x-org and $x-teams on this blocked team workflow.
Use $x-risk on this AI launch plan.
```

The skills are paraphrased operating methods. They are not a quote archive and they do not include the book text.

## Skill Loop

For broad work, start here:

```text
x-router -> selected method -> concrete review -> reusable lesson
```

Common routes:

| Situation | Useful sequence |
|---|---|
| New product or startup idea | `x-purpose -> x-thinking -> x-company-building` |
| Feature or workflow before building | `x-5-step-algo -> x-engineering -> x-urgency` |
| Slow organization or blocked project | `x-org -> x-teams -> x-urgency` |
| Production or delivery bottleneck | `x-manufacturing -> x-engineering -> x-5-step-algo` |
| Risky AI or infrastructure launch | `x-risk -> x-thinking -> x-company-building` |
| Moonshot or long-horizon mission | `x-multiplanetary -> x-risk -> x-company-building` |

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
| `x-router` | Chooses the best method lens. | The request is broad or messy. |
| `x-purpose` | Tests usefulness, ambition, and sustained effort. | Choosing projects, missions, product bets, or career bets. |
| `x-thinking` | Improves reasoning quality. | Strategy, architecture, impossible claims, expensive claims. |
| `x-engineering` | Finds where engineering creates real value. | Technical strategy, build-vs-buy, product architecture. |
| `x-5-step-algo` | Questions, deletes, simplifies, accelerates, then automates. | Feature specs, workflows, migrations, refactors, automations. |
| `x-teams` | Reviews talent density, ownership, and builder culture. | Hiring, founding teams, performance, team health. |
| `x-org` | Removes organizational drag. | Meetings, approvals, cross-team work, unclear ownership. |
| `x-urgency` | Shortens timelines and feedback loops. | Launches, blocked projects, roadmaps, crisis work. |
| `x-manufacturing` | Treats production and delivery as the product. | Operations, CI/CD, support, fulfillment, physical production. |
| `x-founder` | Tests conviction, pain tolerance, and all-in decisions. | Startup commitment, pivots, runway, hard personal bets. |
| `x-company-building` | Turns mission into prototype, survival, sequence, and scale. | Startup roadmaps, product strategy, capital allocation. |
| `x-future` | Applies abundance, AI, robotics, autonomy, and energy lenses. | Long-term technology bets and future-state planning. |
| `x-risk` | Reviews systemic and civilization-scale downside. | AI systems, safety, infrastructure, policy, broad downside. |
| `x-multiplanetary` | Turns moonshots into staged milestones. | Deep-tech, resilience, infrastructure, long-horizon missions. |
| `x-reading` | Recommends books by problem type. | Learning paths for engineering, history, AI, strategy, science. |

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
python3 scripts/install_local.py --symlink-skills
```

Default homes:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

See `docs/HARNESS_MATRIX.md`, `docs/INSTALL.md`, and `docs/SYMLINKS.md`.

## Updating

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
```

Start a new Codex or Claude thread after reinstalling so the updated skills are loaded.

## Repository Layout

```text
elon-musk/
  AGENTS.md                   authoring rules for this repo
  CLAUDE.md                   Claude-compatible pointer to AGENTS.md
  .codex-plugin/plugin.json   native Codex plugin manifest
  .claude-plugin/             Claude-compatible plugin metadata
  .agents/plugins/            repo-local Codex marketplace metadata
  skills/                     15 x-prefixed skills
  references/                 book map, method catalog, source notes
  examples/                   practical prompt examples
  docs/                       install, harness, usage, audit, source boundaries
  scripts/install_local.py    marketplace and skill symlink installer
  scripts/validate_public.py  public repository validator
  tests/                      unit tests for structure and install assumptions
```

## Documentation

| File | Purpose |
|---|---|
| `AGENTS.md` | Maintainer and agent instructions for this repo. |
| `CONCEPTS.md` | Plugin philosophy, workflow, and method families. |
| `docs/HARNESS_MATRIX.md` | Harness Matrix for install, update, uninstall, and compatibility notes. |
| `docs/REFERENCE_AUDIT.md` | What was audited from the reference projects and what changed here. |
| `docs/COMPOUND_ENGINEERING.md` | How Compound Engineering ideas shaped the plugin packaging. |
| `docs/INSTALL.md` | Detailed local install and update paths. |
| `docs/SYMLINKS.md` | How plugin and skill symlinks work. |
| `docs/USAGE.md` | More examples and prompt recipes. |
| `docs/DEVELOPMENT.md` | Maintainer workflow. |
| `docs/SOURCE_BOUNDARIES.md` | Copyright and source-use boundaries. |
| `references/book-map.md` | Maps book sections to skills. |
| `references/method-catalog.md` | Full merged method catalog. |
| `references/source-notes.md` | Source-use guardrails. |

## Validate

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

The public validator checks:

| Area | Check |
|---|---|
| Plugin manifests | Codex, Claude-compatible, and repo-local marketplace metadata exist and parse. |
| Skills | Exactly 15 `x-*` skills with matching frontmatter and UI metadata. |
| Docs | README, AGENTS, install, usage, harness, audit, symlink, source-boundary, and CI files exist. |
| References | Catalog and book map cover every non-router skill. |
| Hygiene | Placeholder text and non-ASCII drift are rejected. |

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

See `docs/SOURCE_BOUNDARIES.md`.

## Disclaimer

This is an independent educational and productivity project. It is not affiliated with, endorsed by, sponsored by, or connected to Elon Musk, Eric Jorgenson, ElonMuskBook.org, Tesla, SpaceX, X, xAI, Neuralink, The Boring Company, or any publisher/rightsholder.

"Elon Musk" is used descriptively to identify the inspiration for the operating patterns.

## License

MIT. See `LICENSE`.
