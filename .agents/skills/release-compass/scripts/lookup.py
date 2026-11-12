#!/usr/bin/env python3
"""Search the bundled release catalog without dependencies or network access."""
import argparse
import json
from pathlib import Path
import re
import sys

PACK = Path(__file__).resolve().parents[1]


def normalize(value):
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def load_catalog():
    terms = json.loads((PACK / "data/terms.json").read_text(encoding="utf-8"))["terms"]
    sources = json.loads((PACK / "data/sources.json").read_text(encoding="utf-8"))
    return terms, sources


def select(terms, query):
    key = normalize(query)
    exact = [t for t in terms if key in {
        normalize(t["id"]), normalize(t["label"]),
        *(normalize(a) for a in t["aliases"]),
    }]
    if exact:
        return exact
    words = key.split()
    return [t for t in terms if all(word in normalize(" ".join([
        t["id"], t["label"], *t["aliases"], t["definition"], t["caveat"],
    ])) for word in words)]


def main(argv=None):
    terms, registry = load_catalog()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", help="Term, alias, or keywords")
    parser.add_argument("--compare", nargs="+", metavar="TERM", help="Resolve each term separately")
    parser.add_argument("--list", action="store_true", help="List the catalog")
    parser.add_argument("--category", choices=sorted({t["category"] for t in terms}))
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)
    if sum([bool(args.query), bool(args.compare), args.list]) > 1:
        parser.error("choose one of query, --compare, or --list")
    if args.query is None and not args.compare and not args.list and not args.category:
        parser.error("provide a query, --compare, --list, or --category")
    if args.query is not None and not normalize(args.query):
        parser.error("query must contain letters or numbers")
    pool = [t for t in terms if not args.category or t["category"] == args.category]
    missing = []
    if args.compare:
        results = []
        for query in args.compare:
            if not normalize(query):
                parser.error("comparison terms must contain letters or numbers")
            matches = select(pool, query)
            if not matches:
                missing.append(query)
            results.extend(t for t in matches if t not in results)
    else:
        results = select(pool, args.query) if args.query else pool
    source_map = {s["id"]: s for s in registry["sources"]}
    expanded = [dict(t, sources=[source_map[i] for i in t["source_ids"]]) for t in results]
    if args.format == "json":
        print(json.dumps({"schema_version": 1, "last_reviewed": registry["last_reviewed"],
                          "count": len(expanded), "missing": missing, "terms": expanded}, indent=2))
    else:
        for t in expanded:
            print(f'{t["label"]} [{t["category"]}]\n  {t["definition"]}\n  Caveat: {t["caveat"]}')
            if t["sources"]:
                print("  Supporting background: " + ", ".join(s["url"] for s in t["sources"]))
            else:
                print("  Evidence: editorial convention; no direct primary definition verified.")
        if not expanded:
            print("No matching terms.")
        if missing:
            print("Unmatched comparison terms: " + ", ".join(missing), file=sys.stderr)
    return 2 if missing or not results else 0


if __name__ == "__main__":
    sys.exit(main())
