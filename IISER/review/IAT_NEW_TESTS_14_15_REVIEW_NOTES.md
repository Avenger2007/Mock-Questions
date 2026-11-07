> **Historical snapshot — milestone corrections, 4 November 2026:** Later canonical changes supersede affected content, answer descriptions, page counts and validation claims below. Read [the correction report](milestone15_fixes/CORRECTION_REPORT.md) and its final source-bound evidence for the current Tests 1–15 checkpoint.

# IAT New Tests 14 and 15 — authoring review

3 November 2026. Both are `pending_revision` papers for 2027 preparation under the verified IAT 2026 pattern. No 2027 brochure is verified. The source syllabus is the stored official 2026 syllabus; this authoring and structural review is not independent academic approval.

| Check | Test 14 | Test 15 |
|---|---:|---:|
| Questions / PDF question labels / PDF solution labels | 60 / 60 / 60 | 60 / 60 / 60 |
| B / C / M / P | 15 / 15 / 15 / 15 | 15 / 15 / 15 / 15 |
| Editorial easy / medium / hard | 9 / 42 / 9 | 9 / 42 / 9 |
| Keys A / B / C / D | 15 / 15 / 15 / 15 | 15 / 15 / 15 / 15 |
| Linked question figures, B / C / P | 2 / 3 / 4 | 2 / 3 / 3 |
| Displayed expressions / PDF pages | 31 / 31 | 31 / 29 |

`validate_iat.py` reports no schema, fixed-ID, option uniqueness, tier, key-balance, figure or solution-component errors. The PDF render checks record source/delivery JSON, PDF and linked-image hashes; XeLaTeX emitted no overfull or missing-glyph warnings. Representative pages from both question and solution halves were rendered and visually inspected. All 120 explanations have at least two connected `Why` sentences and name a separate error for each of the three rejected options. All 30 Mathematics and 30 Physics entries include a displayed worked derivation. This is an author-side check, not a hidden-key expert verification.

## Full-series repetition audit

The 0.78 text-overlap screen initially found an exact earlier constant-term task in Test 8, an exact rational integral in Test 7, an almost matching Hinsberg-class task in Test 9, and another conditional red/blue urn task in Test 10. They were replaced:

- Test 14 Q40 now solves an inverse coefficient-and-exponent condition with two valid parameter values.
- Test 14 Q34 uses a repeated-pole partial fraction and a rational antiderivative.
- Test 14 Q21 combines carbylamine with cold diazonium coupling to distinguish primary aromatic amine.
- Test 14 Q38 conditions on the parity of the product of two numbered tickets.
- Test 14 Q33 changes the earlier quadratic implicit tangent to a product-and-cubic implicit curve; Q41 replaces a weighted geometric sum with separate alternating/harmonic endpoint tests.
- Test 14 Q28 replaces the earlier Be/B ionisation exception with a successive-energy jump and group inference. Test 15 Q19 replaces the earlier cyanide-carbonyl arrow question with an alkene bromination chemoselectivity question.

The final screen leaves four wording candidates for independent editorial judgment: Test 15 Q35 (rational derivative sign) versus Test 8 Q32 (cubic derivative sign); Test 15 Q33 (area between a parabola and the axis) versus Test 4 Q34 (parabola and line); and Test 14 Q34 versus Tests 3 Q34 and 7 Q33 (all begin with a definite rational integral, but the new repeated pole changes decomposition and antiderivative). None is an exact or number-swapped stem. Topic overlap alone is permitted; the distinct calculations and traps should still be reviewed with the entire series.

## Mathematics: item-level PYQ-style calibration

The acquired recent PYQs support numerical, linked-constraint and sign/count reasoning within the NCERT syllabus. These are original questions. An independent reviewer should recompute every result and verify the level, especially editorial hard labels.

| Test 14 | Method and result anchor | Test 15 | Method and result anchor |
|---|---|---|---|
| Q31 | Circle centre-to-horizontal-line distance; y=2 | Q31 | Diameter endpoints fix centre; chord length 2√5 |
| Q32 | Compare both endpoints and interior stationary value; max 3 | Q32 | Focus/directrix gives a²=25, b²=16 |
| Q33 | Product and chain rules in implicit curve; slope −1/2 | Q33 | Symmetry and intercepts give parabola area 32/3 |
| Q34 | Repeated-pole decomposition and both bounds; 1/2−ln(4/3) | Q34 | Logarithmic substitution changes bounds; 1/2 |
| Q35 | Restricted square inverse; √x | Q35 | Rational derivative sign; decreasing on (0,3) |
| Q36 | Full 3D determinant and negative z orientation viewed from +z | Q36 | Range by AM–GM and reciprocal collisions |
| Q37 | Strict monotonicity and onto range for cubic-plus-linear | Q37 | Adj(3×3) determinant equals 2²=4 |
| Q38 | Conditional even-product pairs; 1/7 | Q38 | Exclusivity contradicts independence at positive probabilities |
| Q39 | Multiset stars and bars, C(6,2)=15 | Q39 | Count cos(3x)=1 on half-open full period; 3 |
| Q40 | Constant-term coefficient 15 permits p=1 or 4; sum 5 | Q40 | Line-plane sine of angle from normal projection; 2/3 |
| Q41 | Power series radius plus two unequal endpoint outcomes; [1,3) | Q41 | Collinearity and segment ratio 2:3 |
| Q42 | Each common root gives k=5 or 4; sum 9 | Q42 | Complex equidistance gives imaginary axis |
| Q43 | Variance scales by coefficient squared; 36 | Q43 | Quadratic endpoint signs give strict k>2 |
| Q44 | Eliminate arbitrary family constant; y′=2y/x | Q44 | Sum paired binomial coefficients 112 |
| Q45 | Subtract constant and linear exponential terms; 2 | Q45 | Difference of consecutive partial sums; 26 |

**Physics answer anchors:** Test 14 Q48 integrates 8 J force work then adds the 4 J initial kinetic energy, giving speed 2√3 m/s; Q49 rotational fraction is 1/3; Q57 Cartesian lens signs give a virtual upright image 10 cm left; Q60 removes 100/min background before applying two half-lives, giving 275/min. Test 15 Q47 adds two 1% relative errors to 2%; Q49 annulus inertia is 5mR²/8; Q50 gross work 200 J minus 20 J diverted stirring is 180 J useful; Q55 three half-lives leave 100 of 800 parents and 700 stable daughters.

## Figure checks and release gate

Test 14 Biology figures encode floral whorls and four food-web transfers; Chemistry shows dipole geometry, a Daniell cell and staged stoichiometry; Physics shows an F-x graph, buoyancy geometry, equal positive charges and a near-focus lens object. Test 15 Biology shows frog return paths and a bundle sheath; Chemistry contrasts ligand denticity, aromatic amine protection and two Arrhenius slopes; Physics shows an accelerating tank, glass-to-air incidence and two-slit geometry. The register ties all 17 exact IDs to PNGs, with accessibility text. Figures contain no answer letter or computed solution.

Before student publication: an independent subject specialist should solve all 120 items without viewing keys, check every diagram and distractor, conduct timed attempts to calibrate difficulty, and verify the eventual 2027 notification. Commit and push preserve this review draft; they do not signify academic approval.
