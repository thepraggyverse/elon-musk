import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = [
    "x-setup",
    "x-router",
    "x-review-pack",
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
    "x-memory-refresh",
    "x-handoff",
]
NON_METHOD_CATALOG_EXEMPT = {"x-setup", "x-router"}
NON_ROUTER_SKILLS = [name for name in EXPECTED_SKILLS if name != "x-router"]
BANNED_PLACEHOLDERS = [
    "TO" + "DO",
    "[TO" + "DO",
    "FIX" + "ME",
    "plugin " + "scaffold",
    "Complete and " + "informative",
]
TEXT_SUFFIXES = {".md", ".mdc", ".json", ".yaml", ".yml", ".py"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise AssertionError("missing YAML frontmatter block")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise AssertionError(f"invalid frontmatter line: {line!r}")
        result[key.strip()] = value.strip().strip('"')
    return result


def repository_files() -> list[Path]:
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


class PluginManifestTests(unittest.TestCase):
    def test_manifest_is_valid_and_specific(self):
        manifest_path = ROOT / ".codex-plugin" / "plugin.json"
        data = json.loads(read_text(manifest_path))

        self.assertEqual(data["name"], "elon-musk")
        self.assertEqual(data["skills"], "./skills/")
        self.assertIn("strategy", data["description"])
        self.assertEqual(data["repository"], "https://github.com/thepraggyverse/elon-musk")
        self.assertEqual(data["interface"]["displayName"], "Elon Musk Methods")
        self.assertTrue(any("x-router" in prompt for prompt in data["interface"]["defaultPrompt"]))
        self.assertLessEqual(len(data["interface"]["defaultPrompt"]), 3)
        self.assertFalse(any(token in json.dumps(data) for token in BANNED_PLACEHOLDERS))

    def test_claude_manifest_lists_public_skills(self):
        manifest_path = ROOT / ".claude-plugin" / "plugin.json"
        data = json.loads(read_text(manifest_path))

        self.assertEqual(data["name"], "elon-musk")
        self.assertEqual(data["repository"], "https://github.com/thepraggyverse/elon-musk")
        self.assertEqual(
            sorted(data["skills"]),
            sorted(f"./skills/{name}" for name in EXPECTED_SKILLS),
        )

    def test_repo_local_marketplace_points_to_plugin_root(self):
        marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
        data = json.loads(read_text(marketplace_path))
        self.assertEqual(data["name"], "elon-musk-methods")
        entries = {entry["name"]: entry for entry in data["plugins"]}
        self.assertIn("elon-musk", entries)
        self.assertEqual(entries["elon-musk"]["source"]["path"], "./")
        self.assertEqual(entries["elon-musk"]["policy"]["installation"], "AVAILABLE")
        self.assertEqual(entries["elon-musk"]["policy"]["authentication"], "ON_INSTALL")

    def test_personal_marketplace_entry_points_to_symlink_when_present(self):
        marketplace = Path.home() / ".agents" / "plugins" / "marketplace.json"
        if not marketplace.exists():
            self.skipTest("personal marketplace is not present on this machine")

        data = json.loads(read_text(marketplace))
        entries = {entry["name"]: entry for entry in data.get("plugins", [])}
        self.assertIn("elon-musk", entries)
        self.assertEqual(entries["elon-musk"]["source"]["path"], "./plugins/elon-musk")
        self.assertEqual(entries["elon-musk"]["policy"]["installation"], "AVAILABLE")
        self.assertEqual(entries["elon-musk"]["policy"]["authentication"], "ON_INSTALL")

        linked_plugin = Path.home() / "plugins" / "elon-musk"
        self.assertTrue(linked_plugin.exists(), linked_plugin)
        linked_manifest = linked_plugin.resolve() / ".codex-plugin" / "plugin.json"
        self.assertTrue(linked_manifest.exists(), linked_manifest)
        self.assertEqual(json.loads(read_text(linked_manifest))["name"], "elon-musk")
        if ROOT == linked_plugin.resolve():
            self.assertEqual(linked_plugin.resolve(), ROOT)


class SkillInventoryTests(unittest.TestCase):
    def test_skill_inventory_is_exact_and_searchable(self):
        actual = sorted(path.name for path in (ROOT / "skills").iterdir() if path.is_dir())
        self.assertEqual(sorted(EXPECTED_SKILLS), actual)
        for name in actual:
            self.assertRegex(name, r"^x-[a-z0-9-]+$")
            self.assertLessEqual(len(name), 64)

    def test_every_skill_has_required_files(self):
        for name in EXPECTED_SKILLS:
            with self.subTest(skill=name):
                skill_dir = ROOT / "skills" / name
                self.assertTrue((skill_dir / "SKILL.md").is_file())
                self.assertTrue((skill_dir / "agents" / "openai.yaml").is_file())


class SkillContentTests(unittest.TestCase):
    def test_frontmatter_matches_folder_and_has_rich_trigger_description(self):
        for name in EXPECTED_SKILLS:
            with self.subTest(skill=name):
                text = read_text(ROOT / "skills" / name / "SKILL.md")
                frontmatter = parse_frontmatter(text)
                self.assertEqual(frontmatter["name"], name)
                description = frontmatter["description"]
                self.assertGreaterEqual(len(description), 120)
                self.assertIn("Use", description)
                self.assertFalse(any(token in description for token in BANNED_PLACEHOLDERS))

    def test_skill_bodies_have_operational_sections(self):
        for name in EXPECTED_SKILLS:
            with self.subTest(skill=name):
                text = read_text(ROOT / "skills" / name / "SKILL.md")
                body = text.split("---\n", 2)[-1]
                self.assertIn("# ", body)
                self.assertIn("## Output", body)
                self.assertIn("## Example", body)
                self.assertLess(len(body.splitlines()), 500)
                self.assertFalse(any(token in body for token in BANNED_PLACEHOLDERS))

    def test_router_mentions_every_other_skill(self):
        router = read_text(ROOT / "skills" / "x-router" / "SKILL.md")
        for name in NON_ROUTER_SKILLS:
            with self.subTest(skill=name):
                self.assertIn(f"`{name}`", router)

    def test_openai_yaml_default_prompts_reference_the_skill(self):
        for name in EXPECTED_SKILLS:
            with self.subTest(skill=name):
                yaml_text = read_text(ROOT / "skills" / name / "agents" / "openai.yaml")
                self.assertIn("interface:", yaml_text)
                self.assertIn(f"${name}", yaml_text)
                self.assertFalse(any(token in yaml_text for token in BANNED_PLACEHOLDERS))


class DocumentationCoverageTests(unittest.TestCase):
    def test_readme_lists_all_top_level_skills(self):
        readme = read_text(ROOT / "README.md")
        for name in EXPECTED_SKILLS:
            with self.subTest(skill=name):
                self.assertIn(f"`{name}`", readme)

    def test_catalog_has_all_non_router_skill_sections(self):
        catalog = read_text(ROOT / "references" / "method-catalog.md")
        for name in EXPECTED_SKILLS:
            if name in NON_METHOD_CATALOG_EXEMPT:
                continue
            with self.subTest(skill=name):
                self.assertIn(f"## {name}", catalog)

    def test_book_map_references_every_non_router_skill(self):
        book_map = read_text(ROOT / "references" / "book-map.md")
        for name in NON_ROUTER_SKILLS:
            with self.subTest(skill=name):
                self.assertIn(f"`{name}`", book_map)

    def test_examples_cover_major_use_modes(self):
        examples_dir = ROOT / "examples"
        examples = {path.name: read_text(path) for path in examples_dir.glob("*.md")}
        self.assertEqual(
            {
                "all-skills.md",
                "startup-review.md",
                "feature-plan-review.md",
                "org-review.md",
                "cost-review.md",
                *(f"{name}.md" for name in EXPECTED_SKILLS),
            },
            set(examples),
        )
        combined = "\n".join(examples.values())
        for name in EXPECTED_SKILLS:
            with self.subTest(skill=name):
                self.assertIn(name, combined)

    def test_readme_has_skill_compatibility_table(self):
        readme = read_text(ROOT / "README.md")
        for phrase in [
            "Compatibility Quick Scan",
            "Output artifact",
            "Writes files?",
            "Safe default?",
            "x-setup",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, readme)

    def test_harness_docs_cover_install_update_and_uninstall(self):
        harness = read_text(ROOT / "docs" / "HARNESS_MATRIX.md")
        for phrase in [
            "Codex app",
            "Codex CLI",
            "Claude Code",
            "OpenClaw",
            "Update Checklist",
            "Uninstall Checklist",
            "scripts/check_install.py",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, harness)
        self.assertIn("Codex Skill Budget Check", harness)

    def test_agents_and_readme_explain_repo_contract(self):
        agents = read_text(ROOT / "AGENTS.md")
        readme = read_text(ROOT / "README.md")
        self.assertIn("canonical authoring contract", agents)
        self.assertIn("20 searchable `x-*` skills", readme)
        self.assertIn("Skill Inventory", readme)
        self.assertIn("Harness Matrix", readme)
        self.assertIn("CHANGELOG.md", readme)
        self.assertIn("SECURITY.md", readme)
        self.assertIn("PRIVACY.md", readme)
        self.assertIn("Disclaimer", readme)

    def test_public_docs_cover_release_security_privacy_and_audit(self):
        required = [
            "CHANGELOG.md",
            "SECURITY.md",
            "PRIVACY.md",
            "docs/RELEASE.md",
            "docs/DOCUMENTATION_AUDIT.md",
            "docs/NATIVE_HARNESS_BRIDGES.md",
            "docs/SKILL_INDEX.md",
            "GEMINI.md",
            "gemini-extension.json",
            ".cursor/rules/elon-musk-methods.mdc",
            ".continue/rules/elon-musk-methods.md",
            ".opencode/AGENTS.md",
            ".goosehints",
            "scripts/build_index.py",
            "scripts/check_markdown_links.py",
        ]
        for rel in required:
            with self.subTest(path=rel):
                self.assertTrue((ROOT / rel).is_file())

        changelog = read_text(ROOT / "CHANGELOG.md")
        for phrase in [
            "## Unreleased",
            "x-review-pack",
            "x-memory-refresh",
            "x-setup",
            "x-compound",
            "x-handoff",
            "scripts/check_install.py",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, changelog)

        security = read_text(ROOT / "SECURITY.md")
        for phrase in ["Reporting A Vulnerability", "praggy.dev@gmail.com", "does not run a hosted backend service"]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, security)

        privacy = read_text(ROOT / "PRIVACY.md")
        for phrase in ["does not include telemetry", "does not save raw session logs by default", "docs/reviews/"]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, privacy)

        release = read_text(ROOT / "docs" / "RELEASE.md")
        for phrase in ["CHANGELOG.md", "No-Push Default", "scripts/check_install.py --plugin --skill-links"]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, release)

        audit = read_text(ROOT / "docs" / "DOCUMENTATION_AUDIT.md")
        for phrase in [
            "EveryInc/compound-engineering-plugin",
            "mattpocock/skills",
            "CHANGELOG.md",
            "SECURITY.md",
            "PRIVACY.md",
            "Patterns Intentionally Deferred",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, audit)

    def test_memory_model_documents_local_compounding(self):
        memory = read_text(ROOT / "docs" / "MEMORY_MODEL.md")
        for phrase in [
            "docs/reviews/",
            "docs/lessons/",
            "docs/handoffs/",
            "Do not save",
            "does not read raw session logs by default",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, memory)

    def test_compounding_skills_do_not_claim_session_log_mining(self):
        combined = "\n".join(
            read_text(ROOT / rel)
            for rel in [
                "skills/x-compound/SKILL.md",
                "skills/x-memory-refresh/SKILL.md",
                "skills/x-handoff/SKILL.md",
                "skills/x-review-pack/SKILL.md",
                "skills/x-setup/SKILL.md",
                "README.md",
                "docs/MEMORY_MODEL.md",
            ]
        ).lower()
        for phrase in [
            "session-history",
            "local jsonl discovery",
            "extract session logs",
            "mine session logs",
        ]:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, combined)


class HygieneTests(unittest.TestCase):
    def test_no_placeholder_or_scaffold_language_remains(self):
        for path in repository_files():
            if path.suffix in {".md", ".json", ".yaml"}:
                with self.subTest(path=path.relative_to(ROOT)):
                    text = read_text(path)
                    self.assertFalse(any(token in text for token in BANNED_PLACEHOLDERS))

    def test_ascii_only_for_portable_plugin_files(self):
        for path in repository_files():
            if path.suffix in TEXT_SUFFIXES:
                with self.subTest(path=path.relative_to(ROOT)):
                    data = path.read_bytes()
                    try:
                        data.decode("ascii")
                    except UnicodeDecodeError as exc:
                        self.fail(f"{path.relative_to(ROOT)} contains non-ASCII bytes: {exc}")

    def test_source_notes_protect_against_verbatim_book_copying(self):
        notes = read_text(ROOT / "references" / "source-notes.md")
        self.assertIn("Do not copy long passages", notes)
        self.assertIn("paraphrased method summaries", notes)

    def test_generated_indexes_are_current(self):
        result = subprocess.run(
            ["python3", "scripts/build_index.py", "--check"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
