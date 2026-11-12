# Example requests and expected behavior

## Compare Canary, Nightly and Unstable

Explain their different emphasis, allow overlap and cite Chrome, Rust and
Debian as examples. Do not output a universal risk ranking.

## Is LTS safer than STS for my .NET API?

Distinguish support horizon from quality, then verify the exact .NET version's
current support status and required patch level. Without browsing, do not
invent an end date. Discuss upgrade capacity as a recommendation.

## My 1.4.2 SDK removes a public method. Is 1.4.3 appropriate?

If the SDK follows SemVer and this removal breaks the declared public API,
propose 2.0.0, explain the consumer impact and identify a migration path.
Inspect the project's policy before deciding.

## Deploy Stable to 5% of users first

Identify this as a canary deployment of a stable artifact. Draft exposure and
stop criteria. Execute only with actual user authorization and suitable tools.

## Is package@latest newer than package@next?

Resolve the current tag targets when registry access is available. Do not infer
their ordering from the names. State the query time and exact target versions.

## Write release notes

Request or inspect a change set, identify impact and migrations, then use the
template. Keep unknown test results explicit. Never manufacture changes.

## Non-trigger example

"When does this movie release?" is outside the software-release workflow.
