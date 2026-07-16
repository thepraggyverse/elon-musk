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
5. Check authorization before editing. Completion criterion: proposed edits are shown first unless the current request explicitly authorizes cleanup of the named folders, or a scheduled run has a preauthorized target, path, and scope.

## Boundaries

- Do not read raw harness logs or session histories by default.
- A request to audit or refresh memory authorizes inspection, not deletion or rewriting, unless it explicitly asks to clean, merge, update, archive, or delete.
- Modify notes only when the current request authorizes cleanup of the named scope or a scheduled run has equivalent preauthorization.
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
Authorization basis:
Edits made:
Next action:
```

## Completion Gate

Complete only when every existing memory folder and reviewed note is accounted for, findings cite paths, authorization is explicit, and each proposed or completed edit has one disposition.

## Example

User: "Use x-memory-refresh on this repo."

Answer: inspect local lesson and review folders, report duplicate or stale notes
with paths, ask before modifying Markdown, and leave raw session logs untouched.
