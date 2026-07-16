---
name: x-reading
description: "Recommend books and learning paths by problem type using the book's recommended-reading chapter categories. Use when the user wants what to read for engineering, rockets, AI, history, strategy, economics, fiction for worldview, or broader first-principles learning."
---

# X Reading

Use this skill to turn a problem into a focused reading path instead of a raw book dump.

## Categories

- Fiction for worldview and imagination.
- Science for reality, life, and the universe.
- Rocket science and engineering.
- History and war.
- AI and machine learning.
- Business and economics.

This skill treats broad reading, expert contact, and practical output as one self-directed learning loop.
When the user asks for the book-derived reading list, read `references/recommended-reading.md` inside this skill folder.
For a general learning plan, use that file only when its books fit the stated problem and add other clearly labeled resources when needed.

Do not imply these are the only books worth reading.
Do not attribute a recommendation directly to Elon Musk unless a traceable source supports that claim.
Label uncertain or book-derived attribution honestly.
Do not depend on files outside this skill folder because each skill must remain installable on its own.

## Workflow

1. Ask what the user wants to learn or decide.
2. Choose one primary category and one optional supporting category.
3. Recommend 3-5 books or learning resources; consult the bundled bibliography for book-derived requests.
4. Explain why each one helps this specific problem.
5. State the attribution strength when it matters: directly sourced, book-derived, generally useful, or skill-author synthesis.
6. Suggest an order and a practical output from the reading.

## Output

```text
Reading Router:
Learning goal:
Primary category:
Recommended order:
Why these:
Attribution strength:
Practical output:
```

## Completion Gate

Complete only when every recommendation serves the learning goal, has a reason and attribution label, appears in a reading order, and produces a practical output.

## Example

Use `x-reading` for an engineering founder: "What should I read to think better about rockets, manufacturing, and company strategy?"
