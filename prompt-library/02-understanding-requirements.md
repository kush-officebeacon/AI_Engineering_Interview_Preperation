# Scenario 2: Understanding a requirement

Goal: turn a vague sentence into behaviour, ambiguities, assumptions, and acceptance criteria **before** any code. Template: [the framework](00-prompt-framework.md).

Running example, the kind of sentence an interviewer says out loud:

> Add pagination to the task list.

## Bad prompt

```text
Add pagination to the task list.
```

This is an implementation order. The model will choose offset or cursor, a default page size, error codes, and response shape without telling you it chose them. You will discover the choices in the diff, which is late.

## Improved prompt

```text
Before coding, break down "add pagination to the task list."
List ambiguities and edge cases.
```

This asks for thinking. It still does not show the current API, so the model will invent a response shape that may not match the service. "Edge cases" without the current contract produces a generic list (page 0, negative page) that may not even fit the design it later writes.

## Excellent prompt

```text
Context: Python HTTP API. GET /tasks returns a JSON list of every task. Each task is an object with id, title, status, created_at. There is no pagination today. Tests live in tests/test_tasks.py.
Mode: requirements only. Do not write code and do not propose a library.

Objective: Turn "add pagination to the task list" into a contract I can accept or correct.

Already decided:
- Keep the existing task fields.
- This is a single-process in-memory list. Do not add a database.

Reply in exactly these sections:
1. Ambiguities a reasonable engineer could answer in more than one way.
2. Questions I should ask the interviewer or product owner, ranked, at most five.
3. If I get no answers, the assumption you recommend for each ambiguity, and the cost of being wrong.
4. Edge cases (empty list, page past the end, limit of 0, limit very large, stable ordering).
5. Acceptance criteria as observable statements, each starting with "Given / When / Then" or "GET <url> returns <status> and <body shape>."
6. What is explicitly out of scope.

Do not pick a design in section 5 that section 3 did not mark as an assumption.
```

### Why this is better

- It shows the current contract, so the model extends it instead of replacing it.
- It separates questions (for a human) from assumptions (if the human is not there).
- Acceptance criteria are observable. You can turn them into tests without further translation.
- "Out of scope" is where databases and frameworks go to die, on purpose.
- Ranking the questions matters in an interview. You will not have time to ask twelve.

## What a strong answer lets you say

You should be able to walk into the implementation with sentences like:

> I'm assuming offset and limit as query parameters, default limit 20, maximum 100. A limit above 100 is 422, not a silent clamp, so the client learns. An offset past the end returns 200 and an empty list, not 404, because the resource exists. Order is by `created_at` ascending so pages don't shuffle. I am not adding cursors unless you want stability under inserts.

If you cannot say that, the requirements prompt did not finish its job. Ask a narrower follow-up:

```text
Section 3 assumed a silent clamp at 100. I want a 422 instead.
Rewrite only the acceptance criteria that change.
Leave the rest.
```

## Another situation: a bug report as the requirement

```text
Bug report: "The limiter sometimes lets too many requests through."
Context: one process, an in-memory sliding window, limit 5 per 60 seconds. Tests are single-threaded.

Mode: requirements only. Do not propose a patch.

1. Ways this sentence can be true (boundary, concurrency, clock, keying by user).
2. What information is missing (which key, which timestamps, whether two threads were involved).
3. The smallest reproduction I should try to write before changing code.
4. What I should refuse to "fix" until that reproduction exists.
```

This pairs with [debugging](../engineering-playbook/debugging-and-code-review.md). A vague bug is a requirements problem first.

## What to verify in the answer

- Every acceptance criterion names an input and an observable output.
- No criterion requires a tool or service the "already decided" lines forbade.
- Ambiguities are real for *this* API. "What about GraphQL?" on a JSON list is padding. Discard padding.
- The assumptions are ones you are willing to defend. If you are not, they are still open questions.

## Check your understanding

Why is "list the edge cases" alone not enough to start coding?

An edge case without a required response is still a choice. "Page 0" might be an error, the first page, or meaningless. You need the observable contract, or an assumption you are willing to say out loud.
