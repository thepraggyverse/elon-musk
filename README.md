# Elon Musk Methods

`elon-musk` is an unofficial Codex plugin that turns major method ideas from *The Book of Elon* into a compact set of searchable `x-` prefixed skills.

It is not a quote dump and it does not include the full book text. It is a practical operating-method pack for applying book-derived ideas to product work, engineering, teams, company-building, risk review, long-horizon planning, and learning.

## What Is Included

- 15 top-level `x-*` skills.
- A router skill, `x-router`, for broad "use Elon Musk methods on this" prompts.
- Merged skills with subsections so the full idea set is preserved without creating dozens of tiny skills.
- Book and method references:
  - `references/book-map.md`
  - `references/method-catalog.md`
  - `references/source-notes.md`
- Example prompts in `examples/`.
- Public install, symlink, validation, and development docs.
- Local install scripts for Codex plugin registration and multi-agent skill-home symlinks.
- Unit tests and public validation scripts.

## Why `x-`

Every skill starts with `x-` so it is easy to search and easy to distinguish from other local skill packs.

Examples:

```text
Use x-router on this project idea.
Use x-5-step-algo on this feature plan.
Use x-manufacturing on this delivery pipeline.
```

## Quick Start

Clone into the conventional personal plugin folder:

```bash
mkdir -p ~/plugins
git clone https://github.com/thepraggyverse/elon-musk.git ~/plugins/elon-musk
cd ~/plugins/elon-musk
```

Register with the default personal Codex marketplace:

```bash
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
```

Validate:

