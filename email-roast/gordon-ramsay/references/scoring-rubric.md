# Scoring Rubric

Two independent scores. **Email quality** (0-100) rates the copy. **Enrichment quality** (0-100) rates the data underneath it. A beautiful email built on a guess is still RAW.

---

## 1. Email quality score

Eight categories, 100 points. Score each independently, then sum. Do not round to a pleasing number and do not reverse-engineer points to justify a verdict you have already decided.

| # | Category | Points | Question it answers |
| --- | --- | --- | --- |
| 1 | Data integrity | 20 | Is every factual statement in this email actually supported? |
| 2 | ICP & persona fit | 15 | Is this the right company, and the right human inside it? |
| 3 | Trigger quality | 15 | Why is this arriving today rather than any other day? |
| 4 | Relevance | 15 | Does the offer connect to a problem this person owns? |
| 5 | Clarity | 10 | Can it be understood in one pass on a phone? |
| 6 | Brevity | 10 | Is every sentence earning its place? |
| 7 | Credibility | 10 | Would a skeptical VP believe it? |
| 8 | CTA quality | 5 | How cheap is it to reply? |

### 1. Data integrity — 20

Every name, title, company, number, event, and observation traced to supplied data.

| Band | Points | Looks like |
| --- | --- | --- |
| Clean | 18-20 | All facts sourced. Uncertainty absent or hedged accurately. |
| Minor gaps | 13-17 | One soft inference, clearly plausible, nothing load-bearing. |
| Shaky | 7-12 | Load-bearing claim rests on an assumption. Title or company unconfirmed. |
| Contaminated | 0-6 | Any fabricated detail, contradicted field, or invented observation. |

Any single hallucinated fact caps this category at 5 and triggers hard failure H2.

### 2. ICP & persona fit — 15

Split 8 for account fit, 7 for persona fit.

- **Account (8)** — industry, size, business model, and market match the stated ICP. No ICP supplied: max 5, and note the assumption.
- **Persona (7)** — this title owns this problem and can act. Full marks need the right function *and* the right altitude. A CFO getting an email about developer onboarding friction scores 2 even at a perfect-fit company.

### 3. Trigger quality — 15

| Band | Points | Looks like |
| --- | --- | --- |
| Strong | 13-15 | Specific, dated, sourced, <60 days old, and the recipient plausibly cares. |
| Usable | 9-12 | Real and sourced but 60-120 days old, or account-level rather than personal. |
| Thin | 5-8 | True but generic: "you use HubSpot," "you're in fintech." A segment, not a trigger. |
| Absent | 0-4 | No why-now, or a trigger the recipient would not recognize as relevant. |

Deduct 4 if the trigger is >180 days old and presented as news. Deduct all but 2 if the trigger is unverifiable.

### 4. Relevance — 15

The chain from trigger → problem → offer.

- **13-15** — one-step chain, and the problem is one this persona already has a budget line or a headache for.
- **9-12** — two-step chain, still credible.
- **5-8** — the chain needs the reader to do the work, or the problem is real but not theirs.
- **0-4** — the offer is bolted onto the trigger. "Congrats on the funding, we do payroll software."

### 5. Clarity — 10

One idea. Concrete nouns. No sentence over ~20 words. Ambiguous pronouns, nested clauses, undefined acronyms, and "solutions/platform/enable" abstraction each cost 2.

### 6. Brevity — 10

Body word count, subject excluded:

| Words | Points |
| --- | --- |
| 45-75 | 10 |
| 76-90 | 7 |
| 91-100 | 5 |
| 101-130 | 3 |
| 131+ | 0 |
| Under 40 | 6 — usually too thin to give a reason to reply |

Deduct 2 more for any greeting paragraph that says nothing, and 2 for a signature block longer than the email.

### 7. Credibility — 10

- Named customer or a number with a source: 8-10.
- Honest qualitative proof — "we do this for three Series B fintechs" — with no invented specifics: 6-7.
- No proof, and no proof claimed: 5. Silence is neutral; this is the correct score for an early-stage sender with nothing to cite yet.
- Vague superlatives, "trusted by industry leaders," unattributed percentages: 0-3.

Fabricated logo, customer, or statistic: 0 and hard failure H2/H3.

### 8. CTA quality — 5

| Points | Ask |
| --- | --- |
| 5 | One question answerable in a word or a sentence. "Worth a look?" "Who owns this now?" |
| 3-4 | One specific but heavier ask: a 15-minute call, a named next step. |
| 1-2 | Calendar link in a first touch, 30-minute demo, or a multi-part question. |
| 0 | No ask, or two competing asks. |

Two primary CTAs also trigger hard failure H5.

---

## 2. Verdict assignment

Sum the eight categories, then apply in this order.

**Step 1 — band.**

| Score | Verdict |
| --- | --- |
| 0-49 | RAW |
| 50-69 | BLAND |
| 70-84 | OVERCOOKED if length or complexity is the dominant issue, otherwise BLAND |
| 85-100 | READY TO SEND |

*Dominant issue* in the 70-84 band means the combined loss across Clarity + Brevity is greater than the combined loss across Trigger quality + Relevance. Length is the biggest problem → OVERCOOKED. Otherwise the email is competent and forgettable → BLAND.

