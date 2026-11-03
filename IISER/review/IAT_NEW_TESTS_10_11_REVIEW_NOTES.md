# IAT New Tests 10 and 11 — authoring review

3 November 2026. Both papers are `pending_revision` preparation drafts under the verified 2026 IAT format. The official 2026 brochure states 60 single-correct questions, 15 per Biology, Chemistry, Mathematics and Physics, 180 minutes and +4/−1/0. The official admission site still presents the 2026 cycle; no 2027 brochure was verified during this session. The stored nine-year PYQ inventory and syllabus informed topics and demand, but no PYQ stem was copied.

## Paper and delivery checks

| Check | Test 10 | Test 11 |
|---|---:|---:|
| Questions and extracted PDF solutions | 60 / 60 | 60 / 60 |
| Each of four subjects | 15 | 15 |
| Editorial easy / medium / hard | 9 / 42 / 9 | 9 / 42 / 9 |
| Keys A / B / C / D | 15 each | 15 each |
| Displayed Mathematics and Physics derivations | 30 | 30 |
| `Why` words, minimum / median | 23 / 32 | 23 / 31 |
| Linked figures Biology / Chemistry / Physics | 3 / 2 / 3 | 4 / 3 / 5 |
| Review PDF pages / empty pages | 31 / 0 | 33 / 0 |
| Rendered math expressions | 34 | 33 |
| TeX overfull boxes / missing glyphs | 0 / 0 | 0 / 0 |

The canonical source and delivery JSON are identical in data. `validate_iat.py` passes both files; the XeLaTeX render checks record SHA-256 hashes for source, delivery, PDF and each linked image, 60 extracted questions and 60 solutions. Selected pages from both halves were visually inspected for typeset equations, legibility and figure placement. The temporary browser exporter dependencies were absent after workspace reset, so this batch uses the versioned XeLaTeX review exporter. The review PDFs contain the full paper followed by the answer key and worked explanations.

## Mathematics item-by-item task audit

| Slot | Test 10 reasoning | Test 11 reasoning |
|---|---|---|
| Q31 | Two positive tangent-circle radii from point equation | Ellipse focal distance, eccentricity, then directrix |
| Q32 | Bisect chord and solve right triangle | Implicit product derivative and tangent slope |
| Q33 | Compare two stationary points and endpoints; preserve tied extrema | Find both intersections and integrate upper-minus-lower curve |
| Q34 | Repeated-pole partial fractions with rational and log antiderivatives | Test injection and surjection relative to stated codomain |
| Q35 | Restricted quadratic inverse branch | Adjugate identity followed by 3×3 trace |
| Q36 | Factor determinant for both singular parameter signs | Independent-event intersection and inclusive union |
| Q37 | Condition on the *second* draw, rather than any-colour event | Circular block count and complement |
| Q38 | Adjacent binomial coefficient ratio, then weighted target coefficient | Signed binomial coefficient including cubic weight |
| Q39 | Consecutive partial sums yield an individual term | Three-factor telescoping and first strict threshold crossing |
| Q40 | Scale exponential limit and retain chain factor | Absolute-value parameter branches and nonexisting cusp limit |
| Q41 | Complement line-normal angle with line-plane angle | Separate growth IVP and apply initial condition |
| Q42 | Place identical A letters into nonadjacent gaps | Prove shortest skew-line distance bound is attained |
| Q43 | Reduce quadrant-III angle to principal branch | Scalar triple product vanishing for coplanarity |
| Q44 | Differentiate curve family and eliminate constant | Weighted mean followed by absolute deviation |
| Q45 | Factor sine quadratic, filter cosine sign and endpoints | Reduce three inverse-trig functions in different principal ranges |

The hard-labelled Mathematics items in Test 10 are Q33/Q38/Q45 and in Test 11 Q40/Q45. Their labels are editorial and still need timed student calibration. The authoring audit replaced a two-factor partial-fraction integral, a fixed-sum telescoping task and a number-swapped conditional-probability task after comparison to earlier tests.

## Figures and repetition checks

Test 10 figures: Q02 frog two atria/one ventricle and inflows, Q03 replicated DNA with unchanged centromere count, Q09 target protein band and controls, Q18 metal–water calorimeter readings, Q23 reaction-path barriers with common endpoints, Q52 circular orbit radii, Q53 opposite-charge locations, Q58 concave-mirror object and focal position.

Test 11 figures: Q01 fruit and seed layers, Q02 radial root stele, Q08 fermentation products, Q09 two noncompatible directional cloning ends, Q17 inner versus outer sulfate ion, Q22 cyanide/carbonyl electron arrows, Q28 freezing plateau, Q49 elastic versus plastic stress slope, Q52 pendulum length and lift, Q57 parallel optical layers, Q58 stopping-potential plot, Q59 direct versus cascade hydrogen emission. The relevant values or structures were removed from stems where the diagram must carry the task data.

The 0.78 cross-series similarity screen reports **zero candidates** after revisions. A text screen cannot certify semantic originality. Editorial comparison specifically replaced the Test 10 cardiac-output number swap with a two-state pressure/resistance inference, and the Test 11 series-capacitor charge repeat with a battery-connected dielectric-change ratio. A later manual scan also replaced the Hardy–Weinberg carrier-frequency number swap, the separate-gas rms-speed ratio, and the hydrogen wavelength-ratio item with population pooling, mixture rms and cascade conservation tasks. Recurring chapter themes use different givens, conclusions or reasoning steps. The one-time answer-position correction for six Test 10 Biology items and one Test 11 Biology item was reconciled with every labelled distractor explanation and revalidated.

## Remaining academic gate

Independent reviewers should solve all items with keys hidden, check syllabus scope, one-correct-option uniqueness and figure correctness at full resolution, then conduct a timed student attempt. Difficulty targets and explanation quality have not been validated by student data. These committed drafts are not approved for student publication.
