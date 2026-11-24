# Scenario 3: Planning an implementation

Goal: a plan you can reject before any file changes. Method: [planning](../engineering-playbook/planning-and-architecture.md).

Running example: pagination on `GET /tasks`, after you have accepted the assumptions in [scenario 2](02-understanding-requirements.md).

## Bad prompt

```text
Plan the pagination feature and then implement it.
```

"And then implement" removes the checkpoint. The model will treat the plan as a private scratchpad and show you a diff. You also gave it no constraints, so the plan will include whatever default stack it likes.

## Improved prompt

```text
Write an implementation plan for pagination on GET /tasks.
Include files, risks, and tests.
Do not write the code yet.
```

The stop line is the important improvement. The plan can still be generic, because the model has not been told the current design, the assumptions, or what "good" looks like.

## Excellent prompt

```text
Context: Python HTTP API. GET /tasks in app.py returns every item in the module-level TASKS list. No database. Tests in tests/test_tasks.py cover create and list.
Mode: plan only. Do not edit files. Do not add dependencies.

Objective: A plan I can approve before any code is written.

Decisions already made (do not reopen these):
- Query parameters offset (default 0) and limit (default 20, maximum 100).
- limit < 1 or limit > 100 returns 422 with a short error body.
- offset < 0 returns 422.
- offset past the end returns 200 and an empty list.
- Order by created_at ascending, then id ascending.
- Response body becomes {"items": [...], "offset": n, "limit": n, "total": n}.
- Existing clients: this is a breaking change. Call that out, do not invent a versioned route unless you have a strong reason. I expect to accept the break for this exercise.

Reply in exactly these sections:
1. Feasibility in the current design (is the list enough?).
2. Impact: which current tests and callers break because the body is no longer a bare list?
3. Files to change, and files that must not change.
4. Alternative you are not choosing (cursor pagination), in three sentences, including when it would be better.
5. Risks and how we would notice them.
6. Test list: name, input, expected status and body. Mark which test to write first.
7. Implementation sequence, one slice at a time. First slice must be landable on its own.
8. Open questions, if any decision above is still unsafe.

Stop after the plan.
```

### Why this is better

- The decisions are inputs. The model is not silently re-designing the API.
- Impact analysis is required, because a response-shape change breaks old tests. A plan that ignores that will "fix" them in a later surprise.
- One rejected alternative proves the choice was a choice.
- The first slice is landable. That is what keeps the later agent prompt small.
- "Stop after the plan" is the constraint that makes the mode real even if the tool is capable of editing.

## What to verify in the answer

- Section 3 names files that exist. Open them.
- Section 2 names the actual current tests. If it says "update the list tests" without naming them, go look yourself and see how many assertions depend on a bare list.
- The first slice is smaller than "implement pagination." A good first slice is often "change the response shape and return all items with a total, with one test." Filtering and caps can follow. If the plan's first slice touches five concerns, send it back.
- No new package appears. If one does, the plan ignored the constraint. Do not negotiate with that plan. Restate the constraint.
- You can defend section 4 in your own words. If you cannot, you do not understand the choice yet. Ask:

```text
Explain the failure mode of offset pagination if a task is inserted at the front while a client is midway through the pages.
Do not change the recommendation unless that failure matters for an in-memory list with one client, which is this exercise.
```

## Approving the plan

Say what you accept, in the next prompt, so the implementation prompt does not drift:

```text
Plan accepted with these edits:
- First slice is the response shape only, limit and offset applied, no 422 yet.
- Second slice is validation.
- Do not start until I ask.
```

That approval is yours. The model does not approve its own plan.

## Check your understanding

The plan's first slice is "add a Pagination class, a protocol, and a SQL backend so we can swap stores." What is wrong with that as a first slice in this repository?

It builds a second store the requirement forbade, and it is not landable on its own. The first slice should be the response shape on the list that already exists.
