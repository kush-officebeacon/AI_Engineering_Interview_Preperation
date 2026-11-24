# Scenario 7: Testing and verification

Goal: tests that would fail if the implementation were wrong, plus a check you perform yourself. Method: [validation](../engineering-playbook/validation-and-testing.md).

**A passing test the model wrote is not verification.** You still run it, you still read the assertion, and you still try one input that is not in the file.

Running example: pagination, after slice 1 exists and before you trust it.

## Bad prompt

```text
Write tests for pagination and make sure they pass.
```

"Make sure they pass" tells the model the goal is green, not correct. It will change production code, weaken assertions, or skip tests. You asked for all three failures.

## Improved prompt

```text
Write pytest tests for offset and limit on GET /tasks.
Cover edge cases.
Don't modify app.py.
```

The fence around `app.py` is the right idea. "Edge cases" is still delegated. You may get ten tests for page numbers and none for the breaking change to the response shape.

## Excellent prompt

```text
Context: GET /tasks now returns {"items","offset","limit","total"}. Defaults offset 0, limit 20. Validation (422) is not implemented yet. Do not test 422 in this batch.
Mode: add tests only. Do not edit app.py. If a test fails, leave it failing and report it.

Objective: Tests that lock the slice-1 contract.

Look at tests/test_tasks.py and match its style (the test client, how tasks are created). Do not add a new framework.

Add these tests, with these assertions, not weaker ones:
1. test_list_wrapped_body: after creating two tasks, GET /tasks returns 200, body has items (length 2), total 2, offset 0, limit 20, and items[0] has the same title fields the old test cared about.
2. test_limit_one: create two tasks with different created_at; GET /tasks?limit=1 returns one item, the earlier one, and total 2.
3. test_offset_past_end: create one task; GET /tasks?offset=5 returns 200, items [], total 1.
4. test_order_tie_on_timestamp: two tasks with the same created_at and different ids; the smaller id comes first. Use whatever clock injection already exists. If none exists, construct tasks through the public API in an order that would fail if the sort were unstable, and say so in the test docstring.

Reply with:
- the tests
- which of them you expect to fail against the current app.py, and why

Do not "fix" a failure.
```

### Why this is better

- The assertions are specified. The model is filling in style, not deciding what correct means.
- "Leave it failing" separates test-writing from implementing. A red test is a successful outcome of this prompt.
- The tie-break test admits the honest constraint: if you cannot inject time, say so. That is better than a test that pretends it proved ordering.
- You named the file's existing style so the new tests look like they belong. Reviewing unfamiliar test style is extra work you do not need.

## Negative and regression tests, later slice

```text
Validation now exists. Do not edit app.py.
Add tests, and leave them exactly as strict as this:
- limit=0 -> 422, body has "error"
- limit=101 -> 422
- limit=100 -> 200
- offset=-1 -> 422
- limit=abc -> 422

Also add a regression comment on test_limit_one pointing at the slice bug if we ever return two items for limit=1.

Do not use parametrize unless the file already does. Readable duplicated tests are fine.
Run pytest tests/test_tasks.py and paste the summary line only.
```

## Mocks and fixtures

```text
I need a test for the pure function window_allows(events, now, limit, window_seconds).
Do not mock it. It is the unit under test.
Build the events list in the test so a reader can see the timestamps.
Do not add a fixture that hides the timestamps in another file.
No network, no sleep. Pass `now` in.
```

A mock prompt you should almost never send: "Mock out the limiter so the handler test passes." That test proves the handler called a mock. It does not prove a sixth call is rejected. Ask for a mock only at a boundary you do not own (a clock, a remote service) and say what the fake returns.

## What you do yourself, after the tests exist

This part is not a prompt. It is the job.

1. Read each new assertion. Could it pass for a wrong reason? `assert response.status_code == 200` alone can.
2. Run `pytest` on the file. Read failures. Do not ask the model to "make them pass" until you know whether the test or the code is wrong.
3. Temporarily break the production code in the obvious way (return two items for `limit=1`) and confirm the test goes red. Restore the line. If the test stays green, it is not testing the slice.
4. Send one request the tests do not cover, even a manual one: `limit` omitted, `offset` omitted, both set.

If step 3 feels expensive, do it once per session until it is a habit. It is the fastest way to learn whether you trust your suite.

## What to verify in the model's tests

- Names match the case.
- No `pytest.skip`, no commented assertions, no `except Exception: pass`.
- The test file imports the public surface (the test client, the function) the same way the old tests do.
- A failure report from the model matches a failure you can reproduce with the same command.

## Check your understanding

All four new tests pass on the first run, and the model says "implementation verified." What have you not done yet?

You have not read the assertions, you have not run the file yourself, and you have not broken the branch to see a test go red. The model's sentence is not a run.
