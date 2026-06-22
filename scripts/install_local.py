#!/usr/bin/env python3
"""Install the elon-musk plugin locally.

This can register the plugin in a personal marketplace and/or symlink the
x-prefixed skills into local agent skill homes.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "elon-musk"
DEFAULT_MARKETPLACE = Path.home() / ".agents" / "plugins" / "marketplace.json"
DEFAULT_PLUGIN_LINK = Path.home() / "plugins" / PLUGIN_NAME
DEFAULT_SKILL_HOMES = [
    Path.home() / ".agents" / "skills",
    Path.home() / ".codex" / "skills",
    Path.home() / ".claude" / "skills",
    Path.home() / ".openclaw" / "skills",
    Path.home() / ".openclaw" / "acpx" / "codex-home" / "skills",
]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {
            "name": "personal",
            "interface": {"displayName": "Personal"},
            "plugins": [],
        }
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    data.setdefault("name", "personal")
    data.setdefault("interface", {"displayName": "Personal"})
    data.setdefault("plugins", [])
    if not isinstance(data["plugins"], list):
        raise ValueError(f"{path} plugins field must be a list")
    return data


def marketplace_entry() -> dict:
    return {
        "name": PLUGIN_NAME,
        "source": {
            "source": "local",
            "path": f"./plugins/{PLUGIN_NAME}",
        },
        "policy": {
            "installation": "AVAILABLE",
            "authentication": "ON_INSTALL",
        },
        "category": "Productivity",
    }


def remove_destination(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def ensure_plugin_link(dest: Path, force: bool, dry_run: bool) -> None:
    dest = dest.expanduser()
    if dest.resolve() == ROOT.resolve() if dest.exists() or dest.is_symlink() else False:
        print(f"Plugin path already points to source: {dest}")
        return

    if dest.exists() or dest.is_symlink():
        if not force:
            raise RuntimeError(
                f"{dest} already exists and does not point to {ROOT}. "
                "Move it, remove it, or rerun with --force."
            )
        print(f"{'Would replace' if dry_run else 'Replacing'} plugin path: {dest}")
        if not dry_run:
            remove_destination(dest)

    print(f"{'Would link' if dry_run else 'Linking'} {dest} -> {ROOT}")
    if not dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.symlink_to(ROOT)


def update_marketplace(path: Path, dry_run: bool) -> None:
    data = load_json(path)
    plugins = data["plugins"]
    entry = marketplace_entry()
    replaced = False

    for index, existing in enumerate(plugins):
        if isinstance(existing, dict) and existing.get("name") == PLUGIN_NAME:
            if existing == entry:
                print(f"Marketplace already has {PLUGIN_NAME}: {path}")
                return
            plugins[index] = entry
            replaced = True
            break

    if not replaced:
        plugins.append(entry)

    print(f"{'Would update' if dry_run else 'Updated'} marketplace: {path}")
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def link_one(source: Path, dest: Path, force: bool, dry_run: bool) -> str:
    if dest.exists() or dest.is_symlink():
        if dest.is_symlink() and dest.resolve() == source.resolve():
            return "already"
        if not force:
            return "skipped"
        if not dry_run:
            remove_destination(dest)
    if not dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.symlink_to(source)
    return "linked"


def symlink_skills(skill_homes: list[Path], force: bool, dry_run: bool) -> None:
    skill_sources = sorted((ROOT / "skills").glob("x-*"))
    if not skill_sources:
        raise RuntimeError("No x-* skills found")

    counts = {"linked": 0, "already": 0, "skipped": 0}
    for home in skill_homes:
        home = home.expanduser()
        print(f"Skill home: {home}")
        for source in skill_sources:
            dest = home / source.name
            status = link_one(source, dest, force=force, dry_run=dry_run)
            counts[status] += 1
            if status == "skipped":
                print(f"  skipped existing {dest}")
        if dry_run:
            print("  dry run only")

    print(
        "Symlink summary: "
        + ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install the elon-musk plugin locally")
    parser.add_argument("--marketplace", action="store_true", help="Add plugin to marketplace.json")
    parser.add_argument(
        "--marketplace-path",
        type=Path,
        default=DEFAULT_MARKETPLACE,
        help=f"Marketplace path (default: {DEFAULT_MARKETPLACE})",
    )
    parser.add_argument(
        "--plugin-link",
        type=Path,
        default=DEFAULT_PLUGIN_LINK,
        help=f"Local plugin path used by personal marketplace (default: {DEFAULT_PLUGIN_LINK})",
    )
    parser.add_argument("--symlink-skills", action="store_true", help="Symlink x-* skills into skill homes")
    parser.add_argument(
        "--skill-home",
        type=Path,
        action="append",
        default=[],
        help="Skill home to link into. Repeat for multiple homes. Defaults to common homes.",
    )
    parser.add_argument("--force", action="store_true", help="Replace existing destinations")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.marketplace and not args.symlink_skills:
        print("Nothing to do. Pass --marketplace, --symlink-skills, or both.")
        return 2

    try:
        if args.marketplace:
            ensure_plugin_link(args.plugin_link, force=args.force, dry_run=args.dry_run)
            update_marketplace(args.marketplace_path.expanduser(), dry_run=args.dry_run)
        if args.symlink_skills:
            homes = [p.expanduser() for p in args.skill_home] or DEFAULT_SKILL_HOMES
            symlink_skills(homes, force=args.force, dry_run=args.dry_run)
    except Exception as exc:
        print(f"install failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
