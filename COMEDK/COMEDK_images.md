# COMEDK UGET — image prompts

One entry per question that needs a figure, in the format given in `docs/instructions/COMEDK_Instructions.md` (section "Images"). Keep entries in test and question order. Every entry must match a question with the same `image_reference`.


| Test 1 ID | File | Data required to solve |
|---|---|---|
| COMEDK27-T01-Q014 | images/COMEDK_T01_Q014.png | Force–distance plot through (0,4), (2,4) and (5,0), in metres and newtons |
| COMEDK27-T01-Q055 | images/COMEDK_T01_Q055.png | Ray X and ray Y have incidence sines 0.85 and 0.95 |
| COMEDK27-T01-Q109 | images/COMEDK_T01_Q109.png | Rows of (A concentration, B concentration, initial rate) are (c,d,r), (2c,d,2r), (2c,2d,8r) |
| COMEDK27-T01-Q121 | images/COMEDK_T01_Q121.png | Relation matrix rows (1,1,0), (1,1,1), (0,1,1), with labels 1–3 |

The plotted values are generated from the Test 1 specifications in `tools/comedk/pilot_figures.py`.
