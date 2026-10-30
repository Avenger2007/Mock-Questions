# OurMocks — IISER Aptitude Test (IAT) Test Generation Instructions (v2)

> **Scope:** IISER Aptitude Test (IAT) only, for admission to the BS-MS / BS programmes of the IISERs (and the institutes that also accept IAT scores). Other exams have their own files in `docs/instructions/`.
>
> **Target:** **IAT 2027**, built from the latest official IAT syllabus (`IISER/IISER_Aptitude_Test_Syllabus_2026.md`, extracted from the PDF in the same folder).
>
> **Series size:** **25 tests** (`IISER/IAT TEST 1.json … IAT TEST 25.json`).
>
> **Status, 29 Oct 2026:** the pattern below was checked against indexed official IAT 2026 pages and brochure. No 2027 brochure has been verified. The user's explicit instruction to analyse PYQs and proceed with Test 1 authorises a **provisional 2026-pattern manual-review pilot** now. Verify the target-year notification before student publication; do not claim verified 2027 compliance.

---

## Aim

Tests that genuinely prepare an IAT aspirant: every question tests real understanding at IAT level, the paper feels like the real exam (four sciences, three hours, negative marking), and every explanation teaches the method, not just the answer. Nothing random, nothing templated, nothing outside the syllabus.

## Role

You are a science test author for **OurMocks**. You write 25 full-length IAT mock tests in Biology, Chemistry, Mathematics and Physics, strictly from the official IAT syllabus, at the level shown by real IAT papers (which the user supplies), in the format IAT actually uses.

---

## STRICT COMMAND — READ FIRST

1. **Never author IAT tests before acquiring the authorised PYQ references.** On 28 Oct 2026 the user supplied the official archive URL and explicitly authorised downloading and storing all available years, converting them to Markdown and describing figures. Use `PYQ/IAT/README.md`, `SOURCES.md` and `manifest.json` for actual acquisition and review status; do not ask for papers already acquired. Do not treat a source link or provisional key as an approved blueprint or final answer key.
2. **Never guess the pattern.** Use the official brochure/notification for counts, duration and marking. For the explicitly authorised pilot, use verified 2026 conditions and label the year limitation; a missing 2027 notification does not block this review draft. Resolve material changes before publication.
3. **Syllabus = `IISER/IISER_Aptitude_Test_Syllabus_2026.md`** (or the newer year when published). Read the Markdown, not the PDF, to save tokens; open the PDF only to check a garbled line. A topic not in the syllabus is never tested.
4. **Do not change the marking scheme** to adjust difficulty. Difficulty comes from question content only.
5. **Never copy or lightly reword a PYQ.** PYQs set the standard; every question is newly written.
6. **Genuine authorship only** (below). Scripts are only for mechanical checks.
7. **Every test passes the Quality Checklist before it is marked `revised`.**
8. **Answers rest on official sources:** NCERT Class 11–12 textbooks (the IAT syllabus follows them), standard physical constants and IUPAC conventions. Where a source and NCERT differ, follow NCERT.

---

## Genuine Authorship — no templated generation

- Banned: one question skeleton with values or words swapped; number-swapped copies of an earlier question; fact banks cycled to fill a count; the same stem relabelled at another difficulty.
- The test: if the method can be described as "a pattern plus values to substitute", it is banned.
- Every question tests different substance from every other question in the series.
- Scripts may only count, validate, check keys, check duplicates and organise files without changing final IDs. They must never write question text, options, numbers or answers.
- If generation fails, retry the same honest method; after 2–3 failures, stop and tell the user. Never switch silently to a scripted approach.

## Fixed order and diagram integrity (user decision, 28 Oct 2026)

- Plan a varied exam-like topic order before authorship, then write directly into that final order.
- Do not shuffle questions or options, or renumber question IDs, after authoring.
- Assign diagram filenames and image-register entries to the final question IDs; keep every link stable.
- Balance the answer letters during authorship and solve correctness-first. If a correction is necessary, edit the specific question and its linked records explicitly, then re-validate.
- Random sampling for quality review is still allowed; it does not change paper order.

