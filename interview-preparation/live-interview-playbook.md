# Live interview playbook

A workflow for a round where the interviewer has **explicitly** allowed an AI tool. If they have not, use the last section. The company's written rule wins over this file. Policies are in [the research](../research/company-assessment-research.md). What each stage is proving is in [what interviewers evaluate](what-interviewers-evaluate.md).

Time budget for a 45-minute coding round. Shift it, do not skip the ends.

| Minutes | What you are doing |
| --- | --- |
| 0–5 | Restate, ask, assume |
| 5–10 | Run tests, find the files, say the plan |
| 10–30 | Slices: prompt or type, review, test |
| 30–40 | Edges, a regression, repair |
| 40–45 | What you did, what you left, what would change |

A 60-minute repository round (the length Atlassian prints on its coding guides) gives the middle another 15 minutes. It does not give you a silent first 20.

## The twelve moves

### 1. Receiving the problem

Read it once without the model. Underline the nouns that are data and the verbs that are behaviour.

**Say:** "I'm going to read it once and restate it before I open the assistant."

### 2. Clarifying

Ask at most two questions that change the code. Then assume in public.

**Say:** "If I don't get an answer I'll cap `limit` at 100 and return 422 past that. Tell me if you'd rather I clamp."

### 3. Understanding the repository

Run the tests. Open the handler. Then, if you want a second opinion:

```text
Explain only. Do not edit.
Where does GET /tasks build its response? Cite file and line.
What test covers the unfiltered list?
```

Check the citation. **Say:** "The model pointed at `list_tasks` around the return. I have it open. The existing test expects a bare list, so my change will break that test on purpose and I'll update the assertion to look at `items`."

### 4. The strategy

One minute. Choice, alternative, first slice. **Say:** "Offset and limit. Not cursors. First slice is the happy path and the new JSON shape. Second is the 422s."

### 5. Which AI capabilities

- Ask or a no-edit prompt to confirm the map.
- A plan prompt only if the task is bigger than one function.
- An edit prompt for one slice.
- You type the change yourself when you already know the line. Saying "I'll just change the comparison, it's one line" is a strong use of judgment, not a refusal to be modern.

**Say:** "I'll let it draft the slice. I won't let it pick the status codes. Those are already decided."

### 6. Writing the prompt

Use the slice prompt in [scenario 4](../prompt-library/04-implementing-a-feature.md). Paste your decisions into it. Do not improvise "make it robust."

### 7. Reviewing

Read the diff before `pytest`. **Say:** "I'm reading the diff before I run it. I want to see if it edited the tests."

### 8. Implementing in slices

Green on slice 1, then slice 2. Do not queue the whole ticket.

### 9. Running tests

You run them. If the tool ran them, you run them again. **Say:** "Running `pytest` myself."

### 10. Fixing failures

Diagnose, then a small prompt or a hand edit. Do not say "fix the tests" unless you have decided the test is wrong, and you say why.

### 11. Explaining

Tie each decision to a line. **Say:** "422 is these branches. The empty page is this return, before the error checks, only when offset is past `total`."

### 12. Presenting

**Say:** "Done means: paged JSON, defaults, cap, negative offset rejected, past-the-end empty. Not done: stable paging if the list changes mid-walk. Tests I ran: the file, plus limit 100 and 101. I reverted a class the model added. I can walk any line."

## A full example

The interviewer can see Cursor. AI is allowed. The repository is [task-tracker-api](../practice-repos/task-tracker-api/) before pagination exists. The interviewer says: "Add pagination to the list endpoint. You have about 45 minutes. Talk."

**Candidate, minute 1.** "I'll restate. `GET /tasks` should return a page. I haven't heard the page size, the parameter names, or whether the body can change shape. Today it returns a bare list. I'm assuming `offset` and `limit`, default limit 20, max 100, 422 outside that, and a body of `items`, `offset`, `limit`, and `total`. Order stays `created_at` then `id` if I can see a timestamp. If the list has no timestamp I'll ask before I invent one."

**Interviewer.** "Your assumptions are fine. There's a timestamp."

**Candidate, minute 4.** Runs `pytest -q`. It passes. Opens `app.py`. "State is the `TASKS` list. `list_tasks` returns it directly. I'll keep storage. I won't add a database."

**Candidate, minute 6.** A no-edit prompt:

```text
Explain only. Do not edit.
Cite lines. What does GET /tasks return today, and which test asserts the bare list?
What field can I sort on?
```

The model says `created_at` and names `test_list_tasks`. The candidate opens both. "That matches. I'll sort by `created_at`, then `id`, so equal timestamps don't shuffle."

**Candidate, minute 8.** "Plan. Slice 1: new body, offset, limit, defaults, no validation yet, update the old test so it still checks titles under `items`. Slice 2: 422s. Alternative I am not building: cursor pagination. It matters if we insert during a walk. One client, one list, I'll skip it."

