# Blueprint — CUET (UG) 2027 Chemistry (306)

**Syllabus:** `CUET SYLLABUS/md/Chemistry - 306.md` (NTA "for the year 2026", latest published). Ten units, **Class 12 NCERT only**.
**Series:** 15 tests, `CUET/Chemistry/CUET CHEMISTRY TEST 1–15.json`.

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (no internal choice) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (CUET 2025 Chemistry — analysed, not stored)

Source: shift-wise reports in [Careers360 — CUET 2025 Chemistry question paper analysis](https://university.careers360.com/articles/cuet-2025-chemistry-question-paper-analysis). These are student accounts, not official NTA data.

- **Difficulty:** most shifts were easy to moderate; a few were moderate. Questions are NCERT-based; many theory questions with "confusing options" rather than long calculations.
- **Weightage reported:** organic chemistry dominates (often 24–27 of 50), physical 8–13, inorganic 10–12. Coordination compounds and electrochemistry are prominent; one shift had 7 coordination questions.
- **Formats seen:** standard MCQs, Match List-I/List-II (named reactions, amino acids, cells), assertion–reason, multi-statement questions, **paragraph sets** (electrochemistry, kinetics, coordination, vitamins), numericals (molality, molarity, ppm, colligative properties, Faraday's law, conductance, kinetics), IUPAC naming and structure identification.
- **Frequently asked:** Hofmann bromamide, Sandmeyer, Swarts, Gabriel, azo coupling, HVZ, Clemmensen, Rosenmund, Lucas test, Tollens/Fehling, cumene process, SN1/SN2 order; freon, picric acid, cisplatin, double salts, ambidentate ligands, chelate effect; magnetic moment, lanthanoid contraction; Henry's law, isotonic solutions, Nernst equation, lead storage battery, fuel cells, zero-order graphs; anomers, glucopyranose, sucrose, lactose, maltose, uracil, thyroxine, vitamins.
- **Topics in some 2025 shift reports that are NOT in the 2026 syllabus** (surface chemistry, Tyndall effect, mole concept, thermodynamics, equilibrium, chemical bonding, salt analysis) are **not tested** here.

**What this means for OurMocks:** precise NCERT knowledge plus short numericals under time pressure. Medium and hard difficulty comes from close options, two-step numericals, order/trend judgement, reaction sequences and multi-statement questions — never from content beyond NCERT.

## 3. Unit weight per test (50 questions)

| Group | Unit | Qs |
|---|---|---|
| Physical (15) | I Solutions | 5 |
| | II Electrochemistry | 5 |
| | III Chemical Kinetics | 5 |
| Inorganic (11) | IV d- and f-Block Elements | 5 |
| | V Coordination Compounds | 6 |
| Organic (24) | VI Haloalkanes and Haloarenes | 5 |
| | VII Alcohols, Phenols and Ethers | 5 |
| | VIII Aldehydes, Ketones and Carboxylic Acids | 6 |
| | IX Amines | 4 |
| | X Biomolecules | 4 |
| **Total** | | **50** |

The five-question passage set counts towards its unit's quota (a set may span two units, e.g. VIII + IX); the other units are unchanged and the passage unit gets no extra questions beyond its quota unless another unit in the same group gives one up (±1, totals stay 15/11/24).

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.** Rough split: physical 2/10/3, inorganic 2/7/2, organic 4/15/5 (adjust ±1).

- **Easy:** one NCERT fact, definition, name or formula, cleanly asked.
- **Medium:** one-step numerical, a reaction product, an order of a property, a close distractor set, or two linked facts.
- **Hard:** two-step numerical (e.g. Nernst + ΔG, freezing point with i, half-life chain), multi-step conversion, multi-statement judgement, structure deduction from tests, or CFT/magnetism reasoning.
- **Depth progression:** Tests 1–5 accessible, 6–10 deeper, 11–15 hardest.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Passage / case set (one passage, 5 linked questions) | 5 |
| Match List-I / List-II | 5 |
| Statements "(A)–(D), choose the correct" | 5 |
| Assertion–Reason | 3 |
| Order / sequence (e.g. increasing boiling point, acidity, reactivity; reaction steps) | 3 |
| Data or table reading (kinetics data, E° tables, conductivity tables) | 2 |
| Numericals (outside the passage) | at least 6 |
| Direct concept / reaction / naming | the rest (about 21) |

Non-direct formats = 23 of 50, above the 30% floor.

## 6. Key and order

- Key per test 13 / 12 / 13 / 12 (rotate); no letter more than 3 times in a row; the correct option is never clearly the longest.
- `shuffle_test.py` gives random exam order and keeps the passage set together.

## 7. Writing chemistry in text

- No images. Structures as condensed formulas (CH₃CH₂CH(Br)CH₃, C₆H₅NH₂, C₆H₅–N₂⁺Cl⁻), with IUPAC or common name where it helps. Use Unicode subscripts/superscripts (H₂O, Fe³⁺, 10⁻³, t₁/₂) and arrows (→, ⇌).
- Constants given in the question when needed: R = 8.314 J K⁻¹ mol⁻¹, F = 96500 C mol⁻¹, 2.303RT/F = 0.059 V at 298 K, log 2 = 0.301, log 3 = 0.477.
- Numbers chosen so that the answer needs no calculator (CUET has none).

## 8. Explanations

- Numericals: `Answer:` → `Given` → `Step 1…n` (units carried) → `Common mistake` (what each wrong option comes from).
- Concept / reaction questions: `Answer:` → `Why` → `Why not the others` → `Key point`.
- Every explanation relies on NCERT Class 12 Chemistry (the edition matching the syllabus; for syllabus items dropped from the rationalised NCERT — e.g. metal carbonyls, hormones, corrosion, methods of preparation of glucose — the earlier NCERT text is the source).

## 9. Out of syllabus — never test

Solid state, surface chemistry (adsorption, colloids, Tyndall effect), general principles of metallurgy, p-block elements, polymers, chemistry in everyday life, Class 11 topics (mole concept, thermodynamics, equilibrium, bonding) except as unavoidable background, salt analysis and practical chemistry, integrated rate laws beyond zero and first order.

## 10. Images

None planned. If a figure is ever unavoidable, add `image_reference` and an entry in `CUET/Chemistry/CUET_Chemistry_images.md` (format: `docs/instructions/IAT_Instructions.md` → Images).
