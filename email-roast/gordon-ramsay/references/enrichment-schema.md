# Enrichment Schema

Everything the skill accepts, what it is called elsewhere, and what happens when it is absent. Normalize input to these names before doing anything else. `scripts/validate-input.py` implements the same aliases and the same rules.

---

## 1. Accepted input shapes

All four normalize to the same record set.

| Shape | Example | Handling |
| --- | --- | --- |
| Unstructured notes | "Sarah Chen, VP Eng at Northwind, they just raised a B" | Parse into fields. Anything you inferred rather than read is `UNVERIFIED`. |
| JSON object | `{"campaign": {...}, "prospects": [...]}` | Canonical form. Also accepts a bare prospect object or a bare array. |
| CSV / TSV | Header row + rows | Map headers via the alias table. Unmapped columns go to `custom_fields`. |
| Pasted table | Markdown or spreadsheet paste | Same as CSV. First row is the header unless obviously data. |

Canonical JSON envelope:

```json
{
  "campaign": {
    "icp": "B2B SaaS, 200-1000 employees, product-led",
    "problem": "New engineers take 6+ weeks to ship independently",
    "offer": "Onboarding automation that cuts ramp time",
    "proof": "Cut ramp from 6 weeks to 11 days at Meridian (public case study)",
    "sender_credibility": "Former platform lead at Stripe",
    "cta": "Ask who owns onboarding today",
    "tone": "direct, peer-to-peer",
    "max_words": 75,
    "prohibited_claims": ["SOC 2 certified", "any named customer besides Meridian"],
    "suppression_list": ["competitor.com", "existing-customer.com"]
  },
  "prospects": [
    {
      "record_id": "clay_00417",
      "first_name": "Sarah",
      "last_name": "Chen",
      "job_title": "VP Engineering",
      "seniority": "vp",
      "department": "engineering",
      "location": "Austin, TX",
      "linkedin_url": "https://www.linkedin.com/in/sarahchen",
      "email": "sarah.chen@northwind.io",
      "verification_status": "verified",
      "company_name": "Northwind Systems",
      "domain": "northwind.io",
      "industry": "B2B SaaS",
      "employee_count": 340,
      "estimated_revenue": "$40M-60M",
      "funding_stage": "series_b",
      "tech_stack": ["AWS", "Datadog", "GitHub Actions"],
      "business_model": "subscription",
      "target_market": "mid-market",
      "signals": [
        {
          "type": "job_posting",
          "summary": "Four open platform engineering roles",
          "source_url": "https://northwind.io/careers",
          "source_date": "2026-07-04",
          "confidence": 0.9
        }
      ],
      "suppressed": false
    }
  ]
}
```

`signals` may also be flat fields — `recent_funding`, `recent_hiring`, `leadership_change`, `job_posting`, `product_launch`, `expansion`, `technology_adoption`, `website_change`, `linkedin_activity`, `company_news`, `intent_signal` — each with its own `_source_url` and `_source_date`. Both forms are equivalent; the array is preferred because it carries dates cleanly.

---

## 2. Recipient fields

| Canonical | Type | Required | Aliases |
| --- | --- | --- | --- |
| `record_id` | string | yes (batch) | `id`, `row_id`, `uuid`, `crm_id`, `contact_id`, `Record ID` |
| `first_name` | string | yes | `firstName`, `first`, `fname`, `given_name`, `First Name` |
| `last_name` | string | no | `lastName`, `last`, `lname`, `surname`, `family_name`, `Last Name` |
| `job_title` | string | yes | `title`, `jobTitle`, `position`, `role`, `Job Title` |
| `seniority` | enum | no | `level`, `seniority_level` |
| `department` | string | no | `function`, `team`, `dept` |
| `location` | string | no | `city`, `geo`, `region`, `country` |
| `linkedin_url` | url | no | `linkedin`, `li_url`, `linkedin_profile`, `LinkedIn URL`, `person_linkedin` |
| `email` | email | no* | `work_email`, `email_address`, `business_email`, `Email` |
| `verification_status` | enum | no | `email_status`, `email_verification`, `verification`, `deliverability` |

\* At least one of `email`, `domain`, or `linkedin_url` must be present, or the record cannot be resolved at all.

`seniority` accepts: `c_level`, `vp`, `director`, `manager`, `senior`, `individual_contributor`. Aliases `cxo`/`c-suite`/`executive` → `c_level`; `head`/`head_of` → `director`; `ic`/`staff` → `individual_contributor`.

`verification_status` accepts: `verified`, `catch_all`, `risky`, `unknown`, `invalid`, `unverified`. Aliases: `valid`/`deliverable`/`ok`/`safe` → `verified`; `accept_all` → `catch_all`; `undeliverable`/`bounced`/`bad` → `invalid`. Anything else is an error — an unrecognized status silently treated as good is how bounces happen.

Only `verified` earns full Email confidence. `catch_all` and `risky` score half. `invalid` blocks the send outright.

---

## 3. Company fields

| Canonical | Type | Required | Aliases |
| --- | --- | --- | --- |
| `company_name` | string | yes | `company`, `account`, `organization`, `org`, `employer`, `Company` |
| `domain` | domain | no* | `website`, `company_domain`, `url`, `company_website`, `Domain` |
| `industry` | string | no | `sector`, `vertical`, `naics_description` |
| `employee_count` | int | no | `headcount`, `size`, `employees`, `company_size` |
| `estimated_revenue` | string/int | no | `revenue`, `arr`, `annual_revenue` |
| `funding_stage` | enum | no | `stage`, `last_round`, `funding` |
| `tech_stack` | array | no | `technologies`, `technology_stack`, `tools`, `stack` |
| `business_model` | string | no | `model`, `gtm_model` |
| `target_market` | string | no | `market`, `segment`, `customer_segment` |
| `company_linkedin_url` | url | no | `company_linkedin`, `org_linkedin` |

