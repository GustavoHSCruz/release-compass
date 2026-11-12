# Release workflows

These are suggested practices to adapt to a project's existing policy. They
are not requirements imposed by SemVer or by the catalog's source vendors.

## Explain or compare

Find the terms, classify their dimensions, describe overlap and give a product
example. Avoid claiming that a prerelease will break or that Stable cannot fail.
For a production choice, verify the exact product/version support policy.

## Design a policy

Record the audience, delivery model, compatibility promise, maintenance capacity
and deployment environment. If details are missing, write explicit assumptions.
Choose only channels with a useful audience and an owner. A small library may
need just prerelease and stable, while a runtime can benefit from a release train.

For each channel, define eligibility, entry checks, promotion checks, support
scope, retention and how to leave the channel. Make promotion a decision based
on evidence rather than an arbitrary waiting period.

Example proposal for a small API:

| Channel | Audience | Suggested gate | Support statement |
| --- | --- | --- | --- |
| Preview | Volunteer integration testers | Tests pass; known issues documented | Evaluation only unless explicitly supported |
| RC | Release validation group | Contract checks, migration rehearsal, no open blockers | Candidate, with an explicit expiry |
| Stable | Normal users | Approved evidence and documented recovery plan | Published maintenance policy |

Use [the policy template](../assets/release-policy.md). Specify who approves a
release, without assuming that drafting this policy authorizes publication.

## Prepare a release

Establish immutable artifact identity, change evidence, migration behavior,
consumer communication, observability and recovery constraints. Generate notes
only from inspected changes. Run checks required by the project. Do not claim
checks have passed merely because a template includes a checkbox.

## Deploy separately

Select a traffic strategy after deciding the artifact and support contract.
A canary rollout can first expose a limited traffic share; see
[AWS's explanation](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/canary-deployments.html).
Define the signal, observation interval, stop condition and decision owner for
each step. A traffic switch does not undo a destructive database migration.

## Handle a hotfix

Identify affected versions and maintenance branches, assess compatibility,
apply the fix, verify the relevant regression, and decide which maintained
lines need backports. Propose the version under the project's policy. Preserve
the evidence and release notes even when the delivery is urgent.
