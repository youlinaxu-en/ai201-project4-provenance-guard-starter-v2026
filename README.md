# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **Route (`app.py::submit`).** Receives `{text, creator_id}`. Rejects missing, empty, too-short or oversized text before any model runs, and adds a `content_id` (uuid), the only handle `/appeal` can use later. Rate limiting is added here in unit 8.
2. **Signal one (`detector.py::model_signal`).** gpt2 reads the first 400 tokens and adds a perplexity, squashed to 0–1 (higher = more AI). This is the "reads for meaning" opinion.
3. **Signal two (`stylometry.py::style_signal`).** Looks at the whole text as shapes: sentence-length spread, type-token ratio and punctuation density, each flipped and scaled so higher = more AI. This is the "doesn't read" opinion.
4. **Combining rule (`scoring.py::combine_signals`).** Turns two opinions into one `combined_score`. This is where a disagreement between signals either becomes "unsure" or gets overruled.
5. **Label mapping (`scoring.py::score_to_label`).** Applies the thresholds in `config.py` and adds `guess` (`human`/`unsure`/`ai`), a `confidence`, and plain-language text a writer can read.
6. **Audit log (`audit.py::log_decision`).** Appends one line with all nine fields and `status: decided`. Both signal scores are logged, not just the combined one.
7. **Response, then appeal.** The reader sees the label, and the response carries both signal scores for unit 8's tools. If they disagree, `/appeal` appends an entry and flips `status` to `under_review`; the original decision stays in the log.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** how predictable the text is to gpt2, as perplexity (first 400 tokens only), mapped to 0–1 where higher means more AI.

**Why that might differ between human and AI writing:** a generative model picks likely next words, so its output is easy for a similar model to predict. People pick odd, specific, abrupt words.

**What it can't see:** authorship. It only sees *common words in short, ordinary sentences*, which also describes second-language writers, younger writers and anyone writing plainly on purpose, so they score as AI. In the other direction, ornate prose full of rare words scores as human, so an AI told to write "elaborately" slips through. It also never sees anything past the first 400 tokens.

### Signal two — the style signal

**What it measures:** shape only: how much sentence length varies (stdev ÷ mean), how much vocabulary repeats (type-token ratio), and how dense and varied the punctuation is.

**Why that might differ between human and AI writing:** generated prose tends toward even, mid-length sentences and a narrow vocabulary. Human writing is lumpier.

**What it can't see:** meaning, so it is cheap to move without changing substance. Typos raise vocabulary variety, chopping sentences raises spread, and a pasted quotation or a few em dashes change punctuation. Type-token ratio also falls as text gets longer, so a long human essay can look repetitive. A one-sentence input has no spread, so it returns a neutral 0.5 and signal one carries it.

The two blind spots are mostly independent: plain human writing fools signal one, and light edits to AI text fool signal two.

### The false positive that sets the thresholds

**The writer:** a student writing in their second language submits a plain 150-word reflection they wrote themselves.

- **Scores (estimates, to be confirmed in Milestone 4):** signal one roughly 0.70–0.75 (common vocabulary, short ordinary sentences); signal two roughly 0.6–0.7 (even sentence lengths). Combined at 0.5/0.5 is about 0.68, over the 0.65 threshold: a wrongful "high-confidence AI".
- **What the label says:** on the placeholder numbers, an accusation.
- **What they can do:** `POST /appeal` with reasoning. It only sets `under_review`; nothing re-checks automatically, so a person has to read it.

Both signals fail in the same direction for this writer, so averaging doesn't rescue them. Consequences:

- Raise `AI_THRESHOLD` to about 0.80, deliberately hard to reach, because a wrong AI label costs a writer far more than a missed AI text costs us.
- Keep `HUMAN_THRESHOLD` near 0.35. The wide "unsure" band is where this writer should land.
- Word the "unsure" and "AI" labels as estimates with a visible appeal path, never as a verdict.

The cost is that more AI text gets through, and that falls on whoever relies on the label.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** the combined score is the average of the two signals, each counting half. When the signals disagree, the average lands in the middle, which is the "unsure" band: two methods disagreeing *is* uncertainty. A text only gets the AI label when **both** signals are high. That is deliberate: a wrong AI label costs a writer far more than a missed AI text costs the site.

