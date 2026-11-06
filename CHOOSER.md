# Which tool for which job

This guide helps you pick OpenAI Dots or Grok Bot for each of the 25 AI employees, and tells you when building your own system in Claude Code is still the better choice.

Every reason here comes from the official pages listed in [SOURCES.md](SOURCES.md), read on 2026-11-06. Features and plans change often, so check the official pages before you decide. This guide does not compare prices or speed, because neither company publishes numbers we could check side by side.

## The short version

| If your job mostly... | Pick | Why (from the official pages) |
| --- | --- | --- |
| Lives inside your business apps (email, calendar, CRM, docs, Slack or Teams) | OpenAI Dots | Dots can connect to over 4,000 apps through OpenAI's plugins, and you can talk to your dot in ChatGPT, Slack and Teams. |
| Runs on a schedule and reports back (daily brief, weekly report, reminders) | OpenAI Dots | Your dot can run reminders and recurring checks as scheduled tasks. |
| Needs fine control over what it may do alone | OpenAI Dots | Custom Rules let you choose, per action: take action without asking, take action if pre approved, ask before taking action, or hand off to you. |
| Needs websites that have no clean API (for example browsing LinkedIn profiles) | Grok Bot | xAI says bots sign in and work across apps, tools and websites, including platforms with no clean API or MCP. |
| Needs several employees working at the same time and passing work to each other | Grok Bot | xAI says bots work in parallel, message each other, share context in threads, and can coordinate in a group chat. |
| Is easier to show than to explain | Grok Bot | xAI says you can ask a bot to follow along while you do a job, and it saves your workflow as a routine. |
| Should react to events (a new Slack thread, a GitHub PR) | Grok Bot | xAI's Grok Bot 101 guide says a bot can set its own schedule or listen for events from other apps. |
| Needs to be fully custom, tested and owned by you | Claude Code | See "When Claude Code is still the better choice" below. |

## One important difference: one dot, or many bots

- **OpenAI Dots:** OpenAI's announcement says you start today with your primary dot, that a dot can take a project and run with it while working on several others, and that you will be able to add more dots in the future. It describes teams of dots working together as something it envisions, not something available today. (The help center also says each member of an Enterprise workspace can create one personal dot.) So with Dots, you run all your AI employees as separate projects inside your one dot.
- **Grok Bot:** you create a separate bot for each job. Bots can talk to each other and work in a group chat, so a team of AI employees maps directly to a team of bots.

This is why every recipe in [teams/](teams/) runs best in Grok Bot when you want the employees truly side by side, and why each recipe also shows how to run it as projects inside one dot.

## All 25 employees

"Either" means both tools fit the job well. Pick the one you already pay for and use every day.

