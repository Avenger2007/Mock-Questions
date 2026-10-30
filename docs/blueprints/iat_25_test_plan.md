# IAT: 25-test slot and angle plan

30 October 2026. This is an **editorial reservation for 1,500 original questions**. The [slot register](iat_25_test_slots.tsv) lists each fixed ID, subject, syllabus chapter, class, subtopic focus, angle seed, dominant task target, difficulty target and authoring state. Test 1's 60 rows point to its already authored paper. Tests 2 and 3 have 120 separately specified angle briefs. Tests 4–25 reserve 1,320 distinct combinations of subtopic focus and reasoning demand; the eventual question author must turn each seed into a specific, independently solved task and reject semantic repeats before publication. A unique phrase in a spreadsheet is not proof of a genuinely different question.

## What “equal coverage” means here

Each test has **15 Biology, 15 Chemistry, 15 Mathematics and 15 Physics** questions, with no best-three scoring. Across 25 tests, every retained syllabus family is represented. We do not force each chapter to appear the same number of times: genetics is much broader and more frequent in the acquired PYQs than a narrow chapter such as electromagnetic waves. The minimum frequency for a retained family in the reservation is 5 slots; no current family is dropped simply because it was rare in the recent papers. A chapter's slot count is a preparation choice, not an official paper quota.

| Subject | Total | Main repeated families | Smallest retained family allocation | Class 11 / 12 (coarse chapter tags) |
|---|---:|---|---:|---:|
| Biology | 375 | Genetics 70; human physiology 55; cells 50 | 25 | 190 / 185 |
| Chemistry | 375 | Bonding 30; organic principles, coordination, carbonyls, equilibrium and solutions 25 each | 10 (redox) | 175 / 200 |
| Mathematics | 375 | Coordinate geometry 35; differentiation/integration 30 each | 15 | 185 / 190 |
| Physics | 375 | Electrostatics/ray optics 25 each; induction/current electricity 20 each | 5 (electromagnetic waves) | 175 / 200 |

The class tags come from the stored chapter taxonomy. A question combining Class 11 and Class 12 ideas needs an item-specific classification when it is authored. “Equal” here refers to subject marks and access to the full listed syllabus across the series, with a deliberate Class 11/12 balance. It does not flatten the PYQ weight of the chapters.

## PYQ calibration and limits

The [auditable PYQ analysis](iat_pyq_analysis.md) covers 539 English entries across nine recovered papers; the recent comparison uses 2023–2026 and current-scope denominators of 58/55/59/59 by subject. It finds strong recent shares for genetics and physiology, bonding and organic structure, calculus and coordinate geometry, and electrostatics/energy/optics. Four recent papers cannot establish exact probabilities for 2027, and the acquired 2025 English paper lacks its final Physics question. No target-year 2027 brochure has been verified; the established 2026 pattern is provisional for preparation.

| Dominant task | Biology target per 15 | Chemistry target per 15 | Mathematics target per 15 | Physics target per 15 |
|---|---:|---:|---:|---:|
| Concept or short recall | 7 | 6 | 3 | 2 |
| Numerical | 1 | 4 | 12 | 7 |
| Figure/structure | 4 | 4 | 0 | 5 |
| Graph/table/experiment | 3 | 1 | 0 | 1 |

The task mix is an editorial approximation of the recent PYQ tags: Biology included mechanisms, diagrams, tables and experiments; Chemistry often used structural representations; Mathematics was mostly numerical and conceptual; Physics mixed numerical and visual modelling. A chemical structure can use mhchem text. A diagram target calls for a purposeful representation, never an arbitrary decorative file. The register's task targets may be changed when a specific question needs a better form; record the reason rather than forcing a bad diagram to meet a quota.

## Difficulty and progression

Every paper reserves **9 easy / 42 medium / 9 hard** questions, as instructed (15% / 70% / 15%). The extra easy slot rotates Biology, Chemistry, Mathematics, Physics; the extra hard slot rotates Chemistry, Mathematics, Physics, Biology. Tests 1–8 emphasise accessible application, 9–17 integrate more constraints, and 18–25 use deeper multi-step reasoning while staying within the syllabus. The counts are editorial labels, not measured student difficulty; a label may require a substantive rewrite after timed review.

## Reservation and review contract

1. Use the fixed `IAT27-TNN-QNN` row as an authoring brief. Before writing a question, check the exact official syllabus subtopic and compare its **method and situation** with every earlier test, not just the wording or numerical values. Reject number-swapped or cosmetically changed repeats.
2. For each new paper, write the full stem, four plausible distinct alternatives, an independently worked solution and a misconception behind each distractor. The answer is solved before its final option is placed. Do not shuffle after figure filenames and IDs are assigned.
3. Keep data needed to solve a question inside the JSON stem. If a graph or figure carries essential geometry, add a precise image register entry, render it and inspect its labels, scale, signs and consistency with the solution.
4. Validate 60 IDs/keys/tier distribution and source metadata, re-derive every calculation, inspect all PDF pages and compare chapter/style counts with this plan and the PYQ analysis. A matching count alone does not certify scientific accuracy or originality.
5. Record why any slot is replaced. Rebalance the remaining series so every retained syllabus family and the broad PYQ-style mix remain represented. Verify new official rules when published. Keep draft tests pending academic/timed review until explicitly approved for student release.

## Reproduction

`python tools/iat/plan_25_tests.py` recreates the slot TSV from the versioned syllabus taxonomy, the chapter-profile reservations, Test 1 and the editorial subtopic/angle catalog in that script. It writes **planning metadata only**, never question stems, options or answers. Its assertions require exactly 25 × 60 slots, 15 per subject per test, the 9/42/9 mix, all retained families and stable IDs. The exact seed-duplicate check is useful screening; a human semantic check is still required during authorship.
