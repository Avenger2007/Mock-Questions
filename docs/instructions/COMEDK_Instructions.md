# OurMocks — COMEDK UGET Test Generation Instructions (v2)

> **Scope:** COMEDK UGET (Consortium of Medical, Engineering and Dental Colleges of Karnataka — Under Graduate Entrance Test), for B.E./B.Tech admission. Other exams have their own files in `docs/instructions/`.
>
> **Target:** **COMEDK UGET 2027**.
>
> **Series size:** **25 tests** (`COMEDK/COMEDK UGET TEST 1.json … TEST 25.json`).
>
> **Baseline:** Official COMEDK UGET 2026 pattern and subject syllabi for provisional 2027 preparation. Reconcile the official 2027 notification, duration and syllabus before claiming target-year compliance.
>
> **Sources:** [COMEDK source register](../../COMEDK/SOURCES.md), [past-paper register](../../PYQ/COMEDK/SOURCES.md), [PYQ analysis](../blueprints/comedk_pyq_analysis.md) and [25-test blueprint](../blueprints/comedk.md).

---

## Aim

Tests that genuinely prepare a COMEDK aspirant: a speed-oriented, 180-question PCM paper at real UGET level, with accurate answers and explanations that teach quick, correct methods. Nothing random, templated or outside the syllabus.

## Role

You are a PCM test author for **OurMocks**. You write 25 full-length COMEDK UGET mock tests strictly from the official COMEDK syllabus, calibrated to inspected UGET past-paper evidence and the official format.

---

## STRICT COMMAND — READ FIRST

1. **Read the acquired syllabus and past-paper register before authoring.** Treat official syllabus PDFs as scope authority and the inspected reconstructions as provisional evidence of question style. Seek additional source evidence for claims the current sample cannot support.
2. **Never guess the pattern.** Use only the official notification and brochure.
3. **Syllabus = the official COMEDK subject PDFs.** Use the scope catalog to navigate and inspect the cited pages for exact limits and visually embedded formulas. COMEDK states the paper is based on the CBSE syllabus: **about 33% from Class 11 (2024-25 syllabus) and about 67% from Class 12 (2025-26 syllabus)** (for the 2026 exam; confirm the years for 2027).
4. **Do not change the marking scheme** to adjust difficulty.
5. **Never copy or lightly reword a PYQ.** Every question is newly written.
6. **Genuine authorship only** (below). Scripts are only for mechanical checks.
7. **Every test passes the Quality Checklist before it is marked `revised`.**
8. **Answers rest on official sources:** NCERT Class 11–12, standard constants and IUPAC conventions.

---

## Genuine Authorship — no templated generation

- Banned: question skeletons with swapped values or words; number-swapped copies of earlier questions; fact banks cycled to fill a count; the same stem relabelled at another difficulty.
- If the method can be described as "a pattern plus values to substitute", it is banned. This matters most here, because a 180-question paper tempts shortcuts.
- Scripts may only count, validate, check keys, check duplicates and organise files without changing final IDs.
- If an angle fails review, replace and re-solve it. Record recurring blockers so other eligible slots can proceed.

## Fixed order and diagram integrity (user decision, 28 Oct 2026)

- Plan a varied exam-like topic order before authorship, then write directly into that final order.
- Do not shuffle questions or options, or renumber question IDs, after authoring.
- Assign diagram filenames and image-register entries to the final question IDs; keep every link stable.
- Balance the answer letters during authorship and solve correctness-first. If a correction is necessary, edit the specific question and its linked records explicitly, then re-validate.
- Random sampling for quality review is still allowed; it does not change paper order.

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
| Duration | **180-minute mock clock**. Official 2025 slots support this baseline and 2026 reconstructions agree. Recheck the target-year timing. |
| Language | English only |
| Syllabus basis | CBSE: about 33% Class 11, about 67% Class 12 |

See the [timing evidence and source hierarchy](../../COMEDK/SOURCES.md).

**What the pattern implies for authoring**
- **About 1 minute per question.** UGET rewards speed and accuracy. Most questions must be solvable in 30–90 seconds; long, multi-page problems do not belong here.
- **No negative marking**, so students answer everything. Distractors must still be plausible, because careless elimination must not be enough.
- Each subject has equal weight (60 marks).
- Weight Class 12 about twice as heavily as Class 11 in every subject.

---

## PYQ calibration and syllabus boundaries

Read the [recorded analysis](../blueprints/comedk_pyq_analysis.md) and check the original references for the intended item style. Preserve source tier, session, page or item, and extraction/answer limits. Reject coaching reconstructions with missing content or multiple correct choices as calibration items. Official demo mocks provide interface practice. Compare expected effort and decision-making, and author original content.

Map each item to a verified class, PDF page and scope anchor before drafting. Use the published subject-specific limits. For example, COMEDK lists graphical linear programming while 3-D geometry XII is scoped to lines. Poisson ratio is listed in Physics. Single-slit central maximum is qualitative, and YDSE fringe width is final expression only. Check the source before including AP sums, radioactivity, potentiometers, polarisation, or advanced chemistry simply because they occur elsewhere or in a recall paper.