`employee_count` given as a band (`"201-500"`) is kept as a string and used only for ICP banding, never quoted to the recipient. `funding_stage` accepts `pre_seed`, `seed`, `series_a` through `series_f`, `growth`, `public`, `bootstrapped`, `pe_backed`.

---

## 4. Signal fields

Each signal:

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `type` | enum | yes | One of the eleven signal types listed in §1. |
| `summary` | string | yes | One sentence, factual. Not marketing copy lifted from their site. |
| `source_url` | url | strongly | Absent → signal is `UNVERIFIED` and cannot anchor the opener. |
| `source_date` | ISO date | strongly | Absent → treated as 121-180 days old. See the decay table in `scoring-rubric.md`. |
| `confidence` | float 0-1 | no | Provider score. Absent assumes 0.5. |

A signal with neither `source_url` nor `source_date` is a rumor. It may inform which problem you lead with; it may not be stated as fact to the recipient.

---

## 5. Campaign fields

| Canonical | Type | Required | Aliases |
| --- | --- | --- | --- |
| `icp` | string | yes | `icp_definition`, `target_icp`, `ideal_customer_profile` |
| `problem` | string | yes | `pain`, `pain_point`, `problem_addressed`, `use_case` |
| `offer` | string | yes | `value_prop`, `solution`, `pitch`, `what_we_do` |
| `cta` | string | yes | `desired_cta`, `ask`, `call_to_action`, `next_step` |
| `proof` | string | no | `case_study`, `social_proof`, `evidence`, `results` |
| `sender_credibility` | string | no | `sender_bio`, `credibility`, `about_sender` |
| `tone` | string | no | `voice`, `style` |
| `max_words` | int | no | `word_limit`, `max_length`. Default 75. |
| `prohibited_claims` | array | no | `banned_claims`, `legal_restrictions`, `do_not_say` |
| `suppression_list` | array | no | `suppressed_domains`, `dnc_list`, `exclusions` |

Missing `offer` is hard failure H4 — there is no email to write. Missing `icp` costs ICP fit points and forces a stated assumption. Missing `proof` is fine: write without proof rather than inventing it.

---

## 6. Suppression

A record is suppressed when any of these is true:

- `suppressed`, `do_not_contact`, `opted_out`, `unsubscribed`, or `dnc` is `true`
- `suppression_status` is one of `suppressed`, `dnc`, `do_not_contact`, `opted_out`, `unsubscribed`, `blocked`
- `domain` or the email domain appears in `campaign.suppression_list`

Consequences: hard failure H6, verdict RAW, `send_status: BLOCKED`, final check `BIN IT`, and **no email body is generated**. Do not write copy "in case they resubscribe." Ambiguous suppression is treated as suppressed.

---

## 7. Confidence handling

Providers express confidence differently. Normalize, then map to the enrichment components in `scoring-rubric.md`.

| Input | Normalized | Treated as |
| --- | --- | --- |
| `0.0-1.0` float | as-is | ≥0.85 confirmed · 0.5-0.84 present-but-unverified · <0.5 unusable as fact |
| `0-100` int | ÷100 | same |
| `high` / `medium` / `low` | 0.9 / 0.6 / 0.3 | same |
| `A` / `B` / `C` / `D` grade | 0.95 / 0.75 / 0.5 / 0.25 | same |
| absent | 0.5 | present-but-unverified |

Confidence below 0.5 on a field means that field may guide targeting but may never appear as a stated fact in the email.

**Contradictions** — two sources disagreeing on title or company — score zero for cross-source agreement, cap Identity confidence at 8, and fire hard failure H1. Never pick the more flattering version. Report both and ask.

---

## 8. Missing-data behavior

| Missing field | Behavior |
| --- | --- |
| `first_name` | No greeting name. "Hi there" is acceptable; guessing from an email handle is not. |
| `job_title` | Persona confidence 0. No claims about what they own. Account-level only. |
| `company_name` | Cannot write. Return a data-gap report. |
| `email` | Copy still valid; final check is `VERIFY FIRST` at best. |
| `verification_status` | Treat as `unverified`. Half Email confidence. |
| all signals | No why-now. Trigger quality ≤4. Use account-level relevance — the ICP-wide problem stated honestly, never a fake personal observation. |
| `source_url` | Signal is `UNVERIFIED`. May shape the angle, may not be asserted. |
| `source_date` | Treated as 121-180 days old. Never described as "recent" or "just." |
| `proof` | Omit the proof sentence. Credibility 5, not 0. |
| `icp` | Infer from campaign context, state the assumption in MISSING INGREDIENTS, cap ICP fit at 5. |

The two irreducible fields are `company_name` and `campaign.offer`. Everything else has a documented degradation path.

---

## 9. Field labels in output

Use exactly these in MISSING INGREDIENTS so batch output stays greppable:

- `MISSING` — not in the record.
- `UNVERIFIED` — present, no source or confidence below 0.5.
- `STALE` — sourced but older than 120 days.
- `CONTRADICTED` — two sources disagree.
- `BLANK` — key present, value empty, whitespace, `null`, `"N/A"`, or an unrendered merge tag like `{{first_name}}`.

Format: `field_name — LABEL — what it costs and the cheapest fix.`

```
signals[0].source_date — MISSING — the funding claim can't be called recent; check the press release date.
verification_status — UNVERIFIED — send check drops to VERIFY FIRST; run it through your verifier.
```
