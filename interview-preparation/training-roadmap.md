# Training roadmap

Six levels. Do them in order. Each level names what you should be able to do before you move on. The prompts live in [the prompt library](../prompt-library/00-prompt-framework.md). The method lives in [the playbook](../engineering-playbook/ai-assisted-development.md).

Python throughout. When a level says "the model", use Cursor or Claude. The skill is the same.

## How a session works

1. Read the level's objective. Do not skip to the exercise.
2. Attempt the beginner exercise before the advanced one.
3. Write five lines in [the journal](../practice-log/learning-journal.md): what you asked, what was wrong, what you checked, what you would change.
4. Use the readiness checklist honestly. A green test file is not the checklist.

---

## Level 1. AI fundamentals

**Objective.** Give the model a bounded question, notice a wrong answer, and say what you did not delegate.

**Concepts.** Context versus a bare command. Hallucinated APIs. One objective per prompt. The model does not remember your repository unless you show it. "It compiled" is not a check. See [the framework](../prompt-library/00-prompt-framework.md).

**Exercises.**

- Beginner. Ask three short questions about the Python standard library (`dict.setdefault`, `datetime.now` versus `datetime.now(timezone.utc)`, `list.sort` versus `sorted`). For each, open the official docs and mark the answer right or wrong. Write down one sentence the model said that the docs do not say.
- Intermediate. Rewrite this prompt until it has one objective, a constraint, and an observable done condition: "Make my function production ready and handle edge cases." Use a function you wrote, ten lines or fewer. Do not let it edit yet. Compare the plan it returns with the plan you wanted.
- Advanced. Paste a function that calls `statistics.median_high` and a function that calls a method you invented, `list.median()`. Ask the model to explain both. It should be able to discuss the first and should not pretend the second exists. If it invents a meaning for `list.median`, record that as a caught hallucination.

**Prompts.** The short form and the template in [00-prompt-framework.md](../prompt-library/00-prompt-framework.md).

**Expected result.** A page of notes: three verified library facts, one rewritten prompt, one caught invention.

**Evaluation.** You can point at a sentence and say "this is not in the docs." You did not accept a rewrite you could not read.

**Common mistakes.** Asking the model whether it hallucinates, and believing the answer. Skipping the docs because the explanation sounded fluent. Putting two goals in one prompt ("simplify and add retries").

**Ready when.**

- [ ] You verified at least one answer against documentation, not against a second prompt.
- [ ] You can show a prompt you rejected as too vague, and the replacement.
- [ ] You can name one thing you will not delegate.

---

## Level 2. Codebase exploration

**Objective.** Build a map of a repository you did not write, and correct the model when the map names a file that is not there.

**Concepts.** Entry point, one vertical slice, tests as behaviour, citations. [Navigation](../engineering-playbook/codebase-navigation.md). [Prompt 01](../prompt-library/01-codebase-understanding.md).

**Exercises.** Clone these yourself. Do not vendor them into this project.

