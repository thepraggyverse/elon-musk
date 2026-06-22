# Elon Musk Methods

[![Validate](https://github.com/thepraggyverse/elon-musk/actions/workflows/validate.yml/badge.svg)](https://github.com/thepraggyverse/elon-musk/actions/workflows/validate.yml)

Book-derived `x-*` skills for applying Elon Musk-style operating methods to useful work, engineering, teams, company-building, risk, and moonshot execution.

This is an unofficial Codex plugin. It is not a quote dump and it does not include the full text of *The Book of Elon*. It packages paraphrased, reusable methods into small agent skills.

## Philosophy

The point is not to imitate a person. The point is to preserve reusable moves:

- Choose work that is useful and future-oriented.
- Reason from reality, not analogy.
- Question requirements before accepting them.
- Delete before optimizing.
- Treat engineering and production as the value engine.
- Build teams that can face bad news and still ship.
- Move fast only after the direction is valid.
- Make companies, systems, and missions resilient enough to survive hard phases.

The plugin uses a merged structure: many book ideas are preserved, but only 15 top-level skills appear in search. Smaller ideas live as subsections and in `references/method-catalog.md`.

## Workflow

Start with the router when the situation is broad:

```text
Use $x-router on this startup idea and pick the right Elon Musk methods.
```

Then apply one or two specific methods:

```text
Use $x-purpose to decide whether this project is worth doing.
Use $x-thinking to separate facts from assumptions.
Use $x-5-step-algo to question, delete, simplify, accelerate, and automate.
```

For product or engineering work, a typical loop is:

```text
x-purpose -> x-thinking -> x-5-step-algo -> x-engineering -> x-urgency
```

For company-building:

```text
x-purpose -> x-founder -> x-company-building -> x-teams -> x-manufacturing
```

For high-risk or moonshot work:

```text
x-thinking -> x-risk -> x-multiplanetary -> x-company-building
```

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

Expected output:

| Area | What to inspect |
|---|---|
| Ownership | Who can actually decide? |
| Communication | Which handoffs can become direct owner-to-owner loops? |
| Risk | Which approvals prevent real harm? |
| Culture | Is the team building, waiting, hiding, or debating reality? |

## Full Skill Inventory

| Skill | Purpose | Use When |
|---|---|---|
| `x-router` | Choose the right method lens. | The request is broad or messy. |
| `x-purpose` | Decide if work is useful, ambitious, and worth sustained effort. | Project selection, product bets, career bets, mission checks. |
| `x-thinking` | Improve reasoning quality. | Strategy, architecture, impossible claims, expensive claims. |
| `x-engineering` | Find where engineering creates real value. | Technical strategy, product architecture, build-vs-buy. |
| `x-5-step-algo` | Question, delete, simplify, accelerate, automate. | Feature specs, workflows, automations, migrations, refactors. |
| `x-teams` | Review talent density and builder culture. | Hiring, founding teams, performance, team health. |
| `x-org` | Remove organizational drag. | Meetings, approvals, cross-team work, unclear ownership. |
| `x-urgency` | Shorten timelines and feedback loops. | Launches, blocked projects, roadmaps, crisis work. |
| `x-manufacturing` | Treat production as the product. | Operations, CI/CD, support, fulfillment, physical production. |
| `x-founder` | Test conviction, pain tolerance, and all-in decisions. | Startup commitment, pivots, runway, hard personal bets. |
| `x-company-building` | Turn mission into prototype, survival, sequence, and scale. | Startup roadmaps, product strategy, capital allocation. |
| `x-future` | Apply abundance, AI, robotics, autonomy, and energy lenses. | Long-term technology bets and future-state planning. |
| `x-risk` | Review systemic and civilization-scale downside. | AI systems, safety, infrastructure, policy, broad downside. |
| `x-multiplanetary` | Turn moonshots into staged milestones. | Deep-tech, resilience, infrastructure, long-horizon missions. |
| `x-reading` | Recommend books by problem type. | Learning paths for engineering, history, AI, strategy, science. |

## Merged Method Map

| Top-Level Skill | Merged Methods |
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

## What You Get

```text
elon-musk/
  .codex-plugin/plugin.json
  skills/                     15 x-prefixed skills
  references/                 book map, method catalog, source notes
  examples/                   practical prompt examples
  docs/                       install, symlinks, usage, development, source boundaries
  scripts/install_local.py    marketplace and skill symlink installer
  scripts/validate_public.py  public repository validator
  tests/                      unit tests for structure and install assumptions
```

## Install

### Codex Plugin

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/elon-musk.git ~/plugins/elon-musk
cd ~/plugins/elon-musk
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
```

Verify:

```bash
codex plugin list | grep elon-musk
```

Expected:

```text
elon-musk@personal   installed, enabled  0.1.0    /Users/<you>/plugins/elon-musk
```

### Direct Skill Symlinks

```bash
python3 scripts/install_local.py --symlink-skills
```

Default skill homes:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

See `docs/INSTALL.md` and `docs/SYMLINKS.md`.

## Install Matrix

| Host | Path |
|---|---|
| Codex plugin | `python3 scripts/install_local.py --marketplace` then `codex plugin add elon-musk@personal` |
| Codex loose skills | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.codex/skills` |
| Claude Code loose skills | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.claude/skills` |
| Shared `.agents` home | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.agents/skills` |
| OpenClaw skills | `python3 scripts/install_local.py --symlink-skills --skill-home ~/.openclaw/skills` |

## Documentation

| File | Purpose |
|---|---|
| `CONCEPTS.md` | Plugin philosophy, workflow, and method families. |
| `docs/COMPOUND_ENGINEERING.md` | How Compound Engineering ideas shaped the plugin packaging. |
| `docs/INSTALL.md` | Detailed install and update paths. |
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
| Plugin | Manifest exists, parses, and points to `./skills/`. |
| Skills | Exactly 15 `x-*` skills with matching frontmatter and UI metadata. |
| Docs | Required README, install, usage, symlink, source-boundary, and CI files exist. |
| References | Catalog and book map cover every non-router skill. |
| Hygiene | Placeholder text and non-ASCII drift are rejected. |

## Updating

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
```

Start a new Codex thread after reinstalling so the updated skills are loaded.

## Design References

This repo follows the same broad plugin-as-product pattern as:

- https://github.com/mattpocock/skills
- https://github.com/EveryInc/compound-engineering-plugin
- https://github.com/EveryInc/compound-knowledge-plugin
- https://github.com/steipete/agent-scripts/tree/main/skills

Compound Engineering is especially useful as a reference because it presents a clear philosophy, workflow, skill-purpose inventory, quick examples, install paths across multiple agent hosts, and a "make the system learn" step after each cycle.

See `docs/COMPOUND_ENGINEERING.md` for the exact ideas borrowed for this plugin's packaging.

## Source Boundaries

This repository contains paraphrased operating methods, workflows, and metadata. It does not contain the full text of *The Book of Elon*, long excerpts, transcripts, EPUB files, or extracted chapters.

See `docs/SOURCE_BOUNDARIES.md`.

## Disclaimer

This is an unofficial educational and productivity project. It is not affiliated with, endorsed by, sponsored by, or connected to Elon Musk, Eric Jorgenson, ElonMuskBook.org, Tesla, SpaceX, X, xAI, Neuralink, The Boring Company, or any publisher/rightsholder.

"Elon Musk" is used descriptively to identify the inspiration for the operating patterns.

## License

MIT. See `LICENSE`.
