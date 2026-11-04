# IAT Tests 1–15: milestone corrections

Completed locally 3 November; recovery and delivery verified 4 November 2026. Branch: `fix-iat-milestone-15`. Comparison baseline: `f06d700f1c38516efc7187dc2a5758550afc1e9c`. Status: corrections implemented; independent academic and timed review pending.

The audit's documented scientific, syllabus, repetition, explanation and figure findings have been addressed in the canonical JSON at their existing IDs. All 15 delivery JSON, HTML and PDFs have been regenerated. The frozen audit remains in `IISER/audit/milestone_15/`; it describes the pre-correction snapshot.

## What changed

There are **202 changed question records**: 79 stems, 77 option lists, 192 explanations, 80 focus/syllabus-anchor records, 25 image descriptions and four difficulty labels. These counts overlap. The manually authored replacement/correction sources cover 78 IDs; additional stem edits clarify existing wording and figure use. Fifteen images were redrawn and 25 complete image specifications updated. No question was removed, renumbered or reordered; all stored answer letters remain at their original positions. Some selected answer *content* changed when an invalid or repeated item was replaced.

| Finding | Implemented correction |
|---|---|
| T05 Q02 frog pulmonary return | Distinguishes lung return from cutaneous/systemic return; removes the claim that pulmonary veins return skin blood. |
| T05 Q21 carbonate experiment | Explicit staged model: 10 mmol acid first forms bicarbonate, remaining 5 mmol releases 0.22 g CO2. Stem, choices and calculation agree. |
| T11 Q14 sodium-coupled uptake | States external/internal concentrations, zero voltage, glucose direction and absence of direct ATP supply, resolving the gradient ambiguity. |
| T14 Q41 unlisted general-series convergence | Replaced by an increasing positive GP with specified sum/product and a finite five-term sum. No alternating-series or general power-series convergence test is required. |
| T09 Q15 distractor-label errors | Each wrong exponent is matched to its actual alternative; the selected option is no longer rebutted. All 900 explanations now undergo the label check. |
| T04 Q38 equivalent fractions | Replaced with conditional coin-run enumeration and four distinct choices; added exact-rational option-equivalence screening. |
| T14 Q37 functions under matrix allocation | Restored a genuine inverse-matrix trace task at the existing matrix slot. |
| Stale 9/39/12 guidance | Reconciled the analysis with the current editorial 9 easy / 42 medium / 9 hard policy. This is not an official quota. |
| Brief or prose-only working | Expanded selected solutions into intermediate equations and numbered deductions; migrated Test 1's WHY/alternative sections and displayed all 30 Mathematics/Physics derivations. Added authored Chemistry calculations. |
| Weak demand and implausible alternatives | Reworked the audit's identified hard/medium examples and additional items using linked constraints, branch/domain decisions, physical accounting and plausible errors. Demand remains an editorial judgement pending timed evidence. |

The four difficulty edits are paired: T05 Q02 becomes medium and the strengthened filtration/reabsorption T05 Q12 becomes hard; T09 Q31 becomes medium and the strengthened nonlinear initial-value T09 Q42 becomes hard. Paper and subject tier counts remain consistent with the rotating policy.

## Documented repeated-task clusters

The following replacements resolve the specific 15 clusters in the original audit. A shared syllabus technique can recur; the original identical situations and requested results do not remain repeated within these clusters.

| Cluster | Replaced angle at existing ID(s) |
|---|---|
| R01 implicit tangent | T11 Q32: parametric horizontal tangent and second derivative. |
| R02 identical parabolic area | T07 Q34: absolute-value integral split at its sign change. |
| R03 identical trigonometric integral | T13 Q34: exponential integration by parts. |
| R04 identical line-plane angle | T15 Q40: infer a parallel direction parameter and perpendicular distance. |
| R05 shifted-square inverse | T10 Q35: rational inverse with excluded value; T14 Q35 uses logarithmic inverse/domain reasoning. |
| R06 identical telescoping sum | T06 Q41: infer a GP ratio from adjacent equal-length blocks, then its infinite geometric sum. |
| R07 positive-root threshold | T12 Q43: combine real positive roots with a sum-of-squares bound. |
| R08 repeated fixed point of a line pencil | T09 Q44: minimise positive-intercept triangle area; T13 Q32: construct diameter-circle tangent. |
| R09 partial-sum differencing | T10 Q39: recover square terms from odd increments; T15 Q45: inserted arithmetic means. |
| R10 pooled variance | T03 Q43: standard deviation from moments; T09 Q38: absolute deviation about the median. |
| R11 single defective-item Bayes | T13 Q37: positive-then-negative observations with conditional independence. |
| R12 d6 high/low spin | T08 Q17: geometrical and optical multiplicity with connected chelate donors. |
| R13 repeated booster response | T07 Q08: parasite transmission intervention; T13 Q08: helper/B-cell cooperation and downstream bypass. |
| R14 diazonium coupling versus hydrolysis | T13 Q25: directing-group strategy followed by reduction and diazonium replacement. |
| R15 repeated chelate-effect explanation | T15 Q17: nitrite donor connectivity and linkage isomerism. |

