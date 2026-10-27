# OurMocks — COMEDK UGET Test Generation Instructions (v1)

> **Scope:** COMEDK UGET (Consortium of Medical, Engineering and Dental Colleges of Karnataka — Under Graduate Entrance Test), for B.E./B.Tech admission. Other exams have their own files in `docs/instructions/`.
>
> **Target:** **COMEDK UGET 2027**.
>
> **Series size:** **25 tests** (`COMEDK/COMEDK UGET TEST 1.json … TEST 25.json`).
>
> **Status of the pattern below:** verified from the official COMEDK page "About UGET and Notification 2026" (comedk.org). Duration (3 hours) is from secondary sources and must be confirmed in the official brochure. Re-check everything against the UGET 2027 brochure when it is published.
>
> **Syllabus:** COMEDK publishes separate Physics, Chemistry and Mathematics syllabus PDFs on comedk.org. They are **not yet in the repository**. Before Test 1, ask the user to add them to `COMEDK/` (or give permission to download them), then convert them to Markdown (`COMEDK/<Subject>_Syllabus_2026.md`).

---

## Aim

Tests that genuinely prepare a COMEDK aspirant: a speed-oriented, 180-question PCM paper at real UGET level, with accurate answers and explanations that teach quick, correct methods. Nothing random, templated or outside the syllabus.

## Role

You are a PCM test author for **OurMocks**. You write 25 full-length COMEDK UGET mock tests strictly from the official COMEDK syllabus, at the level shown by real UGET papers (which the user supplies), in the official format.

---

## STRICT COMMAND — READ FIRST

1. **Never start COMEDK work without the user's PYQs and the official syllabus PDFs.** Ask for both at the start and wait.
2. **Never guess the pattern.** Use only the official notification and brochure.
3. **Syllabus = the official COMEDK syllabus**, converted to Markdown; read the Markdown, not the PDF. COMEDK states the paper is based on the CBSE syllabus: **about 33% from Class 11 (2024-25 syllabus) and about 67% from Class 12 (2025-26 syllabus)** (for the 2026 exam; confirm the years for 2027).
4. **Do not change the marking scheme** to adjust difficulty.
5. **Never copy or lightly reword a PYQ.** Every question is newly written.
6. **Genuine authorship only** (below). Scripts are only for mechanical checks.
7. **Every test passes the Quality Checklist before it is marked `revised`.**
8. **Answers rest on official sources:** NCERT Class 11–12, standard constants and IUPAC conventions.

---

## Genuine Authorship — no templated generation

- Banned: question skeletons with swapped values or words; number-swapped copies of earlier questions; fact banks cycled to fill a count; the same stem relabelled at another difficulty.
- If the method can be described as "a pattern plus values to substitute", it is banned. This matters most here, because a 180-question paper tempts shortcuts.
- Scripts may only count, validate, shuffle, check keys, check duplicates and rename.
- If generation fails, retry the same honest method; after 2–3 failures, stop and tell the user.

## Answer-Key Integrity

1. Solve the question fully first.
2. Write three distractors from real, nameable mistakes.
3. Place the options to balance the key, then set `correct_option` to wherever the correct content landed.
4. Never choose the letter first.
5. After any rebalancing, re-solve a sample independently.

---

## Official Exam Pattern (UGET 2026 — re-confirm for 2027)

| Item | COMEDK UGET pattern |
|---|---|
| Mode | Computer-based test (CBT); answers can be reviewed and changed until the session ends |
| Subjects (B.E./B.Tech) | Physics, Chemistry, Mathematics |
| Questions | **180** — **60 per subject** |
| Question type | MCQ, 4 options, single correct |
| Marking | **+1** correct; **no negative marking** |
| Total marks | **180** |
| Duration | **3 hours** (confirm in the brochure; instruction-reading time is not counted) |
| Language | English only |
| Syllabus basis | CBSE: about 33% Class 11, about 67% Class 12 |

