# NISER / NEST Test Instructions (v2, 15 November 2026)

This is the single rule file for the NEST mock-test series (NISER Bhubaneswar and UM-DAE CEBS Mumbai). It replaces `docs/instructions/NISER_Instructions.md` (v1). It adds the lessons of the IAT audit, so the mistakes fixed there are not made again here.

| File | What it is |
|---|---|
| `NISER/NISER_Test_Instructions.md` | this file: rules, do's and don'ts, checklists |
| `NISER/Syllabus.md` | official NEST syllabus, by chapter, with the "not listed" topics |
| `NISER/NEST_25_Test_Plan.md` and `.csv` | the 25-test plan: 2,000 slots, one per question |
| `tools/nest/plan_25_tests.py` | builds and checks the plan (metadata only) |
| `docs/blueprints/nest_pyq_analysis.md` | what the 2024–2026 papers show: chapter counts, style, figures |
| `NISER/NEST_images.md` | one entry per figure question |
| `NISER/NEST TEST <N>.json` | the tests (not written yet) |

**Target:** NEST 2027. The 2027 brochure was not published on 15 November 2026, so the pattern and syllabus below are from the official NEST 2026 brochure and syllabus. Re-check both when the 2027 documents appear, and update this file and `Syllabus.md` before anything else.

---

## 1. Official exam pattern (NEST 2026 brochure, sections 7 and 14)

| Item | NEST pattern |
|---|---|
| Mode | Computer-based test |
| Sections | 4: Biology, Chemistry, Mathematics, Physics |
| Questions | 20 per section, 80 in the paper |
| Type | MCQ, 4 options, only one correct |
| Marks | 60 per section |
| Marking | +3 correct, −1 incorrect, 0 unanswered |
| Duration | 3 hours |
| Language | English and Hindi (we write English) |
| Aids | No calculators or log tables; a simple on-screen calculator is provided |
| Attempt rule | A candidate must attempt at least three sections |
| Total score | Sum of the best three section scores, counting only sections at or above the section cut-off (SMAS) |
| SMAS | 20% of the average of the best 100 scores in that section (90% of that for OBC, 50% for SC/ST) |

What this means for us:
- Every section must work alone as a complete 60-mark paper, because any three sections may count.
- Time is about 2¼ minutes a question for 80 questions, or 3 minutes if a student attempts three sections.
- Arithmetic must be possible by hand or with a basic calculator.

---

## 2. Series rules

| Rule | Value |
|---|---|
| Tests | 25, `NISER/NEST TEST 1.json` to `NEST TEST 25.json` |
| Questions | 80 per test, 2,000 in the series |
| Order | Biology Q1–20, Chemistry Q21–40, Mathematics Q41–60, Physics Q61–80 |
| IDs | `NEST27-TNN-QNN`, fixed for ever |
| Difficulty per section | 3 easy, 13 medium, 4 hard (12 / 52 / 16 per test) |
| Answer key per section | exactly 5 each of A, B, C, D; no letter more than 3 times in a row |
| Shuffling | never; questions and options stay in the authored order |
| Progression | Tests 1–8 most accessible, 9–17 deeper, 18–25 closest to the hardest PYQs. The 3/13/4 split does not change; the depth inside each label does |

---

## 3. The four defects we do not allow

These are the four things the IAT audit had to fix. Every NEST question is checked against them before it is written and again before it is committed.

1. **Out of syllabus.** Every question must map to a topic line in `NISER/Syllabus.md`. If the topic is in the "Not listed" lists there, the question is not written. Class 9–10 science may be used only as background.
2. **Not at PYQ standard or pattern.** Single-correct, four options, NEST style and depth. A one-line substitution is `easy`, never `medium`.
3. **Brief solutions.** Every solution is fully worked (section 6). A two-line explanation is a defect.
4. **Repetition and coverage gaps.** No question repeats another in the series, and every chapter and focus line in the plan gets its questions.

---

## 4. Do's

- **Do** read the plan rows for the test before writing: chapter, focus, angle and difficulty are already decided there.
- **Do** read `Syllabus.md` for the exact topic wording before writing each question.
- **Do** search the existing tests for the idea before writing it (section 7).
- **Do** solve the question completely first, then write the options, then place the correct option to balance the key.
- **Do** build each wrong option from a real, nameable mistake, and say that mistake in the solution.
- **Do** put all data needed to solve the question in the question text.
- **Do** use SI units, standard constants and NCERT conventions; state any constant the student needs (for example g = 10 m s⁻², hc = 1240 eV nm).
- **Do** write KaTeX for mathematics and mhchem for chemistry, correctly JSON-escaped.
- **Do** open a figure and read its values before writing a solution that says "from the figure".
- **Do** update the plan row (`state`, `source_json`, `question_sha256`) in the same commit as the test.
- **Do** say so plainly if a source is missing or an answer is ambiguous, and ask. Never guess.
- **Do** work in batches of five tests and commit one test at a time: `NEST Test <n>: <summary>`.

