# Release Compass

**Understand software release labels. Design release policies agents can explain.**

A community reference and portable Agent Skill for release terminology,
channels, versioning, support lifecycles and promotion workflows. Built with
Claude Code as a primary workflow, with entry points for Codex, Gemini CLI,
Grok Build and other agent clients, including clients powered by DeepSeek.

**57 terms · 8 dimensions · 22 primary-source references · No API key required**

[Browse the catalog](docs/catalog.md) ·
[Use with your agent](docs/agents.md) ·
[Read the skill](.agents/skills/release-compass/SKILL.md) ·
[Contribute](CONTRIBUTING.md)

## Why this exists

Canary, Nightly and Unstable sound like competing stages, but they emphasize
different things. LTS describes a maintenance commitment. A canary deployment
describes traffic exposure. A tag named latest is a publisher-controlled pointer.

Release Compass helps people and agents keep those distinctions clear, find
supporting documentation and turn a project's needs into a practical policy.
It combines a concise skill with selectively loaded references and structured
data instead of requiring the entire reference to enter every conversation.

This is an editorial knowledge base, not an exhaustive industry standard.
Product policies take precedence over generic terminology. Vendor-specific
examples link to official documentation; uncited conventions are marked as such.

## Start in a minute

### Read or search

Start with [the glossary](docs/catalog.md) or search locally with Python 3.10+:

```bash
python3 .agents/skills/release-compass/scripts/lookup.py canary
python3 .agents/skills/release-compass/scripts/lookup.py --compare Canary Nightly Unstable
python3 .agents/skills/release-compass/scripts/lookup.py --category support --format json
```

The lookup tool is offline, uses only Python's standard library and returns
source URLs with its results. Markdown and JSON can also be read without Python.

### Use Claude Code in this checkout

Open the repository with Claude Code, then enter:

```text
/release-compass Compare Canary, Nightly and Unstable with official examples.
```

The repository includes a complete project skill under `.claude/skills/` and a
`CLAUDE.md` importing shared project instructions. A read-only `release-advisor`
subagent is available for focused research. Availability depends on the installed
Claude Code version, session type and organizational settings.

### Install the skill in another project

Run from this checkout and select your actual destination project:

```bash
python3 scripts/install_skill.py --agent claude --project /path/to/your-project
```

Replace `claude` with `codex`, `gemini` or `grok`. To install for your local user
instead, replace `--project /path/to/your-project` with `--user`. Preview the
destination by adding `--dry-run`. Existing files are never overwritten.

The installer copies the complete skill, including references, templates and
lookup data. It does not modify existing instruction files or permission settings.
Review the files before installing community-provided instructions.

## Agent entry points

| Client | Repository instructions | Skill discovery in this checkout | How to ask |
| --- | --- | --- | --- |
| Claude Code | `CLAUDE.md` imports `AGENTS.md` | `.claude/skills/release-compass/` | `/release-compass <question>` |
| Codex | `AGENTS.md` | `.agents/skills/release-compass/` | `$release-compass <question>` |
| Gemini CLI | `GEMINI.md` imports `AGENTS.md` | `.agents/skills/release-compass/` shared alias | Ask to use the release-compass skill |
| Grok Build | Open `AGENTS.md` explicitly if needed | `.grok/skills/release-compass/` | `/release-compass <question>` |
| DeepSeek or another model in an agent client | Depends on that client | Use its supported skill loader or attach the complete skill | Use the portable prompt below |
| Web chat with no repository access | Attach selected Markdown/JSON files | No automatic filesystem discovery assumed | Explain which files were attached |

These are **client capabilities**, not promises made by a model name. Grok Build
support does not imply the same behavior in Grok chat. See
[setup, verification and troubleshooting](docs/agents.md) for authoritative links
and the distinction between documented support and runtime testing.

Portable prompt:

```text
Read AGENTS.md and .agents/skills/release-compass/SKILL.md.
Use only the relevant references to answer my software-release question.
Separate release maturity, channel, audience, support and deployment strategy.
Cite official sources for product-specific claims. Verify live support dates.
My question: <your question>
```

