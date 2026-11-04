# Blueprint — CUET (UG) 2027 Geography (313)

**Syllabus:** `CUET SYLLABUS/md/Geography - 313.md` (NTA "for the year 2026", latest published). Two Class 12 NCERT books only: **A. Fundamentals of Human Geography** and **B. India: People and Economy** (rationalised editions). Physical geography (Class 11), map-drawing practicals and chapters removed in rationalisation are never tested.
**Series:** 15 tests, `CUET/Geography/CUET GEOGRAPHY TEST 1–15.json` (existing file names kept).

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (no internal choice) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (analysed, not stored)

No Geography PYQ is held in the repo, and none is copied. The pattern below follows the published CUET (UG) 2024–2026 domain-paper format (the same NTA template seen in the Economics, History and Accountancy PYQs analysed for those subjects) and public shift analyses of the Geography paper.

- **Formats:** direct NCERT MCQs, **Match List-I/List-II** (ports and states, minerals and mines, farming types and regions, railways and terminals), **multi-statement** questions, **arrange-in-order** (north to south, chronology, stages of demographic transition), **assertion–reason**, and a **passage or data set** (5 linked questions).
- **Content:** both books in roughly equal measure; India's resources, transport and ports and the world's primary activities and transport routes are the heaviest areas.
- **Difficulty:** mostly easy to moderate; difficulty comes from close distractors (e.g. ladang vs milpa, entrepot vs port of call, Bailadila vs Kudremukh) and location knowledge stated in words.

**What the old series got wrong (audit, `docs/audit/CUET-audit-report.md`):** 70% easy; absurd distractors that gave the answer away; 68% of stems under 150 characters; the correct option was the longest in 35% of items; a fake "past paper" reference. This series fixes all five.

## 3. Unit weight per test (50 questions)

| Book | Unit (NCERT chapter) | Qs |
|---|---|---|
| **A. Fundamentals of Human Geography (24)** | A1 Human geography: nature and scope | 2 |
| | A2 The world population: distribution, density, growth, change | 4 |
| | A3 Human development: concept, approaches, indicators, comparisons | 3 |
| | A4 Primary activities: gathering, pastoralism, agriculture, mining | 4 |
| | A5 Secondary activities: manufacturing, its types and location | 3 |
| | A6 Tertiary and quaternary activities | 3 |
| | A7 Transport and communication (world) | 3 |
| | A8 International trade, ports, WTO | 2 |
| **B. India: People and Economy (26)** | B1 Population: distribution, density, growth, composition | 4 |
| | B2 Human settlements: rural types, urban types, functional classes | 2 |
| | B3 Land resources and agriculture | 4 |
| | B4 Water resources | 3 |
| | B5 Mineral and energy resources | 4 |
| | B6 Planning and sustainable development (Bharmaur, Indira Gandhi Canal) | 2 |
| | B7 Transport and communication (India) | 3 |
| | B8 International trade, seaports and airports (India) | 2 |
| | B9 Selected issues: pollution, urban waste, migration, slums, land degradation | 2 |
| **Total** | | **50** |

The five-question case set counts inside its unit's quota; when that quota is below 5, the extra questions come from another unit of the same book, so the book totals stay 24 / 26 (±1).

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.**

- **Easy:** one NCERT fact or definition.
- **Medium:** a close distractor set, a location stated in words, a cause–effect link, a short calculation (density, growth rate, doubling time), matching or a data reading.
- **Hard:** a multi-statement judgement, a four-pair match whose pairs are all plausible, a geographical ordering (north to south, west to east), or a two-step calculation.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Case / passage set (one passage or data table, 5 linked questions) | 5 |
| Match List-I / List-II | 5 |
| Statements "(A)–(D), choose the correct" | 5 |
| Assertion–Reason | 3 |
| Order / sequence (location, chronology, stages) | 3 |
| Numerical or data reading (outside the case set) | 2 |
| Direct concept | the rest (27) |

## 6. Option quality (audit fix)

- All four options are from the **same category** (four ports, four minerals, four farming types), and every distractor is a real NCERT term that a half-prepared student could pick.
- Stems carry context: about two-thirds are at least 150 characters (the case set, matches, statements and assertion–reason items are always long).
- Key per test 13 / 12 / 13 / 12 (rotate); no letter more than 3 times in a row; the correct option is never clearly the longest.
- Statement and assertion–reason answers vary (not always "(A), (B) and (C) only" or "A").
- `shuffle_test.py` gives random exam order and keeps the case set together.

## 7. Facts and figures

- Every fact follows the rationalised NCERT text. Census figures are Census 2011, as in *India: People and Economy*; world figures follow *Fundamentals of Human Geography*. Where a figure is approximate or changes over time, the question tests the rank, trend or category, not the exact number.
- Locations are asked in words (state, river, coast, direction) because no map is shown.

## 8. Explanations

- Concept questions: `Answer:` → `Why` → `Why not the others` → `Key point`.
- Numericals and data questions: `Answer:` → `Given` → `Step 1…n` → `Common mistake`.

## 9. Out of syllabus — never test

Class 11 physical geography (landforms, climate, oceans, soils as physical processes), map work and practical geography (data processing, GIS, cartography), and the chapters removed from the rationalised Class 12 books: world population composition (sex ratio pyramids as a chapter), world human settlements, migration and human development chapters of *India: People and Economy*, and India's manufacturing industries chapter. Items on these appear only where the current syllabus names them (e.g. rural–urban migration under Selected Issues).