## 5. Don'ts

- **Don't** copy or lightly reword a previous-year question. PYQs are analysed for pattern only.
- **Don't** copy an IAT question into NEST, and don't reuse its numbers with a new story.
- **Don't** write number-swapped or reworded copies of an earlier NEST question.
- **Don't** use scripts to write question text, options, numbers or answers. Scripts only count, validate and compare.
- **Don't** choose the answer letter before solving.
- **Don't** use "all of the above", "none of the above" or two options that mean the same thing.
- **Don't** set questions on topics in the "Not listed" lists: for example radioactive decay law, optical instruments, equation of a plane, potentiometer, error propagation, binomial distribution, solid state, surface chemistry, polymers, transport in plants.
- **Don't** relabel difficulty to make the counts fit. Change the question instead.
- **Don't** shuffle, renumber or reorder after authoring.
- **Don't** add a figure unless the question needs it. Never add a decorative figure.
- **Don't** change a question that is already correct. When fixing, change only the defect.
- **Don't** store PYQ PDFs in the repository (it is public).
- **Don't** change the marking scheme or section sizes.

---

## 6. Solutions (strict)

First line of every solution: `Answer: (X) <the option text>.`

### Mathematics and Physics: equations only

No explanatory English sentences. Each line is a labelled equation or a short labelled fact inside `\(...\)`.

```
Answer: (C) 6.
Given: \(...data with units...\)
Formula/Principle: \(...the law or identity used...\)
Step 1: \(...\)
Step 2: \(...\)
Worked derivation: \[...final substitution and value with units...\]
Check: \[...an independent check: a second method, a limiting case, units, or substitution back...\]
Why: \(...the one idea that makes the method work...\)
Why not the others: (A) \(...the slip that gives A...\); (B) \(...\); (D) \(...\).
Key point: \(...the formula or rule to remember...\)
```

Rules: every algebra step is shown; every numerical value carries its unit; the final value equals the keyed option; the check is a real second route, not a repeat.

### Chemistry and Biology: concept, reasoning, why each wrong option is wrong

```
Answer: (B) ...
Concept: the idea being tested, in one or two sentences.
Why: the reasoning that leads to the correct option, step by step.
Why not the others: (A) what is wrong in it, and the mistake that leads there. (C) ... (D) ...
Key point: the fact or rule to remember.
```

Numerical Chemistry questions also carry `Given:`, `Formula/Principle:`, `Step 1:` … and a displayed final calculation. Reaction questions show the equation in mhchem.

---

## 7. No repetition: the procedure

1. **Plan level.** `NEST_25_Test_Plan.csv` gives every slot a different (chapter, focus, angle). `python3 tools/nest/plan_25_tests.py --check` fails if two slots share one.
2. **Before writing a question.** Search the NEST tests already written, and the IAT bank, for the same idea: `python3 tools/iat/grep_bank.py '<regex>'` for IAT, and the same search over `NISER/NEST*.json`. Compare **method and situation**, not only wording.
3. **Read the ledger by hand.** For each chapter, read the earlier questions of that chapter in full before drafting the next one. A wording-overlap score misses reworded repeats.
4. **After each test.** Run a series-wide wording screen and read every flagged pair. Two questions repeat if a student who solved one would solve the other by the same steps.
5. **What counts as a repeat:** same concept with the same method and a similar situation, even with new numbers or a new story. Same chapter with a different task is not a repeat.

---

## 8. Syllabus coverage

- The plan gives each subject 500 slots. Every chapter in `Syllabus.md` has slots, and every focus line is used at least once (the checker enforces this).
- Class 11 / Class 12 slots: Biology 250 / 250, Chemistry 255 / 245, Mathematics 290 / 210, Physics 260 / 240 (see the plan for the current numbers).
- Chapter weights are 60% syllabus breadth and 40% share in the NEST 2024 (two sessions), 2025 and 2026 papers, with a minimum of 5 slots, so no listed chapter is dropped. The largest chapters have 40 slots (inheritance, molecular basis of inheritance, equilibrium, hydrocarbons, coordination compounds, relations and functions, conics, integrals); the smallest have 5.
- The past-paper sample is 80 questions per subject. Re-check the weights if NEST 2027 changes the pattern or when more papers are analysed.
- If a slot must be changed during authoring, edit its CSV row, write the reason in `notes`, and keep the chapter's total unless the user agrees otherwise.

---

### Style targets from the past papers

- **Biology:** at least 10 of the 20 questions are experiment, data-table, pedigree, graph or applied-case questions. Recall-only questions belong in the easy slots.
- **Chemistry:** about one-third organic, one-third inorganic, one-third physical in each section (the plan gives the exact chapters). Organic questions are mostly two- or three-step sequences or reasoned orderings.
- **Mathematics:** prefer "number of solutions", "which statement must hold" and parameter-condition questions to long routine computation.
- **Physics:** one or two estimation or real-context questions per section; a dimensional-analysis or significant-figure question in most tests.