**Override below 70.** Assign OVERCOOKED instead of BLAND when the email is over 100 words or carries more than one CTA, *and* the Clarity + Brevity loss exceeds the Trigger + Relevance loss. A 180-word email with three asks is not bland; it is overcooked, and the fix is a knife rather than a rewrite. Without this override, piling on excess drags the score into the BLAND band and hides the actual diagnosis.

**Step 2 — hard failures.** Any hit blocks READY TO SEND regardless of score. Downgrade to the highest verdict the failure permits, listed below.

| # | Hard failure | Forced verdict |
| --- | --- | --- |
| H1 | Recipient identity unverified or contradicted by another field | RAW |
| H2 | Any hallucinated fact | RAW |
| H3 | Unsupported numerical claim | RAW |
| H4 | No offer — the reader cannot tell what is being proposed | RAW |
| H5 | More than one primary CTA | OVERCOOKED |
| H6 | Suppression / do-not-contact match | RAW, `send_status: BLOCKED` |
| H7 | Personalization drawn from sensitive personal information — health, religion, politics, sexuality, family, legal or financial distress, protected characteristics | RAW |
| H8 | Enrichment quality below 70 on a personalized email | RAW |

H7 covers the "I saw your post about your dad's surgery" genre. Cut it, do not soften it.

**Step 3 — final send check.**

| Output | When |
| --- | --- |
| `SEND` | READY TO SEND, no hard failures, enrichment ≥ 70. |
| `VERIFY FIRST` | Copy holds up, but identity, email status, or a cited fact needs confirming. |
| `RESEARCH FIRST` | Copy is fixable, but the data cannot support personalization yet. Enrichment < 70. |
| `BIN IT` | Suppression match, no ICP fit, or the premise is wrong. Rewriting will not save it. |

---

## 3. Enrichment quality score

Rate the record, not the copy. Eight components, 100 points.

| Component | Points | Full marks require |
| --- | --- | --- |
| Identity confidence | 20 | Name, title, and company confirmed together from one source, or two sources agreeing. |
| Email confidence | 15 | Work email, `verification_status: verified`, checked within 90 days. |
| Employment recency | 15 | Employment confirmed within 90 days. Tenure or start date present. |
| Trigger recency | 15 | Trigger dated within 60 days. |
| Source quality | 10 | Primary source: company site, filing, job board, official announcement, the person's own post. |
| Cross-source agreement | 10 | Two or more independent sources agree on title and company. |
| ICP confidence | 10 | Industry, size, and model all present and matching the ICP definition. |
| Persona confidence | 5 | Seniority and department present and matching the target persona. |

### Scoring each component

Award full points for confirmed, roughly half for present-but-unverified, zero for missing. Contradiction between two sources scores zero for that component *and* caps Identity confidence at 8.

| Band | Meaning | What you may produce |
| --- | --- | --- |
| 85-100 | Send-grade | Fully personalized email, READY TO SEND available. |
| 70-84 | Workable | Personalized email. Flag the weakest component in MISSING INGREDIENTS. |
| 50-69 | Account-level only | Draft using company facts only. No claims about the individual beyond title. Label `NOT READY`. |
| 0-49 | Data-gap report | Say what is missing and what would fix it. Offer the safest account-level draft, clearly labeled. |

Below 70 you must output, in this order:

1. **Data-gap report** — every component under half marks, with the specific field and the cheapest way to fill it.
2. **Safest possible draft** — account-level only, headed `NOT READY — <n>/100 enrichment`.
3. **The one input that unlocks personalization** — name it precisely. "A dated source for the Series B" beats "more research."

### Decay

Trigger recency decays and takes Trigger quality with it:

| Age | Trigger recency | Effect on email score |
| --- | --- | --- |
| 0-30 days | Full | None |
| 31-60 days | −3 | None |
| 61-120 days | −7 | Trigger quality capped at 12 |
| 121-180 days | −11 | Trigger quality capped at 8 |
| 180+ days | 0 | Trigger quality capped at 4, and calling it recent is hard failure H2 |

No `source_date` means unknown age. Treat as 121-180 and label the field `UNVERIFIED`.

---

## 4. Worked example

Record: VP Engineering at a 340-person B2B SaaS company. LinkedIn URL and verified work email present. Trigger: a job posting for four platform engineers, dated 22 days ago, sourced from the company careers page. ICP defined as 200-1000 employee B2B SaaS. Campaign supplies one public case study.

**Enrichment:** identity 20, email 15, employment 13, trigger recency 15, source quality 10, cross-source 8, ICP 10, persona 5 → **96/100.** Send-grade.

**Email quality** for a 64-word draft that opens on the four roles, names onboarding time as the problem, connects the two in one line, offers to cut ramp time, cites the case study with a specific before and after, and asks one question:

Data integrity 19 · ICP & persona 15 · Trigger 14 · Relevance 14 · Clarity 9 · Brevity 10 · Credibility 9 · CTA 5 → **95/100.**

No hard failures → **READY TO SEND**, final check `SEND`. The full email is Example 4 in `examples.md`.

Change one thing — swap the sourced case study for "we cut ramp time 60%" with nothing behind it — and Credibility drops to 0, Data integrity caps at 5, H3 fires, and the verdict becomes **RAW** at 72. One unsourced number costs 23 points and the send.
