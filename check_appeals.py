#!/usr/bin/env python3
"""
Tests criterion 4: an appeal always changes status and is always recorded.

    python app.py                 # one terminal
    python check_appeals.py       # another

scenarios.py can't test this: an appeal needs a content_id that only exists
after a submission. So this submits 10 texts, appeals each, and checks:

  - every appeal returns 200 with status "under_review"
  - every appeal adds exactly ONE `event: appeal` line to the audit log
  - the original decision line is unchanged
  - an unknown content_id returns 404 and adds nothing to the log
"""

import json
import sys
from pathlib import Path

import requests

import config

URL = f"http://{config.HOST}:{config.PORT}"
SAMPLES = Path(__file__).parent / "samples"


def log_lines() -> list[dict]:
    return requests.get(f"{URL}/log").json()["entries"]


def main() -> int:
    files = sorted(SAMPLES.glob("comment_*.txt"))[:10]
    failures = []

    for n, path in enumerate(files, 1):
        creator = f"appeal_check_{n}"
        sub = requests.post(f"{URL}/submit", json={
            "text": path.read_text(encoding="utf-8").strip(), "creator_id": creator})
        if sub.status_code != 200:
            failures.append(f"{path.name}: submit returned {sub.status_code}")
            continue
        content_id = sub.json()["content_id"]

        before = log_lines()
        original = next(e for e in before if e.get("content_id") == content_id)

        resp = requests.post(f"{URL}/appeal", json={
            "content_id": content_id, "reasoning": f"Appeal check {n}: I wrote this."})

        after = log_lines()
        mine = [e for e in after if e.get("content_id") == content_id]
        appeals = [e for e in mine if e.get("event") == "appeal"]
        same_original = next(e for e in after if e.get("content_id") == content_id) == original

        ok = (resp.status_code == 200
              and resp.json().get("status") == "under_review"
              and len(appeals) == 1
              and len(after) == len(before) + 1
              and same_original)
        print(f"  {path.name:16} appeal {resp.status_code}  status={resp.json().get('status')}  "
              f"appeal lines={len(appeals)}  original unchanged={same_original}  {'ok' if ok else 'FAIL'}")
        if not ok:
            failures.append(f"{path.name}: appeal check failed")

    before = len(log_lines())
    bad = requests.post(f"{URL}/appeal", json={
        "content_id": "not-a-real-id", "reasoning": "x"})
    after = len(log_lines())
    ok = bad.status_code == 404 and after == before
    print(f"  unknown id        appeal {bad.status_code}  log grew by {after - before}  {'ok' if ok else 'FAIL'}")
    if not ok:
        failures.append("unknown content_id was not a clean 404")

    print()
    if failures:
        print("FAILED:\n  " + "\n  ".join(failures))
        return 1
    print(f"All {len(files)} appeals changed status and were recorded; the unknown id was refused cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
