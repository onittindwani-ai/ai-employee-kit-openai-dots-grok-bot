# Team recipe 3: Hiring pipeline, from job post to interview day

Four AI employees take a role from your rough notes to interview packs. You make every decision about people.

## Who is on the team

| Order | Employee | File |
| --- | --- | --- |
| 1 | Job Post Writer | [hiring/01](../employees/hiring/01-job-post-writer.md) |
| 2 | CV Screener | [hiring/02](../employees/hiring/02-cv-screener.md) |
| 3 | Candidate Shortlist Ranker | [hiring/03](../employees/hiring/03-candidate-shortlist-ranker.md) |
| 4 | Interview Question Builder | [hiring/04](../employees/hiring/04-interview-question-builder.md) |

Optional fifth: [Interview Scheduler Coordinator](../employees/hiring/05-interview-scheduler-coordinator.md) once you pick who to interview.

## Start with one shared file

Fill in [templates/candidate-scorecard.md](../templates/candidate-scorecard.md) first. All four employees use the same scorecard, which keeps the process fair and the scores comparable.

## How the work flows

```text
Your notes + scorecard --> Job Post Writer --> YOU post the job
                                                    |
                                     CVs arrive in your hiring inbox or ATS
                                                    |
                                CV Screener (scores with quotes, never rejects)
                                                    |
                                Shortlist Ranker (top list, close calls flagged)
                                                    |
                                YOU pick who to interview
                                                    |
                         Interview Question Builder (one pack per candidate)
```

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | You | Job Post Writer | Role notes and the scorecard | Docs folder for the role | You ask for the post |
| 2 | Job Post Writer | You | Job post draft | Docs folder | Draft ready message |
| 3 | CV Screener | Shortlist Ranker | Scores, quotes and labels per candidate ID | Screening sheet | You write "shortlist now" |
| 4 | Shortlist Ranker | You | Ranked short list with close calls | New tab "Shortlist <date>" | Ranker finishes |
| 5 | You | Interview Question Builder | Candidate IDs to interview | Team chat or your dot's conversation | You write "interview <candidate ID>" |

## Run it in Grok Bot

Create the four bots and put them in one group chat:

```text
We run hiring for one role. The scorecard file is the only standard. Use candidate IDs, never names, in this chat.
- CV Screener: after each run, post "Screened <number>: STRONG <n>, MAYBE <n>, WEAK <n>."
- Shortlist Ranker: when I write "shortlist now", build the short list from the screening sheet.
- Interview Question Builder: when I write "interview <candidate ID>", build that candidate's pack.
No one contacts a candidate. No one uses age, gender, photo, nationality, religion, health or family details.
```

## Run it in OpenAI Dots

Add the four prompts as four projects in your dot, then send:

```text
These four projects form one hiring pipeline for one role. The scorecard is the only standard. Use candidate IDs in reports. When I say "shortlist now", run the ranker. When I say "interview <candidate ID>", build the pack. Never contact a candidate.
```

## Fair hiring reminders

- The AI scores, you decide. Read at least the top 10 and a few WEAK CVs yourself.
- Hiring laws differ by country and state, and some places have rules for using automated tools in hiring. Check the rules where you hire before you use an AI screener.
- Tell candidates how you use AI in your process if your local rules require it.
