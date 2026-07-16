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
4. Check specialist boundaries. Completion criterion: the review names any legal, security, safety, medical, financial, HR, accessibility, compliance, or domain review still required.
5. Run a contradiction check. Completion criterion: the recommendation has been compared with approval boundaries, irreversible harm, stop conditions, and unresolved evidence gaps.
6. Close the loop. Offer `x-compound` candidates when the review produced reusable learning. Completion criterion: one to three candidate lessons are shown, or the output says no durable lesson is worth saving. A candidate is not write authorization.
7. Prepare continuation. Use `x-handoff` only when work remains, context is long, or another session/agent will continue. Completion criterion: the final answer names whether a handoff was written or why it was unnecessary.

## Boundaries

- Invoking `x-review-pack` authorizes review only. Do not write durable memory unless the current request separately authorizes the exact save, or a scheduled run has a preauthorized target, path, note type, and scope.
- Do not run every skill. A pack is bounded: one primary lens and at most two supporting lenses.
- Load the selected sibling skills when they are available. If they are unavailable, apply the route from this contract, mark the fallback, and do not pretend their complete instructions were loaded.
- Do not treat an omitted method as evidence that specialist review is unnecessary.
- Do not let an urgency, founder, growth, or simplification lens override a safety gate or stop-worthy risk.
- Do not create a handoff when the review is complete and short enough to summarize in the answer.

## Output

```text
X Review Pack:
Route:
Primary review:
Support checks:
Skill loading: loaded / fallback
Specialist review boundaries:
Contradiction / stop-condition check:
Recommendation:
Compound candidates:
Handoff:
Verification or next action:
```

## Completion Gate

Complete only when routing, loaded-skill or fallback state, primary review, support effects, specialist boundaries, contradiction and stop checks, recommendation, compound candidates, and handoff status are explicit.

## Example

User: "Use x-review-pack on this AI launch plan and close the loop."

Answer: route to `x-risk` with `x-thinking` and `x-company-building` support,
apply the risk review, list any reusable lesson candidates for approval, and
write a handoff only if the launch review needs a later continuation.
