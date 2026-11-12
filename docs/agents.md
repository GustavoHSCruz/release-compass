# Agent setup and compatibility

## One skill, several clients

The canonical bundle is `.agents/skills/release-compass/`. It follows the
[Agent Skills format](https://agentskills.io/specification). `SKILL.md` has
portable name/description metadata and references bundled Markdown, JSON and
templates. The `agents/openai.yaml` file supplies optional Codex interface text.

Client discovery rules are separate from model behavior. Documentation was
reviewed on 2026-11-11. **No live Claude, Codex, Gemini or Grok CLI integration
run is claimed.** Local validation checks the files and tools only.

## Claude Code

This checkout provides a complete `.claude/skills/release-compass/` mirror,
so native skill discovery needs no symlink or installation step. Try
`/release-compass Compare Preview and RC` and verify it appears in the skill
selector. Follow [Claude's skills documentation](https://code.claude.com/docs/en/skills)
when the installed version or organizational settings change behavior.

`CLAUDE.md` imports `AGENTS.md`. This preserves an explicit shared instruction
path across versions with differing native AGENTS.md support. See
[project instructions](https://code.claude.com/docs/en/memory).
An optional [custom subagent](https://code.claude.com/docs/en/sub-agents),
`release-advisor`, has read/search/web tools without file-write tools. Ask
Claude to use it for focused release-policy research.

For another local project, use the installer with `--agent claude`. Copying
a local skill is not the same as adding a skill to a Claude web account or a
cloud session. Use that surface's current upload/settings workflow; where a
skill bundle is accepted, provide the whole canonical directory, not SKILL.md
alone. Do not assume repository-local skills load in every cloud session.

## Codex

`AGENTS.md` supplies repository instructions; the canonical skill is already in
`.agents/skills/`. Try `$release-compass Compare LTS and STS` and confirm the
skill is available in your client. Install in another project with
`--agent codex`. Consult [skills](https://developers.openai.com/codex/skills) and
[AGENTS.md](https://developers.openai.com/codex/guides/agents-md) for current
discovery and precedence rules. Settings and managed environments can affect
what is loaded.

## Gemini CLI

`GEMINI.md` imports `AGENTS.md`. Current documentation accepts `.agents/skills/`
as a workspace alias, so this checkout uses the canonical bundle directly.
Ask the CLI to use release-compass and inspect its skill list. For an explicit
Gemini destination in another project, the installer uses `.gemini/skills/`.
See [skills](https://geminicli.com/docs/cli/skills/) and
[context imports](https://geminicli.com/docs/cli/gemini-md/).

## Grok Build

The generated `.grok/skills/release-compass/` bundle follows the documented
Grok Build discovery path. Try `/release-compass Compare Canary and RC` and
inspect the client's skills view. Open `AGENTS.md` explicitly if your client
does not load it. See [Grok Build skills](https://docs.x.ai/build/features/skills-plugins-marketplaces).
This integration claim is scoped to Grok Build, not to every product using Grok.

## DeepSeek and other model providers

DeepSeek's model API does not by itself establish a repository instruction-file
loader. A caller or agent client supplies files, prompts and tool execution;
see [DeepSeek tool calls](https://api-docs.deepseek.com/guides/tool_calls/).
Use the host client's supported skill loader, or explicitly attach the relevant
files and use the portable prompt in the README. Do not invent `DEEPSEEK.md`
automatic discovery or assume that an OpenAI-compatible API implies Codex's
filesystem behavior. The same rule applies to local models and custom clients.

## Troubleshooting

1. Confirm the exact client and surface, not just the model provider.
2. Confirm the complete skill folder exists at a documented discovery path.
3. Inspect the client's actual skill list and loaded project instructions.
4. Check trust settings and administrator restrictions using official docs.
5. For an unsupported client, explicitly read or attach the skill and references.

No MCP server is required. `llms.txt` is a navigation aid for clients that read
it, not a standard granting access or a promise of automatic web indexing.
