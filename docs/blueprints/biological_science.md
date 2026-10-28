# Blueprint — CUET (UG) 2027 Biological Science (304)

**Syllabus:** `CUET SYLLABUS/md/Biological Science - 304.md` (NTA "for the year 2026", latest published). The syllabus is **Class 12 NCERT only**, numbered Units VI–X.
**Series:** 15 tests, `CUET/Biological Science/CUET BIOLOGICAL SCIENCE TEST 1–15.json`.

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (no internal choice) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (CUET 2024–2025 Biology — analysed, not stored)

Source: shift-wise reports in [Careers360 — CUET 2025 Biology question paper analysis](https://university.careers360.com/articles/cuet-2025-biology-question-paper-analysis), plus the formats NTA has used since 2024. These are student accounts, not official NTA data.

- **Difficulty:** most shifts were easy to moderate; a few were moderate. Questions are NCERT-driven, often lifted from NCERT lines, figures and tables.
- **Formats seen:** direct factual questions (the majority), Match List-I/List-II, statement-based "which are correct", assertion–reason, sequence arrangement (for example the stages of pollen development), **passage-based sets of five questions** (for example on the immune system), and diagram or flowchart questions (for example a population age pyramid).
- **Frequently asked:** gametogenesis, contraceptives and ART (GIFT, IUDs), embryo sac; HIV, malaria life cycle, Widal test, immunity; phenylketonuria, sex-linked inheritance, test cross, codons; in-situ and ex-situ conservation, age pyramids, productivity; insulin, EcoRI, gel electrophoresis, Cry genes.

**What this means for OurMocks:** CUET Biology is less about long reasoning than about **precise NCERT knowledge under time pressure, with close distractors**. Our "medium" and "hard" questions get their difficulty from close options, two-fact links, data or diagram reading, and multi-statement judgement — not from content beyond NCERT.

## 3. Unit weight per test (50 questions)

| Unit | Chapter | Qs |
|---|---|---|
| VI Reproduction (11) | Sexual reproduction in flowering plants | 4 |
| | Human reproduction | 4 |
| | Reproductive health | 3 |
| VII Genetics and Evolution (14) | Principles of inheritance and variation | 5 |
| | Molecular basis of inheritance | 6 |
| | Evolution | 3 |
| VIII Biology and Human Welfare (8) | Human health and disease | 5 |
| | Microbes in human welfare | 3 |
| IX Biotechnology (8) | Principles and processes | 4 |
| | Applications | 4 |
| X Ecology (9) | Organisms and populations | 3 |
| | Ecosystem | 3 |
| | Biodiversity and conservation | 3 |
| **Total** | | **50** |

The five-question passage set counts towards its chapter's quota; the chapter's other questions are reduced to keep the totals above. A case set may span two chapters of the same unit.

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.** Rough split: VI 2/7/2, VII 2/9/3, VIII 1/5/2, IX 1/6/1, X 2/5/2 (adjust ±1 between units so the totals stay 8/32/10).

- **Easy:** one NCERT fact or idea, cleanly asked, with plausible options.
- **Medium:** two linked facts, a close distractor set, or a short application (cross, ratio, pathway step).
- **Hard:** multi-statement judgement, data or pedigree reading, a two-step genetics problem, or linking concepts across chapters — all within NCERT.
- **Depth progression:** Tests 1–5 accessible, 6–10 deeper, 11–15 hardest (more close options, more data and two-step reasoning).

## 5. Formats (every test)

| Format | Count |
|---|---|
| Passage / case set (one passage, 5 linked questions) | 5 |
| Match List-I / List-II | 5 |
| Statements "(A)–(D), choose the correct" | 5 |
| Assertion–Reason | 3 |
| Sequence / order | 2 |
| Data, table or described-diagram reading | 2 |
| Direct concept and application (including genetics numericals) | 28 |

Non-direct formats = 22 of 50 (44%), above the 30% floor.

## 6. Key and order

- Key per test: 13 / 12 / 13 / 12 (rotate which letters get 13); no letter more than 3 times in a row.
- `shuffle_test.py` puts the questions in random exam order and keeps the case set together at the end.

## 7. Explanations

- Concept questions: `Answer:` → `Why` → `Why not the others` (one line each) → `Key point`.
- Genetics and other numericals: `Answer:` → `Given` → `Step 1…n` (Punnett or ratio working shown) → `Common mistake`.
- Every explanation states the NCERT fact it relies on.

## 8. Out of syllabus — never test

- Complement system / membrane attack complex; next-generation sequencing (both flagged by the audit).
- Class 11 topics (classification, cell biology, physiology) except as background a Class 12 question cannot avoid.
- Chapters NCERT removed and the syllabus omits: Reproduction in Organisms (asexual reproduction), Strategies for Enhancement in Food Production (animal husbandry, plant breeding, SCP), Environmental Issues (pollution, ozone, global warming).
- Detailed immunology beyond NCERT (T-cell subtypes beyond helper/killer, MHC), named drugs beyond NCERT, details of DNA sequencing methods.

## 9. Images

Prefer text: pedigrees as written descriptions or text tables, age pyramids as data tables. Where a figure is unavoidable, add `image_reference` and an entry in `CUET/Biological Science/CUET_Biological_Science_images.md` (format: `docs/instructions/IAT_Instructions.md` → Images).
