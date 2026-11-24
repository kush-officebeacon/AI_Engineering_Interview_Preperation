# Company assessment research: LinkedIn, Amazon, Atlassian

Research date: **24 November 2026**. Audience: intern and new-grad software roles, with India called out wherever a source actually distinguishes it.

Read [sources.md](sources.md) for the label definitions and the link register. IDs like `[L3]` point there.

Two questions are kept apart throughout:

- **Category A.** The company uses AI to screen, match, transcribe, or interview candidates.
- **Category B.** The company lets the candidate use an AI coding assistant during an assessment.

A company can do one, both, or neither. Using AI inside the company does not mean candidates may use AI.

## How to use this file before an application

1. Read the official row for the company.
2. Read your own invitation. It overrides this file.
3. If the invitation is silent, ask the recruiter in writing. The question to ask is at the end of each company section.
4. Treat every `[Reported-Candidate]` paragraph as a description of what one person says happened to them.

---

## LinkedIn

### A. Purpose

`[Official]` `[L1]` LinkedIn's engineering careers page says interviews may explore communication, coding, craftsmanship, engineering design and architecture, and leadership. It does not publish a scored rubric, a language requirement, or a statement that AI-assisted problem-solving is a measured competency.

`[Official]` `[L3]` The candidate AI page says the interview should remain "a true reflection of your unique story and skills." After an assessment, candidates should be ready to discuss thinking, trade-offs, and real-world experience. `[Analysis]` That is an ownership requirement: you must be able to defend what you submitted, including work an assistant helped produce, if an assistant was permitted.

`[Official]` `[L1]` Bangalore is listed as an engineering hub alongside Dublin, the US sites, Tel Aviv, and remote. The page does not describe a different interview for India.

### B. Assessment process

`[Official]` `[L2]` The company-wide sequence is:

1. Application. Recruiting checks basic and preferred qualifications on the job description.
2. Conversation. A recruiter call, and possibly a video call with the hiring manager or another team member about experience and technical expertise.
3. Interview. Several more team members, each focused on a different skill. Depending on the role, a case study or a whiteboard exercise. Every interviewer takes notes for the hiring team. The recruiter is supposed to say what the interview involves ahead of time.
4. Decision. The hiring team may need several weeks.

`[Official]` `[L1]` For engineering specifically: an introductory conversation with an engineering recruiter, a technical interview, then interviews with a few LinkedIn engineers and leaders. Recruiters share preparation resources, including interview-prep videos. **No duration is published on these pages.**

`[Unverified]` An official description of an "AI coding" round, its length, its editor, or its task. None of `[L1]`, `[L2]`, or `[L3]` describes one.

`[Reported-Candidate]` 2026 accounts, which disagree:

- `[R-L1]` August 2026, software engineer. A round the candidate calls "AI coding", in CoderPad, with a choice of models including Claude. Task: LRU cache, then TTL, then two further parts the candidate did not finish. The recruiter said not to rely entirely on AI. The interviewer said the candidate had to produce the algorithm; AI was for implementation. Feedback the candidate reports receiving: only two of four tasks completed. This is one person's account of their feedback, not a published scoring rule.
- `[R-L2]` October 2026, Applications teams. Same shape (LRU, four sequential parts, boilerplate provided) but the candidate says they were **not allowed to edit code manually** and had to use AI for every change, including debugging. They report finishing all four and still not being selected.
- `[R-L3]` November 2026, Senior+. A different task (a grid of fire stations and lakes). The candidate says the model could edit the code directly. Senior+ is outside the new-grad scope.

`[Analysis]` The only safe reading is: some candidates in 2026 were told, by a recruiter, that a specific round included AI. The instructions those candidates remember are not the same. Your recruiter's written instructions are the rule for your loop. Do not prepare as if "AI is mandatory and you may not type" and do not prepare as if "AI is banned", until the invitation says which.

### C. AI usage policy

`[Official]` `[L3]`, fetched in full on 24 November 2026:

| Stage | What LinkedIn says |
| --- | --- |
| Resume and cover letter | AI is welcome to draft or refine, if the result accurately reflects real experience, skills, and impact. |
| Research, concepts, mock interviews | Encouraged. AI does not replace your own insights. |
| Live interviews | "Please do not use AI during live interviews unless the recruiting team has explicitly shared in advance that AI is part of the interview format for that role." If it is permitted, the recruiter "will clearly communicate what's allowed and how it will be assessed." |
| Technical and coding assessments | "Please only use AI tools for coding or specialized assessments if your interviewer or interview module explicitly indicates the use of AI is permitted." |
| After you submit | Be ready for follow-up questions on thinking, trade-offs, and experience. |
| If the rule is unclear | "Ask your recruiter." |

