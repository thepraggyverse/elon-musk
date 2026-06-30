---
name: x-review-pack
description: "Run a complete close-the-loop review pack for a project, plan, launch, architecture, organization, or risk decision. Use when the user wants one pass that routes to the right x-prefixed method, applies the review, captures the reusable lesson with approval, and writes a continuation handoff when needed."
---

# X Review Pack

Use this skill when the user wants the whole method loop, not just one lens.
The leading word is `pack`: one bounded review packet that starts with routing
and ends with a checked closeout.

## When To Use

- The user says "review this and close the loop", "run the full pack", or "do the whole method review".
- A plan needs one primary method plus supporting lenses.
- A long review should produce a decision, a reusable lesson candidate, and a continuation handoff if work remains.

## Workflow

1. Route the work. Pick one primary `x-*` method and at most two supporting skills. Completion criterion: the route names why each selected skill is needed and why skipped obvious skills are not needed.
2. Apply the primary method. Use the selected method's output shape. Completion criterion: the recommendation includes evidence, uncertainty, deletion/simplification opportunities when relevant, and next action.
3. Cross-check with supporting skills. Completion criterion: every support lens either changes the recommendation, adds a risk, or is explicitly marked as no material change.
4. Close the loop. Offer `x-compound` candidates when the review produced reusable learning. Completion criterion: one to three candidate lessons are shown, or the output says no durable lesson is worth saving.
5. Prepare continuation. Use `x-handoff` only when work remains, context is long, or another session/agent will continue. Completion criterion: the final answer names whether a handoff was written or why it was unnecessary.

## Boundaries

- Do not write durable memory without approval unless the user explicitly asked for automation or headless mode.
- Do not run every skill. A pack is bounded: one primary lens and at most two supporting lenses.
- Do not create a handoff when the review is complete and short enough to summarize in the answer.

## Output

```text
X Review Pack:
Route:
Primary review:
Support checks:
Recommendation:
Compound candidates:
Handoff:
Verification or next action:
```

## Example

User: "Use x-review-pack on this AI launch plan and close the loop."

Answer: route to `x-risk` with `x-thinking` and `x-company-building` support,
apply the risk review, list any reusable lesson candidates for approval, and
write a handoff only if the launch review needs a later continuation.
