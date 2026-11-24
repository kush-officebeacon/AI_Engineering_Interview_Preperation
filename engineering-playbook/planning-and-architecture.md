# Planning and technical decisions

A plan is a list of decisions you can reject before they become a diff. It is not a formality and it is not a stall. In a 45-minute interview, a five-minute plan is cheap. A fifteen-minute rewrite is not.

## Why planning first is valuable

Code is a bad place to discover that you solved the wrong problem. A plan is cheap to throw away. A multi-file edit is not, especially when an agent has already "helpfully" renamed things.

A written plan also gives the interviewer something to react to. They can say "don't worry about persistence" before you build a database. If you skip the plan, you find that out after the model has added SQLAlchemy.

## What a useful plan contains

Write it in prose or bullets. Cover only what the change needs.

| Section | The question it answers |
| --- | --- |
| Requirement, in your words | What will be true when this is done? |
| Out of scope | What will you refuse to build? |
| Assumptions | What did the prompt leave out, and what are you assuming? |
| Approach | The design in a few sentences. |
| Alternatives | One other way, and why you are not choosing it. |
| Files | Which files change, and which must not. |
| Behaviour and errors | Status codes, edge inputs, what is rejected. |
| Test plan | The cases that should fail before the change and pass after. |
| Risks | What you might get wrong, and how you will notice. |
| Order | The first slice, then the next. |

If a section is "N/A", say why. "No new dependency, the stdlib is enough" is a decision. Omitting the line is a gap.

Prompts that ask for this shape are in [prompt 03](../prompt-library/03-planning-implementation.md).

## Feasibility, impact, dependencies

**Feasibility.** Can this be done inside the existing design? A rate limiter that must survive multiple processes cannot live in a process-local dict. Say that before you code the dict.

**Impact.** Who calls the function you will change? A signature change is a migration, not a tidy-up. Search for callers, or ask the model to list them and then verify the list.

**Dependencies.** Prefer the standard library and what the repository already uses. A new package needs a reason: what it gives you, what you must now trust, and how you would test without the network. Interview tasks almost never need one.

## Architecture in a small service

For a project the size of [task-tracker-api](../practice-repos/task-tracker-api/), the architecture choice is usually:

- Keep the handler thin.
- Put the rule (validation, filtering, the window check) in a function you can test without HTTP.
- Keep storage behind the function that already owns it, unless the requirement changes storage.

That is enough architecture. A repository interface with one implementation is ceremony unless you already have that pattern or you need to fake storage in tests.

Name the trade-off when you choose the simple version: "An in-memory list is not safe across processes. The existing module uses one, and the requirement does not ask for persistence, so I will match it and say the limit."

## Alternatives

Always be able to name one. You do not need a survey.

Example. Pagination:

- **Offset and limit.** Simple, matches SQL, unstable if rows are inserted while someone pages. Fine for this list.
- **Cursor.** Stable under inserts, more code, the client must pass an opaque token. Not worth it unless the interviewer asks about concurrent writes.

Pick one. Say what would make you switch.

## Risks worth writing down

- The requirement is ambiguous and you guessed.
- The change touches a shared structure (a global list, a cache) that other requests use.
- Time zones, inclusive bounds, and empty collections. These are where correct-looking code fails.
- The model will "improve" unrelated code. Your plan should forbid that.

## Sequence

A sequence that survives contact with an agent:

1. Failing test for the new behaviour, if you can write it from the requirement alone.
2. The smallest production change that makes that test pass.
3. The edge-case tests.
4. A cleanup only if the code is hard to explain.

Doing 2 before 1 is sometimes right when you do not yet know the assertion. Then write the test immediately after, from the requirement, not from the implementation. A test copied from the code cannot catch a wrong code.

## Decisions you should be able to defend

Use this sentence:

> I chose X over Y because Z. It fails when W. I would revisit it if V.

Example:

> I chose a `threading.Lock` around the check-and-append over a lock-free structure because the limit is per process and the list is already shared. It fails if two processes share nothing but the requirement, which they don't, here. I would revisit it if the limiter had to be correct across workers.

If you cannot fill X, Y, Z, and W, you do not own the decision yet. Ask the model to argue against your plan. That prompt is in [prompt 08](../prompt-library/08-defending-implementation.md). Then decide. The model's objection is input, not a verdict.

## Check your understanding

1. Why is "no new dependency" a planning outcome rather than a style preference?
2. Your plan says "add a database." The interviewer says the data is already in a list and will stay there. What do you delete from the plan, and what do you keep?
3. When is a five-minute plan a waste?

## Answers

1. Because a dependency changes what you must install, trust, and test. The plan should show that you considered it and rejected it for a reason, or accepted it for a reason.
2. Delete the database, the migration, and the ORM. Keep the behaviour, the edge cases, and the tests. Change the file list.
3. When the change is a few lines you already understand, the test is obvious, and writing the plan takes longer than the edit. Say the decision out loud instead. The [prompt framework](../prompt-library/00-prompt-framework.md) covers when not to write a long prompt. The same judgment applies to plans.
