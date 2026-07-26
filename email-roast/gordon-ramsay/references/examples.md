# Examples

Six worked cases. Each shows the input, a short reasoning summary, the score, the verdict, and the output as the skill would return it. Scores are computed against `scoring-rubric.md`; nothing here is rounded to look tidy. All dates are relative to 2026-07-26.

---

## Example 1 — Generic and feature-heavy → BLAND

### Input

```
Draft:
  Hi Priya,

  I hope this email finds you well! My name is Alex and I'm the founder of
  Leadstack, a revolutionary sales intelligence platform that helps go-to-market
  teams unlock their full potential.

  We offer automated list building, intent data, real-time enrichment, and
  seamless CRM integration — all in one best-in-class solution. Companies that
  use Leadstack see significantly more pipeline.

  I noticed Halcyon is growing quickly and thought you might be interested.

  Would you be open to a 30-minute demo next week to explore how we can help?

  Best, Alex

Record:
  Priya Raman · Director of Sales Development · Halcyon Logistics
  480 employees · freight tech · verified work email
  Signal: 6 open SDR roles, halcyonlogistics.com/careers, 2026-07-09
Campaign:
  ICP: logistics and supply chain, 250-1000 employees
  Problem: SDRs spend their ramp period building lists instead of calling
  Offer: done-for-you list building
  Proof: none supplied
```

### Reasoning summary

The data is fine. The email ignores it. There is a dated, sourced hiring signal sitting in the record — six SDR roles, 17 days old — and the draft reaches for "Halcyon is growing quickly" instead. Everything after the greeting is about the sender. Four features, no problem, no why-now. "Significantly more pipeline" is a claim with nothing behind it, though not a numeric one, so no hard failure. One CTA, but an expensive one. Enrichment **74/100** — workable, weakest component is cross-source agreement.

### Score

`51 / 100` — Data integrity 14 · ICP & persona 12 · Trigger 3 · Relevance 5 · Clarity 5 · Brevity 7 · Credibility 3 · CTA 2

### Output

**VERDICT:** BLAND

**THE ROAST**

- Six open SDR roles were sitting in your enrichment and you wrote "Halcyon is growing quickly." You had the specific and chose the generic.
- Four features in one sentence is not a value proposition, it is a menu. Priya has to pick her own problem, and she won't.
- "Revolutionary," "unlock," "seamless," "best-in-class" — four dead words in 32. Delete them and the sentence says nothing, which is the point.
- "Significantly more pipeline" is the sound of a number you can't cite. Say the real one or say nothing.
- You opened with your own name and job title. Nobody has agreed to care yet.

**MISSING INGREDIENTS**

- `signals[0]` — present but unused — the strongest asset in the record never made it into the email.
- `proof` — MISSING — no case study supplied, so the rebuild carries no proof line. That is correct, not a gap to fill.
- `employee_count` cross-source — UNVERIFIED — 480 from one provider only.

**REBUILT EMAIL**

Subject: six sdr roles

> Priya — 6 open SDR roles on your careers page.
>
> Ramping that many at once usually means reps spend their first month building lists instead of calling. The pipeline math stops working.
>
> We build the lists for them, so week one is dials.
>
> Who owns SDR ramp at Halcyon right now?

*50 words.*

**WHY THIS VERSION WORKS**

- Opens on a dated, sourced fact she can verify in one click.
- One problem — ramp time — instead of four features.
- No proof claim, because there is no proof. Credibility 5 beats Credibility 0.
- The ask is a question she can answer in four words.

**FINAL SEND CHECK:** SEND

---

## Example 2 — Research dump → OVERCOOKED

### Input

