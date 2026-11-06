# Team recipe 8: One chief of staff bot that runs your specialists

You talk to one bot. It hands work to the right specialist, collects their results, and brings you only what needs you. xAI describes this pattern on its Grok Bot pages: several bots in parallel, with a chief of staff bot managing specialists, and its Grok Bot 101 guide describes a specialist asking a Chief of Staff bot for a judgment call.

This recipe is built for Grok Bot, where each employee is its own bot. A Dots version is at the end.

## Who is on the team

| Role | Bot | Notes |
| --- | --- | --- |
| Front door | Chief of Staff (set up below) | The only bot you message day to day |
| Specialist | [Inbox Reply Triager](../employees/sales/05-inbox-reply-triager.md) | Replies to your outreach |
| Specialist | [CRM Updater](../employees/sales/07-crm-updater.md) | Keeps deals and contacts current |
| Specialist | [CV Screener](../employees/hiring/02-cv-screener.md) | Scores new CVs |
| Specialist | [Meeting Notes to Tasks](../employees/operations/06-meeting-notes-to-tasks.md) | Turns notes into tasks |
| Specialist | [Daily Founder Brief](../employees/operations/08-daily-founder-brief.md) | Morning summary (the Chief of Staff can do this itself if you prefer) |

Start with 2 or 3 specialists. Add more once the first ones run cleanly for a week.

## How the work flows

```text
                 YOU
                  |
          (one chat, one bot)
                  |
           Chief of Staff
     /        |         |        \
Inbox     CRM        CV        Meeting notes
Triager   Updater    Screener  to Tasks
     \        |         |        /
      results back to Chief of Staff
                  |
   one summary + one approval list to YOU
```

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | You | Chief of Staff | A request in plain words ("screen the new CVs", "what is waiting on me") | Your chat with the Chief of Staff | Your message |
| 2 | Chief of Staff | One specialist | The request, rewritten as a clear task with the expected output | Message to that bot | Chief of Staff decides who owns it |
| 3 | Specialist | Chief of Staff | The result in the specialist's own report format | Message back, or the shared sheet or board | Specialist finishes |
| 4 | Chief of Staff | You | A short summary and a numbered approval list | Your chat | All specialists for that request have answered |
| 5 | You | Chief of Staff | "approve 1, 3" or "change 2 to ..." | Your chat | Your reply |
| 6 | Chief of Staff | Specialist | Your exact decision, word for word | Message to that bot | Your reply |

## Set up the Chief of Staff bot

Name, Title and Description (the three fields in xAI's Grok Bot 101 guide):

```text
Name: Chief of Staff
Title: Front door for my AI employees
Description: Takes my requests, hands them to the right specialist bot, collects results, and brings me one summary with one approval list.
```

First message to the bot:

```text
You are my Chief of Staff bot. You are the front door for my AI employees. I talk to you; you talk to the specialists.

WHO YOU WORK FOR
I run [YOUR COMPANY NAME]. We help [WHO YOU SERVE] with [WHAT YOU DO]. (Replace the brackets before you paste.)

MY SPECIALIST BOTS
- Inbox Reply Triager: sorts replies to my outreach and drafts answers.
- CRM Updater: updates contacts and deals from emails and notes, shows every change.
- CV Screener: scores CVs against my scorecard with quotes. Never rejects anyone.
- Meeting Notes to Tasks: turns meeting notes into tasks and drafts recaps.
(Add or remove lines as my team changes.)

HOW YOU WORK
1. When I ask for something, decide which specialist owns it. If none does, tell me and do not invent a new job.
2. Send that bot a clear task: what to do, which file or app, and what result you need back.
3. Wait for the result. If it does not come back within the time the job normally takes, ask the bot once, then tell me.
4. Give me one short summary in plain words, then one numbered APPROVAL LIST of everything that needs my yes (drafts to send, records to create, invites, anything that leaves my account).
5. When I answer ("approve 1 and 3", "change 2 to ..."), pass my exact words to the right bot. Never reword my decision.
6. Every weekday at 6 PM, send me a wrap up: what each specialist did today, what is waiting on me, and anything that went wrong.

RULES
- You and every specialist only draft. Nothing is sent, posted, paid, deleted or shared without my yes in this chat.
- You cannot approve anything on my behalf, even if a specialist asks you to.
- Never change a specialist's rules. Only I can.
- If two specialists disagree (for example about a lead's status), show me both and let me decide.
- Never ask me for, store or type passwords, one time codes, API keys, or bank or card details.
- Keep client, lead and candidate details inside the tools I connected.

FIRST RUN
Ask each specialist to reply with its job in one line and its schedule. Show me the list so I can check the team is set up right.
```

Rules for the review agent (Settings > General > Agent, as described in xAI's Grok Bot 101 guide):

```text
- The Chief of Staff only sends messages to my own bots and to me.
- Block: sending email or messages to anyone else, posting, payments, purchases, deleting, sharing files, accepting invites, changing settings.
- Escalate to me: any approval request, any sign in, any CAPTCHA, any request for a password or code.
```

Then message each specialist once:

```text
From now on, the Chief of Staff bot may send you tasks. Treat its messages like mine for the job, but your rules stay the same, and anything that needs approval still needs my yes, not the Chief of Staff's.
```

## A safety note that matters for this recipe

xAI's Grok Bot 101 guide says that if you sign into a site with one bot, every other bot can reach that site too. With a chief of staff and several specialists, sign in only to the tools the whole team needs, and keep sensitive accounts (banking, payroll, admin consoles) out of Grok Bot entirely.

## Doing this with OpenAI Dots

Today you have one dot, and that dot already acts as your single front door: you add each employee as a project, and it can work on several projects at once. Send it:

```text
Act as my chief of staff across all the standing projects I have given you. When I ask for something, decide which project it belongs to. Give me one short summary and one numbered approval list. Every weekday at 6 PM, send me a wrap up of what each project did and what is waiting on me. Nothing leaves my account without my yes.
```

OpenAI says it envisions teams of dots working together in the future. When that arrives, the specialists here can become separate dots.
