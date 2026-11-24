# AI-assisted engineering and interview mastery

A learning system for using Cursor and Claude as an engineer, not as a spectator. The target is intern and new-grad interviews, with the research focused on LinkedIn, Amazon, and Atlassian, and on the difference between companies that **use AI to evaluate candidates** and companies that **let candidates use AI**.

This is not a course you finish by scrolling. Each document ends in something you do.

## The goal

You can look at a change, including one a model drafted, and say what it does, why it is this shape, what you refused, and what you ran to check it. If you cannot say that, the change is not done.

## Start here

1. Read [the research checkpoint](research/research-checkpoint.md) and answer the three questions without looking at the answers.
2. Skim [the cheat sheet](interview-preparation/assessment-cheatsheet.md) so you know the shape of the work.
3. Do Level 1 in [the training roadmap](interview-preparation/training-roadmap.md). Write the session in [the journal](practice-log/learning-journal.md).

Do not start with the mock interview. The mock is Level 6. It is harsh on purpose, and it is useless if you have not practised a slice.

## Map

| If you want to | Open |
| --- | --- |
| Know what LinkedIn, Amazon, and Atlassian have actually published | [research/company-assessment-research.md](research/company-assessment-research.md) |
| See the comparison table | [research/assessment-comparison.md](research/assessment-comparison.md) |
| Separate "AI judges me" from "I may use AI" | [research/ai-in-hiring-trends.md](research/ai-in-hiring-trends.md) |
| Check a source before you repeat it | [research/sources.md](research/sources.md) |
| Learn the working loop | [engineering-playbook/ai-assisted-development.md](engineering-playbook/ai-assisted-development.md) |
| Read a repository | [engineering-playbook/codebase-navigation.md](engineering-playbook/codebase-navigation.md) |
| Plan a change | [engineering-playbook/planning-and-architecture.md](engineering-playbook/planning-and-architecture.md) |
| Decide a diff is wrong | [engineering-playbook/validation-and-testing.md](engineering-playbook/validation-and-testing.md) |
| Debug or review | [engineering-playbook/debugging-and-code-review.md](engineering-playbook/debugging-and-code-review.md) |
| Write a prompt | [prompt-library/00-prompt-framework.md](prompt-library/00-prompt-framework.md) and scenarios [01](prompt-library/01-codebase-understanding.md) through [08](prompt-library/08-defending-implementation.md) |
| See the interview through the interviewer's eyes | [interview-preparation/what-interviewers-evaluate.md](interview-preparation/what-interviewers-evaluate.md) |
| Walk a full round | [interview-preparation/live-interview-playbook.md](interview-preparation/live-interview-playbook.md) |
| Revise the morning of | [interview-preparation/assessment-cheatsheet.md](interview-preparation/assessment-cheatsheet.md) |
| Practise on code | [practice-repos/README.md](practice-repos/README.md) |

Research date for the company pages: **24 November 2026**. Re-read the primary link before an interview that is months later. The invitation you receive beats this repository.

## Commands, in any later chat in this project

A project rule, [mentor mode](.cursor/rules/mentor-mode.mdc), applies to chats here.

| You say | What happens |
| --- | --- |
| Start a mock assessment | An interviewer, a time limit, an AI rule, questions, then nine scores. |
| Quiz me on Level N | One question at a time from that level of the roadmap. |
| Review my prompt | What decision is missing, against the prompt framework. |
| Challenge my implementation | One hard question at a time, tied to the code. |
| Explain X | The playbook's version of X, then a check. |

On practice exercises the mentor should ask before telling, and should not open `SOLUTIONS.md` until you have tried or you explicitly ask.

## Practice code

Python 3.10 or newer.

```bash
cd practice-repos/task-tracker-api
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest tests/test_tasks.py          # passes
pytest tests/test_exercise.py       # fails until you implement the feature
```

The limiter and the cache need only pytest. Their suites fail on purpose. Read each repository README before you run anything, and leave `SOLUTIONS.md` closed.

## What this project will not do

It will not pretend a Reddit post is a company policy. It will not tell you to use an assistant in a round that forbids one. It will not treat a green test run as proof.
