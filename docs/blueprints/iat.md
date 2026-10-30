# OurMocks IAT blueprint: pilot and 25-test coverage reservation

Date: 29 October 2026. Basis: [PYQ analysis](iat_pyq_analysis.md), [chapter appendix](iat_pyq_chapter_counts.md), stored [official 2026 syllabus](../../IISER/IISER_Aptitude_Test_Syllabus_2026.md). User instruction authorises the analysis and Test 1 review draft in this session. Status: pilot awaiting human academic review, not student release.

## Pattern and design

Use 60 single-correct questions, four options each, 15 each in B/C/M/P order, 180 minutes, +4/-1/0, maximum 240. All 60 are available; unanswered questions score zero. There is no NEST-style best-three rule. Official 2026 conditions include an on-screen non-programmable scientific calculator. No verified 2027 brochure is claimed; refresh syllabus and pattern before publication.

Author original questions directly in their final order. Never shuffle options or questions, relabel IDs or move diagrams after authoring. Balance answer positions while constructing the paper, then prioritise mathematical and scientific correctness. Preserve image-linked IDs in every review revision. Do not use the legacy generation scripts.

The user-revised series editorial mix is 9 easy / 42 medium / 9 hard, with the extra easy rotating B, C, M, P and the extra hard rotating C, M, P, B. This is a design choice, not a claimed official difficulty distribution. Test 1 has B = 3/10/2, C = 2/10/3 and M/P = 2/11/2. The revision record supersedes the initial pilot profile: Q44 covers coordinate geometry rather than a second integration slot. Progression: Tests 1–8 accessible foundation in application, 9–17 deeper integration, 18–25 strongest PYQ-style reasoning; no progression by out-of-syllabus material or changed marking.

## Test 1: detailed reservation

The [60-slot plan](iat_test_01_plan.tsv) records every question's chapter, distinct angle, tier, style and planned time. Its original total was 168 minutes. Retained slot times are planning placeholders after the revisions, not measured completion times; a timed student attempt is still required. The authored [JSON](../../IISER/IAT%20TEST%201.json) is the content source for the review PDF. No script writes or permutes question content.

| Section | Questions | Easy / medium / hard | Coverage and style |
|---|---|---|---|
| Biology | 1–15 | 3 / 10 / 2 | All ten broad units; genetics 3, cell 2, human physiology 2, structural organisation 2, others 1 each; mechanisms, crosses, controls, energy budgets and a gel. |
| Chemistry | 16–30 | 2 / 10 / 3 | Physical 6, organic/biomolecules 5, foundation/inorganic 4 by dominant task; carbonyl chemistry 2; all other chosen chapters 1. |
| Mathematics | 31–45 | 2 / 11 / 2 | One integration and one coordinate-geometry item; algebra, counting, functions, 3D, calculus, statistics, probability and vectors. Sequences and binomial theorem rotate into later profiles. |
| Physics | 46–60 | 2 / 11 / 2 | Seven Class 11 and eight Class 12 primary topics; graphs, fluid flow, rotation, thermal reasoning, oscillations/waves, circuits, induction, optics and nuclei/semiconductors. |

Eight relevant figures (not all essential): Q9 thylakoid gradient, Q11 restriction gel, Q21 cumulative gas graph, Q25 alkene connectivity, Q46 velocity graph, Q53 electric-field graph, Q54 resistor bridge, Q57 layered refraction. Each has exact labels, alt text and a matching [image register](../../IISER/IAT_images.md). Chemical formulae use mhchem rather than decorative raster images. Diagrams are drawn deterministically; no AI-generated image is used for exact scientific information.

The expanded [25-test slot plan](iat_25_test_plan.md) and [1,500-slot register](iat_25_test_slots.tsv) now specify subject, chapter, subtopic focus, reasoning seed, style and editorial tier for every test. Tests 2 and 3 have individually written 120 angle briefs; the later seeds are reservations that must be sharpened into specific original tasks during authorship. The chapter profiles below remain the coverage backbone.

## Coverage profiles for the remaining series

Codes are defined in [taxonomy](iat_taxonomy.json). Each profile below contains exactly 15 question slots. A repeated code reserves distinct subtopics/angles, never a repeated or number-swapped question. These are chapter-level reservations, **not 1,500 authored questions**. Test 1 is fully authored; Tests 2 and 3 have specific angle briefs. Before each later batch, make each remaining seed concrete and check against already authored items. Obtain pilot-standard feedback before authoring Tests 2–25.

### Biology

Every profile contains the ten units DIV STR CELL PLANT HUMAN REPRO GEN WELFARE BIOTECH ECO once. Add:

| Profile | Five additional slots |
|---|---|
| A | GEN GEN HUMAN CELL STR |
| B | GEN GEN HUMAN CELL PLANT |
| C | GEN GEN HUMAN CELL BIOTECH |
| D | GEN GEN HUMAN CELL ECO |
| E | GEN HUMAN HUMAN CELL REPRO |

These reservations protect small units while revisiting the strongest recent anchors. Human physiology slots rotate kidney, circulation, respiration, endocrine, neural and movement; genetics rotates inheritance, molecular processes and evolution. No single question represents an entire broad unit exhaustively.

### Chemistry

