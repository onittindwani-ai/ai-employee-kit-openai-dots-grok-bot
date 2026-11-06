# Team recipe 4: Client delivery week

Three AI employees keep client work moving: onboarding new clients, turning meetings into tasks, and building the Friday report. They run in parallel and meet in your weekly report.

## Who is on the team

| Employee | When it runs | File |
| --- | --- | --- |
| Client Onboarding Coordinator | When a deal is Won, then daily until kickoff | [operations/01](../employees/operations/01-client-onboarding-coordinator.md) |
| Meeting Notes to Tasks | After every client meeting | [operations/06](../employees/operations/06-meeting-notes-to-tasks.md) |
| Weekly Client Report Builder | Every Friday at 10 AM | [operations/02](../employees/operations/02-weekly-client-report-builder.md) |

## How the work flows

```text
Deal Won --> Onboarding Coordinator --> client folder + task list --> YOU approve the welcome email
Client meeting --> Meeting Notes to Tasks --> tasks on the client board --> YOU approve the recap
Friday --> Report Builder reads the numbers + the client board --> draft report --> YOU review and send
```

Hand offs:

1. The Onboarding Coordinator creates the client board.
2. Meeting Notes to Tasks adds tasks to that same board.
3. The Report Builder reads the board (done and open tasks) for the "next week's plan" part of the report.

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | CRM (deal marked Won) | Onboarding Coordinator | Client name, contact, start date | CRM | Deal stage changes to Won |
| 2 | Onboarding Coordinator | Meeting Notes to Tasks | The client board | Project tool | "Board ready for <client>" message |
| 3 | Meeting Notes to Tasks | Report Builder | Done and open tasks | The client board | Friday 10 AM run |
| 4 | Report Builder | You | Draft report with CHECK flags | Docs or Slides folder | Report ready message |

## Run it in Grok Bot

Create the three bots. Grok Bot 101 says bots can listen for events from other apps, so set Meeting Notes to Tasks to trigger when new notes appear. Group chat message:

```text
We deliver for clients. Each client has one board in the project tool.
- Onboarding Coordinator: create the board when a deal is Won and post "Board ready for <client>".
- Meeting Notes to Tasks: add tasks only to the matching client's board.
- Report Builder: on Friday, read each client's board for the plan section.
No email, message or report goes to a client without my yes.
```

## Run it in OpenAI Dots

Add the three prompts as three projects in your dot, then send:

```text
These three projects deliver for my clients. Each client has one board. Onboarding creates it, Meeting Notes to Tasks adds to it, and the Friday report reads it. Nothing goes to a client without my yes. Every Friday after the reports are ready, tell me which clients have late tasks.
```

## Your Friday 10 minutes

- Read each report's CHECK flags first.
- Check two numbers per report against the source tool.
- Send the reports yourself.
