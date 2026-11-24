# Assessment cheat sheet

Read this the morning of the interview. The long form is the playbook and the prompt library. If a company rule and this page disagree, the company rule wins. Check the invitation against [the comparison](../research/assessment-comparison.md).

## Workflow

1. Restate the task in two sentences. Name one ambiguity.
2. Ask one question that changes the code, or state an assumption out loud.
3. Run the tests. Open the entry point. Find the one function you will change.
4. Say the approach, the alternative you are not taking, and the first slice.
5. Delegate one slice, or type it if you already know the line.
6. Read the diff. Revert anything you did not ask for.
7. Run the tests yourself. Add the boundary case.
8. Fix causes, not symptoms. Do not edit a test to go green unless the test is wrong, and say why.
9. Close with: what works, what you rejected, what you left unsolved, what you ran.

## Questions before you code

- What is the input and the output, including the error?
- What already exists that I must not break?
- What is explicitly out of scope (storage, auth, scale)?
- How will I know this slice is done?

## Prompt rules

- One objective. Name the files. Say what not to edit.
- Put the decisions you already made in the prompt so they are not reopened.
- "Done when" is a command or an observable result.
- "Do not edit the tests" and "do not edit the code" are different turns. Do not ask for both in one breath unless you mean it.
- After a bad answer, add the fact you learned. "Try again" is not a fact.

## Review checklist

- File list is the one I named.
- No new dependency.
- Tests were not weakened or skipped.
- The boundary (0, 1, exactly the limit, one past) is what I think it is. Read the condition.
- Errors match the contract (422 versus a silent clamp).
- No second design (a class, a cache, a service) I cannot justify.
- I can read each changed line out loud.

## Test checklist

- I ran the command myself.
- The new test would fail if I deleted the new branch.
- I tried one input that is not in the file.
- Neighbour tests still pass.
- I did not mock the function I claim to have tested.

## Debug checklist

- I can reproduce it with one command.
- I can say expected versus actual.
- I have one hypothesis tied to a line.
- The fix is smaller than the function.
- The reproduction is now a test.

## Common AI mistakes

- Invented files, methods, or framework APIs.
- Extra scope: refactors, new packages, "future-proof" layers.
- Tests edited so a wrong implementation passes.
- Off-by-one that the happy path hides.
- Swallowed exceptions. Clamped input that should be rejected.
- `datetime.now()` mixed with UTC. Mutable default arguments. Check-then-act without a lock.
- A confident explanation that does not match the line.

## Never delegate blindly

- Whether you understood the requirement.
- The acceptance criteria.
- Approving the diff.
- A security-sensitive line you have not read.
- The verbal explanation.

## Always verify yourself

- Files cited exist.
- The diff matches the request.
- The test command, re-run by you.
- The boundary input.
- That you can change a line when asked.

## What to say

- "I'll restate, then I'll look at the code."
- "I'm assuming X. The cost if I'm wrong is Y."
- "First slice is only this. I am not building the other part yet."
- "The model added Z. I'm reverting it because..."
- "Expected A, got B, the condition is this line."
- "I left this unsolved on purpose."

## Red flags you are showing dependence

- You cannot start until the assistant replies.
- You send the ticket as the prompt.
- You accept a green run you did not read.
- You say "the AI thought" as the reason.
- You cannot edit the code with the assistant closed.
- You repeat a scale or security claim the code does not implement.
- A failed test is "fixed" by changing the assertion, and you did not notice.

## Rules reminder

| If the invitation says | You |
| --- | --- |
| No AI, or it says nothing | No assistant, no AI autocomplete if they banned it. Same workflow, you type. |
| In-platform assistant only (Meta's published rule, HackerRank's Amazon repo question) | That assistant only. No second laptop tool. |
| Bring your own (Canva's published rule for backend, frontend, ML) | Cursor or Claude is fine. Review anyway. |
| Unclear | Ask before the first prompt. If you cannot ask, do the work yourself. |
