# The prompt framework

A prompt is a specification for one step. It is not a spell, and a longer prompt is not a better one. The right size is the size that removes the decisions you are unwilling to delegate and leaves the ones you are.

Use this with the method in [AI-assisted development](../engineering-playbook/ai-assisted-development.md). The eight scenario files in this folder are worked examples of the same template.

## The parts, and why each exists

| Part | Purpose | Omit it when |
| --- | --- | --- |
| Role and context | Tells the model what kind of help you want (explore, plan, patch, review). Stops it choosing "implement everything." | The conversation already established the mode and you are on turn two of the same task. |
| Objective | One outcome for this turn. | Never, if you want a predictable answer. |
| Background | The requirement, the constraint you already decided, the assumption. | The model can see the ticket and you have not added a decision. |
| Relevant code | Files, functions, the traceback, the failing assertion. `@file` in Cursor. | You truly want a language question with no project. |
| Constraints | What must not change. Files, dependencies, public signatures, style. | The task cannot spill. A one-line question cannot. |
| Requirements | The behaviour, including errors. | You are asking for an explanation, not a change. |
| Expected output | Plan, diff, list of questions, a single function. The shape of the reply. | You are in a casual clarification and any shape will do. |
| Acceptance criteria | How you will judge the reply before you accept it. | You are exploring and have not committed to a change. |
| Testing | What to run, or an instruction not to run the suite and waste the turn. | Explanation-only turns. |
| Verification | What you will check yourself. Writing it down reminds you, and it tells the model not to claim it ran things it cannot run. | |
| Limits | "Do not edit." "Do not add dependencies." "Stop after the plan." | The tool is already in Ask mode and cannot edit. Still useful if the mode can change. |

You will not fill every row every time. An empty row that you skipped on purpose is fine. An empty row you forgot is how the model invents a database.

## Template

Copy this and delete lines that do not apply. Empty headings waste attention.

```text
Context: I am working in <project>. Stack: Python <version>, <frameworks>.
Mode: <explain only | plan only | edit one slice | review only>.

Objective: <one sentence>.

Background:
- Requirement: <what must be true when this is done>.
- Already decided: <decisions the model must not reopen>.
- Assumption: <what you are assuming, so it can disagree>.

Look at:
- <file or function>
- <test or traceback>

Constraints:
- Do not change <files or signatures>.
- Do not add dependencies.
- Match the existing style <one concrete note, e.g. "raise HTTPException, do not invent a new error type">.

Requirements:
- <behaviour 1>
- <error behaviour>

Reply with:
- <the shape: a plan, a patch, a list of risks, a failing test>

Done when:
- <observable check>

Do not:
- <edit / run the app / rewrite tests / refactor unrelated code>
```

## How complexity should change

### Short conversational prompts

Use them when the context is already in the thread and the ask is one fact.

```text
Which function writes to TASKS, and what does it append?
```

A role paragraph here is noise. The failure mode of a short prompt is using it for a change that needed constraints. "Add pagination" is short and bad. "Where is the list mutated?" is short and good.

### Context-rich engineering prompts

Use them for a single change. This is the template above, filled in. Most interview work lives here. The model can see the file, the behaviour, and the fence.

### Multi-step agentic prompts

Use them when the tool will take several actions (search, edit, run tests) and you will not watch every keystroke. Then the prompt must include a stop condition.

```text
Implement only the filter on status. Search for the handler first.
Edit app.py and tests/test_tasks.py only.
Run pytest tests/test_tasks.py.
Stop after that run. Do not start pagination.
```

Without the stop, an agent treats the rest of the ticket as implied work. That is the usual way a 20-line change becomes a rewrite.

### Structured prompts with an output schema

Use them when you will compare options or check claims, not when you want code.

```text
Reply in exactly these sections:
1. Files read (path and symbol)
2. Call chain (one line per hop)
3. Behaviour the tests lock
4. Behaviour with no test
5. Claims you are unsure about

Do not propose a refactor.
```

The schema gives you a checklist. If section 1 names a file that is not in the tree, you stop believing sections 2 through 4.

### Iterative prompts

Use them after you have read the previous answer. Each turn should add information the model did not have: a failing assertion, a constraint, a rejection.

```text
That plan adds Redis. The project has no network service and the requirement is per process.
Revise the plan to use the existing in-memory list and a lock.
Keep the test ideas.
```

Iterating is not repeating "try again." If you have no new fact, you will get a new costume on the same mistake.

## When not to write an elaborate prompt

- You need a definition or a reminder of a standard-library signature. Ask the short question, then verify in the docs if the decision matters.
- You already know the edit and it is three lines. Typing it is faster and leaves less to review. Using a model to avoid typing is fine in production and wasteful in a short interview if the review takes longer than the edit.
- You do not yet understand the requirement. A richer prompt will not create an understanding you can defend. Write down your questions first. The requirements prompts are in [prompt 02](02-understanding-requirements.md).
- The previous turn already contains the context. Add the new constraint only.

Elaborate prompts fail when they hide the objective under background, or when two objectives conflict ("refactor for clarity" and "change nothing about structure"). One objective per prompt.

## What to verify in any reply

Regardless of scenario:

- File names and symbols exist.
- The reply did the task you asked, not the next task.
- Code claims match a quick read of the cited lines.
- No new dependency slipped in.
- You can restate the proposal in your own words. If you cannot, do not apply it.

## Check your understanding

1. Which part of the template stops an agent from adding pagination while you asked for a filter?
2. Give an example of a short prompt that is appropriate, and the same topic as a prompt that is too short.
3. Why should "Done when" be something you can observe?

## Answers

1. The objective, the constraints, and the "Do not" line. One of them might be ignored. All three are harder to misunderstand. The stop condition in a multi-step prompt is the backstop.
2. Appropriate: "What does `dict.setdefault` return if the key exists?" Too short: "Handle duplicates."
3. Because "make it good" is not a check. "pytest tests/test_tasks.py passes and GET /tasks?status=open returns only open tasks" is a check.
