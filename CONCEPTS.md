# Concepts

`elon-musk` is organized around method families, not quotations.

## Core Idea

The useful unit is a reusable move:

- "Question the requirement."
- "Delete before optimizing."
- "Treat the factory as the product."
- "Attack the constraint."
- "Separate reality from public perception."
- "Turn a moonshot into gateway milestones."

Each top-level `x-*` skill packages one family of moves.

## Why Merged Skills

The book contains many ideas. Turning every idea into its own skill would make search noisy. This plugin keeps only 15 top-level skills and stores smaller ideas as subsections.

| Alternative | Problem |
|---|---|
| One giant skill | Too much context and weak routing. |
| One skill per quote | Too noisy and hard to maintain. |
| Merged skills | Search stays clean while coverage stays broad. |

## Method Flow

| Stage | Skills |
|---|---|
| Choose the work | `x-purpose`, `x-founder` |
| Think clearly | `x-thinking`, `x-engineering` |
| Simplify before speed | `x-5-step-algo`, `x-org` |
| Execute faster | `x-urgency`, `x-manufacturing` |
| Build the company | `x-company-building`, `x-teams` |
| Look ahead | `x-future`, `x-risk`, `x-multiplanetary` |
| Learn more | `x-reading` |

## Router Behavior

Use `x-router` when the request is vague. The router should pick one primary skill and at most two supporting skills.

Example:

```text
Use $x-router on this idea:
An AI compliance assistant for small companies.
```

Good route:

| Role | Skill |
|---|---|
| Primary | `x-purpose` |
| Support | `x-thinking` |
| Support | `x-risk` |

## Source Boundary

The plugin preserves practical workflows. It does not preserve the book text. Keep source references at section or method level.
