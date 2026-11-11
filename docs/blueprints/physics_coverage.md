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
| T6 | charged sphere field potential regions, three charge equilibrium, ring axial potential, dielectric half area parallel, electron speed accelerated potential, connected spheres charge density, series then parallel reconnect |
| T7 | dielectric polarisation field reduced, isolated capacitor dielectric voltage, force middle charge line, field bisector two equal charges, energy density capacitor gap, dipole work rotate ninety, capacitor network branch charge, point charge potential value |
| T8 | gauss line sheet shell fields, equipotentials never intersect, field steepest potential decrease, potential values order, proton speed potential drop, plate separation doubled isolated, field from potential gradient, flux cube face centre charge |
| T9 | electrostatic work processes match, isolated sphere capacitance, three series capacitors charge voltage, alpha kinetic energy kilovolt, spheres touched force change, electron force between plates, opposite polarity capacitors energy lost |
| T10 | gauss law any distribution, outside charge zero flux, equilateral triangle two charges field, work separate opposite charges, area doubled gap halved capacitance, line charge field value, capacitor bank voltage rating, dipole equatorial field value |
| T11 | dielectric isolated capacitor effects match, zero field not zero potential, like charges separate pe falls, four distributions field order, electron deflection plates, stacked dielectric layers capacitance, field from 3d potential, merged drops potential |

### P2 Current Electricity

| Test | Skill keys |
|---|---|
| T1 | parallel series resistance, stretched wire resistance, internal resistance terminal voltage, drift velocity copper wire, wheatstone balance fourth arm, cells parallel equivalent emf, bulb rating resistance, semiconductor resistivity temperature |
| T2 | kirchhoff rules conservation, resistivity length independent, temperature coefficient resistance, joule heating time, cells in series internal resistance, balanced bridge equivalent resistance, mobility si unit |
| T3 | current density sigma e, drift velocity tau, resistivity relaxation time, series same current parallel less, terminal voltage emf, ohm law diode, wire dimensions resistance order, bulbs series power total, emf internal resistance two readings, resistivity from resistance dimensions |
| T4 | three identical resistor combinations, junction rule unknown current, current density value, kirchhoff two battery network, electrical energy cost kwh, drift velocity length fixed voltage |
| T5 | current scalar, manganin resistivity temperature, drift opposite field, four resistor network equivalent, terminal voltage discharge, battery charging terminal voltage, resistance ratio length diameter, parallel resistor power |
| T6 | cell short circuit open circuit load, relaxation time temperature, electron density metal temperature, drift field proportional, cell arrangements current order, branch current series parallel, stretched wire percentage resistance, drift speed ratio series wires |
| T7 | parallel three resistors readings, internal resistance voltmeter readings, mixed grouping cells current, temperature from resistance rise, series resistor voltage share, series parallel heat ratio |
| T8 | kirchhoff any circuit, balanced bridge no current, circular wire resistance points, series bulbs power ratio, short circuit current internal resistance, electrons count current time, relaxation time copper |
| T9 | identical cells series parallel emf r, manganin standard resistor, resistivity independent length, four ohm groupings order, wire cut four parallel, mobility drift speed field, parallel pair series power branch |
| T10 | conduction terms meanings match, nichrome wire resistance diameter, heater coil halved power, opposing cells weaker terminal voltage, number parallel resistors current, drift speed current density |
| T11 | internal resistance depends electrolyte, parallel cells small load, best grouping cells maximum current, copper carbon temperature compensation, heat internal resistance minute, voltmeter loading reading, electrons per second filament |

### P3 Magnetic Effects of Current and Magnetism

