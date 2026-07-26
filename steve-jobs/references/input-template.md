# Input template

Copy this, fill it in, paste it to Claude. Five fields. The whole method runs off them.

```
contact:   <first name, title, company>
trigger:   <the specific, checkable thing that happened — a hire, a launch, a posting, an announcement>
offer:     <one sentence: what you do and the outcome. Not the pitch.>
proof:     <one number, one named customer, or one result. Optional but worth finding.>
icp_pain:  <the problem this persona actually has. Optional.>
```

## What makes each field good

**contact.** First name plus enough to know who you are talking to. "Sarah Chen, VP Sales, Ravensworth Freight" is enough. A title alone is not — the email opens with a name.

**trigger.** This is the field that decides whether the email works. It has to be something that happened, that you could point at, and that the recipient knows about. Test it by asking: could this sentence be true of five hundred other companies? If yes, it is a segment, not a trigger.

Good: "posted 12 AE roles in the last month", "moved pricing from per-seat to usage-based in March", "shipped a public API two weeks ago", "their VP Eng started six weeks ago".

Bad: "200-person SaaS company", "growing fast", "uses Salesforce", "recently funded" with no detail on what the money is for.

**offer.** One sentence, plain, no product name required. "We remove pre-call account research from the SDR workflow" works. "An AI-powered GTM intelligence platform that empowers revenue teams" does not — nobody can picture it, so it cannot appear in an 80-word email.

**proof.** One thing. A number the reader can check against their own situation beats a testimonial, and a customer in their segment beats a logo they have never heard of. If you have nothing, leave it blank; the skill will lean on the trigger and tell you that proof was the weakest input.

**icp_pain.** What the person in this seat complains about, in their words rather than your category's words. This shapes the second sentence — the consequence — and it is what stops the email sounding like it was written about the company instead of to a person.

## Optional extras

Add any of these lines if you have them. Each one is used if present and ignored if not.

```
sender:        <your first name, for the sign-off>
constraint:    <anything to avoid — a competitor to not name, a claim legal will not approve>
prior_contact: <if you have emailed or met before, say so; the skill will not write a fake first touch>
```

## Filled example

```
contact:   Sarah Chen, VP Sales, Ravensworth Freight
trigger:   Posted 12 AE roles in the last month
offer:     We remove pre-call account research from the SDR workflow
proof:     Sellers spend ~20 minutes researching each account, ~20 accounts per rep per week
icp_pain:  Ramp time and seller hours lost to manual research
sender:    Alex
```

## If you only have a company name

Go find a trigger before you write. Twenty minutes on their careers page, their changelog, their pricing page, and the recipient's recent posts will produce one. That twenty minutes is the entire difference between an email that gets a reply and one that gets deleted, and no prompt can substitute for it.
