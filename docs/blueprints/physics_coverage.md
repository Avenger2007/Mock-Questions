# Coverage map — CUET (UG) 2027 Physics (322), Tests 1–15

This map was written **before** any test, so that repeats are prevented rather than fixed.

- Every test covers all nine units in the quotas of the blueprint (§3).
- Each item carries short **skill keys** (for example `capacitor energy sharing`, `lens maker biconvex`). A key may be used **at most twice in the series**, in different tests and with different numbers or a different angle. `phy_check.py` flags a third use (`REPEAT-TARGET`); `phy_ship.sh` adds a shipped test's keys to §C.
- `phy_check.py` also compares every stem and sub-topic with all earlier revised tests (`OVERLAP`). A flagged item is rewritten unless only the template is shared.

## A. Format hosts per test

Six match-list items, each in a different unit; six statement items (file order alternates "correct" / "NOT correct"); three sequence items.

| Test | Match-list units | Statement units | Sequence units |
|---|---|---|---|
| 1 | P2, P3, P5, P6, P8, P9 | P1, P3, P4, P6, P7, P9 | P3, P6, P9 |
| 2 | P1, P3, P4, P6, P7, P9 | P1, P2, P4, P5, P7, P8 | P1, P4, P7 |
| 3 | P1, P2, P4, P5, P7, P8 | P2, P3, P5, P6, P8, P9 | P2, P5, P8 |
| 4 | P2, P3, P5, P6, P8, P9 | P1, P3, P4, P6, P7, P9 | P3, P6, P9 |
| 5 | P1, P3, P4, P6, P7, P9 | P1, P2, P4, P5, P7, P8 | P1, P4, P7 |
| 6 | P1, P2, P4, P5, P7, P8 | P2, P3, P5, P6, P8, P9 | P2, P5, P8 |
| 7 | P2, P3, P5, P6, P8, P9 | P1, P3, P4, P6, P7, P9 | P3, P6, P9 |
| 8 | P1, P3, P4, P6, P7, P9 | P1, P2, P4, P5, P7, P8 | P1, P4, P7 |
| 9 | P1, P2, P4, P5, P7, P8 | P2, P3, P5, P6, P8, P9 | P2, P5, P8 |
| 10 | P2, P3, P5, P6, P8, P9 | P1, P3, P4, P6, P7, P9 | P3, P6, P9 |
| 11 | P1, P3, P4, P6, P7, P9 | P1, P2, P4, P5, P7, P8 | P1, P4, P7 |
| 12 | P1, P2, P4, P5, P7, P8 | P2, P3, P5, P6, P8, P9 | P2, P5, P8 |
| 13 | P2, P3, P5, P6, P8, P9 | P1, P3, P4, P6, P7, P9 | P3, P6, P9 |
| 14 | P1, P3, P4, P6, P7, P9 | P1, P2, P4, P5, P7, P8 | P1, P4, P7 |
| 15 | P1, P2, P4, P5, P7, P8 | P2, P3, P5, P6, P8, P9 | P2, P5, P8 |

## B. Depth focus

| Tests | Level |
|---|---|
| 1–5 | NCERT exercise level: one formula or one idea per item, with clean numbers |
| 6–10 | two-step items: combine two results (e.g. capacitor sharing then energy, lens then mirror) |
| 11–15 | hardest: multi-concept items, ratios and limiting cases, graph and data reading, still solvable without a calculator |

## C. Ledgers (filled as tests are shipped)

### P1 Electrostatics

| Test | Skill keys |
|---|---|
| T1 | conductor field zero, equipotential perpendicular, coulomb force two charges, null point two like charges, dielectric battery connected charge, capacitor sharing energy loss, dipole torque uniform field, shell field inside gauss |

### P2 Current Electricity

| Test | Skill keys |
|---|---|
| T1 | parallel series resistance, stretched wire resistance, internal resistance terminal voltage, drift velocity copper wire, wheatstone balance fourth arm, cells parallel equivalent emf, bulb rating resistance, semiconductor resistivity temperature |

### P3 Magnetic Effects of Current and Magnetism

| Test | Skill keys |
|---|---|
| T1 | field loop wire solenoid formulas, magnetic materials properties, field magnitudes order wire loop solenoid, force on current wire angle, galvanometer to ammeter shunt, force parallel wires per metre, charged particle circle radius |

### P4 Electromagnetic Induction and Alternating Currents

| Test | Skill keys |
|---|---|
| T1 | lenz energy conservation, pure inductor phase, capacitor average power, rms from peak voltage, faraday emf flux change turns, lcr impedance power factor, transformer turns ratio voltage, inductance si unit henry |

### P5 Electromagnetic Waves

| Test | Skill keys |
|---|---|
| T1 | em spectrum uses, displacement current capacitor, em wave b0 from e0 |

### P6 Optics

| Test | Skill keys |
|---|---|
| T1 | lens power convex, telescope magnifying power, fringe width ydse, critical angle n two, single slit width central maximum, huygens secondary wavelets, prism dispersion deviation colours, concave mirror image position, lens maker equiconvex, lenses in contact combination, ydse bright dark fringe gap, compound microscope magnifying power, prism minimum deviation index |

### P7 Dual Nature of Matter and Radiation

| Test | Skill keys |
|---|---|
| T1 | photoelectric observations intensity frequency, photon energy wavelength ev, einstein equation stopping potential, de broglie electron accelerated |

### P8 Atoms and Nuclei

| Test | Skill keys |
|---|---|
| T1 | isotopes isobars isotones, nuclear force short range, bohr energy level n two, nuclear radius mass number ratio, binding energy per nucleon helium, rutherford scattering empty space |

### P9 Electronic Devices

| Test | Skill keys |
|---|---|
| T1 | intrinsic extrinsic semiconductor doping, band gap insulator, depletion layer bias, reverse bias current, full wave ripple frequency, band gap order ge si diamond |
