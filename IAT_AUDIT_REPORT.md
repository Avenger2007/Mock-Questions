# IAT audit report (in progress)

Audit started 14 November 2026 against `IAT_BASELINE.md`. One row per test. A test is listed only after every one of its 60 questions has been solved again from the stem, before looking at the stored key.

Scores: **pass**, **minor** (small fixes made) or **fail** (questions replaced or keys corrected).

| Test | Pattern | Syllabus | Difficulty | Repetition | Answer-key errors | Solution quality (before → after) | Status |
|---|---|---|---|---|---|---|---|
| 1 | pass | pass | pass | pass (within test; series check pending) | 0 of 60 | Maths/Physics had prose in the working → 30 rewritten as equations only; Biology/Chemistry already met the standard | Clean |
| 2 | pass | pass | minor: 6 one-step items labelled medium, strengthened (Q18, Q25, Q28, Q47, Q51, Q56) | fail → fixed: Q11 and Q43 repeated Test 1 tasks, replaced | 0 of 60 | Maths/Physics prose and thin rebuttals → 30 rewritten as equations only; 11 Biology/Chemistry numerical solutions expanded | Clean after fixes |
| 3–25 | — | — | — | — | — | — | Not yet audited |

## Changes made

### Test 1 (`IISER/IAT TEST 1.json`)
- No question, option, figure or key changed. All 60 answers re-derived and confirmed; the three Physics figures (Q46, Q53, Q54) were opened and match their questions.
- Q31–Q60 (Mathematics and Physics): explanations rewritten to given data → formula → substitution and each algebraic step → result with units → an independent check, with every line an equation. Each wrong option is now shown by the erroneous equation that produces it. Source text: `IISER/audit/solutions/test01.txt`.
- Q1–Q30 (Biology and Chemistry): unchanged; each already gives the concept, the reasoning and a separate reason for every wrong option, and numerical Chemistry shows its calculation.
- Checks after the edit: `validate_iat.py` 0 errors; strict KaTeX/mhchem parse of 615 expressions, 0 errors.

### Test 2 (`IISER/IAT NEW TEST 2.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q3, Q4, Q17, Q27, Q55 and Q57 agree with their questions.
- **Replaced for repetition (same key letter kept):** Q11 repeated the "unaffected sibling of an affected child, 2/3 carrier" task of Test 1 Q13 → now an X-linked recessive risk updated by an unaffected first son (answer 1/12). Q43 repeated the "perpendicular bisector meets a circle" locus task of Test 1 Q34 → now "z + 4/z is real, z non-real, find |z|" (answer 2).
- **Strengthened because a 'medium' label sat on a one-step item (same topic and key letter):** Q18 (ionisation from n = 2 → kinetic energy of the ejected electron), Q25 (osmotic-pressure ratio now against dissociated NaCl), Q28 (Hess's law now needs a reversal and a 2 mol scale-up), Q47 (work by F = 2x → speed from the work–energy theorem), Q51 (rms speeds at different temperatures and molar masses), Q56 (balanced bridge → also the battery current).
- Q31–Q60: all 30 Maths/Physics solutions rewritten as equations only, each with an independent check.
- Q5, Q6, Q11, Q13, Q18, Q25–Q30: Biology/Chemistry numerical solutions rewritten with every step and a specific reason for each wrong option.
- Checks: `validate_iat.py` 0 errors, key balance still 15/15/15/15, tiers 9/42/9; KaTeX parse 456 expressions, 0 errors.
- Source text: `IISER/audit/solutions/test02.txt`.

## Not verified
- Rendered PDF pages were not regenerated or inspected for Test 1 after the edit (the exporter needs Playwright and Chromium).
- Series-wide near-duplicate comparison is done after all 25 tests are read.
