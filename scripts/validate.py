#!/usr/bin/env python3
"""Validate catalog invariants, references, links, metadata and generated files."""
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

from render_catalog import render
from sync_adapters import sync

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / ".agents/skills/release-compass"
CATEGORIES = {"maturity", "channel", "access", "support", "cadence", "change", "deployment", "versioning"}


def normalize(text):
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


def validate():
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)

    data = json.loads((PACK / "data/terms.json").read_text(encoding="utf-8"))
    registry = json.loads((PACK / "data/sources.json").read_text(encoding="utf-8"))
    require(data["schema_version"] == registry["schema_version"] == 1, "Unsupported schema version")
    terms, sources = data["terms"], registry["sources"]
    require(bool(terms) and bool(sources), "Catalog and source registry must not be empty")
    ids, source_ids = {t["id"] for t in terms}, {s["id"] for s in sources}
    require(len(ids) == len(terms), "Duplicate term IDs")
    require(len(source_ids) == len(sources), "Duplicate source IDs")
    aliases = {}
    term_keys = {"id", "label", "aliases", "category", "definition", "caveat", "source_ids", "evidence", "related"}
    for term in terms:
        name = term["id"]
        require(set(term) == term_keys, f"{name}: unexpected or missing fields")
        require(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)), f"Invalid ID: {name}")
        require(term["category"] in CATEGORIES, f"Unknown category: {name}")
        for field in ("label", "definition", "caveat", "evidence"):
            require(isinstance(term[field], str) and bool(term[field].strip()), f"Missing {field}: {name}")
        for field in ("aliases", "source_ids", "related"):
            require(isinstance(term[field], list) and all(isinstance(x, str) for x in term[field]), f"Invalid {field}: {name}")
            require(len(term[field]) == len(set(term[field])), f"Duplicate {field}: {name}")
        require(set(term["source_ids"]) <= source_ids, f"Unknown source: {name}")
        require(set(term["related"]) <= ids and name not in term["related"], f"Invalid related IDs: {name}")
        expected_evidence = "editorial-synthesis-with-supporting-example" if term["source_ids"] else "editorial-convention"
        require(term["evidence"] == expected_evidence, f"Evidence/source mismatch: {name}")
        for alias in [name, term["label"], *term["aliases"]]:
            key = normalize(alias)
            require(bool(key), f"Empty normalized alias: {name}")
            require(key not in aliases or aliases[key] == name, f"Alias collision: {alias}")
            aliases[key] = name
    reviewed = date.fromisoformat(registry["last_reviewed"])
    require(reviewed <= date.today(), "Review date is in the future")
    for source in sources:
        require(set(source) == {"id", "title", "url", "scope", "checked_on"}, f"Invalid source fields: {source['id']}")
        require(urlparse(source["url"]).scheme == "https", f"Non-HTTPS source: {source['id']}")
        require(date.fromisoformat(source["checked_on"]) <= reviewed, f"Invalid checked date: {source['id']}")
    text = (PACK / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", text)
    require(bool(match), "Skill needs portable name/description YAML frontmatter")
    if match:
        require(match[1] == PACK.name and len(match[1]) <= 64, "Skill name/directory mismatch")
        require(len(match[2]) <= 1024, "Skill description too long")
    require(len(text.splitlines()) < 500, "Skill should use selective references")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        # Validate local file targets. Anchors and remote links need separate review.
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            target = target.strip().split(" ")[0].strip("<>")
            if not target or target.startswith("#") or urlparse(target).scheme:
                continue
            local = unquote(target.split("#", 1)[0])
            require((path.parent / local).exists(), f"Broken local link: {path.relative_to(ROOT)} -> {target}")
    for filename in ("CLAUDE.md", "GEMINI.md"):
        require("@AGENTS.md" in (ROOT / filename).read_text(encoding="utf-8"), f"Missing shared import: {filename}")
    require((ROOT / "docs/catalog.md").read_text(encoding="utf-8") == render(), "Generated catalog drift")
    errors.extend(sync(check=True))
    return errors, len(terms), len(sources)


if __name__ == "__main__":
    try:
        problems, terms, sources = validate()
    except (KeyError, ValueError, TypeError, OSError) as error:
        sys.exit(f"Invalid repository data: {error}")
    if problems:
        sys.exit("\n".join(problems))
    print(f"Validated {terms} terms, {sources} sources, metadata, local links, imports and native mirrors.")
