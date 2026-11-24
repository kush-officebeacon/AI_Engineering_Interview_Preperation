# AI in hiring: two different developments

Research date: **24 November 2026**. Source IDs are in [sources.md](sources.md). Company detail for LinkedIn, Amazon, and Atlassian is in [company-assessment-research.md](company-assessment-research.md). The comparison table is in [assessment-comparison.md](assessment-comparison.md).

## Why the split matters

Companies are doing two things that sound similar and are not.

**Category A. The company uses AI on you.** A model drafts a screen, scores a transcript, recommends a role, or writes the interviewer's notes. You may not be holding a coding assistant at all. The thing being tested is still you, but a model sits in the evaluation path. The fair questions are: do you know it is happening, can you decline, and does a human decide?

**Category B. You are allowed, or expected, to use AI while you do the engineering task.** The company is trying to see how you work when an assistant exists. The fair questions are: which tool, which round, do you have to use it, and can you explain the result?

Mixing them up causes two mistakes. The first is using Cursor in a round that forbids it because "Amazon uses AI." The second is ignoring a round that requires the in-platform assistant because "interviews ban AI."

A third fact sits next to both and is neither: **using AI to prepare** (rewrite a bullet so it is still true, practise a story, look up a concept the night before) is explicitly encouraged by LinkedIn `[L3]`, Anthropic `[N1]`, and Salesforce `[S1]`. Preparation is not the assessment.

## What is actually changing

`[Analysis]`, grounded in the sources below.

1. **Permission is per round, not per company.** LinkedIn's own page says live interviews are human-only unless the recruiter has said that AI is part of that format `[L3]`. Amazon's January 2026 post describes an assistant inside a technical assessment `[A1]`, while a February 2025 press account describes a ban on generative AI in interviews unless explicitly permitted `[A5]`. Atlassian's public handbook does not mention AI `[T1]`; a Principal Backend PDF does, for one coding setup `[T2]`.
2. **The allowed tool is usually the one inside the interview environment.** Meta says no outside AI tools, only the CoderPad assistant `[M1]`. HackerRank's Amazon guide distinguishes "no GenAI" on the single-file question from an embedded assistant on the repository question `[A4]`. Canva is the clear exception in this set: it tells backend, frontend, and ML candidates to bring Copilot, Cursor, or Claude `[C1]`.
3. **The task gets larger when the assistant is allowed.** Canva wrote that its old algorithm questions were solved by an assistant in seconds, so it replaced that screen with ambiguous product work `[C1]`. Atlassian's AI-enabled setup is "extend an existing repository," not "implement a textbook algorithm from a blank file" `[T2]`. `[Analysis]` If you only practise LeetCode, you are practising the round these companies are moving away from in the AI-enabled format, and you are under-practising the rounds that still ban AI.
4. **Ownership did not move.** Canva still expects you to own code you did not type `[C1]`. LinkedIn says follow-ups will probe thinking and trade-offs `[L3]`. Anthropic forbids AI-invented experience `[N1]`. The skill these pages describe is judgment, not prompting speed.
5. **India and new-grad coverage is thinner than blog posts imply.** Amazon says the OA structure can depend on the country and tells you to read the email `[A2]`. Google's reported pilot started as select US teams `[G2]`. Atlassian's written AI-enabled round is in a Principal guide `[T2]`. Do not generalise a US mid-level pilot, or a principal loop, into a Bengaluru new-grad loop.

## Category A: companies using AI to evaluate

Only what a primary source supports.

### LinkedIn, as a product used by other employers

`[Official]` `[L4]` Hirers on LinkedIn can send an AI audio or video screening interview. The hirer edits the AI-drafted questions and the "ideal answers" before sending. You may practise first; practice answers are not shared with the hirer. You may decline; declining does not automatically disqualify you. After a real attempt the hirer gets the recording, the transcript, a summary, and a rating from 1 to 5. The rating is the average of per-answer scores for match to the hirer's ideal answer, supporting detail, and structure. The hirer is responsible for checking the AI output. LinkedIn says it may use Microsoft Azure OpenAI for this product, and that Microsoft and OpenAI do not access member inputs except in circumstances described in LinkedIn's own note.

`[Official]` `[L5]` `[L6]` Hiring Assistant matches profile and resume data to qualifications and can run a screening conversation that a recruiter can take over. Recruiters must review AI output before deciding.

`[Analysis]` If a *future employer* invites you to a LinkedIn AI screen, you are in Category A. Speak in concrete examples. The rating description rewards evidence and structure, not jargon. Do not treat that product as LinkedIn's own software-engineer loop.

### Amazon

`[Official]` `[A1]`, 22 January 2026:

- Interview transcription pilot. Recording starts only with explicit consent. Candidates are told what is recorded, how it is used, and how long it is kept. The stated purpose is to let the human interviewer pay attention. 83% of candidates in the pilot reported more engaging conversations. Planned to reach more candidates during 2026. This is not a published statement that a model scores you.
- Role matching during screening. Candidates who reach interviews through this matching are described as 24% more likely to get a positive outcome after the initial loop than those evaluated without it. The post does not say the model is the hiring decision.

