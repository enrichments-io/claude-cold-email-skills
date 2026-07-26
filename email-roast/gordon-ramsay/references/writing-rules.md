# Writing Rules

Rules for the rebuilt email only. The roast has its own voice; the email has none of it.

---

## 1. Non-negotiables

The final email must:

1. Use only supplied or verifiable evidence.
2. Lead with relevance to them, not with the sender's company.
3. Carry one main idea.
4. Carry one CTA.
5. Fit 45-75 words in the body, or the campaign's `max_words`.
6. Never mention enrichment, scraping, AI, data providers, sequences, or "your profile came up in a search."
7. Never expose scores, verdicts, internal labels, or research notes.
8. Never fabricate a customer, outcome, statistic, trigger, or relationship.

When proof is unavailable, **delete the proof sentence.** Do not soften an invented claim into "companies like yours often see..." — that is the same lie with a hedge on it.

When the signal is weak, use **account-level relevance**: the problem this ICP has, stated plainly, with no pretense of having researched the individual. An honest "most platform teams at your size hit this at around 300 engineers" beats a fake "I was reading your blog."

---

## 2. Banned openers

| Banned | Why | Instead |
| --- | --- | --- |
| "I hope this email finds you well" | Costs a line, says nothing, marks the email as bulk. | Start on their situation. |
| "I noticed / I saw / I came across" | The tell of scraped personalization. Everyone in B2B knows it. | State the fact without narrating your discovery of it. |
| "Quick question" | Never is one. Burned as a subject line. | Ask the actual question. |
| "Hope you're having a great week" | Filler. | Delete. |
| "My name is X and I'm the Y at Z" | Nobody has agreed to care yet. | Sender identity belongs in the signature. |
| "Congrats on the funding!" | Every other email in the inbox that week. | Use the funding as a *reason*, not a greeting. |
| "I'll keep this short" | Then be short. | Delete. |
| "Reaching out because..." | Throat-clearing. | Delete, keep what follows. |

Rewrite of the classic:

> ~~Hi Sarah, I hope this finds you well! I noticed Northwind recently raised a Series B — congrats!~~
>
> Sarah — four open platform roles on your careers page.

---

## 3. Banned vocabulary

**Jargon:** revolutionary, game-changing, game-changer, synergy, synergistic, cutting-edge, best-in-class, world-class, industry-leading, next-generation, paradigm shift, disruptive, seamless, frictionless, turnkey, holistic, robust, leverage (as a verb), unlock, supercharge, 10x, ninja, rockstar, unicorn.

**Empty nouns:** solutions, offerings, capabilities, verticals, learnings, bandwidth, alignment, ecosystem, journey, space (as in "the CRM space").

**Spam triggers:** free, guarantee, guaranteed, risk-free, act now, limited time, exclusive offer, no obligation, once-in-a-lifetime, urgent, don't miss out, click here, 100%, ALL CAPS words, more than one exclamation mark in the whole email.

**Fake urgency:** "before the end of the quarter," "only taking on two more clients," "closing this out," "last chance." If the deadline is real, name it and its cause. If not, delete it.

**Over-familiarity:** "Hey buddy," "my friend," "Hope the kids are well," first-name repetition beyond the greeting, and any presumption of an existing relationship.

Adjective budget: **two per email.** Concrete nouns and verbs do the work.

---

## 4. Structure

```
Subject:  2-5 words, lowercase, no punctuation tricks, no personalization tokens
Greeting: First name + em dash, or "Hi <First>,"
Line 1:   The evidence. One sentence, one fact, verifiable.
Line 2:   The problem that fact implies. Their problem, in their language.
Line 3:   The offer. What you do about it, in one clause.
Line 4:   Proof — only if real. One clause.
Line 5:   The ask. One question.
Sign-off: Name. Optionally one line of role/company. Nothing else.
```

Line breaks between each. No paragraph over two sentences. Total 45-75 words.

### Subject lines

Good: `four platform roles` · `onboarding at 340` · `ramp time` · `your careers page`

Bad: `Quick question` · `Sarah, thoughts?` · `Boost Your Engineering Velocity 🚀` · `Re: our conversation` (there was no conversation) · anything with `{{merge_tag}}` visible.

Lowercase reads as typed by a human. Title Case reads as a campaign. Never fake a reply or forward.

### The ask, cheapest first

