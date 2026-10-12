---
name: prototype
description: Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like.
---

# Prototype

A prototype is **throwaway code that answers a question**. The question decides the shape.

## 工作流协作

先明确要消除的不确定性、成功信号、产物位置与保留/清理边界；当前源码或现有证据足以回答时直接查证。复用项目规则与 `$pennix-decision-grill` 处理重要选择，不因原型另建 tracker、临时分支或第二任务。原型只授权已选范围；后续真实实现、部署和发布仍沿项目合同。保留代码必须满足项目质量要求，不因“原型”免除必要验证。

## Pick a branch

Identify which question is being answered, using the user's prompt, the surrounding code, or by asking if the user is around:

- **"Does this logic / state model feel right?"** → [LOGIC.md](LOGIC.md). Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the state machine through cases that are hard to reason about on paper, and that a non-developer can drive.
- **"What should this look like?"** → [UI.md](UI.md). Generate several radically different UI variations on a single route, switchable via a URL search param and a floating bottom bar.

The two branches produce different artifacts. Resolve consequential ambiguity through the native decision path; a local reversible format choice may follow the question and surrounding code, with its assumption stated.

## Rules that apply to both

1. **Throwaway from day one, and clearly marked as such.** Locate the prototype code close to where it will actually be used (next to the module or page it's prototyping for) so context is obvious, but name it so a casual reader can see it's a prototype, not production. For throwaway UI routes, obey whatever routing convention the project already uses; don't invent a new top-level structure.
2. **Trivial to run.** A UI prototype starts from one command in the project's task runner: `pnpm <name>`, `python <path>`, `bun <path>`, etc. A logic demo is a single HTML file the user double-clicks. Either way, no thinking required to start it.
3. **No persistence by default.** State lives in memory. Persistence is the thing the prototype is _checking_, not something it should depend on. If the question explicitly involves a database, hit a scratch DB or a local file with a clear "PROTOTYPE, wipe me" name.
4. **Skip unnecessary polish.** Keep verification proportionate to the question and risk; protect real data and errors that would invalidate the result. Any retained logic follows the project's normal tests and quality requirements. No speculative abstractions.
5. **Surface the state.** After every action (logic) or on every variant switch (UI), print or render the full relevant state so the user can see what changed.
6. **Capture the answer when done.** Record the verdict, question and limitations in the current task or other existing natural artifact. Retention, cleanup and incorporation into real code follow the user's objective and project authorization; no throwaway branch, issue or permanent prototype is mandatory.
