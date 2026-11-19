"""Build or verify COMEDK reservations. This tool never writes questions or angles."""
import argparse
import csv
import io
import json
from itertools import zip_longest
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLUEPRINTS = ROOT / "docs" / "blueprints"
SUBJECTS = "PCM"
CLASS_COUNTS = {11: 20, 12: 40}
TIERS = ["easy"] * 9 + ["medium"] * 39 + ["hard"] * 12
FOCUSES = [
    "Foundational model choice", "Units and conventions", "Classification boundaries",
    "Algebraic constraints", "Conditions and applicability", "Interpreting a representation",
    "Comparing outcomes", "Connecting two short steps", "Contrasting plausible methods",
    "Changing a physical or chemical condition", "Selecting a valid statement",
    "Finding an admissible input", "Interpreting a limiting case", "Diagnosing a common error",
    "Short symbolic reasoning", "Identifying the decisive evidence", "Checking a chained inference",
    "Mixed pacing", "Endpoint and sign decisions", "Comparing neighbouring cases",
    "Tight time-budget challenge", "Using a diagram or graph efficiently",
    "Checking exceptions and assumptions", "Verifying a result", "Full timed dress rehearsal",
]


def load_scope():
    groups = defaultdict(list)
    for line in Path(__file__).with_name("scope.txt").read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        subject, grade, pages, chapter, anchors = line.split("|")
        grade = int(grade)
        for anchor in anchors.split(";"):
            group = groups[subject, grade]
            ident = f"{subject}{grade}-{len(group) + 1:03}"
            group.append(dict(anchor_id=ident, subject=subject, class_level=grade,
                              pdf_page=pages, chapter=chapter, anchor=anchor.strip()))
    # Interleave chapter queues so a contiguous quota still samples a broad range.
    for key, group in groups.items():
        chapters = defaultdict(list)
        for row in group:
            chapters[row["chapter"]].append(row)
        groups[key] = [row for layer in zip_longest(*chapters.values())
                       for row in layer if row is not None]
    return groups


def csv_text(rows):
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def build():
    groups = load_scope()
    uses = defaultdict(list)
    questions = []
    overview = []
    chapter_counts = Counter()
    for test, focus in enumerate(FOCUSES, 1):
        tier_phase = (test - 1) * 11
        for section, subject in enumerate(SUBJECTS):
            picks = []
            for grade, quota in CLASS_COUNTS.items():
                pool = groups[subject, grade]
                assert len(pool) >= quota
                offset = (test - 1) * quota
                picks.append([pool[(offset + i) % len(pool)] for i in range(quota)])
            # Interleave classes before authorship. IDs and their order freeze at authoring.
            ordered = [row for i in range(20)
                       for row in (picks[1][2 * i], picks[0][i], picks[1][2 * i + 1])]
            for position, row in enumerate(ordered, 1):
                anchor = row["anchor_id"]
                visit = len(uses[anchor]) + 1
                slot = section * 60 + position
                ident = f"COMEDK27-T{test:02}-Q{slot:03}"
                uses[anchor].append(ident)
                questions.append(dict(test=test, question=slot, id=ident, **row,
                                      anchor_visit=visit, difficulty_target=TIERS[(position * 7 + tier_phase + section * 3) % 60],
                                      paper_focus=focus, angle_status="unapproved", status="reserved"))
                chapter_counts[subject, row["class_level"], row["chapter"]] += 1
        stage = "Foundation" if test <= 8 else "Mixed application" if test <= 17 else "Exam rehearsal"
        overview.append(dict(test=test, stage=stage, pacing_focus=focus,
                             physics=60, chemistry=60, mathematics=60, class_11=60,
                             class_12=120, easy=27, medium=117, hard=36, minutes=180,
                             reservations=180, authored=0))
    scope = [dict(**row, reservations=len(uses[row["anchor_id"]]),
                  first_reserved_test=int(uses[row["anchor_id"]][0].split("-T")[1][:2]),
                  first_reserved_id=uses[row["anchor_id"]][0], evidence_status="planned",
                  evidence_question_ids="") for pool in groups.values() for row in pool]
    assert len(questions) == len({q["id"] for q in questions}) == 4500
    for test in range(1, 26):
        for subject in SUBJECTS:
            rows = [r for r in questions if r["test"] == test and r["subject"] == subject]
            assert len(rows) == len({r["anchor_id"] for r in rows}) == 60
            assert Counter(r["class_level"] for r in rows) == CLASS_COUNTS
            assert Counter(r["difficulty_target"] for r in rows) == Counter(TIERS)
    assert all(r["reservations"] for r in scope)
    summary = dict(tests=25, reservations=len(questions), approved_angles=0, authored_questions=0,
                   coverage_anchors=len(scope),
                   anchors_by_subject=dict(Counter(r["subject"] for r in scope)),
                   chapter_class_groups=len(chapter_counts),
                   minimum_chapter_reservations=min(chapter_counts.values()),
                   all_anchors_first_assigned_by=max(r["first_reserved_test"] for r in scope),
                   minimum_anchor_reservations=min(r["reservations"] for r in scope))
    return {
        "comedk_25_test_plan.csv": csv_text(overview),
        "comedk_25_test_slots.csv": csv_text(questions),
        "comedk_syllabus_coverage.csv": csv_text(scope),
        "comedk_plan_check.json": json.dumps(summary, indent=2) + "\n",
    }, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Create the un-authored baseline schedules.")
    args = parser.parse_args()
    outputs, summary = build()
    if args.write and list((ROOT / "COMEDK").glob("COMEDK UGET TEST *.json")):
        raise SystemExit("Canonical papers exist. Reconcile the live plan instead of regenerating reservations.")
    for filename, content in outputs.items():
        path = BLUEPRINTS / filename
        if args.write:
            path.write_text(content)
        elif not path.is_file() or path.read_text() != content:
            raise SystemExit(f"Baseline mismatch: {path.relative_to(ROOT)}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