The page does **not** name Cursor, Claude, ChatGPT, or GitHub Copilot. It does **not** say that prompts are recorded or scored. `[Unverified]` Any claim that LinkedIn reviews your prompt transcript. `[Official-Platform]` `[H1]` HackerRank can store an AI-assistant transcript in the interview report, and CoderPad documents an AI Assist panel, but neither page says LinkedIn has turned that on.

`[Analysis]` For a new grad in India, the default from the official page is: no AI in a live interview and no AI in a coding assessment, unless the recruiter or the assessment screen says otherwise. Permission for one round does not carry to the next.

### D. What LinkedIn says it values

From `[L1]` and `[L3]`, not from candidate blogs:

- Communication and the ability to explain trade-offs.
- Coding and craftsmanship. "Craftsmanship" is LinkedIn's word; the page does not define it further.
- Engineering design and architecture.
- Leadership, which for a new grad means how you work with other people, not people management.
- Authenticity. Materials and answers should be yours.
- Judgment about when AI is in bounds.

### Category A, kept separate

LinkedIn also builds AI that **employers** use. That is not permission for you to use AI, and it is not a statement that LinkedIn's own SWE loop is graded by a model.

- `[Official]` `[L4]` "AI interview" is a LinkedIn product. A hirer can invite applicants to an audio or video screening call with an AI interviewer. Questions are drafted by AI and edited by the hirer. Hirers receive the recording, transcript, an AI summary, and a 5-point rating (average of per-answer ratings for match to an ideal answer, supporting detail, and clarity). The hirer must review the AI output. Declining the AI interview does not automatically disqualify you. This article describes hirers using LinkedIn. It does not say LinkedIn employees are hired this way.
- `[Official]` `[L5]` `[L6]` Hiring Assistant is a recruiter agent: sourcing, qualification summaries, and a screening agent that can draft questions and summarise a conversation. The recruiter stays in the loop and is responsible for checking the output. October 2025 engineering post.

### Question to send a LinkedIn recruiter

> For each round in my loop, is AI assistance permitted? If yes, which tool, may I use anything outside that tool, will my prompts be reviewed, and what will you be assessing about how I use it?

---

## Amazon

### A. Purpose

Two official descriptions exist. They are not the same assessment.

`[Official]` `[A2]` The university and recent-graduate SDE page says interviews look for technical proficiency and behavioural skills tied to the mission of being Earth's most customer-centric company. The online assessment (OA) evaluates coding skills, technical problem solving, and Amazon's Leadership Principles. No Amazon-specific knowledge is required.

`[Official]` `[A1]` On 22 January 2026 Amazon's Director of Talent Acquisition Science wrote that SDE work now includes generative AI (Amazon Q, Cline, and Kiro) for writing, documenting, debugging, refactoring, and testing. Amazon has "reimagined our technical assessments" so candidates "work with an interactive AI assistant on a real coding platform" and still "demonstrate their distinct skills." The post says 87% of candidates reported that the coding questions related to the role. It does not say this replaced the university OA, and it does not give a duration, a platform name, or a country list.

`[Analysis]` Amazon is trying to measure building skill in an environment closer to how its SDEs work, on the assessment described in `[A1]`. The university page `[A2]` is still written as a test of your own coding and of Leadership Principles. Which one you sit is decided by the email you receive, not by this summary.

### B. Assessment process

#### What the university page says (intern and new grad)

`[Official]` `[A2]`, fetched 24 November 2026. Scope: current university students and recent graduates, full-time and internship SDE roles. "Depending on the country the role is in, the OA will be in one or two parts. Check your OA email." That sentence is the India-relevant official fact: structure can vary by country, and the email is the authority. The page does not say which structure India uses.

Set aside up to two hours. After each section you get an email saying whether you continue.

Full-time SDE OA components and average times published on the page:

| Component | Average time |
| --- | --- |
| Coding assessment | 70 minutes |
| Workstyles assessment | 15 minutes |
| Work simulation | 60 minutes |
| Feedback survey | 5 minutes |

Internship OA: about 90 minutes total. Coding 70 minutes, Workstyles 15 minutes, feedback survey 5 minutes. The internship list on this page does **not** include the work simulation.

Coding rules on this page:

- Public online resources are allowed, for example the Java JDK or the C++ Standard Template Library.
- Do not use sites that require a login, or private repositories.
- "Your browser usage is logged."
- Do not use print screen. The session is terminated and you are locked out.
- "Avoid copying and pasting in the assessment. We expect this to be your own code."
- A practice test exists and is not scored.
- Laptop or desktop. Mobile is discouraged.
- The feedback survey is required. Skipping it delays results.

