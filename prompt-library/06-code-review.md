# Scenario 6: Code review

Goal: a review that looks for mistakes, which you then confirm or reject by reading the code. Method: [debugging and review](../engineering-playbook/debugging-and-code-review.md).

Running example: a diff that adds pagination to `GET /tasks`.

## Bad prompt

```text
Review this code. Is it good?
```

You will get praise, a few style nits, and "consider adding comments." Nothing you can act on, and a false sense that a second party approved the change. The model is not a second party. It is the same kind of system that wrote the code.

## Improved prompt

```text
Review this diff for bugs, edge cases, and security issues.
Be critical.
```

"Be critical" helps. Without the requirement, the diff, and a structure, the review drifts into generic advice (add type hints, add a try/except) that may fight the surrounding file.

## Excellent prompt

```text
Context: You are reviewing a diff I may have written with an assistant. Assume it contains mistakes. Your job is to find them, not to encourage me.
Mode: review only. Do not edit.

Objective: Find defects in this pagination change.

Requirement the diff must meet:
- GET /tasks?offset=&limit= returns {"items","offset","limit","total"}
- order is created_at, then id
- limit default 20, maximum 100, otherwise 422
- offset < 0 returns 422
- offset past the end returns 200 and an empty items list
- no new dependencies
- only app.py and tests/test_tasks.py should change

Diff:
<paste, or tell the model to look at the working tree and quote lines>

Hunt in this order. For each item, either quote the line and say why it violates the requirement, or say "not seen" with the line you checked:
1. Logic that returns the wrong slice or the wrong total.
2. Boundary values: limit 1, limit 100, limit 101, offset 0, offset -1, offset past the end, empty list.
3. Existing tests weakened or deleted.
4. Error handling that hides bugs (bare except, clamped values where the requirement says 422).
5. Security only if this diff introduced a new input that reaches a query, a shell, or a path. If it did not, say "no new sink" and move on.
6. Consistency with the rest of app.py (how other handlers return errors).
7. Unnecessary complexity: code that does not serve the requirement.

End with:
- Defects you would block on (must fix).
- Notes you would not block on.
- One thing you are unsure about.

Do not praise the diff. Do not suggest a rewrite unless a blocker cannot be fixed locally.
```

### Why this is better

- "Assume it contains mistakes" counters the default of agreeable review.
- The requirement is in the prompt, so findings are violations of a contract, not taste.
- "Not seen" plus the line you checked is falsifiable. "No issues found" is not.
- Security is scoped. A pagination diff does not need an essay on OAuth.
- Blockers are separated from notes, so you do not treat a naming quibble as a failed solution.
- No praise. Praise crowds out the list.

## What to verify in the review

The model will invent defects. That does not make the prompt bad. It means you confirm.

- Open every quoted line. If the quote does not match, discard that finding.
- A blocker must name a broken requirement or a real regression. "Not using a pagination library" is not a blocker under this requirement.
- "Unsure" items need a look, not automatic agreement.
- Run the boundary the review claims is broken. If `limit=101` already returns 422, the finding is wrong. Good. You learned the code.

## A shorter version for a second pass

Once you trust the shape, you can narrow:

```text
Look only at the slice bounds in list_tasks.
I believe offset=10, limit=10 on a 25-item list returns items 10 through 19 and total 25.
Confirm or quote the line that makes that false.
Do not review anything else.
```

Narrow reviews catch the thing you are worried about. Broad reviews catch the thing you forgot. Do the broad one first on a diff you did not write yourself. Do the narrow one when you already have a hypothesis.

## Check your understanding

The review says "this endpoint is vulnerable to SQL injection." The handler filters a Python list with a comparison. How do you respond?

Reject it. There is no SQL sink. Say what you checked. Do not add a parameterised-query layer to look careful.
