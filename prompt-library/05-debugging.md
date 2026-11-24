# Scenario 5: Debugging

Goal: a cause, then a small fix, then a test that locks the cause. Method: [debugging](../engineering-playbook/debugging-and-code-review.md).

Running example: a sliding window that allows six calls when the limit is five.

## Bad prompt

```text
The rate limiter test is failing. Fix it.
```

You did not include the failure, the requirement, or a ban on editing the test. The cheapest "fix" is to change the assertion or the constant. Both go green. Both can be wrong.

## Improved prompt

```text
pytest fails on test_sixth_call_is_rejected.
Here is the traceback:
<paste>

Explain the bug and propose a fix. Don't change the tests.
```

This is close. You still asked for a fix in the same breath as an explanation, and you did not say what the requirement is, so the model may explain a different bug than the one the test encodes.

## Excellent prompt (cause first)

```text
Context: practice-repos/rate-limiter-bugs. Limit is 5 events per 60 seconds for a key. The new event should be rejected when 5 events are already inside the window.
Mode: explain only. Do not edit files.

Objective: Explain why test_sixth_call_is_rejected fails.

Look at:
- the traceback below
- the assertion
- the function the assertion calls

Traceback:
<paste the assertion error, including the expected and actual values>

Reply in exactly these sections:
1. What the test believes the requirement is (from the assertion, not from the implementation).
2. What the implementation does on the 6th call, citing the condition and the line.
3. Up to three hypotheses. For each: the line, why it would cause this actual value, and one observation that would rule it out.
4. Which hypothesis you think is most likely, and what you would print or assert to confirm it.
5. What you will not change yet.

Do not propose a patch in this reply.
```

### Why this is better

- The requirement is taken from the test, and the model must show it understood that.
- Hypotheses are tied to lines, so you can reject the ones that cite imaginary code.
- A confirming observation comes before a patch. That is the whole point of the scenario.
- "Do not propose a patch" feels strict and is useful. If the patch is in front of you, you will evaluate the patch instead of the cause.

## After you confirm the cause

```text
Confirmed: the check is `len(recent) > limit` after the new timestamp is appended, so the 6th timestamp is accepted. limit stays 5.

Mode: edit one slice.
Change the check so the call is rejected when 5 timestamps are already in the window, before appending.
Do not change the limit constant.
Do not edit tests in this step. I will run them.
Edit only the limiter function.
Show the condition before and after.
```

Then you run the test. If you want a regression test the model drafts:

```text
The fix is in. Do not change production code.
Add one test that sends exactly 5 calls and expects all of them allowed, and keep the existing test that the 6th is rejected.
Use the same clock injection the other tests use.
Do not add a framework.
```

## Logs, when the failure is not a unit test

```text
Here are 40 lines of log around the failure. The request id is 9f2.
Mode: explain only.

1. Which lines are the same request.
2. The first line where the state is already wrong.
3. What is still unknown because the log does not contain it.

Do not suggest a new logging framework. If one field is missing, name that field.
```

## What to verify

- Section 2 of the diagnosis quotes a condition that is actually in the file. If the quote is paraphrased into something cleaner than the code, go read the real line.
- The model did not "fix" a different failure (a typo in a message, a flaky time) than the one in the assertion.
- The patch is smaller than the diagnosis. A ten-line rewrite for a one-character comparison is a new bug surface.
- You re-run the previously passing neighbour, not only the test that failed.
- You can state the cause without looking at the model's words.

## Check your understanding

The model changes `limit` from 5 to 4 and the sixth-call test passes. Why is that not a fix?

The requirement is five allowed calls. The fifth-call test, if you still have it, now fails. Even if you deleted that test, you changed the contract to silence the symptom. The comparison is what was wrong.
