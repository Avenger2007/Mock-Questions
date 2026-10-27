# Accountancy (301) — CUET (UG) 2027 test blueprint

**Source:** `CUET SYLLABUS/Accountancy - 301.pdf` (NTA syllabus for the year 2026, the latest published).
**Pattern reference:** NTA's official 2024 and 2025 Accountancy papers, analysed for pattern only. No questions were copied.

## Paper structure (follows NTA's Unit V choice, in force since May 2025)

| Section | Content | Questions | Candidate attempts |
|---|---|---|---|
| A | Units I–IV (compulsory) | 40 (Q1–40) | all 40 |
| B1 | Unit V: Analysis of Financial Statements | 10 (Q41–50) | **either** B1 |
| B2 | Optional to Unit V: Computerised Accounting System | 10 (Q51–60) | **or** B2 |

Each file has 60 questions, and a candidate attempts 50. The exam rules are 60 minutes, +5 for a correct answer, −1 for a wrong one and 0 if unattempted.
JSON fields: `total_questions: 60`, `questions_to_attempt: 50`, `common_sections: ["A"]`, `optional_sections: ["B1","B2"]`, and a `section` field on every question.

## Unit weighting in Section A (every test)

| Unit | Questions |
|---|---|
| I Accounting for Partnership | 8 |
| II Reconstitution of a Partnership Firm | 14 |
| III Dissolution of Partnership Firm (no piecemeal distribution, sale to a company or insolvency) | 5 |
| IV Company Accounts — Share and Debenture Capital | 13 |

## Difficulty (every test, either path = 8 easy / 32 medium / 10 hard)

| Section | Easy | Medium | Hard |
|---|---|---|---|
| A | 6 | 26 | 8 |
| B1 | 2 | 6 | 2 |
| B2 | 2 | 6 | 2 |

The tier mix is the same in all 25 tests. Later tests get harder through the questions themselves: more adjustments per numerical, longer cases and closer distractors. Test 1 is the most accessible and Test 25 the most demanding.

## Question formats (per test)

| Format | Section A | B1 | B2 |
|---|---|---|---|
| Case-based set (one passage, 5 linked questions; NTA 2025 style) | 1 set | — | — |
| Match List-I / List-II | 2 | 1 | 1 |
| Choose the correct statements (A)–(D) | 4 | 1 | 1 |
| Sequence / order | 1 | — | — |
| Assertion–Reason | 2 | — | — |
| Numerical (1–3 steps, more in later tests) | about 14 | about 5 | 2–3 |
| Direct concept | remainder | remainder | remainder |

## Answer key

The key is balanced across A, B, C and D on each path (12–13 each), with **no more than 3 identical answers in a row** (`validate_papers.py` checks this).

## Explanation format

The `explanation` field is a single string with sections separated by line breaks, and the first line is always `Answer: (X) …`.

- **Concept questions:** `Answer`, `Why`, `Why not the others` (one line per wrong option), `Key point`
- **Numerical questions:** `Answer`, `Given`, `Formula`, `Step 1…n`, `Common mistake` (which slip leads to which distractor)
