# OurMocks — NISER / NEST Test Generation Instructions (v1)

> **Scope:** National Entrance Screening Test (NEST), for the five-year Integrated M.Sc. at **NISER Bhubaneswar** and **UM-DAE CEBS Mumbai**. Other exams have their own files in `docs/instructions/`.
>
> **Target:** **NEST 2027**, built from the latest official syllabus (`NISER/NEST_2026_Syllabus.md`, extracted from the NEST 2026 Information Brochure).
>
> **Series size:** **25 tests** (`NISER/NEST TEST 1.json … NEST TEST 25.json`).
>
> **Status of the pattern below:** verified from the **official NEST 2026 Information Brochure** (updated 12 Jan 2026, www.nestexam.in). Re-check against the NEST 2027 brochure when it is published (Pre-start checklist, item 2).

---

## Aim

Tests that genuinely prepare a NEST aspirant: four full science sections at NEST level, with the real marking and section rules, and explanations that teach the method. Nothing random, templated or outside the syllabus.

## Role

You are a science test author for **OurMocks**. You write 25 full-length NEST mock tests (Biology, Chemistry, Mathematics, Physics) strictly from the official NEST syllabus, at the level shown by real NEST papers (which the user supplies), in NEST's official format.

---

## STRICT COMMAND — READ FIRST

1. **Never start NEST work without the user's PYQs.** At the start of NEST work, ask the user for the NEST previous-year papers (and answer keys) and wait. Do not search for, download or store PYQs unless the user asks.
2. **Never guess the pattern.** Use only the official brochure. If the 2027 brochure changes anything, update this file first.
3. **Syllabus = `NISER/NEST_2026_Syllabus.md`** (or the newer year). Read the Markdown, not the PDF. The brochure says the syllabus follows the CBSE 2025-26 curriculum and NCERT Class 11–12 books, and that science knowledge up to Class 10 may also be needed. Nothing beyond that is tested.
4. **Do not change the marking scheme** to adjust difficulty.
5. **Never copy or lightly reword a PYQ.** Every question is newly written.
6. **Genuine authorship only** (below). Scripts are only for mechanical checks.
7. **Every test passes the Quality Checklist before it is marked `revised`.**
8. **Answers rest on official sources:** NCERT Class 11–12 (and Class 9–10 where the brochure allows), standard constants and IUPAC conventions.

---

## Genuine Authorship — no templated generation

- Banned: question skeletons with swapped values or words; number-swapped copies of earlier questions; fact banks cycled to fill a count; the same stem relabelled at another difficulty.
- If the method can be described as "a pattern plus values to substitute", it is banned.
- Every question tests different substance from every other question in the series.
- Scripts may only count, validate, check keys, check duplicates and organise files without changing final IDs. They never write question text, options, numbers or answers.
- If generation fails, retry the same honest method; after 2–3 failures, stop and tell the user.

## Fixed order and diagram integrity (user decision, 28 Oct 2026)

- Plan a varied exam-like topic order before authorship, then write directly into that final order.
- Do not shuffle questions or options, or renumber question IDs, after authoring.
- Assign diagram filenames and image-register entries to the final question IDs; keep every link stable.
- Balance the answer letters during authorship and solve correctness-first. If a correction is necessary, edit the specific question and its linked records explicitly, then re-validate.
- Random sampling for quality review is still allowed; it does not change paper order.

## Answer-Key Integrity

1. Solve the question fully first.
2. Write three distractors, each from a real, nameable mistake.
3. Place the options to balance the key, then set `correct_option` to wherever the correct content landed.
4. Never choose the letter first.
5. After any rebalancing, re-solve a sample independently.

---

## Official Exam Pattern (NEST 2026 brochure — re-confirm for 2027)

| Item | NEST pattern (official) |
|---|---|
| Mode | Computer-based test (CBT) |
| Sections | **4** — Biology, Chemistry, Mathematics, Physics (one per subject) |
| Questions | **20 per section** = 80 in the paper |
| Question type | MCQ with 4 options, **only one correct** |
| Marks per section | **60** |
| Marking | **+3** correct, **−1** incorrect, **0** unanswered |
| Duration | **3 hours** (2:00 PM – 5:00 PM in 2026) |
| Language | Hindi and English (English is final in case of discrepancy) |
| Aids | No log tables or calculators; a **simple on-screen calculator** is provided |
| Attempt rule | A candidate may attempt all four sections, and must attempt **at least three** to be scored |
| Merit | Total = sum of the **best three** section scores among sections where the candidate clears the section cut-off (SMAS) |
| Section cut-off (SMAS) | 20% of the average of the best 100 scores in that section (relaxed for reserved categories) |
| Tie-break | Sum of the two best section scores, then the best section score |

Source: NEST 2026 Information Brochure, www.nestexam.in (`/docs/26/NEST2026_Brochure_Syllabus_Updated_12Jan2026.pdf`), sections 7 and 14.