```
Draft (177 words):
  Hi Marcus,

  I've been following Corvus Health for a while now and I have to say I'm really
  impressed with what you're building in the healthcare data space. I saw your
  talk at Data Council about the Snowflake migration, read your engineering blog
  post about your dbt adoption, and noticed on LinkedIn that you're hiring three
  analytics engineers. I also saw that Corvus was named to the Inc. 5000 list
  last year — congratulations on the growth!

  At Modelgate, we've built a comprehensive data observability and governance
  platform that provides automated lineage tracking, column-level data quality
  monitoring, anomaly detection, cost attribution for warehouse spend, and a full
  model catalog with ownership assignment. We work with dozens of data teams
  across healthcare, fintech, and e-commerce, and our customers typically see
  substantial improvements in data reliability.

  Given everything happening at Corvus right now, I think there could be a really
  strong fit here.

  Would you be open to a 30-minute call next week? You can also grab time
  directly on my calendar here, or just reply if you have questions.

  Best regards, Jordan

Record:
  Marcus Webb · Director of Data Engineering · Corvus Health · 900 employees
  Signals: Data Council talk on Snowflake migration (2026-06-18, conference site)
           3 open analytics engineer roles (2026-07-02, careers page)
Campaign:
  Problem: post-migration dbt models end up unowned and undocumented
  Offer: model catalog with ownership assignment
  Proof: two healthcare data teams run it post-migration (supplied, unnamed)
```

### Reasoning summary

Every fact is real and sourced — this is the rare draft with a data integrity problem of the opposite kind. It has *too much* evidence and no argument. Four research findings before a single word about Marcus's problem, then five features, then a fit assertion with nothing under it, then three separate asks. Clarity collapses because there is no single idea to hold onto. Brevity scores zero at 177 words. H5 fires on the three CTAs. Enrichment **88/100**.

Score lands at 68, inside the BLAND band, but the override applies: over 100 words, more than one CTA, and Clarity + Brevity loss (16) exceeds Trigger + Relevance loss (6). This is not a bland email. It is an overcooked one, and the fix is a knife.

### Score

`68 / 100` — Data integrity 18 · ICP & persona 14 · Trigger 13 · Relevance 12 · Clarity 4 · Brevity 0 · Credibility 7 · CTA 0

### Output

**VERDICT:** OVERCOOKED

**THE ROAST**

- You did four pieces of research and put all four in the email. Research is for choosing the one thing to say, not for proving you did research.
- 177 words and Marcus's problem appears in none of them. He learns what you sell before he learns why he should care.
- Five features in one sentence. By the third, he has stopped reading; by the fifth, he couldn't name the first.
- Three asks — a call, a calendar link, and a reply. Every extra option is a reason to close the tab.
- "I think there could be a really strong fit here" is a conclusion with no argument in front of it. You asserted the fit instead of demonstrating it.

**MISSING INGREDIENTS**

- Nothing missing. This is a discipline problem, not a data problem.
- `proof` — UNVERIFIED as written — "dozens of data teams" and "substantial improvements" overstate what the record supports. The record says two healthcare teams. Use that.

**REBUILT EMAIL**

Subject: post-migration ownership

> Marcus — your team's Snowflake migration came up in the Data Council talk last month.
>
> The part that usually hurts isn't the migration, it's the six months after, when every dbt model needs an owner and nobody has time to document them.
>
> We handle that layer. Two other healthcare data teams run it post-migration.
>
> Worth 15 minutes?

*56 words.*

**WHY THIS VERSION WORKS**

- One research finding, chosen because it sets up the problem. The other three stay in the CRM.
- Names the pain that comes *after* the thing he already knows about — that is the part he hasn't solved yet.
- Proof shrunk to what the record actually supports: two teams, unnamed, no invented percentage.
- One ask, one question mark.

**FINAL SEND CHECK:** SEND

---

## Example 3 — Weak and contradictory data → RAW

### Input