Do not use the present sample to assert official topic weights, exact difficulty rates or figure frequency. The 25-test plan allocates coverage by breadth. Proceed with draft batches of two using desk calibration. Finish the first paper’s review before locking the second paper. Keep timing and difficulty estimates provisional until COMEDK candidates provide measured attempts.

## Difficulty Standard (OurMocks standard: 15% / 65% / 20%)

| Level | Per subject (60) | Whole paper (180) |
|---|---|---|
| Easy | **9** | 27 |
| Medium | **39** | 117 |
| Hard | **12** | 36 |

- Exact in every subject.
- **Easy:** direct application of one formula or fact, target about 30 seconds — but never trivial.
- **Medium:** a model decision, a concept twist or two short steps. Target about 50 seconds.
- **Hard:** bounded multi-step reasoning or a subtle condition. Target about 100 seconds as a planning estimate. Check the reasoning demand during desk review and revise the estimate when candidate timing is available.
- **Progression comes from depth, not the mix:** Tests 1–8 most accessible, 9–17 deeper, 18–25 mixed timed rehearsal with more condition and interpretation checks.
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

When a question genuinely needs a figure, add `"image_reference": "COMEDK_T<NN>_Q<NNN>.png"` and an entry in `COMEDK/COMEDK_images.md`:

```markdown
## Test 2 — Q47 (COMEDK27-T02-Q047) — Physics
- **File name:** COMEDK_T02_Q047.png
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

## Explanations

- Start with `Answer: (X)` and state the correct result.
- For Mathematics and Physics, show the governing equation and why it applies, then the substitution, every material transformation, branch or sign decision, final result and a valid check as applicable. Preserve units. Brief explanatory sentences clarify the model and conditions.
- For numerical Chemistry, balance reactions and track the stagewise amounts, units, charge and conditions. For organic and inorganic questions, explain the structure, governing trend, conditions or exception that selects the result.
- Include a distinct `Why not the others` reason for each labelled distractor. Refute the actual option. An approximate shortcut is optional and must state its validity conditions.
- Use the repo's rendered math conventions. Check parsed maths and the actual page, especially symbols, signs, image placement and option layout.

## Test Series Structure

1. 25 tests, `COMEDK/COMEDK UGET TEST <N>.json`, N = 1–25.
2. Each test is a full UGET paper: Physics 60, Chemistry 60, Mathematics 60; 180 marks; +1, no negative marking.
3. Use Physics, Chemistry, Mathematics as the fixed mock convention, consistent with the official listing. Exact CBT ordering remains unverified. Author questions in their final order within each subject; subjects are not mixed. **Do not shuffle or renumber after authoring.**
4. No question repeats, or is a reworded or number-swapped copy of, any other question in the series.
5. Balance the series using the official scope ledger and maintain the 20/40 Class XI/XII subject reservation. A planned slot is not evidence of tested coverage.

---

## Workflow

1. Use the [initial reserve schedule](../blueprints/comedk_25_test_slots.csv) and [coverage map](../blueprints/comedk_syllabus_coverage.csv). Run `python3 tools/comedk/plan_series.py` against the initial plan.
2. For each planned question, fill the [angle register](../blueprints/comedk_angle_register.csv) before drafting. The task description must identify the object, constraints, governing method, decisive inference, requested result, distractor logic and nearest comparison. Approve after comparing with authored COMEDK mocks and their approved angles for internal repetition, and with relevant COMEDK PYQs for task style, scope fit and accidental copying. Use exam-specific sources throughout. Same topic is allowed. A new number, wording, incidental figure or reversing givens does not on its own change the task.
3. Author one 60-question subject at a time. Independently solve from the stem and figure before checking the intended key. Reject equivalent options, loose rounding, unstated assumptions and unfair time demand. Inspect every actual figure and confirm the required information is available, correct and readable.
4. Validate structure plus expected class/tier counts, keys, image existence and absence of detectable repeats. Treat lexical checks as candidate generation only. Use editorial comparison where stems take different forms but ask for the same reasoning. Preserve question and option order and the assigned IDs. Never run `shuffle_test.py`.
5. Record material scope coverage with the exact question ID and final source hash. Keep canonical JSON, delivery JSON, PDFs, HTML, figures, index and hashes in agreement. Rebuild and inspect affected outputs after a correction. Record what was solved, rendered and reviewed.
6. Use `pending_revision` for drafts. Use `revised` after the final file passes the applicable academic, structural, visual and delivery checks. Timed pilot feedback is needed before claiming calibrated pace; do not publish unsupported approval or coverage claims.

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
- [ ] Every key was re-derived during review. Resample changed or high-risk items after final assembly.
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
  "syllabus_source": "COMEDK/sources/<official subject syllabus PDF filename>",
  "notification_source": "COMEDK UGET Information Brochure, comedk.org",
  "past_paper_reference": "Source IDs and locators from PYQ/COMEDK/SOURCES.md, with source tier",
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

## Working efficiently

Use the catalog and page anchors for scope checks, then read the actual source where a qualifier or formula affects the decision. Draft by subject and checkpoint at a verified boundary. Record evidence and angle decisions as the work progresses. Keep a current handoff with the baseline, completed slots, open flags and next subject.
