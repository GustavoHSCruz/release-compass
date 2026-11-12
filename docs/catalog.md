# Release terminology catalog

An editorial glossary, not an exhaustive standard. Supporting sources illustrate
usage; they do not formally define every term in every product. See the
[source registry](../.agents/skills/release-compass/data/sources.json) for scope.

Generated from [terms.json](../.agents/skills/release-compass/data/terms.json).
Run `python3 scripts/render_catalog.py` after changing the data.

## Maturity

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Prototype | An implementation used to test feasibility or an idea. | It may be disposable and is not necessarily a published release. | Editorial convention; no direct primary definition verified |
| Pre-Alpha | Early development before the project considers itself ready for alpha testing. | There is no cross-project entry or exit criterion. | Editorial convention; no direct primary definition verified |
| Experimental | A feature or build offered for experimentation without a stable commitment. | This can describe a single feature inside an otherwise stable product. | [kubernetes](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) |
| Alpha | An early testing stage with incomplete or changing behavior. | Feature completeness and support guarantees are project-defined. | [nuget](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning) |
| Beta | A prerelease stage intended to collect feedback and identify defects. | Feature completeness and production eligibility require a product policy. | [nuget](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning) |
| Preview | An umbrella label for functionality available before its intended general release. | Preview is not a standardized position between alpha and beta. | Editorial convention; no direct primary definition verified |
| Developer Preview | An advance release aimed at developers evaluating APIs or integrations. | It does not by itself promise API compatibility. | Editorial convention; no direct primary definition verified |
| Technical Preview | An advance technology evaluation made available before a final offering. | Availability does not imply a production-support commitment. | Editorial convention; no direct primary definition verified |
| Release Candidate | A build proposed as the final release if acceptance checks reveal no blocking issues. | An RC is still a prerelease; production support can have explicit exceptions. | [nuget](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning) |
| Stable | A release or channel the project considers suitable for its normal supported use. | Stable is a project claim, not a guarantee of zero bugs or unchanged behavior. | [debian](https://www.debian.org/releases/) |
| Final | The published outcome of a particular release cycle. | An ordinary word such as release can also mean any published build. | [nuget](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning) |
| General Availability | A milestone making a product or feature generally available under its published policy. | Support scope, regions and production eligibility remain vendor-specific. | [kubernetes](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) |
| Release to Manufacturing | A traditional milestone when a build is handed off for manufacturing or distribution. | It need not share the same date as public availability. | Editorial convention; no direct primary definition verified |

## Channel

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Canary | An early-feedback channel exposing very recent changes to detect problems quickly. | A Canary channel and a canary deployment describe different things. | [chrome](https://developer.chrome.com/docs/web-platform/chrome-release-channels) |
| Nightly | A build or channel produced on a nightly development schedule. | The schedule does not certify maturity, and skipped builds are possible. | [rust](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html) |
| Daily | A build produced on a daily schedule, regardless of the time of day. | Cadence alone gives no stability guarantee. | Editorial convention; no direct primary definition verified |
| Snapshot | A captured state of the code or artifacts at a particular point in development. | Snapshot identifiers and mutability rules vary by ecosystem. | Editorial convention; no direct primary definition verified |
| Development | A channel following active development before broader stabilization. | Its relationship to preview or nightly depends on the project. | [chrome](https://developer.chrome.com/docs/web-platform/chrome-release-channels) |
| Unstable | A development stream that accepts changes before stable-release qualification. | The name is not a measured crash rate; Debian has specific usage. | [debian](https://www.debian.org/releases/) |
| Testing | A stream used to evaluate changes before promotion to a stable release. | Debian Testing is a named distribution, not a generic QA environment. | [debian](https://www.debian.org/releases/) |
| Edge | A label emphasizing access to very recent changes. | It can be a product name or a publisher-defined channel. | Editorial convention; no direct primary definition verified |
| Insider | A vendor-branded program offering access to upcoming changes. | A program can contain several channels with different guarantees. | Editorial convention; no direct primary definition verified |
| Next | A publisher-defined pointer or channel for upcoming work. | A next tag can point at any version the publisher chooses. | [npm](https://docs.npmjs.com/adding-dist-tags-to-packages/) |
| Latest | A publisher-controlled pointer to a selected package version. | Do not infer highest version, newest timestamp, or stable from the name. | [npm](https://docs.npmjs.com/adding-dist-tags-to-packages/) |

## Access

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Early Access | Access to software or features before their intended general release. | This describes access timing, not a fixed maturity stage. | Editorial convention; no direct primary definition verified |
| Private Preview | An advance offering restricted to selected participants. | Access rules do not establish stability or support. | Editorial convention; no direct primary definition verified |
| Public Preview | An advance offering open to a broad public audience. | Public availability is not equivalent to GA. | Editorial convention; no direct primary definition verified |
| Closed Beta | A beta restricted to an invited or selected audience. | Closed describes participation, while beta describes the stated stage. | Editorial convention; no direct primary definition verified |
| Open Beta | A beta made available for public participation. | Public participation does not guarantee production readiness. | Editorial convention; no direct primary definition verified |

## Support

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Long Term Support | A release with a provider-defined extended maintenance period. | Duration, patch requirements and covered components vary. | [dotnet](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core), [ubuntu](https://ubuntu.com/about/release-cycle) |
| Standard Term Support | A standard-duration support track used by products such as .NET. | It is not a lower-quality maturity tier than LTS. | [dotnet](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) |
| Extended Support Release | A release track designed for a longer maintenance or deployment horizon. | Its actual lifecycle is product-specific. | [firefox](https://www.mozilla.org/en-US/firefox/channel/desktop/) |
| Extended Stable | A stable track offering a longer interval between some feature updates. | Slower feature cadence does not mean security updates can be ignored. | Editorial convention; no direct primary definition verified |
| Interim Release | A release between longer-lived releases, commonly with a shorter support window. | Interim can be a fully supported stable release. | [ubuntu](https://ubuntu.com/about/release-cycle) |
| Oldstable | The previous stable release in ecosystems using this label. | The label alone does not establish whether support is still available. | [debian](https://www.debian.org/releases/) |
| Legacy | An older implementation or release retained for compatibility or migration. | Legacy has no universal support deadline. | Editorial convention; no direct primary definition verified |
| Deprecated | A feature, version or practice marked for transition away from continued use. | Deprecated does not necessarily mean already removed or immediately unsupported. | [lifecycle](https://learn.microsoft.com/en-us/lifecycle/definitions) |
| End of Life | The end of a provider-defined lifecycle or support period. | EOL and end of support may be separate milestones in a specific policy. | [lifecycle](https://learn.microsoft.com/en-us/lifecycle/definitions) |

## Cadence

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Rolling Release | A distribution model evolving through a continuous stream of package updates. | This is separate from rolling deployment and can contain stable packages. | Editorial convention; no direct primary definition verified |
| Fixed Release | A distribution model organized around discrete named or numbered releases. | Update and maintenance policies still need to be specified. | [ubuntu](https://ubuntu.com/about/release-cycle) |
| Release Train | A recurring schedule in which ready work advances through release stages. | Unready features may wait for a later train. | [rust](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html) |

## Change

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Point Release | An incremental update within an existing release line. | Some distributions use it for refreshed installation media; it is not always a SemVer patch. | [ubuntu](https://ubuntu.com/about/release-cycle) |
| Major Release | Under SemVer, an increment communicating incompatible public API changes. | Other version schemes assign different meanings to major numbers. | [semver](https://semver.org/spec/v2.0.0.html) |
| Minor Release | Under SemVer, an increment for backward-compatible functionality. | The public API contract determines compatibility. | [semver](https://semver.org/spec/v2.0.0.html) |
| Patch Release | Under SemVer, an increment for backward-compatible bug fixes. | A small diff does not prove a change is backward compatible. | [semver](https://semver.org/spec/v2.0.0.html) |
| Hotfix | A targeted fix delivered outside or faster than the ordinary release schedule. | Urgency does not waive verification or determine the version increment. | Editorial convention; no direct primary definition verified |
| Security Release | An update intended to address security issues. | It can also be a patch, maintenance release or backport. | [lifecycle](https://learn.microsoft.com/en-us/lifecycle/definitions) |
| Maintenance Release | A release focused on sustaining or correcting an existing release line. | Its exact scope can include more than bug fixes. | [lifecycle](https://learn.microsoft.com/en-us/lifecycle/definitions) |
| Service Pack | A packaged collection of updates for a product release. | This is a vendor-specific packaging convention. | [lifecycle](https://learn.microsoft.com/en-us/lifecycle/definitions) |
| Backport | A change adapted from a newer development line to an older one. | Backport describes the adaptation, not a maturity stage or complete release. | Editorial convention; no direct primary definition verified |

## Versioning

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Prerelease | Under SemVer, a version carrying a hyphen-prefixed prerelease identifier. | It has lower precedence than the corresponding normal version. | [semver](https://semver.org/spec/v2.0.0.html) |
| Build Metadata | Under SemVer, plus-prefixed metadata attached to a version. | Build metadata does not affect version precedence. | [semver](https://semver.org/spec/v2.0.0.html) |
| Semantic Versioning | A specification relating version numbers to a declared public API. | It does not define Canary, Preview, LTS or deployment strategies. | [semver](https://semver.org/spec/v2.0.0.html) |

## Deployment

| Term | Meaning | Caveat | Supporting background |
| --- | --- | --- | --- |
| Canary Deployment | A deployment that initially exposes a new version to a limited audience or traffic share. | It can deploy a stable build and does not define a release channel. | [aws-canary](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/canary-deployments.html) |
| Blue/Green Deployment | A deployment approach using separate old and new environments to switch traffic. | Database changes and shared state need their own transition plan. | Editorial convention; no direct primary definition verified |
| Rolling Deployment | A deployment that replaces instances in successive groups. | Old and new versions may run together; this is separate from rolling release. | Editorial convention; no direct primary definition verified |
| Feature Flag | A control allowing selected behavior to be enabled separately from distributing the code. | A flag is not a substitute for compatibility and lifecycle policy. | [kubernetes](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) |
