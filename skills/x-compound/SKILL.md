---
name: x-compound
description: "Extract one to three reusable lessons or method reviews from a completed x-prefixed method session and save only user-approved local Markdown. Use after strategy, engineering, team, risk, company-building, or execution work should compound into future reviews without storing raw session logs."
---

# X Compound

Use this skill after a useful `x-*` method review, decision, plan, or
postmortem. The goal is to capture only the part that will make future work
faster or clearer.

## When To Use

- The user says "compound this", "save what we learned", or "what should we remember?"
- A method review produced a reusable decision, pattern, tradeoff, or warning.
- A project is ending and the next similar project should start smarter.
- A prior assumption changed and older local notes may need an update.

## Boundaries

- Save local Markdown only.
- Do not save book text, long quotes, EPUB contents, transcripts, secrets, or raw session logs.
- Do not create more than three durable notes from one session.
- A direct current request such as "compound this" or "save this lesson" authorizes only the described note in the current target project.
- A candidate emitted by `x-review-pack` is not write authorization.
- A scheduled or non-interactive run may write only when its configuration preauthorizes the target project, path, note type, and scope.
- If authorization is absent or ambiguous, show the draft and do not write.
- Prefer updating an existing note when the new learning replaces or sharpens it.

## Workflow

1. Identify one to three compoundable items. If nothing is worth saving, say that and stop.
2. Classify each item:
   - `method-review`: a concrete decision, tradeoff, or review output.
   - `reusable-lesson`: a pattern that should guide future work.
3. Choose the target path:
   - `docs/reviews/YYYY-MM-DD-slug.md` for method reviews.
   - `docs/lessons/YYYY-MM-DD-slug.md` for reusable lessons.
4. Draft frontmatter with `type`, `methods`, `tags`, `confidence`, `created`, `source`, and `resurfaces_when`.
5. Search for duplicates before writing. Check `docs/reviews/`, `docs/lessons/`, `docs/knowledge/`, and `docs/solutions/` when they exist.
6. Check for stale contradictions. If an older note conflicts with the new lesson, show the conflict and recommend update, keep both, or skip.
7. Record the authorization basis: direct current request, approved draft, or preauthorized scheduled scope.
8. If the authorization does not cover this exact target and note, present the draft and wait.
9. Write the authorized note, then report the saved path, tags, and future retrieval triggers.

## Note Shape

For a method review, include:

- Review question.
- Methods used.
- Recommendation.
- Rejected alternatives.
- Evidence and uncertainty.
- Next action.

For a reusable lesson, include:

- What changed in understanding.
- When to apply it.
- Why it matters.
- Concrete example.
- What would make it stale.

## Output

```text
X Compound:
Candidates:
Duplicate/stale check:
Approved notes:
Authorization basis:
Saved paths:
Tags:
Resurfaces when:
Next action:
```

## Completion Gate

Complete only when every candidate has a type, duplicate and stale check, target path, retrieval trigger, authorization basis, and either a saved path or an explicit no-write result.

## Example

User: "Compound the feature-plan review we just did."

Answer: extract one lesson such as "delete dashboard exports before automating
report delivery", check existing `docs/lessons/`, ask for approval, then save a
small Markdown note with `methods: [x-5-step-algo, x-manufacturing]`.
