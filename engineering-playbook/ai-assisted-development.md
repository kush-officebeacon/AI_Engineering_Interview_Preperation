# AI-assisted development

You are the engineer. The model is a fast collaborator with no accountability. This document is the method the rest of the project assumes. Python is the example language.

## Why this matters

An assistant can draft a function in seconds and be wrong in a way that still runs. Interviewers who can see your session are not grading the draft. They are grading whether you noticed. Canva's engineering post says the candidates who did well asked questions, delegated bounded pieces, and fixed the model's mistakes. The candidates who struggled could code, and still could not tell when a suggestion was bad. That post is one company, not a universal rubric. The failure mode is still the one to train against. See [the research](../research/ai-in-hiring-trends.md).

## Driving the agent, and being driven

**Being driven** looks like this. You paste the ticket, accept a multi-file diff, run the one test the model wrote, and say "it passes." You cannot explain a line when asked. If the model invented a helper, you keep it because deleting it feels slow.

**Driving** looks like this. You can state the requirement in your own words before the first prompt. You decide which files are in scope. You ask for a plan, then for one change, then you read the diff. You run a test you could have described before the code existed. When the model is wrong, you say what is wrong and how you know.

The difference is not politeness and it is not prompt length. It is who holds the decision.

## A working loop

Use this on every non-trivial change. Skip steps only when you can say why.

1. **Restate the problem** in one or two sentences, including what "done" means.
2. **Inspect the code yourself** for a few minutes. Find the entry point and one existing test. A model that explores for you is useful after you have a landmark, not before. See [codebase navigation](codebase-navigation.md).
3. **List what is ambiguous.** Ask a person if one is available. Otherwise write the assumption down. See [planning](planning-and-architecture.md).
4. **Decide the slice.** One behaviour, one layer, or one bug. Not "implement the feature."
5. **Prompt for that slice** with the constraints and the files. The template is in [the prompt framework](../prompt-library/00-prompt-framework.md).
6. **Read the diff before you run it.** Look for files you did not name, new dependencies, and behaviour you did not ask for.
7. **Run the smallest check** that would fail if this slice were wrong.
8. **Then** ask for the next slice.

If you cannot do step 6, you are not ready to accept the change. Ask the model to explain the diff in terms of the requirement. If the explanation is still opaque, reject the diff and take a smaller slice. "I don't understand this, so I won't ship it" is a correct engineering decision.

## What to delegate, and what not to

| Good delegation | Poor delegation |
| --- | --- |
| "Explain this function and name its callers." You can check callers with search. | "Figure out the codebase and change whatever needs changing." |
| "Draft the pagination query. Do not change the response shape." | "Add pagination" with no contract. |
| "List three ways this race can happen. Do not edit files." | "Make it thread-safe" as the first and only instruction. |
| "Write a failing test for the empty-page case." | "Write tests so the suite is green." |

Never hand over, even when a tool is allowed:

- The decision that the requirement is understood.
- The decision that a diff is correct.
- A security-sensitive choice (authentication, authorisation, injection, secrets) that you have not read.
- A new dependency you have not justified.
- The explanation you will give a reviewer or an interviewer.

## How a session should sound

Talk in decisions, not in tool narration.

Weak: "I'll just ask the AI."

Strong: "The handler returns every row. The tests only cover the unfiltered list. I'm going to add a limit and an offset, defaulting limit to 20, and reject a limit above 100. I'll have the model draft the query function only, then I'll read it and run the new tests."

That second version can be checked. The first cannot.

## Cursor, specifically

Cursor has more than one way to work. Pick the one that matches the step.

- **Ask.** Explanations and hypotheses. No edits. Use this while you are still understanding the code or the bug.
- **Plan.** A written approach, files, risks, and sequence. Use this before a multi-file change. Read the plan. Delete steps you do not want.
- **Agent.** Edits. Give it a slice, not the whole ticket. Stop it if it leaves the files you named.

Mention files with `@` so the model is looking at the code you mean. A prompt that says "the repository" and attaches nothing invites a generic answer.

Claude in the browser is the same method with worse file context. Paste the function and the test, not the whole repository, unless the tool can actually read the tree.

## When the model is wrong

1. Say what you observed, not "this is bad." Example: "The test expects 429 on the 6th call within 60 seconds. The implementation returns 200. The window check uses `>` against a limit of 5, so the 6th call is allowed."
2. Ask for the smallest fix, or write the fix yourself if it is smaller than the prompt.
3. Re-run the test that failed and one neighbouring test that used to pass.
4. If the model "fixes" the test instead of the code, reject that. The test was the specification.

A longer treatment is in [debugging and code review](debugging-and-code-review.md) and [validation](validation-and-testing.md).

## Check your understanding

1. You have a green test suite after an agent edited seven files. What do you still not know?
2. Name one task you would give Ask mode and one you would give Agent mode on the same bug.
3. Why is "make it thread-safe" a weak first prompt?

Practise this loop at Level 3 in [the training roadmap](../interview-preparation/training-roadmap.md).

## Answers

1. You do not know whether the tests cover the requirement, whether a passing test was edited to match a wrong implementation, or what those seven files now do.
2. Ask: "Why does this assertion fail?" Agent: "Change the comparison on line N so the 6th call returns 429. Do not edit the tests."
3. It names a quality, not a behaviour, a location, or a check. The model will pick a locking strategy you may not be able to justify.
