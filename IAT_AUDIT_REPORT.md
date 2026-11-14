# IAT audit report (in progress)

Audit started 14 November 2026 against `IAT_BASELINE.md`. One row per test. A test is listed only after every one of its 60 questions has been solved again from the stem, before looking at the stored key.

Scores: **pass**, **minor** (small fixes made) or **fail** (questions replaced or keys corrected).

| Test | Pattern | Syllabus | Difficulty | Repetition | Answer-key errors | Solution quality (before → after) | Status |
|---|---|---|---|---|---|---|---|
| 1 | pass | pass | pass | pass (within test; series check pending) | 0 of 60 | Maths/Physics had prose in the working → 30 rewritten as equations only; Biology/Chemistry already met the standard | Clean |
| 2 | pass | pass | minor: 6 one-step items labelled medium, strengthened (Q18, Q25, Q28, Q47, Q51, Q56) | fail → fixed: Q11 and Q43 repeated Test 1 tasks, replaced | 0 of 60 | Maths/Physics prose and thin rebuttals → 30 rewritten as equations only; 11 Biology/Chemistry numerical solutions expanded | Clean after fixes |
| 3 | pass | fail → fixed: Q4 (transpiration) is from the deleted Transport in Plants chapter, replaced | minor: 5 one-step items labelled medium, strengthened (Q10, Q27, Q47, Q51, Q58) | pass within test (Q42 uses the same sign-of-f(k) idea as Test 1 Q43 but with two conditions; kept) | 0 of 60 (Q30 data were unrealistic and were corrected) | 30 Maths/Physics rewritten as equations only; 7 Biology/Chemistry numerical solutions expanded | Clean after fixes |
| 4 | pass | fail → fixed: Q46 (error propagation) and Q58 (thin-film interference) are not in the 2026 syllabus, replaced | minor: 4 one-step items labelled medium, strengthened (Q27, Q51, Q53, Q54) | fail → fixed: 7 questions repeated earlier tests (Q5, Q13, Q20, Q30, Q35, Q52, Q60), replaced | 0 of 60 | 30 Maths/Physics rewritten as equations only; 14 Biology/Chemistry solutions rewritten | Clean after fixes; 2 items flagged |
| 5 | pass | pass; Q58 used the term 'fringe visibility', which the NCERT text does not define, re-asked | minor: 2 one-step items labelled medium, strengthened (Q53, Q56) | fail → fixed: 6 questions repeated earlier tests (Q3, Q19, Q20, Q22, Q57, Q60), replaced | 0 of 60 | 30 Maths/Physics rewritten as equations only; 12 Biology/Chemistry solutions rewritten | Clean after fixes; 2 items flagged |
| 6 | pass | fail → fixed: Q46 (error propagation) replaced; Q37 reworded (the word 'nullspace' is not in NCERT) | fail → fixed: Q54 was labelled hard but was one step, replaced; Q51 was filed under Oscillations but was not SHM, replaced | fail → fixed: 11 questions repeated earlier tests or another question in this test, replaced | 0 of 60 | 30 Maths/Physics rewritten as equations only; 13 Biology/Chemistry solutions rewritten | Clean after fixes; 3 items flagged |
| 7 | pass | fail → fixed: Q45 (arithmetic-geometric series) is not in the 2026 syllabus, replaced | pass | fail → fixed: 12 questions repeated earlier tests or another question in this test, replaced | 0 of 60 | 30 Maths/Physics rewritten as equations only; 15 Biology/Chemistry solutions rewritten | Clean after fixes; 3 items flagged |
| 8 | pass | fail → fixed: Q60 (thin-film interference) replaced | pass (Q4 is a simple subtraction labelled medium; flagged) | fail → fixed: 14 questions repeated earlier tests, replaced or re-asked | 0 of 60; Q33 had a malformed option, fixed | 30 Maths/Physics rewritten as equations only; 17 Biology/Chemistry solutions rewritten | Clean after fixes; 3 items flagged |
| 9–25 | — | — | — | — | — | — | Not yet audited |

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

### Test 5 (`IISER/IAT NEW TEST 5.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q5, Q7, Q14, Q18, Q28, Q48, Q55 and Q58 agree with their questions.
- **Replaced for repetition (same key letter):**
  - Q3 peroxisome from catalase in a fraction = Test 2 Q3 → fraction of an unsynchronised culture in S phase.
  - Q19 λ(3→2)/λ(2→1) = 27/5 = Test 2 Q59 exactly → Bohr radius ratio for He⁺ (n = 3) and H (n = 1).
  - Q20 isoelectronic ionic radii = Test 1 Q28 → why chlorine has a more negative electron gain enthalpy than fluorine.
  - Q22 phenoxide resonance and acidity = Test 3 Q25 → IUPAC name of a keto acid.
  - Q57 the same lens-plus-plane-mirror set-up and numbers as Test 2 Q57 → focal length from a threefold real image on a screen 80 cm away.
  - Q60 activities of two isotopes with half-lives 2 h and 4 h = Test 3 Q60 → ratio of nuclear radii from R = R₀A^(1/3).
