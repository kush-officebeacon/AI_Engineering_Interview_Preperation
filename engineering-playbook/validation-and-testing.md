# Validation and testing

**Rule: never accept an implementation because it compiles, imports, or passes a single test.**

A green run means "the checks you actually executed succeeded." It does not mean the requirement is met, the right files were read, or the edge that will show up in review was tried.

## Why this matters

Models write code that is locally plausible. The bugs that get through are the ones that look like the shape of a correct program: the right status code on the example in the prompt, the wrong status code on the input nobody mentioned. Your job is to build a check the model did not get to design alone.

## The validation sequence

Do these in order. Stop when one fails and fix that before trusting the next.

### 1. Did it understand the requirement?

Compare the diff to your own restatement, not to the model's summary. Look for:

- Behaviour you did not ask for (logging frameworks, new endpoints, refactors).
- Behaviour you did ask for that is missing.
- A comment that says the code does something the code does not do.

Ask: "Which sentence of the requirement does each changed function satisfy?" Check the mapping. If a function maps to nothing, it is probably noise.

### 2. Did it inspect the right files?

The model should name files it read. Open them. If the answer cites `services/tasks.py` and the repository has `app.py` only, the rest of the answer is suspect. Search for the symbol yourself.

### 3. Did it invent an API?

Common inventions in Python:

- A method that does not exist on the type you are holding (`list.first()`, `dict.get_or_raise`).
- A standard-library function with the wrong signature (`datetime.utcnow()` is real but naive and deprecated in spirit; `datetime.now(timezone.utc)` is the one you can justify).
- An import from a package that is not in `requirements.txt` and is not in the standard library.
- A FastAPI dependency or Pydantic v1 call in a v2 project, or the reverse.

If you do not recognise a call, look it up in the version this project uses, or ask the model for the documentation URL and open it. Do not accept "this is the standard way" as evidence.

### 4. Read the diff

Read in this order:

1. The file list. Anything unexpected stops you.
2. The tests, if they changed. A test that was weakened to go green is a failed solution.
3. The production change, hunk by hunk. For each hunk: what behaviour changed, and which test or manual check covers it?
4. Error paths. What happens on bad input? Is the error the one the requirement implies?

### 5. Run more than the test the model likes

- The new tests.
- The old tests around the same function.
- One input you invented that is not in the file: empty string, limit of 0, limit of -1, a timestamp in the future, two calls at the same timestamp.

If there is no test harness, run the function from a tiny script or the REPL and write down the inputs and outputs. "I ran it" without inputs is not a verification.

### 6. Logs and runtime behaviour

A stack trace is evidence. Read the exception type and the last frame in **your** code, not the first frame in a library. Print statements the model added are not a fix. Remove them once you have the answer, unless the project already logs at that boundary.

### 7. Edge cases that pass for the wrong reason

| Looks correct | Is wrong |
| --- | --- |
| `if len(items) > limit` with limit 5 | The 6th item is the first failure only if you count from 1 and the check happens before append. Off-by-one often passes a test that uses 1 and 100 and fails at the boundary. |
| `except Exception: return []` | The test for "no results" passes. A programming error is now invisible. |
| A mock that returns the expected value | The test passes without executing the branch you think you wrote. |
| `datetime.now()` compared to a UTC timestamp | Passes on a UTC machine. Fails elsewhere, or fails for one hour around a DST change. |
| A lock acquired after the read | The test is single-threaded, so it passes. Two threads still both observe "under the limit." |

The rate-limiter repository in `practice-repos/rate-limiter-bugs/` is built from this table. Do the exercise before you read its solution notes.

### 8. Security, at the level this code needs

You are not doing a penetration test. You are looking for mistakes that are normal in generated code:

- Building a shell command or a SQL string by concatenation.
- Returning an internal exception message to the client.
- Trusting a client-supplied id for authorisation ("this user id in the body is who I am").
- Logging secrets, tokens, or full card numbers.
- `eval`, `pickle.loads` on untrusted bytes, or `yaml.load` instead of `yaml.safe_load`.
- A new dependency you did not ask for.

If the change does not touch those surfaces, say so: "This slice does not take a query string into a shell or a database. The risk I do have is unbounded `limit`, so I cap it."

### 9. Is it more complicated than the problem?

Warning signs:

- A class hierarchy for one rule.
- A cache in front of an in-memory list.
- Configuration for a value that should be a parameter.
- Error types the rest of the file does not use.

Ask: "What would the smallest version of this function be?" If you can write it in half the lines and still meet the tests, prefer yours. You have to be able to read it under questioning.

### 10. Regressions

Run the tests that used to pass. If the suite is large, run the directory you touched and any test that imports the module you changed. A model that updates a shared helper can break a caller it never mentioned.

## Tests worth asking for

Ask the model to draft tests, then you edit them. You own the assertion. Categories:

- **Unit.** One function, no network. The window check, the filter, the eviction.
- **Integration.** The HTTP call through the app into the store, still in memory. Enough to show the route is wired.
- **Edge.** Empty, boundary (exactly the limit), just over the limit, duplicate ids.
- **Negative.** Wrong types, missing fields, limit of 0. Expect a specific status or exception, not "it doesn't crash" alone.
- **Regression.** A test that failed before the fix and now passes, named for the bug. This stops the bug coming back.
- **Fixtures.** Build the smallest object. A fixture that hides the input makes the test harder to review.

The prompts are in [prompt 07](../prompt-library/07-testing-and-verification.md).

### What you check in a test the model wrote

- The assertion matches the requirement, not the implementation. If the code returns 200 and the test expects 200 because that is what the code does, the test is circular.
- The test would fail if you deleted the new branch. Mutate the code or reason about it. This is mutation thinking. You do not need a framework.
- Names describe the case: `test_sixth_call_within_window_is_rejected`, not `test_rate_limit_2`.
- No skip, no broad `except`, no assertion on a mock's return value that the code under test never computed.

## When you cannot understand the code

Do not leave it in the tree because the tests passed.

1. Ask for an explanation of one function, line by line, tied to the requirement.
2. If you still cannot restate it, ask for a simpler rewrite that preserves behaviour, or rewrite it yourself.
3. If the simpler form fails a test, you have found either a real edge or a test that encodes an accident. Decide which, explicitly.

Shipping code you cannot explain is the failure this project exists to prevent. In an interview it is disqualifying in the only sense that matters: you cannot answer the next question.

## Check your understanding

1. All tests pass. Why is that not sufficient?
2. Give one example of a test that passes for the wrong reason.
3. The model adds `requests` to call a URL the requirement never mentioned. What do you do before anything else?

## Answers

1. The tests may be incomplete, edited to match the bug, or mocking away the bug. You still compare the diff to the requirement and try an input that is not in the suite.
2. `except Exception: return []` satisfies a test that only checks "empty input returns an empty list."
3. Revert that dependency. Then look at why the model thought a network call was required. The requirement and the model have diverged. Fix the understanding before the next prompt.
