# Usage

This document gives practical prompt recipes for the `elon-musk` plugin.

## Start With The Router

Use this when you do not know which skill fits:

```text
Use $x-router on this situation:
<paste project, decision, workflow, idea, or problem>
```

Expected output:

```text
X Router:
Primary skill:
Supporting skills:
Why:
Use it like:
```

## Product Idea Review

```text
Use $x-purpose and $x-thinking on this product idea:
<idea>
```

Look for:

| Area | Question |
|---|---|
| Usefulness | Who benefits and how? |
| Future | What future does this make more likely? |
| Assumptions | What are we copying from others? |
| First proof | What would prove the idea quickly? |

## Feature Plan Review

```text
Use $x-5-step-algo on this feature spec:
<spec>
```

Look for:

| Step | Output |
|---|---|
| Question | Requirement owner, reason, evidence, validity. |
| Delete | Features, steps, fields, meetings, or approvals to remove. |
| Simplify | Smallest viable path. |
| Accelerate | Shorter feedback loop. |
| Automate | Automate now, later, or not at all. |

## Engineering Strategy

```text
Use $x-engineering on this architecture decision:
<decision>
```

Use when:

- Build-vs-buy is unclear.
- The hard engineering problem is buried.
- Product value depends on making something real, reliable, or cheap.
- The team needs a chief-engineer view across product, cost, design, and operations.

## Team And Org Review

```text
Use $x-teams and $x-org on this team problem:
<problem>
```

Look for:

| Skill | Focus |
|---|---|
| `x-teams` | Talent density, ownership, feedback, builder culture. |
| `x-org` | Handoffs, meetings, approvals, boundaries, decision paths. |

## Manufacturing Or Delivery Pipeline

```text
Use $x-manufacturing on this delivery process:
<process>
```

This works for physical manufacturing and software operations. Treat CI, review, deploy, support, and reporting as a production path.

Expected output:

```text
Manufacturing Review:
Production path:
Constraint:
Supplier/dependency risks:
Delete candidates:
Simplified path:
Throughput experiment:
```

## Startup Or Founder Decision

```text
Use $x-founder and $x-company-building on this decision:
<decision>
```

Use when deciding whether to:

- Quit a job.
- Pivot.
- Raise money.
- Kill a product.
- Narrow the first customer.
- Bet more time or capital.

## Risk Review

```text
Use $x-risk on this AI agent launch:
<launch plan>
```

Look for:

| Risk Type | Examples |
|---|---|
| AI | Misuse, autonomy, alignment, control. |
| Regulation | Stale approvals, compliance gaps, process drag. |
| Infrastructure | Vendor failure, data loss, brittle dependencies. |
| Social/systemic | Trust, incentives, public harm, long-term fragility. |

## Moonshot Planning

```text
Use $x-multiplanetary on this moonshot:
<mission>
```

Expected framing:

| Element | Meaning |
|---|---|
| Mission | Why this matters. |
| Gateway milestone | First capability that unlocks the rest. |
| Mission metric | The one metric that aligns decisions. |
| Capability thresholds | Stages from barely possible to durable. |
| Next proof | The next concrete test. |

## Reading Path

```text
Use $x-reading to build a reading path for:
<learning goal>
```

The skill routes across:

- Fiction.
- Science.
- Rocket science and engineering.
- History.
- AI and machine learning.
- Business and economics.

## Save A Reusable Lesson

```text
Use $x-compound to save the reusable lesson from the review we just did.
```

Look for:

| Area | Question |
|---|---|
| Candidate | Is this useful enough to help a future session? |
| Type | Is it a concrete review or a reusable lesson? |
| Duplicate | Does a similar note already exist? |
| Staleness | Does this contradict an older note? |
| Retrieval | When should this resurface? |

The direct request above authorizes that described save in the current project.
A lesson candidate produced by `x-review-pack` does not authorize a write.
Scheduled runs require a preauthorized target, path, note type, and scope.

## Write A Handoff

```text
Use $x-handoff to write a continuation handoff for this strategy review.
```

Expected output:

```text
X Handoff:
Saved path:
Next task:
Suggested skills:
Open risks:
```

Use this before switching sessions, pausing long work, or handing a method
review to another agent.
