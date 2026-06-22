#!/usr/bin/env python3
"""Check a local elon-musk plugin installation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "elon-musk"
EXPECTED_SKILLS = [
    "x-router",
    "x-purpose",
    "x-thinking",
    "x-engineering",
    "x-5-step-algo",
    "x-teams",
    "x-org",
    "x-urgency",
    "x-manufacturing",
    "x-founder",
    "x-company-building",
    "x-future",
    "x-risk",
    "x-multiplanetary",
    "x-reading",
    "x-compound",
    "x-handoff",
]
DEFAULT_SKILL_HOMES = [
    Path.home() / ".agents" / "skills",
    Path.home() / ".codex" / "skills",
    Path.home() / ".claude" / "skills",
    Path.home() / ".openclaw" / "skills",
    Path.home() / ".openclaw" / "acpx" / "codex-home" / "skills",
]


class CheckState:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def ok(self, message: str) -> None:
        print(f"ok: {message}")

    def warn(self, message: str) -> None:
        self.warnings.append(message)
        print(f"warn: {message}")

    def fail(self, message: str) -> None:
        self.failures.append(message)
        print(f"fail: {message}")


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def repo_version() -> str:
    manifest = read_json(ROOT / ".codex-plugin" / "plugin.json")
    version = manifest.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError(".codex-plugin/plugin.json must define version")
    return version


def check_marketplace(state: CheckState) -> None:
    marketplace = Path.home() / ".agents" / "plugins" / "marketplace.json"
    if not marketplace.exists():
        state.fail(f"missing marketplace: {marketplace}")
        return

    data = read_json(marketplace)
    entries = data.get("plugins", [])
    match = next(
        (entry for entry in entries if isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME),
        None,
    )
    if not match:
        state.fail(f"marketplace has no {PLUGIN_NAME} entry: {marketplace}")
        return

    source_path = match.get("source", {}).get("path")
    if source_path != f"./plugins/{PLUGIN_NAME}":
        state.fail(f"marketplace source path should be ./plugins/{PLUGIN_NAME}, got {source_path!r}")
    else:
        state.ok(f"marketplace entry points at {source_path}")


def check_plugin_link(state: CheckState) -> None:
    link = Path.home() / "plugins" / PLUGIN_NAME
    if not link.exists():
        state.fail(f"missing plugin link/path: {link}")
        return

    resolved = link.resolve()
    if resolved != ROOT.resolve():
        state.fail(f"{link} resolves to {resolved}, expected {ROOT.resolve()}")
        return

    state.ok(f"{link} resolves to this checkout")


def check_codex_cache(state: CheckState, version: str) -> None:
    cache = Path.home() / ".codex" / "plugins" / "cache" / "personal" / PLUGIN_NAME / version
    if not cache.exists():
        state.fail(f"missing Codex cache: {cache}")
        return

    manifest_path = cache / ".codex-plugin" / "plugin.json"
    if not manifest_path.exists():
        state.fail(f"missing cached manifest: {manifest_path}")
        return

    manifest = read_json(manifest_path)
    prompts = manifest.get("interface", {}).get("defaultPrompt")
    if not isinstance(prompts, list):
        state.fail("cached manifest interface.defaultPrompt must be a list")
    elif len(prompts) > 3:
        state.fail("cached manifest exceeds Codex's three default prompt limit")
    else:
        state.ok(f"cached manifest defaultPrompt count is {len(prompts)}")

    missing = []
    for skill in EXPECTED_SKILLS:
        if not (cache / "skills" / skill / "SKILL.md").exists():
            missing.append(skill)
    if missing:
        state.fail("cached skills missing: " + ", ".join(missing))
    else:
        state.ok(f"Codex cache contains all {len(EXPECTED_SKILLS)} skills")


def check_skill_homes(state: CheckState, homes: list[Path]) -> None:
    for home in homes:
        missing = []
        wrong = []
        for skill in EXPECTED_SKILLS:
            dest = home.expanduser() / skill
            if not dest.exists():
                missing.append(skill)
                continue
            if dest.resolve() != (ROOT / "skills" / skill).resolve():
                wrong.append(f"{skill}->{dest.resolve()}")
        if missing:
            state.fail(f"{home} missing links: {', '.join(missing)}")
        elif wrong:
            state.fail(f"{home} has wrong targets: {', '.join(wrong[:3])}")
        else:
            state.ok(f"{home} links all {len(EXPECTED_SKILLS)} skills")


def check_codex_plugin_list(state: CheckState) -> None:
    try:
        result = subprocess.run(
            ["codex", "plugin", "list"],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError:
        state.warn("codex CLI not found; skipped codex plugin list")
        return

    combined = result.stdout + result.stderr
    if "elon-musk@personal" in combined and "installed, enabled" in combined:
        state.ok("codex plugin list shows elon-musk@personal installed and enabled")
    else:
        state.fail("codex plugin list does not show elon-musk@personal installed and enabled")


def check_prompt_visibility(state: CheckState, strict: bool) -> None:
    try:
        result = subprocess.run(
            ["codex", "debug", "prompt-input"],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError:
        state.warn("codex CLI not found; skipped prompt-input visibility check")
        return

    combined = result.stdout + result.stderr
    visible = [skill for skill in EXPECTED_SKILLS if skill in combined]
    if "skills context budget" in combined or "skills scan truncated" in combined:
        message = "Codex reported global skill budget or scan truncation"
        if strict:
            state.fail(message)
        else:
            state.warn(message)

    if "x-compound" in visible and "x-handoff" in visible:
        state.ok("prompt-input includes x-compound and x-handoff")
        return

    message = (
        "prompt-input does not include x-compound and x-handoff; installed cache may be valid, "
        "but automatic x-* invocation is unreliable in this Codex profile"
    )
    if strict:
        state.fail(message)
    else:
        state.warn(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the local elon-musk install")
    parser.add_argument(
        "--plugin",
        action="store_true",
        help="Check the Codex personal marketplace, plugin link, cache, and plugin list",
    )
    parser.add_argument(
        "--prompt-input",
        action="store_true",
        help="Also inspect codex debug prompt-input for model-visible skills",
    )
    parser.add_argument(
        "--strict-prompt-input",
        action="store_true",
        help="Fail if prompt-input does not expose x-compound and x-handoff",
    )
    parser.add_argument(
        "--skill-links",
        action="store_true",
        help="Check the default direct skill-home symlinks",
    )
    parser.add_argument(
        "--skill-home",
        type=Path,
        action="append",
        default=[],
        help="Skill home to check. Repeat for multiple homes. Implies --skill-links.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = CheckState()
    version = repo_version()
    check_plugin = args.plugin or not (args.skill_links or args.skill_home)

    if check_plugin:
        check_marketplace(state)
        check_plugin_link(state)
        check_codex_cache(state, version)
        check_codex_plugin_list(state)
    else:
        state.ok("Codex plugin check skipped; pass --plugin to validate marketplace/cache")

    if args.skill_links or args.skill_home:
        check_skill_homes(state, [p.expanduser() for p in args.skill_home] or DEFAULT_SKILL_HOMES)
    else:
        state.ok("direct skill-home link check skipped; pass --skill-links to validate symlinks")

    if args.prompt_input or args.strict_prompt_input:
        check_prompt_visibility(state, strict=args.strict_prompt_input)

    if state.warnings:
        print(f"warnings: {len(state.warnings)}")
    if state.failures:
        print(f"failures: {len(state.failures)}", file=sys.stderr)
        return 1
    print("install check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
