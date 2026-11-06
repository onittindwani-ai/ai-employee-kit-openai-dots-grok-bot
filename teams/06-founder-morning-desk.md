# Team recipe 6: Founder morning desk

Four AI employees work overnight and early morning so your day starts with one screen: replies sorted, invoices checked, tickets sorted, and a brief that pulls it together.

## Who is on the team

| Employee | When it runs | File |
| --- | --- | --- |
| Inbox Reply Triager | Every 2 hours, last run before 7 AM | [sales/05](../employees/sales/05-inbox-reply-triager.md) |
| Invoice and Payment Reminder Drafts | Tuesday and Friday at 6 AM (moved earlier for this recipe) | [operations/05](../employees/operations/05-invoice-and-payment-reminder-drafts.md) |
| Support Ticket Triager | Every 30 minutes | [operations/07](../employees/operations/07-support-ticket-triager.md) |
| Daily Founder Brief | Every weekday at 7:30 AM | [operations/08](../employees/operations/08-daily-founder-brief.md) |

## How the work flows

```text
Inbox Reply Triager ----\
Invoice Reminders -------+--> their reports --> Daily Founder Brief (7:30 AM) --> YOU
Support Ticket Triager --/
```

The brief reads the latest report from the other three, so you read one message instead of four.

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | Inbox Reply Triager | Daily Founder Brief | Sorted replies and drafts | Team chat or its project report | Last run before 7 AM |
| 2 | Invoice Reminders | Daily Founder Brief | Due, overdue and NEEDS ME invoices | Team chat or its project report | 6 AM run on Tuesday and Friday |
| 3 | Support Ticket Triager | Daily Founder Brief | URGENT, drafts and NEEDS ME tickets | Team chat or its project report | Every 30 minutes |
| 4 | Daily Founder Brief | You | One screen brief | ChatGPT, Slack or team chat | 7:30 AM |

## Run it in Grok Bot

Create the four bots and a group chat:

```text
This is my morning desk. Reply Triager, Invoice Reminders and Ticket Triager: post your latest report here before 7:15 AM.
Founder Brief: at 7:30 AM, read those reports plus my calendar and CRM, and post my brief, with everything waiting on me at the top.
No one sends, pays, closes or deletes anything.
```

## Run it in OpenAI Dots

This recipe fits Dots well, because the brief lives in your business apps and runs on a schedule. Add the four prompts as projects, then send:

```text
These four projects are my morning desk. The Daily Founder Brief at 7:30 AM should include the latest results from the Reply Triager, Invoice Reminders and Ticket Triager projects. Put everything waiting on me at the top. Send it to me in ChatGPT and in Slack.
```

## Make it better each week

At the end of each week, tell the Brief one thing it should have flagged and one thing it can drop.
