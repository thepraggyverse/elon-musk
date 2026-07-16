"""Shared direct-skill installation profiles."""

from __future__ import annotations

from pathlib import Path


PROFILE_SKILL_HOMES = {
    "agents": (Path.home() / ".agents" / "skills",),
    "codex": (Path.home() / ".codex" / "skills",),
    "claude": (Path.home() / ".claude" / "skills",),
    "openclaw": (Path.home() / ".openclaw" / "skills",),
    "openclaw-codex": (Path.home() / ".openclaw" / "acpx" / "codex-home" / "skills",),
}
PROFILE_CHOICES = tuple(PROFILE_SKILL_HOMES) + ("all",)


def resolve_skill_homes(profiles: list[str], custom_homes: list[Path]) -> list[Path]:
    homes = [path.expanduser() for path in custom_homes]
    selected = list(PROFILE_SKILL_HOMES) if "all" in profiles else profiles
    for profile in selected:
        homes.extend(PROFILE_SKILL_HOMES[profile])

    unique = []
    seen = set()
    for home in homes:
        key = str(home)
        if key not in seen:
            seen.add(key)
            unique.append(home)
    return unique
