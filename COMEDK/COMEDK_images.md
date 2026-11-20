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
