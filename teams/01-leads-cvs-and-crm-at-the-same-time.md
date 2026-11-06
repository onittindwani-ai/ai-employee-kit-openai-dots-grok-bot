# Team recipe 1: Leads, CVs and the CRM, all at the same time

Three AI employees work side by side. One finds LinkedIn leads, one screens CVs, and one keeps the CRM up to date. They do not wait for each other. You review one combined report at the end of the day.

## Who is on the team

| Employee | Job | File |
| --- | --- | --- |
| LinkedIn Lead Finder | Finds new leads that match your ideal customer | [sales/01](../employees/sales/01-linkedin-lead-finder.md) |
| CV Screener | Scores new CVs against your scorecard | [hiring/02](../employees/hiring/02-cv-screener.md) |
| CRM Updater | Updates contacts and deals from emails and notes | [sales/07](../employees/sales/07-crm-updater.md) |

## How the work flows

```text
            +------------------------+
 Monday --> | LinkedIn Lead Finder   | --> new rows in the lead list --+
            +------------------------+                                |
                                                                      v
            +------------------------+                      +-------------------+
 Daily ---> | CRM Updater            | <-- emails, notes    | CRM: new leads    |
            +------------------------+                      | added after your  |
                                                            | yes               |
            +------------------------+                      +-------------------+
 Daily ---> | CV Screener            | --> screening sheet
            +------------------------+

 6 PM: one combined report to you (what each did, what waits for you)
```

Hand offs:

1. **Lead Finder to CRM Updater.** The Lead Finder writes new leads to the lead list. The CRM Updater lists them as "new contacts to create" and waits for your yes before adding them to the CRM.
2. **CV Screener works alone.** It only reads CVs and writes to the screening sheet. It never touches the CRM.
3. **Everyone reports to you.** Nothing goes out to a lead or a candidate.

## Hand off table

| Step | From | To | What is passed | Where it lives | What starts the next step |
| --- | --- | --- | --- | --- | --- |
| 1 | LinkedIn Lead Finder | CRM Updater | New lead rows (name, title, company, link, why they fit) | Lead list sheet | Lead Finder posts "Added <n> leads" in the team chat |
| 2 | CRM Updater | You | List of new contacts to create | Team chat or your dot's report | CRM Updater's run after the Lead Finder message |
| 3 | You | CRM Updater | Your yes or no per contact | Team chat or your dot's conversation | Your reply |
| 4 | CV Screener | You | Scores with quotes and labels | Screening sheet | CV Screener's daily 5 PM run |
| 5 | All three | You | One combined report | Team chat or your dot's conversation | 6 PM |

## Run it in Grok Bot (best fit for this recipe)

xAI says bots can work in parallel, message each other and coordinate in a group chat, which is exactly this recipe.

1. Create the three bots using the Grok Bot prompts in their employee files.
2. Create a group chat with all three bots and you.
3. Send this to the group:

```text
This is our team chat. Each of you keeps your own job and your own rules.
- LinkedIn Lead Finder: when you add leads, post a one line summary here: "Added <number> leads to the lead list."
- CRM Updater: when you see that message, read the new rows and list them as new contacts to create. Do not create them until I say yes in this chat.
- CV Screener: post a one line summary here after each run.
At 6 PM, CRM Updater, please post one combined report for all three of you:
1. What each bot did today (numbers only)
2. Everything waiting for my approval
3. Anything that went wrong
Never send anything to a lead or a candidate. Never share a lead's or candidate's details outside this chat and the sheets I connected.
```

Note from xAI's Grok Bot 101 guide: if you sign into a site with one bot, every other bot can reach that site too. Only sign in to what this team needs.

## Run it in OpenAI Dots

OpenAI says you start with your primary dot, and that a dot can run a project while working on several others. So run the three employees as three projects inside your one dot.

1. Paste each employee's Dots prompt as its own project.
2. Then send this:

```text
You now run three standing projects for me: LinkedIn Lead Finder, CV Screener and CRM Updater. Keep each project's rules separate.
When the Lead Finder adds leads, the CRM Updater should list them as new contacts to create and wait for my yes.
Every weekday at 6 PM, send me one combined report:
1. What each project did today (numbers only)
2. Everything waiting for my approval
3. Anything that went wrong
```

## Your daily 5 minutes

1. Read the combined report. Approve or reject the new CRM contacts.
2. Spot check 2 leads and 2 CV scores (see each employee's "How to check its work in 2 minutes").
3. Reply with any correction in the same chat.
