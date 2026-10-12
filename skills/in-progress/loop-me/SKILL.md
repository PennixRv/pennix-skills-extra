---
name: loop-me
description: Only when explicitly invoked, design a repeated-work process with clear triggers, outputs and justified human checkpoints, using the existing decision workflow and an explicit document location.
disable-model-invocation: true
argument-hint: "A workflow to design, or nothing to go find one"
---

Use `$pennix-decision-grill` for consequential choices and produce a workflow specification in an explicit existing document location. Reuse settled decisions and available facts. Writing the specification does not authorize automation, scheduling, deployment or a second task system; edits preserve user content and follow the native text interface.

## The loop lens

A **loop** is a repeated activity within the user's requested scope. Use the lens to assess whether specifying it would help; do not interview the user's whole life or introduce unrelated automation candidates by default.

A **workflow** describes one loop: its trigger, inputs, outputs, responsible operators, meaningful failure handling and completion signals. Its specification uses the agreed natural document location, without imposing a `workflows/` directory.

## Vocabulary

A shared language, reached for only when a workflow calls for it: never a checklist. **Mandate nothing structural**: a workflow needs no AI, no checkpoint, and no schedule unless the grilling shows it does.

- **Trigger**: what fires each run, an **event** (a new email, a new issue) or a **schedule** (every morning). Event-triggering is usually the more efficient.
- **Checkpoint**: a human-in-the-loop point where the user is asked to verify or decide. Some workflows have none and run autonomously; some use no AI at all.
- **Checkpoint timing**: prepare evidence before a decision, but ask consequential choices when their answers constrain later work. Place execution reviews where they protect the actual process; do not always defer them to the end.
- **Brief**: what a checkpoint presents, a tight, decision-ready summary (what was produced, why, and a link down to the asset itself), never the raw output. The user reads a brief, not a draft. Speed of review is imperative.

## Definition of done

A workflow spec is ready when its essential choices, operators, interfaces, failure handling and acceptance signals support implementation. Record dynamic facts and reopening conditions; do not explore theoretical questions to prolong the interview. Implementation still follows the project's existing plan/approval path.

## The workspace

- Confirm the specification's actual document location and reuse relevant existing task or process records.
- Preserve evidence, real answers and assumptions there. Do not create a second `NOTES.md`, task ledger or scheduler automatically. A process may use events or schedules, AI or no AI, according to the actual need.
