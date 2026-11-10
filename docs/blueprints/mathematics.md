# Blueprint — CUET (UG) 2027 Mathematics / Applied Mathematics (319)

**Syllabus:** `CUET SYLLABUS/Mathematics - 319.pdf` (NTA "for the year 2026", latest published): Section A1 (common), Section B1 (Mathematics), Section B2 (Applied Mathematics).
**Series:** 15 tests, `CUET/Mathematics/CUET MATHEMATICS TEST 1–15.json`.
**Sources for answers:** NCERT Mathematics Class XII Parts I–II (B1 and the common section); CBSE Applied Mathematics Class XII curriculum (B2: modulo arithmetic, alligation, time series, t-test, financial mathematics, CS/PS).

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Section A (common) | 15 questions, compulsory for everyone |
| Section B1 (Mathematics) | 35 questions |
| Section B2 (Applied Mathematics) | 35 questions |
| Attempt | all of A + all of **either** B1 **or** B2 = **50 questions** |
| Questions per test file | 85 (15 + 35 + 35) |
| Duration / marking | 60 minutes; +5 / −1 / 0; 4 options, one correct |

The section sizes are from the 2024 NTA booklet (319, code A): "15+35+35". The 2026 paper still carries both B1 items (Bayes, area) and B2 items (degrees of freedom, effective rate, parameter vs statistic). Since 2025, NTA has made every question in the chosen sections compulsory, so a candidate answers 15 + 35 = 50. Each test file stores the three sections in the same way as Accountancy B1/B2 (`sections`, `common_sections: ["A"]`, `optional_sections: ["B1","B2"]`).

## 2. PYQ analysis (NTA 2024, 2025, 2026 papers; analysed, not stored)

- **Level:** NCERT exercise level, moderate. Most items take one or two steps, with close numerical options and few long computations. Typical items: area under \(y=3x+2\) between ordinates, area between \(y=3\cos x\) and \(y=3\), \(AB=A,\ BA=B \Rightarrow A^2=A,\ B^2=B\), Bayes with letters on an envelope, effective rate for 6% compounded half-yearly, degrees of freedom \(n-1\).
- **Formats (2024, 85 questions):** about 9 match-list items (properties of \([x]\), probability-distribution constants, function types, depreciation data) and about 5 multi-statement items ("Choose the correct answer from the options given below"). There were **no** sequence, assertion–reason or passage items. The 2026 paper adds statement items on matrices (\(a_{ij}=|i-j|\)) and on parameters.
- **What this means for OurMocks:** many short numericals with traps in the distractors, plus a steady share of match and statement items that test properties and definitions together. There are no case sets.

## 3. Unit weight per test

### Section A — common (15)
| Code | Unit (A1 syllabus) | Qs |
|---|---|---|
| C1 | Algebra: matrices, determinants, inverse, matrix method | 4 |
| C2 | Calculus: second-order derivatives, increasing/decreasing, maxima and minima | 3 |
| C3 | Integration: indefinite (simple), definite, area under a simple curve | 3 |
| C4 | Differential equations: order and degree, variable separable | 2 |
| C5 | Probability distributions (simple probability, random variable, mean) | 2 |
| C6 | Linear programming: graphical method, feasible region, optimal solution | 1 |

### Section B1 — Mathematics (35)
| Code | Unit | Qs |
|---|---|---|
| M1 | Relations and functions (reflexive, symmetric, transitive, equivalence; one-one, onto) | 3 |
| M2 | Inverse trigonometric functions (domain, range, principal values) | 2 |
| M3 | Matrices (types, operations, symmetric/skew, invertibility) | 2 |
| M4 | Determinants (minors, cofactors, adjoint, inverse, area, consistency) | 3 |
| M5 | Continuity and differentiability (chain, implicit, parametric, log differentiation, second order) | 4 |
| M6 | Applications of derivatives (rate of change, monotonicity, maxima/minima) | 3 |
| M7 | Integrals (substitution, partial fractions, by parts, standard forms, definite-integral properties) | 4 |
| M8 | Applications of integrals (area under lines, circles, parabolas, ellipses in standard form) | 1 |
| M9 | Differential equations (order, degree, separable, homogeneous, linear) | 3 |
| M10 | Vectors (types, section formula, dot and cross product, projection, area) | 3 |
| M11 | Three-dimensional geometry (direction cosines, lines, angle, skew lines, shortest distance) | 3 |
| M12 | Linear programming | 1 |
| M13 | Probability (conditional, multiplication theorem, independence, total probability, Bayes) | 3 |

