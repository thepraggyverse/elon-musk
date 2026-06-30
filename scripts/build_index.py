#!/usr/bin/env python3
"""Generate skill index and example docs from one metadata table."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILLS = [
    {
        "name": "x-setup",
        "group": "workflow",
        "does": "Checks plugin install state, cache, symlinks, and prompt visibility.",
        "when": "Setup, update, or skill discoverability looks wrong.",
        "artifact": "Install and visibility diagnosis",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-setup to check whether the plugin is installed and visible.",
        "output": "Install state, prompt visibility, issues, and one next command.",
    },
    {
        "name": "x-router",
        "group": "workflow",
        "does": "Chooses the best method lens.",
        "when": "The request is broad or messy.",
        "artifact": "Skill route and prompt",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-router on this messy startup idea.",
        "output": "Primary skill, supporting skills, why, and a ready-to-use follow-up prompt.",
    },
    {
        "name": "x-review-pack",
        "group": "workflow",
        "does": "Runs routing, method review, compound candidates, and handoff closeout.",
        "when": "A plan needs a complete close-the-loop review.",
        "artifact": "Route, review, compound candidates, and handoff decision",
        "writes": "Only via x-compound or x-handoff rules",
        "safe": "Yes",
        "prompt": "Use x-review-pack on this launch plan and close the loop.",
        "output": "Bounded route, primary review, support checks, reusable lesson candidates, and handoff status.",
    },
    {
        "name": "x-purpose",
        "group": "method",
        "does": "Tests usefulness, ambition, and sustained effort.",
        "when": "Choosing projects, missions, product bets, or career bets.",
        "artifact": "Project or mission review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-purpose on this product bet before I spend a month on it.",
        "output": "Usefulness test, future value, effort price, and go/no-go pressure.",
    },
    {
        "name": "x-thinking",
        "group": "method",
        "does": "Improves reasoning quality.",
        "when": "Strategy, architecture, impossible claims, expensive claims.",
        "artifact": "Assumption and reasoning review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-thinking on this architecture claim: this must be realtime.",
        "output": "Assumptions, first-principles rebuild, constraints, and uncertainty.",
    },
    {
        "name": "x-engineering",
        "group": "method",
        "does": "Finds where engineering creates real value.",
        "when": "Technical strategy, build-vs-buy, product architecture.",
        "artifact": "Engineering leverage review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-engineering on this build-vs-buy decision.",
        "output": "Where engineering creates value, technical leverage, and taste risks.",
    },
    {
        "name": "x-5-step-algo",
        "group": "method",
        "does": "Questions, deletes, simplifies, accelerates, then automates.",
        "when": "Feature specs, workflows, migrations, refactors, automations.",
        "artifact": "Requirement deletion and simplification plan",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-5-step-algo on this feature spec.",
        "output": "Question, delete, simplify, accelerate, automate sequence.",
    },
    {
        "name": "x-teams",
        "group": "method",
        "does": "Reviews talent density, ownership, and builder culture.",
        "when": "Hiring, founding teams, performance, team health.",
        "artifact": "Team capability and ownership review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-teams on this founding team plan.",
        "output": "Talent density, ownership, feedback, and builder-culture review.",
    },
    {
        "name": "x-org",
        "group": "method",
        "does": "Removes organizational drag.",
        "when": "Meetings, approvals, cross-team work, unclear ownership.",
        "artifact": "Organization drag review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-org on this approval-heavy workflow.",
        "output": "Direct communication path, stale process, owner map, and simpler language.",
    },
    {
        "name": "x-urgency",
        "group": "method",
        "does": "Shortens timelines and feedback loops.",
        "when": "Launches, blocked projects, roadmaps, crisis work.",
        "artifact": "Timeline compression plan",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-urgency on this slipping launch.",
        "output": "Time risk, parallel work, one scoreboard, and next 72-hour moves.",
    },
    {
        "name": "x-manufacturing",
        "group": "method",
        "does": "Treats production and delivery as the product.",
        "when": "Operations, CI/CD, support, fulfillment, physical production.",
        "artifact": "Production path and bottleneck review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-manufacturing on this weekly reporting pipeline.",
        "output": "Production path, constraint, throughput, and dependency bottlenecks.",
    },
    {
        "name": "x-founder",
        "group": "method",
        "does": "Tests conviction, pain tolerance, and all-in decisions.",
        "when": "Startup commitment, pivots, runway, hard personal bets.",
        "artifact": "Founder commitment review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-founder on whether I should commit to this startup.",
        "output": "Conviction, pain tolerance, runway, fear, and all-in decision quality.",
    },
    {
        "name": "x-company-building",
        "group": "method",
        "does": "Turns mission into prototype, survival, sequence, and scale.",
        "when": "Startup roadmaps, product strategy, capital allocation.",
        "artifact": "Prototype, sequence, and survival plan",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-company-building on this first product roadmap.",
        "output": "Prototype proof, sequence, survival constraints, and public reality check.",
    },
    {
        "name": "x-future",
        "group": "method",
        "does": "Applies abundance, AI, robotics, autonomy, and energy lenses.",
        "when": "Long-term technology bets and future-state planning.",
        "artifact": "Future-state opportunity review",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-future on this robotics and AI opportunity.",
        "output": "Abundance, autonomy, energy, human-machine, and timing lenses.",
    },
    {
        "name": "x-risk",
        "group": "method",
        "does": "Reviews systemic and civilization-scale downside.",
        "when": "AI systems, safety, infrastructure, policy, broad downside.",
        "artifact": "Risk map and release gates",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-risk on this AI agent release.",
        "output": "Downside map, systemic risk, mitigations, and release gates.",
    },
    {
        "name": "x-multiplanetary",
        "group": "method",
        "does": "Turns moonshots into staged milestones.",
        "when": "Deep-tech, resilience, infrastructure, long-horizon missions.",
        "artifact": "Moonshot milestone plan",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-multiplanetary on this moonshot infrastructure plan.",
        "output": "Staged milestones, gateway proofs, resilience value, and long-horizon execution.",
    },
    {
        "name": "x-reading",
        "group": "method",
        "does": "Recommends books by problem type.",
        "when": "Learning paths for engineering, history, AI, strategy, science.",
        "artifact": "Reading path by problem type",
        "writes": "No",
        "safe": "Yes",
        "prompt": "Use x-reading to build a learning list for hard-tech company building.",
        "output": "Books by problem type, why each helps, and reading sequence.",
    },
    {
        "name": "x-compound",
        "group": "workflow",
        "does": "Saves approved lessons and reviews as local Markdown memory.",
        "when": "After a useful method session should guide future work.",
        "artifact": "Approved Markdown lesson or review",
        "writes": "Only after approval",
        "safe": "Yes",
        "prompt": "Use x-compound to save the reusable lesson from this review.",
        "output": "Candidate notes, duplicate check, approval request, and saved Markdown path.",
    },
    {
        "name": "x-memory-refresh",
        "group": "workflow",
        "does": "Audits local lessons and reviews for stale or duplicate memory.",
        "when": "Saved method memory has accumulated and needs pruning.",
        "artifact": "Memory audit with proposed edits",
        "writes": "Only after approval",
        "safe": "Yes",
        "prompt": "Use x-memory-refresh on this repo's docs/lessons and docs/reviews.",
        "output": "Folders checked, notes reviewed, duplicate findings, stale findings, and proposed edits.",
    },
    {
        "name": "x-handoff",
        "group": "workflow",
        "does": "Writes a redacted continuation handoff.",
        "when": "Long reviews, context transitions, or next-session briefs.",
        "artifact": "Redacted continuation note",
        "writes": "Temp by default",
        "safe": "Yes",
        "prompt": "Use x-handoff to write a continuation note for this strategy review.",
        "output": "Redacted state, decisions, next steps, risks, and suggested next skills.",
    },
]


def table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def skill_link(name: str) -> str:
    return f"`{name}`"


def render_skill_index() -> str:
    inventory_rows = [
        [skill_link(item["name"]), item["does"], item["when"]]
        for item in SKILLS
    ]
    compat_rows = [
        [skill_link(item["name"]), item["artifact"], item["writes"], item["safe"]]
        for item in SKILLS
    ]
    workflow_rows = [
        [skill_link(item["name"]), item["does"]]
        for item in SKILLS
        if item["group"] == "workflow"
    ]
    return "\n\n".join(
        [
            "# Skill Index",
            "Generated by `scripts/build_index.py`. Edit the script metadata, then regenerate this file.",
            "## Inventory",
            table(["Skill", "What it does", "Use when"], inventory_rows),
            "## Workflow Skills",
            table(["Workflow skill", "What it adds"], workflow_rows),
            "## Compatibility Quick Scan",
            table(["Skill", "Output artifact", "Writes files?", "Safe default?"], compat_rows),
        ]
    ) + "\n"


def render_all_examples() -> str:
    rows = [
        [skill_link(item["name"]), f"`{item['prompt']}`", item["output"]]
        for item in SKILLS
    ]
    return "\n\n".join(
        [
            "# All Skills Example Index",
            "Generated by `scripts/build_index.py`. Edit the script metadata, then regenerate this file.",
            "Use this file as a quick product tour. Each row gives a concrete prompt shape and the expected output artifact.",
            table(["Skill", "Example prompt", "Expected output"], rows),
            "## Close The Loop Example",
            "```text\nUse x-review-pack on this launch plan.\nApprove x-compound only if a reusable lesson is worth saving.\nUse x-handoff only if another session needs to continue the work.\n```",
            "Expected result: a bounded review that produces a decision, approved memory only when useful, and a compact continuation artifact only when needed.",
        ]
    ) + "\n"


def render_skill_example(item: dict[str, str]) -> str:
    return "\n\n".join(
        [
            f"# {item['name']} Example",
            "Generated by `scripts/build_index.py`. Edit the script metadata, then regenerate this file.",
            "## Prompt",
            f"```text\n{item['prompt']}\n```",
            "## Expected Output",
            item["output"],
            "## Use When",
            item["when"],
            "## Write Behavior",
            item["writes"],
        ]
    ) + "\n"


def generated_files() -> dict[Path, str]:
    files: dict[Path, str] = {
        ROOT / "docs" / "SKILL_INDEX.md": render_skill_index(),
        ROOT / "examples" / "all-skills.md": render_all_examples(),
    }
    for item in SKILLS:
        files[ROOT / "examples" / f"{item['name']}.md"] = render_skill_example(item)
    return files


def write_files() -> None:
    for path, text in generated_files().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="ascii")


def check_files() -> int:
    mismatches = []
    for path, expected in generated_files().items():
        actual = path.read_text(encoding="ascii") if path.exists() else None
        if actual != expected:
            mismatches.append(path.relative_to(ROOT).as_posix())
    if mismatches:
        print("generated files are stale:")
        for rel in mismatches:
            print(f"  {rel}")
        print("run: python3 scripts/build_index.py")
        return 1
    print("generated index files are current")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate skill index and examples")
    parser.add_argument("--check", action="store_true", help="Fail when generated files are stale")
    args = parser.parse_args()
    if args.check:
        return check_files()
    write_files()
    print(f"generated {len(generated_files())} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
