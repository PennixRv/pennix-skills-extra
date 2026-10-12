# Design It Twice

When the user wants to explore alternative interfaces for a chosen candidate, compare a few distinct approaches in the main session. Based on "Design It Twice" (Ousterhout): consider alternatives before settling on the first idea.

Uses the vocabulary in [SKILL.md](SKILL.md): **module**, **interface**, **seam**, **adapter**, **leverage**.

## Process

### 1. Frame the problem space

Write a user-facing explanation of the problem space for the chosen candidate:

- The constraints any new interface would need to satisfy
- The dependencies it would rely on, and which category they fall into (see [DEEPENING.md](DEEPENING.md))
- A rough illustrative code sketch to ground the constraints, not a proposal, just a way to make the constraints concrete

Use existing evidence and settled constraints, then continue Step 2 within the authorized scope. Consequential missing choices follow the native decision path.

### 2. Compare distinct approaches

Develop a small number of meaningfully different interfaces in the main session. Do not introduce sub-agents solely for this method or flexibility unsupported by current callers; any separately authorized collaboration follows the project's native contract.

Use the same technical evidence (file paths, coupling, dependency category from [DEEPENING.md](DEEPENING.md), what sits behind the seam). Useful viewpoints are:

- Minimize what callers must know while preserving required behaviour.
- Make the most common existing caller straightforward.
- Where dependencies genuinely vary, compare appropriate ports and adapters.

Keep the definitions in [SKILL.md](SKILL.md) consistent with the project's existing domain terminology; no new glossary is required.

For each candidate record:

1. Interface (types, methods, params, plus invariants, ordering, error modes)
2. Usage example showing how callers use it
3. What the implementation hides behind the seam
4. Dependency strategy and adapters (see [DEEPENING.md](DEEPENING.md))
5. Trade-offs: where leverage is high, where it's thin

### 3. Present and compare

Present designs sequentially so the user can absorb each one, then compare them in prose. Contrast by **depth** (leverage at the interface), **locality** (where change concentrates), and **seam placement**.

After comparing, give your own recommendation: which design you think is strongest and why. If elements from different designs would combine well, propose a hybrid. Be opinionated: the user wants a strong read, not a menu.
