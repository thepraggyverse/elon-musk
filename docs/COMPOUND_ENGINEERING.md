# Compound Engineering Reference

This plugin is book-derived, but its packaging borrows useful documentation ideas from Every's Compound Engineering guide:

https://every.to/guides/compound-engineering

The guide's central packaging lesson is simple: a good agent system should make future work easier, not just complete the current task. For this plugin, that means each skill should help the agent produce clearer decisions, reusable reviews, and better next prompts.

## What We Borrow

| Compound Engineering idea | How this plugin uses it |
|---|---|
| Philosophy first | `README.md` explains why the plugin exists before listing files. |
| Main loop | `CONCEPTS.md` and `docs/USAGE.md` show reusable method loops. |
| Explicit inventory | `README.md` lists every top-level `x-*` skill with purpose and use case. |
| Plugin as product | Install, update, validation, and symlink paths are documented. |
| Agent-native docs | The repo keeps prompts, examples, references, and validators in predictable places. |
| Compound step | Maintainers should turn good outputs into examples, references, or tests. |
| Safety nets | Validation and unit tests check structure, source boundaries, and skill coverage. |

## What We Do Differently

| Compound Engineering | Elon Musk Methods |
|---|---|
| Large workflow system for software development. | Compact method pack for reasoning, building, teams, and company strategy. |
| Many agents, commands, and skills. | 15 searchable `x-*` skills, with subsections for smaller ideas. |
| Creates project execution artifacts. | Produces reviews, lenses, prompts, and decision frames. |
| Focuses on AI-native engineering loops. | Focuses on book-derived operating methods. |

## Recommended User Loop

Use the plugin as a lightweight operating layer:

```text
1. Route the problem with x-router.
2. Pick one primary method and at most two support methods.
3. Produce a concrete review, plan, or decision.
4. Capture the reusable lesson in examples, references, or project docs.
5. Add validation when the lesson can be checked automatically.
```

Example:

```text
Use $x-router on this product idea.
Then use $x-purpose and $x-5-step-algo to produce a one-page build/no-build review.
Afterward, summarize the reusable pattern we should keep for future product reviews.
```

## Project Artifacts

For a project using this plugin, useful agent-readable artifacts are:

| Artifact | Purpose |
|---|---|
| `AGENTS.md` | Project preferences, constraints, verification commands, and lessons. |
| `docs/plans/` | Written plans before implementation. |
| `docs/reviews/` | Decision reviews from `x-purpose`, `x-risk`, `x-org`, or `x-teams`. |
| `docs/lessons/` | Reusable findings after a project finishes. |
| `examples/` | Stable prompts that show how to use the skills well. |

This repository does not create those folders automatically. It documents them as a recommended pattern for projects that want the plugin to compound over time.

## Three Review Questions

When an agent uses one of these methods, ask:

| Question | Why it helps |
|---|---|
| What was the hardest judgment call? | Exposes hidden tradeoffs. |
| What alternatives were rejected? | Shows whether the agent considered enough options. |
| What are you least confident about? | Surfaces weak assumptions before they become decisions. |

These questions pair well with `x-thinking`, `x-risk`, and `x-company-building`.

## Maintainer Checklist

When improving the plugin:

```text
1. Add a reusable method only if it changes agent behavior.
2. Prefer merging related ideas into an existing x-* skill.
3. Add or update examples when a prompt pattern proves useful.
4. Add reference notes instead of copying source text.
5. Add tests when the behavior can be checked structurally.
6. Run python3 scripts/validate_public.py.
7. Run PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v.
```

The goal is not to grow forever. The goal is to make each future use clearer, faster, and easier to verify.
