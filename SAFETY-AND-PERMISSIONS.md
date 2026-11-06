# Safety and permissions

AI employees work inside your real accounts. That is what makes them useful, and it is why the rules below matter. Read this once before you set up your first employee.

Both companies say the same thing in their own words: OpenAI says "Dots can still make mistakes, so always review consequential work", and xAI's Grok Bot 101 guide says that with plain language rules "you are trusting the model to follow what you wrote." Plan for mistakes.

## The 5 rules every employee in this kit follows

1. **Draft only.** It asks you before it sends, posts, publishes, pays, buys, deletes or contacts anyone. Every time, not just the first time.
2. **No passwords, codes or keys.** It never asks for, stores or types a password, one time code, API key, or bank or card details.
3. **No invented facts.** If it cannot check something, it writes NOT FOUND or UNVERIFIED.
4. **Ask, do not guess.** Unclear input means a question to you.
5. **Keep data inside your tools.** Client, lead and candidate details stay in the apps you connected.

These rules are written into every prompt in this kit. Also set them in each tool's own controls, because a prompt alone is not a lock.

## Set the controls in each tool

### OpenAI Dots

From OpenAI's announcement and help center (see [SOURCES.md](SOURCES.md)):

- **Choose which apps your dot can use.** Connect only what the job needs. Permission to read may not include permission to change or send, so check each app's allowed actions.
- **Custom rules.** For each kind of action you can pick: take action without asking, take action if pre approved, ask before taking action, or hand off to you. On mobile this is under Customize > Custom rules. Suggested settings for this kit:
  - Sending email or messages: Ask before taking action.
  - Posting or publishing: Ask before taking action.
  - Purchases and payments: Hand off to you.
  - Sharing files or folders: Ask before taking action.
- **Know what "pre approved" means.** OpenAI says it means you explicitly asked for the action in your prompt, and that asking for a draft does not authorize sending it.
- **Proactive research is read only.** OpenAI says background research uses read only tools that cannot send messages, change app content, or control your browser or computer.
- **Watch the work.** Use Activity View or your dot's profile to see what is in progress, scheduled and completed.
- **Your own computer stays separate** unless you choose to connect it. Only connect it if a job truly needs it.
- **Pause** your dot from its profile any time.
- **Stopping a task does not undo actions it already finished.** Review before you approve, not after.

### Grok Bot

From xAI's announcement and Grok Bot 101 guide:

- **Write rules in Settings > General > Agent.** A separate review agent checks proposed actions and can allow, block, or escalate to you. Allow and block lists steer that reviewer.
- **Use a block list.** Each employee file includes one: sending email or messages, posting, payments, purchases, deleting, accepting invites, sharing files, changing settings.
- **Sign ins are shared across bots.** xAI's guide says that if you log into a site with one bot, every other bot can reach that site too. Sign in only to what your whole team of bots needs, and never sign in to banking, payroll or admin consoles.
- **A logged in bot can do what you can do.** The same guide gives the example that if you log into a shopping site on a computer the agent can use, it could technically buy things. That is why purchases and payments are blocked in every prompt here.
- **Hand back for sign ins.** When a flow needs a CAPTCHA or a 2FA login, the bot can hand the desktop back to you. Do these steps yourself.

## Before anything is sent: the review habit

Every employee file ends with "How to check its work in 2 minutes". Do that check every day for the first 2 weeks, then a few times a week. In particular:

- Read every draft before you send it. Out loud if it matters.
- Check one fact or number per report against its source.
- Look at what it skipped or flagged, not only what it did.

## Data privacy

- **Connect the least.** Read only access where you can. One inbox, not all of them.
- **Client data.** Some contracts limit where client data may go. Check your client agreements and each vendor's terms before you connect client systems.
- **Candidate data.** CVs hold personal data. Use candidate IDs in reports, never record protected traits, and follow the hiring and data laws where you hire. Some places have specific rules for using automated tools in hiring.
- **Leads.** Use public, work related information only. Respect each platform's terms (for example LinkedIn's rules on automated activity) and the email and privacy laws where your leads live.
- **Training settings.** OpenAI says it does not use content from ChatGPT Business, Enterprise or Edu workspaces to train its models by default, and on personal plans you can control whether your dot's conversations are used. Check the current settings yourself. For Grok Bot, check xAI's current terms.

## Never give an AI employee

- Your passwords or anyone else's.
- One time codes, recovery codes, or 2FA apps.
- Bank, card or payment details.
- Government ID numbers.
- Access to payroll, banking or admin consoles.

If an employee asks for any of these, stop it, check its instructions, and do the step yourself.

## If something goes wrong

1. Pause the employee (Dots: pause from the profile; Grok Bot: stop the bot's routine).
2. Look at its activity to see exactly what it did.
3. Undo what you can by hand, and tell anyone affected.
4. Add a rule that would have prevented it, then restart on a small batch.
