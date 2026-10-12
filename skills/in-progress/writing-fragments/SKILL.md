---
name: writing-fragments
description: "Only when explicitly invoked for collaborative writing, collect sourced raw fragments in an explicit document without fixing article structure; preserve user edits and distinguish candidates from verified facts."
disable-model-invocation: true
---

<what-to-do>

This is **explore** within the requested writing topic: collect possible material without fixing an article structure. Important choices use `$pennix-decision-grill`; do not prolong an interview when the existing material and answers are sufficient.

中文素材按 `$pennix-chinese-tech-writing` 撰写；语义编辑走原生 `apply_patch`，复读目标文件并保留用户改动。保留引用来源、事实/候选/个人判断与不确定性；素材不是已验证的任务事实，不自动晋升为知识或项目规则。普通技术改写不需要素材探索阶段。

As fragments emerge from either side of the conversation, append them to a single markdown file.

If the user did not pass a path, ask once where to save the document, then remember it for the rest of the session.

Capture fragments from the very first thing the user says, including the initial prompt.

For a new standalone fragments document, start with a working H1 title; preserve any existing document format and necessary source attribution.

</what-to-do>

<supporting-info>

## What is a fragment

A fragment is any piece of text that might survive into the final article. It must be _readable by the author_ (the author can tell what it means), but it does not need to define its terms or be comprehensible to a cold reader. The bar is "is this a piece of good writing?", not "is this a self-contained argument?"

Fragments are deliberately heterogeneous. Examples of what could be a fragment:

- A sharp sentence you'd want to deploy somewhere but don't yet know where.
- A claim with a one-line justification.
- A vignette: a thing that happened, a code snippet, a scenario, an analogy.
- A half-thought: "something about how X feels like Y, work this out later."
- A quote, a piece of dialogue, an overheard line.
- A list of related observations that hang together by feel.
- A complaint, a confession, a punchline.
- A **leading word**: a compact metaphor or coinage the whole piece can hang on (one term that names the idea, the way _tracer bullets_ or _fog of war_ names a whole pattern).

A recurring image or term can help the piece when it fits the topic and reader. Preserve established technical terminology; do not force a coinage or treat it as inherently more valuable than evidence and concrete observations.

The novelist's diary is the model: years of unstructured noticings that later get mined for raw material. Fragments are noticings.

## File format

```markdown
# Working title

A first fragment lives here.

It can be multiple paragraphs. It can include lists, code, quotes: whatever
shape the fragment naturally takes.

---

A second fragment.

---

> A quoted line that the user wants to keep around.

A reaction to it.

---

- A cluster of related observations
- That hang together by feel
- And want to be near each other
```

Fragments are separated by a horizontal rule (`\n---\n`). No headings inside the body. No tags. No order beyond the order they were added.

## Writing rhythm

Append silently. Don't ask permission for each fragment. Mention what you added in passing ("adding that"), but don't interrupt the conversation with save dialogs.

Before every write: re-read the file from disk. The user may have edited, reordered, or deleted fragments between turns, so preserve their changes. Never overwrite the file; only append (or, if the user asks, edit a specific fragment in place).

The user can say "cut the last one", "rewrite that one sharper", "merge those two" at any time. Treat those as first-class instructions.

</supporting-info>