**The numbers:**

- `combined = 0.5 × model_score + 0.5 × style_score` (`WEIGHT_MODEL_SIGNAL`, `WEIGHT_STYLE_SIGNAL` in `config.py`)
- Combined ≤ **0.35** → human. Combined ≥ **0.80** → AI. Between → unsure. I raised `AI_THRESHOLD` from the starter's 0.65 to 0.80 for the reason above.
- Inside `style_signal`, the three measures are weighted **0.8** sentence-length spread, **0.1** type-token ratio, **0.1** punctuation density. On my 25 sample files only the sentence-length spread separated AI from human; the other two showed no usable difference (AI text even had a *higher* type-token ratio), so they carry little weight.
- Signal one's midpoint (45) and steepness (1.6) are unchanged from the starter.

⚠️ The style signal's scaling ends were set by looking at the same 25 files I tested on, so scores on those files are optimistic. The real test is new input.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

`samples/human_01.txt` is a real person's Reddit comment with unusually even sentence lengths. The model signal reads it as human-ish (**0.426**) but the style signal reads it as AI-ish (**0.730**), because the style signal only sees that the sentences are all about the same length. The average is **0.578**, so the rule calls it "unsure": not accused, not cleared. The opposite split also happens: `samples/comment_09.txt` scores **0.603** on the model signal but only **0.063** on style (its sentences vary a lot), and averages to **0.333**, a "human" label.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. Nothing in it looked like the kind of writing automated tools produce. |
| unsure | 0.35 – 0.80 | We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal. |
| high-confidence AI | 0.80 – 1.00 | This looks like it was probably written by an AI tool. This is an estimate, not proof, and we can be wrong. If you wrote it yourself, please appeal and a person will read it. |

All three are reachable: in my tests `samples/comment_05.txt` scored 0.138 (human), `samples/formal_01.txt` scored 0.507 (unsure) and `samples/ai_02.txt` scored 0.813 (AI).

**Why I worded the "unsure" one this way:**
I talked with claude, and then deleted "plain and even" to avoid it was expalined as "your writing part is normal".


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

The text is the opening paragraph of *The Prisoner of Zenda* (1894, public domain), a formal piece of human writing; it is shortened to `...` below and in full in `samples/formal_01.txt`.

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "When I read a story, I skip the explanations; ...", "creator_id": "student-1"}'
```

```json
{
  "combined_score": 0.507,
  "confidence": 0.51,
  "content_id": "453eba19-c3ca-4e9f-b884-32222c80bc6c",
  "guess": "unsure",
  "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
  "model_score": 0.469,
  "status": "decided",
  "style_score": 0.545
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "453eba19-c3ca-4e9f-b884-32222c80bc6c", "reasoning": "I wrote this myself for class."}'
```

```json
{
  "content_id": "453eba19-c3ca-4e9f-b884-32222c80bc6c",
  "message": "Thank you. A person will read your appeal. Your original result stays on record.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.507,
      "content_id": "453eba19-c3ca-4e9f-b884-32222c80bc6c",
      "creator_id": "student-1",
      "guess": "unsure",
      "label": "We can't tell. Our checks gave mixed results, so this is not a finding that anyone used AI. If you wrote it yourself, you don't need to do anything. If you'd like a person to look at it, you can appeal.",
      "model_score": 0.469,
      "status": "decided",
      "style_score": 0.545,
      "timestamp": "2026-11-04T23:46:51+00:00"
    },
    {
      "content_id": "453eba19-c3ca-4e9f-b884-32222c80bc6c",
      "creator_id": "student-1",
      "event": "appeal",
      "reasoning": "I wrote this myself for class.",
      "status": "under_review",
      "timestamp": "2026-11-04T23:46:52+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*Ask AI to judge the comment work or not
- *What came back:* Claude checked the topic of each comments and give opinions
- *What I changed:*Some unrealted opinions were deleted in collection part

**Moment 2**

- *What I asked for:* Ask Claude to check errors 
- *What came back:* it gives me some feedback about the signal history 
- *What I changed:* I checked each of them to make sure we dont't have divergence on that

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