### Anthropic, on its own hiring

`[Official]` `[N1]`, updated 10 July 2025. Anthropic uses Claude to draft job descriptions, interview questions, and candidate emails, to analyse hiring metrics, to transcribe interviews, and to identify people to source. "We don't use your data to train Claude or let Claude make hiring decisions." Transcription and sourcing are Category A activities. The decision, as stated, stays with humans.

### HireVue, as a vendor, not as an employer in this study

`[Official]` HireVue's 2026 explainability statement, retrieved 24 November 2026 from the company's own PDF, says its video-interview AI uses the transcript only. It does not analyse face, body, background, or tone. Where "Interview Insights" is enabled, a model (the statement names Claude 3.7 Sonnet via AWS Bedrock) summarises the transcript and maps quotes to competencies. The statement says this layer does not create a new score. AI-scored assessments, when a customer turns them on, are a separate path. **No source in this pass says LinkedIn, Amazon, or Atlassian use HireVue for engineering hires.** It is here so you can recognise the vendor if an invitation names it.

### What Category A asks of you

`[Analysis]`

- Assume a human will read a transcript if you were told the interview is recorded or AI-screened. Speak in examples you can expand.
- If consent is requested, read what is retained. Amazon's post says it explains retention `[A1]`.
- Do not invent metrics to satisfy an "ideal answer." Anthropic's rule against fabricated experience is the right standard even where it is not the employer `[N1]`.
- Ask whether a human reviews the output before a decision. LinkedIn's product page says the hirer must `[L4]`. If another vendor is silent, ask.

## Category B: companies letting candidates use AI

### Meta (official, the clearest page in this set)

`[Official]` `[M1]`, Meta Careers hiring process, fetched 24 November 2026.

- "Select roles now include an authorized AI assistant within CoderPad."
- "Candidates are expected to use this AI assistant as part of the interview."
- What it says it evaluates: problem-solving, coding, debugging, and collaboration.
- Models you can pick inside CoderPad: Claude, ChatGPT, Gemini, and Meta's models.
- Design interviews use CoderPad with Mermaid markdown and the same assistant.
- "No outside AI tools or assistance are authorized."
- Languages for the AI-Native Coding Interview include Python, Java, TypeScript, C++, C#, Kotlin, Swift, Rust, and Go. You choose at the start.
- Preparation: a practice session in the same tool, via Career Profile.
- Process shape: recruiter conversation, initial screening, full loop. Typical duration of the whole process is about 2 to 3 months. **The page does not publish the length of the coding round.**

`[Reported-Candidate]` Secondary pages often say the coding round is 60 minutes. That number is not on `[M1]`. Treat it as unverified.

`[Analysis]` Meta is the model of "the assistant is required, and it is theirs." Practise reading an unfamiliar multi-file Python project, asking a model for a bounded change, and rejecting a wrong one. Do not practise by pasting the whole task in one prompt. Outside tools, including Cursor on your laptop, are outside the written rule.

### Google (press only)

`[Reported-Press]` `[G1]` Computerworld, 26 August 2025. A Google spokesperson said Google had banned AI tools during virtual interviews because it wants fundamental coding skills, and that some candidates are brought on site.

`[Reported-Press]` `[G2]` Business Insider, 7 May 2026, describing an internal document. A pilot for junior to mid-level software roles on select US teams, starting in the second half of 2026, would allow an approved assistant during a "code comprehension" round: read, debug, and optimise an existing code base. Interviewers would evaluate AI fluency, including prompt engineering, output validation, and debugging. The full article was not retrieved; this is from the public extract.

`[Reported-Press]` `[G3]` Business Insider, 20 October 2026. BI reports that the formats had been rolled out more broadly, that candidates can use Gemini in the code-comprehension interview, and that many engineers are expected to show AI fluency. The full article was not retrieved. BI attributes this to documents it reviewed, not to a Google careers page.

`[Unverified]` A Google careers page stating this policy. `[Unverified]` That the pilot includes India or new-grad roles in India. The May description was select US teams.

`[Analysis]` Until a recruiter says your loop includes the code-comprehension round, prepare to write and explain code with no assistant. The skills BI says Google would score in the pilot (validation, debugging, prompts) are the same skills this project trains, and they are worth having even if your loop never allows the tool.

### Microsoft (official page is silent)

`[Official]` `[MS1]`, interview tips, fetched 24 November 2026. Microsoft wants clarifying questions, stated assumptions, and a narration of your approach, "including the tools you would use and why." It wants fundamental knowledge, capability, and learning potential. It recommends STAR(R): situation, task, action, result, reflection. The page does **not** say AI is banned and does **not** say AI is allowed during the interview.

`[Unverified]` A sentence quoted by some 2026 policy trackers ("demonstrate their own skills without outside assistance unless explicitly permitted") does not appear on the page retrieved on 24 November 2026. Do not cite it as Microsoft's current text.

