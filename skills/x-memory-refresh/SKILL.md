---
name: x-memory-refresh
description: "Refresh local x-prefixed method memory by auditing approved Markdown reviews, lessons, handoffs, knowledge notes, and solution notes for duplicates, stale claims, missing retrieval triggers, and unsafe saved content. Use when docs/reviews or docs/lessons have accumulated and should be pruned before future method work relies on them."
---

# X Memory Refresh

Use this skill after `x-compound` has created enough local notes that memory may
need pruning. The leading word is `refresh`: keep useful memory current without
turning it into raw transcript storage.

## When To Use

- The user says "refresh memory", "audit lessons", "dedupe notes", or "clean up reviews".
- `docs/reviews/`, `docs/lessons/`, `docs/knowledge/`, or `docs/solutions/` contains several local notes.
- A newer decision may contradict older saved guidance.
- Future reviews are starting to resurface stale or duplicate lessons.

## Workflow

1. Find local memory folders that exist: `docs/reviews/`, `docs/lessons/`, `docs/knowledge/`, `docs/solutions/`, and `docs/handoffs/`. Completion criterion: every existing folder is listed and missing folders are not treated as errors.
2. Read Markdown frontmatter and headings. Completion criterion: every note considered has path, type, methods, tags, confidence, created date when present, and resurfacing triggers recorded or marked missing.
3. Detect duplicates and stale conflicts. Completion criterion: each finding cites the affected paths and gives one action: keep, merge, update, archive, or delete.
4. Check boundaries. Completion criterion: flag any raw transcripts, secrets, long book excerpts, or private data instead of copying them into the answer.
5. Ask before editing. Completion criterion: proposed edits are shown first unless the user explicitly requested automated cleanup.

## Boundaries

- Do not read raw harness logs or session histories by default.
- Do not save new memory unless the user approves the proposed change.
- Prefer small Markdown edits over new tooling until memory volume justifies automation.
- If no memory folders exist, report that no refresh is needed and suggest `x-compound` after future reviews.

## Output

```text
X Memory Refresh:
Folders checked:
Notes reviewed:
Duplicate findings:
Stale findings:
Boundary findings:
Proposed edits:
Next action:
```

## Example

User: "Use x-memory-refresh on this repo."

Answer: inspect local lesson and review folders, report duplicate or stale notes
with paths, ask before modifying Markdown, and leave raw session logs untouched.
