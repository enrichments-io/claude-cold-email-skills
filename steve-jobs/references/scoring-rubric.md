# Reply-intent scoring rubric

100 points across three dimensions. The score predicts one thing: whether this person types a reply. It does not predict whether they buy, and it is not a measure of how good the writing is.

Ship at 75 or above. Below 75, name the missing input instead of shipping with a caveat.

## Relevance — 40 points

Would the recipient recognize this email as being about them specifically?

| Points | What it looks like |
| --- | --- |
| 36-40 | Names a specific event at their company, and states a consequence of it that the recipient would agree with. Could not be sent to any other company without rewriting. |
| 28-35 | Names a specific event, but the consequence is generic or slightly off for their role. |
| 20-27 | Uses a real fact about them, but one that is public, obvious, and true of their whole segment — headcount, funding, industry, tech stack. |
| 10-19 | Persona-level relevance only. Right title, nothing else. |
| 0-9 | Could be sent to anyone. Sending this is worse than sending nothing, because it identifies itself as bulk. |

The dividing line between 27 and 28 is the one that matters. Everything at 27 and below is a mail merge with extra steps.

## Clarity — 30 points

Can the recipient understand the whole email in one pass on a phone?

| Points | What it looks like |
| --- | --- |
| 27-30 | One point. Plain words. Every sentence under about 15 words. Nothing has to be re-read. |
| 21-26 | One point, but one sentence is doing too much or one term is category jargon. |
| 14-20 | Two points competing, or the reader has to work out which sentence is the important one. |
| 7-13 | Feature list, or three value propositions, or the point arrives after the third sentence. |
| 0-6 | The recipient cannot tell what is being offered or why they were emailed. |

Deduct 3 points for any sentence that restates the previous one, and 5 for any sentence introducing the sender before the email has said anything about the recipient.

## Reply effort — 30 points

How much work is it to answer?

| Points | What it looks like |
| --- | --- |
| 27-30 | One question, answerable in one word, with no decision attached. "Worth seeing?" |
| 21-26 | One question, but answering implies a small commitment — sharing a number, agreeing to receive something. |
| 14-20 | The ask requires a choice between options, or asks them to pick a time. |
| 7-13 | Calendar link, or a request for a 15- or 30-minute meeting in a first touch. |
| 0-6 | Two asks, an ask buried mid-email, or no clear ask at all. |

A calendar link in a first touch caps this dimension at 13 regardless of how the rest reads. You are asking a stranger to spend thirty minutes before they have spent thirty seconds.

## Automatic failures

These score 0 overall regardless of the dimensions, because they are not weak emails, they are emails that damage the sender:

- A fabricated fact — an invented number, customer, funding round, or event.
- Arithmetic that does not compute from the supplied figures.
- A claim about the product that the input does not support.
- A banned opener surviving into the final draft.
- Impersonation: text written as if from Steve Jobs, a quote attributed to him, or a signature in his name.
- Over 80 words in the body.

## Reading the score

**90-100.** Send it. The trigger is real, the consequence lands, and the ask is free.

**75-89.** Send it, and note which dimension was lowest — that is the input to improve next time, not the copy.

**60-74.** Do not send. The email is competent and forgettable. Almost always the trigger is the problem; go find a better one rather than editing sentences.

**Below 60.** Do not send, and do not edit. Nothing at this level is fixable at the copy layer.

## Calibrating on your own list

Score twenty emails you already sent — ten that got replies and ten that did not — before trusting the rubric on new ones. If the replied-to emails are not scoring materially higher, the weights are wrong for your market, and the fix is to shift points toward whichever dimension actually separated them. Move 5 points at a time and re-score all twenty.