### Section B2 — Applied Mathematics (35)
| Code | Unit | Qs |
|---|---|---|
| AM1 | Numbers, quantification and numerical applications (modulo, congruence, alligation, boats, pipes, races, numerical inequalities) | 6 |
| AM2 | Algebra (matrices, determinants, inverse, simultaneous equations) | 4 |
| AM3 | Calculus (higher derivatives, marginal cost and revenue, monotonicity, maxima/minima, integration, CS/PS, differential equations) | 8 |
| AM4 | Probability distributions (random variable, expectation, variance, binomial, Poisson, normal) | 5 |
| AM5 | Time-based data (time series, components, trend by moving averages and least squares) | 3 |
| AM6 | Inferential statistics (population and sample, parameter and statistic, CLT, hypotheses, one-sample t-test, degrees of freedom) | 3 |
| AM7 | Financial mathematics (perpetuity, sinking fund, EMI, returns, CAGR, straight-line depreciation, bonds) | 4 |
| AM8 | Linear programming (formulation, types, graphical solution) | 2 |

A unit may move ±1 within its own section when a test needs it; section totals never change.

## 4. Difficulty (every attempted path)

| Section | Easy | Medium | Hard |
|---|---|---|---|
| A (15) | 2 | 10 | 3 |
| B1 (35) | 6 | 22 | 7 |
| B2 (35) | 6 | 22 | 7 |
| **A + B1 or A + B2** | **8** | **32** | **10** |

- **Easy:** one definition, formula or property, applied in one step.
- **Medium:** a one- or two-step computation (standard integral, derivative, determinant, probability), or a property chosen from close options.
- **Hard:** a multi-step computation (Bayes with three causes, shortest distance, a linear DE with a non-trivial integrating factor, EMI or bond valuation, a t-statistic), a match list or statement set where every part needs working, or a trap that NCERT students often fall into.
- **Depth progression:** Tests 1–5 are accessible, 6–10 deeper, 11–15 the hardest, while keeping 8 / 32 / 10.

## 5. Formats (every test)

| Format | A | B1 | B2 | Attempted path |
|---|---|---|---|---|
| Match List-I / List-II | 1 | 3 | 3 | 4 |
| Statements "(A)–(D), choose the correct" | 2 | 4 | 4 | 6 |
| Numerical / direct single-answer | 12 | 28 | 28 | 40 |

- Match items are in different units within a section, and their correct patterns differ within a test.
- Statement items are medium or hard. They vary between "which are correct" and "which are NOT correct".
- No sequence, assertion–reason or passage items, because the NTA 319 papers have none.
- No figures. Regions, graphs and tables are described in words or given as KaTeX tables.

## 6. Notation and explanations

- All mathematics is KaTeX: inline `\( … \)`, display `\[ … \]`. Matrices use `\begin{bmatrix} … \end{bmatrix}`, determinants `\begin{vmatrix} … \end{vmatrix}`.
- **Numerical explanation:** `Answer:` (generated) / `Given:` / `Formula:` / `Step 1 … Step n` / `Common mistake:` (the slip behind at least one distractor) / `Key point:`.
- **Concept explanation** (definitions, properties, statements): `Why:` / `Why not the others:` / `Key point:`.
- Every distractor comes from a real slip, such as a sign error, a wrong limit, the wrong formula, \(n\) instead of \(n-1\), or simple interest instead of compound.

## 7. Answer key and order

- Odd tests: A 4/4/4/3; B1 and B2 9/8/9/9 each, so each path is **13/12/13/12**.
- Even tests: A 3/4/4/4; B1 and B2 9/9/8/9 each, so each path is **12/13/12/13**.
- `shuffle_test.py` mixes units inside each section and keeps B1 and B2 separate; no answer run is longer than 3.
- For text options, the correct option is never clearly the longest (≤ 1.15 × the next one).

## 8. No repeats

`docs/blueprints/mathematics_coverage.md` §C records, for each unit and test, the skill each item tests (for example `det adj kA`, `bayes three urns`, `emi reducing`). A key may be used **at most three times** in the series, in different tests and with different numbers or functions. Mathematics skills recur by nature, so the limit is three rather than the two used for theory subjects. Stems are checked against earlier tests for near-duplicates (`OVERLAP`).

## 9. Out of scope (not tested)

Anything not in the 2026 syllabus: integrals of trigonometric powers by reduction, \(\int_0^{\pi/2}\log\sin x\,dx\)-type results, planes in 3D (only lines are in the syllabus), the Mean Value Theorem, approximations by differentials, binary operations, the composition of functions beyond simple cases, and permutations/combinations as a topic. The old bank's Level 10 questions on \(\int \sin^6 x\) and \(\log \sin x\) are not reused. B2 is limited to its listed topics: no index numbers, no regression, no chi-square.
