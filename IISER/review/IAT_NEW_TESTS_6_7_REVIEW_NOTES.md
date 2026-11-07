> **Historical snapshot — milestone corrections, 4 November 2026:** Later canonical changes supersede affected content, answer descriptions, page counts and validation claims below. Read [the correction report](milestone15_fixes/CORRECTION_REPORT.md) and its final source-bound evidence for the current Tests 1–15 checkpoint.

# IAT New Tests 6 and 7 — authoring and review notes

1 November 2026. Both are `pending_revision` preparation drafts under the verified IAT 2026 scheme. No 2027 brochure has been verified. The stored PYQ ledger and syllabus guided topic and reasoning style; no PYQ text was copied. The 25-test slot register now records the 120 authored tasks, leaving 1,080 reservations for Tests 8–25.

## Paper and explanation checks

| Check | Test 6 | Test 7 |
|---|---:|---:|
| Questions and solutions | 60 / 60 | 60 / 60 |
| Per-subject questions | 15 each | 15 each |
| Editorial easy/medium/hard | 9 / 42 / 9 | 9 / 42 / 9 |
| Keys A/B/C/D | 15 / 15 / 15 / 15 | 15 / 15 / 15 / 15 |
| Displayed M/P derivations | 30 / 30 | 30 / 30 |
| `Why` word count, min/median (diagnostic) | 25 / 44 | 30 / 39 |
| Figures B/C/P | 2 / 2 / 2 | 2 / 2 / 2 |
| PDF pages, empty pages | 51, 0 | 51, 0 |
| Parsed math expressions | 160 | 84 |
| Render overflow / oversized blocks | 0 / 0 | 0 / 0 |

The structural validator passed both canonical JSON files. Every incorrect option has an individually labelled rebuttal. Source JSON, delivery JSON, HTML and PDF hashes agree with the respective render-check files. Rendered question and solution pages from each subject were sampled visually; equations and linked figures were legible. The automated overlap screen at its 0.78 threshold reported zero candidate pairs across Tests 1–7. This text screen misses semantic repeats, so a human editor must compare task method, data representation and traps.

## Mathematics item-level task check

These comparisons use the reasoning-demand patterns documented in `docs/blueprints/iat_pyq_analysis.md`, rather than asserting that a particular PYQ is identical. Each displayed solution was checked against its keyed option during authoring. Difficulty labels are editorial and require timed calibration.

| Test 6 ID | Task beyond direct recall | Test 7 ID | Task beyond direct recall |
|---|---|---|---|
| Q31 | Complete square, locate tangent boundary, subtract chord lengths | Q31 | Extract focal ratio and directrix from two geometric coordinates |
| Q32 | Squeeze oscillatory quotient and compare one-sided cusp slopes | Q32 | Derive a normal, solve second line-parabola intersection |
| Q33 | Test stationary point against both closed-interval endpoints | Q33 | Partial fractions with both logarithmic endpoint contributions |
| Q34 | Separate odd/even rational terms before definite integration | Q34 | Locate crossings, order curves and integrate their difference |
| Q35 | Prove restricted range, solve quadratic inverse and select branch | Q35 | Product-rule implicit slope and tangent intercept |
| Q36 | Compute scalar triple product and solve coplanarity parameter | Q36 | Counterexample to injection plus continuity proof of surjection |
| Q37 | Factor determinant, then solve nullspace at singular parameter | Q37 | Combine inverse, adjugate and 3×3 scalar determinant laws |
| Q38 | Conditional event under sampling without replacement | Q38 | Calculate a conditioned union and reject false independence |
| Q39 | Circular block count with forbidden adjacent pair | Q39 | Reduce periodic tangent to principal inverse range |
| Q40 | Collapse conjugate factors and extract signed even coefficient | Q40 | Common-normal projection for skew-line distance |
| Q41 | Two-step telescoping with two terms left at each boundary | Q41 | Distinguish vector projection from scalar projection |
| Q42 | Check two possible common roots and deduplicate three parameter values | Q42 | Enforce real conjugate root before expanding cubic |
| Q43 | Distinguish mean translation from deviation scaling | Q43 | Apply distinct-root and two strict interval bounds |
| Q44 | Separate IVP, choose positive crossing before singularity | Q44 | Count two versus one central binomial coefficients |
| Q45 | Split absolute value for opposite one-sided limits | Q45 | Shift-and-subtract a finite weighted geometric sum |

The original hard-labelled Test 6 Q35/Q37/Q42 and Test 7 Q32/Q37 were replaced with tasks requiring multiple conditions or stages after the first PDF inspection. Test 6 Q34 was replaced because its earlier reflection-integral method was too close to Test 1 Q35. Test 7 Q45 was rephrased to distinguish its weighted-series task from Test 6 Q41's telescoping task. The overlap screen was rerun after these edits.

## Figure inventory and task dependencies

Test 6: Q02 root stele/pith, Q06 pollen tube acceptance, Q17 two wet-test outcomes, Q27 initial-rate table, Q53 two positive charges, Q58 first diffraction minima. Test 7: Q02 oriented leaf mesophyll, Q06 functional-megaspore lineage, Q17 square-planar ligand positions, Q20 quantum-number table, Q56 decreasing inward magnetic flux, Q58 fourth double-slit fringe. Each is linked by its fixed ID and registered in `IISER/IAT_images.md`. The rate and quantum-number values were removed from their stems so the figures carry required information.

## Remaining academic gate

An independent subject reviewer should solve all 120 questions with the key hidden, verify one correct option and each distractor, inspect each figure at full resolution, and record corrections by stable ID. A timed student attempt is also pending. Structural validation, arithmetic spot checks, PDF rendering and a remote commit do not approve these drafts for student publication.
