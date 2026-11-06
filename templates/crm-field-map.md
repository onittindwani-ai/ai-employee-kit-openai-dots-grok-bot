# CRM field map

Used by: [CRM Updater](../employees/sales/07-crm-updater.md), [Lead Enricher and Qualifier](../employees/sales/02-lead-enricher-and-qualifier.md), [Inbox Reply Triager](../employees/sales/05-inbox-reply-triager.md), [Lost Deal Win Back](../employees/sales/09-lost-deal-win-back.md), [Client Onboarding Coordinator](../employees/operations/01-client-onboarding-coordinator.md).

This tells your AI employees exactly which CRM fields exist, what each means, and who may change it. An AI employee may only touch fields marked "AI may update". Everything else is yours.

Works for any CRM (HubSpot, Pipedrive, Attio, Close, Notion, Airtable or a Google Sheet). Use your CRM's real field names in the first column.

## How to fill it in (15 minutes)

1. Open your CRM and list every field you actually use. Ignore the rest.
2. For each field, write what it means in one line, and the allowed values if it is a drop down.
3. Decide who may change it: AI may update, AI may suggest (you decide), or owner only.
4. Write the stage rules: what must be true for a deal to move to each stage.

## Contacts

| Field name in your CRM | What it means | Allowed values | Who may change it |
| --- | --- | --- | --- |
| Email | Main work email | | AI may suggest |
| Job title | Current title | | AI may update |
| Last contact date | Last email or call either way | A date | AI may update |
| Lead score | Fit score from the ICP sheet | 1 to 10 | AI may update |
| Lead status | Where they are in outreach | empty score, scored, draft ready, sent, replied, closed | AI may update (except closed) |
| Do not contact | They asked not to be contacted | yes or no | AI may set to yes, owner only to set back to no |
| | | | |

## Deals

| Field name in your CRM | What it means | Allowed values | Who may change it |
| --- | --- | --- | --- |
| Stage | Deal stage | Contacted, Meeting booked, Proposal sent, Won, Lost | AI may update up to Proposal sent; Won and Lost owner only |
| Next step | The next agreed action and date | Free text | AI may update |
| Deal value | Expected value | A number | Owner only |
| Lost reason | Why it was lost | Timing, Budget, Went quiet, Chose another provider, Not a fit | Owner only |
| Notes | Short dated notes | Free text, add only, never delete | AI may update (add only) |
| | | | |

## Stage rules

| Move to | Only when |
| --- | --- |
| Meeting booked | An email or calendar invite confirms a date |
| Proposal sent | You sent the proposal (the AI only drafts it) |
| Won | Owner only, after a signed agreement or payment |
| Lost | Owner only |

## Never stored in the CRM by an AI employee

Passwords, one time codes, API keys, bank or card details, government ID numbers, health details, or anything a contact shared in confidence.
