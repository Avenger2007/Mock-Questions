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
| T2 | potential dipole distance dependence, potential inside conductor constant, capacitance independent of charge, series same charge parallel same voltage, capacitance arrangements order, work done charge potential difference, mixed capacitor grouping, dielectric isolated capacitor energy, conservative field no closed loops |
| T3 | parallel plate capacitance formula, energy density field, field near conductor sheet, potential centre square charges, field from force on charge, dipole axial field value, gauss flux net charge, dielectric slab partial thickness, potential energy like charges closer |
| T4 | charge quantised conserved additive, excess electrons from charge, field midpoint unlike charges, potential energy three charges triangle, parallel plate capacitance value, series capacitors voltage division, closed path work electrostatic |
| T5 | electrostatic quantities si units, field lines properties, capacitor stored energy order, dipole moment value, charge from field and potential, uniform field potential difference angle, force near charged sheet |

### P2 Current Electricity

| Test | Skill keys |
|---|---|
| T1 | parallel series resistance, stretched wire resistance, internal resistance terminal voltage, drift velocity copper wire, wheatstone balance fourth arm, cells parallel equivalent emf, bulb rating resistance, semiconductor resistivity temperature |
| T2 | kirchhoff rules conservation, resistivity length independent, temperature coefficient resistance, joule heating time, cells in series internal resistance, balanced bridge equivalent resistance, mobility si unit |
| T3 | current density sigma e, drift velocity tau, resistivity relaxation time, series same current parallel less, terminal voltage emf, ohm law diode, wire dimensions resistance order, bulbs series power total, emf internal resistance two readings, resistivity from resistance dimensions |
| T4 | three identical resistor combinations, junction rule unknown current, current density value, kirchhoff two battery network, electrical energy cost kwh, drift velocity length fixed voltage |
| T5 | current scalar, manganin resistivity temperature, drift opposite field, four resistor network equivalent, terminal voltage discharge, battery charging terminal voltage, resistance ratio length diameter, parallel resistor power |

### P3 Magnetic Effects of Current and Magnetism

| Test | Skill keys |
|---|---|
| T1 | field loop wire solenoid formulas, magnetic materials properties, field magnitudes order wire loop solenoid, force on current wire angle, galvanometer to ammeter shunt, force parallel wires per metre, charged particle circle radius |
| T2 | magnetic quantities si units, semicircle field centre, coil magnetic moment, coil torque plane angle, galvanometer to voltmeter series, force charge parallel field, velocity selector crossed fields |
| T3 | parallel wires opposite currents, magnetic force no work, long wire field value, solenoid field turns length, concentric coils opposite currents, force electron magnetic field, bar magnet torque angle, diamagnetic non uniform field |
| T4 | charge path straight circle helix, ammeter low resistance, ampere circuital law, galvanometer turns sensitivity, radius order equal speed particles, loop axial field ratio, galvanometer current sensitivity, work rotate magnet antiparallel, period proton circular motion |
| T5 | bar magnet axial equatorial, magnet potential energy torque, force wire perpendicular field, solenoid current for field, neutral point parallel wires, magnetic moment from max torque, proton kinetic energy circle radius, susceptibility dimensionless |

### P4 Electromagnetic Induction and Alternating Currents

| Test | Skill keys |
|---|---|
| T1 | lenz energy conservation, pure inductor phase, capacitor average power, rms from peak voltage, faraday emf flux change turns, lcr impedance power factor, transformer turns ratio voltage, inductance si unit henry |
| T2 | reactance expressions, resonance angular frequency, motional emf expression, transformer mutual induction dc, step down current, reactance values order 50 hz, motional emf rod value, resonance angular frequency value, rl circuit impedance reactance |
| T3 | phase resistor inductor capacitor, lcr inductive phase, mutual inductance emf value, solenoid self inductance, peak current from rms, capacitive reactance value, resonance voltage across inductor |
| T4 | flux maximum plane perpendicular, emf rate of change flux, flux through coil angle, ac generator peak emf, rotating rod emf, transformer current ratio, lcr average power |
| T5 | induction ac units, resonance impedance minimum, power factor resistive, inductive reactance frequency, impedance order circuits, induced charge flux change resistance, inductor current mains, resistor average power peak voltage |

### P5 Electromagnetic Waves