The page mentions a webcam FAQ and, for North America only, an identification FAQ. The FAQ answers themselves did not expand in the fetch, so this file does not claim that India requires a webcam or ID. `[Unverified]` for India specifically.

If you pass, "Amazon will reach out directly." `[Unverified in this pass]` The number of later rounds, whether there is a Bar Raiser, and the loop length. The loop page was not re-fetched on 24 November 2026. Ask the recruiter. Do not memorise a third-party "five rounds" diagram as if it were on amazon.jobs.

#### What the SDE II page says (not your level, included so you do not mix them up)

`[Official]` `[A3]` SDE II OA: coding challenge of 90 minutes for two questions, about 15 minutes of system design, about 10 minutes of work styles. Seven days to complete. Notified within two days. The page tells candidates to get comfortable in HackerRank and to write real code, not pseudocode. This is an experienced-hire page.

#### What HackerRank's Amazon guide says (platform, when that challenge is yours)

`[Official-Platform]` `[A4]`, HackerRank candidate article "Preparing for your Amazon OA", last updated about August 2026:

- The challenge has a single-file coding question and a multi-file Code Repository question. You pick a framework for the repository before the test starts and cannot switch. You finish coding first; you cannot go back after you enter the repository section.
- GenAI on the single-file coding question: **not permitted**.
- Code Repository: an embedded AI Assistant, only if the test setter enabled it.
- The assistant can explain files, help you find where to change code, explain errors, and suggest syntax. "The AI Assistant does not generate full working solutions." Using it is optional. "You will not be penalized for using the assistant."
- "Does my evaluator see what I type in the AI Assistant? Yes. The platform records your conversation with the AI Assistant and makes the transcript visible to your evaluator. Interactions with the AI Assistant are not considered in your score."

`[Analysis]` That last pair of sentences is easy to misuse. The transcript can be seen. HackerRank says the interaction is not part of the score. You should still assume a human can read it, and you should not assume Amazon has published the same "not scored" sentence. Amazon's own pages `[A1]` and `[A2]` do not say this.

#### What candidates report about the newer OA

`[Reported-Candidate]` `[R-A1]` Nyrion, updated 19 November 2026, says it read 31 threads from February to October 2026 and summarises a roughly 100-minute section (algorithm plus a repository with failing tests) and an assistant that explains code but usually will not edit files. Nyrion also says not every packet had this format, including some EU intern candidates in July and August 2026 who still got classic questions. **This project did not re-read those threads.** Use this only as a reason to read your invitation carefully. Do not treat "six tests" or "the assistant refuses to edit" as Amazon policy.

### C. AI usage policy

| Stage | Source | Rule |
| --- | --- | --- |
| University / new-grad coding OA, as written on `[A2]` | Official | Public documentation yes. Login sites and private repos no. Browser usage logged. Your own code expected. The page does not mention an AI assistant. |
| Reimagined technical assessment in the 22 Jan 2026 post `[A1]` | Official | An interactive AI assistant on a real coding platform, inside that assessment. The post does not authorise Cursor, Claude, ChatGPT, or Copilot on your own machine. |
| HackerRank Amazon Coding Challenge, when that is the test `[A4]` | Official-Platform | No GenAI on the single-file question. Embedded assistant on the repository question if enabled. Transcript visible to the evaluator. |
| Interviews | Reported-Press `[A5]` | Business Insider, 27 February 2025, quotes internal recruiter guidelines: "please do not use GenAl tools during your interview unless explicitly permitted." "Failure to adhere to these guidelines may result in disqualification from the recruitment process." An Amazon spokesperson told BI that, when applicable, candidates must acknowledge they will not use "unauthorized tools, like GenAI." The same article says candidates may talk about how they used generative AI to gain efficiency in a job. BI also reports internal "signs" recruiters were given (typing during a question, reading answers, eyes tracking text). Those signs are from the guidelines BI says it obtained. They are not published on amazon.jobs. |
| Your own Cursor / Claude / Copilot during an Amazon interview or OA | Unverified as permitted | No official page retrieved here allows them. `[Analysis]` Absence of a ban on amazon.jobs is not permission. `[A5]` is the press account of a ban unless you are explicitly permitted. `[A1]` permits an assistant Amazon puts in the assessment, not a tool you bring. |

`[Analysis]` The January 2026 assessment and the February 2025 interview guideline are not in conflict once you separate the stages. Amazon can put an assistant inside one test and still tell candidates not to use generative AI in interviews unless that interview explicitly allows it. Do not carry permission from the OA into the loop.

