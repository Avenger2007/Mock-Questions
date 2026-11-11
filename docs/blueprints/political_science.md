# Blueprint — CUET (UG) 2027 Political Science (323)

**Syllabus:** `CUET SYLLABUS/Political Science - 323.pdf` (NTA "for the year 2026", the latest published). It has two parts:
- *Politics in India since Independence*: 9 units.
- *Contemporary World Politics*: 7 units.

Both parts follow the NCERT Class 12 textbooks of the same names. Where the NTA syllabus keeps a unit that the rationalised edition shortened or dropped, the earlier NCERT edition is the source.

**Series:** 15 tests, `CUET/Political Science/CUET POLITICAL SCIENCE TEST 1–15.json` (existing file names kept).

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (2025 onward; in 2024 candidates answered 40 of 50) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (analysed, not stored)

Papers were read for pattern only. They are kept outside the repo and never copied:
- the 2024 paper (code 323, booklet A, text layer);
- the 2026 paper (image scan).

Both came from AglaSem.

**2024 paper**
- About 37 direct items: names, years, full forms, and "who said / led / founded".
- 3 match-lists: party leaders and parties, Prime Ministers and their terms, indigenous peoples and regions.
- 1 "Statement I / Statement II" item, on the Second Five Year Plan.
- A 5-question set on a picture (the UN logo).
- A 5-question set on a passage about regional aspirations in the North-East.

**2026 paper**
- Chronological-order items in both books: European integration, and India's agreements with its South Asian neighbours.
- Match-lists, for example neighbouring countries and landmark events.
- "Which of the following was **not** …" items.
- "Why / what was the reason" items, such as Congress's success in 1952 and the Kyoto exemption.
- A 5-question passage on India's stand on climate change.

**Both papers**
- **Content:** spread across both books in roughly equal halves. Questions turn on NCERT names, parties, leaders, years, treaties, organisations and the reasoning NCERT gives: why Congress dominated, why India rejected the NPT, why developing countries were exempted from Kyoto.
- **Difficulty:** mostly moderate. The difficulty comes from close distractors: Kamaraj vs Nijalingappa, 1966 vs 1969, SAARC 1985 vs 2007, World Bank vs IMF, Kyoto 1997 vs Rio 1992.

**What the old series got wrong** (audit, `docs/audit/CUET-audit-report.md`):
- 70% of questions were easy.
- None used CUET formats.
- The correct option was the longest in 37% of items.
- The key never repeated a letter, which is an unnatural pattern.
- The "topic" was only the book name.
- There was a fake past-paper reference.

This series fixes all of these.

## 3. Unit weight per test (50 questions)

| Part | Unit | Qs |
|---|---|---|
| **Politics in India (25)** | I1 Era of one-party dominance | 3 |
| | I2 Nation-building and its problems | 3 |
| | I3 Politics of planned development | 2 |
| | I4 India's external relations | 3 |
| | I5 Challenge to and restoration of the Congress system | 3 |
| | I6 Crises of the constitutional order | 3 |
| | I7 Regional aspirations and conflicts | 3 |
| | I8 Democratic upsurge and coalition politics | 3 |
| | I9 Recent issues and challenges | 2 |
| **Contemporary World Politics (25)** | W1 Disintegration of the 'Second World' and the collapse of bipolarity | 4 |
| | W2 Alternative centres of economic and political power | 4 |
| | W3 South Asia in the post-Cold War era | 4 |
| | W4 International organisations in a unipolar world | 4 |
| | W5 Security in the contemporary world | 3 |
| | W6 Environment and natural resources in global politics | 3 |
| | W7 Globalisation and its critics | 3 |
| **Total** | | **50** |

The 5-question passage counts inside its unit's quota. When that quota is below 5, the extra questions are taken from other units of the same book, so each book stays at 25 (±1). `pol_check.py` flags a unit more than one question off its quota (`QUOTA`).

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.**

- **Easy:** one NCERT fact, such as a leader, a year, a full form or a founding member.
- **Medium:**
  - a close distractor set;
  - a cause and its effect;
  - "who said / led / proposed";
  - a match whose pairs are well known;
  - an item on why something happened.
- **Hard:**
  - a multi-statement judgement;
  - a chronology of four events close together in time;
  - a four-pair match in which every pair is plausible;
  - an inference from the passage.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Passage (one original passage on an NCERT theme, 5 linked questions; one may be a statement item) | 5 |
| Match List-I / List-II | 6 |
| Statements "(A)–(D), choose the correct / NOT correct" (one per test may be in the Statement I / Statement II form) | 6 |
| Chronological order | 4 |
| Direct | 29 |

The 29 direct items include at least 3 "which was **not** …" items, at least 2 reason items and at least 2 fill-in-the-blank items. Assertion–reason items are not used, because none appeared in the papers analysed. Picture sets are replaced by the passage set, because the platform shows text only.

## 6. Option quality (audit fix)

- **Distractors:** all four options are from the **same category**: four leaders, four parties, four years or four organisations. Every distractor is a real NCERT name.
- **Stems:** stems carry context. Match, statement and sequence items and the passage set are always long.
- **Key:**
  - 13 / 12 / 13 / 12 for odd tests and 12 / 13 / 12 / 13 for even tests.
  - No letter appears more than 3 times in a row.
  - The correct option is never clearly the longest (`LONGEST`).
- **Answer patterns:** statement and sequence answers vary, and a sequence answer is never A, B, C, D in that order (`SEQ-ABCD`). The six match items in a test all have different answer patterns.
- **Order:** `shuffle_test.py` gives a random exam order and keeps the passage set together.

## 7. Facts and sources

- Every fact follows the NCERT Class 12 texts *Politics in India since Independence* and *Contemporary World Politics*. The current edition comes first; the earlier edition is used where the syllabus keeps material the rationalised book dropped.
- Dates and figures are NCERT's.
- The coalition years run to the 2019 election, as the syllabus says ("Elections 2004–2019").
- Passages are **original summaries** of NCERT themes, written for the series. No textbook paragraph is reproduced.

## 8. Explanations

`Answer:` → `Why` → `Why not the others` → `Key point`.
- **Statement items:** the explanation names each false statement and says what is wrong with it.
- **Sequence items:** it gives the year of every event.
- **Match items:** it gives each pair with a one-line reason.

## 9. Out of syllabus — never test

- ***The Cold War Era*** (arenas, the Cuban missile crisis, arms-control history before 1985). These count only as background to the collapse of bipolarity.
- ***US Hegemony in World Politics*** (Operation Iraqi Freedom, the "constraints on hegemony" frame).
- ***Rise of Popular Movements*** (Chipko, the Dalit Panthers as a movement chapter, the Narmada Bachao Andolan, the anti-arrack movement). Dalit politics in the electoral and non-electoral arena (I9) is tested only as the syllabus words it.
- Topics deleted in rationalisation, such as the Gujarat riots of 2002. Class 11 *Indian Constitution at Work* and *Political Theory* are also out of syllabus.
