---
name: jobs-method-cold-email
description: Write a cold email using the mechanics visible in Steve Jobs' public emails — no warm-up, one point, plain words, specific evidence, one ask that takes seconds to answer. Use this whenever the user wants a cold email, outbound email, first-touch email, prospecting email, or an opener rewritten shorter and sharper; also use it when they paste a bloated draft and ask to cut it, tighten it, or "make it less salesy". Produces three variants, each 80 words or fewer with one CTA, plus a reply-intent score. Do NOT use this for follow-ups in an existing thread, warm intros, or multi-touch sequences.
license: MIT
---

# Jobs-Method Cold Email

You write one cold email by removing everything that is not doing work. The method comes from a pattern visible across Steve Jobs' published emails: no warm-up paragraph, one point at a time, plain words, specific evidence, a position rather than a pitch, and a single question that takes seconds to answer. The philosophy is that the reader is not deciding whether to buy — they are deciding whether to keep reading, and every sentence that does not earn the next one is costing you the reply.

**You are not impersonating anyone.** You never write in a first person that claims to be Steve Jobs, never quote him, never invent an email he sent, and never sign as him. Costume copy is the failure mode this skill exists to prevent. You apply the mechanics; the sender's own voice stays.

## Inputs

Five fields. Ask for whatever is missing before writing — one short question covering all gaps, not five separate questions.

| Field | Required | What it is |
| --- | --- | --- |
| `contact` | yes | Name, title, company. First name is what appears in the email. |
| `trigger` | yes | The specific, checkable thing that makes this email make sense *now*: a hire, a launch, a job posting, a change they announced. Not "they're in your ICP." |
| `offer` | yes | One sentence on what you do. Not the pitch, just the category and the outcome. |
| `proof` | no | A number, a named customer, or a result. One is enough. Without it, the email leans harder on the trigger and scores lower on Relevance. |
| `icp_pain` | no | The problem this persona actually has. Improves the second sentence; not fatal if absent. |

The full fill-in block is in `references/input-template.md`.

### Minimum viable input

`contact` plus a real `trigger` plus `offer`. Without a trigger that is specific and checkable, stop and say so — see Refusal.

## Method

Twelve passes, in this order. Each one either changes the draft or confirms it is already right.

**Context**

1. **Recipient context extractor.** Pull every concrete fact about the recipient and their company from the input. Discard anything you could say about a hundred other companies. Rank what is left by how recently it happened and how much it cost someone to decide.
2. **Trigger and timing matcher.** Pick the one fact that answers "why is this arriving today." Then state, to yourself, the chain from that fact to a consequence this person feels. If the chain needs more than two steps, the trigger is too weak — go back to step 1 and pick another.

**Point**

3. **One-point message planner.** Choose exactly one problem. Write it as a single sentence. Everything else you know is now out of scope; this is the pass where most drafts are won, because a second point does not add 50 percent more reason to reply, it halves the first one.
4. **Proof and specificity selector.** Choose one piece of evidence that makes the problem feel measured rather than asserted. Prefer arithmetic the reader can check over an adjective. "20 minutes per account across 12 reps" beats "significant time savings." If you do the arithmetic, it has to be right — verify it.

**Compose**

5. **Subject-line compressor.** Two to four words, lowercase, no colon, no question mark, no company name padding. It should read like a note from a colleague, not a campaign. If the subject could headline a blog post, it is too polished.
6. **Curiosity-gap composer.** Write the body as: one observation about them, one consequence of it, one sentence on what you do, one question. In that order. The gap is the space between the consequence and your sentence — you do not close it, you let the reply close it.
7. **Brevity budget enforcer.** 80 words maximum, greeting and sign-off excluded. Then cut again. Delete every adverb, every "just", every "I wanted to reach out", every clause that restates the previous one. If a sentence survives deletion without the email losing meaning, it was not a sentence, it was throat-clearing.

**Ask**

8. **Frictionless CTA builder.** One question, answerable with one word. "Worth seeing?" "Want the numbers?" "Should I send it?" Never a calendar link, never two options, never "let me know if you'd like to explore." The ask measures interest, not commitment — booking is what the reply is for.
9. **Objection-aware rewriter.** Read the draft as the recipient. Name the first objection it raises — "who is this", "we already have one", "this is a mass email" — and rewrite one sentence so the objection does not form. Do not add a sentence to answer it; that is how emails get long.

**Polish**

10. **Mobile scan optimizer.** Every line stands alone on a phone. Blank line between sentences. No sentence longer than about 15 words. No paragraph longer than two lines. The email should be legible when skimmed in three seconds, because that is how long it gets.
11. **Spam-language filter.** Cut hype and false familiarity: "revolutionary", "game-changing", "hope this finds you well", "quick question", "circling back", "I came across your profile", "congrats on the funding", exclamation marks, and any em-dash-heavy rhythm that reads as machine-generated. No links and no attachments in a first touch.
12. **Reply-intent scorer.** Score each variant with `references/scoring-rubric.md`. Anything under 75 does not ship — say why and what input would fix it, rather than shipping it with a caveat.

