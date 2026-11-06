# Team recipe 7: From interested reply to proposal on the same day

Four AI employees move a warm lead from "yes, tell me more" to a proposal draft, with you leading every conversation.

## Who is on the team

| Order | Employee | File |
| --- | --- | --- |
| 1 | Inbox Reply Triager | [sales/05](../employees/sales/05-inbox-reply-triager.md) |
| 2 | Meeting Prep Brief | [sales/06](../employees/sales/06-meeting-prep-brief.md) |
| 3 | CRM Updater | [sales/07](../employees/sales/07-crm-updater.md) |
| 4 | Proposal First Draft | [sales/08](../employees/sales/08-proposal-first-draft.md) |

## How the work flows

```text
Reply labelled INTERESTED --> draft reply --> YOU send, call booked
        |
Meeting Prep Brief (1 hour before the call) --> YOU take the call
        |
CRM Updater (after the call, from your notes) --> stage and next step
        |
Proposal First Draft (same day) --> YOU fill prices and terms, then send
```

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | Inbox Reply Triager | You | INTERESTED reply with a draft answer | Drafts folder and team chat | Reply arrives |
| 2 | You | Meeting Prep Brief | A booked call on your calendar | Calendar | You book the call |
| 3 | Meeting Prep Brief | You | One page brief | Team chat or your dot's conversation | 1 hour before the call |
| 4 | You | CRM Updater | Your call notes | Notes app | You save the notes |
| 5 | You | Proposal First Draft | "proposal <company>" | Team chat or your dot's conversation | Your message |
| 6 | Proposal First Draft | You | Proposal draft with [YOU FILL IN] fields | Docs folder | Draft ready message |

## Run it in Grok Bot

Create the four bots and a group chat:

```text
We turn interested replies into proposals.
- Reply Triager: post every INTERESTED reply here with the company name.
- Meeting Prep: when a call with that company is on my calendar, post the brief here 1 hour before.
- CRM Updater: after the call, update the deal from my notes and post the changes.
- Proposal Drafter: when I write "proposal <company>", draft it from the call notes.
Never send anything. Never write prices, discounts or legal terms.
```

## Run it in OpenAI Dots

Add the four prompts as projects in your dot, then send:

```text
These four projects take an interested reply to a proposal draft. When a reply is INTERESTED, watch my calendar for the call, prepare the brief 1 hour before, update the CRM after I add call notes, and when I say "proposal <company>", draft it. Never send anything. Never write prices or legal terms.
```

## The one rule that matters

The proposal draft leaves every price and promise as [YOU FILL IN]. Keep it that way.