| Test | Skill keys |
|---|---|
| T1 | field loop wire solenoid formulas, magnetic materials properties, field magnitudes order wire loop solenoid, force on current wire angle, galvanometer to ammeter shunt, force parallel wires per metre, charged particle circle radius |
| T2 | magnetic quantities si units, semicircle field centre, coil magnetic moment, coil torque plane angle, galvanometer to voltmeter series, force charge parallel field, velocity selector crossed fields |
| T3 | parallel wires opposite currents, magnetic force no work, long wire field value, solenoid field turns length, concentric coils opposite currents, force electron magnetic field, bar magnet torque angle, diamagnetic non uniform field |
| T4 | charge path straight circle helix, ammeter low resistance, ampere circuital law, galvanometer turns sensitivity, radius order equal speed particles, loop axial field ratio, galvanometer current sensitivity, work rotate magnet antiparallel, period proton circular motion |
| T5 | bar magnet axial equatorial, magnet potential energy torque, force wire perpendicular field, solenoid current for field, neutral point parallel wires, magnetic moment from max torque, proton kinetic energy circle radius, susceptibility dimensionless |
| T6 | field lines inside bar magnet, current loop dipole, helix pitch proton, wire field distance for value, voltmeter range extension, force loop near wire, orbiting electron magnetic moment, relative permeability from susceptibility |
| T7 | meters conversion ideal resistance, magnetic force no kinetic energy, solenoid end half field, loop torque order shapes, ammeter range extension shunt, midpoint field opposite currents, electron radius after acceleration, coil turns centre field |
| T8 | magnetic force situations, loop rewound turns field factor, field inside thick wire, alpha force magnetic field, circle square same wire moment, susceptibility from magnetisation, shunt one ninth current share |
| T9 | ammeter series high resistance false, radial field linear scale, loop current from centre field, proton deuteron equal ke radius, parallel wires force two metres, square coil maximum torque, galvanometer resistance from shunt, electron speed circle field |
| T10 | susceptibility kinds match, ampere law any closed loop, solenoid uniform inside, period of revolution particles order, electron revolution frequency, perpendicular loops net field, semicircular wire force, magnetisation from moment volume |
| T11 | toroid solenoid fields match, alpha radius after acceleration, antiparallel wires outside point field, voltage sensitivity galvanometer, velocity selector then circle proton, galvanometer voltmeter ammeter pair, relative permeability from b h |

### P4 Electromagnetic Induction and Alternating Currents

| Test | Skill keys |
|---|---|
| T1 | lenz energy conservation, pure inductor phase, capacitor average power, rms from peak voltage, faraday emf flux change turns, lcr impedance power factor, transformer turns ratio voltage, inductance si unit henry |
| T2 | reactance expressions, resonance angular frequency, motional emf expression, transformer mutual induction dc, step down current, reactance values order 50 hz, motional emf rod value, resonance angular frequency value, rl circuit impedance reactance |
| T3 | phase resistor inductor capacitor, lcr inductive phase, mutual inductance emf value, solenoid self inductance, peak current from rms, capacitive reactance value, resonance voltage across inductor |
| T4 | flux maximum plane perpendicular, emf rate of change flux, flux through coil angle, ac generator peak emf, rotating rod emf, transformer current ratio, lcr average power |
| T5 | induction ac units, resonance impedance minimum, power factor resistive, inductive reactance frequency, impedance order circuits, induced charge flux change resistance, inductor current mains, resistor average power peak voltage |
| T6 | induced emf kinds expressions, capacitance for resonance, transformer efficiency primary current, phase angle lcr value, force pull loop out of field, inductive reactance value 100 hz |
| T7 | wattless current, average ac zero, generator emf revolutions per second, self inductance from emf, average power phase equations, impedance above resonance, coaxial solenoids mutual inductance |
| T8 | induction devices laws roles, mutual inductance orientation, induced emf open circuit, component currents mains order, sliding rod power dissipated, transformer secondary turns, resonant frequency hertz |
| T9 | ac quantities sine equation match, inductor energy stored, rc circuit impedance current, rl circuit average power, self inductance flux linkage, resonance current resistance only |
| T10 | capacitor current leads, inductor no average power, loop current falling field, aircraft wing emf, lcr capacitor voltage off resonance, mains peak voltage, transmission line loss |
| T11 | lcr resonance quantities match, inductance core dependence, mutual inductance reciprocal, generator peak emf order, lcr average power off resonance, coil flipped charge, transformer load primary current |

### P5 Electromagnetic Waves