- **Re-asked on the same figure:** Q58 asked for 'fringe visibility' without defining it → now asks for the amplitude ratio of the two beams from Imax = 9 and Imin = 1 (key letter unchanged).
- **Strengthened one-step 'medium' items:** Q53 (Gauss's law, now with a charge outside the surface), Q56 (mutual induction, rate now found from a current change).
- **Change made in Test 3 because of this test:** Test 3 Q5 (lower pH favours unloading of oxygen) repeated the idea of Test 5 Q5, which carries a figure. Test 3 Q5 was replaced by a question on the regulation of breathing by CO₂ and H⁺.
- **Flagged, left unchanged:** Q14 uses non-competitive inhibition (the NCERT chapter names only competitive inhibition, though the graph description is self-contained); Q12 extends the filtered-load idea of Test 2 Q13 with a marker step. The user should decide whether to keep them.
- Q31–Q60 rewritten as equations only; Q3, Q6, Q12, Q19, Q20, Q21, Q22, Q26, Q27, Q28, Q29, Q30 rewritten in full.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 444 expressions, 0 errors. Source text: `IISER/audit/solutions/test05.txt`.

### Test 6 (`IISER/IAT NEW TEST 6.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q2, Q6, Q17, Q27, Q53 and Q58 agree with their questions.
- **Replaced for repetition (same key letter):**
  - Q9 sticky versus blunt ligation = Test 2 Q9 → why PCR needs a thermostable polymerase.
  - Q14 chromosomes and DNA after S phase = Test 1 Q7 → bivalents and chromatids in meiosis I.
  - Q16 zero dipole of CO₂ = Test 3 Q16 → highest bond order among O₂⁺, O₂, O₂⁻, O₂²⁻.
  - Q19 Tollens test for propanal versus propanone repeated Q23 of the same test → metamers.
  - Q21 SN2 inversion = Test 2 Q21 → Wurtz–Fittig preparation of toluene.
  - Q28 two-step Hess sum = Test 2 Q28 → ΔH − ΔU = Δn(g)RT for ammonia synthesis.
  - Q30 spin-only moment = Test 2 Q30 → which ion is colourless (d¹⁰).
  - Q38 conditional draw from 4 red and 3 blue balls = Test 3 Q38 → conditional probability with two dice.
  - Q39 one forbidden adjacency at a round table = the simpler half of Test 2 Q42 → committee with at least 3 women.
  - Q47 Atwood machine in an accelerating lift = Test 2 Q46 → block on a rough incline.
  - Q54 balanced Wheatstone bridge (a third bridge-ratio item, and labelled hard) → maximum power from a cell with internal resistance.
- **Out of syllabus, replaced:** Q46 percentage uncertainty of a product → dimensional analysis of a drop's oscillation period.
- **Topic mismatch, replaced:** Q51 used a = 2x, which is not simple harmonic motion → speed at a given displacement in SHM.
- **Reworded:** Q37 asked what 'spans its nullspace' → 'which nonzero vector v satisfies Av = 0'; options and key unchanged.
- **Changes made in earlier tests because of this test** (the Test 6 questions carry figures, so the earlier ones were changed): Test 2 Q17 (ionisation isomers by BaCl₂ and AgNO₃ tests) now asks the type of isomerism and the number of ions, on the same figure. Test 3 Q6 (self-incompatibility) is now a question on emasculation and bagging.
- **Flagged, left unchanged:** Q3 (a one-step subtraction labelled medium); Q11 (lac operon without a repressor, close to Test 3 Q12 on an operator mutant); Q27 (initial-rate orders from a figure, the same skill as Test 2 Q27).
- Q31–Q60 rewritten as equations only; Q3, Q9, Q14, Q16, Q18–Q21, Q25, Q27–Q30 rewritten in full.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse, 0 errors. Source text: `IISER/audit/solutions/test06.txt`.

### Test 7 (`IISER/IAT NEW TEST 7.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q2, Q6, Q17, Q20, Q56 and Q58 agree with their questions.
- **Out of syllabus, replaced:** Q45 summed an arithmetic-geometric progression (the syllabus lists only AP, GP and Σn, Σn², Σn³) → 1·2 + 2·3 + … + 10·11 from the special series.
- **Replaced for repetition (same key letter):**
  - Q1 red alga from pigments and floridean starch = Test 3 Q1 → class of fungi from mycelium and spores.
  - Q3 spindle checkpoint = Test 2 Q14 → where 70S ribosomes occur in a plant cell.
  - Q4 light and CO₂ as limiting factors = Test 2 Q4 → why fermentation must regenerate NAD⁺.
  - Q7 carrier chance 2/3 for an unaffected sibling (already used in Test 1 Q13 and Test 4 Q12) → molecular basis of sickle-cell anaemia.
  - Q9 insertional inactivation of a marker = Test 4 Q9 → visualising DNA with ethidium bromide under UV.
  - Q16 carbonate resonance = Test 1 Q16 → intramolecular versus intermolecular hydrogen bonding in nitrophenols.
  - Q23 HBr with and without peroxide = Test 2 Q20 (and close to Q22 of this test) → Friedel–Crafts acylation.
  - Q28 van't Hoff factor from a freezing-point ratio = inverse of Test 6 Q25 → elevation of boiling point.
  - Q31 ellipse eccentricity and directrix = inverse of Test 2 Q32 → distance between parallel lines.
  - Q33 partial fractions on 1/((x+1)(x+2)) = same denominator as Test 4 Q33 → ∫x cos x dx by parts.
  - Q35 tangent to x² + xy + y² = 7 = number-swapped Test 3 Q32 → logarithmic differentiation of x^(sin x).
  - Q40 shortest distance between skew lines = number-swapped Test 2 Q41 → distance of a point from a plane.
- **Changes made in earlier tests because of this test:** Test 3 Q54 (capacitor at fixed voltage) was a subset of Test 7 Q54, which covers both fixed voltage and fixed charge → now a question on equipotential surfaces. Test 4 Q13 (my earlier replacement on oxygen delivery) overlapped Test 7 Q13 → now heart rate from the spacing of QRS complexes.
- **Flagged, left unchanged:** Q5 is filed under Human Physiology but tests allergy (Human Health and Disease); Q26 (sucrose is non-reducing) is close to Test 1 Q29; Q47 gives the lift's acceleration although the answer does not need it.
- Q31–Q60 rewritten as equations only; Q1, Q3, Q4, Q6, Q7, Q9, Q11, Q13, Q15, Q16, Q21, Q23, Q27, Q28, Q29 rewritten in full.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 432 expressions, 0 errors. Source text: `IISER/audit/solutions/test07.txt`.

### Test 8 (`IISER/IAT NEW TEST 8.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q2, Q15, Q17, Q28, Q53 and Q58 agree with their questions.
- **Formatting error fixed:** Q33 option D had an unbalanced bracket, `√2−1)/3`; now (√2−1)/3.
- **Out of syllabus, replaced:** Q60 thin-film reflection → Malus's law with unpolarised light.
- **Replaced or re-asked for repetition (same key letter):**
  - Q2 inferior ovary from a figure = Test 4 Q2 → same figure, now asks which plants show this ovary position.
  - Q5 Bohr shift = Test 5 Q5 → which vessel carries oxygenated blood from the lungs.
  - Q6 ploidy after double fertilisation = the simple case of Test 1 Q8 → meiotic divisions needed for 100 seeds.
  - Q13 filtered load minus excretion = Test 2 Q13 → air reaching the alveoli per minute.
  - Q14 catalase marks peroxisomes = Test 2 Q3 → effect of doubling enzyme at saturating substrate.
  - Q16 σ and π bonds of a nitrile = Test 4 Q16 → axial and equatorial bonds of PCl₅.
  - Q18 formal charge on N in nitrate = Test 4 Q18 exactly → bond order and bond length in CO, CO₂, CO₃²⁻.
  - Q30 Zaitsev product from 2-bromobutane = part of Test 2 Q21 → Finkelstein reaction.
  - Q32 increasing intervals of a cubic = Test 5 Q32 → rate of change of a sphere's volume.
  - Q35 trace of X from AX = B = number-swapped Test 4 Q37 → k in A² − 4A + kI = O.
  - Q38 term independent of x = number-swapped Test 2 Q38 → sum of alternate binomial coefficients.
  - Q51 period ratio of springs in series and parallel = Test 2 Q52 exactly → displacement where kinetic and potential energies are equal.
  - Q54 terminal voltage of a cell = number-swapped Test 3 Q55 → current division in a series–parallel network.
  - Q57 minimum deviation of a prism = inverse of Test 4 Q57 → image in a concave mirror for an object inside the focus.
- **Changes made in earlier tests because of this test:** Test 2 Q2 (inferior ovary, a third copy without a figure) → vexillary aestivation. Test 2 Q55 used the same field graph and asked for V(3a) − V(0), which Test 8 Q53 also asks → now asks where the kinetic energy of a released charge is greatest, on the same figure. Test 3 Q28 (positive deviation from Raoult's law, repeated here with a figure) → Henry's law.
- **Flagged, left unchanged:** Q4 (one subtraction, labelled medium); Q27 (sign of ΔG with temperature, the third question of this kind after Test 1 Q18 and Test 7 Q30); Q44 (mean and variance under Y = aX + b, close to Test 6 Q43).
- Q31–Q60 rewritten as equations only; Q2, Q4–Q7, Q10–Q14, Q16, Q18, Q24, Q25, Q27, Q28, Q30 rewritten in full.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 421 expressions, 0 errors. Source text: `IISER/audit/solutions/test08.txt`.

## Not verified
- Rendered PDF pages were not regenerated or inspected for Test 1 after the edit (the exporter needs Playwright and Chromium).
- Series-wide near-duplicate comparison is done after all 25 tests are read.
