"""
What your test runs. <- UNIT 8, MILESTONE 3

Each of the five criteria in criteria.md has something run against it here.
`run_eval.py` runs everything in SCENARIOS three times.

    criterion 1  human comments      10 real Reddit comments, none should be called AI (at most 1)
    criterion 2  plain writing       5 plain human texts, none should be called AI
    criterion 3  spread check        5 clearly-AI + 5 clearly-human, to see the gap and all three labels
    criterion 4  the appeal path     NOT HERE. It needs a submission first and then an appeal
                                     against the content_id that came back, which this file
                                     can't express. It is tested by `check_appeals.py`.
    criterion 5  bad input           7 malformed or oversized requests, sent exactly as written

Texts are read from samples/, where SOURCES.md says where each came from.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point.

run_eval.py builds creator_ids from the first 12 characters of the scenario name,
so those 12 characters must differ between scenarios.
"""

from pathlib import Path

SAMPLES = Path(__file__).parent / "samples"


def _read(pattern: str) -> list[str]:
    """Every sample file matching a pattern, in name order."""
    return [p.read_text(encoding="utf-8").strip() for p in sorted(SAMPLES.glob(pattern))]


SCENARIOS = [
    {
        "name": "human comments",
        "criterion": 1,
        "texts": _read("comment_*.txt"),
    },
    {
        "name": "plain writing",
        "criterion": 2,
        "texts": _read("plain_*.txt"),
    },
    {
        # The first five are clearly AI, the last five clearly human.
        "name": "spread check",
        "criterion": 3,
        "texts": _read("ai_*.txt") + _read("human_*.txt"),
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                          # no text field
            {"text": "", "creator_id": "eval_bad_empty"},                # empty
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},  # whitespace only
            {"text": 12345, "creator_id": "eval_bad_number"},            # not a string
            ["some", "list"],                                            # body is a list
            {"text": "Some writing with nobody attached to it, so the service has no creator to count."},
            {"text": "word " * 5000, "creator_id": "eval_bad_huge"},     # 25,000 characters
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            # (a bare list is allowed here on purpose: a body that isn't an
            # object is one of the cases being tested)
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
