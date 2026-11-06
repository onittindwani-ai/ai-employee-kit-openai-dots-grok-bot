# Team recipe 5: Content engine

Two AI employees turn your raw ideas into a full, balanced content calendar. You approve every post and post it yourself.

## Who is on the team

| Employee | Job | File |
| --- | --- | --- |
| Marketing Post Drafter | Turns your ideas and wins into drafts in your voice | [operations/03](../employees/operations/03-marketing-post-drafter.md) |
| Content Calendar Keeper | Fills empty slots, keeps the topic mix, flags what needs you | [operations/04](../employees/operations/04-content-calendar-keeper.md) |

## How the work flows

```text
You drop raw ideas (voice notes, call learnings, wins)
        |
Marketing Post Drafter (Monday 8 AM) --> drafts doc
        |
Content Calendar Keeper (Monday 9 AM) --> fills the next 2 weeks --> NEEDS ME list
        |
YOU edit, approve and post
```

The one hour gap matters: the Drafter finishes before the Keeper starts.

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | You | Post Drafter | Raw ideas | Notes app or ideas channel | You drop an idea any time |
| 2 | Post Drafter | Calendar Keeper | Drafts with their source idea | Drafts doc | "Drafts ready" at about 8:30 AM Monday |
| 3 | Calendar Keeper | You | NEEDS ME list | Calendar and team chat | 9 AM Monday run |
| 4 | You | Calendar Keeper | Status READY after your edit | Calendar | You change the status |

## Run it in Grok Bot

Create both bots and a group chat:

```text
We run my content. The drafts doc is how you pass work.
- Post Drafter: when drafts are ready, post "Drafts ready: <number>".
- Calendar Keeper: after that message, fill the calendar and post the NEEDS ME list.
No one posts, schedules or publishes anything. No client names or numbers without my written permission note.
```

## Run it in OpenAI Dots

Add both prompts as projects in your dot, then send:

```text
These two projects run my content. The Post Drafter fills the drafts doc on Monday at 8 AM. The Calendar Keeper uses it at 9 AM. Never post or schedule anything. On Monday at 9:30 AM, send me one message with the NEEDS ME list.
```

## Keep it honest

- Every number in a post should come from a note you wrote. Ask the Drafter for the source of any number you do not recognise.
- Never post a client result without the client's permission.