### D. What Amazon says it values

- `[A2]` Coding skill, technical problem solving, Leadership Principles. The OA page does not list the principles by name.
- `[A1]` The ability to do the kind of problem-solving its developers do with an assistant available, while still showing skills that are yours. The post names fairness, security, and transparency about when the candidate is interacting with AI.
- `[A5]`, as reported | Authentic skills in the interview. Talking about past use of AI is described as allowed. Using it live, unless permitted, is described as grounds for disqualification.

### Category A, kept separate

`[Official]` `[A1]`:

- A **pilot** adds recording and real-time transcription to Amazon's interview system so interviewers can stop splitting attention between notes and the conversation. Explicit consent is required before recording. Amazon says it explains what is recorded, how recordings are used, and how long they are kept. 83% of candidates in the pilot reported more engaging conversations. The post says the tool should reach more candidates in 2026. This is note-taking assistance for human interviewers. It is not an AI interviewer, and it is not a claim that your coding session is recorded.
- Machine learning recommends other roles and evaluates fit during initial screening. When this matching is used, candidates who reach the interview stage are "24% more likely to receive a positive outcome after their initial interview loop" than those evaluated without it. The post does not say a model auto-rejects applicants, and it does not publish the features of the model.

### Question to send an Amazon recruiter

> Which OA will I receive, the version on the university prep page or the version with an interactive AI assistant? If an assistant is included, is it only the one inside the test? For the interview loop, are any generative AI tools permitted, and do I need to acknowledge a no-unauthorised-tools statement?

---

## Atlassian

### A. Purpose

`[Official]` `[T1]` The engineering interview handbook, fetched 24 November 2026, says Atlassian does not evaluate language proficiency. It looks for problem-solving, learning agility, and how you think. You choose the language. Clean code matters. Trade-offs such as verbosity versus optimisation matter more than a missing line, which "won't cost you the job."

The same page says the company wants to see how you explore a problem: which questions you ask, how you talk about reliability and cost, who you would partner with, and which technologies you would use. Follow-up questions get harder or easier as you go. That laddering is how they assess learning agility. "If you don't know what to do, say so."

A Hiring Committee, independent of the interviewers, sees interview feedback and CV information and looks at skills, strengths, and behaviours. There is no single "perfect candidate" profile.

`[Official]` `[T2]` The Principal Backend guide adds, for its AI-enabled code-design interview, that the task is the work Atlassian says it does every day: extend or improve an existing repository by adding features, fixing bugs, or refactoring. Deep knowledge of the repository's language is not what is being assessed. You may ask the AI to explain syntax or patterns.

### B. Assessment process

#### Handbook (general engineering; no AI round described)

`[Official]` `[T1]`:

1. Coding, in two parts: Data Structures, and Code Design. Your language. Own IDE, or CodePair if you cannot set one up.
2. Systems design, **60 minutes**. Practical, not theoretical. Many viable solutions. Draw on past experience.
3. Manager interview, usually one-on-one with the hiring manager or a more senior manager. Past projects, collaboration, communication, where you want your career to go.
4. Values interview. Alignment with Atlassian's five values. The interviewer is often **not** from the hiring team (the page gives Sales, HR, or Customer Support as examples). Fairly informal. Mindset and how it guides actions.
5. Interviewers debrief. Hiring Committee decides.

The handbook does not publish durations for the coding, manager, or values sessions. It does not mention HackerRank, an AI assistant, or a graduate-specific loop. `[Unverified]` That every engineering candidate, or every India new grad, goes through all five of these.

#### Principal Backend guide (a different level)

`[Official]` `[T2]`, PDF marked ©2024, CSD-13796_DRD-09/24. Title: Principal Backend Engineer. Atlassian says the guide can be amended and that more specific policies prevail.

| Stage | What the PDF says | Duration in the PDF |
| --- | --- | --- |
| 1 | Coding interview | Each coding interview capped at 60 minutes |
| 2 | Coding interview and system design | System design 60 minutes |
| 3 | Leadership craft interview and values interview | Leadership craft 60 minutes. Values 45 minutes |

Two different coding setups are written down:

- **Data Structures.** Your IDE and your testing framework. Screen share. CodePair if you have no IDE. The PDF does not mention AI here.
- **AI-Enabled Code Design.** "AI-enabled interviews will use a HackerRank IDE equipped with AI coding assistants, with access to an existing code repository." Extend, fix, or refactor. The language is fixed. You are not expected to be an expert in it. Suggested sentence: "I'm not very familiar with this language, but here's how I'll approach this with AI." Screen share via Zoom.