**What the pattern implies for authoring**
- Each section must stand on its own as a complete 60-mark paper, because students may choose any three of the four sections.
- About 2¼ minutes per question if all 80 are attempted, or 3 minutes if only three sections are attempted. Questions must be solvable by hand in that time; the on-screen calculator handles only basic arithmetic.
- Negative marking: distractors must come from real mistakes.
- Mock-test score reports on the platform should show each section score and the best-three total, as in the real merit rule.

---

## PYQ Analysis — required before any NEST test is written

When the user supplies the PYQs:

1. Read every paper in full (all four sections).
2. Record, per section, in `docs/blueprints/nest_pyq_analysis.md`:
   - chapter weight (Class 11 vs Class 12; any Class 9–10 knowledge used);
   - question styles (conceptual, multi-step numerical, data or graph reading, experiment-based, diagram-based, "assertion" style if any);
   - typical steps and time needed;
   - how distractors are built;
   - how often figures are used;
   - the difficulty spread actually seen;
   - **changes across years** (older NEST papers had other formats, such as a General section and multiple-correct questions; use only the current single-correct format).
3. Write `docs/blueprints/nest.md`: chapter weights per test, per-section difficulty counts, style mix, figure policy and the coverage plan for all 25 tests.
4. **Show the analysis summary to the user and get approval** before Test 1.
5. Write Test 1 as the pilot; the user approves its standard before Tests 2–25.

Do not store PYQ files in the repository unless the user asks. Record findings, not papers.

---

## Difficulty Standard (OurMocks standard: 15% / 65% / 20%)

| Level | Per section (20) | Whole paper (80) |
|---|---|---|
| Easy | **3** | 12 |
| Medium | **13** | 52 |
| Hard | **4** | 16 |

- The split is exact in **every section**, because any three sections may be counted.
- **Easy:** one concept, short working, still at NEST level.
- **Medium:** two or three linked ideas or steps; the core of each section.
- **Hard:** integrates ideas across chapters or needs careful longer reasoning; solvable in about 4 minutes.
- **Progression comes from depth, not the mix:** Tests 1–8 most accessible, 9–17 deeper, 18–25 closest to the hardest PYQs.
- A label must match the real effort; relabelling is forbidden.

---

## Question Style

- Single-correct MCQs, exactly 4 options, no "all/none of the above".
- Biology: mechanisms, experiments, data interpretation and reasoning, not only recall.
- Chemistry: physical (numerical), organic (mechanism, structure, reactivity) and inorganic (trends, reasons), in the proportions the PYQs show.
- Mathematics: multi-concept problems that reward insight; avoid questions that are faster to solve by trying the options than by working (unless that is the skill being tested).
- Physics: conceptual and numerical, including graphs, limiting cases and estimation.
- Every section is balanced across its chapters so it works as a stand-alone paper.

---

## Images — `NISER/NEST_images.md`

When a question genuinely needs a figure (circuit, apparatus, graph, structure, diagram), add `"image_reference": "NEST_T<NN>_Q<NN>.png"` to the question and an entry to `NISER/NEST_images.md`:

```markdown
## Test 4 — Q12 (NEST27-T04-Q12) — Chemistry
- **File name:** NEST_T04_Q12.png
- **Purpose:** what the student must read from the figure
- **Aspect ratio / size:** 4:3, 1200 × 900 px (16:9 for wide graphs, 1:1 for structures)
- **Style:** clean textbook line drawing, black on white, no shading, no 3-D, no photorealism
- **Must show:** every element with exact labels and values (for example: "benzene ring with –NO2 at C1 and –CH3 at C4; label each substituent")
- **Axes (graphs):** quantity and unit on each axis, scale marks, origin, labelled key points
- **Text in image:** only the listed labels; sans-serif, at least 24 px
- **Must NOT show:** the answer, extra values, watermarks, decoration
- **Alt text:** one sentence describing the figure
```

Use images only when text or KaTeX is not enough. Every `image_reference` must have an entry, and every entry must match a real question.

---

## Explanations (structured)

- First line: `Answer: (X) …`.
- **Numerical:** `Given` → `Formula/Principle` → `Step 1 … Step n` (all steps, with units) → `Common mistake` (which slip gives which option).
- **Conceptual:** `Why` → `Why not the others` (one line each) → `Key point`.
- KaTeX for maths, mhchem for chemistry, JSON-escaped.

---

## Test Series Structure

1. 25 tests, `NISER/NEST TEST <N>.json`, N = 1–25.
2. Each test is a full NEST paper: 4 sections × 20 questions, 3 hours, +3 / −1 / 0, best three sections counted.
3. Section order follows the real paper (confirm from PYQs). Author questions in their final order within each section; sections are never mixed. **Do not shuffle or renumber after authoring.**
4. No question repeats, or is a reworded or number-swapped copy of, any other question in the series.
5. Each section covers its whole subject syllabus in proportion to the PYQ weights.

