# Scenario 4: Implementing a feature

Goal: one slice at a time, reviewed, consistent with the code that is already there. Method: [AI-assisted development](../engineering-playbook/ai-assisted-development.md). The plan you are implementing is the one from [scenario 3](03-planning-implementation.md).

## Bad prompt

```text
Implement pagination across the codebase. Make it production ready.
Use best practices.
```

"Across the codebase" and "production ready" are how you get a new package, a new layer, and a diff you will not finish reading. "Best practices" lets the model pick the practices.

## Improved prompt

```text
Implement offset/limit pagination on GET /tasks in app.py.
Update the tests.
Don't refactor unrelated code.
```

The file and the "don't refactor" line are real constraints. The prompt still bundles behaviour, validation, response shape, and tests into one turn. When the diff is wrong, you will not know which decision failed.

## Excellent prompt (first slice only)

```text
Context: app.py, GET /tasks returns a bare JSON list from the module-level TASKS list. Plan already accepted:
response body becomes {"items", "offset", "limit", "total"}, ordered by created_at then id.
This slice does not include 422 validation. Invalid limits are out of scope until the next prompt.

Mode: edit one slice.

Objective: Apply offset and limit and return the new body. Default offset 0, default limit 20. Do not enforce the maximum yet.

Look at: app.py, tests/test_tasks.py.

Constraints:
- Edit only app.py and tests/test_tasks.py.
- Do not add dependencies.
- Do not rename existing fields on a task.
- Do not introduce a class hierarchy. A small function is fine if the handler is getting hard to read. Match the style of the file you are editing.
- Update existing tests that break because the body is no longer a list. Do not weaken them: they should still check the task data, now under "items".

Requirements for this slice:
- GET /tasks returns all items when there are fewer than 20, with total equal to the count.
- GET /tasks?offset=0&limit=1 returns one item and the true total.
- Order is created_at ascending, then id ascending.

Reply with:
- The diff, or the edit itself.
- One sentence per changed test saying what it now asserts.

Done when:
- pytest tests/test_tasks.py passes.
- You have not added validation yet. If you did, revert it.

Do not start the 422 slice.
```

### Why this is better

- One behaviour. You can review it.
- The previous decision is repeated so the model does not "recall" a different plan.
- Existing tests must keep their strength. That sentence is what stops a green suite built by deleting assertions.
- The done condition includes a negative check ("you have not added validation"). Agents over-build. Tell them what finished looks like.
- Style guidance is concrete ("no class hierarchy", "match the file"), not "clean code."

## The next slice, after you have read the diff and run the tests

```text
Slice 2 of pagination. Slice 1 is accepted. Do not redo it.

Add validation only:
- limit < 1 or limit > 100 returns 422
- offset < 0 returns 422
- error body {"error": "<short reason>"}
- non-integer values return 422

Edit only app.py and tests/test_tasks.py.
Add tests for those four cases.
Do not change the success-body shape from slice 1.
Run pytest tests/test_tasks.py.
```

If slice 1 was wrong, do not paper over it inside slice 2. Say what failed:

```text
Slice 1 is not accepted.
GET /tasks?limit=1 returns two items. The slice is wrong, not the test.
Fix the limit handling in the list function only.
Show me the condition you changed.
```

## Asking for an explanation without another edit

```text
Explain the list function as it stands.
For each parameter, what happens, including the defaults.
Do not edit.
I will tell you if a sentence does not match the code.
```

Then you check. The point of the last line is to keep yourself honest.

## What to verify before the next slice

- The file list is only what you named.
- The new body matches the plan. Count the keys.
- Old assertions still check something meaningful. Open the test. If a test changed from `assert data[0]["title"] == "A"` to `assert response.status_code == 200`, the suite got weaker. Put the assertion back.
- Defaults match the decision (20 and 0, not 10 and 1, which is a common silent substitution).
- You can point at the sort key and say what happens when two timestamps match.

## Check your understanding

Slice 1's diff also wraps `TASKS` in a class "for future database support" and all tests pass. Do you accept it?

No. The tests do not make the class part of the requirement. Revert it. A passing suite can hide scope you did not ask for.
