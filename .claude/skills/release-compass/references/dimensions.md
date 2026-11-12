# Release dimensions

Release names mix different questions. These categories are an editorial model,
not a standard that vendors must follow. Entries and caveats live in
[terms.json](../data/terms.json); sources live in [sources.json](../data/sources.json).

| Dimension | Question | Examples |
| --- | --- | --- |
| Maturity | What readiness claim is being made? | Alpha, Beta, RC, Stable, GA |
| Channel | Which stream delivers changes? | Canary, Nightly, Dev, Unstable |
| Access | Who can participate, and when? | Private Preview, Open Beta, EA |
| Support | What maintenance commitment applies? | LTS, STS, ESR, EOL |
| Cadence | How are updates organized? | Rolling Release, Fixed Release, Train |
| Change | What kind of update is this? | Major, Patch, Hotfix, Backport |
| Versioning | How is version identity expressed? | SemVer, prerelease, build metadata |
| Deployment | How does running traffic receive a change? | Canary, Blue/Green, Rolling |

## Canary, Nightly and Unstable

Canary emphasizes early feedback, Nightly emphasizes a build schedule, and
Unstable describes a development stream's qualification policy. A project can
produce an unstable nightly build and distribute it through a Canary channel.
This overlap is a useful explanation, not a claim that vendors use all three.

Compare primary examples: [Chrome](https://developer.chrome.com/docs/web-platform/chrome-release-channels),
[Rust](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html), and
[Debian](https://www.debian.org/releases/).

## Common mistakes

- Preview is not universally between Alpha and Beta.
- LTS does not automatically mean more thoroughly tested than STS.
- A mutable tag named latest does not prove that its target is stable.
- A stable release can be distributed with a canary deployment.
- A rolling-release distribution can ship stable upstream packages.
- Feature maturity is separate from the containing product's release status.
- Deprecation, removal and end of support can have different dates.
- No finite glossary contains every label used by every project.

Treat risk as contextual: documented guarantees, test evidence, compatibility,
support, data migrations and recovery options matter more than the label alone.