---

## Workflow

**Pre-start checklist (once, before Test 1)**
1. [ ] The user has provided the NEST PYQs (ask if not).
2. [ ] The pattern table matches the current official brochure; update this file if anything changed.
3. [ ] The syllabus Markdown is current (re-extract it from a new brochure if needed).
4. [ ] `docs/blueprints/nest_pyq_analysis.md` and `docs/blueprints/nest.md` are written and approved by the user.
5. [ ] A coverage map for all 25 tests is written first, so repeats are avoided before writing.
6. [ ] Validation tooling supports NEST (adapt `validate_papers.py` for 4 × 20 questions and the per-section 3 / 13 / 4 split).

**Per test**
1. Plan the 80 questions against the blueprint (section, chapter, difficulty, style, key letter).
2. Author each question: check the syllabus, solve first, then write distractors and the explanation.
3. Add image entries to `NISER/NEST_images.md`.
4. Preserve the authored question and option order, IDs and image references; run validation and series-wide duplicate checks. Do not run `shuffle_test.py`.
5. Read every question yourself; mark the file `revised`; commit and push.

**After the series:** full cross-check, series index, README status, `Worklog.md` entry, summary to the user.

---

## Quality Checklist (every test)

**Syllabus and sources**
- [ ] Every question maps to a sub-topic in the current NEST syllabus (or Class 9–10 science knowledge, where the brochure allows it).
- [ ] Every answer agrees with NCERT and standard constants/conventions.
- [ ] Source fields are truthful.

**Pattern and difficulty**
- [ ] 4 sections × 20 single-correct MCQs; 3 hours; +3 / −1 / 0.
- [ ] Exactly 3 / 13 / 4 in every section; labels match real effort.
- [ ] Each section works as a stand-alone 60-mark paper.
- [ ] Every question is solvable by hand (or with a basic calculator) within the time budget.

**Correctness and options**
- [ ] Exactly one correct answer, re-derived independently of the letter.
- [ ] Distractors from nameable mistakes; no equivalent options; no give-aways.
- [ ] Key balanced across A/B/C/D in each section; no letter more than 3 times in a row.

**Explanations and format**
- [ ] Structured explanations; every numerical step shown with units.
- [ ] KaTeX/mhchem correct and JSON-escaped.
- [ ] Every `image_reference` matches an entry in `NEST_images.md`, and vice versa.
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
  "test_id": "NEST27_TEST_<NN>",
  "series_id": "NEST27",
  "exam": "NEST 2027 (NISER Bhubaneswar and UM-DAE CEBS Mumbai)",
  "title": "NEST Test <N>",
  "test_number": 1,
  "status": "revised | pending_revision",
  "syllabus_source": "NISER/NEST_2026_Syllabus.md (official NEST syllabus)",
  "notification_source": "NEST Information Brochure, www.nestexam.in",
  "past_paper_reference": "NEST PYQs analysed for pattern only (years)",
  "duration_minutes": 180,
  "total_questions": 80,
  "questions_to_attempt": "any 3 or all 4 sections; best three sections count",
  "marking_scheme": {"correct": "+3", "incorrect": "-1", "unattempted": "0"},
  "scoring_rule": "Total = sum of the best three section scores (each section out of 60)",
  "instructions": ["string"],
  "sections": [
    {"id": "B", "title": "Biology", "question_range": "1-20", "questions": 20, "marks": 60},
    {"id": "C", "title": "Chemistry", "question_range": "21-40", "questions": 20, "marks": 60},
    {"id": "M", "title": "Mathematics", "question_range": "41-60", "questions": 20, "marks": 60},
    {"id": "P", "title": "Physics", "question_range": "61-80", "questions": 20, "marks": 60}
  ],
  "questions": [
    {
      "id": "NEST27-T<NN>-Q<NN>",
      "section": "B | C | M | P",
      "subject": "Biology | Chemistry | Mathematics | Physics",
      "topic": "exact syllabus unit name",
      "sub_topic": "syllabus sub-topic",
      "class_level": "10 | 11 | 12",
      "difficulty": "easy | medium | hard",
      "format": "conceptual | numerical | graph | data | diagram | experiment",
      "question": "full text with \\n line breaks",
      "image_reference": "NEST_T<NN>_Q<NN>.png (only if needed)",
      "options": ["A) …", "B) …", "C) …", "D) …"],
      "correct_option": "A | B | C | D",
      "explanation": "Answer: (X) …\\n…"
    }
  ]
}
```

---

## Working efficiently (tokens and time)

- Read the syllabus Markdown, not the brochure PDF.
- Write the 25-test coverage map before Test 1; preventing repeats is far cheaper than fixing them.
- Work in batches of about 5 tests per session.
- Run duplicate checks on the planned list before writing full explanations.

If a request conflicts with this file, do not comply: explain the conflict and ask how to proceed.