| Test | Skill keys |
|---|---|
| T1 | em spectrum uses, displacement current capacitor, em wave b0 from e0 |
| T2 | em waves no medium, e and b in phase, em wave frequency from wavelength, gamma rays origin |
| T3 | em spectrum wavelength ranges, em waves carry momentum, speed mu0 epsilon0, em bands frequency order |
| T4 | em wave sources production, fm wavelength from frequency, em wave speed medium permittivity |
| T5 | constant velocity no radiation, displacement current changing field, em wave e0 from b0, longest wavelength band |

### P6 Optics

| Test | Skill keys |
|---|---|
| T1 | lens power convex, telescope magnifying power, fringe width ydse, critical angle n two, single slit width central maximum, huygens secondary wavelets, prism dispersion deviation colours, concave mirror image position, lens maker equiconvex, lenses in contact combination, ydse bright dark fringe gap, compound microscope magnifying power, prism minimum deviation index |
| T2 | tir diamond example, dispersion prism example, diffraction slit example, apparent depth water, convex lens image beyond 2f, convex mirror image, ydse fringe width in water, single slit central maximum width, telescope tube length, critical angle speed in medium, frequency unchanged refraction |
| T3 | simple microscope focal length, concave lens power negative, refractive index from speed, simple microscope near point, concave mirror inside focus, refraction single spherical surface, ydse wavelength from fringe width, lens in liquid focal length, thin prism deviation, coherent sources meaning |
| T4 | mirror focal length radius, concave lens power, refractive index from speed value, telescope magnification value, fringe width colour, fringe width slit separation, huygens explains refraction, critical angle order media, convex lens object inside focus, combined power lenses dioptre, telescope image near point, ydse intensity path difference, critical angle glass water, plano convex lens maker |
| T5 | instrument formulas magnifying power, snell law refraction angle, concave mirror image size, focal length from magnification, fringe count wavelength change, angular fringe width, tir circle radius under water, prism minimum deviation value, ydse demonstrates interference |

### P7 Dual Nature of Matter and Radiation

| Test | Skill keys |
|---|---|
| T1 | photoelectric observations intensity frequency, photon energy wavelength ev, einstein equation stopping potential, de broglie electron accelerated |
| T2 | photoelectric terms meanings, photon momentum neutral, photon energy intensity, de broglie same kinetic energy order, photons per second laser |
| T3 | photon momentum formula, electron wavelength formula, einstein equation formula, work function threshold wavelength, max kinetic energy frequency, de broglie ratio proton alpha |
| T4 | de broglie momentum inverse, electron microscope wave nature, photon momentum value, electron wavelength from speed, planck constant stopping potential slope |
| T5 | photoelectric dependence graphs, threshold frequency condition, frequency number of electrons, photon momentum order radiations, stopping potential wavelength halved |

### P8 Atoms and Nuclei

| Test | Skill keys |
|---|---|
| T1 | isotopes isobars isotones, nuclear force short range, bohr energy level n two, nuclear radius mass number ratio, binding energy per nucleon helium, rutherford scattering empty space |
| T2 | bohr postulates stationary orbit, hydrogen transition energy 3 to 2, bohr radius n two, binding energy deuteron, nuclear density constant |
| T3 | hydrogen energies ionisation excitation, nuclear force strength, binding energy peak iron, mass defect sign, nuclear radius order, mass defect energy value, hydrogen transition wavelength 2 to 1 |
| T4 | atomic models thomson rutherford bohr, closest approach alpha gold, ground state potential energy, nuclear radius value, fission rate per watt |
| T5 | fission fusion mass products, spectral lines from level count, fusion q value deuterons, binding per nucleon iron, bohr speed with n |

### P9 Electronic Devices

| Test | Skill keys |
|---|---|
| T1 | intrinsic extrinsic semiconductor doping, band gap insulator, depletion layer bias, reverse bias current, full wave ripple frequency, band gap order ge si diamond |
| T2 | donor acceptor levels, majority carriers p n type, mass action law hole density, depletion region immobile ions |
| T3 | boron doping p type, intrinsic zero kelvin insulator, full wave output frequency, diode use rectifier |
| T4 | bias depletion width, barrier potential si ge, n type neutral, donor pentavalent, conductivity order materials |
| T5 | half full wave rectifier diodes, ideal diode switch, doping density ppm, acceptor ion negative |