`[Analysis]` "The tools you would use and why" means explain your choice. It is not a written licence to run Copilot during a live coding exercise. Ask the recruiter.

### Uber (hub confirmed, rule second-hand)

`[Official]` `[U1]` The interview-prep hub exists at jobs.uber.com. The role-guide text did not come through in the fetch.

`[Reported-Secondary]` `[U2]` Pages updated in October and November 2026 quote Uber engineering guides as saying AI tools are not allowed during interviews unless the recruiter says otherwise, naming ChatGPT, automated response generators, and code auto-completion, and adding that some technical interviews may include an AI agent in the coding environment, with advance notice.

`[Analysis]` Behave as if outside AI is off unless your Uber recruiter writes otherwise. If they say an in-environment agent is provided, use only that. Confirm the quote against the PDF or page your recruiter actually sends; this project did not.

### Salesforce (official)

`[Official]` `[S1]`, Amanda Norton, Salesforce blog, 13 August 2025.

- AI may help you prepare and draft applications or cover letters, if every claim is true. The interviewer is assessing your thoughts and accomplishments.
- "Unless your interviewer specifically prompts you for an exercise, please do not use AI tools during the interview itself."
- Accessibility use goes through the recruiter.
- Do not record or transcribe the interview. The post says violating that could affect your candidacy.
- The post does not describe an engineering OA. `[Analysis]` If you get a coding test, follow that test's own rules. The blog post does not authorise AI there.

### Canva (official, and the opposite policy)

`[Official]` `[C1]`, Simon Newton, Canva Engineering, 11 June 2025.

- Backend, Machine Learning, and Frontend candidates are **expected** to use tools such as Copilot, Cursor, and Claude in technical interviews.
- A competency called AI-Assisted Coding replaced the Computer Science Fundamentals screen for backend and frontend. The stated reason: assistants solved the old questions immediately, and real work is mostly reading and changing existing code.
- What Canva says it now watches: when you use AI, how you break down an ambiguous requirement, whether your technical decisions are sound, whether you can find and fix bad generated code, and whether the result is at a production standard.
- Canva says candidates are told in advance and should practise.
- Code fluency is still required. You own the code whether you typed it or not.
- The post does not give a duration, a city, or a new-grad-only variant.

`[Analysis]` Canva is the company in this set that matches "bring Cursor" most closely. The behaviour it describes as successful is the behaviour in [the live interview playbook](../interview-preparation/live-interview-playbook.md): clarify, delegate a bounded piece, review, debug. The behaviour it describes as weak is accepting the first completion.

### Anthropic (official, mostly no)

`[Official]` `[N1]`, 10 July 2025.

| Stage | Rule |
| --- | --- |
| Application | Write the first draft yourself. Claude may refine it. Do not let Claude invent experience. |
| Take-home | No Claude unless the prompt says so. Example of a clear permission: "You may use Claude for this coding challenge." |
| Preparation | Encouraged, including research and mock answers. |
| Live interview | No AI unless they say so. |

Anthropic publishes the prompts it considers in and out of bounds. Read them before you apply there. The rule is about honesty of experience, not about whether Claude is a good model.

### Shopify (not established)

`[Unverified]` A candidate-facing AI rule for interviews. Shopify's public line that AI is part of how employees work, and the April 2025 CEO memo about employees using AI before asking for headcount, are about staff. `[Analysis]` Do not convert an employee expectation into a candidate permission. Ask the recruiter. If an assessment page forbids outside help, that page wins.

## What this means for a new grad in India

`[Analysis]`

- Your most likely default, on the pages that actually govern LinkedIn and the Amazon university OA, is **no assistant you bring yourself**. LinkedIn says so `[L3]`. Amazon's student page expects your own code and logs the browser `[A2]`.
- You may still meet an **in-platform** assistant if the invitation is the newer Amazon challenge `[A1]` `[A4]` or an Atlassian round that matches the principal guide's AI-enabled setup `[T2]`. Read the invitation the day it arrives, not the week before from memory.
- Meta and Canva are the employers in this set whose **own pages** say the candidate uses an assistant. Google's version is press reporting of a pilot that started in the US `[G2]`.
- The skills transfer in both directions. Clarifying a requirement, tracing a repository, reviewing a diff, and explaining a trade-off are what you do when AI is banned (you just type the code yourself) and what you do when AI is allowed (you refuse to ship a diff you cannot explain).

## Open items to re-check before you rely on this file

Policies move. Re-read the primary URL, not this summary, if your interview is more than a few months after 24 November 2026.

- Does Amazon's university OA page still omit the assistant, and does your India email match `[A1]` or `[A2]`?
- Has LinkedIn published an engineering-specific AI-round guide, or does `[L3]` still say "only if the recruiter says this round includes AI"?
- Has Atlassian put the AI-Enabled Code Design interview into a graduate or India guide, or does it remain in `[T2]`?
- Has Google published the code-comprehension round on a careers page, and does it include India?
- Does the Uber role guide your recruiter sends match the secondary quote in `[U2]`?
