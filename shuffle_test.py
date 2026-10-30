#!/usr/bin/env python3
"""
Arrange a CUET test in exam order — mechanical only (no content changes).

The NTA paper mixes units at random. This tool:
  * shuffles the questions inside each section (units mixed),
  * keeps every case/passage set (same `case_id`) together, in its original
    internal order, at the end of its section (as in NTA papers),
  * keeps choice sections (e.g. Accountancy B1/B2) separate and in place,
  * retries until no answer letter repeats more than 3 times in a row on any
    attempt path,
  * renumbers question ids (…-Q01, …-Q02) to match the new positions.

The seed is the test number, so re-running gives the same order.
Usage: python3 shuffle_test.py "CUET/Accountancy/CUET ACCOUNTANCY TEST 2.json" [...]
IAT, NEST and COMEDK are deliberately rejected: their authored order and diagram IDs are fixed.
"""
import json, random, re, sys
from pathlib import Path


def max_run(keys):
    return max((len(m.group(0)) for m in re.finditer(r"(.)\1*", keys)), default=0)


def arrange(questions, rng):
    groups, singles = {}, []
    for q in questions:
        if q.get("case_id"):
            groups.setdefault(q["case_id"], []).append(q)
        else:
            singles.append(q)
    rng.shuffle(singles)
    return singles + [q for g in groups.values() for q in g]


def shuffle_file(path):
    data = json.load(open(path, encoding="utf-8"))
    # These series are authored in final order; IDs also identify diagram assets.
    series = str(data.get("series_id", "")).upper()
    exam = str(data.get("exam", "")).upper()
    folders = {part.upper() for part in Path(path).parts}
    if (series.startswith(("IAT", "NEST", "COMEDK"))
            or folders.intersection({"IISER", "NISER", "COMEDK"})
            or re.search(r"\b(?:IISER|IAT|NISER|NEST|COMEDK)\b", exam)):
        sys.exit(f"{path}: shuffling is disabled for IAT, NEST and COMEDK; preserve final order and diagram references")
    qs = data["questions"]
    order = []
    for q in qs:
        s = q.get("section", "_all")
        if s not in order:
            order.append(s)
    common = data.get("common_sections") or [s for s in order if s not in data.get("optional_sections", [])]
    paths = [common + [o] for o in data.get("optional_sections", [])] or [order]
    rng = random.Random(1000 + int(data.get("test_number", 0)))
    for _ in range(5000):
        by_sec = {s: arrange([q for q in qs if q.get("section", "_all") == s], rng) for s in order}
        if all(max_run("".join(q["correct_option"] for s in p for q in by_sec[s])) <= 3 for p in paths):
            break
    else:
        sys.exit(f"{path}: could not avoid long answer runs; rebalance the key")
    new = [q for s in order for q in by_sec[s]]
    for i, q in enumerate(new, 1):
        q["id"] = re.sub(r"Q\d+$", f"Q{i:02d}", q["id"])
    data["questions"] = new
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(path, "a", encoding="utf-8").write("\n")
    print(f"{path}: arranged {len(new)} questions")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        shuffle_file(p)
