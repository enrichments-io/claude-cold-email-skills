# Claude Skills for Cold Emails

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

### Install

```bash
cp -r claude-cold-email-skills ~/.claude/skills/
```

Then just ask for a cold email. The skill triggers on its own.

Anywhere else that loads Claude Skills, drop the folder in. Or paste `SKILL.md`
straight into a chat and give it the five fields.

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
claude-cold-email-skills/<identity>/
├── SKILL.md
└── references/
    ├── input-template.md
    └── scoring-rubric.md
```

## License

MIT. Inspired by publicly published emails. Not affiliated with or endorsed by
Steve Jobs or Apple.
