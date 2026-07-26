# Claude Skills for Cold Emails

Two skills. One writes cold emails, one tears them apart. Neither impersonates
anybody.

```
claude-cold-email-skills/
├── steve-jobs/              write a cold email
└── email-roast/            audit and rebuild one
    └── gordon-ramsay/
```

## Install

Each skill folder needs to land directly in your skills directory — Claude looks
for `SKILL.md` one level down, so copy the leaf folders, not the repo.

```bash
cp -r steve-jobs email-roast/gordon-ramsay ~/.claude/skills/
```

Then just ask. Both skills trigger on their own. Anywhere else that loads Claude
Skills, drop the folders in. Or paste a `SKILL.md` straight into a chat.

## 1. Steve Jobs

A cold email skill built from the mechanics visible in Steve Jobs' public emails:
no warm-up paragraph, one point at a time, plain words, specific evidence, a
position rather than a pitch, and one ask that takes seconds to answer.

Not a prompt that says "pretend you're Steve Jobs." That produces costume copy.
This skill never impersonates him, never quotes him, and never signs as him — it
applies the mechanics and leaves your voice alone.

### What it does

You give it five fields. It runs twelve passes over the draft and returns three
variants that argue different things, each 80 words or fewer with one CTA, each
scored for whether the recipient will actually reply.

```
INPUT → CONTEXT → POINT → PROOF → ASK → SCORE
```

The twelve passes: recipient context extractor, trigger and timing matcher,
one-point message planner, proof and specificity selector, subject-line
compressor, curiosity-gap composer, brevity budget enforcer, frictionless CTA
builder, objection-aware rewriter, mobile scan optimizer, spam-language filter,
reply-intent scorer.

### The five inputs

`contact`, `trigger`, `offer`, `proof`, `icp_pain`. Fill-in block and guidance on
what makes each one good: [`references/input-template.md`](steve-jobs/references/input-template.md).

`trigger` is the field that decides whether the email works. If it could be true
of five hundred other companies, it is a segment, not a trigger, and the skill
will tell you so instead of writing around it.

### Example output

```
Subject: twelve AEs

Sarah - you're hiring 12 AEs.

If each spends 20 minutes researching an account, that's 80 seller-hours every week.

We remove that step.

Worth seeing?
```

One observation. One consequence. One promise. One easy reply.

### Scoring

Every variant is scored out of 100 across Relevance (40), Clarity (30), and Reply
effort (30), with automatic failures for fabricated facts, arithmetic that does
not compute, calendar links in a first touch, and anything over 80 words. Full
rubric and how to calibrate it against your own sent mail:
[`references/scoring-rubric.md`](steve-jobs/references/scoring-rubric.md).

Below 75, the skill refuses and tells you which input to go improve. That refusal
is the most useful thing it does — a generic opener is not neutral, it tells the
reader a machine sent this.

### Files

```
steve-jobs/
├── SKILL.md
└── references/
    ├── input-template.md
    └── scoring-rubric.md
```

## 2. Gordon Ramsay

A kitchen inspection for cold emails. It tastes the email, says exactly what is
wrong with it, checks whether your enrichment can even support the claims you are
making, and then cooks it properly.

Same rule as above: no impersonation, no catchphrases, no celebrity voice. The
critique is direct because direct is useful. The rebuilt email is plain enough to
send to a VP tomorrow morning.

### What it does

Feed it a draft, an enriched record, a Clay row, a CSV, or a whole batch. It runs
three stages — prep the ingredients, cook the copy, taste before sending — and
returns a verdict, a score, the roast, what data you are missing, and a rebuilt
email of 45–75 words.

```
INPUT → PREP → COOK → TASTE → VERDICT
```

Five modes: roast (audit only), rewrite, from-data, sequence (opener plus three
follow-ups that each earn their reply), and batch.

### The four verdicts

| | |
| --- | --- |
| **RAW** | Ingredients missing or unreliable. Do not send. |
| **BLAND** | Technically fine, completely forgettable. Rewrite. |
| **OVERCOOKED** | Too long, too many features, too many asks. Cut. |
| **READY TO SEND** | Accurate, specific, short, easy to answer. |

### Scoring

Out of 100, across data integrity (20), ICP and persona fit (15), trigger quality
(15), relevance (15), clarity (10), brevity (10), credibility (10), and CTA
quality (5). Eight hard failures block a send at any score — a hallucinated fact,
an unsourced number, two CTAs, a suppression match, and so on. Full logic:
[`references/scoring-rubric.md`](email-roast/gordon-ramsay/references/scoring-rubric.md).

The part that does the most work is the **enrichment gate**. Your data gets its
own score out of 100 — identity, email, employment recency, trigger recency,
source quality, cross-source agreement, ICP, persona. Below 70 it will not write
a personalized email at all. You get a data-gap report, the safest account-level
draft labeled `NOT READY`, and the one input that would unlock the good version.

That refusal is the point. Fake personalization is worse than none — it tells the
reader a machine sent this, and it does it in the first line.

### Example output

```
### VERDICT
BLAND

### SCORE
51 / 100

### THE ROAST
- Six open SDR roles were sitting in your enrichment and you wrote
  "Halcyon is growing quickly." You had the specific and chose the generic.
- Four features in one sentence is not a value proposition, it is a menu.
- "Significantly more pipeline" is the sound of a number you can't cite.

### REBUILT EMAIL
Subject: six sdr roles

Priya — 6 open SDR roles on your careers page.

Ramping that many at once usually means reps spend their first month
building lists instead of calling. The pipeline math stops working.

We build the lists for them, so week one is dials.

Who owns SDR ramp at Halcyon right now?

### FINAL SEND CHECK
SEND
```

Six worked examples, one per verdict plus a batch and a refusal:
[`references/examples.md`](email-roast/gordon-ramsay/references/examples.md).

### Batches

Paste a CSV, a JSON array, a Clay export, or a table. You get one result per row
— verdict, score, subject, body, missing data, send status — in a markdown table
to read and a JSON array to import. Row order and record IDs survive the trip.

Duplicates get flagged, suppressed contacts get no copy written at all, and
nothing leaks between rows: evidence found for row 3 never shows up in row 7.

### Files

```
email-roast/gordon-ramsay/
├── SKILL.md
└── references/
    ├── scoring-rubric.md
    ├── enrichment-schema.md
    ├── writing-rules.md
    └── examples.md
```

## License

MIT. Inspired by publicly published emails and by the general idea of a kitchen
inspection. Not affiliated with, endorsed by, or written in the voice of Steve
Jobs, Apple, or Gordon Ramsay.
