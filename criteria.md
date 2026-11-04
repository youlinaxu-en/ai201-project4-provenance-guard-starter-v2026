# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Ordinary human writing is rarely called AI

Of 10 pieces of human-written text (real Reddit comments and posts on different
topics, 100–300 words each, no typos added or removed by me), at most 1 is
labeled high-confidence AI. This must hold in each of three trials, not on average.

**Why this target:** On a writing site a wrong accusation costs the writer far more
than a missed detection costs the site, so I allow 1 in 10 and no more. I don't
set it at 0 because I can't verify a two-signal system gets to zero, but 1 in 10
is already a number I'd have to defend to the person it hit.

**Where the 10 come from:** `samples/comment_01.txt` to `comment_10.txt`, each
with its source recorded in `samples/SOURCES.md`. I did not write them, so I
can't prove none are AI-written; I chose posts with specific personal detail and
no template phrasing to make that unlikely.

---

## 2. Plain, conventional writing is never labeled AI

Of 5 pieces of plainly written human text (short sentences, common words, the way
a second-language writer or a younger student writes), 0 are labeled
high-confidence AI, and at least 3 land in "unsure" or "human". This must hold in
all three trials.

**Why this target:** Signal one scores common words in short sentences as
machine-like, so this is the writer my system is most likely to wrongly accuse
and the one with the least room to argue back. I expect to struggle with this one,
which is why it is a separate criterion and zero is the target. A criterion 1 pass
could otherwise hide a failure here, because my own writing isn't plain.

---

## 3. AI and human text score apart, and all three labels are reachable

Across 5 clearly-AI and 5 clearly-human pieces, the mean combined score of the AI
pieces is at least 0.30 higher than the mean of the human pieces, and no
clearly-AI piece gets the "human" label. Across all submissions in my calibration
set, each of the three labels (human, unsure, AI) is produced at least once.

**Why this target:** A 0.30 gap is wide enough that the unsure band (0.35–0.80) can
sit between the groups instead of swallowing both. A system that can't separate
obvious cases can't be trusted on hard ones. Calling clearly-AI text "human" is
allowed to happen occasionally (that is the cheap error), but a label that
nothing can reach is a broken label, so each must appear at least once.

---

## 4. An appeal always changes status and is always recorded

For 10 appeals on 10 real `content_id` values, all 10 return 200 with
`status: "under_review"` and add exactly one `event: "appeal"` line to the audit
log, and the original decision line is unchanged. For an unknown `content_id`,
the response is 404 and nothing is added to the log.

**Why this target:** The appeal is the only thing standing between a wrong
accusation and nothing at all, so there is no acceptable failure rate: 10 out of
10, not 9. The unknown-id case matters because a typo that silently "succeeds"
tells a writer their appeal was filed when it wasn't.

---

## 5. Bad input is refused cleanly and never crashes the service

For each of these 7 inputs to `/submit`, the response is a 4xx with a JSON body
containing an `error` code, never a 500: missing `text`, empty `text`,
whitespace-only `text`, non-string `text`, a body that is a bare JSON list,
missing `creator_id`, and 25,000 characters of text. Each refusal appears in the
audit log, and `/ping` still answers 200 afterwards.

**Why this target:** A crash on malformed input is one of the most common real
failures, and the attack set in unit 8 will send exactly these. Seven specific
inputs with a specific status class is checkable, which "handles bad input
gracefully" is not. Logging the refusals means an attack can't hide as an absence.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