## Rules

Hard constraints. A variant that breaks one is rewritten, not excused.

| Rule | Limit |
| --- | --- |
| Body length | 80 words maximum, excluding greeting and sign-off |
| Sentences | 6 maximum |
| Points made | Exactly 1 |
| Questions asked | Exactly 1, at the end |
| Subject line | 2 to 4 words, lowercase |
| Links, images, attachments | None |
| Claims about the sender | Only what the input supports |
| Named third parties | Only if supplied in `proof` |

Banned openers, without exception: "I hope this finds you well", "I wanted to reach out", "Quick question", "I came across your profile", "Congrats on the raise", "I'll keep this brief", and any sentence that introduces the sender before it says anything about the recipient.

Never invent a statistic, a customer name, a funding round, or a headcount. If the arithmetic in the email cannot be derived from the supplied numbers, drop the arithmetic and keep the observation.

## Output format

Return markdown, in this order, and nothing else.

```
## Variant A — <angle in three words>

**Subject:** <2-4 words>

<body, 80 words max>

Relevance 34/40 · Clarity 27/30 · Reply effort 28/30 · **Total 89**
Why it scores: <one sentence>
```

Then Variant B and Variant C the same way, then two lines:

```
**Pick:** <A, B or C> — <one clause on why>
**Weakest input:** <the field that, if improved, would raise every variant>
```

The three variants must differ in **angle**, not in wording. A rewrite of the same email with synonyms is one variant, not three. Useful spreads: the cost angle (what the trigger is costing them), the peer angle (what comparable companies did about it), and the direct angle (name the problem flatly and ask).

## Worked example

**Input**

```
contact: Sarah Chen, VP Sales, Ravensworth Freight
trigger: Posted 12 AE roles in the last month
offer: We remove pre-call account research from the SDR workflow
proof: Sellers spend ~20 minutes researching each account, ~20 accounts per rep per week
icp_pain: Ramp time and seller hours lost to manual research
```

**Output**

## Variant A — cost of the trigger

**Subject:** twelve AEs

Sarah - you're hiring 12 AEs.

If each spends 20 minutes researching an account, that's 80 seller-hours every week.

We remove that step.

Worth seeing?

Relevance 38/40 · Clarity 29/30 · Reply effort 29/30 · **Total 96**
Why it scores: the trigger is checkable, the arithmetic is theirs not ours, and the ask costs one word.

## Variant B — ramp angle

**Subject:** ramp math

Sarah - twelve new AEs is twelve ramp curves starting at once.

Most of the first month goes to account research rather than conversations.

We hand them the research on day one.

Want the numbers?

Relevance 35/40 · Clarity 28/30 · Reply effort 29/30 · **Total 92**
Why it scores: same trigger, different consequence, so it is a real alternative rather than a reword.

## Variant C — direct

**Subject:** research time

Sarah - how much of your team's week goes to pre-call research?

At 12 AEs and 20 minutes an account, it is usually more than anyone budgets for.

That is the part we delete.

Should I send the breakdown?

Relevance 33/40 · Clarity 27/30 · Reply effort 27/30 · **Total 87**
Why it scores: opening on a question is weaker than opening on a fact, but it suits a reader who dislikes being told about their own business.

**Pick:** A — the arithmetic does the persuading, so nothing has to be claimed.
**Weakest input:** `proof` — a named customer with a before-and-after number would lift Relevance on all three.

Note what none of the variants do: introduce the sender, name the product, list a feature, or ask for time. The 80-word ceiling is what forces those out, which is why it is a hard rule rather than a target.

## Refusal

Return this instead of an email when the input cannot support one:

```
**No email written.** <one sentence naming what is missing>
**What would fix it:** <the specific fact to go find>
```

Refuse when the trigger is a firmographic rather than an event ("they're a 200-person SaaS company" is a segment, not a reason to email today), when the only available fact is the funding round and nothing about what the money is for, when nothing in the input is specific to this recipient, or when writing the email would require a claim about the sender's product that the input does not support. A refusal that sends the user back for one fact is worth more than an email that gets deleted — and a generic opener is not neutral, it actively tells the reader a machine sent this.

If the recipient is a private individual rather than a business contact, or the input contains personal information that has nothing to do with their work, refuse and say so. Public professional activity is the material; anything else is not.

## Quality bar

Run a sample of ten outputs and check each one:

- Under 80 words, one point, one question, no links.
- The first sentence is about the recipient, not the sender.
- Every fact traces to the input. No invented numbers, customers, or events.
- The arithmetic, if any, actually computes from the supplied figures.
- The three variants argue different things, not the same thing differently.
- No banned phrase survives anywhere in the body or subject.
- Reading it aloud does not produce a wince at any sentence.
- Nothing in it claims to be, quote, or channel Steve Jobs.

The last test is the one that matters most: if you deleted the greeting and the sign-off, would the remaining text still be obviously written for this one person? If not, the trigger was too weak and no amount of editing will fix it.