```bash
python3 scripts/validate_public.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Then start a new Codex thread and try:

```text
Use $x-router to choose the right Elon Musk method for this project.
```

## Install Options

### Option 1: Codex Plugin

Use this when you want the plugin visible through Codex plugin management:

```bash
python3 scripts/install_local.py --marketplace
codex plugin add elon-musk@personal
```

The installer updates:

```text
~/.agents/plugins/marketplace.json
```

with:

```json
{
  "name": "elon-musk",
  "source": {
    "source": "local",
    "path": "./plugins/elon-musk"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

If the repo is not already located at `~/plugins/elon-musk`, the installer creates:

```text
~/plugins/elon-musk -> /path/to/your/clone
```

This symlink is important because the personal marketplace root is `~`, so `./plugins/elon-musk` resolves to `~/plugins/elon-musk`.

### Option 2: Direct Skill Symlinks

Use this when an agent reads loose `SKILL.md` folders directly:

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

Each target receives symlinks like:

```text
~/.codex/skills/x-router -> ~/plugins/elon-musk/skills/x-router
~/.codex/skills/x-5-step-algo -> ~/plugins/elon-musk/skills/x-5-step-algo
```

### Option 3: Plugin Plus Skill Symlinks

```bash
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
```

Use this if you want Codex plugin visibility and direct skill exposure for other harnesses.

See:

- `docs/INSTALL.md`
- `docs/SYMLINKS.md`
- `docs/DEVELOPMENT.md`
- `docs/SOURCE_BOUNDARIES.md`

## Skill Map

| Skill | What it does | Unmerged methods inside | Example use |
|---|---|---|---|
| `x-router` | Chooses the right method lens. | all method families | "Which Elon Musk method should I use here?" |
| `x-purpose` | Decides if work is useful, ambitious, and worth the pain. | be useful, fight for the future, start before ready, create more than consume, work like hell, fear | "Is this app worth building?" |
| `x-thinking` | Improves reasoning quality. | truth calibration, first principles, thinking in limits, less wrong | "What assumptions are we copying?" |
| `x-engineering` | Finds engineering leverage. | engineering magic, engineering wins, chief engineer mindset, value creation | "Where is the real engineering value?" |
| `x-5-step-algo` | Runs the core build/process algorithm. | question, delete, simplify, accelerate, automate, overdelete/addback | "Simplify this workflow before automating." |
| `x-teams` | Reviews people quality and builder culture. | exceptional ability, special forces, feedback, builders | "Do we need more people or better owners?" |
| `x-org` | Removes organizational drag. | direct communication, simple language, no stale boundaries, permission to fail | "Why is this decision so slow?" |
| `x-urgency` | Speeds learning and execution. | time risk, parallel work, impossible breakdown, aggressive timelines | "How can we prove this this week?" |
| `x-manufacturing` | Treats production as the product. | make stuff, factory as product, constraints, suppliers, moat | "What limits our release throughput?" |
| `x-founder` | Tests conviction and endurance. | all-in, adversity, eat glass, fear, runway | "Should I go all in?" |
| `x-company-building` | Turns mission into company sequence. | prototypes, survival, public reality, more for less, anchor trust | "What is the build sequence?" |
| `x-future` | Applies abundance and technology future lenses. | AI, robotics, autonomy, energy, human-machine upgrades | "What becomes abundant if this works?" |
| `x-risk` | Reviews systemic downside. | AI risk, regulation, war, energy, population, asteroids | "What failure modes matter at scale?" |
| `x-multiplanetary` | Turns moonshots into staged milestones. | gateway milestones, civilization backup, long-horizon execution | "What is our gateway milestone?" |
| `x-reading` | Recommends books by problem type. | fiction, science, engineering, history, AI, business | "What should I read for this problem?" |

## How To Use

Start with the router when the situation is broad:

```text
Use $x-router on this startup idea and pick the best method.
```

Use a specific skill when you know the lens:

```text
Use $x-5-step-algo on this product spec.
Use $x-teams on this hiring plan.
Use $x-risk on this AI agent launch.
```

Give the agent enough raw material: the plan, spec, decision, cost, workflow, team context, or goal. These skills are designed to operate on real context, not slogans.

## Repository Layout

```text
elon-musk/
  .codex-plugin/plugin.json
  skills/
    x-router/
    x-purpose/
    x-thinking/
    x-engineering/
    x-5-step-algo/
    x-teams/
    x-org/
    x-urgency/
    x-manufacturing/
    x-founder/
    x-company-building/
    x-future/
    x-risk/
    x-multiplanetary/
    x-reading/
  references/
    book-map.md
    method-catalog.md
    source-notes.md
  examples/
  docs/
  scripts/
  tests/
```

## Validate

Run the public validator:

```bash
python3 scripts/validate_public.py
```

Run the unit suite:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

If local Codex skill/plugin creator helpers are installed, `validate_public.py` will also run those validators.

## Updating

```bash
cd ~/plugins/elon-musk
git pull --ff-only
python3 scripts/install_local.py --marketplace --symlink-skills
codex plugin add elon-musk@personal
python3 scripts/validate_public.py
```

Start a new Codex thread after reinstalling so the updated skills are loaded.

## Design Notes

This pack follows the same broad pattern as the shared skill/plugin ecosystem:

- Small, procedural skills instead of one giant mega-skill.
- A router for vague requests.
- A stable prefix for search.
- References for broader context.
- Scripts for install, symlink setup, and validation.
- Public source-boundary docs.

Useful references:

- https://github.com/mattpocock/skills
- https://github.com/EveryInc/compound-engineering-plugin
- https://github.com/EveryInc/compound-knowledge-plugin
- https://github.com/steipete/agent-scripts/tree/main/skills

## Source Boundaries

This repository contains paraphrased operating methods, workflows, and metadata. It does not contain the full text of *The Book of Elon*, long excerpts, transcripts, or other copyrighted source material.

See `docs/SOURCE_BOUNDARIES.md`.

## Disclaimer

This is an unofficial educational and productivity project. It is not affiliated with, endorsed by, sponsored by, or connected to Elon Musk, Eric Jorgenson, ElonMuskBook.org, Tesla, SpaceX, X, xAI, Neuralink, The Boring Company, or any publisher/rightsholder.

"Elon Musk" is used descriptively to identify the inspiration for the operating patterns.

## License

MIT. See `LICENSE`.
