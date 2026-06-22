#!/usr/bin/env python3
"""Validate the public elon-musk plugin repository."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
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
BANNED = ["TO" + "DO", "[TO" + "DO", "FIX" + "ME", "Complete and " + "informative"]
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py"}


def fail(message: str) -> None:
    print(f"validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"{path} is not UTF-8 text")


def repository_files() -> list[Path]:
    """Return tracked and untracked non-ignored files for public validation."""

    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return [path for path in ROOT.rglob("*") if path.is_file()]

    files = []
    for rel in result.stdout.splitlines():
        path = ROOT / rel
        if path.is_file():
            files.append(path)
    return files


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("skill frontmatter missing")
    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = json.loads(value)
        frontmatter[key.strip()] = value
    return frontmatter


def validate_plugin_json() -> None:
    path = ROOT / ".codex-plugin" / "plugin.json"
    if not path.exists():
        fail("missing .codex-plugin/plugin.json")
    data = json.loads(read_text(path))
    if data.get("name") != "elon-musk":
        fail("plugin name must be elon-musk")
    if data.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")
    interface = data.get("interface")
    if not isinstance(interface, dict):
        fail("plugin interface must be an object")
    for key in ["displayName", "shortDescription", "longDescription", "defaultPrompt"]:
        if not interface.get(key):
            fail(f"plugin interface missing {key}")
    if data.get("repository") != "https://github.com/thepraggyverse/elon-musk":
        fail("plugin repository URL is missing or wrong")
    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or len(prompts) < 3:
        fail("plugin interface defaultPrompt must be a list of at least three prompts")
    if len(prompts) > 3:
        fail("plugin interface defaultPrompt must not exceed Codex's three prompt limit")


def validate_auxiliary_manifests() -> None:
    claude = ROOT / ".claude-plugin" / "plugin.json"
    if not claude.exists():
        fail("missing .claude-plugin/plugin.json")
    data = json.loads(read_text(claude))
    if data.get("name") != "elon-musk":
        fail("claude plugin name must be elon-musk")
    skills = data.get("skills")
    if not isinstance(skills, list):
        fail("claude plugin skills must be a list")
    expected_paths = [f"./skills/{skill}" for skill in EXPECTED_SKILLS]
    if sorted(skills) != sorted(expected_paths):
        fail("claude plugin skills list does not match expected inventory")

    claude_marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    if not claude_marketplace.exists():
        fail("missing .claude-plugin/marketplace.json")
    marketplace = json.loads(read_text(claude_marketplace))
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not any(p.get("name") == "elon-musk" for p in plugins if isinstance(p, dict)):
        fail("claude marketplace missing elon-musk entry")

    codex_marketplace = ROOT / ".agents" / "plugins" / "marketplace.json"
    if not codex_marketplace.exists():
        fail("missing .agents/plugins/marketplace.json")
    codex_data = json.loads(read_text(codex_marketplace))
    entries = codex_data.get("plugins")
    if not isinstance(entries, list) or not entries:
        fail("repo-local codex marketplace has no plugins")
    entry = entries[0]
    if entry.get("name") != "elon-musk":
        fail("repo-local codex marketplace first plugin must be elon-musk")
    if entry.get("source", {}).get("path") != "./":
        fail("repo-local codex marketplace should point at repo root")
    if entry.get("policy", {}).get("installation") != "AVAILABLE":
        fail("repo-local codex marketplace installation policy must be AVAILABLE")


def validate_skills() -> int:
    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        fail("missing skills directory")
    actual = sorted(path.name for path in skills_dir.iterdir() if path.is_dir())
    if actual != sorted(EXPECTED_SKILLS):
        fail(f"skill inventory mismatch: {actual}")

    for skill_name in EXPECTED_SKILLS:
        skill_dir = skills_dir / skill_name
        skill_md = skill_dir / "SKILL.md"
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if not skill_md.exists():
            fail(f"{skill_name} missing SKILL.md")
        if not openai_yaml.exists():
            fail(f"{skill_name} missing agents/openai.yaml")
        text = read_text(skill_md)
        fm = parse_frontmatter(text)
        if fm.get("name") != skill_name:
            fail(f"{skill_name} frontmatter name mismatch")
        if len(fm.get("description", "")) < 120:
            fail(f"{skill_name} description too short")
        if any(token in text for token in BANNED):
            fail(f"{skill_name} contains placeholder text")
        yaml_text = read_text(openai_yaml)
        if f"${skill_name}" not in yaml_text:
            fail(f"{skill_name} openai.yaml default prompt must mention ${skill_name}")
    return len(EXPECTED_SKILLS)


def validate_references() -> None:
    required = [
        "book-map.md",
        "method-catalog.md",
        "source-notes.md",
    ]
    for rel in required:
        path = ROOT / "references" / rel
        if not path.exists():
            fail(f"missing references/{rel}")
    catalog = read_text(ROOT / "references" / "method-catalog.md")
    for skill in EXPECTED_SKILLS:
        if skill == "x-router":
            continue
        if f"## {skill}" not in catalog:
            fail(f"method catalog missing {skill}")


def validate_docs() -> None:
    required = [
        "AGENTS.md",
        "CLAUDE.md",
        "README.md",
        "CHANGELOG.md",
        "CONCEPTS.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "docs/COMPOUND_ENGINEERING.md",
        "docs/DOCUMENTATION_AUDIT.md",
        "docs/HARNESS_MATRIX.md",
        "docs/INSTALL.md",
        "docs/MEMORY_MODEL.md",
        "docs/REFERENCE_AUDIT.md",
        "docs/RELEASE.md",
        "docs/SYMLINKS.md",
        "docs/USAGE.md",
        "docs/DEVELOPMENT.md",
        "docs/SOURCE_BOUNDARIES.md",
        "PRIVACY.md",
        "SECURITY.md",
        ".github/workflows/validate.yml",
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        ".agents/plugins/marketplace.json",
        "scripts/check_install.py",
        "scripts/install_local.py",
        "scripts/validate_public.py",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")

    readme = read_text(ROOT / "README.md")
    if "17 searchable `x-*` skills" not in readme:
        fail("README must state the 17-skill inventory")
    if "CHANGELOG.md" not in readme:
        fail("README must link the changelog")

    changelog = read_text(ROOT / "CHANGELOG.md")
    for phrase in ["## Unreleased", "x-compound", "x-handoff", "scripts/check_install.py"]:
        if phrase not in changelog:
            fail(f"CHANGELOG.md missing {phrase}")

    privacy = read_text(ROOT / "PRIVACY.md")
    for phrase in ["does not include telemetry", "does not save raw session logs by default", "docs/reviews/"]:
        if phrase not in privacy:
            fail(f"PRIVACY.md missing {phrase}")

    security = read_text(ROOT / "SECURITY.md")
    for phrase in ["Reporting A Vulnerability", "praggy.dev@gmail.com", "does not run a hosted backend service"]:
        if phrase not in security:
            fail(f"SECURITY.md missing {phrase}")

    release = read_text(ROOT / "docs" / "RELEASE.md")
    for phrase in ["CHANGELOG.md", "No-Push Default", "scripts/check_install.py --plugin --skill-links"]:
        if phrase not in release:
            fail(f"docs/RELEASE.md missing {phrase}")

    doc_audit = read_text(ROOT / "docs" / "DOCUMENTATION_AUDIT.md")
    for phrase in [
        "EveryInc/compound-engineering-plugin",
        "mattpocock/skills",
        "CHANGELOG.md",
        "SECURITY.md",
        "PRIVACY.md",
        "Patterns Intentionally Deferred",
    ]:
        if phrase not in doc_audit:
            fail(f"docs/DOCUMENTATION_AUDIT.md missing {phrase}")


def validate_memory_model() -> None:
    memory = read_text(ROOT / "docs" / "MEMORY_MODEL.md")
    required_phrases = [
        "docs/reviews/",
        "docs/lessons/",
        "docs/handoffs/",
        "Do not save",
        "does not read raw session logs by default",
    ]
    for phrase in required_phrases:
        if phrase not in memory:
            fail(f"docs/MEMORY_MODEL.md missing {phrase}")

    for rel in [
        "skills/x-compound/SKILL.md",
        "skills/x-handoff/SKILL.md",
        "README.md",
        "docs/MEMORY_MODEL.md",
    ]:
        text = read_text(ROOT / rel).lower()
        forbidden = [
            "session-history",
            "local jsonl discovery",
            "extract session logs",
            "mine session logs",
        ]
        for phrase in forbidden:
            if phrase in text:
                fail(f"{rel} appears to claim default session-log mining: {phrase}")


def validate_hygiene() -> None:
    for path in repository_files():
        if path.suffix in TEXT_SUFFIXES:
            text = read_text(path)
            if any(token in text for token in BANNED):
                fail(f"{path.relative_to(ROOT)} contains placeholder text")
            try:
                path.read_bytes().decode("ascii")
            except UnicodeDecodeError as exc:
                fail(f"{path.relative_to(ROOT)} contains non-ASCII bytes: {exc}")


def optional_codex_validators() -> None:
    plugin_validator = Path.home() / ".codex" / "skills" / ".system" / "plugin-creator" / "scripts" / "validate_plugin.py"
    skill_validator = Path.home() / ".codex" / "skills" / ".system" / "skill-creator" / "scripts" / "quick_validate.py"

    if plugin_validator.exists():
        subprocess.run([sys.executable, str(plugin_validator), str(ROOT)], check=True)
    if skill_validator.exists():
        for skill in EXPECTED_SKILLS:
            subprocess.run([sys.executable, str(skill_validator), str(ROOT / "skills" / skill)], check=True)


def main() -> int:
    validate_plugin_json()
    validate_auxiliary_manifests()
    skill_count = validate_skills()
    validate_references()
    validate_docs()
    validate_memory_model()
    validate_hygiene()
    optional_codex_validators()
    print(f"Public validation passed: {skill_count} x-prefixed skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
