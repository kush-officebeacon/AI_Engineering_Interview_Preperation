# What interviewers actually evaluate

Assume the interviewer can see the session: prompts, diffs, terminal, tests, and what you say. Some companies do this by screen share (Atlassian's guides say you screen share). Some platforms store the assistant transcript (HackerRank's Amazon guide says the evaluator can see it). Some rounds have no assistant at all. The behaviours below are what a strong session shows in every case. Where a tool is forbidden, "delegate" means you do not. The thinking steps stay.

This is `[Analysis]`. It is informed by what companies have written they care about: LinkedIn on trade-offs and authenticity, Atlassian on narration and learning agility, Canva on reviewing generated code, Meta on debugging and collaboration. Those pages are cited in [the research](../research/company-assessment-research.md). They are not a shared scoring rubric. No company here has published the twelve rows below as a form.

For each stage: what they are looking for, what a weak candidate does, what a strong candidate does, what you say, and what evidence is left behind.

## 1. Understanding the problem before touching the code

**Looking for:** You can restate the goal, the constraints, and what "done" means. You notice what was not said.

**Weak:** Opens the editor or the chat and types the ticket in. Asks "should I use a class?" before stating what the feature does.

**Strong:** Writes two or three sentences in their own words. Lists the input, the output, and one ambiguity. Asks the highest-value question first.

**Say:** "I'll restate it. We need `GET /tasks` to return a page, not the whole list. You haven't said the page size or what an out-of-range page returns. I'm assuming limit 20 and an empty page past the end, unless you want something else."

**Evidence:** A short note, visible, before the first code prompt. The prompt, when it comes, contains those decisions.

**Follow-up:** "What if a client is on page two and a new task is inserted at the front?" "Why did you ask about the error code and not about the database?"

## 2. Investigating an existing repository

**Looking for:** You build a map from the files, and you can run the tests. You do not trust a tour you did not check.

**Weak:** Asks "explain this codebase" and reads the answer aloud. Cannot name the test command.

**Strong:** Finds the README, runs the tests, opens the entry point, then asks the model for a slice and verifies the paths.

**Say:** "Tests pass with `pytest`. The list handler is `list_tasks` in `app.py`. I'm going to trace who mutates `TASKS` before I change the response."

**Evidence:** A test run in the terminal. A prompt that cites a real file. You correcting the model when it names a file that is not there.

**Follow-up:** "Where is the data stored, and what happens on restart?" "Show me the test that would fail if you broke creation."

## 3. Finding the relevant files and dependencies

**Looking for:** A small set of files, and a reason each is in the set. Awareness of callers.

**Weak:** Lets an agent touch every file. Cannot say which change was necessary.

**Strong:** Names the handler, the pure function if there is one, and the test file. Says "I am not changing storage."

**Say:** "The behaviour lives in `list_tasks`. Callers are the route and `tests/test_tasks.py`. I'll edit those two. There is no separate repository layer, and I won't add one."

**Evidence:** The diff's file list matches the sentence you said before the edit.

**Follow-up:** "What else imports this function?" "Why didn't you split the file?"

## 4. Identifying missing requirements

**Looking for:** You notice ambiguity and you either ask or you label an assumption. You do not hide the guess inside the code.

**Weak:** Fills every gap silently. When asked, says "the AI decided."

**Strong:** Ranks one or two questions. States the assumption and the cost of being wrong.

**Say:** "The two gaps that change the code are the maximum page size and whether this is a breaking change to the JSON shape. I'll assume a max of 100 with 422, and a breaking change, and I'll flag both."

**Evidence:** The assumption is in the prompt or in a comment you are willing to defend. Not a comment the model added that you have not read.

**Follow-up:** "What did you consider and reject?" "What would you do if I said the old clients must keep working?"

## 5. Communicating the approach

**Looking for:** A plan with a choice, an alternative, and a first slice. Short enough to interrupt.

**Weak:** Disappears into a long agent run. Or describes a framework they are not going to build.

**Strong:** Says the approach in under a minute, names what they are not building, and starts the first slice after a pause for the interviewer to object.

**Say:** "I'll keep the list in memory. Offset and limit in the query string. First I'll change the response shape and make one test pass. Then I'll add the 422s. Cursor pagination would be more stable if rows were inserted during paging. I don't think we need it here."

**Evidence:** A plan prompt, or a spoken plan, that matches the first diff. The first diff is smaller than the whole feature.

**Follow-up:** "Why not a cursor?" "What's the first test you'll write?"

## 6. Deciding what to delegate

**Looking for:** Judgment. The model does bounded work. You keep the contract, the review, and the final call.

**Weak:** One prompt: "implement the ticket." Or the opposite: refuses a tool that the interviewer just said is allowed, and then runs out of time typing boilerplate they could have checked.

**Strong:** Delegates a draft of a function or a test. Does not delegate the question "is this the requirement?" When the tool is forbidden, does the same steps by hand and says so.

**Say:** "I'll have the model draft the slice function. I'll write the assertion myself so the test isn't copied from the implementation." Or, if AI is off: "This round doesn't allow an assistant. I'll write the slice directly. Same contract."

**Evidence:** Prompts with a file list and a stop. Your own edits on top of the draft are visible in the diff.

**Follow-up:** "Why did you give it the tests as well?" "What would you not let it touch?"

