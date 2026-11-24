# Scenario 1: Understanding an unfamiliar codebase

Goal: a map you can check, not an essay. Method: [codebase navigation](../engineering-playbook/codebase-navigation.md). Template: [the framework](00-prompt-framework.md).

The running example is a small Python service you have just opened. You have not read it yet. The same prompts work if you replace the paths.

## Bad prompt

```text
Explain this codebase.
```

The model will pick a depth, invent a structure if it cannot see the files, and bury the entry point under paragraphs. You have no way to tell a real file from a guessed one.

## Improved prompt

```text
Look at this repository and tell me:
- the entry point
- the main modules
- how a request flows
- where the tests are

Keep it short.
```

Better, because it names the artefacts you need. Still weak, because it does not say which tree, does not demand file paths, and does not forbid a refactor. "How a request flows" invites a generic web diagram.

## Excellent prompt

```text
Context: Python service in this workspace. I have not changed anything. I need a map before I edit.
Mode: explain only. Do not propose features and do not edit files.

Objective: Map one vertical slice, not the whole repository.

Look at the files that exist. Cite path and line for every claim.

Reply in exactly these sections:
1. How to run the tests (the command you found, or "not found").
2. Entry point (file, symbol, line).
3. One path: from the HTTP or CLI entry to the place state changes, one hop per line, each with a file.
4. Where that state lives (type and lifetime: in-memory, file, database).
5. Tests that execute this path (file and test name). If none, say none.
6. Claims you could not verify from the files.

Do not describe files you did not open. If a section is missing in the repo, write "not present."
```

In Cursor, add `@` references once you have spotted a README or `app.py`, or let the agent search and then you confirm. In Claude without repository access, paste the tree (`find` output) and the entry file instead of pretending it can see them.

### Why this is better

- One slice, so the answer stays checkable.
- A fixed shape, so a missing file shows up as a blank section instead of smooth prose.
- Citations, so you can open the line.
- An explicit "do not invent" rule, aimed at the failure mode that matters here.
- "How to run the tests" is first because a map you cannot execute is a story.

## What to verify in the answer

- Every path exists. Search or open it.
- The entry point is actually invoked (a `if __name__` block, a framework convention, a console script). Not just a file named `main.py`.
- The call chain is real: each hop's function contains a call to the next, or a registration that leads there.
- The test named really calls this path and does not only mock it away.
- Section 6 is not empty by default. A model that is sure of everything on a first look is overclaiming. Spot-check one "sure" claim.

## A follow-up once the map is real

```text
Using only app.py and tests/test_tasks.py, list the behaviours that are tested and the behaviours that are not.
Do not suggest an implementation.
For each untested behaviour, one sentence on why it might matter.
```

## Check your understanding

You got a confident paragraph about `TaskService` and a repository layer. `grep -R TaskService` prints nothing. What is the status of the rest of that answer?

The rest is untrusted until you check it the same way. One invented symbol means the model is describing a repository it wishes you had.