| Test | Skill keys |
|---|---|
| T1 | em spectrum uses, displacement current capacitor, em wave b0 from e0 |
| T2 | em waves no medium, e and b in phase, em wave frequency from wavelength, gamma rays origin |
| T3 | em spectrum wavelength ranges, em waves carry momentum, speed mu0 epsilon0, em bands frequency order |
| T4 | em wave sources production, fm wavelength from frequency, em wave speed medium permittivity |
| T5 | constant velocity no radiation, displacement current changing field, em wave e0 from b0, longest wavelength band |
| T6 | em wave k omega relations, uv lasik, microwave oven, gamma remote control, photon energy order bands |
| T7 | wavelength to frequency bands, displacement current value, wavelength in medium |
| T8 | x rays frequency uv, infrared physiotherapy, omega from wave number, light travel time sun |
| T9 | em waves history scientists, ozone absorbs uv, radio lower frequency microwaves, wavelengths frequency order |
| T10 | em detectors match, wavelength in medium ghz, lasik ultraviolet |
| T11 | e over b equals c, radiation pressure, wave equation wavelength e0, one micrometre band |

### P6 Optics

| Test | Skill keys |
|---|---|
| T1 | lens power convex, telescope magnifying power, fringe width ydse, critical angle n two, single slit width central maximum, huygens secondary wavelets, prism dispersion deviation colours, concave mirror image position, lens maker equiconvex, lenses in contact combination, ydse bright dark fringe gap, compound microscope magnifying power, prism minimum deviation index |
| T2 | tir diamond example, dispersion prism example, diffraction slit example, apparent depth water, convex lens image beyond 2f, convex mirror image, ydse fringe width in water, single slit central maximum width, telescope tube length, critical angle speed in medium, frequency unchanged refraction |
| T3 | simple microscope focal length, concave lens power negative, refractive index from speed, simple microscope near point, concave mirror inside focus, refraction single spherical surface, ydse wavelength from fringe width, lens in liquid focal length, thin prism deviation, coherent sources meaning |
| T4 | mirror focal length radius, concave lens power, refractive index from speed value, telescope magnification value, fringe width colour, fringe width slit separation, huygens explains refraction, critical angle order media, convex lens object inside focus, combined power lenses dioptre, telescope image near point, ydse intensity path difference, critical angle glass water, plano convex lens maker |
| T5 | instrument formulas magnifying power, snell law refraction angle, concave mirror image size, focal length from magnification, fringe count wavelength change, angular fringe width, tir circle radius under water, prism minimum deviation value, ydse demonstrates interference |
| T6 | mirror focal length medium independent, convex rear view, object distance magnification mirror, glass slab normal shift, ydse two wavelengths coincide, telescope eyepiece from length, microscope objective object distance, speed from critical angle sine, diverging lens power, single slit first minimum width |
| T7 | convex lens image positions, telescope objective focal length long, microscope image inverted, lens power order, lens two positions focal length, ydse dark fringes either side, thin prism angle from deviation, refraction glass to air angle, convex mirror magnification value, microscope intermediate image |
| T8 | critical angle values indices, microscope tube length, equiconcave lens maker, unequal slits intensity ratio, apparent depth two layers, convex mirror focal from image, two convex lenses power, single slit angular width central, speed ratio two media |
| T9 | red faster in glass, frequency unchanged refraction, concave mirror 45 cm image, concave lens object at f, concave refracting surface image, simple microscope infinity, fourth bright fringe distance, prism minimum deviation index 1.5, index from real apparent depth, tir conditions denser rarer |
| T10 | power to focal length match, concave magnified real false, convex always virtual, fringe width settings order, image height convex lens, path difference third dark, central band screen width, prism normal incidence deviation, light time glass plate, bird seen by fish apparent height |
| T11 | ydse changes effects match, lens in denser liquid diverges, minimum object image distance 4f, intensity path difference sixth, fibre core cladding critical angle, prism incidence at minimum deviation, telescope separation near point image, first secondary maximum angle, biconvex unequal radii |

### P7 Dual Nature of Matter and Radiation

