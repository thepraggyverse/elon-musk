#!/usr/bin/env python3
"""Validate behavior fixtures and optionally run them through Codex or Claude."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES_PATH = ROOT / "tests" / "behavior_fixtures.json"


def load_fixtures() -> list[dict]:
    fixtures = json.loads(FIXTURES_PATH.read_text(encoding="ascii"))
    if not isinstance(fixtures, list) or not fixtures:
        raise ValueError("behavior fixtures must be a non-empty list")

    seen = set()
    for fixture in fixtures:
        fixture_id = fixture.get("id")
        skill = fixture.get("skill")
        prompt = fixture.get("prompt")
        groups = fixture.get("required_groups")
        forbidden = fixture.get("forbidden", [])
        forbidden_patterns = fixture.get("forbidden_patterns", [])
        if (
            not isinstance(fixture_id, str)
            or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", fixture_id)
            or fixture_id in seen
        ):
            raise ValueError(f"invalid or duplicate fixture id: {fixture_id!r}")
        seen.add(fixture_id)
        if not isinstance(skill, str) or not (ROOT / "skills" / skill / "SKILL.md").is_file():
            raise ValueError(f"{fixture_id}: unknown skill {skill!r}")
        if not isinstance(prompt, str) or len(prompt) < 40:
            raise ValueError(f"{fixture_id}: prompt is too short")
        if skill.lower() in prompt.lower():
            raise ValueError(f"{fixture_id}: prompt must remain source-blind")
        if not isinstance(groups, list) or not groups:
            raise ValueError(f"{fixture_id}: required_groups must be non-empty")
        if any(not isinstance(group, list) or not group or any(not isinstance(item, str) for item in group) for group in groups):
            raise ValueError(f"{fixture_id}: invalid required_groups")
        if not isinstance(forbidden, list) or any(not isinstance(item, str) for item in forbidden):
            raise ValueError(f"{fixture_id}: invalid forbidden list")
        if not isinstance(forbidden_patterns, list) or any(not isinstance(item, str) for item in forbidden_patterns):
            raise ValueError(f"{fixture_id}: invalid forbidden_patterns list")
        for pattern in forbidden_patterns:
            re.compile(pattern)
    return fixtures


def evaluate_output(fixture: dict, output: str) -> tuple[bool, list[str]]:
    normalized = output.lower()
    issues = []
    for group in fixture["required_groups"]:
        if not any(term.lower() in normalized for term in group):
            issues.append("missing one of: " + ", ".join(group))
    for term in fixture.get("forbidden", []):
        if term.lower() in normalized:
            issues.append(f"forbidden phrase present: {term}")
    for pattern in fixture.get("forbidden_patterns", []):
        if re.search(pattern, output, flags=re.IGNORECASE | re.MULTILINE):
            issues.append(f"forbidden pattern matched: {pattern}")
    return not issues, issues


def build_prompt(fixture: dict, invoke_mode: str = "path") -> str:
    if invoke_mode == "named":
        return "\n".join(
            [
                f"Use ${fixture['skill']} for this task.",
                "Answer the task directly using the skill's output contract.",
                "Do not edit files or perform external actions.",
                "Task:",
                fixture["prompt"],
            ]
        )
    skill_path = ROOT / "skills" / fixture["skill"] / "SKILL.md"
    return "\n".join(
        [
            f"Read and follow the skill at {skill_path}.",
            "Answer the task directly using the skill's output contract.",
            "Do not edit files or perform external actions.",
            "Task:",
            fixture["prompt"],
        ]
    )


def run_codex(prompt: str, timeout: int) -> str:
    if not shutil.which("codex"):
        raise RuntimeError("codex CLI not found")
    with tempfile.NamedTemporaryFile(prefix="elon-musk-behavior-", suffix=".txt", delete=False) as handle:
        output_path = Path(handle.name)
    try:
        subprocess.run(
            [
                "codex",
                "exec",
                "--ephemeral",
                "--sandbox",
                "read-only",
                "--skip-git-repo-check",
                "-C",
                str(ROOT),
                "-o",
                str(output_path),
                prompt,
            ],
            check=True,
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        return output_path.read_text(encoding="utf-8")
    finally:
        output_path.unlink(missing_ok=True)


def run_claude(prompt: str, timeout: int) -> str:
    if not shutil.which("claude"):
        raise RuntimeError("claude CLI not found")
    result = subprocess.run(
        ["claude", "-p", "--plugin-dir", str(ROOT), prompt],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--harness", choices=["codex", "claude"])
    parser.add_argument("--fixture", action="append", default=[])
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--invoke-mode",
        choices=["path", "named"],
        default="path",
        help="Use an exact SKILL.md path to test behavior or a $name invocation to test harness discovery.",
    )
    args = parser.parse_args()

    fixtures = load_fixtures()
    selected = [item for item in fixtures if not args.fixture or item["id"] in args.fixture]
    unknown = sorted(set(args.fixture) - {item["id"] for item in fixtures})
    if unknown:
        raise SystemExit("unknown fixtures: " + ", ".join(unknown))

    print(f"Behavior fixture validation passed: {len(fixtures)} fixtures")
    if not args.harness:
        return 0

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)

    failures = 0
    runner = run_codex if args.harness == "codex" else run_claude
    for fixture in selected:
        try:
            output = runner(build_prompt(fixture, args.invoke_mode), args.timeout)
            passed, issues = evaluate_output(fixture, output)
        except subprocess.CalledProcessError as exc:
            detail = (exc.stderr or exc.stdout or str(exc)).strip()
            passed, issues, output = False, [detail], ""
        except (RuntimeError, subprocess.TimeoutExpired) as exc:
            passed, issues, output = False, [str(exc)], ""
        status = "PASS" if passed else "FAIL"
        print(f"{status} {fixture['id']} ({fixture['skill']}, {args.invoke_mode})")
        for issue in issues:
            print(f"  {issue}")
        if args.output_dir:
            (args.output_dir / f"{fixture['id']}.md").write_text(output, encoding="utf-8")
        failures += int(not passed)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
