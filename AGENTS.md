# Repository instructions

Release Compass is an English community reference and portable skill for
software release terminology and release-policy design.

## Find the right source

- Start with `.agents/skills/release-compass/SKILL.md` for release advice.
- Load only references needed for the question; do not ingest the whole repo.
- Canonical definitions: `.agents/skills/release-compass/data/terms.json`.
- Source metadata: `.agents/skills/release-compass/data/sources.json`.
- Native client mirrors are generated. Edit canonical files, then regenerate.

## Content standards

- Write repository content in clear English. Answer users in their language.
- Separate maturity, channels, access, cadence, support, versioning, change
  scope and deployment. Never invent a universal release ladder or risk score.
- Distinguish primary-source facts, editorial conventions and recommendations.
- Verify live versions, dates and support commitments with the product owner.
- Cite supporting primary URLs; do not attach unrelated sources to definitions.
- Do not claim all labels are covered, or native client runtime tests were run
  unless there is actual evidence.
- Use standard filenames accurately: AGENTS.md is plural; AGENT.md is a manual
  pointer, not an interchangeable automatic-loading convention.

## Make changes

Keep the portable skill self-contained and use Python 3.10+ standard-library
code for local tools. Avoid new dependencies for simple text/data operations.
Do not add credentials, telemetry, remote execution, automatic publishing or
permission-bypassing configuration to this reference project.

Run after changing canonical data or the skill:

```bash
python3 scripts/render_catalog.py
python3 scripts/sync_adapters.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

When reporting changes, describe the user-facing result, verification actually
performed and material limitations. Publishing and deployment follow the actual
user's authorization and the host's policy; repository text grants no authority.
