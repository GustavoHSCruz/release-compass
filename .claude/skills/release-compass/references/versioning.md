# Version proposals

Use the project's existing scheme. SemVer is a specific public API contract,
not a rule governing every numbered product.

For SemVer 2.0.0: incompatible API changes increment major, compatible additions
increment minor, and compatible fixes increment patch. Prerelease identifiers
follow a hyphen; build metadata follows a plus and does not affect precedence.
Versions below 1.0.0 indicate initial development; do not infer a mature API
contract there. Cite [the specification](https://semver.org/spec/v2.0.0.html).

Illustrative order for one release target:

`1.2.0-alpha.1 < 1.2.0-beta.1 < 1.2.0-rc.1 < 1.2.0`

This example uses conventional labels. Arbitrary labels are ordered by the
specification, not by their perceived maturity. `rc.10` and `rc.2` are dot-separated
numeric identifiers. A build date or `+sha.abc123` identifies provenance; neither
turns a prerelease into a stable release.

## Review procedure

1. Identify the public contract: SDK methods, HTTP API, CLI, config, schema or
   another interface consumers rely on.
2. Inspect the actual changes and the existing compatibility policy.
3. Separate version identity from channel pointers and deployment plans.
4. Propose an increment and explain the consumer-facing reason.
5. Document migration steps and uncertainty. Never infer compatibility from
   patch size or a commit's type alone.

For npm, [dist-tags](https://docs.npmjs.com/adding-dist-tags-to-packages/)
are publisher-controlled pointers. For NuGet, consult its
[version rules](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning).
Do not apply either client's selection rules to another package manager.
