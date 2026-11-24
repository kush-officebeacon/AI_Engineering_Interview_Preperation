# Scenario 8: Explaining and defending an implementation

Goal: practise being questioned until you can answer without the model. The model plays a skeptical reviewer. You still check its challenges against the code, because it will invent some.

Method: [planning](../engineering-playbook/planning-and-architecture.md) and the ownership sections of [what interviewers evaluate](../interview-preparation/what-interviewers-evaluate.md).

## Bad prompt

```text
Explain my implementation so I sound senior in the interview.
```

This asks for a performance. The model will inflate the design ("this ensures horizontal scalability") beyond what the code does. If you repeat that sentence and the interviewer asks how many processes you ran, you will not have an answer. Sounding senior is a side effect of understanding the code. It is not a prompt target.

## Improved prompt

```text
Challenge my pagination implementation.
Ask me tough questions, including alternatives and failure modes.
```

The instinct is right. Without the code and a ban on inventing requirements, the questions will be generic ("how does this scale to a million users?") and you will practise hand-waving.

## Excellent prompt

```text
Context: You are a senior engineer reviewing my work. I must answer in my own words later, so your questions should be ones the code can actually answer. Do not flatter me. Do not rewrite the code.
Mode: question me. One round at a time. Wait for my answer. If my answer is vague or contradicts the code, say what is wrong with it and ask again. Do not give me the full answer on the first correction.

The code:
<paste list_tasks and the tests, or point at the files>

The decisions I think I made:
- offset/limit, default 20, max 100, 422 outside that
- offset past the end is 200 and empty items
- sort by created_at, then id
- in-memory list, no database, because that is what the project already did

Ask, across the conversation, questions in this spirit (use the code, not this list verbatim, and skip any that do not apply):
- Why this approach instead of cursor pagination?
- What did you decide not to build?
- What input makes this wrong?
- What happens on invalid input? Point at the line.
- What happens if two requests hit this list at once?
- What would you change if this had to run as more than one process?
- Which test would fail if the sort tie-break disappeared?

Start with the question that would embarrass me most if I could not answer it.
Do not ask more than one question in the first message.
```

### Why this is better

- It forbids the model from answering for you. The learning is in your reply.
- "Contradicts the code" gives it a standard other than vibe.
- One question at a time matches a real interview. A list of eight questions lets you pick the easy one.
- "Embarrass me most" pushes it toward the hole, not the tutorial.
- Your stated decisions give it something to attack. A defender with no stated decision gets philosophy questions.

## Prompts for a specific challenge

Use these when you want to drill one topic. Paste the function.

```text
Ask me only about invalid input.
I will answer. Then quote the line that confirms or contradicts me.
Do not fix the code.
```

```text
I chose offset pagination. Argue for cursors in four sentences, using this API's actual failure mode (inserts while paging).
Then stop. I will decide whether the argument applies to a single-user exercise.
Do not change the code.
```

```text
Pretend this list is now shared by several processes and the limit must be global.
Ask me what in the current function becomes false.
Accept "I would not pretend a lock fixes this" as a valid direction.
Do not generate a Redis design unless I ask.
```

```text
I cannot explain this helper the model wrote.
Ask me three questions that force me to read it, starting with "what does this return on an empty list?"
If I get one wrong, point at the line and let me try again.
Do not replace the helper yet.
```

The last one is the rule from the validation guide: code you cannot explain is not done. The model is a tutor here, not an author.

## What to verify while you practise

- The "embarrassing" question is about your code. If it asks about Kubernetes and you wrote a list slice, say "that isn't this change" and ask for a question about the slice. You are allowed to reject a bad interview question from a model. You should also notice if a human interviewer asks it, and answer the scope honestly: "This design is one process. Across processes the list is the wrong store. I haven't built the other store."
- When the model says you contradicted the code, open the line before you agree.
- After a session, close the chat and answer the same question on paper. If you can only answer with the chat open, you watched an explanation. You did not learn it.

## A closing check you can run on yourself

Say these out loud, with no model:

1. What does `GET /tasks?limit=1` return, field by field?
2. Why is the maximum enforced in the handler and not in the client?
3. What did you leave unsolved on purpose?
4. Which test fails if you delete the tie-break?
5. What would you refuse to claim in an interview?

If one of them is fuzzy, that is the next prompt. Not "explain the whole feature."

## Check your understanding

The model asks, "How does this handle a thundering herd?" You implemented a page of a list. What is a strong answer, and what is a weak one?

Strong: "It doesn't. This is one list in one process. A herd is not a failure mode of the slice. Across processes I would not keep this store." Weak: a paragraph about load balancers that your code does not implement.
