# Memory Model

`elon-musk` is designed to make each useful method pass easier to reuse later.
The memory model is intentionally small: local Markdown, clear frontmatter, and
explicit authorization before durable notes are saved.

## What Gets Saved

Use `x-compound` after a useful review, plan, decision, or postmortem. It can
save two kinds of durable notes in the project where the work happened:

| Folder | Use for | Example |
|---|---|---|
| `docs/reviews/` | Concrete method reviews, decisions, and tradeoff records. | A build/no-build review from `x-purpose` and `x-risk`. |
| `docs/lessons/` | Reusable patterns that should guide future work. | A repeated deletion pattern found by `x-5-step-algo`. |
| `docs/handoffs/` | Optional repo-local handoffs when the user asks for them. | A continuation note for a long project review. |

`x-handoff` writes to OS temp by default instead of the repo. Use repo-local
handoffs only when the user explicitly asks for durable project handoff files.

Use `x-memory-refresh` after several approved notes accumulate. It audits
existing local Markdown for duplicates, stale contradictions, missing retrieval
triggers, and unsafe saved content. It does not read raw session logs by
default.

## What Never Gets Saved

Do not save:

- book text, long quotes, quote collections, EPUB contents, or transcripts;
- raw conversation transcripts or harness history files;
- secrets, credentials, auth URLs, private keys, or sensitive personal data;
- raw tool output when a short evidence summary is enough;
- speculative lessons that the user has not authorized.

The plugin does not read raw session logs by default and does not depend on
harness-specific history files. Future log analysis, if ever added, should be
opt-in, local-only, redacted, and disabled by default.

## Review Frontmatter

Use this shape for files under `docs/reviews/`:

```yaml
---
type: method-review
methods: [x-purpose, x-risk]
tags: [product-bet, launch-risk]
confidence: medium
created: 2026-06-22
source: "Product launch review"
resurfaces_when:
  - "A similar product bet is being evaluated"
  - "Launch risk or downside is unclear"
---
```

The body should include:

- the decision or review question;
- the method lenses used;
- the recommendation;
- rejected alternatives;
- evidence, uncertainty, and next action.

## Lesson Frontmatter

Use this shape for files under `docs/lessons/`:

```yaml
---
type: reusable-lesson
methods: [x-5-step-algo, x-manufacturing]
tags: [workflow, delete-before-automation]
confidence: high
created: 2026-06-22
source: "Weekly reporting pipeline review"
resurfaces_when:
  - "A workflow is being automated"
  - "A process has many manual handoffs"
---
```

The body should include:

- what was learned;
- when to apply it;
- why it matters;
- a concrete example;
- what would make the lesson stale.

## Authorization Rule

Durable memory requires a clear authorization basis.
A direct current request such as "compound this" authorizes the described note in the current target project.
A review-pack candidate by itself does not authorize a write.
An audit or refresh request authorizes inspection but not cleanup unless it explicitly asks for changes.
When authorization is not already exact, show the proposed learning, file path, frontmatter, and body summary before writing.

A scheduled or non-interactive run may write only when its configuration preauthorizes the target project, path, note type, and scope.
There is no generic automation bypass.
Every write reports its authorization basis and remains compact, local, and easy to delete.

## Retrieval Rule

Future work should search `docs/reviews/`, `docs/lessons/`, `docs/knowledge/`,
and `docs/solutions/` when those folders exist. Use tags, method names, and the
`resurfaces_when` field to decide whether a saved note applies.

If a new lesson contradicts an older note, prefer updating or marking the older
note stale over creating silent duplicates.
