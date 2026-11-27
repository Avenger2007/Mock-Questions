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

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T14-Q026 | images/COMEDK_T14_Q026.png | Three standing-wave loops with both string ends fixed |
| COMEDK27-T14-Q054 | images/COMEDK_T14_Q054.png | Vertical electric field and horizontal propagation in the plane of the figure |
| COMEDK27-T14-Q175 | images/COMEDK_T14_Q175.png | Feasible vertices A(0,0), B(3,0), C(2,2) and D(0,3) |
| COMEDK27-T14-Q180 | images/COMEDK_T14_Q180.png | Increasing graph with horizontal asymptotes marked at ±π/2 |
| COMEDK27-T15-Q002 | images/COMEDK_T15_Q002.png | Piecewise linear velocity trace through (0,−2), (3,4) and (6,2) in SI units |
| COMEDK27-T15-Q006 | images/COMEDK_T15_Q006.png | Equal potential steps with unequal line spacing near P, Q and R |
| COMEDK27-T15-Q022 | images/COMEDK_T15_Q022.png | Schematic binding-energy curve showing a higher value at B than at A |
| COMEDK27-T15-Q058 | images/COMEDK_T15_Q058.png | Sinusoidal input and positive output pulses separated by blank half-cycles |
| COMEDK27-T15-Q065 | images/COMEDK_T15_Q065.png | Ethane Newman projection with the three rear bonds offset from the front bonds |
| COMEDK27-T15-Q134 | images/COMEDK_T15_Q134.png | Disjoint Venn counts of 8, 5, 7 and 5 |
| COMEDK27-T15-Q137 | images/COMEDK_T15_Q137.png | Relation arrows 1→a, 2→a, 2→b and 3→c |
| COMEDK27-T15-Q143 | images/COMEDK_T15_Q143.png | Complex plane with z marked at (−2,1) |

Generate these figures with `python tools/comedk/tests_14_15_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T16-Q023 | images/COMEDK_T16_Q023.png | The stress–strain trace is straight through O to P, with changing slope beyond P |
| COMEDK27-T16-Q047 | images/COMEDK_T16_Q047.png | Position–time line X has a constant nonzero slope and curve Y steepens |
| COMEDK27-T16-Q051 | images/COMEDK_T16_Q051.png | Photoelectric trace G has a more negative stopping intercept than F |
| COMEDK27-T16-Q139 | images/COMEDK_T16_Q139.png | Two line segments meet at x=0 with unequal slopes |
| COMEDK27-T16-Q169 | images/COMEDK_T16_Q169.png | Feasible vertices A(0,0), B(5,0), C(4,2) and D(1,4) |
| COMEDK27-T17-Q019 | images/COMEDK_T17_Q019.png | P and R are at 20 V and Q is at 10 V |
| COMEDK27-T17-Q021 | images/COMEDK_T17_Q021.png | The Y curve has greater voltage than X at 3 A |
| COMEDK27-T17-Q082 | images/COMEDK_T17_Q082.png | Three paired lower orbitals and two singly occupied upper orbitals |
| COMEDK27-T17-Q176 | images/COMEDK_T17_Q176.png | Left and right rays include endpoints −1 and 4, respectively |

Generate these figures with `python tools/comedk/tests_16_17_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T18-Q011 | images/COMEDK_T18_Q011.png | X reverses slope at the shared point P, while Y keeps a positive slope |
| COMEDK27-T18-Q037 | images/COMEDK_T18_Q037.png | The torque-magnitude curve peaks at a 90° angle |
| COMEDK27-T18-Q050 | images/COMEDK_T18_Q050.png | The velocity trace rises from 0 to 2 s, then falls while staying positive from 2 to 5 s |
| COMEDK27-T18-Q063 | images/COMEDK_T18_Q063.png | The strong-electrolyte molar-conductivity trace falls as square-root concentration increases |
| COMEDK27-T18-Q082 | images/COMEDK_T18_Q082.png | One X and one Y occupy each of three opposite octahedral position pairs |
| COMEDK27-T18-Q133 | images/COMEDK_T18_Q133.png | A line and a curved branch share a filled joining point and common tangent at x=0 |
| COMEDK27-T18-Q149 | images/COMEDK_T18_Q149.png | Relation arrows 1→a, 2→b and 3→b leave c with no incoming arrow |
| COMEDK27-T18-Q155 | images/COMEDK_T18_Q155.png | The Argand point z is at (0,−3) |
| COMEDK27-T18-Q163 | images/COMEDK_T18_Q163.png | Feasible vertices A(0,1), B(3,0), C(4,3) and D(0,4) |
| COMEDK27-T18-Q168 | images/COMEDK_T18_Q168.png | The inverse cosine curve passes through (0,π/2) |
| COMEDK27-T19-Q003 | images/COMEDK_T19_Q003.png | Radius SP joins the centre of curvature to a point on the wavefront |
| COMEDK27-T19-Q033 | images/COMEDK_T19_Q033.png | P and Q lie on 12 V and R on 30 V |
| COMEDK27-T19-Q036 | images/COMEDK_T19_Q036.png | A circular path is centred around a long wire perpendicular to the drawing |
| COMEDK27-T19-Q049 | images/COMEDK_T19_Q049.png | Approximate mass numbers and binding-per-nucleon ordinates for A, B and C |
| COMEDK27-T19-Q128 | images/COMEDK_T19_Q128.png | Filled endpoints (−1,2) and (3,6) of a rising graph |

