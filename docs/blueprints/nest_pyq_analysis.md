# NEST past-paper analysis (for the NISER / CEBS test series)

Written 15 November 2026. Findings only: the papers are **not** stored in this repository. They are published with answers at `https://www.nestexam.in` (Syllabus / Brochure / Archive).

## What was analysed

| Paper | Questions read | Note |
|---|---:|---|
| NEST 2026 | 80 | final answer key published; the site notes one question each in Chemistry and Physics was dropped |
| NEST 2025 | 80 | |
| NEST 2024 Session 1 | 80 | |
| NEST 2024 Session 2 | 80 | |

- Total: 320 questions, 80 per subject. All four papers have the current pattern: 4 sections × 20 single-correct questions.
- **Method and limits:** the English question stems were extracted as text and each question was tagged with one chapter code by reading its stem. Options and figures were not read, and mathematical symbols extract poorly, so a few tags are judgement calls. The tags are in `nest_pyq_tags.txt`.
- **Not analysed:** NEST 2023 (both sessions are mostly images, so the text does not extract) and papers before 2023 (older formats). 80 questions per subject is a small sample; chapter shares below are a guide, not a forecast.

## Pattern seen in all four papers

- Every question has four options and one correct answer. There are no multiple-correct, integer-type or matching-only questions.
- The published papers list the correct option first (2026 key: "correct answers are option A in all the questions"), and the order is shuffled in the examination. So the published papers give no information about key-letter balance; our 5/5/5/5 rule stays.
- Questions inside a section are not in syllabus order; chapters are mixed.

## Style by subject

| Measure (per 20 questions) | Biology | Chemistry | Mathematics | Physics |
|---|---:|---:|---:|---:|
| Questions that refer to a figure, graph or diagram | 1 to 6 (average 4) | 2 to 4 | 0 to 1 | 3 to 5 |
| Questions built on an experiment, a table or a set of statements | 7 to 11 | 0 to 3 | 0 | 0 to 1 |
| Typical stem length (characters) | 400 to 500 | 200 to 330 | 150 to 200 | 250 to 290 |

- **Biology** is the least like a textbook test. Most questions describe an experiment, a data table, a pedigree, a graph or an unfamiliar organism and ask for a deduction. Plain recall is rare. Genetics, molecular biology, biochemistry, cell biology, evolution and ecology dominate. Human physiology chapters are thin: no question in these four papers on digestion, excretion, locomotion, endocrine system or human reproduction.
- **Chemistry** is about one-third organic (multi-step reaction sequences with products P, Q, R; aromaticity; order of reactivity), one-third inorganic (coordination compounds, d and f block, bonding and molecular orbitals) and one-third physical (equilibrium, thermodynamics, kinetics, electrochemistry), with physical questions often set on two compared systems or a graph.
- **Mathematics** is short-stemmed and proof-flavoured: "the number of solutions", "which statement is true", functions defined by a property, equivalence relations, counting. Calculus (limits, continuity, integrals, differential equations), functions and relations, conics and circle geometry, complex numbers and polynomial roots, probability, and matrices carry most of the section. No question on linear programming, statistics, mathematical induction or applications of derivatives as a routine optimisation.
- **Physics** mixes short conceptual questions with estimates from real contexts (Earth's rotation, melting ice, an asteroid impact, a solar probe, an earthquake scale). Dimensional analysis and significant figures appear every year. Modern physics (atoms and nuclei) is heavier than its syllabus length suggests. No question on AC circuits; only one each on current electricity, laws of motion and electromagnetic induction.

## Chapter counts (4 papers, 80 questions per subject)

**Biology:** inheritance 8; biomolecules 7; molecular basis of inheritance 7; evolution 7; living world and classification 6; cell 6; biotechnology principles 5; organisms and populations 5; photosynthesis 4; health and diseases 4; anatomy of flowering plants 3; ecosystem 3; cell cycle 2; respiration 2; breathing 2; neural control 2; biodiversity 2; plant growth 1; circulation 1; no single listed chapter (animal behaviour, stomatal movement) 3; all other chapters 0.

**Chemistry:** coordination compounds 8; equilibrium 7; hydrocarbons 7; alcohols, phenols and ethers 7; bonding 6; d and f block 6; aldehydes, ketones and acids 6; thermodynamics 5; kinetics 5; atom 3; redox 3; electrochemistry 3; biomolecules 3; mole concept 2; periodicity 2; organic principles 2; solutions 2; amines 2; haloalkanes 1.

**Mathematics:** conics and circles 9; relations and functions 8; complex numbers and polynomial roots 8; continuity and differentiability 7; integrals 7; probability 6; matrices and determinants 5; trigonometry 4; differential equations 4; limits 3; permutations and combinations 2; sequences 2; straight lines 2; inverse trigonometry 2; area 2; 3D 2; sets 1; binomial 1; vectors 1; no single listed chapter (number theory, plane geometry) 4; statistics, induction, inequalities, applications of derivatives, linear programming 0.

**Physics:** ray optics 7; thermodynamics 6; atoms 6; units and dimensions 5; oscillations 5; moving charges and magnetism 5; nuclei 5; work and energy 4; gravitation 4; thermal properties 4; electromagnetic waves 4; fluids 3; kinetic theory 3; waves 3; electric field 3; potential and capacitance 3; rotation 2; wave optics 2; motion in a plane 1; laws of motion 1; current electricity 1; induction 1; dual nature 1; semiconductors 1; straight-line motion, solids, magnetism and matter, alternating current 0.

## Questions that go outside the listed syllabus

The papers sometimes use ideas that the published syllabus does not list: radioactive decay treated as first-order kinetics (Chemistry 2024, 2025), stomatal movement and phloem transport (Biology 2025, 2026), animal behaviour experiments (Biology 2025, 2026), reading a character table as a phylogeny, number theory and plane geometry (Mathematics). **Our rule does not change:** we set questions only on listed topics. Two allowances follow from the papers: a first-order decay may be used as a kinetics example in Chemistry, and a Biology question may give an unfamiliar system in the stem as long as the reasoning needs only listed topics.

## What changed in the plan

- Chapter slot counts were reset to **60% syllabus breadth + 40% past-paper share**, rounded to multiples of 5 with a minimum of 5, so every listed chapter keeps slots even where the four papers had none. Before and after numbers are in `nest_plan_calibration.json` and in the plan document.
- Largest increases: Biology classification, biomolecules, evolution; Chemistry coordination compounds, alcohols and phenols; Mathematics relations and functions, complex numbers and polynomial roots, conics, continuity and differentiability; Physics units, atoms, nuclei.
- Largest decreases: human physiology and reproduction chapters, animal and plant kingdom; organic principles; applications of derivatives, statistics, linear programming; alternating current, current electricity, straight-line motion.
- Four focus lines were added in Mathematics to give room for the extra slots (polynomial roots, circles touching lines and each other, functional equations).

## What this means for writing questions

1. Biology: at least half of each section should be an experiment, data, pedigree, graph or applied-case question; keep recall-only questions to the easy slots.
2. Chemistry: organic questions should mostly be two- or three-step sequences or reasoned orderings; physical questions should need a set-up, not one formula.
3. Mathematics: prefer "number of solutions", "which statement must hold" and parameter-condition questions to long routine computation.
4. Physics: include one or two estimation or real-context questions per section and at least one dimensional-analysis or significant-figure question in most tests.
5. Figures: Biology and Physics papers use about four per section. Our limit stays at two image questions per section (figures are produced by hand); the remaining data should be given as tables or text.