## 7. Constructing prompts

**Looking for:** Constraints, an observable done condition, and no conflicting goals. You are specific because you understand the task, not because you memorised a template.

**Weak:** "Make it production ready and follow best practices." Or a page of template with the objective missing.

**Strong:** One slice, the files, the behaviour, what not to do, how you will judge it.

**Say:** "I'm going to ask for the limit check only, and I'll tell it not to touch the sort we already accepted."

**Evidence:** The prompt text itself, if the interviewer can see the chat. A prompt you would be willing to read aloud.

**Follow-up:** "Read me the prompt you just sent." "What did you deliberately leave out?"

## 8. Reviewing generated changes

**Looking for:** You read the diff before you trust the run. You reject scope creep. You notice a weakened test.

**Weak:** Watches the agent finish, sees green, says "looks good." Cannot describe a hunk.

**Strong:** Reads the file list, then the tests, then the logic. Reverts an unrelated refactor. Points at a line and says what it does.

**Say:** "It also wrapped the list in a class. I'm reverting that. The slice itself is these four lines. `items[offset:offset+limit]` with the total taken before the slice. I'll run the tests after the revert."

**Evidence:** A revert or a follow-up prompt that quotes the mistake. Time spent in the diff, visible on the screen share.

**Follow-up:** "What did the model change that you didn't ask for?" "Read the condition and tell me what limit=0 does."

## 9. Verifying independently

**Looking for:** Checks that were not designed solely by the model. A command you ran. An input you picked.

**Weak:** "The AI said the tests pass." One happy-path test.

**Strong:** Runs pytest themselves. Adds the boundary (exactly the limit, one past it). Breaks the code briefly to see the test go red, or can explain why a particular assertion would fail.

**Say:** "Pytest is green, 11 passed. I'm also sending limit=100 and limit=101 by hand. 100 is 200, 101 is 422. That's the cap."

**Evidence:** The terminal scrollback. A test for the boundary that you can open and explain.

**Follow-up:** "What input did you try that is not in the file?" "How do you know the test isn't passing for the wrong reason?"

## 10. Reacting when the AI is wrong

**Looking for:** You notice, you say what is wrong, you don't insult the tool or obey it. The next prompt contains the new fact.

**Weak:** Sends "try again" with no new information. Or apologises and keeps the bug because the suite is green. Or argues with the interviewer that the model must be right.

**Strong:** States the expected value and the actual value. Points at the condition. Asks for a smaller correction or types it.

**Say:** "The 6th call returned 200. The check uses `>` after append, so five existing events still allow another. I'll change it to reject when the window is already full, before append. I am not changing the limit from 5 to 4. That would fake the test."

**Evidence:** A diagnosis prompt that forbids a patch, then a small patch. The constant `5` still 5.

**Follow-up:** "How did you know the test was the spec and not the code?" "What would you do if you couldn't reproduce it?"

## 11. Explaining trade-offs and alternatives

**Looking for:** One real alternative. A reason. A condition under which you would switch. No fabricated scale numbers.

**Weak:** "This is optimal and production ready." Or a memorised lecture about microservices that the code does not implement.

**Strong:** Names the discarded option and the failure mode of the chosen one.

**Say:** "Offset is fine for this list. It lies if a row is inserted while you page: you can skip or repeat an item. A cursor would fix that. I'd switch if we had concurrent writers. We don't, in this exercise, and I didn't want the extra token."

**Evidence:** You can point at the line that would be wrong under the failure mode you just named.

**Follow-up:** "What did you leave unsolved on purpose?" "How would the tests change if we required the cursor?"

## 12. Demonstrating ownership

**Looking for:** You stand behind the result, including lines you did not type. You know what you did not do. You do not blame the tool.

**Weak:** "That's what the AI generated." Cannot modify the code when asked. Agrees with every hint without thinking.

**Strong:** "I accepted this diff. The part I would not defend is gone. Here's the limit I chose and the test that locks it. If you want the old JSON shape preserved, I'd add it as a separate path rather than pretend this is compatible."

**Evidence:** You can edit a line live, correctly, when asked. You can say "I don't know" and then find out from the code in front of you.

**Follow-up:** "Change the default from 20 to 10." "Delete the helper and inline it. Does anything break?" "Which line would you be least happy to see in a year?"

## How this shows up on a score

The mock rubric in [mock assessments](mock-assessments.md) scores nine dimensions. A correct program you cannot explain is capped. A wrong program you can diagnose is not a zero. Interviewers at the companies in the research set keep saying, in different words, that they want the thinking. Believe that when you are tempted to hide a prompt.

## Check your understanding

1. The suite is green and you cannot explain the helper. Which stage have you failed, even though stage 9 looks done?
2. The interviewer says the assistant is allowed. You never use it and you finish half the task. Is that automatically strong?
3. Name the evidence, not the speech, for stage 8.

## Answers

1. Ownership, and review. A green suite is not stage 9 unless you ran a check you understand. It is certainly not stage 12.
2. No. Refusing a permitted tool and running out of time is a judgment miss at stage 6. Using it blindly is also a miss. The strong move is to use it where it is faster and still review.
3. A revert, a follow-up prompt that quotes a bad line, or time on screen in the diff before the test run. Speech without that evidence is cheap.