| Group | Employee | Best tool | Why |
| --- | --- | --- | --- |
| Sales | [LinkedIn Lead Finder](employees/sales/01-linkedin-lead-finder.md) | Grok Bot | Grok Bot can sign in and work across apps and websites, including sites with no clean API or MCP. You can ask a Grok Bot to follow along the next time you do the job, and it saves your steps as a routine. |
| Sales | [Lead Enricher and Qualifier](employees/sales/02-lead-enricher-and-qualifier.md) | Either | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Grok Bot can sign in and work across apps and websites, including sites with no clean API or MCP. |
| Sales | [Cold Email First Drafts](employees/sales/03-cold-email-first-drafts.md) | OpenAI Dots | You can connect your personal email to your dot, and its background research uses read only tools that cannot send messages. Dots have Custom Rules where you pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. |
| Sales | [Follow Up Writer](employees/sales/04-follow-up-writer.md) | OpenAI Dots | Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. You can connect your personal email to your dot, and its background research uses read only tools that cannot send messages. |
| Sales | [Inbox Reply Triager](employees/sales/05-inbox-reply-triager.md) | OpenAI Dots | You can connect your personal email to your dot, and its background research uses read only tools that cannot send messages. Dots have Custom Rules where you pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. |
| Sales | [Meeting Prep Brief](employees/sales/06-meeting-prep-brief.md) | OpenAI Dots | Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. |
| Sales | [CRM Updater](employees/sales/07-crm-updater.md) | Either | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Grok Bot lets you run several bots at the same time, and they can message each other and share context. |
| Sales | [Proposal First Draft](employees/sales/08-proposal-first-draft.md) | OpenAI Dots | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Dots have Custom Rules where you pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. |
| Sales | [Lost Deal Win Back](employees/sales/09-lost-deal-win-back.md) | Either | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Grok Bot can sign in and work across apps and websites, including sites with no clean API or MCP. |
| Hiring | [Job Post Writer](employees/hiring/01-job-post-writer.md) | OpenAI Dots | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. You can message your dot in ChatGPT, Slack and Teams, and it keeps the same context in every place. |
| Hiring | [CV Screener](employees/hiring/02-cv-screener.md) | Either | Grok Bot lets you run several bots at the same time, and they can message each other and share context. Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. |
| Hiring | [Candidate Shortlist Ranker](employees/hiring/03-candidate-shortlist-ranker.md) | Either | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Grok Bot lets you run several bots at the same time, and they can message each other and share context. |
| Hiring | [Interview Question Builder](employees/hiring/04-interview-question-builder.md) | OpenAI Dots | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. |
| Hiring | [Interview Scheduler Coordinator](employees/hiring/05-interview-scheduler-coordinator.md) | OpenAI Dots | Dots have Custom Rules where you pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. |
| Hiring | [Reference Check Drafts](employees/hiring/06-reference-check-drafts.md) | OpenAI Dots | You can connect your personal email to your dot, and its background research uses read only tools that cannot send messages. Dots have Custom Rules where you pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. |
| Hiring | [Offer Letter Draft](employees/hiring/07-offer-letter-draft.md) | OpenAI Dots | Dots have Custom Rules where you pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. |
| Hiring | [New Hire Onboarding Checklist](employees/hiring/08-new-hire-onboarding-checklist.md) | OpenAI Dots | Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. You can message your dot in ChatGPT, Slack and Teams, and it keeps the same context in every place. |
| Operations | [Client Onboarding Coordinator](employees/operations/01-client-onboarding-coordinator.md) | OpenAI Dots | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. |
| Operations | [Weekly Client Report Builder](employees/operations/02-weekly-client-report-builder.md) | OpenAI Dots | Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. |
| Operations | [Marketing Post Drafter](employees/operations/03-marketing-post-drafter.md) | OpenAI Dots | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. You can message your dot in ChatGPT, Slack and Teams, and it keeps the same context in every place. |
| Operations | [Content Calendar Keeper](employees/operations/04-content-calendar-keeper.md) | Either | Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. A Grok Bot can set its own schedule or listen for events, like a Slack thread or a GitHub PR. |
| Operations | [Invoice and Payment Reminder Drafts](employees/operations/05-invoice-and-payment-reminder-drafts.md) | OpenAI Dots | Dots have Custom Rules where you pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. |
| Operations | [Meeting Notes to Tasks](employees/operations/06-meeting-notes-to-tasks.md) | Either | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. A Grok Bot can set its own schedule or listen for events, like a Slack thread or a GitHub PR. |
| Operations | [Support Ticket Triager](employees/operations/07-support-ticket-triager.md) | Grok Bot | A Grok Bot can set its own schedule or listen for events, like a Slack thread or a GitHub PR. Grok Bot can sign in and work across apps and websites, including sites with no clean API or MCP. |
| Operations | [Daily Founder Brief](employees/operations/08-daily-founder-brief.md) | OpenAI Dots | Dots can connect to over 4,000 apps through OpenAI's plugins, so it can reach the business tools this job lives in. Your dot can run reminders and recurring checks as scheduled tasks, and the results show up in the conversation. |

## How to decide when it says "Either"

1. Where does the data live? Mostly in connected business apps: lean to Dots. Mostly on websites without a clean API: lean to Grok Bot.
2. Does this job hand work to another employee? If yes and you want them to run at the same time, lean to Grok Bot.
3. Which one does your team already use? A tool you open every day beats a slightly better fit you forget about.
4. Try it for one week on real but low risk work, and use the "How to check its work in 2 minutes" list in each employee file every day.

## When Claude Code is still the better choice

Dots and Grok Bot give you ready, always on employees. That is the fastest way to start. A custom system you build with a coding tool such as Claude Code is a different trade, and it is still the better choice in some cases:

- **You need full control of the logic.** In a custom build, every rule is code you can read, change and test. In Dots and Grok Bot, rules are written in plain language and checked by the vendor's review system. xAI says it plainly: you are trusting the model to follow what you wrote.
- **You need repeatable, tested results.** A custom build can have tests that run on every change, so the same input gives a result you have checked. That matters for scoring, routing and anything a client pays you to get right every time.
- **You sell the system to clients.** If the system is your product, you usually want to own the code, run it where your client needs it, and keep it in your own repository.
- **Your data has strict rules.** Some client contracts or regulations decide where data may go. A custom build lets you choose where it runs and which services see the data. Check each vendor's own terms before you put client data in a hosted agent.
- **The job is narrow and runs at high volume.** A focused script often costs less to run and is easier to check than a general agent.

And the fair other side:

- Building and maintaining a custom system takes real time and skill. Dots and Grok Bot take minutes to start.
- Ready agents come with their own cloud computer, browser, scheduling, approvals and phone access out of the box. In a custom build you set all of that up yourself.
- For many founder and agency jobs (drafting, sorting, research, reports) a ready employee with good rules is enough.

A sensible path: start with a ready employee from this kit, run it for a few weeks, and only build a custom version of the jobs that become important, repeatable and worth testing.
