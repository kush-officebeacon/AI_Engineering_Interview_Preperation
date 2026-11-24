# Mock assessments

Say **Start a mock assessment** in this project. The mentor rule tells the assistant to follow this file. You can also run one alone with a timer and score yourself. Self-scores are useful. They are kinder than a real interviewer. Write them down anyway.

## How a mock runs

1. Ask which level the candidate has finished. If they do not know, use Challenge A.
2. State, in the first message:
   - the challenge id and the problem
   - whether AI is allowed, and which tools
   - the time limit
   - what "done" means
   - that you will not write the solution while the clock runs
3. During the attempt, act as the interviewer.
   - If the candidate is silent, ask what they are assuming.
   - If they paste the whole ticket into the model, ask them to read the prompt aloud and say what they left unconstrained.
   - If they are wrong, ask what the code does on one input. Do not hand them the patch.
   - One hint is a question. A second hint can point at a file or a condition. Do not give a third hint as code.
4. Stop at the time limit even if they are mid-edit.
5. Score with the rubric below. A technically correct result they cannot explain or cannot show a check for is capped at 4 on coding decisions and at 4 on ownership.
6. Append a short entry to [the journal](../practice-log/learning-journal.md) using the template there.

Teach with questions on practice days. On a scored mock, stay in interviewer mode until the score is delivered. After the score, you may teach.

## Rubric

Score each dimension from 1 to 10. The anchor is the behaviour, not the vibe.

| Score | Meaning |
| --- | --- |
| 1–3 | Missing, or actively misleading (hidden AI use, tests edited to go green, explanation that contradicts the code). |
| 4–5 | Attempted. Gaps they did not notice. |
| 6–7 | Solid. One real weakness they can correct. |
| 8–9 | Strong under questions. Trade-offs are real. |
| 10 | You would be comfortable with them owning this change. Rare. Do not give it for a kata that only matches a template. |

| Dimension | What a 7 requires | What pulls it down |
| --- | --- | --- |
| Problem understanding | Restates behaviour, names an ambiguity or a conscious assumption. | Starts coding on a misread and never checks. |
| Repository investigation | Runs the tests, names the file they will change. | Cannot find the handler without a tour they did not verify. |
| Planning | Says the first slice and one alternative they are not building. | One prompt for the whole ticket, or a design the code does not contain. |
| Prompt quality | Constraints, files, a done condition. Or no prompt, because they typed a change they understood. | "Fix it" / "make it production ready". |
| Appropriate use of AI | Matches the round's rule. Delegates a draft, keeps the decision. | Uses AI when it was forbidden, or refuses a permitted tool and stalls. |
| Coding decisions | The change matches the contract. Edges they touched are correct. | A green suite with the wrong status code, a weakened test, or a new dependency they cannot justify. |
| Verification | They ran the tests. They can name one input outside the file they thought about. | "The model said it passed." |
| Communication | An observer can follow the decisions. | Silence, or a speech that does not match the diff. |
| Ownership | They defend lines they did not type, and they say what is unfinished. | "That's what the AI generated." Correct code they cannot change when asked. Cap at 4. |

Overall is not an average you hide behind. State the lowest dimension and why it dominates the hiring read.

## Evaluation template

```text
Challenge:
Time used:
AI rule:
Result (tests / how far):

Scores
- Problem understanding: n — reason
- Repository investigation: n — reason
- Planning: n — reason
- Prompt quality: n — reason
- Appropriate use of AI: n — reason
- Coding decisions: n — reason
- Verification: n — reason
- Communication: n — reason
- Ownership: n — reason

Cap applied: yes/no, because
Strongest moment:
Weakest moment:
Next drill (one exercise, not a personality note):
```

## Challenge bank

### A. Paged list, AI allowed

- **Level:** 3 or 6. **Time:** 45 minutes. **AI:** allowed (Cursor or Claude).
- **Repo:** [task-tracker-api](../practice-repos/task-tracker-api/).
- **Problem:** Implement the behaviours in `tests/test_exercise.py`. Do not edit those tests. Existing tests must stay meaningful.
- **Interviewer note:** Ask, at minute 10, whether `status` and `limit` together return a bare list or an object. There is no single answer in the tests. Judge the decision, not a secret answer.
- **Done:** Exercise tests pass, old tests pass, candidate can explain the body shape.

### B. Paged list, AI forbidden

- Same as A. **Time:** 45 minutes. **AI:** not allowed, including autocomplete if you can turn it off.
- **Interviewer note:** If they reach for a tool, stop them once. A second time ends the round as a rule break, score appropriate-use at 2, and still score the engineering they did before that.

### C. Four failing tests

- **Level:** 4. **Time:** 40 minutes. **AI:** allowed for explanation. Ask them to keep the first prompt from editing.
- **Repo:** [rate-limiter-bugs](../practice-repos/rate-limiter-bugs/).
- **Problem:** Make `pytest` pass without editing tests. Do not open `SOLUTIONS.md`.
- **Interviewer note:** If they change `limit` to 4, ask what the fifth call does. If they delete `after_check`, ask whether the race is gone or only the demonstration.

### D. Cache kata

- **Level:** 6. **Time:** 45 minutes. **AI:** allowed.
- **Repo:** [lru-cache-kata](../practice-repos/lru-cache-kata/).
- **Problem:** Parts 1 to 4 in order, as far as they can get. Later parts must not break earlier tests.
- **Interviewer note:** At the end, close the assistant and ask them to evict a key on paper. If they cannot, ownership is capped.

### E. Cache kata, no AI

- Same as D. **AI:** not allowed. **Time:** 45 minutes. Part 4 is optional if parts 1–3 are explained.

### F. Review, no implementation

- **Level:** 4 or 6. **Time:** 20 minutes. **AI:** allowed only as a reviewer, using [prompt 06](../prompt-library/06-code-review.md). They must confirm or reject each finding.
- **Problem:** Give them this function and this requirement. Requirement: at most `limit` calls per `window` seconds; the call that reaches `limit + 1` is rejected; `limit` stays what the caller passed.

```python
def allow(events, now, limit, window):
    recent = [t for t in events if (now - t).total_seconds() <= window]
    if len(recent) > limit:
        return False
    events.append(now)
    return True
```

- **Interviewer note:** Defects they should be able to find: `<=` keeps an event exactly `window` seconds old, so the window is a second too long if the contract is a half-open interval; `>` allows the call when `len(recent) == limit`. A finding about SQL injection is a false positive. Judge whether they reject it.

### G. Unfamiliar file

- **Level:** 2. **Time:** 25 minutes. **AI:** allowed, explain-only.
- **Problem:** In a clone of `pallets/click` or `psf/requests`, trace one path and name one missing test. No code changes.
- **Interviewer note:** Ask them to open a file the model cited. If it does not exist, that moment is the score.

## After the mock

One drill, not five. Examples: "redo challenge A slice 1 only, and revert one extra change", "write the concurrency cause without looking", "run challenge B for 20 minutes."

The journal is the record. The score without a next drill is a number.
