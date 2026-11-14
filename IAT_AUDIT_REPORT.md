# IAT audit report (in progress)

Audit started 14 November 2026 against `IAT_BASELINE.md`. One row per test. A test is listed only after every one of its 60 questions has been solved again from the stem, before looking at the stored key.

Scores: **pass**, **minor** (small fixes made) or **fail** (questions replaced or keys corrected).

| Test | Pattern | Syllabus | Difficulty | Repetition | Answer-key errors | Solution quality (before → after) | Status |
|---|---|---|---|---|---|---|---|
| 1 | pass | pass | pass | pass (within test; series check pending) | 0 of 60 | Maths/Physics had prose in the working → 30 rewritten as equations only; Biology/Chemistry already met the standard | Clean |
| 2 | pass | pass | minor: 6 one-step items labelled medium, strengthened (Q18, Q25, Q28, Q47, Q51, Q56) | fail → fixed: Q11 and Q43 repeated Test 1 tasks, replaced | 0 of 60 | Maths/Physics prose and thin rebuttals → 30 rewritten as equations only; 11 Biology/Chemistry numerical solutions expanded | Clean after fixes |
| 3 | pass | fail → fixed: Q4 (transpiration) is from the deleted Transport in Plants chapter, replaced | minor: 5 one-step items labelled medium, strengthened (Q10, Q27, Q47, Q51, Q58) | pass within test (Q42 uses the same sign-of-f(k) idea as Test 1 Q43 but with two conditions; kept) | 0 of 60 (Q30 data were unrealistic and were corrected) | 30 Maths/Physics rewritten as equations only; 7 Biology/Chemistry numerical solutions expanded | Clean after fixes |
| 4 | pass | fail → fixed: Q46 (error propagation) and Q58 (thin-film interference) are not in the 2026 syllabus, replaced | minor: 4 one-step items labelled medium, strengthened (Q27, Q51, Q53, Q54) | fail → fixed: 7 questions repeated earlier tests (Q5, Q13, Q20, Q30, Q35, Q52, Q60), replaced | 0 of 60 | 30 Maths/Physics rewritten as equations only; 14 Biology/Chemistry solutions rewritten | Clean after fixes; 2 items flagged |
| 5–25 | — | — | — | — | — | — | Not yet audited |

## Changes made

### Test 1 (`IISER/IAT TEST 1.json`)
- No question, option, figure or key changed. All 60 answers re-derived and confirmed; the three Physics figures (Q46, Q53, Q54) were opened and match their questions.
- Q31–Q60 (Mathematics and Physics): explanations rewritten to given data → formula → substitution and each algebraic step → result with units → an independent check, with every line an equation. Each wrong option is now shown by the erroneous equation that produces it. Source text: `IISER/audit/solutions/test01.txt`.
- Q1–Q30 (Biology and Chemistry): unchanged; each already gives the concept, the reasoning and a separate reason for every wrong option, and numerical Chemistry shows its calculation.
- Checks after the edit: `validate_iat.py` 0 errors; strict KaTeX/mhchem parse of 615 expressions, 0 errors.

