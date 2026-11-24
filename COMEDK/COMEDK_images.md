# COMEDK UGET — image prompts

One entry per question that needs a figure, in the format given in `docs/instructions/COMEDK_Instructions.md` (section "Images"). Keep entries in test and question order. Every entry must match a question with the same `image_reference`.


| Test 1 ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T01-Q014 | images/COMEDK_T01_Q014.png | Force–distance plot through (0,4), (2,4) and (5,0), in metres and newtons |
| COMEDK27-T01-Q055 | images/COMEDK_T01_Q055.png | Ray X and ray Y have incidence sines 0.85 and 0.95 |
| COMEDK27-T01-Q109 | images/COMEDK_T01_Q109.png | Rows of (A concentration, B concentration, initial rate) are (c,d,r), (2c,d,2r), (2c,2d,8r) |
| COMEDK27-T01-Q121 | images/COMEDK_T01_Q121.png | Relation matrix rows (1,1,0), (1,1,1), (0,1,1), with labels 1–3 |

The plotted values are generated from the Test 1 specifications in `tools/comedk/pilot_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T02-Q020 | images/COMEDK_T02_Q020.png | One SHM cycle from +A, with the first time-axis crossing at T/4 and a descending trace |
| COMEDK27-T02-Q054 | images/COMEDK_T02_Q054.png | Two wires spaced d apart, with 3 A upward on the left and 6 A downward on the right |
| COMEDK27-T02-Q082 | images/COMEDK_T02_Q082.png | Chlorido groups occupy opposite axial sites; four A ligands occupy equatorial sites |
| COMEDK27-T02-Q146 | images/COMEDK_T02_Q146.png | Venn diagram with disjoint region counts 13 in A only, 12 in both, and 18 in B only |
| COMEDK27-T03-Q011 | images/COMEDK_T03_Q011.png | Position in metres against time in seconds, straight from (2,8) to (5,2) |
| COMEDK27-T03-Q050 | images/COMEDK_T03_Q050.png | Velocity in m/s against time in seconds, straight from (0,−2) to (3,4) |
| COMEDK27-T03-Q104 | images/COMEDK_T03_Q104.png | Two axial bonds, two equatorial bonds, and two dots at the third equatorial site |
| COMEDK27-T03-Q151 | images/COMEDK_T03_Q151.png | Feasible polygon vertices A(0,0), B(5,0), C(3,4), and D(0,5) |

Generate the Test 2 and Test 3 figures with `python tools/comedk/batch_figures.py`. Their alt text is in `COMEDK/authoring/batch_figure_meta.json` and the assembled questions.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T04-Q036 | images/COMEDK_T04_Q036.png | Diode I–V curve with P in reverse bias, Q at small forward current and R at larger forward current |
| COMEDK27-T04-Q055 | images/COMEDK_T04_Q055.png | Terminal voltage and current points P(1 A, 10 V) and Q(3 A, 6 V) |
| COMEDK27-T04-Q080 | images/COMEDK_T04_Q080.png | Four orbital lobes between the x and y axes, with signs alternating across each axis |
| COMEDK27-T04-Q142 | images/COMEDK_T04_Q142.png | Feasible polygon A(0,0), B(4,0), C(3,2), D(0,3) |
| COMEDK27-T05-Q002 | images/COMEDK_T05_Q002.png | Velocity–time trace from (0 s, −4 m/s) to (6 s, 8 m/s), crossing zero at 2 s |
| COMEDK27-T05-Q019 | images/COMEDK_T05_Q019.png | Dashed Gaussian surface between the shell labelled +Q and the outer shell labelled −2Q |
| COMEDK27-T05-Q086 | images/COMEDK_T05_Q086.png | Carbonate Lewis contributor with two single bonds and one double bond. The marked O has one bond and three lone pairs. |
| COMEDK27-T05-Q145 | images/COMEDK_T05_Q145.png | Feasible triangle A(5,0), B(2,3), C(5,3), and objective level x+y=5 through A and B |

Generate these figures with `python tools/comedk/tests_04_05_figures.py`. Figure descriptions are in `COMEDK/authoring/batch_figure_meta.json`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T06-Q013 | images/COMEDK_T06_Q013.png | Current against voltage at P(2 V, 1 A) and Q(4 V, 4 A) |
| COMEDK27-T06-Q014 | images/COMEDK_T06_Q014.png | Straight force–position trace from (0 m, 12 N) to (3 m, 0 N) |
| COMEDK27-T06-Q063 | images/COMEDK_T06_Q063.png | Molar conductivity curves, with Y showing a much stronger fractional rise on dilution than X |
| COMEDK27-T06-Q136 | images/COMEDK_T06_Q136.png | Feasible polygon A(0,0), B(5,0), C(3,2), D(0,4) |
| COMEDK27-T07-Q004 | images/COMEDK_T07_Q004.png | Three voltage traces, with alternating, positive-only half-wave, and positive full-wave lobes |
| COMEDK27-T07-Q035 | images/COMEDK_T07_Q035.png | Force–time triangle with peak 6 N and base 0.20 s |
| COMEDK27-T07-Q082 | images/COMEDK_T07_Q082.png | Octahedral energy splitting with a fully paired lower group and empty upper orbitals |
| COMEDK27-T07-Q139 | images/COMEDK_T07_Q139.png | Feasible polygon A(0,0), B(4,0), C(3,3), D(0,3) |

Generate these figures with `python tools/comedk/tests_06_07_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T08-Q011 | images/COMEDK_T08_Q011.png | Position–time trace with equal displacements at B and C and motion between them |
| COMEDK27-T08-Q082 | images/COMEDK_T08_Q082.png | Octahedral arrangement with two axial A sites opposite each other and one equatorial A site |
| COMEDK27-T08-Q130 | images/COMEDK_T08_Q130.png | Feasible polygon A(0,0), B(4,0), C(3,3), D(0,5) and interior point E(1,2) |
| COMEDK27-T08-Q170 | images/COMEDK_T08_Q170.png | Venn region counts of 9 in A only, 6 in B only and 4 outside both |
| COMEDK27-T09-Q003 | images/COMEDK_T09_Q003.png | Forward diode curve with Q on a steeper portion than P |
| COMEDK27-T09-Q047 | images/COMEDK_T09_Q047.png | Horizontal pipe sections with cross-sectional areas 4A and A |
| COMEDK27-T09-Q064 | images/COMEDK_T09_Q064.png | Initial tangent and interval secant of a falling concentration curve |
| COMEDK27-T09-Q133 | images/COMEDK_T09_Q133.png | Feasible polygon A(0,0), B(5,0), C(4,2), D(0,3) |