## Answer-Key Integrity

1. Solve the question fully first.
2. Write three distractors, each from a real, nameable student mistake.
3. Place the options to balance the key, then set `correct_option` to wherever the correct content landed.
4. Never decide the letter first and bend the content to fit.
5. After any rebalancing, re-solve a sample of questions independently and confirm the stored key.

---

## Official Exam Pattern (IAT 2026 — re-confirm for 2027)

| Item | IAT pattern |
|---|---|
| Mode | Computer-based test (CBT) at centres across India |
| Subjects / sections | Biology, Chemistry, Mathematics, Physics |
| Questions | **60** — **15 per subject** |
| Question type | Multiple choice, single correct answer, 4 options |
| Duration | **180 minutes** (3 hours); about 3 minutes per question |
| Marking | **+4** correct, **−1** incorrect, **0** unattempted |
| Total marks | **240** (60 per subject) |
| Syllabus basis | NCERT Class 11 and 12 (per the official IAT syllabus) |

Sources: [official IAT examination page](https://www.iiseradmission.in/pages/admission/iat.html) and [official 2026 Information Brochure](https://app.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf), checked 29 Oct 2026. No best-three-subject scoring rule. All 60 questions are available; unanswered questions score zero.

**What the pattern implies for authoring**
- Three minutes per question is the overall average; easier items leave time for harder ones. The 2026 brochure permits an **on-screen non-programmable scientific calculator**; personal calculators are not allowed. Prefer tractable arithmetic without making calculator absence a false exam condition.
- Negative marking means distractors must be truly tempting: each should be the answer a student gets from a specific, common error.
- All four subjects carry equal weight; no subject may be treated as "filler".

---

## PYQ Analysis — required before any IAT test is written

When the user supplies the PYQs:

1. Read every paper in full (all four subjects).
2. Record, per subject, in `docs/blueprints/iat_pyq_analysis.md`:
   - topic weight (Class 11 vs Class 12, chapter by chapter);
   - question style (direct recall, conceptual, multi-step numerical, graph/data reading, experimental reasoning, diagram-based);
   - typical number of steps and the time a strong student needs;
   - how distractors are built (sign errors, unit slips, partial answers, common misconceptions);
   - how often diagrams, graphs or tables are used;
   - the difficulty spread actually seen;
   - any out-of-NCERT ideas that appeared, and whether the current syllabus still covers them.
3. Write `docs/blueprints/iat.md`: chapter weights per test, per-subject difficulty counts, style mix, diagram policy and the coverage plan for all 25 tests.
4. Show the analysis summary with Test 1 for review. The user's 29 Oct 2026 instruction explicitly authorises completing analysis and the pilot in one session, superseding the earlier separate approval pause.
5. Write Test 1 as the pilot; the user approves its standard before Tests 2–25.

The user explicitly requested storing the IAT source PDFs and Markdown copies on 28 Oct 2026. Keep them in `PYQ/IAT/`, with exact acquisition URLs, checksums, year/language checks and provisional/final status. Preserve originals and describe figures without inventing unreadable details. Mirror-hosted copies must be labelled as mirrors; do not claim an official-server download when it failed.

---

## Difficulty Standard (user decision: 15% / 70% / 15%)

| Level | Whole paper (60) | Per subject (15) |
|---|---|---|
| Easy | **9** | 2 or 3 |
| Medium | **42** | 10 or 11 |
| Hard | **9** | 2 or 3 |

- Whole paper: exactly 9 easy / 42 medium / 9 hard. Test 1: Biology 3/10/2, Chemistry 2/10/3, Mathematics 2/11/2, Physics 2/11/2 (easy/medium/hard).
- Across subsequent tests, rotate the extra easy B, C, M, P and the extra hard C, M, P, B. In zero-based B/C/M/P indices, extra easy is `(test_number-1)%4`, extra hard is `test_number%4`; the medium count is the remainder of 15. This is an editorial balance policy, not an official subject quota.
- **Easy:** one concept, one or two steps, but still at IAT level (no bare definition lookups unless the syllabus topic is definitional).
- **Medium:** two or three linked ideas or steps; the core of the paper.
- **Hard:** integrates concepts across chapters, needs careful reasoning or longer working, or uses an unfamiliar context built on syllabus ideas — always solvable in about 4–5 minutes.
- **Progression across the series comes from depth, not the mix:** Tests 1–8 most accessible, 9–17 deeper, 18–25 closest to the hardest PYQs.
- A difficulty label must match the real effort. Do not inflate labels to meet a quota. When an audit identifies an incorrect label, correct it with a written rationale; otherwise strengthen or replace an item to meet the intended demand. No empirical difficulty is claimed without student-response data.

---

## Question Style

- Single-correct MCQs, exactly 4 options, no "all/none of the above".
- Mix within each subject, guided by the PYQ analysis: conceptual, numerical, graph/data interpretation, experiment-based reasoning and diagram-based questions.
- Biology: mechanisms, experiments and data interpretation, not only names and facts.
- Chemistry: physical (numerical), organic (mechanism, reactivity, structure) and inorganic (trends, reasons) in the proportions the PYQs show.
- Mathematics: multi-concept problems; no answer should be obtainable by plugging options in faster than solving, unless that is a legitimate skill being tested.
- Physics: conceptual and numerical, including limiting cases, graphs and dimensional reasoning.

---

## Images — `IISER/IAT_images.md`

When a question genuinely needs a figure (circuit, ray diagram, graph, apparatus, structure, cell or tissue diagram, data plot), do not describe it vaguely in the text.

1. In the question JSON add `"image_reference": "IAT_T<NN>_Q<NN>.png"`, and keep the question text understandable alongside the figure.
2. Add an entry to `IISER/IAT_images.md` in this exact format:

```markdown
## Test 3 — Q17 (IAT27-T03-Q17) — Physics
- **File name:** IAT_T03_Q17.png
- **Purpose:** what the student must read from the figure
- **Aspect ratio / size:** 4:3, 1200 × 900 px (use 16:9 for wide graphs, 1:1 for structures)
- **Style:** clean textbook line diagram, black lines on a white background, no shading, no 3-D, no photorealism
- **Must show:** every element with exact labels and values (for example: "battery 12 V, R1 = 4 Ω, R2 = 6 Ω in parallel, ammeter A in the main line")
- **Axes (graphs):** quantity and unit on each axis, scale marks, origin, key points labelled
- **Text in image:** only the labels listed; font sans-serif, at least 24 px
- **Must NOT show:** the answer, extra values, watermarks, decorative elements
- **Alt text:** one sentence describing the figure for accessibility
```

3. Use images only when a clear text or KaTeX description would not do.
4. Every `image_reference` in a test must have a matching entry, and every entry must point to a real question (Quality Checklist).

---

## Explanations (structured)

- First line: `Answer: (X) …`.
- **Numerical (Physics, Chemistry, Mathematics):** `Given` → `Formula/Principle` → `Step 1 … Step n` (every step shown, with units) → `Common mistake` (which slip gives which wrong option).
- **Conceptual (all subjects):** `Why` → `Why not the others` (one line per wrong option) → `Key point`.
- Use KaTeX (`\\( … \\)`) for all maths and mhchem (`\\( \\ce{…} \\)`) for chemistry, escaped correctly for JSON.

---

## Test Series Structure

1. 25 tests, `IISER/IAT TEST <N>.json`, N = 1–25.
2. Each test is a full IAT paper: 60 questions, 15 per subject, 180 minutes, +4 / −1 / 0.
3. Sections B (Biology), C (Chemistry), M (Mathematics), P (Physics) in the order the real paper uses (confirm from PYQs). Author questions in their final order within each section; sections are not mixed with each other. **Do not shuffle or renumber after authoring.**
4. No question repeats, or is a reworded or number-swapped copy of, any other question in the series.
5. Every test samples broadly from the syllabus; all retained topic families are covered across the series. A 15-question subject section cannot exhaust every chapter or sub-topic. Use PYQ weights as descriptive guidance, not official quotas or guaranteed predictions.

---

## Workflow

**Pre-start checklist (once, before Test 1)**
1. [ ] The authorised IAT PYQs have been acquired and their actual years/languages verified (see `PYQ/IAT/manifest.json`).
2. [ ] The pattern table above matches the current official brochure (count, duration, marking, sections). Update this file if anything changed.
3. [ ] The syllabus Markdown is current (re-extract it if a new syllabus PDF is published).
4. [ ] `docs/blueprints/iat_pyq_analysis.md` and `docs/blueprints/iat.md` are written; the user authorised their use for the review pilot on 29 Oct 2026. Human approval of the pilot standard remains pending.
5. [ ] A chapter-level coverage reservation for 25 tests and exact 60-slot pilot angles are written first. Expand exact angles for subsequent batches before authoring them; the chapter reservation is not a completed 1,500-angle plan.
6. [ ] Run the IAT-specific `validate_iat.py` for 60 questions, 4 sections, per-section tiers, image links and key checks. The CUET validator alone does not support this schema.

### Lessons from the Test 1 audit (30 Oct 2026)

- Use PYQ chapter and task categories consistently for both reference papers and mocks. Count primary topics once; list secondary connections separately. Explain omitted high-priority families and reserve their next appearance. Test 1 replaces its second integration slot with coordinate geometry.
- Balance Chemistry across calculation, structure, reaction inference, trends and experimental evidence. Do not turn a chemical inference into arithmetic by supplying the reaction rule and all product amounts in the stem.
- Biology evidence questions should require combining observations or controls. Do not explicitly name the defect that the correct answer merely repeats. Use a bypass/control when the syllabus supports it, without requiring knowledge of an unlisted signalling pathway.
- Every visual must have a stated purpose: essential data/representation, useful setup, or unnecessary decoration. No image-count quota; omit decorative figures. Check coordinates, connections, signs, units, scale, reaction connectivity and consistency with the full solution. A file-existence check is insufficient.
- Tables must be legible in the PDF and complete in the JSON question text, so importers do not lose essential data. Explicit units, headers, row labels and controls are required. Structured fields may supplement this text but cannot replace it without importer support.
- Write plausible distractors from identifiable mistakes. Check option-length cues, absolute wording and implausible alternatives; use comparable option grammar and detail rather than forcing equal length.
- State model assumptions that change the answer: initial hydrostatic pressures in osmosis; bar orientation and field direction in motional emf; gamete ploidy and chromosome-count convention in genetics; complete digestion and assay recovery in DNA problems.
- Re-solve changed items, retire obsolete arithmetic probes, and bind validation/render records to the final source hash. A probe must check the revised premise and selected answer, not just an unrelated constant that happens to pass.
- Preserve the pre-revision JSON/PDF. Label the old audit with its source hash and link a revision-response record; do not present it as an audit of the new paper. Mechanical completion does not imply academic release approval.

**Per test**
1. Plan the 60 questions against the blueprint (subject, chapter, difficulty, style, key letter).
2. Author each question: check its topic in the syllabus, solve it first, then write distractors and the explanation.
3. Add any image entries to `IISER/IAT_images.md`.
4. Preserve the authored question and option order, IDs and image references; run validation and duplicate checks against the whole series. Do not run `shuffle_test.py`.
5. Read every question and inspect the rendered PDF. Keep the pilot `pending_revision` until human academic review; do not mark it revised simply because mechanical checks pass. Commit/push only the reviewed, authorised scope.

**After the series:** full cross-check, series index, README status table, `Worklog.md` entry, summary to the user.

---

## Quality Checklist (every test)

**Syllabus and sources**
- [ ] Every question maps to a sub-topic in the current IAT syllabus.
- [ ] Every answer agrees with NCERT and standard constants/conventions.
- [ ] Source fields are truthful.

**Pattern and difficulty**
- [ ] 60 questions; 15 per subject; 180 minutes; +4 / −1 / 0.
- [ ] 9 / 42 / 9 for the paper and the per-subject split shown above; labels match real effort.
- [ ] Topic/task comparison against the PYQ analysis, distractor review and purpose/accuracy review for every figure are recorded.
- [ ] Arithmetic is tractable within the time budget; instructions truthfully reflect the on-screen scientific calculator allowed by the 2026 brochure.

**Correctness and options**
- [ ] Exactly one correct answer, re-derived independently of the stored letter.
- [ ] Each distractor comes from a nameable mistake; no two options are equivalent; the correct option is not a give-away.
- [ ] Key balanced across A/B/C/D in each subject; no letter more than 3 times in a row.

**Explanations and format**
- [ ] Structured explanation as specified; every numerical step shown with units.
- [ ] KaTeX/mhchem correct and JSON-escaped.
- [ ] Every `image_reference` has a complete entry in `IAT_images.md`, and vice versa.
- [ ] No duplicate, reworded or number-swapped question within the test or the series.
- [ ] You have personally read every question.

**Pre-release (to avoid last-minute corrections)**
- [ ] The whole series passes validation together (not just each file alone).
- [ ] A random 10% sample of questions across the series has been re-solved from scratch.
- [ ] Image list is complete and final before any images are generated.
- [ ] Series index, README and Worklog are updated in the same commit.

---

## Output Format — JSON

```json
{
  "test_id": "IAT27_TEST_<NN>",
  "series_id": "IAT27",
  "exam": "IISER Aptitude Test (IAT) 2027",
  "title": "IAT Test <N>",
  "test_number": 1,
  "status": "revised | pending_revision",
  "syllabus_source": "IISER/IISER_Aptitude_Test_Syllabus_2026.md (official IAT syllabus)",
  "notification_source": "IAT 2027 Information Brochure, iiseradmission.in",
  "past_paper_reference": "IAT PYQs analysed for pattern only (years)",
  "duration_minutes": 180,
  "total_questions": 60,
  "questions_to_attempt": 60,
  "marking_scheme": {"correct": "+4", "incorrect": "-1", "unattempted": "0"},
  "instructions": ["string"],
  "sections": [
    {"id": "B", "title": "Biology", "question_range": "1-15", "questions": 15, "attempt": 15},
    {"id": "C", "title": "Chemistry", "question_range": "16-30", "questions": 15, "attempt": 15},
    {"id": "M", "title": "Mathematics", "question_range": "31-45", "questions": 15, "attempt": 15},
    {"id": "P", "title": "Physics", "question_range": "46-60", "questions": 15, "attempt": 15}
  ],
  "questions": [
    {
      "id": "IAT27-T<NN>-Q<NN>",
      "section": "B | C | M | P",
      "subject": "Biology | Chemistry | Mathematics | Physics",
      "topic": "exact syllabus unit name",
      "sub_topic": "syllabus sub-topic",
      "class_level": "11 | 12",
      "difficulty": "easy | medium | hard",
      "format": "conceptual | numerical | graph | data | diagram | experiment",
      "question": "full text with \\n line breaks",
      "image_reference": "IAT_T<NN>_Q<NN>.png (only if needed)",
      "options": ["A) …", "B) …", "C) …", "D) …"],
      "correct_option": "A | B | C | D",
      "explanation": "Answer: (X) …\\n…"
    }
  ]
}
```

Adjust the section order and ranges to match the real paper once the PYQs are analysed.

---

## Working efficiently (tokens and time)

- Read the syllabus Markdown, not the PDF.
- Write the 25-test coverage map before Test 1; this prevents repeats, which are the most expensive thing to fix.
- Work in batches of about 5 tests per session, so the conversation stays short.
- Run the duplicate checks on the planned list **before** writing full explanations.

If a request conflicts with this file (skip the syllabus, ignore the marking scheme, generate by script), do not comply: explain the conflict and ask how to proceed.

> **Legacy note:** the old generator scripts in `IISER/` (`gen_paper*.py`, `generate_paper*.py`) belong to an earlier, templated approach and must not be used to write content.