For a web chat, attach the named files and the references the question needs.
A repository URL alone does not grant a client browsing or file-reading tools.

## What you can do

| Goal | Starting point |
| --- | --- |
| Explain Alpha, Beta, Preview, RC, GA and Stable | [Catalog](docs/catalog.md) |
| Compare Canary, Nightly, Unstable and Testing | [Dimensions](.agents/skills/release-compass/references/dimensions.md) |
| Propose channels and promotion gates | [Workflows](.agents/skills/release-compass/references/workflows.md) |
| Propose a version from actual API changes | [Versioning](.agents/skills/release-compass/references/versioning.md) |
| Compare ecosystem conventions | [Examples](.agents/skills/release-compass/references/ecosystems.md) |
| Draft a project's policy | [Policy template](.agents/skills/release-compass/assets/release-policy.md) |
| Review release evidence | [Checklist](.agents/skills/release-compass/assets/release-checklist.md) |
| Write factual release notes | [Notes template](.agents/skills/release-compass/assets/release-notes.md) |
| Find sources or reuse structured data | [Source registry](.agents/skills/release-compass/data/sources.json) and [terms](.agents/skills/release-compass/data/terms.json) |

Example requests:

- "Design a small .NET library's Preview, RC and Stable policy. State assumptions."
- "We removed a public SDK method. Explain the version change under SemVer."
- "Explain why a stable artifact can use a canary rollout."
- "Check the current support status of this exact runtime version and cite the policy."

## How the repository is organized

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Canonical instructions for working in this repository |
| `AGENT.md` | Manual compatibility pointer; not a universal discovery filename |
| `CLAUDE.md`, `GEMINI.md` | Client-specific imports of shared instructions |
| `.agents/skills/release-compass/` | Canonical, self-contained skill bundle |
| `.claude/skills/`, `.grok/skills/` | Generated complete mirrors for native discovery |
| `.claude/agents/release-advisor.md` | Optional research subagent for Claude Code |
| `docs/` | Human catalog, setup, data conventions and maintenance guidance |
| `scripts/` | Installation, mirror generation, catalog rendering and validation |
| `tests/`, `evals/` | Executable regressions and manual agent-behavior scenarios |
| `.github/` | Community issue forms, pull request template and validation workflow |
| `llms.txt` | Navigation index for clients that choose to read it |

`SKILL.md` teaches a reusable workflow. `AGENTS.md` tells an agent how to work
in this repository. A Claude subagent file defines a separate specialist.
These files serve different purposes and are not interchangeable.

## Evidence and freshness

The initial research reviewed 22 primary documentation sources on
**2026-11-11**, including Agent Skills, Anthropic, OpenAI, Google, xAI, DeepSeek,
SemVer and product-specific release policies. Definitions are written as
editorial synthesis. A supporting example is not a universal definition.

The bundle intentionally avoids a table of "currently supported versions" or
fixed vendor support durations. Those facts change. Agents should verify live
claims with the product owner and disclose when browsing is unavailable.

There is no background crawler, hosted API, MCP server, telemetry, model API
integration or automatic package publication. No agent CLI end-to-end execution
is claimed by the static compatibility documentation.

## Contribute

Corrections, missing terms, clearer examples and additional client integrations
are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md). For a new definition,
include a primary source or explicitly mark it as an editorial convention.
Keep canonical data in one place and regenerate the mirrors and human catalog.

```bash
python3 scripts/render_catalog.py
python3 scripts/sync_adapters.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

See [the evaluation scenarios](evals/scenarios.json) for questions to try with
an actual agent. Automated validation checks packaging and behavior of local
tools; the scenarios require separate model runs.

## License

[MIT](LICENSE) applies to this repository's original code and documentation.
Linked third-party documentation retains its own terms. This is an independent
community project and is not affiliated with or endorsed by any AI vendor.
