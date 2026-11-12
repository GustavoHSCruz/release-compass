#!/usr/bin/env python3
"""Generate the human catalog from canonical JSON, or check it for drift."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / ".agents/skills/release-compass"


def render():
    terms = json.loads((PACK / "data/terms.json").read_text(encoding="utf-8"))["terms"]
    sources = {s["id"]: s for s in json.loads((PACK / "data/sources.json").read_text(encoding="utf-8"))["sources"]}
    lines = ["# Release terminology catalog", "",
             "An editorial glossary, not an exhaustive standard. Supporting sources illustrate",
             "usage; they do not formally define every term in every product. See the",
             "[source registry](../.agents/skills/release-compass/data/sources.json) for scope.", "",
             "Generated from [terms.json](../.agents/skills/release-compass/data/terms.json).",
             "Run `python3 scripts/render_catalog.py` after changing the data.", ""]
    for category in dict.fromkeys(t["category"] for t in terms):
        lines += [f"## {category.title()}", "", "| Term | Meaning | Caveat | Supporting background |",
                  "| --- | --- | --- | --- |"]
        for t in terms:
            if t["category"] != category:
                continue
            links = ", ".join(f'[{i}]({sources[i]["url"]})' for i in t["source_ids"])
            if not links:
                links = "Editorial convention; no direct primary definition verified"
            cells = [t["label"], t["definition"], t["caveat"], links]
            lines.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    target = ROOT / "docs/catalog.md"
    content = render()
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            parser.exit(1, "Catalog is out of date. Run python3 scripts/render_catalog.py\n")
        print("Catalog matches canonical JSON.")
    else:
        target.write_text(content, encoding="utf-8")
        print("Updated docs/catalog.md")


if __name__ == "__main__":
    main()