1. "Worth a look?"
2. "Who owns this at Northwind now?"
3. "Want the two-line version of how it works?"
4. "Open to 15 minutes next week?"
5. ~~Calendar link in a first touch.~~ Never. It asks the reader to schedule with a stranger.

One question mark in the email. Two questions is two CTAs, and two CTAs is hard failure H5.

---

## 5. Sentence-level rules

- Contractions: yes. "You're," "we've," "doesn't." Their absence reads like a legal notice.
- Sentences under 20 words. Most under 12.
- Active voice. "Your team ships in six weeks," not "shipping is achieved in six weeks."
- Their vocabulary, not the sender's category. "Ramp time" if that is what they call it.
- Numbers as digits: "4 roles," "340 people." Faster to scan.
- No emoji. No bold. No bullet lists in a first touch — bullets look like a deck.
- No links in touch #1 unless the user asks. Links depress deliverability and raise the cost of reading.
- One space after periods. No double line breaks mid-thought. Nothing that looks like it survived a paste from Word.

---

## 6. Personalization honesty test

Before any personalized line ships, both must be true:

1. **Source test** — can you point to the field or URL it came from?
2. **Surprise test** — would the recipient be surprised to learn a stranger knows it?

Passes both → strong opener. Passes 1 only → true but generic; usable, not remarkable. Passes 2 only → **you are guessing.** Cut it.

| Line | Source | Surprise | Verdict |
| --- | --- | --- | --- |
| "Four open platform roles on your careers page." | ✓ | ✓ | Ship it. |
| "You're on AWS." | ✓ | ✗ | True, weak. Use as support, not the opener. |
| "You must be under pressure after the raise." | ✗ | ✓ | Invented. Cut. |
| "Loved your recent post!" (no post in the record) | ✗ | ✗ | Fabrication. Cut and flag. |

Never repeat their own website copy back to them. They wrote it. Quoting the tagline proves you read one page and understood nothing.

---

## 7. Follow-ups

Every follow-up carries a new reason to reply. Banned entirely: "just bumping this," "circling back," "following up," "did you see my last email," "top of mind," "checking in," a lone "?", and re-sending the original with "thoughts?" on top.

| # | Timing | Job | Words |
| --- | --- | --- | --- |
| 2 | +3 days | One new piece of evidence on the same problem. | <50 |
| 3 | +5 days | A different problem, or the same one from another angle. Never repeat #1's argument louder. | <50 |
| 4 | +7 days | Close the loop. No ask, no guilt, no fake deadline. | <35 |

Breakup email that works:

> Sarah — I'll stop here. If onboarding time becomes a priority after the platform hires land, I'm easy to find.

Breakup emails that do not: "I guess you're not interested?" · "Should I close your file?" · "Third and final attempt." Passive aggression is memorable for the wrong reason.

---

## 8. Before and after

**A. Feature dump → one idea**

> ~~Our platform offers automated onboarding, integrated analytics, custom workflows, and enterprise-grade security to help teams like yours unlock their full potential.~~
>
> New engineers at your size usually take six weeks to ship alone. We cut that to under two.

**B. Fake research → honest account-level**

> ~~I was reading about Northwind's impressive growth journey and thought I'd reach out.~~
>
> Most platform teams hit an onboarding wall somewhere past 300 engineers.

**C. Unsupported number → removed**

> ~~We help companies increase pipeline by 40%.~~
>
> We do this for three Series B fintechs. *(Only if true and supplied. Otherwise delete the line — Credibility 5 beats Credibility 0.)*

**D. Two CTAs → one**

> ~~Would you be open to a 30-minute demo next week? Or feel free to book time here, or just reply with questions!~~
>
> Worth a look?

**E. Manufactured urgency → real reason**

> ~~We only have two onboarding slots left this quarter — act now!~~
>
> Worth sorting before the four new hires start.

**F. Setup paragraph → deleted**

> ~~My name is Alex and I'm the founder of Rampline, a company dedicated to helping engineering organizations of all sizes streamline and optimize their onboarding processes...~~
>
> *(Deleted. It goes in the signature. Start at the evidence.)*

---

## 9. Final read-aloud

Read the email out loud. It fails if you hear:

- A sentence you would not say to someone standing in front of you.
- A word you have never spoken aloud in your life.
- A compliment you cannot substantiate.
- Two things being asked for.
- A pause where you have to reread a clause.

One informed person writing to another. That is the whole standard.
