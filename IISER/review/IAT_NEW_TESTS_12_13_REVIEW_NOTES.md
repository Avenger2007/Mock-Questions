> **Historical snapshot — milestone corrections, 4 November 2026:** Later canonical changes supersede affected content, answer descriptions, page counts and validation claims below. Read [the correction report](milestone15_fixes/CORRECTION_REPORT.md) and its final source-bound evidence for the current Tests 1–15 checkpoint.

# IAT New Tests 12 and 13 — authoring review

3 November 2026. Both papers are `pending_revision` drafts for 2027 preparation using the verified 2026 IAT format, not an official paper or a verified 2027 notification. The official 2026 brochure specifies 60 single-correct questions, 15 in each of Biology, Chemistry, Mathematics and Physics, 180 minutes and +4/−1/0.

## Delivery and self-check

| Check | Test 12 | Test 13 |
|---|---:|---:|
| Questions and extracted PDF solutions | 60 / 60 | 60 / 60 |
| B / C / M / P | 15 / 15 / 15 / 15 | 15 / 15 / 15 / 15 |
| Editorial easy / medium / hard | 9 / 42 / 9 | 9 / 42 / 9 |
| Keys A / B / C / D | 15 / 15 / 15 / 15 | 15 / 15 / 15 / 15 |
| Linked question-bearing figures | 11 (B4,C4,P3) | 10 (B4,C2,P4) |
| Displayed math expressions in review PDF | 31 | 31 |
| PDF pages | 31 | 30 |

`validate_iat.py` reports no schema, tier, key or figure errors. The XeLaTeX render check records the SHA-256 of canonical and delivery JSON, PDF and every linked figure; all 60 question labels and all 60 solution labels were extracted; logs have no overfull lines or missing glyphs. Full-page contact sheets and representative figure pages were visually inspected. All 120 `Why` sections now have at least two connected sentences, with median 36.5 and 35 words respectively; 24 initially pooled distractor explanations were separated into individually named errors. The Test 12 prism was redrawn with a true 60° apex and surface normals so its 50° entry/exit labels agree with a 40° deviation. The Test 13 resistor node B was connected explicitly.

The text-overlap screen runs against all Tests 1–13 at threshold 0.78. It initially flagged seven close items; Test 12 Q29, Q32, Q35, Q37, Q41 and Q42 and Test 13 Q42 were replaced or materially redesigned. The final screen leaves three wording-based candidates: Test 12 Q35 uses a radical and reversing transformed bounds, whereas Test 3 Q34 uses two rational antiderivatives and Test 9 Q35 uses trigonometric symmetry; Test 12 Q42 uses a variable-coefficient integrating factor, whereas Test 9 Q42 is a nonlinear homogeneous substitution. These methods, data and requested results are distinct; their common generic integration/ODE opening words account for the text score. The residual candidates remain visible for independent review rather than being silently suppressed.

Difficulty labels are editorial, not empirical. Two easy-to-mislabel Test 12 Biology taxonomy/embryo-sac items were changed to medium and conditional-risk/resource-intervention items moved to hard. Test 13's single-step dimension item was changed to medium and its two-pass lens/mirror item to hard. Test 13 Chemistry Q20 now requires both first-ionisation exceptions. These label choices still need timed-student calibration.

## Mathematics item-level PYQ task calibration

The 2023–2026 PYQ ledger supports a mostly numerical Mathematics section with domains, linked conditions and plausible sign/count traps. These are original tasks, not PYQ copies. The table records the dominant method and a check an independent reviewer should redo.

| Test 12 | Method and check | Test 13 | Method and check |
|---|---|---|---|
| Q31 | Matrix elimination; solve both coordinates before sum | Q31 | Hyperbola asymptote slope b/a |
| Q32 | Exactly-two inclusion/exclusion across three divisibility sets | Q32 | Parameterised line family; cancel constant and k coefficients |
| Q33 | Equivalence relation; all three axioms and residue classes | Q33 | Differentiability; solve continuity, slope and point constraints |
| Q34 | Roots of unity; chord geometry before triangle area | Q34 | Integral symmetry x↔π−x |
| Q35 | Radical substitution; transform bounds and sign | Q35 | Composition domain; exclude preimages of outer pole |
| Q36 | Plane intersection; satisfy two constraints simultaneously | Q36 | Determinant row addition versus swap |
| Q37 | Global monotonicity parameter and minimum bound | Q37 | Bayes with unequal source priors |
| Q38 | Mean fixes missing datum; verify variance separately | Q38 | Ratio of adjacent binomial coefficients |
| Q39 | Removable hole; finite limit assigned | Q39 | Two weighted infinite series through one generating function |
| Q40 | Conditional coin count after first trial fixed | Q40 | Continuity parameter via scaled sine limit |
| Q41 | Sum trig roots; include both closed endpoints | Q41 | Foot of perpendicular versus correction vector |
| Q42 | Linear ODE with nonconstant coefficient and initial value | Q42 | Exactly one of two lattice checkpoints |
| Q43 | Positive distinct roots: sum, product and discriminant | Q43 | Complex conjugate-root necessity |
| Q44 | Implicit normal slope, negative reciprocal | Q44 | Homogeneous ODE substitution y=xv |
| Q45 | Scalar projection, norm versus squared norm | Q45 | Square a compound-angle sum with domain-independent result |

**Physics numerical verification anchors:** Test 12 Q47 gives x=0.20 m by energy conservation, Q49 gives terminal-speed ratio 4 from Stokes drag, Q53 gives +E₀a from signed field area, Q54 gives one-half energy with a battery connected, Q60 gives 3/8 of total initial activity. Test 13 Q47 gives g/3 for connected blocks, Q49 gives compressive stress YαΔT, Q54 reduces two equal 2R branches to R, Q57 uses the mirror-plane point as object for the return lens traversal (oblique rays need not retrace individually), and Q58 gives visibility 4/5.

## Image purpose and remaining gate

Test 12 Biology: hierarchy, leaf layers, thylakoid proton gradient and plasmid marker geometry. Chemistry: nitrile bond geometry, square-planar placements, carbonyl connectivity and vapour-pressure curves. Physics: acceleration graph, signed field graph and prism ray geometry. Test 13 Biology: algal chloroplast evidence, flower whorl insertion, primer orientation and gel fragment lengths. Chemistry: lone-pair geometry and pre/post reaction pressure chart. Physics: enclosed charges, resistor nodes, changing inward magnetic flux and diode I–V curve. The register contains exact IDs and accessibility descriptions.

A hidden-key independent academic check of all 120 answers, syllabus references and figure science, followed by timed student attempts and target-year brochure verification, remains necessary before student release. A structural pass or remote push does not grant academic approval.
