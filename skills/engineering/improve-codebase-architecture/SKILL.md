---
name: improve-codebase-architecture
description: "在具名子系统或有证据的变化热点存在架构摩擦时，检查耦合、浅模块和测试边界，提出有源码依据的改进候选；普通局部修复不触发全仓审查。"
---

# Improve Codebase Architecture

Surface architectural friction and propose **deepening opportunities**: refactors that turn shallow modules into deep ones. The aim is testability and AI-navigability.

This command is _informed_ by the project's domain model and built on a shared design vocabulary:

- Use `$codebase-design` when its vocabulary helps explain the candidate. Preserve actual component, API and domain names rather than imposing a renaming exercise.
- Existing glossary, ADRs and project specs provide context where present; no new glossary or ADR is mandatory.

当前范围存在架构摩擦或需要改进候选时采用，不要求用户点名。本 Skill 负责发现候选与解释证据，不授权架构改造。检索按问题选择适用来源，跨组件或职责不清时使用 `$pennix-workflow-routing`；重要选择按 `$pennix-decision-grill`，项目任务、阶段接受与实施授权沿现有 Trellis 工作流。完成候选后返回当前决策或方案；具体模块接口比较可采用 `codebase-design`，不因此扩大扫描范围。

## Process

### 1. Explore

**Scope before you scan: YAGNI.** Deepening a module pays off by making future changes to it easier, so put extra weight on the parts of the codebase that have recently changed. Decide *where* to look before you look:

- If the user named a direction (a module, a subsystem, a pain point), take it, and skip the inference below.
- Otherwise, inspect a bounded relevant part of commit history to find demonstrated hotspots. If there is no clear hotspot, state the uncertainty and clarify the useful scope; do not silently expand to a whole-repository audit.

Read applicable project rules, relevant code, and any existing glossary or ADR in the chosen area.

The main session examines the chosen scope and records evidence of friction:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow**, with an interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called (no **locality**)?
- Where do tightly-coupled modules leak across their seams?
- Which parts of the codebase are untested, or hard to test through their current interface?

Apply the **deletion test** to anything you suspect is shallow: would deleting it concentrate complexity, or just move it? A "yes, concentrates" is the signal you want.

### 2. Present grounded candidates

Present candidates in the current task's natural review artifact. Markdown and small Mermaid diagrams are suitable defaults. Use an HTML report only when it materially helps the requested review, with an explicit artifact path and local resources; do not automatically open applications or load CDNs.

Use before/after diagrams when they make the actual relationship easier to assess. Preserve the evidence and limitations in prose; a diagram does not prove a hypothetical improvement.

For each candidate, cover the relevant evidence in the chosen format:

- **Files**: which files/modules are involved
- **Problem**: why the current architecture is causing friction
- **Solution**: plain English description of what would change
- **Benefits**: explained in terms of locality and leverage, and how tests would improve
- **Before / After diagram**: optional when it clarifies the actual boundary change
- **Recommendation strength**: explain whether it is strong, worth exploring or speculative, and why; a badge is optional

End the report with a **Top recommendation** section: which candidate you'd tackle first and why.

Use existing domain terminology and accurate source identifiers; explain a differing contextual meaning only when it affects the candidate.

**ADR conflicts**: if a candidate contradicts an existing ADR, only surface it when the friction is real enough to warrant revisiting the ADR. Mark it clearly in the card (e.g. a warning callout: _"contradicts ADR-0007, but worth reopening because…"_). Don't list every theoretical refactor an ADR forbids.

For an appropriate optional HTML artifact, see [HTML-REPORT.md](HTML-REPORT.md).

Before detailed interface design, resolve any important candidate selection through `$pennix-decision-grill`; reuse choices the user has already made.

### 3. Grilling loop

Once a candidate is chosen, use the existing Grill and project planning route for constraints, dependencies, interfaces, tests, validation and rollout. Preserve coverage before replacing old tests.

Record actual decisions and rejected candidates with their reasons in the current natural task artifact. Knowledge publication or project conventions need their own applicable authorization; do not create glossary/ADR files or modify code as a side effect of selecting a candidate. Compare alternative interfaces using `$codebase-design` in the main session when useful.