```
Draft:
  Hi Tom, congrats on the recent Series A! As VP Marketing at Blackstone Media
  you're probably under real pressure to prove ROI right now. We helped Zenith
  Agency increase client retention by 34% — worth a chat?

Record:
  first_name: Tom · last_name: Alvarez
  job_title: "VP Marketing"            (source: CRM, imported 2024)
  linkedin_url headline: "Senior Marketing Manager"   (source: LinkedIn)
  company_name: "Blackstone Media"     (CRM)
  company_alt_name: "Blackstone Digital"  (enrichment provider)
  domain: blackstonemedia.co.uk
  email: tom@blackstonemedia.com · verification_status: unknown
  Signal: recent_funding, "raised Series A", source_date 2021-03-15
Campaign:
  Offer: automated multi-platform ad reporting
  Proof: none supplied
```

### Reasoning summary

Four separate integrity failures. The title contradicts itself across sources — CRM says VP, LinkedIn says Senior Manager — which is H1 and caps identity confidence at 8. The company name has two variants and the email domain (`.com`) does not match the record domain (`.co.uk`), so the address is probably wrong as well as unverified. The "recent" Series A is dated 2021: over five years old, called recent in the email, which is H2. Zenith Agency and the 34% figure appear nowhere in the campaign, which supplies no proof at all — a fabricated customer and a fabricated statistic, H2 and H3. And "you're probably under real pressure" is invented interior life.

Enrichment: identity 8 · email 4 · employment recency 3 · trigger recency 0 · source quality 3 · cross-source 0 · ICP 4 · persona 2 = **24/100**. Below 70, so H8 fires too. No personalized email is available at any score.

### Score

`31 / 100` — Data integrity 3 · ICP & persona 4 · Trigger 2 · Relevance 3 · Clarity 6 · Brevity 8 · Credibility 2 · CTA 3

Hard failures: H1, H2, H3, H8.

### Output

**VERDICT:** RAW

**THE ROAST**

- You promoted Tom. Your CRM says VP Marketing, his LinkedIn says Senior Marketing Manager, and you picked the flattering one. If he is the wrong seniority for this pitch, the email is dead on the first line — and if he was demoted, it is worse than dead.
- The "recent" Series A closed in March 2021. That is not a trigger, it is an archaeology finding.
- Zenith Agency and the 34% are not in your data. Somebody invented a customer and a number. That is the one mistake that costs the domain, not just the reply.
- "You're probably under real pressure to prove ROI" — you don't know that. You are describing a marketing job, not this person's week.
- The email goes to `@blackstonemedia.com` and the record says `blackstonemedia.co.uk`. One of those bounces.

**MISSING INGREDIENTS**

- `job_title` — CONTRADICTED — CRM "VP Marketing" vs LinkedIn "Senior Marketing Manager". Blocks any title-dependent framing.
- `company_name` — CONTRADICTED — "Blackstone Media" vs "Blackstone Digital".
- `domain` / `email` — CONTRADICTED — `.co.uk` record vs `.com` address. Deliverability risk before anything else.
- `verification_status` — `unknown` — not a sendable state.
- `signals[0].source_date` — STALE — 2021-03-15, over 1,900 days old.
- `proof` — MISSING — the campaign supplies none, so Zenith and the 34% were fabricated. Removed.

**ACCOUNT-LEVEL DRAFT — NOT READY — 24/100 enrichment**

Subject: monday reporting

> Tom — most independent media agencies pull reporting from four or five ad platforms, and someone loses Monday morning stitching it into a single client deck.
>
> We automate that stitch, so the deck builds itself overnight.
>
> Is that still a manual job at Blackstone, or have you already solved it?

*49 words. No title claim, no funding reference, no proof, and only the part of the company name both sources agree on.*

**WHAT WOULD UNLOCK THE PERSONALIZED VERSION**

One confirmed title from a primary source — his LinkedIn profile or the company team page — and one dated signal from the last 60 days. Everything else can stay as is.

**FINAL SEND CHECK:** RESEARCH FIRST

---

## Example 4 — Strong signal → READY TO SEND

### Input

