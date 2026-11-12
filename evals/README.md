# Agent behavior evaluation

`scenarios.json` contains manual evaluation prompts and observable criteria.
These are specifications, not recorded successful model runs.

Run a scenario in a fresh session with the complete skill available. Record:
date, client version, model, discovery/installation method, browsing availability,
prompt, actual output and pass/fail reasons for each criterion. For live-data
questions, judge whether the agent verifies the policy rather than expecting a
hardcoded support date. Evaluate multiple runs if reliability matters.

Local tool tests do not measure instruction following, retrieval quality or
native agent discovery. Publish a results file only after actual runs.
