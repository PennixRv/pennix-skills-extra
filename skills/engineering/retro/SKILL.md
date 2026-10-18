---
name: retro
description: "Only when explicitly invoked, review the current or specified coding session for evidenced navigation, tool, rule, check and information friction; propose improvements without changing the environment."
disable-model-invocation: true
---

The user has asked for a **retrospective**. You are suggesting improvements to the coding agent's **environment** to improve future runs.

## Steps

1. Use `$pennix-chinese-tech-writing` for Chinese technical content. Keep this review separate from implementing its recommendations; bug recurrence prevention remains the project's Trellis break-loop responsibility when applicable.

2. Read only relevant primary evidence for the specified session, defaulting to the current one. Historical conversation retrieval uses `trellis-session-insight` where available; do not sweep all session history or persist raw logs.

3. Look for candidates for improvement in these categories.

- **Navigation**: check the actual search path, existing context-mode/CodeGraph/Windsurf facilities and why they were not used or failed. A pointer or new index is a candidate only when current facilities do not cover the evidenced need; do not initialize an index.
- **Automated checks**: inspect relevant existing checks, CI and guardrails, their actual coverage and failure or non-execution. Recommend reuse, adjustment or a new check only when the observed risk justifies it; absence alone does not prove a defect.
- **Coding standards**: verify the alleged violation against actual requirements and project rules. Mechanical errors may suit an existing deterministic check; judgment requires relevant context and evidence. Name the responsible source repository before suggesting a rule, Hook or CI change; do not create another standards file automatically.
- **Global AGENTS.md**: are there any steering instructions that should be moved to coding standards (or automated checks) instead? _Use when_ the AGENTS.md file is particularly large - in the repo OR the user's global scope.
- **Tool economy**: did the agent make expensive tool calls that could be streamlined? Is there any custom tooling (CLI's, MCP's) that is particularly token-inefficient? _Use when_ the agent made an expensive tool call.
- **Instruction friction**: identify conflicting, ambiguous or duplicated instructions with examples of their actual effect; do not infer model behaviour or ineffectiveness from wording alone.
- **Information access**: look for opportunities to increase the agent's access to information. Teeing dev server logs, readonly access to third-party services. _Use when_ a crucial piece of information was not available to the agent.

4. Present verified candidates in severity order, with evidence, current coverage, uncertainty, responsible component and suggested landing point. Follow the existing Grill/approval route before any protected-target change; do not modify the environment, deploy tools or write knowledge automatically.

## Reference

### Implementation vs Review

For coding work, distinguish implementation from review: implementation explores, writes code and diagnoses failures; review checks the resulting behaviour against the actual requirements and project standards.

Review must follow the connected behaviour, relevant requirements and callers rather than relying on the diff alone. Context pressure depends on the actual review; do not assume a separate reviewer exists or require sub-agents. Both implementation and review follow the applicable project standards.

### Files

You have access to several files in the repo:

- `CLAUDE.md`/`AGENTS.md`: these files are pushed to the context window of any agent working in this repo. They should be used incredibly sparingly, usually only for **navigation pointers** to other files.
- Existing project specs and standards: apply when relevant during both implementation and review; preserve their actual ownership and entry points.
- Docs: use docs as references files, pointed to by other files. Look for existing docs before writing new ones.
- Skills: respect each Skill's discoverable scope and current owner contract. Reference existing methods instead of creating a competing workflow entry.
