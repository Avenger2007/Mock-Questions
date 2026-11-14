# IAT audit report (in progress)

Audit started 14 November 2026 against `IAT_BASELINE.md`. One row per test. A test is listed only after every one of its 60 questions has been solved again from the stem, before looking at the stored key.

Scores: **pass**, **minor** (small fixes made) or **fail** (questions replaced or keys corrected).

| Test | Pattern | Syllabus | Difficulty | Repetition | Answer-key errors | Solution quality (before → after) | Status |
|---|---|---|---|---|---|---|---|
| 1 | pass | pass | pass | pass (within test; series check pending) | 0 of 60 | Maths/Physics had prose in the working → 30 rewritten as equations only; Biology/Chemistry already met the standard | Clean |
| 2–25 | — | — | — | — | — | — | Not yet audited |

## Changes made

### Test 1 (`IISER/IAT TEST 1.json`)
- No question, option, figure or key changed. All 60 answers re-derived and confirmed; the three Physics figures (Q46, Q53, Q54) were opened and match their questions.
- Q31–Q60 (Mathematics and Physics): explanations rewritten to given data → formula → substitution and each algebraic step → result with units → an independent check, with every line an equation. Each wrong option is now shown by the erroneous equation that produces it. Source text: `IISER/audit/solutions/test01.txt`.
- Q1–Q30 (Biology and Chemistry): unchanged; each already gives the concept, the reasoning and a separate reason for every wrong option, and numerical Chemistry shows its calculation.
- Checks after the edit: `validate_iat.py` 0 errors; strict KaTeX/mhchem parse of 615 expressions, 0 errors.

## Not verified
- Rendered PDF pages were not regenerated or inspected for Test 1 after the edit (the exporter needs Playwright and Chromium).
- Series-wide near-duplicate comparison is done after all 25 tests are read.