Generate these figures with `python tools/comedk/tests_18_19_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T20-Q002 | images/COMEDK_T20_Q002.png | Velocity–time vertices O=(0 s,0 m/s), A=(2 s,6 m/s), B=(7 s,0 m/s). |
| COMEDK27-T20-Q082 | images/COMEDK_T20_Q082.png | Octahedral M with one B directly above and one B directly below, and four A equatorial ligands. |
| COMEDK27-T20-Q127 | images/COMEDK_T20_Q127.png | Both branches meet an open point at (1,2). A filled point at (1,4) gives the function value. |
| COMEDK27-T20-Q157 | images/COMEDK_T20_Q157.png | Shaded feasible polygon with vertices (0,0), (4,0), (4,2), (2,4) and (0,3). |
| COMEDK27-T20-Q162 | images/COMEDK_T20_Q162.png | Increasing curve from the filled endpoint (−1,−π/2) to (1,π/2), passing through the origin. |
| COMEDK27-T21-Q014 | images/COMEDK_T21_Q014.png | Force–position vertices (0,0), (1,4), (3,0), (4,−3) and (5,0), with position in m and force in N. |
| COMEDK27-T21-Q018 | images/COMEDK_T21_Q018.png | X rises from zero at −3 V, Y at −1 V. At −2 V X is above the axis and Y lies on it. |
| COMEDK27-T21-Q023 | images/COMEDK_T21_Q023.png | Two straight stress–strain lines through the origin. X is steeper than Y. |
| COMEDK27-T21-Q082 | images/COMEDK_T21_Q082.png | Octahedral d-orbital filling. Three lower t₂g orbitals hold two electrons each, and both higher e_g orbitals are empty. |
| COMEDK27-T21-Q128 | images/COMEDK_T21_Q128.png | A leftward ray begins at an open dot at −2 and a rightward ray at a closed dot at 3. |
| COMEDK27-T21-Q161 | images/COMEDK_T21_Q161.png | Arrows run from set A to set B as 1→q, 2→p and 3→q. The target r receives no arrow. |
| COMEDK27-T21-Q167 | images/COMEDK_T21_Q167.png | The Argand diagram marks z at real coordinate 2 and imaginary coordinate 1. |
| COMEDK27-T21-Q171 | images/COMEDK_T21_Q171.png | Vector u points right, and vector v points up from the shared origin. |

Generate these figures with `python tools/comedk/tests_20_21_figures.py`.

| Question ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T22-Q003 | images/COMEDK_T22_Q003.png | Binding energy per nucleon at B is about 8.8 MeV and at C about 7.6 MeV. |
| COMEDK27-T22-Q035 | images/COMEDK_T22_Q035.png | Force–time vertices (0,0),(2,8),(3,8),(5,−4), with time in seconds and force in newtons. |
| COMEDK27-T22-Q082 | images/COMEDK_T22_Q082.png | Both diagrams show octahedral centres. In I the three X ligands occupy one end of each axis. In II two X ligands occupy opposite ends of one axis. |
| COMEDK27-T22-Q137 | images/COMEDK_T22_Q137.png | A to B arrows map 1→p and 2→r. B to C arrows map p→4, q→7 and r→4. |
| COMEDK27-T22-Q151 | images/COMEDK_T22_Q151.png | Feasible quadrilateral with A=(0,0), B=(4,0), C=(4,3), D=(0,2). |
| COMEDK27-T22-Q156 | images/COMEDK_T22_Q156.png | X tends to −π/2 and π/2. Y is the same shape shifted upward and tends to 0 and π. |
| COMEDK27-T23-Q011 | images/COMEDK_T23_Q011.png | Position–time vertices O=(0,0), A=(2,2), B=(3,0), C=(5,4), with seconds and metres. |
| COMEDK27-T23-Q031 | images/COMEDK_T23_Q031.png | Photocurrent is positive at 0 V and falls to zero at a collector voltage of −2 V. |
| COMEDK27-T23-Q050 | images/COMEDK_T23_Q050.png | Velocity–time vertices A=(0,0), B=(1,3), C=(3,0), D=(4,−2), E=(6,−1), in seconds and m/s. |
| COMEDK27-T23-Q082 | images/COMEDK_T23_Q082.png | Five d orbitals in each drawing. I shows three pairs and no single electrons. II shows one pair and four single electrons. |
| COMEDK27-T23-Q095 | images/COMEDK_T23_Q095.png | Ethane viewed along C–C with each dashed rear C–H bond aligned behind a solid front C–H bond. |
| COMEDK27-T23-Q142 | images/COMEDK_T23_Q142.png | Feasible region polygon with O=(0,0), P=(3,0), Q=(3,2), R=(0,4). |

Generate these figures with `python tools/comedk/tests_22_23_figures.py`.
