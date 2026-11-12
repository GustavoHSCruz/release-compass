# Data contract

Canonical JSON lives in `.agents/skills/release-compass/data/`. Both files
declare `schema_version: 1`; consumers should reject unknown major schemas.
The lookup CLI returns a versioned JSON object containing count, missing
comparison queries, expanded terms and the registry's last review date.

| Term field | Meaning |
| --- | --- |
| `id` | Stable lowercase identifier; preserve it when changing display text |
| `label` | Human display name |
| `aliases` | Alternative names used by exact-match search |
| `category` | One editorial primary dimension; not a universal classification |
| `definition` | Concise editorial explanation |
| `caveat` | Limitation or likely confusion |
| `source_ids` | Supporting examples in sources.json; can be empty |
| `evidence` | `editorial-convention` or `editorial-synthesis-with-supporting-example` |
| `related` | Other term IDs; not an ordered promotion path |

Source records have `id`, `title`, `url`, `scope` and `checked_on`. The registry
records `last_reviewed`. A checked date records a documentation review, not a
promise that every linked page remains unchanged or accessible.

No definition is asserted to be a direct quote or a cross-industry standard.
An empty source list explicitly means no direct primary definition was verified
for that convention during the initial review. Do not fill it with an unrelated
reference merely to make the entry look sourced.

The CLI normalizes case and punctuation, prioritizes exact IDs/names/aliases,
then performs a simple all-keywords search. It does not provide semantic search.
`--compare` resolves each supplied query and reports missing queries with exit
code 2. Empty results also exit 2. Successful lookups exit 0.