| Profile | Fifteen primary-topic slots |
|---|---|
| A | BOND COORD THERM CARB ELEC AMINE REDOX KIN CARB GOC SOL STO PERIOD BIO EQ |
| B | BOND COORD ATOM GOC HC HALO ALCO CARB AMINE SOL ELEC KIN THERM EQ DF |
| C | BOND COORD DF PERIOD ATOM STO GOC HC HALO ALCO BIO EQ SOL ELEC THERM |
| D | BOND COORD BOND ATOM GOC CARB AMINE BIO KIN EQ REDOX THERM SOL HC HALO |
| E | BOND COORD DF ATOM PERIOD STO GOC CARB ALCO AMINE BIO SOL ELEC KIN EQ |

Bonding, coordination and organic principles persist; structure of atom, d/f-block, hydrocarbons, halo compounds and alcohols rotate explicitly. The retained syllabus's 19 topic families all occur across the profiles. Excluded historical detail does not re-enter through an “inorganic” quota.

### Mathematics

| Profile | Fifteen primary-topic slots |
|---|---|
| A | MATRIX COUNT SET COMPLEX INT 3D DIFF STAT LIMIT PROB TRIG DE QUAD COORD VECTOR |
| B | COORD COORD DIFF INT SET MATRIX PROB BINOM SEQ LIMIT 3D COUNT COMPLEX DE TRIG |
| C | COORD DIFF DIFF INT SET VECTOR MATRIX PROB COUNT BINOM SEQ QUAD STAT DE LIMIT |
| D | COORD COORD INT INT DIFF SET MATRIX PROB TRIG 3D VECTOR COMPLEX QUAD BINOM SEQ |
| E | COORD DIFF INT SET MATRIX PROB COUNT BINOM SEQ LIMIT DE 3D VECTOR STAT TRIG |

All 17 current taxonomy families occur. Coordinate geometry slots must span lines, circles and conics over the series, not repeatedly the same circle identity. Calculus slots rotate transformations, monotonicity, extrema, integral methods and area. Linear programming remains on hold because only the umbrella heading names it in the stored syllabus.

### Physics

| Profile | Fifteen primary-topic slots |
|---|---|
| A | KIN UNITS FLUID ROT THERMO SHM WAVE ELECTRO CURRENT NUC EMI RAY AC SEMI WAVEOPT |
| B | FORCE WORK GRAV SOLID THERMAL KTG SHM CAP MAG ELECTRO CURRENT RAY DUAL ATOM EMI |
| C | KIN WORK ROT FLUID THERMO WAVE GRAV ELECTRO CAP CURRENT MAG AC RAY EMW NUC |
| D | UNITS FORCE SOLID THERMAL KTG SHM WAVE ELECTRO CURRENT EMI AC RAY WAVEOPT DUAL SEMI |
| E | KIN FORCE WORK ROT GRAV FLUID THERMO ELECTRO CAP MAG EMI RAY WAVEOPT ATOM NUC |

All 26 current primary-topic families occur. Alternate approximately 7/8 or 8/7 Class 11/12 slots; exact per-paper allocation follows the profile. Concepts like energy can also be secondary reasoning in a question classified elsewhere. Avoid counting that as complete primary-chapter coverage.

## Reservation by test

| Test | B profile | C profile | M profile | P profile | Subject with 3 easy |
|---:|---|---|---|---|---|
| 1 | A | A | A | A | Biology |
| 2 | B | B | B | B | Chemistry |
| 3 | C | C | C | C | Mathematics |
| 4 | D | D | D | D | Physics |
| 5 | E | E | E | E | Biology |
| 6 | A | B | C | D | Chemistry |
| 7 | B | C | D | E | Mathematics |
| 8 | C | D | E | A | Physics |
| 9 | D | E | A | B | Biology |
| 10 | E | A | B | C | Chemistry |
| 11 | A | C | E | B | Mathematics |
| 12 | B | D | A | C | Physics |
| 13 | C | E | B | D | Biology |
| 14 | D | A | C | E | Chemistry |
| 15 | E | B | D | A | Mathematics |
| 16 | A | D | B | E | Physics |
| 17 | B | E | C | A | Biology |
| 18 | C | A | D | B | Chemistry |
| 19 | D | B | E | C | Mathematics |
| 20 | E | C | A | D | Physics |
| 21 | A | E | D | C | Biology |
| 22 | B | A | E | D | Chemistry |
| 23 | C | B | A | E | Mathematics |
| 24 | D | C | B | A | Physics |
| 25 | E | D | C | B | Biology |

## Review and release contract

1. Run `python validate_iat.py` for schema, fixed order, section counts, tiers, options, source fields, image existence and registry links. The existing CUET validator is not an IAT validator.
2. Parse all maths with KaTeX/mhchem in strict error mode, render the PDF, inspect all pages and check all six diagrams. Keep answer key and solutions after the question paper.
3. Re-derive numerical results from the stem, check conceptual alternatives, and compare the selected content with the stored letter. Mechanical arithmetic checks supplement this review; they do not certify pedagogy or eliminate every ambiguity.
4. Keep `pending_revision` until a human reviewer approves academic accuracy, syllabus fit, distractors, timing and tier labels. Record any correction against its stable ID.
5. Before student publication, verify the target-year brochure and review all provenance/licensing requirements for redistributing third-party source PDFs. Original pilot content and locally stored reference papers have different provenance.
6. Expand subsequent exact angle plans before further authorship; do not claim the series is complete because chapter reservations exist. Commit only the reviewed scope; do not push unreviewed mass-generated papers.