- Beginner. [`pallets/click`](https://github.com/pallets/click). Find how a command function becomes a CLI command. Name the file and the function. Run the test command from the project docs. Ask the model for the same map with the excellent prompt in scenario 01, then check every path.
- Intermediate. [`psf/requests`](https://github.com/psf/requests). Trace one `GET` from the public function to the place the response status is read. List the tests that would fail if status handling broke. Discard any test the model names that does not exist.
- Advanced. In `requests` or `click`, find one behaviour that has no direct test. Say why that matters. Do not open a pull request unless you want to. The exercise is the map.

**Expected result.** A one-page trace in the shape from the navigation guide, with paths you opened.

**Evaluation.** Every file you mention exists. You ran something. You caught at least one over-claim, or you can say you checked three claims and all three were real.

**Common mistakes.** Asking for "the architecture" and reading the essay aloud. Trusting a class diagram. Never running the tests because install was annoying. Write down the install failure instead of inventing a trace.

**Ready when.**

- [ ] You can state entry point, one call chain, and one test from memory of the files, then confirm.
- [ ] You have rejected a nonexistent path.
- [ ] You can say what the tests do not cover.

---

## Level 3. Controlled implementation

**Objective.** Add a small feature in slices. The model may draft a slice. You approve the diff.

**Concepts.** Assumptions, a plan, one slice, no new dependency, tests that keep their strength. [Planning](../engineering-playbook/planning-and-architecture.md). [Prompts 02–04](../prompt-library/02-understanding-requirements.md).

**Repository.** [task-tracker-api](../practice-repos/task-tracker-api/).

**Exercises.**

- Beginner. `GET /tasks?status=open` returns a bare list. Only that. Update or add tests. Leave pagination alone. `tests/test_tasks.py` still passes.
- Intermediate. Pagination as its own slice, using the contract in the repository README. Decide, in writing, what happens when `status` and `limit` are both present before you implement the combination. The exercise tests do not cover it. Your decision should.
- Advanced. Do the intermediate exercise again from a clean tree with a 45-minute timer, narrating as in [the live playbook](live-interview-playbook.md). One revert of something the model added that you did not ask for.

**Expected result.** A diff limited to the handler and the tests. A sentence for the assumption. Pytest output you ran.

**Evaluation.** You can point at the slice bounds and the 422. You did not add a database or a class hierarchy. Old title assertions still exist.

**Common mistakes.** One prompt for filter, pagination, and "clean architecture." Editing `test_exercise.py` so the current code passes. Claiming the combination of filter and page is obvious without stating the body shape.

**Ready when.**

- [ ] `pytest` for the behaviour you implemented passes, and you can name a test you did not weaken.
- [ ] You reverted or refused at least one extra change, or the diff never had one and you can say how you checked.
- [ ] You can explain the response shape without the chat open.

---

## Level 4. Debugging and validation

**Objective.** Name a cause before a patch. Recognise a shallow fix.

**Concepts.** Reproduce, hypothesis, minimal fix, regression test, tests that pass for the wrong reason. [Debugging](../engineering-playbook/debugging-and-code-review.md). [Validation](../engineering-playbook/validation-and-testing.md). [Prompts 05–07](../prompt-library/05-debugging.md).

**Repository.** [rate-limiter-bugs](../practice-repos/rate-limiter-bugs/). Do not open `SOLUTIONS.md` first.

**Exercises.**

- Beginner. Only `tests/test_window_bounds.py`. Write the cause in one sentence before you edit. The fifth-call test is already green. Explain why that does not mean the function is right.
- Intermediate. The buffer bug and the timezone bug. For time zones, propose a fix and then predict which of the two tests it fails. If your first fix fails one test, that is the exercise working.
- Advanced. The concurrency test. Explain the seam. Write a fix that does not deadlock and does not delete the test. Then run the whole suite.

**Expected result.** Four causes, four small diffs, a green suite, and a note of one shallow patch you did not keep.

**Evaluation.** You did not change `limit` from 5 to 4. You did not edit tests to go green. You can still fail the old code in your head.

**Common mistakes.** "Fix the limiter" as the first prompt. Clearing the shared list and calling it done. Stripping `tzinfo` and calling it UTC. Deleting `after_check` so the test stops failing.

**Ready when.**

- [ ] You can explain each failure with expected versus actual.
- [ ] The full suite is green and you ran it yourself.
- [ ] You opened `SOLUTIONS.md` only after that, and you can say where your fix differs.

---

## Level 5. Agentic engineering

**Objective.** A multi-step change with a plan, a stop condition, and tests, where the tool may touch more than one file and you still direct it.

**Concepts.** Plan approval, impact on old tests, sequence, risks. [Prompt 03](../prompt-library/03-planning-implementation.md) and the multi-step section of the framework.

**Exercises.**

- Beginner. In the task tracker, after Level 3, add `DELETE /tasks/{id}` that returns 204 and 404. Plan first. One file of production code, one test file. Agent prompt includes "stop after pytest".
- Intermediate. Add an optional `due` field. Reject a due date you cannot parse with 422. Decide the order when both `due` and `created_at` exist. Impact: which old tests send JSON that now needs to stay valid?
- Advanced. Pick a small issue in `pallets/click` or `psf/requests` labelled as a good first issue, or a documentation bug you can turn into a test. Write a plan that names files. Stop after the plan and review it against the real files before any edit. You do not have to open a pull request. If you edit, stay inside the files the plan named.

**Expected result.** A written plan, then a diff that matches it, then a test run.

**Evaluation.** The plan was editable. You caught drift ("it also reformatted the file"). You can say what you left out.

**Common mistakes.** Letting "while you're there" survive into the diff. A plan that introduces a new package for one parse. Starting the agent before you know the test command.

**Ready when.**

- [ ] The plan and the diff tell the same story.
- [ ] You can name one risk you wrote down before coding.
- [ ] Old tests were updated on purpose, not weakened.

---

## Level 6. Interview simulation

**Objective.** A timed round with narration. The score is the rubric in [mock assessments](mock-assessments.md), not the number of green tests alone.

**Concepts.** The twelve moves in [the live playbook](live-interview-playbook.md). The cheat sheet. Ownership.

**Repository.** [lru-cache-kata](../practice-repos/lru-cache-kata/), or a fresh task-tracker slice if you want a repository round instead of a kata.

**Exercises.**

- Beginner. 30 minutes, part 1 only, AI allowed, talk through the eviction choice. Stop even if you want part 2. Score communication and verification.
- Intermediate. 45 minutes, parts 1–3, AI allowed. Part 4 only if the earlier tests still pass. Use [prompt 08](../prompt-library/08-defending-implementation.md) afterwards, with the chat that implements closed, and answer out loud.
- Advanced. Same kata, 45 minutes, **AI not allowed**. Then, on another day, the same kata with AI allowed. Compare the two journal entries. The point is to see what you still have when the tool is gone, and what the tool sped up when you were allowed to use it.

Say **Start a mock assessment** to run one of the scripted challenges with the mentor rule. That is the advanced form of this level.

**Expected result.** A journal entry with the nine scores, filled by you on the beginner attempt and by the mentor on a formal mock.

**Evaluation.** You can explain every part you claim is done. An unfinished part you described clearly scores higher than a finished part you cannot read.

**Common mistakes.** Spending the clock on part 4 with part 1 still wrong. Asking the model to implement all four parts in one prompt. Treating a reported LinkedIn format as a promise that your real interview will be this kata.

**Ready when.**

- [ ] You have done one timed round with AI and one without.
- [ ] Your journal has at least one dimension under 7, and a specific next drill.
- [ ] You can give the closing statement from the live playbook without reading it.

## After level 6

Re-read the company page for the employer you are about to talk to, the week of the interview, not this roadmap. Rules move. The invitation wins. Then use [the cheat sheet](assessment-cheatsheet.md) the morning of.
