# IAT baseline for the 25-test audit

Written 14 November 2026, before any test file is edited. It records what the real exam looks like, using only files in this repo, and the rubric every test is scored against.

## 1. Sources used and what is missing

| Source | Where | Status |
|---|---|---|
| Official syllabus (2026) | `IISER/IISER_Aptitude_Test_Syllabus_2026.md` and the PDF beside it | In repo. Read in full. |
| Previous-year papers | `PYQ/IAT/md/` and `pdf/`: English 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025 and the 2026 provisional key | In repo. Mirror copies, not official-server downloads (`PYQ/IAT/SOURCES.md`). |
| Tagged PYQ ledger | `docs/blueprints/iat_pyq_ledger.json`, `iat_pyq_analysis.md`, `iat_pyq_chapter_counts.md` | In repo. 539 questions, each tagged by hand for chapter, task and difficulty on 29 Oct 2026. |
| Authoring rules | `docs/instructions/IAT_Instructions.md` (v3), `docs/blueprints/iat.md` | In repo. Source of truth for house rules. |
| Official information brochure | — | **Not in the repo.** The instructions file cites the 2026 brochure by link and says it was checked on 29 Oct 2026. |

**Not available, so not asserted here:**
- The 2020 paper, and any paper before 2017.
- A final (non-provisional) 2026 answer key. No PYQ answer key has been independently certified.
- The 2027 brochure. Everything below is the 2026 pattern.
- The marking scheme of each past year. The archived papers do not print it, so only the 2026 scheme recorded in the instructions file is used.
- The 60th question of the 2025 English paper (the archive copy ends at Physics Q14).

## 2. Exam pattern (2026, from `docs/instructions/IAT_Instructions.md`)

| Item | Value |
|---|---|
| Mode | Computer-based test |
| Subjects | Biology, Chemistry, Mathematics, Physics, in that order |
| Questions | 60: 15 per subject, all available to every candidate |
| Type | Single-correct multiple choice, 4 options |
| Duration | 180 minutes |
| Marking | +4 correct, −1 incorrect, 0 unattempted |
| Maximum | 240 (60 per subject) |
| Calculator | On-screen non-programmable scientific calculator; no personal calculator |
| Syllabus basis | NCERT Classes 11 and 12, as listed in the official syllabus |

Checked against the papers: eight of the nine archived English papers have 60 questions in four blocks of 15 in the order above; the 2025 copy has 59.

## 3. Topic weightage (from the tagged ledger)

Recent window = 2023–2026 (239 questions). Shares are of questions inside the current syllabus. They describe the papers; they are not a forecast. One question is about 1.7 percentage points.

**Biology (58 in scope):** Genetics and Evolution 12 (20.7%), Human Physiology 10 (17.2%), Cell 7 (12.1%), Biotechnology 6 (10.3%), Structural Organisation 5, Plant Physiology 5, Diversity 4, Ecology 4, Reproduction 3, Human Welfare 2.

**Chemistry (55 in scope):** Bonding 7 (12.7%), Organic basic principles 6 (10.9%), Coordination 5, Carbonyls and acids 5, Atomic structure 4, Thermodynamics 4, Solutions 3, Electrochemistry 3, Kinetics 3, Periodicity 2, Haloalkanes 2, Alcohols 2, Amines 2, Biomolecules 2, and 1 each for Basic concepts, d- and f-block, Equilibrium, Redox, Hydrocarbons.

**Mathematics (59 in scope):** Coordinate geometry 6, Differentiation 6, Integration 6 (10.2% each), Relations and functions 5, Matrices and determinants 4, Probability 4, then 3 each for Permutations, Binomial, Complex numbers, 3-D geometry, Sequences, Limits, Differential equations, and 2 each for Quadratics, Vectors, Statistics; Trigonometry 1.

**Physics (59 in scope):** Electrostatics (fields and potential) 6 (10.2%), Work-energy 5, Oscillations 4, Ray optics 4, then 3 each for Rotation, Thermodynamics, Waves, Induction, and 1–2 each for every other listed chapter. Laws of Motion had 0 as a primary topic in the window.

Class 11 to Class 12 split in the window is close to even in every subject (Biology 33/27, Chemistry 28/32, Mathematics 28/32, Physics 30/29).

The full all-years table per chapter is in `docs/blueprints/iat_pyq_chapter_counts.md`.

**Outside the current syllabus although seen in old papers (22 questions flagged):** transport in plants, mineral nutrition, digestion, environmental issues; detailed p-block, states of matter, solid state, polymers, metallurgy, surface chemistry; mathematical induction, linear programming (heading only); logic gates, Zener diode. A mock question on any of these is out of syllabus.

## 4. Question style, traps and numerical share

Dominant task per question, 2023–2026:

| Task | Biology (60) | Chemistry (60) | Mathematics (60) | Physics (59) |
|---|---:|---:|---:|---:|
| Recall | 8 | 4 | 0 | 1 |
| Conceptual | 21 | 19 | 22 | 7 |
| Numerical | 5 | 12 | 37 | 31 |
| Table / match | 7 | 1 | 0 | 0 |
| Diagram / structure | 12 | 20 | 1 | 19 |
| Graph | 4 | 4 | 0 | 1 |
| Experiment | 3 | 0 | 0 | 0 |

