"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

# type_token_ratio looks at this many words, so texts of different lengths
# are measured on the same footing.
TTR_WINDOW = 70

# How each raw measure maps onto a 0-1 "AI-like" score: a value at or beyond
# the *_AI end scores 1.0, at or beyond the *_HUMAN end scores 0.0, linear
# between. These ends were set by looking at the 25 files in samples/ - so they
# are calibrated on the same texts they are tested on. Treat results on those
# files as optimistic.
SPREAD_AI, SPREAD_HUMAN = 0.15, 0.60    # sentence-length coefficient of variation
TTR_AI, TTR_HUMAN = 0.65, 0.90          # unique words / words, first 70 words
PUNCT_AI, PUNCT_HUMAN = 0.03, 0.15      # non-full-stop punctuation per word

# Spread did nearly all the separating on the samples; TTR and punctuation
# showed no usable difference, so they carry little weight.
WEIGHT_SPREAD, WEIGHT_TTR, WEIGHT_PUNCT = 0.8, 0.1, 0.1


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    # One sentence has no spread. Return 0.0 here; style_signal() checks the
    # sentence count itself and leaves this measure out rather than treating
    # "can't tell" as "very AI-like".
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean  # coefficient of variation


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    # Only the first TTR_WINDOW words count. TTR falls as text gets longer, so
    # measuring every text over the same number of words keeps a 90-word
    # comment and a 250-word one comparable.
    tokens = words(text)[:TTR_WINDOW]
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    n_words = len(words(text))
    if n_words == 0:
        return 0.0
    # Everything except the full stop: commas, semicolons, colons, dashes,
    # brackets, quotes, apostrophes, question and exclamation marks. Full stops
    # just count sentences, which sentence_length_spread already covers.
    marks = re.findall(r"[,;:!?()\"'“”‘’—–…-]", text)
    return len(marks) / n_words


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    # A one-sentence input has no spread to measure. Say "can't tell" (0.5)
    # and let signal one carry it, instead of calling it AI-like.
    if len(sentences(text)) < 2:
        return 0.5

    def clamp(x: float) -> float:
        return min(max(x, 0.0), 1.0)

    # Each measure becomes a 0-1 "how AI-like" score, higher = more AI.
    # Low spread -> AI-like (even sentences). Low TTR -> AI-like (narrow
    # vocabulary). Low punctuation -> AI-like (flat, uncomplicated).
    spread_score = clamp((SPREAD_HUMAN - sentence_length_spread(text)) / (SPREAD_HUMAN - SPREAD_AI))
    ttr_score = clamp((TTR_HUMAN - type_token_ratio(text)) / (TTR_HUMAN - TTR_AI))
    punct_score = clamp((PUNCT_HUMAN - punctuation_density(text)) / (PUNCT_HUMAN - PUNCT_AI))

    score = (
        WEIGHT_SPREAD * spread_score
        + WEIGHT_TTR * ttr_score
        + WEIGHT_PUNCT * punct_score
    )
    return round(clamp(score), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