```
Record:
  Sarah Chen · VP Engineering · Northwind Systems
  340 employees · B2B SaaS · Austin TX
  linkedin.com/in/sarahchen · sarah.chen@northwind.io · verified
  Signal: job_posting — "4 open platform engineering roles"
          northwind.io/careers · 2026-07-04 · confidence 0.9
Campaign:
  ICP: B2B SaaS, 200-1000 employees, product-led
  Problem: new engineers take 6+ weeks to ship independently
  Offer: onboarding automation that cuts ramp time
  Proof: Meridian went 6 weeks → 11 days (public case study)
  CTA: ask who owns onboarding today
```

### Reasoning summary

From-data mode, nothing to roast. Identity confirmed on two sources, verified work email, trigger 22 days old from a primary source, exact ICP and persona match, and a real, citable case study. Enrichment breaks down as identity 20 · email 15 · employment 13 · trigger recency 15 · source quality 10 · cross-source 8 · ICP 10 · persona 5 = **96/100**. Send-grade, so a personalized email is available.

The one point not taken: employment recency is 13 rather than 15 because no start date or tenure is in the record. Worth a line in MISSING INGREDIENTS, not worth blocking.

### Score

`95 / 100` — Data integrity 19 · ICP & persona 15 · Trigger 14 · Relevance 14 · Clarity 9 · Brevity 10 · Credibility 9 · CTA 5

### Output

**VERDICT:** READY TO SEND

**THE ROAST**

- Barely anything to say, which is its own kind of suspicious — check the careers page is still live before this sends. A trigger that has been fixed is a trigger that makes you look slow.
- "Without a buddy" is doing a lot of work in line two. It is the right phrase for an engineering audience and the wrong one if Sarah forwards this to procurement.
- The Meridian number is the only thing in here a skeptic can attack. Make sure the case study is public and the link works if she asks.

**MISSING INGREDIENTS**

- `tenure` / `start_date` — MISSING — costs 2 points of employment recency. No effect on the copy.
- Cross-source agreement — partial — title confirmed on LinkedIn and the company team page, but not a third source. Enough.

**REBUILT EMAIL**

Subject: four platform roles

> Sarah — 4 open platform engineering roles on your careers page.
>
> At 340 people, the usual bottleneck isn't hiring them, it's the six weeks before a new platform engineer can ship without a buddy. Four at once makes that six weeks expensive.
>
> We cut ramp to under two weeks. Meridian went from six weeks to eleven days.
>
> Who owns onboarding for the platform team now?

*64 words.*

**WHY THIS VERSION WORKS**

- Opens on a fact she can check in one click, dated 22 days ago.
- Multiplies the problem by her own number — four hires, six weeks each — instead of asserting it is painful.
- One proof point, publicly citable, with a specific before and after.
- The ask is a routing question, which is the cheapest thing a VP can answer.

**FINAL SEND CHECK:** SEND

---

## Example 5 — Batch with a duplicate and a suppressed contact

### Input

```json
{
  "campaign": {
    "icp": "B2B SaaS and industrial tech, 200-1000 employees",
    "problem": "new engineers take 6+ weeks to ship independently",
    "offer": "onboarding automation that cuts ramp time",
    "proof": "Meridian went 6 weeks to 11 days (public case study)",
    "cta": "ask who owns onboarding today",
    "suppression_list": ["ridgelinelegal.com"]
  },
  "prospects": [
    {"record_id": "clay_0417", "first_name": "Sarah",  "job_title": "VP Engineering",        "company_name": "Northwind Systems",  "domain": "northwind.io",          "email": "sarah.chen@northwind.io",  "verification_status": "verified"},
    {"record_id": "clay_0418", "first_name": "Lena",   "job_title": "Head of Platform",      "company_name": "Fernwood Robotics",  "domain": "fernwood.dev",          "email": "l.ortiz@fernwood.dev",     "verification_status": "catch_all"},
    {"record_id": "clay_0419", "first_name": "Dev",    "job_title": "Engineering Manager",   "company_name": "Kestrel Freight",    "domain": "kestrelfreight.com",    "email": "",                          "verification_status": "unknown"},
    {"record_id": "clay_0420", "first_name": "Sarah",  "job_title": "VP of Engineering",     "company_name": "Northwind",          "domain": "northwind.io",          "email": "sarah.chen@northwind.io",  "verification_status": "verified"},
    {"record_id": "clay_0421", "first_name": "Dana",   "job_title": "General Counsel",       "company_name": "Ridgeline Legal",    "domain": "ridgelinelegal.com",    "email": "d.whitfield@ridgelinelegal.com", "verification_status": "verified"}
  ]
}
```

