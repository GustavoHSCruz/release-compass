# Contributing to Release Compass

Small, well-supported corrections are welcome. Keep changes focused on software
releases and agent usability. Use English for repository content.

## Propose a change

Search existing issues and the catalog first. Describe the concrete ambiguity or
missing behavior. For a vendor-specific claim, link its primary documentation
and state the product/client/version scope. For a general convention without a
verified primary definition, mark it as an editorial convention.

## Update the source of truth

- Add or revise terms in `.agents/skills/release-compass/data/terms.json`.
- Add supporting sources and checked dates to the adjacent `sources.json`.
- Keep IDs stable and aliases unambiguous.
- Keep the skill short; place details in its bundled references.
- Do not edit generated Claude/Grok mirrors or the generated catalog directly.
- Avoid unsupported claims of universal naming, stability or client compatibility.

## Validate locally

Use Python 3.10+ with no additional packages:

```bash
python3 scripts/render_catalog.py
python3 scripts/sync_adapters.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

For an agent integration, also run relevant scenarios in `evals/scenarios.json`
using the actual client. Include version, environment, date and observed result.
Static checks do not demonstrate that an agent loaded or followed instructions.

## Submit a pull request

Explain the problem, the resulting behavior and the checks actually run. Include
source links and disclose untested client behavior. By contributing, you agree
to license your original contribution under this repository's MIT license.

Treat other contributors with respect. Discuss claims and evidence rather than
people. Do not post personal data, credentials or private repository contents.
