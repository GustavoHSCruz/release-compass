#!/usr/bin/env python3
"""Copy the complete skill to an explicitly selected host discovery directory."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents/skills/release-compass"
LOCATIONS = {"claude": ".claude", "codex": ".agents", "gemini": ".gemini", "grok": ".grok"}


def install(agent, base, dry_run=False):
    destination = Path(base).expanduser().resolve() / LOCATIONS[agent] / "skills/release-compass"
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Already exists; nothing overwritten: {destination}")
    # Reject redirected parent directories rather than writing through symlinks.
    if destination.resolve() != destination:
        raise ValueError(f"Destination uses a symlinked parent: {destination}")
    if SOURCE.resolve() in destination.parents:
        raise ValueError("Cannot install inside the source skill")
    if dry_run:
        return destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True, choices=LOCATIONS)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--project", type=Path, help="Destination project directory")
    scope.add_argument("--user", action="store_true", help="Use the current user's home directory")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        destination = install(args.agent, Path.home() if args.user else args.project, args.dry_run)
    except (OSError, ValueError) as error:
        parser.exit(2, f"{error}\n")
    print(f'{"Would install" if args.dry_run else "Installed"}: {destination}')
    print("This copies the skill only. It does not change agent permissions, credentials or project instructions.")


if __name__ == "__main__":
    main()
