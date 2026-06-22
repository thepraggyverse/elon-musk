# Privacy And Data Handling

## Summary

`elon-musk` is a local skill plugin made of Markdown instructions, plugin
metadata, validation scripts, and install helpers.

- The plugin does not include telemetry or analytics code.
- The plugin does not run a background service that uploads workspace data.
- The plugin does not save raw session logs by default.
- Data leaves your machine only when your host AI tool, model provider, or an
  explicitly invoked external integration sends it.

## What May Send Data

### AI Hosts And Model Providers

When you run these skills in Codex, Claude Code, OpenClaw, or another AI tool,
that host may send prompts, files, code, or other context to its configured
model provider. That behavior is controlled by the host and provider, not by
this repository.

### Explicit Tools And Integrations

The skills may ask the agent to read local project files or write local
Markdown notes when the user approves. If the user also invokes external tools,
connectors, browsers, package managers, or web search, those tools may make
network requests under their own policies.

### Package And Installer Infrastructure

Installing or updating the repository through Git, Codex plugin tooling, or
shell package managers may contact GitHub, package registries, or the user's
configured plugin marketplaces.

## Local Memory

`x-compound` saves only approved local Markdown notes under paths such as
`docs/reviews/` or `docs/lessons/` inside the user's project. `x-handoff` writes
redacted continuation notes to OS temp by default unless the user asks for a
repo-local durable handoff.

Do not save:

- secrets or credentials;
- raw chat transcripts;
- EPUB contents or long copyrighted excerpts;
- private notes that the user did not approve for durable storage.

For the full memory contract, see `docs/MEMORY_MODEL.md`.

## Data Ownership

This repository does not operate a backend service for collecting or retaining
project data. Users own the local notes, reviews, handoffs, and project files
created when using the skills.

## Security Reporting

For security issues, follow `SECURITY.md`.
