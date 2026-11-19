"""Assemble authored pilot rows. Never change the option ordering after initial freeze."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "COMEDK"
SUBJECTS = {"P": "Physics", "C": "Chemistry", "M": "Mathematics"}
FIGURES = {
    14: ("graph", "Force–position plot: 4 N up to 2 m, then linear to 0 N at 5 m."),
    55: ("diagram", "Incidence sines: ray X 0.85 and ray Y 0.95."),
    109: ("diagram", "Three runs (A, B, rate): (c,d,r), (2c,d,2r), (2c,2d,8r)."),
    121: ("diagram", "Relation matrix rows 110, 111, 011, ordered 1, 2, 3."),
}
LETTERS = "ABCD"


def assemble():
    with (ROOT / "docs/blueprints/comedk_25_test_slots.csv").open(newline="") as stream:
        plan = {int(r["question"]): r for r in csv.DictReader(stream) if r["test"] == "1"}
    questions = []
    sections = []
    for section, (code, name) in enumerate(SUBJECTS.items()):
        rows = (DIR / f"authoring/test01_{code}.txt").read_text().splitlines()
        keys = (DIR / f"authoring/test01_{code}.key").read_text().split()
        assert len(rows) == len(keys) == 60 and Counter(keys) == dict.fromkeys(LETTERS, 15)
        for index, (row, key) in enumerate(zip(rows, keys), section * 60 + 1):
            number, stem, answer, *tail = [value.strip() for value in row.split("|")]
            wrong1, wrong2, wrong3, working, reasons = tail
            distractors = [wrong1, wrong2, wrong3]
            assert int(number) == index
            assert len(reasons.split("~")) == 3
            assert len({answer, *distractors}) == 4
            ordered = distractors.copy()
            ordered.insert(LETTERS.index(key), answer)
            labels = [letter for letter in LETTERS if letter != key]
            rebuttals = " ".join(f"({letter}) {reason}." for letter, reason in zip(labels, reasons.split("~")))
            slot = plan[index]
            question = {
                "id": slot["id"],
                "section": code,
                "subject": name,
                "topic": slot["chapter"],
                "sub_topic": slot["anchor"],
                "syllabus_anchor_id": slot["anchor_id"],
                "syllabus_pdf_page": slot["pdf_page"],
                "class_level": slot["class_level"],
                "difficulty": slot["difficulty_target"],
                "format": "numerical" if re.search(r"[=×∫]", working) else "conceptual",
                "question": stem,
                "options": [f"{letter}) {option}" for letter, option in zip(LETTERS, ordered)],
                "correct_option": key,
                "explanation": f"Answer: ({key}) {answer}\nWhy and working: {working}\nWhy not the others: {rebuttals}",
            }
            if index in FIGURES:
                question["format"], question["image_alt"] = FIGURES[index]
                question["image_reference"] = f"COMEDK_T01_Q{index:03}.png"
                assert (DIR / "images" / question["image_reference"]).is_file()
            questions.append(question)
        first = section * 60 + 1
        sections.append({"id": code, "title": name, "question_range": f"{first}-{first + 59}",
                         "questions": 60, "attempt": 60})
    all_keys = "".join(q["correct_option"] for q in questions)
    assert not re.search(r"(.)\1{3}", all_keys)
    return {
        "test_id": "COMEDK27_TEST_01",
        "series_id": "COMEDK27",
        "exam": "COMEDK UGET preparation",
        "title": "COMEDK UGET Test 1",
        "test_number": 1,
        "status": "pending_revision",
        "syllabus_source": "COMEDK/SOURCES.md and official subject PDFs (2026 baseline)",
        "notification_source": "COMEDK UGET Information Brochure 2026, section 16",
        "past_paper_reference": "docs/blueprints/comedk_pyq_analysis.md",
        "duration_minutes": 180,
        "maximum_marks": 180,
        "total_questions": 180,
        "questions_to_attempt": 180,
        "marking_scheme": {"correct": "+1", "incorrect": "0", "unattempted": "0"},
        "image_base_path": "COMEDK/images",
        "instructions": ["Choose one answer per question.", "One mark per correct answer. No negative marking."],
        "sections": sections,
        "questions": questions,
    }


if __name__ == "__main__":
    path = DIR / "COMEDK UGET TEST 1.json"
    path.write_text(json.dumps(assemble(), ensure_ascii=False, indent=2) + "\n")
    print(path.relative_to(ROOT))