| Test | Skill keys |
|---|---|
| T1 | photoelectric observations intensity frequency, photon energy wavelength ev, einstein equation stopping potential, de broglie electron accelerated |
| T2 | photoelectric terms meanings, photon momentum neutral, photon energy intensity, de broglie same kinetic energy order, photons per second laser |
| T3 | photon momentum formula, electron wavelength formula, einstein equation formula, work function threshold wavelength, max kinetic energy frequency, de broglie ratio proton alpha |
| T4 | de broglie momentum inverse, electron microscope wave nature, photon momentum value, electron wavelength from speed, planck constant stopping potential slope |
| T5 | photoelectric dependence graphs, threshold frequency condition, frequency number of electrons, photon momentum order radiations, stopping potential wavelength halved |
| T6 | experiments wave particle evidence, stopping potential difference wavelengths, electron wavelength ratio voltages, photoelectron speed from energy |
| T7 | kmax frequency slope h, stopping potential slope same, kmax not proportional, photocurrent quantum efficiency, proton wavelength kinetic energy, threshold frequency from work function |
| T8 | photon electron values match, photoemission instantaneous, intense light below threshold, same voltage particles wavelength order, photons per second ratio colours |
| T9 | work function threshold wavelength match, wavelength for stopping potential, photoelectron speed 200 nm, voltage for electron wavelength |
| T10 | caesium visible emission, stopping potential intensity independent, electron momentum from wavelength, photon equal momentum electron, stopping potential from threshold wavelength |
| T11 | matter wave values match, stopping potential differs metals, saturation all collected, electrons photons wavelength order, sunlight photon flux |

### P8 Atoms and Nuclei

| Test | Skill keys |
|---|---|
| T1 | isotopes isobars isotones, nuclear force short range, bohr energy level n two, nuclear radius mass number ratio, binding energy per nucleon helium, rutherford scattering empty space |
| T2 | bohr postulates stationary orbit, hydrogen transition energy 3 to 2, bohr radius n two, binding energy deuteron, nuclear density constant |
| T3 | hydrogen energies ionisation excitation, nuclear force strength, binding energy peak iron, mass defect sign, nuclear radius order, mass defect energy value, hydrogen transition wavelength 2 to 1 |
| T4 | atomic models thomson rutherford bohr, closest approach alpha gold, ground state potential energy, nuclear radius value, fission rate per watt |
| T5 | fission fusion mass products, spectral lines from level count, fusion q value deuterons, binding per nucleon iron, bohr speed with n |
| T6 | hydrogen series regions, carbon 14 neutrons protons, isotopes hydrogen, binding per nucleon order, lyman balmer first line ratio, mass equivalent energy fission |
| T7 | bohr quantities scaling n, ionise from n three wavelength, balmer series limit, carbon twelve binding energy, energy equivalent one gram |
| T8 | rutherford model line spectrum, nucleus size range, excitation energy 2 to 4, hydrogen line 4 to 2 wavelength, fission energy from binding curve, nuclear radius ratio mass numbers |
| T9 | hydrogen n2 radius energies match, series regions, lyman ends n1, transitions photon energy order, electron speed third orbit, lithium proton q value |
| T10 | nuclear constants match, paschen first line wavelength, minimum energy balmer lines, angular momentum third orbit, uranium mass per day reactor |
| T11 | nuclear force repulsive short, radius cube root, de broglie bohr third orbit, ionisation frequency n2, deuteron triton fusion energy, oxygen mass defect |

### P9 Electronic Devices

| Test | Skill keys |
|---|---|
| T1 | intrinsic extrinsic semiconductor doping, band gap insulator, depletion layer bias, reverse bias current, full wave ripple frequency, band gap order ge si diamond |
| T2 | donor acceptor levels, majority carriers p n type, mass action law hole density, depletion region immobile ions |
| T3 | boron doping p type, intrinsic zero kelvin insulator, full wave output frequency, diode use rectifier |
| T4 | bias depletion width, barrier potential si ge, n type neutral, donor pentavalent, conductivity order materials |
| T5 | half full wave rectifier diodes, ideal diode switch, doping density ppm, acceptor ion negative |
| T6 | ideal diode reverse resistance, majority minority bias currents, diode series resistor current, bias from potentials |
| T7 | rectifier output filter centre tap, holes direction field, holes positive carriers, thermal pair generation, depletion region formation order |
| T8 | diode circuit currents, rectifier peak output rms input, centre tap diodes conducting |
| T9 | n type majority holes false, band overlap conductor, electron density p type, forward bias depletion narrows |
| T10 | dopant valency carriers match, rectifier pure dc false, full wave ripple double, ripple frequency rectifiers order |
| T11 | silicon carrier densities match, centre tap peak silicon drop, parallel diode branches current |
