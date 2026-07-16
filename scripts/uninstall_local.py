#!/usr/bin/env python3
"""Safely remove local links created for the elon-musk plugin."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from install_profiles import PROFILE_CHOICES, resolve_skill_homes


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "elon-musk"
DEFAULT_MARKETPLACE = Path.home() / ".agents" / "plugins" / "marketplace.json"
DEFAULT_PLUGIN_LINK = Path.home() / "plugins" / PLUGIN_NAME


def remove_skill_links(homes: list[Path], dry_run: bool) -> tuple[int, int]:
    removed = 0
    skipped = 0
    for home in homes:
        print(f"Skill home: {home}")
        for source in sorted((ROOT / "skills").glob("x-*")):
            dest = home / source.name
            if not dest.is_symlink():
                continue
            if dest.resolve() != source.resolve():
                print(f"  skipped foreign link {dest} -> {dest.resolve()}")
                skipped += 1
                continue
            print(f"  {'would remove' if dry_run else 'removed'} {dest}")
            if not dry_run:
                dest.unlink()
            removed += 1
    return removed, skipped


def remove_plugin_link(path: Path, dry_run: bool) -> bool:
    path = path.expanduser()
    if not path.is_symlink():
        print(f"Plugin link not removed because it is not a symlink: {path}")
        return False
    if path.resolve() != ROOT.resolve():
        print(f"Plugin link not removed because it points elsewhere: {path} -> {path.resolve()}")
        return False
    print(f"{'Would remove' if dry_run else 'Removed'} plugin link: {path}")
    if not dry_run:
        path.unlink()
    return True


def remove_marketplace_entry(path: Path, plugin_link: Path, dry_run: bool) -> bool:
    path = path.expanduser()
    plugin_link = plugin_link.expanduser()
    if not path.exists():
        print(f"Marketplace does not exist: {path}")
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    plugins = data.get("plugins")
    if not isinstance(plugins, list):
        raise ValueError(f"{path} plugins field must be a list")
    matching = [item for item in plugins if isinstance(item, dict) and item.get("name") == PLUGIN_NAME]
    if not matching:
        print(f"Marketplace has no {PLUGIN_NAME} entry: {path}")
        return False
    if not plugin_link.is_symlink() or plugin_link.resolve() != ROOT.resolve():
        target = plugin_link.resolve() if plugin_link.exists() or plugin_link.is_symlink() else "missing"
        print(f"Marketplace entry not removed because plugin link is not owned by this checkout: {plugin_link} -> {target}")
        return False

    expected_source = {"source": "local", "path": f"./plugins/{PLUGIN_NAME}"}
    kept = [
        item
        for item in plugins
        if not (
            isinstance(item, dict)
            and item.get("name") == PLUGIN_NAME
            and item.get("source") == expected_source
        )
    ]
    if len(kept) == len(plugins):
        print(f"Marketplace {PLUGIN_NAME} entry not removed because its source is foreign: {path}")
        return False
    data["plugins"] = kept
    print(f"{'Would update' if dry_run else 'Updated'} marketplace: {path}")
    if not dry_run:
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-links", action="store_true", help="Remove this checkout's direct skill links")
    parser.add_argument("--profile", choices=PROFILE_CHOICES, action="append", default=[])
    parser.add_argument("--skill-home", type=Path, action="append", default=[])
    parser.add_argument("--plugin-link", action="store_true", help="Remove the plugin source symlink if it targets this checkout")
    parser.add_argument("--plugin-link-path", type=Path, default=DEFAULT_PLUGIN_LINK)
    parser.add_argument("--marketplace", action="store_true", help="Remove the personal marketplace entry")
    parser.add_argument("--marketplace-path", type=Path, default=DEFAULT_MARKETPLACE)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not (args.skill_links or args.plugin_link or args.marketplace):
        print("Nothing to do. Select --skill-links, --plugin-link, or --marketplace.", file=sys.stderr)
        return 2
    if args.skill_links and not (args.profile or args.skill_home):
        print("uninstall failed: --skill-links requires --profile or --skill-home", file=sys.stderr)
        return 2
    try:
        if args.skill_links:
            removed, skipped = remove_skill_links(resolve_skill_homes(args.profile, args.skill_home), args.dry_run)
            print(f"Skill-link summary: matched={removed}, skipped_foreign={skipped}")
        if args.marketplace:
            remove_marketplace_entry(args.marketplace_path, args.plugin_link_path, args.dry_run)
        if args.plugin_link:
            remove_plugin_link(args.plugin_link_path, args.dry_run)
    except Exception as exc:
        print(f"uninstall failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