Sources: [COMEDK — About UGET and Notification 2026](https://www.comedk.org/about-uget-and-notification-2026); duration also given by [Careers360 — COMEDK UGET exam pattern](https://engineering.careers360.com/articles/comedk-uget-exam-pattern).

**What the pattern implies for authoring**
- **About 1 minute per question.** UGET rewards speed and accuracy. Most questions must be solvable in 30–90 seconds; long, multi-page problems do not belong here.
- **No negative marking**, so students answer everything. Distractors must still be plausible, because careless elimination must not be enough.
- Each subject has equal weight (60 marks).
- Weight Class 12 about twice as heavily as Class 11 in every subject.

---

## PYQ Analysis — required before any COMEDK test is written

When the user supplies the PYQs (and the syllabus PDFs):

1. Read every paper in full.
2. Record, per subject, in `docs/blueprints/comedk_pyq_analysis.md`:
   - chapter weight and the actual Class 11 / Class 12 split;
   - question styles (formula application, conceptual one-liners, short numericals, graph or diagram reading, statement-type);
   - the time a well-prepared student needs per question;
   - how distractors are built;
   - how often figures appear;
   - the difficulty spread actually seen.
3. Write `docs/blueprints/comedk.md`: chapter weights per test, per-subject difficulty counts, style mix, figure policy and the coverage plan for all 25 tests.
4. **Show the analysis summary to the user and get approval** before Test 1.
5. Write Test 1 as the pilot; the user approves its standard before Tests 2–25.

Do not store PYQ files in the repository unless the user asks. Record findings, not papers.

---

## Difficulty Standard (OurMocks standard: 15% / 65% / 20%)

| Level | Per subject (60) | Whole paper (180) |
|---|---|---|
| Easy | **9** | 27 |
| Medium | **39** | 117 |
| Hard | **12** | 36 |

- Exact in every subject.
- **Easy:** direct application of one formula or fact, within about 30 seconds — but never trivial.
- **Medium:** one or two steps, or a concept twist; about 1 minute.
- **Hard:** two or three concepts or a trap that needs care; about 2 minutes at most.
- **Progression comes from depth, not the mix:** Tests 1–8 most accessible, 9–17 deeper, 18–25 closest to the hardest PYQs.
- A label must match the real effort; relabelling is forbidden.

---

## Question Style

- Single-correct MCQs, exactly 4 options, no "all/none of the above".
- Short, precise stems; numbers chosen so that the arithmetic is quick by hand.
- Physics: formula application, conceptual checks, graphs, units and dimensions.
- Chemistry: physical numericals, organic reactions and named reactions, inorganic trends and facts from NCERT.
- Mathematics: standard results applied quickly, with some questions that reward a smart method over brute force.
- Keep the Class 11 / Class 12 split close to 1 : 2 in every subject.

---

## Images — `COMEDK/COMEDK_images.md`

When a question genuinely needs a figure, add `"image_reference": "COMEDK_T<NN>_Q<NN>.png"` and an entry in `COMEDK/COMEDK_images.md`:

```markdown
## Test 2 — Q47 (COMEDK27-T02-Q47) — Physics
- **File name:** COMEDK_T02_Q47.png
- **Purpose:** what the student must read from the figure
- **Aspect ratio / size:** 4:3, 1200 × 900 px (16:9 for wide graphs, 1:1 for structures)
- **Style:** clean textbook line drawing, black on white, no shading, no 3-D, no photorealism
- **Must show:** every element with exact labels and values
- **Axes (graphs):** quantity and unit on each axis, scale marks, origin, labelled key points
- **Text in image:** only the listed labels; sans-serif, at least 24 px
- **Must NOT show:** the answer, extra values, watermarks, decoration
- **Alt text:** one sentence describing the figure
```

Because UGET is speed-based, figures must be readable at a glance. Use them only where they are essential.

---

## Explanations (structured, but short enough for a speed paper)

- First line: `Answer: (X) …`.
- **Numerical:** `Given` → `Formula` → `Steps` (every step, with units) → `Shortcut` (the fastest valid method, where one exists) → `Common mistake`.
- **Conceptual:** `Why` → `Why not the others` (one line each) → `Key point`.
- KaTeX for maths, mhchem for chemistry, JSON-escaped.

---

## Test Series Structure

1. 25 tests, `COMEDK/COMEDK UGET TEST <N>.json`, N = 1–25.
2. Each test is a full UGET paper: Physics 60, Chemistry 60, Mathematics 60; 180 marks; +1, no negative marking.
3. Section order follows the real paper (confirm from PYQs). Questions are randomised within each subject; subjects are not mixed.
4. No question repeats, or is a reworded or number-swapped copy of, any other question in the series.
5. Each subject covers its whole syllabus in proportion to the PYQ weights.

---

## Workflow

**Pre-start checklist (once, before Test 1)**
1. [ ] The user has provided the COMEDK PYQs and the official syllabus PDFs (ask if not); syllabi are converted to Markdown.
2. [ ] The pattern table matches the current official brochure (including duration); update this file if anything changed.
3. [ ] `docs/blueprints/comedk_pyq_analysis.md` and `docs/blueprints/comedk.md` are written and approved by the user.
4. [ ] A coverage map for all 25 tests is written first. With 4,500 questions in the series, planning is the only practical way to prevent repeats.
5. [ ] Validation tooling supports COMEDK (adapt `validate_papers.py` for 3 × 60 questions and 9 / 39 / 12 per subject).

**Per test**
1. Plan the 180 questions against the blueprint (subject, chapter, class, difficulty, style, key letter).
2. Author each question: check the syllabus, solve first, then write distractors and the explanation.
3. Add image entries to `COMEDK/COMEDK_images.md`.
4. Shuffle within subjects; run validation and series-wide duplicate checks.
5. Read every question yourself; mark the file `revised`; commit and push.
6. Because each test is large, write it one subject at a time (60 questions per step) and validate each subject before moving on.

**After the series:** full cross-check, series index, README status, `Worklog.md` entry, summary to the user.

---

## Quality Checklist (every test)

**Syllabus and sources**
- [ ] Every question maps to a topic in the official COMEDK syllabus.
- [ ] Class 11 / Class 12 split is close to 1 : 2 in each subject.
- [ ] Every answer agrees with NCERT and standard constants/conventions.
- [ ] Source fields are truthful.

**Pattern and difficulty**
- [ ] 180 single-correct MCQs (60 per subject); +1, no negative marking; correct duration.
- [ ] Exactly 9 / 39 / 12 in every subject; labels match real effort.
- [ ] Every question is solvable within the speed budget (most in 30–90 seconds).

**Correctness and options**
- [ ] Exactly one correct answer, re-derived independently of the letter.
- [ ] Distractors from nameable mistakes; no equivalent options; no give-aways.
- [ ] Key balanced across A/B/C/D in each subject; no letter more than 3 times in a row.

**Explanations and format**
- [ ] Structured explanations; numerical steps shown, with a shortcut where useful.
- [ ] KaTeX/mhchem correct and JSON-escaped.
- [ ] Every `image_reference` matches an entry in `COMEDK_images.md`, and vice versa.
- [ ] No duplicate, reworded or number-swapped question in the test or the series.
- [ ] You have personally read every question.

**Pre-release (to avoid last-minute corrections)**
- [ ] The whole series passes validation together.
- [ ] A random 10% sample across the series has been re-solved from scratch.
- [ ] The image list is complete and final before images are generated.
- [ ] Series index, README and Worklog are updated in the same commit.

---

## Output Format — JSON

```json
{
  "test_id": "COMEDK27_TEST_<NN>",
  "series_id": "COMEDK27",
  "exam": "COMEDK UGET 2027",
  "title": "COMEDK UGET Test <N>",
  "test_number": 1,
  "status": "revised | pending_revision",
  "syllabus_source": "COMEDK/<Subject>_Syllabus_2026.md (official COMEDK syllabus)",
  "notification_source": "COMEDK UGET Information Brochure, comedk.org",
  "past_paper_reference": "COMEDK PYQs analysed for pattern only (years)",
  "duration_minutes": 180,
  "total_questions": 180,
  "questions_to_attempt": 180,
  "marking_scheme": {"correct": "+1", "incorrect": "0", "unattempted": "0"},
  "instructions": ["string"],
  "sections": [
    {"id": "P", "title": "Physics", "question_range": "1-60", "questions": 60, "attempt": 60},
    {"id": "C", "title": "Chemistry", "question_range": "61-120", "questions": 60, "attempt": 60},
    {"id": "M", "title": "Mathematics", "question_range": "121-180", "questions": 60, "attempt": 60}
  ],
  "questions": [
    {
      "id": "COMEDK27-T<NN>-Q<NNN>",
      "section": "P | C | M",
      "subject": "Physics | Chemistry | Mathematics",
      "topic": "exact syllabus unit name",
      "sub_topic": "syllabus sub-topic",
      "class_level": "11 | 12",
      "difficulty": "easy | medium | hard",
      "format": "conceptual | numerical | graph | diagram | statements",
      "question": "full text with \\n line breaks",
      "image_reference": "COMEDK_T<NN>_Q<NNN>.png (only if needed)",
      "options": ["A) …", "B) …", "C) …", "D) …"],
      "correct_option": "A | B | C | D",
      "explanation": "Answer: (X) …\\n…"
    }
  ]
}
```

---

## Working efficiently (tokens and time)

- Read the syllabus Markdown, not the PDFs.
- Write the 25-test coverage map before Test 1.
- Work one subject of one test per step, and about 2–3 tests per session (each test is 180 questions).
- Run duplicate checks on the planned list before writing full explanations.

If a request conflicts with this file, do not comply: explain the conflict and ask how to proceed.