- **Numerical share:** Biology about 8%, Chemistry about 20% (more if structure questions that need a count are included), Mathematics about 62%, Physics about 53% by dominant task. Many Physics diagram questions also end in a symbolic or numeric result.
- **Biology:** mostly "which statement is correct / false", mechanism and consequence, matching tables, one or two crosses or gel/plasmid maps per paper. Traps swap ploidy, generation, cause and effect.
- **Chemistry:** about a third is organic reaction schemes drawn as structures; physical chemistry gives data and constants in the stem. Traps: wrong selectivity, a missed neutralisation before a buffer, a reversed Nernst quotient, adding E° values instead of ΔG°.
- **Mathematics:** every question needs working; none is a definition. Answers are often "which statement is TRUE" about a function or a set. Traps: strict versus closed endpoints, inverse-trig branches, zero as a leading digit, "at least" versus "exactly".
- **Physics:** symbolic answers are common; the model must be chosen before substituting. Traps: energy versus momentum conservation, sign of work or emf, rms versus mean, the circuit after it has settled.

My own reading of the full 2025 paper agrees with the ledger's description.

## 5. Difficulty

Editorial tiers from the ledger, 2023–2026 (no candidate data exists):

| Tier | Biology | Chemistry | Mathematics | Physics |
|---|---:|---:|---:|---:|
| Easy | 12 | 9 | 9 | 5 |
| Medium | 39 | 38 | 38 | 31 |
| Hard | 9 | 13 | 13 | 23 |

- Roughly 15% easy, 62% medium, 24% hard over the window, with Physics the hardest section.
- The house target for mocks is 9 easy / 42 medium / 9 hard per paper (15% / 70% / 15%), with the extra easy and extra hard slot rotating by subject. This is the user's editorial choice of 28–29 Oct 2026, slightly easier than the recent papers at the hard end.
- Real easy questions are still one clean idea at NCERT depth (for example the 2025 centromere and triglyceride items). Real hard questions take about 4–5 minutes.

## 6. State of the 25 mock tests before the audit

Files: `IISER/IAT TEST 1.json` and `IISER/IAT NEW TEST 2.json` … `IAT NEW TEST 25.json` (25 confirmed). Last IISER commit before the audit: `7c7269e`.

`python3 validate_iat.py` on all 25: 0 errors. Every paper has 60 questions, 15 per subject, 9/42/9 tiers, and exactly 15 of each answer letter. All 25 are `pending_revision`. This is a structure check only.

Explanation length (characters), which hints at where solutions are thin:

| Tests | Shortest | Median |
|---|---:|---:|
| 1 | 484 | 1,019 |
| 2–5 | 567–659 | 721–790 |
| 6–15 | 294–449 | 519–695 |
| 16–25 | 516–795 | 883–1,103 |

A first sample from Test 12 found two items labelled medium that are one-step (torque ratio τ = Iα; allowed quantum numbers), with one-line working. Tests 6–15 are the likeliest to need the most rewriting.

## 7. Audit rubric (applied to every test)

1. **Pattern:** 60 questions, 15 per subject in B, C, M, P order, 4 options, +4/−1/0, 180 minutes.
2. **Syllabus:** each question maps to a line of the 2026 syllabus; section 3's out-of-scope list is a fail.
3. **Difficulty:** label matches real effort; a one-step item is not medium; hard is solvable in 4–5 minutes.
4. **Repetition:** no duplicate or near-duplicate inside a test or across the 25 (`tools/iat/check_series_overlap.py` plus reading); no copied PYQ.
5. **Answer key:** each question is solved again from the stem before looking at the key; options, units and data are checked; exactly one option is right.
6. **Solution quality:** see section 8.
7. **Formatting:** KaTeX and mhchem parse, options intact, every `image_reference` has a file and a register entry.

Scores per test in the report: pass / minor / fail for each of the seven.

## 8. Solution format used in the audit

The user's rules of 14 Nov 2026 are applied on top of the repo format, which the validator still enforces (first line `Answer: (X)`, the labels `Why:`, `Why not the others:`, `Key point:`, and for Mathematics and Physics `Worked derivation:` with display maths).

- **Mathematics and Physics:** `Given` → `Formula` → `Worked derivation` (substitution and every algebraic step as displayed equations) → final value with units → `Check`. The content under every label is equations and symbols, not sentences. `Why:` carries the governing law and its condition as an equation; each wrong option is shown by the erroneous equation that produces it. No phrases such as "we can see that".
- **Chemistry and Biology:** concept, reasoning for the correct option, and a separate reason why each wrong option fails. Numerical Chemistry also shows the full calculation with units.
- The final answer in the solution must equal the keyed option.

**One point needs the user's confirmation** (work proceeds on this reading meanwhile): the repo labels `Why:`, `Why not the others:` and `Key point:` are kept for Mathematics and Physics, filled with equations instead of prose, so the existing validator and PDF exporter keep working.
