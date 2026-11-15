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
| 9 | pass | fail → fixed: Q49 (Poisson's ratio) is not in the 2026 syllabus, replaced | minor: Q56 was one step, replaced | fail → fixed: 20 questions repeated earlier tests, replaced | 0 of 60 | 30 Maths/Physics rewritten as equations only; 18 Biology/Chemistry solutions rewritten | Clean after fixes; 5 items flagged |
| 10 | pass | pass | minor: Q48 was one step, extended to include the energy change; Q36, Q40, Q47, Q51, Q56 are one-step items (see flags) | fail → fixed: 17 questions repeated earlier tests or this test, replaced | 0 of 60 | 30 Maths/Physics rewritten as equations only; 24 Biology/Chemistry solutions rewritten | Clean after fixes; 5 items flagged |
| 11 | pass | fail → fixed: Q4 (transpiration) and Q15 (interfascicular cambium, secondary growth) are not in the current NCERT text, replaced | minor: Q13, Q46 and Q60 were one step, replaced | fail → fixed: 19 questions repeated earlier tests or this test, replaced | 0 of 60 | all 60 rewritten (30 Maths/Physics as equations only) | Clean after fixes; 8 items flagged |
| 12 | pass | pass | minor: Q48 and Q59 were one step, replaced | fail → fixed: 16 questions repeated earlier tests, replaced | 0 of 60 | all 60 rewritten (30 Maths/Physics as equations only) | Clean after fixes; 8 items flagged |
| 13 | pass | pass | minor: Q56 was one step, replaced; Q29 is one step, kept | fail → fixed: 12 questions repeated earlier tests, replaced | 0 of 60 | all 60 rewritten (30 Maths/Physics as equations only) | Clean after fixes; 10 items flagged |
| 14 | pass | pass | minor: Q43, Q46, Q52 and Q56 were one step, replaced | fail → fixed: 18 questions repeated earlier tests, replaced | 0 of 60 | all 60 rewritten (30 Maths/Physics as equations only) | Clean after fixes; 8 items flagged |
| 15 | pass | fail → fixed: Q47 (propagation of percentage errors) is not in the syllabus, replaced | minor: Q54 and Q58 were one step, replaced | fail → fixed: 13 questions repeated earlier tests, replaced | 0 of 60 | all 60 rewritten (30 Maths/Physics as equations only) | Clean after fixes; 11 items flagged |
| 16 | pass | fail → fixed: Q15 (secondary xylem and phloem from the cambium) is not in the current NCERT text, replaced | pass (harder than Tests 1–15, close to the real paper's upper range) | pass: no repeat of Tests 1–15 except Q29, fixed in Test 8 | 0 of 60 | 30 Maths/Physics rewritten as equations only; Biology/Chemistry solutions were already complete and are kept | Clean after fixes; 4 items flagged |
| 17–25 | — | — | — | — | — | — | Not yet audited |

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

### Test 9 (`IISER/IAT NEW TEST 9.json`)
- All 60 answers re-derived; no key was wrong. Figure specifications for Q3, Q4, Q17, Q27, Q46, Q51, Q53 and Q59 agree with their questions.
- **Out of syllabus, replaced:** Q49 Poisson's ratio (removed from the NCERT chapter and not in the syllabus list) → fractional volume change from the bulk modulus.
- **Replaced for repetition (same key letter).** This test repeated more earlier questions than any other so far:
  - Biology: Q6 (ovule → seed, ovary → fruit = Test 4 Q6) → hCG and the corpus luteum; Q7 (X-linked father = Test 5 Q11) → ABO groups from AB × O; Q9 (ampicillin/tetracycline selection = Test 4 Q9) → RNA interference against Meloidogyne; Q11 (leading strand direction = Test 6 Q7) → Hershey–Chase experiment; Q12 (constitutive lac expression = Test 3 Q12 and Test 6 Q11) → 61 sense codons and AUG; Q13 (thyroxine–TSH feedback = Test 6 Q5) → growth hormone and dwarfism; Q15 (species–area exponent = inverse of Test 4 Q15) → dN/dt from birth and death rates.
  - Chemistry: Q16 (lone pairs compress the angle = Test 2 Q16) → hybridisation in C₂H₂, C₂H₄, C₂H₆; Q19 (656 nm line, the sixth hydrogen-transition item in nine tests) → orbitals in the n = 3 shell; Q20 (N versus O ionisation = Test 3 Q19) → second ionisation enthalpy of sodium; Q22 (p-nitro versus p-methoxy benzoic acid = Test 3 Q22) → steam distillation of aniline; Q25 (Hinsberg test = mirror of Test 4 Q22) → limits of the Gabriel synthesis; Q26 (amino acid above its pI = Test 3 Q26) → scurvy and vitamin C; Q28 (concentration cell = number-swapped Test 2 Q26) → Kohlrausch's law; Q30 (Q < K goes forward = mirror of Test 5 Q30) → Le Chatelier's principle for ammonia.
  - Mathematics: Q32 (lattice paths avoiding a point = number-swapped Test 3 Q39) → four-digit even numbers with distinct digits; Q33 (domain of a composition, third of its kind) → number of one-one functions; Q40 (Bayes with two urns, third of its kind and the same P(R) = 7/18 as Test 5 Q36) → exactly two sixes in three rolls; Q43 (both roots in (0,3) = the interval of Test 7 Q43) → α⁵ + β⁵ from a recurrence.
  - Physics: Q56 (6 Ω ∥ 6 Ω + 2 Ω, one step) → resistance of a wire stretched to double length; Q57 (lens and plane mirror = Test 2 Q57 exactly) → critical angle.
- **Changes made in earlier tests because of this test:** Test 2 Q54 (v × B for the same vectors that Test 9 Q54 uses in a velocity selector) → radius of path of a proton and an alpha particle. Test 6 Q30 (my earlier replacement on a colourless d¹⁰ ion, too close to Test 9 Q18 on d⁰) → general configuration of the d-block. Test 7 Q33 (my earlier ∫x cos x dx, too close to Test 9 Q35) → ∫tan²x dx. Test 8 Q51 (my earlier K = U question, too close to Test 9 Q52) → maximum acceleration in SHM.
- **Flagged, left unchanged:** Q3 (competitive inhibition from a figure, third appearance after Test 1 Q3 and Test 5 Q14); Q5 (presynaptic defect, the mirror of Test 3 Q13); Q8 (names p53, which the NCERT text does not); Q14 (uses the word 'translocation' for a step of translation); Q31 (determinant of an adjugate, close to Test 7 Q37). Also noted for the user: Test 2 Q49 and Test 6 Q48 use elastic strain energy, which was removed from the NCERT chapter together with Poisson's ratio; they were left in place because they can be read off the stress–strain curve.
- Q31–Q60 rewritten as equations only; 18 Biology/Chemistry solutions rewritten in full.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 418 expressions, 0 errors. Source text: `IISER/audit/solutions/test09.txt`.

### Test 10 (`IISER/IAT NEW TEST 10.json`)
- All 60 answers re-derived; no key was wrong. The figures for Q18, Q52, Q53 and Q58 were opened and agree with the questions and solutions; those for Q2, Q3, Q9 and Q23 were checked only against the question text.
- **Formatting fixed:** Q34, the integrand is now typeset as a fraction (it was written on one line and could be misread).
- **Replaced for repetition (same key letter):**
  - Biology: Q1 (exposed ovules of a gymnosperm = Test 2 Q1 and Test 4 Q1) → Annelida from its body plan; Q4 (respiratory quotient = Test 4 Q4) → source of the O₂ released in photosynthesis; Q8 (= Test 4 Q8) → passive immunity from colostrum; Q10 (equal richness, unequal biodiversity value = Test 5 Q10) → age pyramid of an expanding population; Q11 (silent mutation = Test 6 Q12) → trisomy 21 from a karyotype; Q12 (booster dose and memory cells = Test 2 Q8) → ADH deficiency; Q13 (third cardiac-output calculation) → oxygen-carrying capacity of blood; Q14 (repeated Q3 of this test and Test 1 Q7) → length, turns and nucleotides of a 1000 bp DNA; Q15 (corpus luteum as the source of progesterone = Test 5 Q15) → Leydig cells and LH.
  - Chemistry: Q16 (third zero-dipole item) → coordinate bond in NH₄⁺; Q17 (chelate effect = Test 5 Q17) → IUPAC name of [Cr(H₂O)₄Cl₂]Cl; Q19 (two successive percentage yields = Test 3 Q21) → limiting reagent and excess reagent; Q20 (one-step Faraday calculation, part of Test 5 Q28) → ΔG° = −nFE° for an Fe–Ag cell; Q21 (= Test 5 Q25) → basic strength of methylamines in water; Q24 (= Test 5 Q23) → decarboxylation with soda lime; Q27 (empirical formula CH₂O = Test 6 Q20) → volume of NaOH for a diprotic acid; Q30 (buffer after adding acid = Test 6 Q29) → K_c for H₂ + I₂ ⇌ 2HI.
  - Physics: Q48 (angular speed when I becomes I/4, one step) → same situation, now also asks for the change in rotational kinetic energy.
- **Changes made in earlier tests because of this test:** Test 4 Q1 (exposed ovules, the same question as Test 2 Q1) → heterocysts of Nostoc and Anabaena. Test 5 Q20 (my earlier replacement on the electron gain enthalpy of F and Cl, the same point as Test 10 Q28) → amphoteric Al₂O₃. Test 8 Q57 (my earlier replacement on a concave mirror with the object inside the focus, the same as the figure question Test 10 Q58) → image in a convex mirror.
- **Flagged, left unchanged:** Q3 (chromosome and DNA content from a figure, close to Test 1 Q7); Q33 (f(x) = x³ − 3x, used for the fourth time after Test 5 Q32, Test 6 Q33 and Test 7 Q36, though the question asked is different each time); Q41 (line–plane angle with direction (1, 2, 2), as in Test 5 Q42); Q53 (figure with +q and −4q, the same layout as Test 3 Q53, which asks for the zero of potential instead of field). In the Q58 figure the labels 'F: 10 cm' and 'object: 5 cm' touch each other; the figure is readable but should be redrawn. Q36, Q40, Q47, Q51 and Q56 are one-step questions; they are kept because a real paper also has a few direct items.
- Q31–Q60 rewritten as equations only; 24 Biology/Chemistry solutions rewritten in full. Six conceptual solutions (Q2, Q3, Q9, Q23, Q25, Q28) already met the format and were left as they were.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 433 expressions, 0 errors. Source text: `IISER/audit/solutions/test10.txt`.

### Test 11 (`IISER/IAT NEW TEST 11.json`)
- All 60 answers re-derived; no key was wrong. The figures for Q2, Q17, Q28, Q49, Q57 and Q58 were opened and agree with the questions and solutions; those for Q1, Q8, Q9, Q22, Q52 and Q59 were checked only against the question text.
- **Out of syllabus, replaced:** Q4 (transpiration and the water-vapour gradient; Transport in Plants is not in the syllabus) → ethylene and fruit ripening; Q15 (interfascicular cambium; secondary growth was removed from the NCERT chapter, and the item also repeated Test 6 Q15) → sieve tube elements and companion cells.
- **Replaced for repetition (same key letter):**
  - Biology: Q6 (self-incompatibility = Test 6 Q6) → cleistogamous flowers; Q11 (selection for pesticide resistance = Test 4 Q7) → homologous organs; Q12 (third dihybrid test cross after Test 4 Q11 and Test 8 Q7) → incomplete dominance in snapdragon; Q13 (filtered minus excreted, one subtraction; third clearance item) → percentage of filtrate reabsorbed per day; Q14 (Na⁺–glucose co-transport = Test 3 Q3) → zinc as an enzyme cofactor.
  - Chemistry: Q16 (valid resonance form of carbonate = Test 1 Q16) → covalent character of LiCl; Q18 (lanthanoid contraction = Test 5 Q18) → oxidation states of actinoids; Q19 (smallest isoelectronic ion = Test 1 Q28) → diagonal relationship of Li and Mg; Q20 (Balmer series limit, one more hydrogen-level item) → energy of a mole of photons; Q24 (bromobenzene and S_N2 = Test 3 Q24) → Saytzeff elimination from 2-bromobutane; Q25 (anisole + HI = Test 5 Q24) → Reimer–Tiemann reaction; Q26 (sucrose before and after hydrolysis = Test 7 Q26) → denaturation of proteins; Q27 (K_a from the same numbers that Test 7 Q27 uses for pH) → pH of Ba(OH)₂; Q29 (electrolysis of CuSO₄ = Test 3 Q29) → molar conductivity from conductivity.
  - Mathematics: Q43 (coplanar vectors = number-swapped Test 6 Q36) → direction cosines; Q44 (mean deviation with frequencies 1, 2, 1 = number-swapped Test 5 Q44) → variance of the first n even numbers.
  - Physics: Q46 (normal force in a lift, one step; = Test 5 Q47) → contact force between two blocks; Q54 (energy of a magnetic dipole, the same idea as Q55 of this test) → radius and period of a proton in a magnetic field; Q56 (Wheatstone bridge with the same arms 2, 3, 4 Ω as Test 2 Q56) → same question with arms 10, 15, 20 and 25 Ω, answer unchanged; Q60 (rotating rod, one step; = Test 6 Q55) → charge that flows when the flux through a coil changes.
- **Flagged, left unchanged:** Q1 (figure; seed inside a fruit wall, the reverse of Test 2 Q1); Q2 (figure; dicot root from a four-armed xylem star, the same identification as Test 6 Q2 and Test 16 Q2); Q17 (figure; ionisation isomers, the same idea as Test 6 Q17, though that one infers the formula from the tests); Q33 (third area-between-two-parabolas item after Test 2 Q34 and Test 4 Q34); Q36 (uses P(A) = 1/2, P(B) = 1/3 like Test 7 Q38, but for independent events); Q42 (skew-line distance, same method as Test 2 Q41); Q50 (ice and water, same data type as Test 2 Q50 but only part of the ice melts); Q53 (C and 2C in series with a dielectric, the battery-connected version of Test 2 Q53).
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 414 expressions, 0 errors. Source text: `IISER/audit/solutions/test11.txt`.

### Test 12 (`IISER/IAT NEW TEST 12.json`)
- All 60 answers re-derived; no key was wrong. The eleven figure questions (Q1, Q2, Q4, Q9, Q16, Q17, Q21, Q28, Q46, Q53, Q58) state their data in the question text; the figures themselves were not opened.
- **Replaced for repetition (same key letter):**
  - Biology: Q7 (carrier risk of an unaffected sibling, third use after Test 1 Q13 and Test 4 Q12) → exactly one affected child out of three; Q8 (antibiotic selects pre-existing resistance = Test 4 Q7) → Miller's experiment; Q10 (competition for one limiting resource = Test 7 Q10) → predator removal and loss of diversity; Q12 (X-linked father, all daughters carriers = Test 5 Q11) → pleiotropy; Q13 (thyroxine–TSH feedback = Test 6 Q5) → melatonin; Q14 (competitive inhibition, fourth use after Test 1 Q3, Test 5 Q14 and Test 9 Q3) → classes of enzymes; Q15 (limiting factors of photosynthesis = Test 2 Q4) → cytokinin and leaf senescence.
  - Chemistry: Q19 (valid quantum-number set = Test 7 Q20) → configuration of chromium; Q20 (resonance-stabilised carbocation = Test 8 Q20) → identifying an electrophile; Q23 (hydrolysis of Gly–Ala–Gly = Test 8 Q23) → sugar of DNA and RNA; Q24 (rate law from three trials, third use after Test 2 Q27 and Test 6 Q27) → rates of formation from stoichiometry; Q26 (five electrons for MnO₄⁻, already used in Test 7 Q18 and Test 10 Q22) → oxidation numbers of oxygen.
  - Mathematics: Q33 (congruence modulo 4 = Test 4 Q36) → number of equivalence relations on a three-element set; Q45 (used the same two vectors as Test 10 Q41) → same question with new vectors, answer unchanged.
  - Physics: Q48 (α₁/α₂ for the same torque, one step; = Test 5 Q49) → angular acceleration of a pivoted rod; Q52 (period at 4r = Test 7 Q50 exactly) → speeds at perihelion and aphelion; Q55 (terminal voltage = number-swapped Test 3 Q55) → two bulbs in series; Q59 (f = c/λ, one step) → binding energy per nucleon from the mass defect.
- **Change made in an earlier test because of this test:** Test 4 Q9 (ampR/tetR insertional inactivation, the same as the figure question Test 12 Q9) → Ti plasmid of Agrobacterium.
- **Flagged, left unchanged:** Q4 (figure; ATP from an imposed pH gradient, close to Test 1 Q9); Q5 (postsynaptic receptor block, close to Test 3 Q13 and Test 9 Q5); Q11 (intercross of linked heterozygotes, same method as Test 1 Q4 with different numbers and a different class asked for); Q16 (figure; hybridisation of a nitrile carbon, near Test 4 Q16); Q18 (nitrate formal charge, extends Test 4 Q18); Q21 (figure; Tollens and iodoform, third use after Test 1 Q19 and Test 6 Q23); Q37 (another x³ − 3ax function); Q57 (width of the resonance curve, which the NCERT text treats only briefly).
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 408 expressions, 0 errors. Source text: `IISER/audit/solutions/test12.txt`.

### Test 13 (`IISER/IAT NEW TEST 13.json`)
- All 60 answers re-derived; no key was wrong. The ten figure questions (Q1, Q2, Q9, Q15, Q16, Q30, Q53, Q54, Q55, Q60) state their data in the question text; the figures themselves were not opened.
- **Replaced for repetition (same key letter):**
  - Biology: Q6 (embryo 2n and endosperm 3n, the plain form of Test 1 Q8) → cells of the pollen grain at shedding; Q7 (leading strand direction = Test 6 Q7) → what accumulates without DNA ligase; Q10 (NPP = GPP − R = Test 8 Q10) → population size from births, deaths and migration; Q11 (operator mutation gives constitutive expression = Test 3 Q12 and Test 6 Q11) → codon–anticodon pairing; Q14 (chromosome number and DNA content at metaphase = Test 1 Q7 and Test 10 Q3) → DNA content in G₂ and in a gamete.
  - Chemistry: Q17 (low-spin d⁶ has no unpaired electrons = Test 3 Q17) → coordination number and oxidation state in [Co(en)₃]³⁺; Q23 (cyanide bonds through carbon = Test 11 Q22) → aldehydes versus ketones in nucleophilic addition; Q26 (zwitterion at the isoelectric point = Test 3 Q26) → starch and cellulose; Q28 (κ falls and Λm rises on dilution = Test 6 Q26) → lead storage battery.
  - Mathematics: Q35 (domain of g∘f, third use after Test 3 Q35 and Test 5 Q34) → f(f(x)) for a fractional linear function; Q41 (foot of the perpendicular on 3x + 4y − 10 = 0, the same line as Test 9 Q36) → line through a point perpendicular to a given line.
  - Physics: Q52 (pulse inverted at a denser string = Test 6 Q52) → resonant frequencies of a closed pipe; Q56 (Z from R, X_L, X_C in one step; = Test 6 Q56) → resonant angular frequency.
- **Flagged, left unchanged:** Q2 (figure; hypogynous flower, same idea as Test 4 Q2 and Test 9 Q2); Q13 (primary versus secondary thyroid failure, extends Test 6 Q5); Q15 (figure; 900 bp cut into 600 + 300 bp, the same fragment sizes as Test 1 Q11); Q20 (Be > B and N > O, overlaps Test 3 Q19); Q27 (positive deviation, near the figure question Test 9 Q27); Q29 (three half-lives, one step); Q34 (integration by parts, same method as Test 9 Q35); Q36 (determinant after row operations, near Test 9 Q31); Q42 (lattice paths through marked points, same method as Test 3 Q39); Q58 (defines and uses fringe visibility, a term the NCERT text does not use; the formula is given in the question).
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 384 expressions, 0 errors. Source text: `IISER/audit/solutions/test13.txt`.

### Test 14 (`IISER/IAT NEW TEST 14.json`)
- All 60 answers re-derived; no key was wrong. The figure questions (Q2, Q10, Q16, Q20, Q27, Q48, Q51, Q53, Q57) state their data in the question text; the figures themselves were not opened.
- **Replaced for repetition (same key letter):**
  - Biology: Q1 (moss sporophyte depends on the gametophyte = Test 8 Q1) → gemmae of Marchantia; Q3 (spindle poison stops the cell at metaphase = Test 2 Q14) → the G₀ stage; Q6 (integuments → seed coat, ovary wall → fruit wall = Test 4 Q6) → false fruits; Q7 (genotype of an unaffected child of two carriers, the idea of Test 1 Q13) → polygenic inheritance; Q12 (pesticide resistance and selection = Test 4 Q7) → founder effect; Q13 (low pH shifts the O₂ curve to the right = Test 11 Q5) → direction of gas exchange from partial pressures; Q14 (glycosidic bond = Test 11 Q3) → most abundant proteins.
  - Chemistry: Q18 (ΔH < 0, ΔS < 0, the number-swapped Test 8 Q27, and the fourth item of this kind) → standard enthalpy of formation of diamond; Q19 (which compound gives self-aldol = Test 9 Q23) → strongest acid among four; Q24 (hydrolysis of ethanoyl chloride = Test 4 Q21) → esterification; Q25 (functional isomers = Test 10 Q25) → position isomers; Q29 (A = T and G = C counting, third use after Test 5 Q26 and Test 10 Q29) → fibrous and globular proteins; Q30 (buffer after adding base = Test 6 Q29) → pH of 10⁻⁸ M HCl.
  - Mathematics: Q32 (maximum of x³ − 3x + 1, the sixth use of this cubic) → maximum of x⁴ − 2x² on the same interval; Q43 (variance under 2x + 5, one step; = Test 6 Q43 and Test 8 Q44) → number removed from a mean; Q44 (differential equation of y = Cx² = Test 10 Q44) → integrating factor.
  - Physics: Q46 (time to the top for 20 m s⁻¹, one step; = Test 7 Q46) → distance fallen in the third second; Q47 (tension in a lift, third lift item) → time to slide down a smooth incline; Q50 (escape speed ratio, third use after Test 2 Q48 and Test 9 Q48) → height at which g falls to a quarter; Q52 (ΔU = Q − W, one step; = Test 7 Q52) → first law with W = pΔV; Q54 (dielectric in an isolated capacitor = Test 9 Q53) → capacitance when area, separation and dielectric all change; Q56 (½LI², one step) → peak emf of a generator.
- **Change made in an earlier test because of this review:** Test 12 Q27 (ΔH > 0 and ΔS > 0, which I had only flagged, is the same question as Test 7 Q30) → sign of the entropy change.
- **Flagged, left unchanged:** Q2 (figure; floral formula, fourth floral-position item after Tests 4, 9 and 13); Q4 (C₄ plants avoid photorespiration, fourth C₃/C₄ item); Q9 (control for insertional inactivation, related to Test 12 Q9); Q15 (species–area relation, extends Test 4 Q15); Q16 (figure; zero dipole of CO₂ = Test 3 Q16); Q34 (repeated-factor partial fractions, same method as Test 10 Q34); Q49 (rotational fraction for a rolling disc, near Test 7 Q49); Q45 and Q58 are short but not repeats.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 0 errors. Source text: `IISER/audit/solutions/test14.txt`.

### Test 15 (`IISER/IAT NEW TEST 15.json`)
- All 60 answers re-derived; no key was wrong. The figure questions (Q2, Q4, Q17, Q24, Q27, Q48, Q57, Q60) state their data in the question text; the figures themselves were not opened.
- **Out of syllabus, replaced:** Q47 (maximum percentage error of a product) → dimensional analysis of the period of a pendulum.
- **Replaced for repetition (same key letter):**
  - Biology: Q5 (fraction of filtered load reabsorbed, fourth clearance calculation) → pulse pressure; Q15 (regression of the corpus luteum starts menstruation = Test 5 Q15) → site of fertilisation and stage at implantation.
  - Chemistry: Q16 (octet-respecting form of carbonate = Test 1 Q16) → odd-electron molecules; Q18 (1/λ for the 3 → 2 line, one more hydrogen-level item) → capacity of the 4d subshell; Q20 (Markovnikov addition of HBr to propene = Test 2 Q20 and Test 7 Q22) → Baeyer's test; Q21 (S_N1 rate depends only on the substrate = Test 4 Q30) → Grignard reagents and moisture; Q26 (anode of a concentration cell = Test 2 Q26) → electrolysis of molten NaCl; Q29 (degree of ionisation with the same K_a and concentration as Test 7 Q27) → pH after partial neutralisation; Q30 (permanganate in acid and in base = Test 7 Q18) → why transition metals are catalysts.
  - Mathematics: Q37 (det(adj A), third adjoint item after Test 7 Q37 and Test 11 Q35) → determinant of a 3 × 3 skew-symmetric matrix; Q38 (mutually exclusive events cannot be independent = Test 7 Q38) → P(king or heart).
  - Physics: Q49 (disc with a concentric hole = Test 8 Q49 exactly) → parallel-axis theorem for a disc; Q53 (energy of a dipole turned through 90°, fourth dipole item) → potential and field at the centre of a charged shell; Q54 (J = I/A, one step) → two cells in series with internal resistance; Q58 (tan φ = X/R, one step) → phase and power in a capacitive circuit.
- **Flagged, left unchanged:** Q2 (figure; frog heart, as in Test 10 Q2); Q4 (figure; Kranz anatomy = Test 9 Q4); Q8 (lost DNA-damage checkpoint, near Test 9 Q8); Q11 (carrier mother, one more X-linked risk item); Q25 (van 't Hoff factor in one step); Q27 (figure; activation energies from two Arrhenius slopes, the number-swapped Test 4 Q24); Q32 (ellipse from foci and directrices, as in Test 2 Q32); Q33 (area under a parabola, fourth area item); Q36 (surjective but not injective, same classification as Test 11 Q34); Q51 (springs in parallel, near Test 2 Q52); Q57 (figure; total internal reflection at 50°, near Test 7 Q57).
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 0 errors. Source text: `IISER/audit/solutions/test15.txt`.

### Test 16 (`IISER/IAT NEW TEST 16.json`)
- All 60 answers re-derived; no key was wrong. This test is written at a higher level than Tests 1–15 and repeats almost nothing from them. The figure questions state their data in the question text; the figures themselves were not opened.
- **Out of syllabus, replaced:** Q15 (direction of secondary xylem and phloem; secondary growth was removed from the NCERT chapter) → living and dead elements of xylem.
- **Change made in an earlier test because of this test:** Test 8 Q29 (cyclohexene from its ozonolysis product, the same as the figure question Test 16 Q29) → Kolbe's electrolytic method.
- **Flagged, left unchanged:** Q2 (figure; root and stem bundles, the third such figure after Test 6 Q2 and Test 11 Q2, and one option mentions secondary xylem); Q4 (respiratory quotient of fermentation, which the NCERT text does not discuss); Q16 (figure; σ and π bond count, a longer version of Test 4 Q16); Q22 (Hinsberg test for three amines, extends Test 4 Q22).
- Q31–Q60 rewritten as equations only. The Biology and Chemistry solutions already give the concept, the reasoning and a reason against each wrong option, so only Q15 was rewritten.
- Checks: `validate_iat.py` 0 errors, 15/15/15/15, 9/42/9; KaTeX parse 0 errors. Source text: `IISER/audit/solutions/test16.txt`.

## Not verified
- Rendered PDF pages were not regenerated or inspected for Test 1 after the edit (the exporter needs Playwright and Chromium).
- Series-wide near-duplicate comparison is done after all 25 tests are read.
