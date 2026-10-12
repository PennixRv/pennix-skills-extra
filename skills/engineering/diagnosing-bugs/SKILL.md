---
name: diagnosing-bugs
description: Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.
---

# Diagnosing Bugs

A discipline for hard bugs. Skip phases only when explicitly justified.

## 工作流协作

聚焦修复前的症状、可证伪假设、定向探测与回归信号。先遵守项目规则和 `$pennix-workflow-routing` 的工具/职责边界；保留已有证据和不确定性，不因复现困难无限扩大探测。修复、发布和持久化沿已有授权及项目任务推进；修复后复发预防由 Trellis `break-loop` 负责。HITL 模板通过 `bash scripts/hitl-loop.template.sh` 使用，不依赖可执行位、不在安装后运行；真正交互使用用户终端或宿主原生入口。

When exploring the codebase, read `GLOSSARY.md` (if it exists) to get a clear mental model of the relevant modules, and check ADRs in the area you're touching.

## Redact

This skill has you show commands, outputs and captured artifacts. **Redact every secret first**: write `<REDACTED>` in its place. Build loops against env vars, so the credential stays in the environment rather than in what you show. Captured artifacts carry auth headers: quote only the lines that carry the signal.

If the redacted output is not enough to diagnose the bug, say so and ask the user.

## Phase 1: Build a feedback loop

Build the tightest useful pass/fail signal for the reported symptom. Bisection, hypothesis-testing, and instrumentation become easier with such a signal; when it is unavailable, use the best verified observations and state what they cannot prove.

Keep reproduction work bounded by the question, available resources and authorization. Stop widening it when current evidence is enough to test a useful hypothesis.

### Ways to construct one, in roughly this order

1. **Failing test** at whatever seam reaches the bug: unit, integration, e2e.
2. **Curl / HTTP script** against a running dev server.
3. **CLI invocation** with a fixture input, diffing stdout against a known-good snapshot.
4. **Headless browser script** (Playwright / Puppeteer) that drives the UI and asserts on DOM/console/network.
5. **Replay a captured trace.** Save a real network request / payload / event log to disk; replay it through the code path in isolation.
6. **Throwaway harness.** Spin up a minimal subset of the system (one service, mocked deps) that exercises the bug code path with a single function call.
7. **Property / fuzz loop.** If the bug is "sometimes wrong output", run 1000 random inputs and look for the failure mode.
8. **Bisection harness.** If the bug appeared between two known states (commit, dataset, version), automate "boot at state X, check, repeat" so you can `git bisect run` it.
9. **Differential loop.** Run the same input through old-version vs new-version (or two configs) and diff outputs.
10. **HITL bash script.** Last resort. If a human must click, drive _them_ with `scripts/hitl-loop.template.sh` so the loop is still structured. Captured output feeds back to you.

Build the right feedback loop, and the bug is 90% fixed.

### Tighten the loop

Treat the loop as a product. Once you have _a_ loop, **tighten** it:

- Can I make it faster? (Cache setup, skip unrelated init, narrow the test scope.)
- Can I make the signal sharper? (Assert on the specific symptom, not "didn't crash".)
- Can I make it more deterministic? (Pin time, seed RNG, isolate filesystem, freeze network.)

A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight, a debugging superpower.

### Non-deterministic bugs

The goal is a useful reproduction rate, not a perfect repro. Use bounded repeats or targeted timing probes when justified. Resource pressure, parallel stress or production instrumentation require the relevant environment's authorization and limits; record the observed rate and uncertainty.

### When you genuinely cannot build a loop

State what you tried and what is missing. Continue with verified logs, current code, a known regression window or other available evidence when it can distinguish hypotheses; label the uncertainty and verification limit. Ask only for necessary missing access or a redacted observation. Additional production instrumentation follows the existing approval path.

### Preferred feedback signal: a tight loop that goes red

When feasible, name **one command** (a script path, a test invocation, a curl) that you have **already run at least once** (show the invocation and its output, redacted). Assess it against these properties and record any limits:

- [ ] **Red-capable**: it drives the actual bug code path and asserts the **user's exact symptom**, so it can go red on this bug and green once fixed. Not "runs without erroring"; it must be able to _catch this specific bug_.
- [ ] **Repeatable**: same verdict where possible; for flaky bugs record the observed rate and uncertainty within the agreed resource limit.
- [ ] **Timely**: short enough for useful feedback within the available environment's limits.
- [ ] **Runnable**: unattended when possible; human interaction uses the host's native interface or a user-run script such as `scripts/hitl-loop.template.sh`.

Prefer a runnable signal before deeper investigation. If a red-capable command is unavailable, keep the missing signal explicit and investigate only hypotheses supported by existing evidence.

## Phase 2: Reproduce + minimise

Run the loop. Watch it go red as the bug appears.

Confirm:

- [ ] The loop produces the failure mode the **user** described, not a different failure that happens to be nearby. Wrong bug = wrong fix.
- [ ] The failure is reproducible across multiple runs (or, for non-deterministic bugs, reproducible at a high enough rate to debug against).
- [ ] You have captured the exact symptom (error message, wrong output, slow timing) so later phases can verify the fix actually addresses it.

### Minimise

Once it's red, shrink the repro to the **smallest scenario that still goes red**. Cut inputs, callers, config, data, and steps **one at a time**, re-running the loop after each cut, and keep only what's load-bearing for the failure.

Why bother: a minimal repro shrinks the hypothesis space in Phase 3 (fewer moving parts left to suspect) and becomes the clean regression test in Phase 5.

Done when **every remaining element is load-bearing**: removing any one of them makes the loop go green.

Minimise when possible without losing the user's symptom. If reproduction is not quickly available, proceed with the evidence and limitations already recorded rather than treating this phase as an absolute gate.

## Phase 3: Hypothesise

Generate a small ranked set of plausible hypotheses; one clear, well-supported cause need not be padded into several alternatives.

Each hypothesis must be **falsifiable**: state the prediction it makes.

> Format: "If <X> is the cause, then <changing Y> will make the bug disappear / <changing Z> will make it worse."

If you cannot state the prediction, the hypothesis is a vibe: discard or sharpen it.

Show the material hypotheses and their evidence when it helps the user assess the investigation. Continue already authorized probes; an unanswered consequential user choice remains blocked under the native Grill/host contract and is never resolved by elapsed time.

## Phase 4: Instrument

Each probe must map to a specific prediction from Phase 3. **Change one variable at a time.**

Tool preference:

1. **Debugger / REPL inspection** if the env supports it. One breakpoint beats ten logs.
2. **Targeted logs** at the boundaries that distinguish hypotheses.
3. Never "log everything and grep".

**Tag every debug log** with a unique prefix, e.g. `[DEBUG-a4f2]`. Cleanup at the end becomes a single grep. Untagged logs survive; tagged logs die.

**Perf branch.** For performance regressions, logs are usually wrong. Instead: establish a baseline measurement (timing harness, `performance.now()`, profiler, query plan), then bisect. Measure first, fix second.

## Phase 5: Fix + regression test

Write the regression test **before the fix**, but only if there is a **correct seam** for it.

A correct seam is one where the test exercises the **real bug pattern** as it occurs at the call site. If the only available seam is too shallow (single-caller test when the bug needs multiple callers, unit test that can't replicate the chain that triggered the bug), a regression test there gives false confidence.

**If no correct seam exists, that itself is the finding.** Note it. The codebase architecture is preventing the bug from being locked down. Flag this for the next phase.

If a correct seam exists:

1. Turn the minimised repro into a failing test at that seam.
2. Watch it fail. If you forced the red by mutating code or a fixture, `diff` against a pristine copy to prove the mutation landed before you trust it.
3. Apply the fix.
4. Watch it pass.
5. Re-run the Phase 1 feedback loop against the original (un-minimised) scenario.

## Phase 6: Cleanup

Required before declaring done:

- [ ] Original symptom is rechecked with the available feedback signal; missing reproduction or environmental limits remain explicit
- [ ] Regression test passes (or absence of seam is documented)
- [ ] All `[DEBUG-...]` instrumentation removed (`grep` the prefix)
- [ ] Temporary artifacts retained or cleaned up according to their established ownership and the task's authorization
- [ ] The hypothesis that turned out correct is stated in the commit / PR message, so the next debugger learns