### Reasoning summary

Five rows, three emails. Row 4 is row 1 arriving from a second provider — same email, same domain, cosmetic differences in company name and title — so it is marked `duplicate_of: clay_0417` and no copy is generated. Row 5 matches the campaign suppression list on domain: H6, `BLOCKED`, no body, `BIN IT`. Row 3 has no email address, no signal, and enrichment of 38, so it gets an account-level draft labelled NOT READY rather than a personalized one. Row 2 is `catch_all`, which is sendable but scores half on email confidence and drops the send check to `VERIFY FIRST`.

No evidence crosses rows. Row 1's Meridian proof is campaign-level and available to all; Northwind's careers page is not, and does not appear in rows 2 or 3.

Note where the `NOT READY` label sits on row 3: inside the `body` field, not only in `notes`. A label in a metadata column gets dropped by the first import mapping that ignores it. A label in the body cannot be sent without someone noticing.

### Output

| # | record_id | Verdict | Score | Enrich | Send | Subject |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | clay_0417 | READY TO SEND | 95 | 96 | SEND | four platform roles |
| 2 | clay_0418 | READY TO SEND | 86 | 71 | VERIFY FIRST | ramp time at fernwood |
| 3 | clay_0419 | RAW | 48 | 38 | RESEARCH FIRST | onboarding at kestrel |
| 4 | clay_0420 | — | — | — | DUPLICATE | — |
| 5 | clay_0421 | RAW | — | — | BLOCKED | — |

```json
[
  {
    "record_id": "clay_0417",
    "verdict": "READY TO SEND", "score": 95, "enrichment_score": 96,
    "send_status": "SEND",
    "subject": "four platform roles",
    "body": "Sarah — 4 open platform engineering roles on your careers page.\n\nAt 340 people, the usual bottleneck isn't hiring them, it's the six weeks before a new platform engineer can ship without a buddy. Four at once makes that six weeks expensive.\n\nWe cut ramp to under two weeks. Meridian went from six weeks to eleven days.\n\nWho owns onboarding for the platform team now?",
    "missing_fields": ["start_date"],
    "hard_failures": [], "duplicate_of": null, "suppressed": false,
    "notes": "Careers page signal 22 days old. Re-check it is live before send."
  },
  {
    "record_id": "clay_0418",
    "verdict": "READY TO SEND", "score": 86, "enrichment_score": 71,
    "send_status": "VERIFY FIRST",
    "subject": "ramp time at fernwood",
    "body": "Lena — hardware-adjacent platform teams tend to lose the most time on the first month, when a new engineer can't ship without someone watching.\n\nWe cut that to under two weeks. Meridian went from six weeks to eleven days.\n\nWho owns onboarding for your platform team now?",
    "missing_fields": ["signals", "employee_count"],
    "hard_failures": [], "duplicate_of": null, "suppressed": false,
    "notes": "catch_all email — half email confidence. No signal, so account-level relevance only. No claim made about Fernwood specifically."
  },
  {
    "record_id": "clay_0419",
    "verdict": "RAW", "score": 48, "enrichment_score": 38,
    "send_status": "RESEARCH FIRST",
    "subject": "onboarding at kestrel",
    "body": "NOT READY — 38/100 enrichment. Account-level draft only: Dev — logistics engineering teams usually hit a wall on onboarding somewhere past 150 engineers, when the runbooks stop matching the systems.\n\nWe cut first-ship time to under two weeks.\n\nIs onboarding a problem at Kestrel yet, or still manageable?",
    "missing_fields": ["email", "signals", "employee_count", "industry", "linkedin_url"],
    "hard_failures": ["H8"], "duplicate_of": null, "suppressed": false,
    "notes": "No email address and no signal. Needs a verified address and one dated trigger before this is sendable."
  },
  {
    "record_id": "clay_0420",
    "verdict": null, "score": null, "enrichment_score": null,
    "send_status": "DUPLICATE",
    "subject": null, "body": null,
    "missing_fields": [], "hard_failures": [],
    "duplicate_of": "clay_0417", "suppressed": false,
    "notes": "Same work email and domain as clay_0417. Company name and title differ cosmetically. First occurrence kept."
  },
  {
    "record_id": "clay_0421",
    "verdict": "RAW", "score": null, "enrichment_score": null,
    "send_status": "BLOCKED",
    "subject": null, "body": null,
    "missing_fields": [], "hard_failures": ["H6"],
    "duplicate_of": null, "suppressed": true,
    "notes": "Domain ridgelinelegal.com is on the campaign suppression list. No copy generated. Also outside ICP — General Counsel is not the persona."
  }
]
```

