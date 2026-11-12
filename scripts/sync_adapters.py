#!/usr/bin/env python3
"""Generate complete native skill mirrors; never delete unexpected files."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents/skills/release-compass"
TARGETS = [ROOT / ".claude/skills/release-compass", ROOT / ".grok/skills/release-compass"]


def files(path):
    return {p.relative_to(path) for p in path.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}


def sync(check=False):
    expected = files(SOURCE)
    problems = []
    for target in TARGETS:
        extras = files(target) - expected
        for path in sorted(extras):
            problems.append(f"Unexpected mirror file: {target / path}")
        for path in sorted(expected):
            source_file, dest_file = SOURCE / path, target / path
            if check:
                if not dest_file.exists() or source_file.read_bytes() != dest_file.read_bytes():
                    problems.append(f"Out-of-date mirror: {dest_file}")
            else:
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source_file, dest_file)
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    problems = sync(args.check)
    if problems:
        parser.exit(1, "\n".join(problems) + "\n")
    print("Native skill mirrors match." if args.check else "Updated native skill mirrors.")


if __name__ == "__main__":
    main()
