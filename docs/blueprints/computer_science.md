# Blueprint — CUET (UG) 2027 Computer Science / Informatics Practices (308)

**Syllabus:** `CUET SYLLABUS/md/Computer Science - 308.md` (NTA "for the year 2026", latest published).
**Series:** 15 tests, `CUET/Computer Science/CUET COMPUTER SCIENCE TEST 1–15.json`.

## 1. Paper pattern

| Item | Value |
|---|---|
| Sections | **A** (common: Database Concepts, SQL I and II, Computer Networks) — 15 questions; **B1** Computer Science — 35 questions; **B2** Informatics Practices — 35 questions |
| A candidate attempts | all 15 of Section A **plus** all 35 of EITHER B1 OR B2 = **50** (the bulletin's "50 questions, all compulsory") |
| Questions in each file | 85 (15 + 35 + 35) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

Evidence: the NTA bulletin (50 compulsory questions per test paper) and the structure of the 2025 paper (85 numbered questions: common Section A, then B1 and B2), analysed but not copied; [Physics Wallah](https://www.pw.live/exams/cuet/cuet-2025-computer-science-chapter-wise-weightage/) and [Careers360](https://www.careers360.com/question-i-am-about-to-give-cuet-exam-2025-and-i-have-opted-for-cs-as-one-of-the-subjectsi-had-cs-in-class-12-rather-than-ipbut-the-question-paper-consists-of-2-b-parts-and-i-am-confused-whether-both-are-compulsary-to-attempt-or-optional-as-b2-is-solely-based-upon-ip-do-i-need-to-study-ip-too/amp) describe Section A as 15 common questions and B1/B2 as the CS and IP parts. The file uses `sections`, `common_sections: ["A"]` and `optional_sections: ["B1","B2"]`, as for Accountancy.

## 2. PYQ analysis (CUET 2025 paper — analysed, not stored)

- **Formats seen:** direct concept MCQs, many **SQL output** questions on a small given table (COUNT with NULL, ROUND, MID/INSTR, NOW format), **Python code** questions (file modes, pickle, exception order), **postfix evaluation**, dry runs of binary search and bubble sort, **Match List-I/List-II** (about 8 in the paper), **arrange in order** (exception-handling blocks, steps of linear search, bubble sort steps, series-from-dictionary steps), "identify the incorrect statement", and scenario questions (repeaters, DoS, recording a video as data).
- **Section A** stresses relational algebra (selection, projection, set operations, join), keys, constraints (DEFAULT), DISTINCT, LIKE, and IP addresses.
- **B1** has about 5 exception/file questions, 3–4 stack/queue, 3 searching, 2–3 sorting, 3 data/statistics, 5 database/SQL, 3 data communication, 3 security.
- **B2** has about 5 SQL, 6–7 Pandas I, 5 Pandas II, 6–7 Matplotlib, 4–5 networks/web, 4–5 societal impacts.
- **Difficulty:** mostly easy to moderate; difficulty comes from exact syntax, close options and dry runs.

**What this means for OurMocks:** precise NCERT (CS/IP Class 11–12 as named in the syllabus) knowledge, exact Python/MySQL/Pandas behaviour, and small dry runs — every output is computed and checked, never guessed.

## 3. Weight per test

| Section | Unit | Qs |
|---|---|---|
| **A (15)** | Database concepts | 4 |
| | SQL I (DDL/DML, math and text functions) | 4 |
| | SQL II (date, aggregate, GROUP BY/HAVING/ORDER BY, set operations, JOIN) | 4 |
| | Computer networks | 3 |
| **B1 (35)** | Exception handling and file handling | 5 |
| | Stack | 4 |
| | Queue and deque | 3 |
| | Searching and hashing | 4 |
| | Sorting | 3 |
| | Understanding data | 3 |
| | Database concepts and SQL (B1 depth: constraints, data types, queries) | 6 |
| | Networks, DNS and data communication | 4 |
| | Security aspects | 3 |
| **B2 (35)** | SQL queries (functions, aggregates, GROUP BY) | 5 |
| | Pandas I (Series, DataFrame, indexing, CSV) | 8 |
| | Pandas II (statistics, groupby, sorting, pivot, missing values, SQL link) | 6 |
| | Matplotlib | 6 |
| | Networks and the web | 4 |
| | Societal impacts | 5 |
| | Project-based learning | 1 |

Each optional section has its own 5-question case set, which counts inside its unit's quota.

## 4. Difficulty

Every attempt path (A + B1, A + B2) is **8 easy / 32 medium / 10 hard**: Section A 2 / 10 / 3; B1 6 / 22 / 7; B2 6 / 22 / 7.

## 5. Formats (per section)

| Format | A | B1 | B2 |
|---|---|---|---|
| Case set (5 linked questions) | — | 5 | 5 |
| Match List-I / List-II | 1 | 4 | 4 |
| Statements "(A)–(D), choose the correct" | 1 | 4 | 4 |
| Assertion–Reason | 1 | 2 | 2 |
| Arrange in order | 1 | 2 | 2 |
| Output / dry run (SQL result, Python output, postfix value, search/sort pass) | 4 | 6 | 6 |
| Direct concept | 7 | 12 | 12 |

Per path: 5 match, 5 statements, 3 AR, 3 sequence, 10 output/dry-run, 5 case.

## 6. Key and order

Key per section about even (A 4/4/4/3; B1 and B2 9/9/9/8, rotating); no letter more than 3 times in a row; correct option never clearly the longest. `shuffle_test.py` keeps sections separate and the case set together at the end of its section.

## 7. Writing code in questions

- Python code and SQL are written in plain text inside the question with `\n` line breaks and 4-space indentation. Every Python output is executed before release; every SQL result is worked out on the given rows using MySQL rules (NULLs ignored by aggregates except COUNT(*), ROUND half away from zero, MID/SUBSTRING 1-based, INSTR returns 0 when absent).
- Tables are given as text tables with a header row.

## 8. Explanations

- Output questions: `Answer:` → `Given` → `Step 1…n` (trace) → `Common mistake`.
- Concept questions: `Answer:` → `Why` → `Why not the others` → `Key point`.
- Every explanation follows NCERT Computer Science / Informatics Practices.

## 9. Out of syllabus — never test

Python topics outside the syllabus (classes/OOP, recursion questions not linked to the units, lambda-heavy code), SQL beyond the list (sub-queries, views, triggers, stored procedures, indexes), NumPy beyond its mention, network layers beyond NCERT (OSI model detail, subnetting), cryptography algorithms.
