#!/usr/bin/env python3
"""Check local Markdown links in repository docs."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def markdown_files() -> list[Path]:
    result = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        result.append(path)
    for path in ROOT.rglob("*.mdc"):
        if ".git" not in path.parts:
            result.append(path)
    return sorted(result)


def is_external(target: str) -> bool:
    return (
        "://" in target
        or target.startswith("#")
        or target.startswith("mailto:")
        or target.startswith("app://")
    )


def normalize_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target.split("#", 1)[0]


def main() -> int:
    failures = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1)
            if is_external(raw):
                continue
            target = normalize_target(raw)
            if not target:
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{path.relative_to(ROOT)} links outside repo: {raw}")
                continue
            if not candidate.exists():
                failures.append(f"{path.relative_to(ROOT)} missing link target: {raw}")

    if failures:
        print("markdown link check failed:")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print(f"markdown link check passed: {len(markdown_files())} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