**Summary:** 5 records · 3 emails generated · READY TO SEND 2 · RAW 2 · 1 duplicate · 1 suppressed · SEND 1 · VERIFY FIRST 1 · RESEARCH FIRST 1 · BLOCKED 1.

---

## Example 6 — Refusing to invent personalization

### Input

> "Write a cold email to Jordan Reyes, CTO at Vantage Freight. Make it feel really personal — mention something about their LinkedIn or a recent post. Offer is our API monitoring tool."

```
Record:
  first_name: Jordan · job_title: CTO · company_name: Vantage Freight
  Everything else: absent. No LinkedIn URL, no posts, no signals,
  no domain, no email, no employee count, no industry detail.
```

### Reasoning summary

The request explicitly asks for a personal detail the record does not contain. There is no LinkedIn URL, so there is no post to reference, and inventing one is H2. The correct move is not a hedged fake ("I've been following your work") — that is the same fabrication wearing a coat. Refuse the personal line, deliver the account-level email, and name the single input that would change the answer.

Enrichment: identity 10 · email 0 · employment 0 · trigger 0 · source quality 0 · cross-source 0 · ICP 5 · persona 4 = **19/100**.

### Output

**VERDICT:** RAW — insufficient data for personalization

**WHAT I WON'T DO**

There is no LinkedIn URL in this record and no post attached to it. I can't reference something I don't have, and a vague stand-in — "loved your recent post," "I've been following your work at Vantage" — is a fabrication that Jordan can spot in about a second. Fake personalization is worse than none: it tells the reader a machine sent this, and it does it in the first line.

**MISSING INGREDIENTS**

- `linkedin_url` — MISSING — no profile, therefore no post, therefore no personal opener.
- `signals` — MISSING — no why-now of any kind.
- `email` / `domain` — MISSING — nothing to send to.
- `industry` / `employee_count` — MISSING — ICP fit is an assumption.

**ACCOUNT-LEVEL DRAFT — NOT READY — 19/100 enrichment**

Subject: api monitoring

> Jordan — freight platforms usually find out an integration broke when a customer calls, not when it breaks. The carrier APIs go quiet and nothing in the stack notices for hours.
>
> We watch them and page you instead.
>
> Is that a real problem at Vantage, or already covered?

*47 words. Nothing claimed about Jordan personally. Nothing claimed about Vantage that isn't a general truth about the category, phrased as one.*

**ONE INPUT THAT UNLOCKS THE PERSONALIZED VERSION**

Jordan's LinkedIn URL, or a dated item from the last 60 days — a job posting, a carrier integration announcement, a stack change. Any one of the three moves this from account-level to specific.

**FINAL SEND CHECK:** RESEARCH FIRST