### Test 2 (`IISER/IAT NEW TEST 2.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q3, Q4, Q17, Q27, Q55 and Q57 agree with their questions.
- **Replaced for repetition (same key letter kept):** Q11 repeated the "unaffected sibling of an affected child, 2/3 carrier" task of Test 1 Q13 → now an X-linked recessive risk traced through an affected maternal grandfather (answer 1/8). (A first draft used an update by an unaffected first son; it was changed because Test 4 Q12 already uses that update.) Q43 repeated the "perpendicular bisector meets a circle" locus task of Test 1 Q34 → now "z + 4/z is real, z non-real, find |z|" (answer 2).
- **Strengthened because a 'medium' label sat on a one-step item (same topic and key letter):** Q18 (ionisation from n = 2 → kinetic energy of the ejected electron), Q25 (osmotic-pressure ratio now against dissociated NaCl), Q28 (Hess's law now needs a reversal and a 2 mol scale-up), Q47 (work by F = 2x → speed from the work–energy theorem), Q51 (rms speeds at different temperatures and molar masses), Q56 (balanced bridge → also the battery current).
- Q31–Q60: all 30 Maths/Physics solutions rewritten as equations only, each with an independent check.
- Q5, Q6, Q11, Q13, Q18, Q25–Q30: Biology/Chemistry numerical solutions rewritten with every step and a specific reason for each wrong option.
- Checks: `validate_iat.py` 0 errors, key balance still 15/15/15/15, tiers 9/42/9; KaTeX parse 456 expressions, 0 errors.
- Source text: `IISER/audit/solutions/test02.txt`.

### Test 3 (`IISER/IAT NEW TEST 3.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q7, Q15, Q17, Q23, Q48 and Q53 agree with their questions.
- **Out of syllabus, replaced:** Q4 asked about transpiration and the vapour-pressure gradient, which belongs to Transport in Plants (not in the 2026 syllabus) → now a plant-growth-regulator question (gibberellin restores a dwarf pea; auxin on a cut stump keeps apical dominance), same key letter.
- **Data corrected:** Q30 gave a 6.0 °C rise, which implies −100.8 kJ/mol for a neutralisation. Changed to a 3.4 °C rise with a strong acid, giving the real value of −57.1 kJ/mol; options updated, key letter unchanged.
- **Strengthened one-step 'medium' items (same topic and key letter):** Q10 (detritus now includes egested material), Q27 (common-ion solubility → factor relative to pure water), Q47 (F·v → rate of change of speed), Q51 (phase difference now needs the wavelength from v and f), Q58 (optical path → extra phase for a given wavelength).
- Q3 uses Na⁺–glucose co-transport; the idea is not named in the retained chapters, but the stem supplies everything needed. Left unchanged and flagged for the user.
- Q31–Q60: all 30 Maths/Physics solutions rewritten as equations only with a check. Q4, Q10, Q11, Q20, Q21, Q27, Q30 rewritten in full.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 427 expressions, 0 errors. Source text: `IISER/audit/solutions/test03.txt`.

### Test 4 (`IISER/IAT NEW TEST 4.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q2, Q8, Q16, Q24, Q49 and Q56 agree with their questions.
- **Out of syllabus, replaced (same key letter):** Q46 maximum percentage uncertainty of R = V/I (error propagation is not in the Units list; the repo's own rule of 6 Nov removed it) → significant figures in a density. Q58 thin-film reflection (only Young's experiment, diffraction and polarisation are listed) → Young's fringe width when the apparatus is immersed in water.
- **Replaced for repetition (same key letter):**
  - Q5 primary/secondary immune response = Test 2 Q8 (and was filed under Human Physiology) → voltage-gated Na⁺ channel block: resting potential kept, no action potential.
  - Q13 cardiac output = HR × SV = Test 2 Q5 → oxygen delivered per minute from cardiac output.
  - Q20 1,2-hydride shift to a more stable carbocation = Test 2 Q19 → Lassaigne's test, blood-red colour for N and S together.
  - Q30 aryl versus alkyl C–Cl reactivity = Test 3 Q24 → SN1 rate of a tertiary halide is independent of hydroxide.
  - Q35 implicit tangent to x² + xy + y² = c = Test 3 Q32 → derivative of tan⁻¹(2x/(1 − x²)).
  - Q52 beat-frequency ambiguity = Test 1 Q52 → wave speed on a stretched string (easy).
  - Q60 half-wave rectifier mean power = Test 1 Q59 → current through a forward-biased silicon diode.
- **Strengthened one-step 'medium' items:** Q27 (mixing two different liquids), Q51 (pendulum with both L and g changed), Q53 (potential for an oblique displacement in a uniform field), Q54 (drift speed in a wire of double diameter).
- **Flagged, left unchanged:** Q55 (energy exchange in an ideal LC circuit; LC oscillations are not named in the syllabus, though the energy formulas are) and Q56 (resonance bandwidth; the sharpness of resonance is not named). The user should decide whether to keep them.
- Q31–Q60 rewritten as equations only; Q3, Q4, Q5, Q10, Q12, Q13, Q15, Q17, Q19, Q20, Q25, Q27, Q28, Q30 rewritten in full.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 453 expressions, 0 errors. Source text: `IISER/audit/solutions/test04.txt`.

## Not verified
- Rendered PDF pages were not regenerated or inspected for Test 1 after the edit (the exporter needs Playwright and Chromium).
- Series-wide near-duplicate comparison is done after all 25 tests are read.
