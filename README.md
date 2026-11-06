# AI Employee Kit for OpenAI Dots and Grok Bot

25 ready AI employees for sales, hiring and operations, with the exact setup prompts for both OpenAI Dots and Grok Bot, and a guide on which one to use for each job.

OpenAI Dots and Grok Bot are always on AI agents: each one has its own computer in the cloud, works inside the apps you connect, and keeps going after you close the chat. This kit turns them into employees with a clear job, clear rules, and a report you can check in 2 minutes. You do not need to build your own agent system to start.

Made for AI agency owners and founders who want leads found, CVs screened, marketing posts drafted and client operations handled, while they keep every final decision.

## What is inside

| Part | Count | Where |
| --- | --- | --- |
| AI employees, sales | 9 | [employees/sales](employees/sales) |
| AI employees, hiring | 8 | [employees/hiring](employees/hiring) |
| AI employees, operations | 8 | [employees/operations](employees/operations) |
| Setup prompts | 50 (one for Dots and one for Grok Bot per employee) | inside each employee file |
| Team recipes (employees working together, with exact hand offs) | 8 | [teams](teams) |
| Guide on which tool to use for each job | 1 | [CHOOSER.md](CHOOSER.md) |
| Templates (scorecard, ideal customer profile, CRM field map, weekly report) | 4 | [templates](templates) |
| Safety and permissions guide | 1 | [SAFETY-AND-PERMISSIONS.md](SAFETY-AND-PERMISSIONS.md) |
| Sources for every product fact | 1 | [SOURCES.md](SOURCES.md) |

Every employee file has the same parts: the job in one line, what it does for you, the best tool and why, the apps it needs, a full Dots prompt, a full Grok Bot prompt (with review agent rules and a "follow along once" step), its rules and permission points, its report format, a labelled synthetic sample, and a 2 minute check.

## The 25 employees

**Sales:** LinkedIn Lead Finder, Lead Enricher and Qualifier, Cold Email First Drafts, Follow Up Writer, Inbox Reply Triager, Meeting Prep Brief, CRM Updater, Proposal First Draft, Lost Deal Win Back.

**Hiring:** Job Post Writer, CV Screener, Candidate Shortlist Ranker, Interview Question Builder, Interview Scheduler Coordinator, Reference Check Drafts, Offer Letter Draft, New Hire Onboarding Checklist.

**Operations:** Client Onboarding Coordinator, Weekly Client Report Builder, Marketing Post Drafter, Content Calendar Keeper, Invoice and Payment Reminder Drafts, Meeting Notes to Tasks, Support Ticket Triager, Daily Founder Brief.

## Quick start in 3 steps

1. **Pick one employee** from the list above. A good first one is the [Daily Founder Brief](employees/operations/08-daily-founder-brief.md) or the [Inbox Reply Triager](employees/sales/05-inbox-reply-triager.md), because they only read and draft.
2. **Fill in the template it uses** (for example the [ideal customer profile](templates/ideal-customer-profile.md) for sales jobs or the [candidate scorecard](templates/candidate-scorecard.md) for hiring), then paste the employee's prompt into your tool:
   - **OpenAI Dots:** open your dot in ChatGPT and paste the Dots prompt as a new project for it. Today you have one dot, and it can run several projects at once.
   - **Grok Bot:** create a new bot, fill in its Name, Title and Description, paste the first message and the review agent rules, then let it follow along while you do the job once.
3. **Run a small trial and check it.** Every prompt asks for a trial run on 3 items first. Use the employee's "How to check its work in 2 minutes" list, correct it in the chat, then let it start its schedule.

When one employee runs well, join a few into a [team recipe](teams).

## Which tool should I use?

The short answer from [CHOOSER.md](CHOOSER.md):

| If the job mostly... | Pick |
| --- | --- |
| Lives in your business apps (email, calendar, CRM, docs, Slack, Teams) | OpenAI Dots |
| Runs on a schedule and reports back | OpenAI Dots |
| Needs websites with no clean API, like browsing LinkedIn profiles | Grok Bot |
| Needs several employees working at the same time, passing work to each other | Grok Bot |
| Is easier to show once than to explain | Grok Bot |
| Must be fully custom, tested and owned by you | Build it yourself, for example in Claude Code |

Of the 25 employees, the chooser marks 16 for OpenAI Dots, 2 for Grok Bot and 7 as either. Most of these jobs live inside business apps, which is where Dots is strongest; Grok Bot shines when you want many employees running side by side, which is why most team recipes favour it. The full table, with a reason for each, is in [CHOOSER.md](CHOOSER.md).

## Honest limits

- **These are prompts and plans, not software.** The kit does not install anything or connect to your accounts. You set it up in the tools yourself.
- **No results are promised.** We make no claims about speed, accuracy or revenue. Run each employee on a small batch and check its work.
- **Both products are new and change often.** Grok Bot is in beta. Dots are rolling out gradually to eligible plans. Facts in this kit were checked on 2026-11-06 against the official pages in [SOURCES.md](SOURCES.md). Check those pages before you rely on any detail.
- **No prices.** Neither product's price is stated here. Check each company's plan page.
- **Button names may differ.** Where the official pages name a setting, we use that name. Where they do not, we describe the step in plain words.
- **You are responsible for what is sent.** Every employee drafts and asks first, but you approve. Follow the laws and platform rules that apply to you, including email, privacy and hiring laws, and each site's terms (for example LinkedIn's rules on automated activity).
- **Sample outputs are synthetic.** Every name and company in a sample is made up and labelled as an example.

## Check the kit yourself

The kit has a small checker that confirms every file is complete:

```bash
python3 tests/check_kit.py
```

It runs on every push through GitHub Actions.

You can also download the zip from the latest release.

## Licence

MIT. See [LICENSE](LICENSE). Use it, change it, and share it.

OpenAI, ChatGPT and Dots are names of OpenAI. Grok and Grok Bot are names of xAI. This kit is independent and is not made by or endorsed by either company.

Made by Onit Tindwani.