The final lexical screen at 0.78 flags eight pairs, with no exact or number-masked identical stems. They were inspected: rational versus polynomial monotonicity; exponential integration by parts versus simple partial fractions; linear versus nonlinear homogeneous ODE; substitution versus rational decomposition; substitution versus trigonometric integration by parts; one-parabola versus two-curve enclosed area; repeated-pole partial fractions versus a mixed rational difference; and repeated-pole versus simple-pole partial fractions. These use different mathematical objects or constraints and were retained. This is targeted editorial comparison, not a proof that no semantic repetition remains anywhere in the bank. The original audit demonstrates why a green text screen alone is insufficient.

## Syllabus and PYQ calibration

Changed focus records include explicit listed-subtopic anchors in the JSON and revision TSVs. The general-series breach is removed; the revised T13 Q39 also uses finite AP/GP comparisons. Frog anatomy, renal handling, immunity, coordination, stoichiometry, capacitance, induction and the replacement mathematics stay within the stored 2026 syllabus families. Hypothetical classification data in T13 Q37 tests probability rather than medical knowledge.

The stored 539-entry PYQ ledger remains the comparison evidence. Examples used to assess the revised mathematical demand include:

| Stored PYQ benchmark | Revised demand comparison |
|---|---|
| 2024 Mathematics Q2, PDF p35: chained geometric loci | T15 Q42 preserves squared distances and completes a circle; T15 Q31 additionally links circle geometry and tangent intersection. These are original tasks, not rewrites of the PYQ. |
| 2024 Mathematics Q4, p37: sequence/partial-sum constraint | T10 Q39 derives terms from increments; T13 Q39 links a GP term count to a separate AP sum. |
| 2024 Mathematics Q8, p41 and 2026 Q6, p38: relation properties | T08 Q34 requires closure, equivalence classes and minimum additions rather than merely recognising a relation label. |
| 2024 Mathematics Q9, p42: finite binomial identity | T11 Q38 combines first and second weighted coefficient sums; the explanation shows the differentiation and evaluation. |
| 2024 Mathematics Q14, p47: initial value and ODE transformation | T09 Q42 carries a positive branch/domain through a homogeneous substitution; T13 Q44 then proves curve ordering before an area integral. |
| 2026 Mathematics Q1, p33: short quadratic-coefficient reasoning | Direct questions remain appropriate. T15 Q43 adds two strict root-location intervals; it is not classified by its chapter name alone. |
| 2026 Mathematics Q7, p39: integral with a branch change | T07 Q34 explicitly splits an absolute value at zero; this accessible item is intentionally shorter than multi-stage hard items. |
| 2026 Mathematics Q12, p44: GP constrained by a recurrence | T14 Q41 uses positivity, sum/product, ordering and a finite sum, all within the listed sequence syllabus. |

These comparisons do not establish identical difficulty or measured timing. The 2026 source is a provisional-key document; its option-letter convention is not used to infer exam answer balance. No verified 2027 compliance is claimed.

`chapter_coverage.json` compares all 60 subject/test groups against their reservations. Family counts match after explicitly reporting legacy name aliases. Old combined headings in the pilot are not silently treated as precise independently reviewed classifications. This is metadata consistency, not a new content-based retagging of all 900 items or proof of equal subtopic coverage.

## Verification and limits

| Check | Result / scope |
|---|---|
| Strengthened structural/design validator | 15/15 papers, 900 questions pass, including Test 1's current explanation gate. Checks keys, counts, image links, display equations, exact-rational alternatives and distractor labels. |
| Changed-item calculation probes | 59/59 author-side symbolic, rational or exhaustive checks from transcribed inputs; selected answer content is checked. This is not an independent 900-answer certification. |
| Strict KaTeX/mhchem parsing | 1,770 expressions parse without errors across 15 offline HTML deliveries. Browser layout was not tested because a compatible browser was unavailable. |
| XeLaTeX PDF checks | All 15 PDFs regenerated: 493 pages, 60 question labels and 60 solution labels per paper, no empty pages, overfull-box or missing-character warnings. |
| Visual review | All 15 redrawn figures and 23 selected solution pages reviewed; selected page IDs are recorded in `visual_sample_pages.json`. Not every one of the 493 pages received a fresh visual reading. |
| Delivery integrity | Canonical and delivery JSON are byte-identical; PDF, HTML and all 118 linked image hashes bind to final source hashes. |
| Preservation | All 900 IDs, order and stored answer letters preserved. `main` and previous branches are not overwritten by this repair branch. |

The bank remains **pending independent subject review with keys hidden and timed attempts**. Structural, symbolic and rendering passes cannot establish scientific correctness, meaningful challenge or originality for every unsampled item. The implemented corrections should be reviewed from these final source hashes before student release.

## Evidence and continuation

- `item_change_ledger.json`: every changed question and field.
- `final_manifest.json`: final source/delivery/image checksums and PDF page counts.
- `structural_validation.json`, `arithmetic_checks.json`, `math_parse.json`: current checks.
- `overlap_screen.json`, `chapter_coverage.json`, `visual_sample_pages.json`: supporting evidence and explicit scope.
- `IISER/revisions/README.md`: authored correction sources and reproduction order.

The instruction file now requires displayed mathematical working, scientific assumptions, all three correctly labelled alternative explanations, syllabus anchors, actual method comparison and meaningful figures for every test. Historical assembly and plan-generation scripts stop before overwriting corrected files. Earlier review notes and pilot arithmetic records are dated historical evidence unless their hashes match the current source. Continue from the remote `fix-iat-milestone-15` checkpoint rather than an older scratch path or test-generation branch.
