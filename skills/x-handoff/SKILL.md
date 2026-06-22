---
name: x-handoff
description: "Create a compact redacted continuation handoff for long x-prefixed method work, including current state, suggested next skills, evidence, tests, risks, and exact next actions. Use when a strategy, engineering, team, risk, or company-building review needs to continue in a fresh session."
---

# X Handoff

Use this skill when current work should continue later or move to another agent
without losing the useful context.

## When To Use

- The user asks for a handoff, continuation note, or next-session brief.
- A long `x-*` method review is ending before the work is fully complete.
- The next agent needs exact state, not a broad summary.
- The conversation contains decisions that should be referenced but not copied into every artifact.

## Boundaries

- Save to OS temp by default, not the repository.
- Use a stable path when the user asks for one, such as `/tmp/elon-musk-handoff.md`.
- Write repo-local handoffs only when the user asks for durable project files.
- Redact secrets, credentials, private URLs, personal data, raw transcripts, and raw tool output.
- Reference existing artifacts by path or URL instead of duplicating their contents.

## Workflow

1. Identify the handoff audience and next task.
2. Capture current state: repo, branch, changed files, relevant artifacts, and latest verification.
3. Capture decisions made and why they matter.
4. List suggested next skills, usually `x-router`, a primary method skill, `x-compound`, or another concrete `x-*` skill.
5. List blockers, risks, and open questions.
6. Redact sensitive material and remove unrelated conversation history.
7. Write the handoff to OS temp, then report the path and the intended next action.

## Handoff Shape

Use this structure:

```text
# Handoff

## Goal
## Current State
## Decisions
## Changed Files Or Artifacts
## Verification
## Suggested Skills
## Open Risks
## Next Actions
```

## Output

```text
X Handoff:
Saved path:
Next task:
Suggested skills:
Open risks:
```

## Example

User: "Write a handoff for continuing this company-building review tomorrow."

Answer: create a redacted temp handoff that names the repo or artifact paths,
summarizes the active decision, suggests `x-company-building` and `x-compound`,
and lists the exact next action for the fresh session.
