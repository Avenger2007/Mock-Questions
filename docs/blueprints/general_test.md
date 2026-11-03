# Blueprint — CUET (UG) 2027 General Test (501)

**Syllabus:** `CUET SYLLABUS/md/General Test - 501.md` (NTA "for the year 2026", latest published). Topics: General Knowledge and Current Affairs; General Mental Ability and Numerical Ability; Quantitative Reasoning (simple application of basic mathematical concepts — arithmetic, algebra, geometry, mensuration, statistics); Logical and Analytical Reasoning; General Science and Environment Literacy.
**Series:** 15 tests, `CUET/General Test/CUET GENERAL TEST TEST 1–15.json` (existing file names kept).

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (no internal choice) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |
| Calculator | not allowed — every number is chosen so that it can be worked by hand in about a minute |

## 2. PYQ analysis (CUET 2025 and 2026 General Test — analysed, not stored)

Sources: shift-wise analyses of the 2025 and 2026 General Test published by Careers360, Physics Wallah, Self Studies and Career Launcher (candidate-reported, not NTA data), and memory-based question lists. No question was copied.

| Area | Share reported across shifts | What it looked like |
|---|---|---|
| Quantitative / numerical | about 12–20 | number system, percentage, ratio, profit and loss, SI/CI, time and work, speed and trains, averages, mensuration, mean/median/mode, probability, heights and distances, coordinate geometry; some passage- or table-based sets |
| Reasoning (mental ability + logical) | about 11–18 | series, coding-decoding, blood relations, direction, ranking, clock, calendar, analogy, classification, mirror/water images, seating arrangement, Venn diagrams, syllogism, assertion–reason |
| General knowledge and current affairs | about 15–20 (one shift about 30) | static GK weighted above current affairs; history (battles, dynasties, freedom movement, chronology), geography (dams, rivers, mountains, borders, neighbours), polity (Articles), books and authors, awards, sports, space missions; current affairs from the 12–18 months before the exam |
| General science and environment | about 3–6, inside GK | basic physics, chemistry and biology (human and animal senses, formulas, the Tyndall effect, nuclear fuel), ecology and environment |

Formats reported: mostly single-answer MCQs, with some **match-the-following**, **statement-based** items, **assertion–reason**, **chronological ordering**, and **data interpretation** from tables or bar graphs. Difficulty: mostly easy to moderate; harder shifts were long rather than deep, so time pressure matters.

**What this means for OurMocks:** quick, clean arithmetic with close distractors from common slips; reasoning that needs a careful step or two; accurate, checkable facts; and current affairs with dates.

## 3. Area weight per test (50 questions)

| Area | Code | Qs | Slots |
|---|---|---|---|
| **Numerical Ability and Quantitative Reasoning** | Q | 10 | number system, percentage or ratio (alternate), profit–loss–discount, simple/compound interest, time and work, speed–distance–time, averages / ages / mixtures, algebra, geometry or heights and distances (alternate), mensuration |
| | D | 5 | one data-interpretation set (a table of figures, written in text) with 5 linked questions: totals, percentages, ratios, average/median, change |
| **General Mental Ability** | M | 7 | number or letter series, coding–decoding, blood relations, direction sense, ranking / order, calendar or clock (alternate), analogy or classification |
| **Logical and Analytical Reasoning** | L | 6 | syllogism, seating or scheduling puzzle, Venn / sets, statement–conclusion or assumption, inequality or mathematical operations, assertion–reason |
| **General Knowledge (static)** | G | 8 | ancient/medieval history 1, modern India and the freedom movement 1, Indian geography 1, world geography 1, polity 2, economy 1, culture / books / firsts 1 |
| **General Science and Environment Literacy** | S | 9 | physics 2, chemistry 2, biology 2, environment 3 (ecology and biodiversity, climate and pollution, conservation laws, conventions and protected areas) |
| **Current Affairs** | C | 5 | national schemes and governance, international events, sports, science and space, awards / reports / appointments |
| **Total** | | **50** | |

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.** Rough split: quant + DI 2 / 10 / 3, reasoning 2 / 8 / 3, GK + science + CA 4 / 14 / 4 (±1).

- **Easy:** one fact, one formula or one direct step.
- **Medium:** two steps of arithmetic, a reasoning chain of two links, a close distractor set, or a match.
- **Hard:** a three-step problem, a puzzle with several conditions, a statement or assertion–reason item that needs every part right, or a DI question that combines two rows.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Data-interpretation set (one table, 5 linked questions) | 5 |
| Match List-I / List-II | 3 |
| Statements "(A)–(D), choose the correct" | 3 |
| Assertion–reason | 2 |
| Sequence / chronology | 2 |
| Direct | 35 |

Assertion–reason options follow NTA's standard form, written out in words: (A) both true and Reason explains Assertion; (B) both true, Reason does not explain Assertion; (C) Assertion true, Reason false; (D) Assertion false, Reason true.

## 6. Facts and sources

- **Static GK and science** follow NCERT (Classes 6–12 Social Science and Science), the Constitution of India, and official sites (PIB, ISRO, RBI, Census, MoEFCC). Facts that change (record holders, rankings, office-holders) are asked only with a date ("in 2025") or not at all.
- **Current affairs window:** January 2025 to October 2026. Every item is checked against an official or major news source when it is written, and the explanation states the date. Events after October 2026 cannot be covered yet: **the current-affairs items should be refreshed in early 2027**, before the exam, by replacing the oldest items with newer ones of the same type.
- Sensitive matters (military operations, communal or party-political disputes) are not used as current affairs.

## 7. Key and order

- Key per test about 13 / 12 / 13 / 12 (rotate); no letter more than 3 times in a row; the correct option is never clearly the longest.
- Numerical distractors come from real slips (wrong base for a percentage, simple interest in place of compound, adding instead of subtracting relative speed).
- `shuffle_test.py` gives random exam order and keeps the data-interpretation set together.

## 8. Explanations

- **Numerical and data questions:** `Answer:` → Given → Step 1, 2, … → Common mistake.
- **Reasoning:** `Answer:` → the steps or arrangement that decide it → why the other options fail → Key point.
- **GK, science and current affairs:** `Answer:` → Why (the fact, with source or date) → Why not the others → Key point.

## 9. Out of scope — never test

Advanced mathematics beyond Class 10 level application (calculus, matrices, complex numbers), figure-only non-verbal items that need a picture (the platform shows text), trivia with no learning value (exact numbers that no source agrees on), and current affairs that are disputed, sensitive or older than January 2025.
