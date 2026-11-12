# Blueprint — CUET (UG) 2027 Agriculture (302)

**Syllabus:** `CUET SYLLABUS/Agriculture - 302.pdf` (NTA "for the year 2026", the latest published). It has four units:
- **Unit 1:** Agrometeorology, Genetics and Plant Breeding, Biochemistry and Microbiology (this unit also includes Seed Science).
- **Unit 2:** Livestock Production.
- **Unit 3:** Crop Production.
- **Unit 4:** Horticulture.

NCERT has no Class 12 Agriculture textbook, so these are the sources:
- The NIOS Senior Secondary Agriculture course and ICAR e-course material.
- NCERT Biology Classes 11–12 for the cell, genetics, biomolecules, microbes and plant breeding.
- Standard agronomy, animal husbandry and horticulture references, including the TNAU Agritech Portal and ICAR institute pages, for crop-specific facts.

Every answer rests on a fact that these sources state the same way. When sources differ (for example, exact seed rates or breed yields), the item asks for the value or range they share, or the question is not set.

**Series:** 15 tests, `CUET/Agriculture/CUET AGRICULTURE TEST 1–15.json`. This is a new subject; the repo had no earlier Agriculture tests.

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (2025 onward; in 2024 candidates answered 40 of 50) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (analysed, not stored)

Papers were read for pattern only. They are kept outside the repo and never copied:
- 2024, 19 July shift 1 (image scan);
- 2026 (image scan).

Both came from AglaSem. The 2025 paper is a scan of the same kind and adds nothing new.

**2024 paper**
- 40 standalone items, then two 5-question passage sets: "Oilseeds scenario of India" and "Mandarin orange".
- The passage questions ask for a figure, name, family or propagation method stated in the passage.

**2026 paper**
- Direct fact items, for example:
  - DNA as a polymer of deoxyribonucleotides;
  - the parasitic weed of sorghum (*Striga*);
  - the nutrient that helps nodulation (boron);
  - the order to which black soils belong (Vertisols).
- Match-lists, such as aneuploidy (2n−1, 2n+1, 2n−2, 2n+2) and indices of fruit maturity (visual, physical, chemical, physiological).
- Sequences, for example:
  - transcription, replication and translation;
  - "arrange the crops in the order oilseed, sugar, fodder, fibre".
- Multi-select items such as "microbes are useful as…" and "fruits and vegetables are important because…".
- "Which is **not** an objective of plant breeding" items.
- A 5-question passage on goats: breeds, CIRG Mathura, chevon, and "the poor man's cow".

**Both papers**
- **Spread:** questions come from all four units. Crop production and livestock are the heaviest, then genetics and breeding, then horticulture.
- **Content:** items turn on names (breeds, pathogens, weeds, varieties, scientific names), categories (crop groups, fertilizer types, soil orders), processes in order, and short reasons.
- **Difficulty:** mostly moderate. The difficulty comes from close distractors: Rinderpest vs FMD, Vertisols vs Inceptisols, *Phalaris minor* vs *Avena fatua*, monosomy vs nullisomy.

## 3. Unit weight per test (50 questions)

| Unit | Sub-unit (key) | Qs |
|---|---|---|
| **Unit 1 (16)** | A1 Agrometeorology | 3 |
| | A2 Genetics and plant breeding (cell, genetic material, Mendel, inheritance, breeding methods, biotechnology) | 5 |
| | A3 Biochemistry | 3 |
| | A4 Microbiology | 3 |
| | A5 Seed science | 2 |
| **Unit 2 (10)** | L1 Scope, importance, White Revolution, breeds | 3 |
| | L2 Housing, feeding, ration, management, diseases | 4 |
| | L3 Artificial insemination; milk processing and products | 2 |
| | L4 Fisheries | 1 |
| **Unit 3 (16)** | C1 Foodgrain targets, crop classification, sustainable and modern agriculture | 3 |
| | C2 Soil, fertility, nutrients, fertilizers, manures, problem soils | 4 |
| | C3 Irrigation and drainage | 3 |
| | C4 Weed control | 2 |
| | C5 Field crops: practices, pests and diseases, IPM, post-harvest, millets | 4 |
| **Unit 4 (8)** | H1 Importance, orchard and gardens, planting, training and pruning, plant types, propagation | 3 |
| | H2 Cultivation of the listed fruits, vegetables and flowers | 3 |
| | H3 Preservation; jams, jellies, ketchup and chips | 2 |
| **Total** | | **50** |

**How the passage is counted:**
- The 5-question passage counts in its own sub-unit, which may exceed its quota.
- The extra questions are taken from other sub-units, so no other sub-unit is more than 1 off its quota.
- The passage's unit may be up to 3 over its unit total. Every other unit is at most 1 under its total.
- `agri_check.py` enforces this with the flags `QUOTA` and `PART-QUOTA`.

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.**

- **Easy:** a single fact, such as a breed's home tract, a causal organism, a full form or a scientific name.
- **Medium:**
  - close distractors;
  - a cause and its effect;
  - a deficiency symptom;
  - a crop's critical stage;
  - a well-known match;
  - an item asking why.
- **Hard:**
  - a multi-statement judgement;
  - a four-step process in order;
  - a four-pair match in which every pair is plausible;
  - a short calculation (seed rate, fertilizer quantity, irrigation depth);
  - an inference from the passage.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Passage (one original passage, 5 linked questions) | 5 |
| Match List-I / List-II | 6 |
| Statements "(A)–(D), choose the correct / NOT correct" | 6 |
| Order / sequence | 4 |
| Direct | 29 |

The 29 direct items include:
- at least 3 "which is **not** …" items;
- at least 2 reason items;
- at least 2 fill-in-the-blank items.

Assertion–reason items are not used, because none appeared in the papers analysed.

## 6. Option quality

- **Distractors:** all four options come from the same category: four breeds, four pathogens, four fertilizers or four soil orders. Every distractor is a real term from the syllabus area.
- **Key:**
  - 13 / 12 / 13 / 12 for odd tests and 12 / 13 / 12 / 13 for even tests.
  - No letter appears more than 3 times in a row.
  - The correct option is never clearly the longest (`LONGEST`).
- **Answer patterns:** sequence answers are never A, B, C, D in that order (`SEQ-ABCD`). The six match items in a test all have different answer patterns.
- **Order:** `shuffle_test.py` gives a random exam order and keeps the passage set together.

## 7. Explanations

Every explanation has three parts:
1. **Why:** the fact or the working, set out step by step for calculations.
2. **Why not the others:** a reason for each wrong option.
3. **Key point:** a one-line takeaway.

## 8. Tools

`tools/cuet_agri/`, with the same workflow as Political Science (see its `README.md`). The coverage plan and answer-fact ledgers are in `docs/blueprints/agriculture_coverage.md`.
