# Team recipe 2: Outbound pipeline, from lead to first email to follow up

Four AI employees pass work down a line: find, qualify, draft, follow up. You only touch the steps that leave your account.

## Who is on the team

| Order | Employee | File |
| --- | --- | --- |
| 1 | LinkedIn Lead Finder | [sales/01](../employees/sales/01-linkedin-lead-finder.md) |
| 2 | Lead Enricher and Qualifier | [sales/02](../employees/sales/02-lead-enricher-and-qualifier.md) |
| 3 | Cold Email First Drafts | [sales/03](../employees/sales/03-cold-email-first-drafts.md) |
| 4 | Follow Up Writer | [sales/04](../employees/sales/04-follow-up-writer.md) |

## How the work flows

```text
Lead Finder --(new rows)--> Enricher and Qualifier --(HOT and WARM)--> Cold Email Drafts
                                                                          |
                                                              YOU review and send
                                                                          |
                                                    Follow Up Writer (quiet threads)
                                                                          |
                                                              YOU review and send
```

Hand offs:

1. The Lead Finder adds leads with an empty score.
2. The Enricher scores every lead with an empty score. NOT A FIT leads stop here.
3. The Cold Email writer drafts only for HOT and WARM leads and marks them "draft ready".
4. You read, edit and send. Then mark the lead "sent" in the list.
5. The Follow Up Writer looks only at leads marked "sent" with no reply.

The status column in the lead list is the hand off: empty score, scored, draft ready, sent, replied, closed.

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | LinkedIn Lead Finder | Enricher and Qualifier | Leads with an empty score | Lead list, status column empty | Monday run finishes |
| 2 | Enricher and Qualifier | Cold Email First Drafts | Scored leads, status set to scored | Lead list | Daily 10 AM run |
| 3 | Cold Email First Drafts | You | Drafts for HOT and WARM leads, status set to draft ready | Your email drafts folder | Daily 11 AM run |
| 4 | You | Follow Up Writer | Sent emails, status set to sent | Your sent folder and the lead list | You press send and update the status |
| 5 | Follow Up Writer | You | Follow up drafts in the same thread | Your email drafts folder | Daily 2 PM run finds quiet threads |

## Run it in Grok Bot

Create the four bots. Put them in one group chat and send:

```text
We run one outbound line. The status column in the lead list is how you pass work.
- Lead Finder: add leads with an empty score.
- Enricher: score leads with an empty score, then set status to "scored".
- Cold Email Drafts: draft only for HOT or WARM leads with status "scored", then set "draft ready".
- Follow Up Writer: only leads with status "sent" and no reply.
No one sends anything. Post a one line summary here after each run.
Every Friday at 4 PM, Enricher, post a funnel count: leads found, HOT, WARM, NOT A FIT, drafts ready, sent, replies.
```

## Run it in OpenAI Dots

Add the four employee prompts as four projects in your dot, then send:

```text
These four projects form one outbound line, and the status column in the lead list is how they pass work (empty score, scored, draft ready, sent, replied, closed). Keep each project's rules. Never send anything. Every Friday at 4 PM, send me the funnel count: leads found, HOT, WARM, NOT A FIT, drafts ready, sent, replies.
```

## Your weekly check

- Read every draft before you send it. This is the step that protects your reputation.
- Look at the NOT A FIT reasons once a week. If good leads are being dropped, fix your ideal customer profile.
- Keep sending volume low and personal. Follow your email provider's sending rules and the anti spam laws where your leads live.
