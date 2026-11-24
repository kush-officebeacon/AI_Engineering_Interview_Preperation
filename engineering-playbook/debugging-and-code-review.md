# Debugging and reviewing AI output

A fix you cannot connect to a cause will be wrong in the next case. Ask the model to help you find the cause. Do not ask it to "fix the error" as the first move.

## Why an immediate fix is a poor first prompt

The model optimises for a diff that makes the current symptom go away. That is often:

- A broader `except`.
- A test edited to the new, wrong output.
- A special case for the one input in the traceback.
- A retry loop around a bug that is logical, not flaky.

You get a green run and a larger problem. The interviewer, if they can see the prompt, sees that you treated the symptom as the task.

## A debugging loop

1. **Reproduce.** One command, one input, one failure. If you cannot reproduce it, you do not have a bug you can fix. Write the command down.
2. **Read the failure.** Exception type, message, the frame that is your code. Not the twenty frames inside a library, except to see what your code passed in.
3. **Hypothesise.** One sentence: "I think the window is exclusive on the left, so a call exactly 60 seconds ago is dropped, and the limit is never reached." More than three hypotheses means you have not looked at the code yet.
4. **Distinguish them.** A log line, a print of the bound, or a smaller test. Each experiment should rule something out.
5. **Fix the smallest thing that addresses the cause.** Not a neighbouring cleanup.
6. **Regression test.** The input from step 1 becomes a test. Re-run the neighbours.

Prompts for each step are in [prompt 05](../prompt-library/05-debugging.md).

### How the model helps, per step

| Step | A good ask | A bad ask |
| --- | --- | --- |
| Reproduce | "Here is the command and the traceback. What input reaches this line?" | "Fix it." |
| Hypothesise | "Give three causes, each tied to a line. Do not edit." | "What's wrong with my code?" with no error and no file |
| Distinguish | "What would I print to tell hypothesis A from B?" | "Add logging everywhere." |
| Fix | "Change the comparison on this line so an event at `now - window` is still inside. Leave the tests." | "Make the tests pass." |

## Reviewing a diff like an adversary

A review that says "looks good" is useless. Ask the model to attack the change, then check its attacks. Some of its attacks will be fictional. Those are still useful: you confirm they are fictional by reading the code, which is another pass.

Cover, when the change can actually have the problem:

- **Logic.** Off-by-one, inverted conditions, stale values after update.
- **Edges.** Empty, None, duplicates, maximum, exactly-on-the-boundary.
- **Security.** See the list in [validation](validation-and-testing.md). Do not paste a generic OWASP essay into the review if the change is a sort.
- **Performance.** An accidental `O(n^2)` inside a request, a query in a loop, a copy of a large list on every call. Ignore micro-optimisations of code that runs once.
- **Maintainability.** Names, dead parameters, a second way of doing something the file already does.
- **Concurrency.** Check-then-act on shared mutable state. A test with one thread will not catch it. Say so, and either add a lock or state that single-threaded use is the assumption.
- **Error handling.** Swallowed exceptions, errors that should be 4xx returned as 500, partial updates left behind.
- **Compatibility.** Signature changes, response fields removed, behaviour of existing callers.
- **Consistency.** Does this file use `HTTPException` while the new code returns a bare dict?

The adversarial prompt is in [prompt 06](../prompt-library/06-code-review.md).

### How you judge the review

The model will over-report. For each finding:

- **Confirm** by reading the line. Keep it.
- **Reject** with a reason ("that method exists on `datetime` in 3.11; I checked"). Drop it.
- **Defer** if it is real but out of scope. Say that to the interviewer. Do not silently expand the task.

## Worked micro-example

Symptom: the limiter allows 6 calls. The requirement says 5 per 60 seconds.

A weak prompt: "The rate limiter is broken, please fix."

A model might change `limit` from 5 to 4. The sample test that sends 6 calls now fails closed. The requirement is now wrong, and a test that sends exactly 5 also fails.

A strong sequence:

1. You write down: call number 5 should succeed, call number 6 should fail.
2. You read the condition: `if len(recent) > limit`.
3. You see that the call is appended before the check, or after. You look. Suppose the check is `>` and the call is counted before the comparison. Five existing calls mean `len == 5`, `5 > 5` is false, the 6th is allowed.
4. You tell the model: "The check uses `>` after the new timestamp is included, so the call that reaches `limit + 1` is allowed. Change it so the call is rejected when `len(recent) >= limit` before append. Do not change the limit constant."
5. You add a test at exactly 5 and exactly 6.

The cause is a sentence you could say without the model. The model can type the edit. You decide the sentence.

## Check your understanding

1. Why is editing the test to match the code sometimes the correct outcome, and usually not?
2. A review comment says "this is not thread-safe." The function is a pure calculator with no shared state. What do you do with the comment?
3. You cannot reproduce the failure. What do you refuse to do?

## Answers

1. Correct when the test encoded the bug and the requirement says the new behaviour is right. You should be able to point at the requirement. Usually the test is the spec and the code is wrong.
2. Reject it. Thread safety is about shared mutable state. Say why it does not apply. Do not add a lock to look thorough.
3. You refuse to change production code. Get a reproduction first, or you will "fix" a guess.