---

## 9. Figures

- A figure is used only when text or KaTeX cannot carry the information (graph, circuit, apparatus, structure, pedigree, gel, anatomical diagram).
- At most 2 figure questions per section in Biology, Chemistry and Physics, and normally none in Mathematics, placed on slots whose angle is a graph, data, structure or experiment task.
- File name `NEST_T<NN>_Q<NN>.png`, set in `image_reference`, with a full entry in `NISER/NEST_images.md` (purpose, size, style, what it must show, axes, labels, what it must not show, alt text).
- The image prompt must be complete enough that the figure can be drawn without reading the solution, and must never reveal the answer.
- Figures are produced and checked by the user. A figure question is not changed after its image exists, unless the user asks.

---

## 10. Before Test 1 (pre-start checklist)

- [ ] NEST 2027 brochure checked; pattern table and `Syllabus.md` updated if anything changed.
- [x] PYQ analysis written in `docs/blueprints/nest_pyq_analysis.md` from the official papers on `https://www.nestexam.in` (NEST 2024 two sessions, 2025, 2026; 320 questions). Tags are in `docs/blueprints/nest_pyq_tags.txt`. The papers themselves are not stored.
- [x] Chapter weights in the plan adjusted to the PYQ analysis; plan regenerated and checked (15 November 2026).
- [ ] The user has approved the PYQ summary and the plan.
- [ ] `validate_nest.py` written: 80 questions, 20 per section, fixed IDs, 3/13/4 per section, 5/5/5/5 keys per section, required solution labels, KaTeX check, image-register match.
- [ ] Test 1 written as the pilot and approved by the user before Tests 2–25.

## 11. Per-test workflow

1. Print the 80 plan rows for the test.
2. For each row: read the syllabus line, search for earlier questions on the idea, solve, write the question, options and solution.
3. Add image entries for figure questions.
4. Run the validator, the KaTeX check and the series-wide repetition screen; read every flagged pair.
5. Re-solve the whole test independently of the key (not a sample).
6. Update the plan rows and run `python3 tools/nest/plan_25_tests.py --check`.
7. Commit `NEST Test <n>: <summary>` and push.

## 12. Quality checklist (every test)

**Syllabus**
- [ ] Each question maps to a line in `Syllabus.md`; none uses a "Not listed" topic.
- [ ] Each question matches its plan row (chapter, focus, angle, difficulty) or the row was updated with a reason.

**Pattern and difficulty**
- [ ] 80 single-correct MCQs, 20 per section, in the fixed order with fixed IDs.
- [ ] 3 / 13 / 4 in every section, and each label matches the real effort.
- [ ] Solvable by hand in the time budget.

**Correctness**
- [ ] Exactly one correct option, re-derived independently.
- [ ] Each distractor comes from a nameable mistake; no two options are equivalent.
- [ ] 5 / 5 / 5 / 5 keys in every section.

**Solutions**
- [ ] Mathematics and Physics: equations only, all steps, units, a real check, final value equals the key.
- [ ] Chemistry and Biology: concept, reasoning, and why each wrong option is wrong.
- [ ] KaTeX and mhchem render with no errors.

**Repetition and records**
- [ ] No repeat inside the test, in the NEST series, or of an IAT question.
- [ ] Every `image_reference` has a register entry and the reverse.
- [ ] Plan rows updated; plan check passes; one commit for the test.

---

## 13. JSON format

Top-level fields: `test_id` (`NEST27_TEST_<NN>`), `series_id` (`NEST27`), `exam`, `title`, `test_number`, `status`, `syllabus_source` (`NISER/Syllabus.md`), `notification_source`, `duration_minutes` (180), `total_questions` (80), `marking_scheme` (`+3`, `-1`, `0`), `scoring_rule` (best three sections), `instructions`, `sections`, `questions`.

Each question:

```json
{
  "id": "NEST27-T01-Q01",
  "section": "B | C | M | P",
  "subject": "Biology | Chemistry | Mathematics | Physics",
  "topic": "chapter name as in Syllabus.md",
  "sub_topic": "the plan focus, made specific",
  "class_level": "11 | 12",
  "difficulty": "easy | medium | hard",
  "format": "conceptual | numerical | graph | data | diagram | experiment",
  "question": "full text",
  "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
  "correct_option": "A | B | C | D",
  "explanation": "Answer: (X) ...\n...",
  "image_reference": "NEST_T01_Q01.png (only if needed)",
  "image_alt": "one sentence (only if needed)"
}
```

---

## 14. Working efficiently

- Read `Syllabus.md` and the plan rows; do not re-read the brochure PDF.
- Prevent repeats at planning and drafting time; fixing them later costs far more.
- When auditing, change only the four defect types in section 3 and leave correct questions and figure questions alone.
- Keep tool output short: print only the rows or questions being worked on.

If a request conflicts with this file, say what the conflict is and ask before going on.
