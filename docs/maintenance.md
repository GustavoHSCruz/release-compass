# Maintenance

## Source and content updates

Review changed vendor claims against primary documentation. Record the source
scope and checked date. Revise definitions and examples rather than copying
large portions of vendor documentation. Preserve the distinction between
editorial conventions and directly supported product examples.

Dates, client discovery behavior and support policies deserve rechecking before
a claim is used operationally. There is no automated freshness monitor.

## Generated files

Edit the canonical bundle in `.agents/skills/release-compass/`, then run:

```bash
python3 scripts/render_catalog.py
python3 scripts/sync_adapters.py
```

The first generates `docs/catalog.md`. The second writes complete Claude and
Grok mirrors from canonical files. It reports unexpected files rather than
silently deleting them. Review the diff before committing generated changes.
Gemini uses the shared `.agents/skills/` alias and has no duplicate bundle here.

## Validation

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validation checks schema-level invariants, alias collisions, source/related IDs,
skill metadata, local Markdown links, instruction imports and generated-file
drift. It deliberately does not assert HTTP link health or live agent discovery.
Tests cover search behavior and installation into disposable directories,
including lookup after the source checkout is unavailable.

For client behavior, run [the manual scenarios](../evals/scenarios.json) in the
actual installed client. Record client/model versions, date, prompt, observed
result and pass/fail rationale. Never replace this evidence with a blanket
"works with all agents" badge.