Generate these figures with `python tools/comedk/tests_08_09_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T10-Q002 | images/COMEDK_T10_Q002.png | Velocity increases from 1 m/s at 1 s to 13 m/s at 5 s |
| COMEDK27-T10-Q040 | images/COMEDK_T10_Q040.png | Sample X has a linear voltage–current trace through the origin; sample Y has a curved trace |
| COMEDK27-T10-Q081 | images/COMEDK_T10_Q081.png | Chromium-containing solution changes from yellow to orange |
| COMEDK27-T10-Q124 | images/COMEDK_T10_Q124.png | Feasible vertices A(0,2), B(2,0), C(5,0), D(0,5) |
| COMEDK27-T10-Q145 | images/COMEDK_T10_Q145.png | Shaded right half of an upper semicircle of radius 3 |
| COMEDK27-T11-Q023 | images/COMEDK_T11_Q023.png | Straight stress–strain segment through (0.001, 200 MPa) and (0.002, 400 MPa) |
| COMEDK27-T11-Q090 | images/COMEDK_T11_Q090.png | Three Fischer projections with the same end groups and different hydroxyl orientations |
| COMEDK27-T11-Q127 | images/COMEDK_T11_Q127.png | Feasible polygon and a reference objective line with equation 2x+y=8 |
| COMEDK27-T11-Q138 | images/COMEDK_T11_Q138.png | Graph of the derivative with a negative-to-positive crossing at x=2 |

Generate these figures with `python tools/comedk/tests_10_11_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T12-Q054 | images/COMEDK_T12_Q054.png | Voltage–current points P(1 A, 2 V), Q(2 A, 3 V) and R(3 A, 7 V) |
| COMEDK27-T12-Q082 | images/COMEDK_T12_Q082.png | Square-planar X–M–X and Y–M–Y axes |
| COMEDK27-T12-Q122 | images/COMEDK_T12_Q122.png | Venn region counts of 7 in A only, 4 in both, 8 in B only and 6 outside both |
| COMEDK27-T12-Q125 | images/COMEDK_T12_Q125.png | Relation arrows from 1 to 2 and from 2 to 3 |
| COMEDK27-T13-Q009 | images/COMEDK_T13_Q009.png | Binding energy per nucleon at three labelled positions on a schematic mass-number curve |
| COMEDK27-T13-Q045 | images/COMEDK_T13_Q045.png | Sinusoidal input and positive output lobes for both input polarities |
| COMEDK27-T13-Q064 | images/COMEDK_T13_Q064.png | Tangents to concentration at L and M, with L falling faster |
| COMEDK27-T13-Q121 | images/COMEDK_T13_Q121.png | Feasible polygon with A(0,0), B(4,0), C(3,1) and D(0,3) |

Generate these figures with `python tools/comedk/tests_12_13_figures.py`.