**Candidate, minute 10.** Sends the slice-1 prompt from [scenario 4](../prompt-library/04-implementing-a-feature.md), with the file paths filled in.

**The model** edits `app.py`, updates tests, and also adds a `PaginationParams` class plus a comment about future SQL.

**Candidate, minute 16.** "I'm not taking the class. The handler is ten lines. A class implies a second implementation we don't have." Reverts the class, keeps the slice. Reads the slice aloud: "Total is `len` before slicing. Slice is `[offset:offset+limit]`. Defaults applied if the query params are missing. It also used `reverse=True`. I asked for ascending. I'll flip that before I run." Flips it.

**Candidate, minute 18.** `pytest -q`. One failure: a test still indexes the JSON as a list. "That's the break I predicted. I'll update that assertion to `body['items']` and keep the title check." Does it by hand. Pytest passes.

**Candidate, minute 22.** Slice-2 prompt: 422 for `limit` outside 1..100, `offset < 0`, non-integers. "Do not change the success shape."

**The model** implements the checks but clamps `limit=101` to 100 and returns 200. The new test expected 422 and fails.

**Candidate, minute 28.** "The test is right and the code is wrong. I asked for 422, not a clamp. Clamping hides a client bug." Changes the branch by hand from a clamp to `HTTPException(422)`. Runs pytest. Green. "I'll add the case `limit=100` returns 200 so the boundary is locked on both sides." Adds that test by hand. Green.

**Candidate, minute 34.** Manual check they mention out loud: "Empty store, `offset=0`. I expect `items: []`, `total: 0`, 200. I'll look at whether the handler crashes on an empty list before the slice." Reads the code. It doesn't crash. Runs a one-off or a tiny test. "Good."

**Candidate, minute 38.** "I'm looking at concurrency because the list is global. Two requests can interleave. For pagination that's a torn page, not a crash. A lock would be new scope. I won't add it unless you want it. I'll say the limitation."

**Interviewer.** "Why not cursors?"

**Candidate.** "A cursor encodes the last `created_at` and `id` you returned. The next page asks for items strictly after that pair. Insertions earlier in the list don't shift you. The cost is a token the client must store, and a comparison instead of a slice. Worth it with concurrent writers. This exercise doesn't have them."

**Candidate, minute 43.** "What I shipped: paged body, defaults 0 and 20, max 100, 422 on bad limit, bad offset, and non-integers, past-the-end is an empty page, sort by time then id. What I rejected: a pagination class, clamping, a database, a cursor. Tests: `pytest` on this file, including the boundaries. I can change the default if you want to see me do it live."

### What control looked like

The candidate let the model draft and refused three things: a class, a descending sort, and a clamp. Each refusal had a reason tied to a decision they stated earlier. They ran the tests themselves. They could answer the alternative. They did not claim the list was safe across threads.

### A version that loses the round with a green suite

Same model output. The candidate accepts the class, the descending sort, and the clamp. They ask the model to "fix the failing test" and it changes 422 to 200. Pytest is green. The interviewer asks what `limit=101` returns. The candidate says "the AI set it up to be safe." They cannot find the clamp. That session fails the ownership test in [what interviewers evaluate](what-interviewers-evaluate.md) even though the terminal is green.

## When AI is not permitted

LinkedIn's default, Amazon's reported interview rule, Anthropic's live-interview rule, and Salesforce's interview rule are all "no, unless this round says yes." Confirm in [the comparison](../research/assessment-comparison.md) and then in your invitation. If the answer is no:

- Close the assistant. Disable editor AI completion if the rule names auto-completion (Uber's secondary-quoted guide does).
- Do not keep a second device in the conversation. The Amazon press account treats live generative AI as disqualifying unless permitted.
- Keep every other step. Restate, assume, trace, slice, test, explain. You type the code. The slices get smaller, not sloppier.
- Do not lie if you used a tool anyway. Undisclosed use is the failure mode those policies describe. If you are unsure mid-round, ask before the prompt, not after.

Preparation the night before is a different stage. LinkedIn, Anthropic, and Salesforce say preparation with AI is fine if the result is still true and still yours. Do not bring those notes into a round that forbids the tool, and do not recite an answer you cannot unpack.

## Check your understanding

1. The model clamps `limit`. The tests fail. What do you say before the next edit?
2. AI is allowed, the change is a one-line comparison, and you know the line. What is the strong move?
3. You are not sure the round allows Cursor. What do you do?

## Answers

1. "The test expects 422 and the code clamps to 100 and returns 200. The test matches the decision I stated. I'll change the branch, not the assertion."
2. Type the comparison yourself and say why. Reviewing a one-line model edit costs more than writing it.
3. Ask the interviewer before the first prompt. If you cannot get an answer, do the work without the assistant.
