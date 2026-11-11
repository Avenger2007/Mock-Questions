# Blueprint — CUET (UG) 2027 Physics (322)

**Syllabus:** `CUET SYLLABUS/Physics - 322.pdf` (NTA "for the year 2026", latest published), 9 units.
**Series:** 15 tests, `CUET/Physics/CUET PHYSICS TEST 1–15.json`.
**Source for answers:** NCERT Physics Class XII, Parts I and II (rationalised edition). Constants as NCERT: \(k = 9 \times 10^9\) N m² C⁻², \(\mu_0 = 4\pi \times 10^{-7}\) T m A⁻¹, \(e = 1.6 \times 10^{-19}\) C, \(h = 6.6 \times 10^{-34}\) J s (or \(6.63\)), \(c = 3 \times 10^8\) m s⁻¹, \(hc \approx 1240\) eV nm, \(m_e = 9.1 \times 10^{-31}\) kg, 1 u = 931.5 MeV.

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, **all compulsory** (2025 and 2026 papers; the 2024 paper was "answer any 40 of 50") |
| Duration / marking | 60 minutes; +5 / −1 / 0; 4 options, one correct |
| Calculator | not allowed, so numbers must work by hand |
| Order | units are mixed in the test file (`shuffle_test.py`), as in the real paper |

## 2. PYQ analysis (NTA 2024 and 2026 papers; analysed, not stored)

- **Coverage:** every unit appears; Optics, Electrostatics and Magnetism carry the most items, EM waves and Electronic Devices the fewest.
- **Formats (2026, sampled):** about 6–8 match-list items (e.g. field dependence on \(r\) for a point charge, dipole, line charge and sheet; quantity vs formula for emf, field, current density, mobility; hydrogen series vs wave-number expression), about 6 "identify the correct statements" items (Gauss's theorem facts; inductor and capacitor in d.c.), and 3–4 sequence items (work functions in order of threshold wavelength; susceptibility order; shortest wavelengths of hydrogen series). The rest are short numericals and one-line concept questions; a few use a figure.
- **Level:** NCERT level, one or two steps. Typical numericals: potential at the centre of a charged ring, equilibrium charge between two charges, energy after a charged capacitor is joined to an identical one, field at the centre of a 3/4 loop, photons emitted per second by a 66 W source, de Broglie momentum ratio.
- **What this means for OurMocks:** many short numericals with traps in the distractors, plus a steady share (about 30%) of match, statement and sequence items. The old bank had almost none of these and 70% easy items.

## 3. Unit weight per test (50 questions)

| Code | Unit | Qs |
|---|---|---|
| P1 | Electrostatics | 7 |
| P2 | Current Electricity | 6 |
| P3 | Magnetic Effects of Current and Magnetism | 7 |
| P4 | Electromagnetic Induction and Alternating Currents | 6 |
| P5 | Electromagnetic Waves | 3 |
| P6 | Optics | 9 |
| P7 | Dual Nature of Matter and Radiation | 4 |
| P8 | Atoms and Nuclei | 5 |
| P9 | Electronic Devices | 3 |

Quotas are exact in every test (`phy_check.py` flag `QUOTA`).

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.** Tests 11–15 carry the hardest items (see the coverage map §B).

## 5. Formats (every test)

| Format | Per test | Rules |
|---|---|---|
| Match-list | 6 | each in a different unit; List-I (A)–(D), List-II (I)–(IV); the six correct patterns all differ |
| Statements | 6 | "Which of the statements given above are correct?" and "…is/are NOT correct?" alternate in file order; vary which statement is false |
| Sequence | 3 | arrange (A)–(D) in an order; the answer is never (A), (B), (C), (D) |
| Numerical | at least 20 | step-by-step working |
| Direct | the rest | one-line concept questions |

**Answer key:** 13 / 12 / 13 / 12 (odd tests) and 12 / 13 / 12 / 13 (even tests); no letter more than 3 times in a row after shuffling.

## 6. Option quality

- Distractors come from real mistakes: a wrong power of 10, a missing factor of 2 or \(\pi\), the series/parallel swap, the sign convention, a reciprocal.
- The correct option is never clearly the longest (`LONGEST`).
- Units are written in every numerical option.

## 7. Explanations

- **Numerical:** Given / Formula / Step 1, 2, … / Common mistake (which option a slip leads to) / Key point.
- **Concept, match, statements, sequence:** Why / Why not the others / Key point (or Steps for match and sequence).
- Mathematics in KaTeX `\( … \)`.

## 8. Out of scope — never test

These are in older NCERT editions or other exams but **not** in the 2026 syllabus:

- Radioactivity: decay law, half-life, mean life, α/β/γ decay equations.
- Transistors, logic gates, Zener diode, LED, photodiode, solar cell, special-purpose diodes.
- Communication systems.
- Polarisation, Malus's law, Brewster's law; resolving power; Doppler effect in light.
- Earth's magnetism (dip, declination); hysteresis loops; Gauss's law for magnetism; cyclotron.
- Potentiometer and metre bridge (Wheatstone bridge stays); RC circuits and LC oscillations; eddy currents; energy stored in an inductor.
- Davisson–Germer experiment.
- Hydrogen spectra beyond a qualitative treatment and the simple series expressions (no long Rydberg calculations).