Preparation themes in the PDF: show more than one solution and why you picked one; testing, especially TDD; narrate your thinking; a debugger is welcome.

`[Official]` `[T3]`, frontend P30–P50 guide, search extract only. Coding capped at 60 minutes, own IDE or CodePair, debugger encouraged, TDD recommended, system design 60 minutes. The extract did not mention an AI assistant. Do not assume the frontend guide and the principal guide are the same process.

`[Reported-Candidate]` `[R-T1]` One intern candidate, August 2026, described an online assessment of three coding questions, then an interviewer-present HackerRank repository task with plan and agent mode, then a values conversation. `[Analysis]` This matches the *shape* of the principal guide's AI-enabled setup (HackerRank, repository, AI assistant) but the writer is an intern, and the principal PDF is not an intern policy. One Reddit post does not establish that India new grads get this round.

`[Unverified]` An official Atlassian page that says graduate or India candidates sit the AI-Enabled Code Design interview.

### C. AI usage policy

| Stage | What is actually written |
| --- | --- |
| Handbook coding and system design `[T1]` | No AI rule at all. `[Analysis]` Silence is not permission to open Cursor. |
| Data Structures, principal guide `[T2]` | Own IDE, screen share. AI is not mentioned. |
| AI-Enabled Code Design, principal guide `[T2]` | The assistant inside the HackerRank IDE for that interview. The guide says you can ask it to explain syntax or patterns. It does not say you may also use Cursor, Claude, or Copilot on a second screen. Screen share means the interviewer can see the session. |
| Values, manager, leadership, system design | No source here permits an AI assistant. |
| Disclosure | The principal guide does not say "disclose that you used AI." It tells you to talk through your approach, including being unfamiliar with the language and using AI to proceed. `[Analysis]` In that round, use of the provided assistant is the format, not a confession. |
| Prompt review | `[T2]` says you screen share. `[Official-Platform]` `[H1]` says HackerRank's interview report can include the full assistant conversation, for interviews where the customer enabled the assistant. `[Analysis]` It is reasonable to behave as if the interviewer can see your prompts, because you are screen sharing. It is not accurate to say Atlassian has published "we score your prompt transcript." |
| If the rule is unclear | The handbook tells you to talk to your Talent Acquisition Partner about adjustments. `[Analysis]` Ask that person whether your round is the AI-enabled one, and whether any tool other than the in-interview assistant is allowed. |

### D. What Atlassian says it values

From `[T1]` and `[T2]`:

- Problem-solving and learning agility, including changing your answer when a new constraint appears.
- How you think, not a perfect compile on the first try.
- Code quality and tests. TDD is named in the role guides.
- Communication. Narrate. Say when you are stuck.
- Trade-offs, reliability, cost, and who you would work with.
- Values. The principal guide uses these as behavioural themes: Play, as a team; Be the change you seek; Don't #@!% the customer; Open company, no bullshit; Build with heart and balance. The handbook says there are five values and does not list the names on the page that was fetched; the names above are from `[T2]`.
- In the AI-enabled code-design setup only: using an assistant to work in an unfamiliar language, while still extending, fixing, or refactoring the repository yourself in the sense that you own the result.

### Category A

`[Unverified]` Any Atlassian page, in this pass, that says Atlassian uses an AI interviewer or an AI grader on engineering candidates. Do not infer one from the fact that an interview *contains* an assistant the candidate uses. That is Category B.

### Question to send an Atlassian recruiter

> Is my coding round the Data Structures setup on my own IDE, the Code Design setup, or the AI-Enabled Code Design setup in HackerRank? If AI is included, is the in-platform assistant the only tool I may use, and will you be watching the session?

---

## What to do when a rule is unclear

This is `[Analysis]`, and it matches the explicit "ask your recruiter" line on `[L3]`.

1. Do not infer permission from a company's internal use of AI, from a blog post about a different level, or from a Reddit thread.
2. Before the round, ask in writing. Keep the reply.
3. If you are already in the session and the tool is sitting there, ask the interviewer before you type a prompt: "Is this assistant part of the assessment, and is it the only one I should use?"
4. If you cannot get an answer, do the work without an assistant. A round you complete yourself is defensible. A round you assisted in secret is the failure mode described in the Amazon press account `[A5]`.
5. When an assistant is explicitly allowed, still narrate, still read the diff, and still be ready for the follow-up. LinkedIn `[L3]`, Atlassian `[T1]`, and Amazon `[A1]` all say, in different words, that the point is what *you* can do.
