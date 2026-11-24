# Navigating an unfamiliar codebase

The goal is a map you can defend: where execution starts, where the data changes, and which tests lock the behaviour. An assistant can walk faster than you. It can also describe a file that does not exist. You check.

## Why this matters

Atlassian's AI-enabled code-design setup, in the Principal guide, hands you a repository in a language you may not know and asks you to extend it. Amazon's HackerRank repository question is the same shape: read `README.md`, find the right file, run tests. Meta's careers page tells candidates to practise reading and debugging existing code. Sources are in [the research](../research/company-assessment-research.md). Even in a round with no assistant, this is the skill. You just don't have a model to cross-check.

## What to find, in order

Spend a few minutes before any prompt. You are building landmarks so you can catch a hallucinated one.

1. **The README and the test command.** If you cannot run the project, say so and fix the run before you design anything.
2. **The entry point.** For a service: the app factory, `main`, or the router registration. For a library: what `__init__.py` exports.
3. **The path of one request or one call.** Route to function to storage and back. Write it in four lines.
4. **The nearest test.** The test file is often a better description of behaviour than the comments.
5. **The conventions.** How errors are returned, how names are spelled, whether the project uses dataclasses or dicts. Matching them is part of the task.

Only then ask the model to extend the map.

## How to use the model without believing it

Ask for claims you can falsify.

- "List the functions that handle `POST /tasks`. Cite file and line." Then open the file.
- "What test covers a missing task id?" Then run that test, or confirm it does not exist.
- "Draw the call chain from `create_task` to the place the dict is mutated." Then search for `create_task`.

Reject answers that name modules you cannot find with search. That is the most common navigation hallucination: a plausible `services/task_service.py` in a project that keeps everything in `app.py`.

Prompts at three levels of quality are in [prompt 01](../prompt-library/01-codebase-understanding.md).

## A trace you should be able to say out loud

Use this shape. It is short enough for an interview.

> A `POST /tasks` enters `app.py` at `create_task`. That function checks the title, appends a dict to the module-level `TASKS` list, and returns 201. `tests/test_tasks.py::test_create_task` covers the happy path. Nothing covers a blank title. Storage is in memory, so a restart drops the data. I am not changing storage unless the requirement says so.

If you cannot fill in the file names from the repository in front of you, you are not ready to edit.

## Data, not just control flow

Control flow is who calls whom. Data flow is what the payload looks like at each step.

- What fields enter?
- What is added (ids, timestamps)?
- What is stripped before the response?
- What is persisted, and in what type?

Bugs hide in the translation. A handler accepts `due` as a string. A later filter compares it to a `datetime`. Both files look locally correct.

## Tests are documentation

Search for the function name inside `tests/`. Note:

- What is asserted (status, body, side effect).
- What is missing (auth, empty input, limits).
- Whether tests hit the real function or a mock so wide that the function is never executed.

A mock that replaces the function under test does not tell you the function works. Say that out loud if you see it.

## When the repository is large

Do not ask for an architecture essay on the first prompt. Constrain the walk.

- One directory.
- One endpoint.
- One failing test.

Ask the model to stop after the entry point and the files that endpoint touches. You can widen the map if the change actually crosses a boundary. Most interview repositories are small enough that one vertical slice is the whole task.

Open-source practice targets are in Level 2 of [the roadmap](../interview-preparation/training-roadmap.md): `pallets/click` and `psf/requests`. The point of those exercises is to check the model's map against the code, not to produce a diagram.

## Check your understanding

1. The model says validation lives in `validators.py`. Search finds no such file. What do you do?
2. Why is the nearest test more trustworthy than a docstring?
3. What is the difference between a call graph and a data-flow trace, in one example?

## Answers

1. You discard that part of the answer and search for the actual check (`if not title`, a schema, a dependency). You do not create `validators.py` to match the story.
2. A test fails when behaviour changes. A docstring does not.
3. Call graph: `create_task` calls `TaskStore.add`. Data flow: the JSON field `title` becomes `task["title"]` and is later compared as a string in the filter. The bug can be in the second even when the first is right.
