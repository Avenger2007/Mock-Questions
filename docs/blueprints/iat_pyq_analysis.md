# IAT PYQ analysis and preparation priorities

Prepared 29 October 2026 for OurMocks. This is a descriptive study of the acquired papers, followed by an editorial blueprint for original mock questions. It is not an official chapter-weightage notification or a calibrated prediction of the next paper.

## Evidence and method

The English corpus contains **539 questions from nine papers**: 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025 and 2026. Eight papers have 60 questions; the acquired 2025 English copy has 59 and ends at Physics question 14. That absent item is not imputed. The 2020 paper has not been recovered. Hindi copies support accessibility and figure interpretation but are not counted again as independent questions. See [archive provenance](../../PYQ/IAT/SOURCES.md) and [manifest](../../PYQ/IAT/manifest.json).

The official archive was supplied by the user, but its server could not be downloaded reliably. Stored PDFs came from labelled mirrors; they are not misrepresented as official-server downloads. The 2026 copy is a **provisional key document** with an explicit first-option answer convention. Its option-letter order cannot estimate real-exam answer distributions. OCR, especially the scanned 2018 copy, contains formula and layout errors. Original PDFs and page images are authoritative when text is unclear.

Every acquired English question received a manual primary-chapter, dominant-task and difficulty tag. Primary-class labels are derived coarsely from the chapter-family taxonomy, not separately assigned at the sub-topic level for all 539 items. The [539-row ledger](iat_pyq_ledger.json) includes source PDF and one-based PDF page; [manual tags](iat_pyq_manual_tags.txt) and [taxonomy](iat_taxonomy.json) make the choices inspectable. Cross-chapter items are counted once, against their dominant topic. Some mathematics families span both classes; the derived class split is approximate and unsuitable for exact Class 11/12 quota decisions. The broad syllabus units are not equal-sized chapters, so percentages across units need that context.

Difficulty is **an editorial estimate**, not observed candidate success rate, item discrimination or official difficulty. Easy means a direct concept or short computation; medium means linked reasoning or two to three substantive steps; hard means integration, cases, or a longer derivation. Estimated time is for planning a strong prepared student's attempt, not measured examination timing. Another reviewer may reasonably change a tag. The source answer keys have not been comprehensively certified by this classification exercise.

Historical papers contain material outside, or ambiguous under, the stored 2026 syllabus. **22 questions** are flagged for historical/scope review, rather than silently used as current-topic targets. These include transport/mineral nutrition, digestion, environmental issues, detailed p-block chemistry, states of matter, solid state, polymers, metallurgy, surface chemistry, mathematical induction, heading-only linear programming, logic gates and Zener-diode detail. Some nitrogen-fixation content overlaps the retained Microbes in Human Welfare unit and needs item-specific review. These flags mean inspect the precise scope; they are not a claim that all related concepts are excluded.

All-year counts describe the archive. **2023–2026** is the recent comparison window: 239 questions, with current-scope denominators **58 Biology, 55 Chemistry, 59 Mathematics and 59 Physics** after the eight review flags in 2023. Older papers inform style and breadth. They are not given equal predictive force under a changed syllabus. Rebuild all counts with `python tools/iat/analyse_pyq.py`; complete tables are in [chapter-count appendix](iat_pyq_chapter_counts.md) and [machine-readable metrics](iat_pyq_metrics.json).

## Main patterns and weightage

| Subject | Recent current-scope leaders | Interpretation for mocks |
|---|---|---|
| Biology, n=58 | Genetics/evolution 12 (20.7%); human physiology 10 (17.2%); cell 7 (12.1%); biotechnology 6 (10.3%) | Give inheritance, mechanisms and experimental interpretation repeated attention; retain all ten broad biology units. |
| Chemistry, n=55 | Bonding 7 (12.7%); organic principles 6 (10.9%); coordination 5 (9.1%); carbonyl/carboxyl chemistry 5 (9.1%) | Connect bonding to inorganic reasoning and organic structure to reactions; maintain physical-chemistry calculations. |
| Mathematics, n=59 | Coordinate geometry, differentiation and integration 6 each (10.2% each); relations/functions 5 (8.5%); matrices and probability 4 each (6.8%) | Use calculus and algebra throughout the series, with genuine geometry coverage rather than only formula substitution. |
| Physics, n=59 | Electrostatics 6 (10.2%); work/energy 5 (8.5%); oscillations and ray optics 4 each (6.8%); rotation, thermodynamics, waves and induction 3 each (5.1%) | Mix mechanics with electricity, optics and modern physics; reward modelling, signs, graphs and conservation laws. |

These percentages describe questions in the specified window. For example, 12/58 genetics questions means about three per recent paper on average, **not** a 20.7% probability that an unseen question will be genetics. Four recent papers are a small sample. A one-question reclassification changes a subject share by roughly 1.7–1.8 percentage points.

Recent coarse primary Class 11/Class 12 counts under this taxonomy are Biology **33/27**, Chemistry **28/32**, Mathematics **28/32**, Physics **30/29**. They include the scope-review items and should not be confused with the scope-filtered chapter denominators above. They suggest broad coverage of both classes, not a fixed official 50:50 rule. Mathematics especially needs item-level remapping for a precise split: limits, functions, probability and differentiation have material in both classes, and functional equations may use Class 11 functions with Class 12 optimisation.

## Style, figures and distractors

The dominant-task coding is mutually exclusive. An organic structure question can also involve calculation; it is counted under the task doing most of the work, rather than once in every applicable category.

| Dominant task, recent window | Biology (60) | Chemistry (60) | Mathematics (60) | Physics (59) |
|---|---:|---:|---:|---:|
| Recall | 8 | 4 | 0 | 1 |
| Conceptual | 21 | 19 | 22 | 7 |
| Numerical | 5 | 12 | 37 | 31 |
| Table/match | 7 | 1 | 0 | 0 |
| Diagram/structure | 12 | 20 | 1 | 19 |
| Graph | 4 | 4 | 0 | 1 |
| Experiment | 3 | 0 | 0 | 0 |

Diagram/graph/table as the dominant task totals **23/60 Biology, 25/60 Chemistry, 1/60 Mathematics and 20/59 Physics**. These are task tags, not an exact inventory of every embedded illustration. Chemistry's count includes molecular structures naturally expressible in mhchem; it does not imply 20 separate raster figures per paper. Experimental reasoning can be conveyed in prose and is not restricted to the experiment tag.

Biology questions often ask which mechanism explains an observation, interpretation of a cross or pedigree, or the consequence of a controlled perturbation. Distractors interchange ploidy, generations, cause and effect, or conditional and unconditional probabilities. Numerical genetics questions need enough assumptions to avoid hidden sex, viability or phase ambiguities.

Chemistry moves between representations: structure, periodic reasoning, reagents, stoichiometry, equilibrium and plots. Plausible distractors use the wrong reaction selectivity, ignore an acid–base reaction before a buffer calculation, reverse a Nernst quotient, or confuse formal oxidation state with actual charge. Organic drawings must preserve bonds and stereochemistry. Typesetting a formula is preferable to an unnecessary picture.

Mathematics rewards domains, branch choices, symmetry, root location and counting constraints. Common traps are accepting an endpoint forbidden by a strict inequality, ignoring an inverse-trigonometric quadrant, averaging group variances without mean shifts, or counting “at least” instead of “exactly”. Coordinate geometry remains a series priority even when a particular test uses other geometry skills.

Physics frequently requires choosing the model before substituting: signed versus unsigned area, conservation of momentum versus energy, the circuit after a connection changes, or rms versus mean and real versus apparent power. Graphs and circuits must show every datum needed to solve them and must not reveal an intermediate answer.

## Difficulty and time

| Recent editorial tier | Biology | Chemistry | Mathematics | Physics |
|---|---:|---:|---:|---:|
| Easy | 12/60 | 9/60 | 9/60 | 5/59 |
| Medium | 39/60 | 38/60 | 38/60 | 31/59 |
| Hard | 9/60 | 13/60 | 13/60 | 23/59 |

Physics appears harder under this rubric, and 2024–2026 have more hard tags than 2023. This is a reviewer judgement affected by the acquired copies and task classification, not a statistically demonstrated rising difficulty trend. No empirical score distribution is available. Publish no predicted cut-off or score-to-rank conversion from these tags.

The OurMocks **9 easy / 39 medium / 12 hard** split is an editorial design target, not the observed distribution of every PYQ. Pilot subject splits are 3/9/3 in Biology and 2/10/3 in each other subject. Budget approximately 1.5 minutes for easy, 2–3 for medium, and 4–5 for hard questions, with time left for switching subjects and reviewing. The detailed pilot plan totals about 168 minutes; real timings need a human timed trial.

## Prediction translated into preparation priorities

Use three broad priorities rather than pretending to forecast exact questions:

1. **Recurring anchors:** genetics/cell/human physiology; bonding/organic principles/coordination/carbonyls; calculus/functions/matrices/probability/coordinate geometry; electrostatics/energy/oscillations/optics. Revisit these with different reasoning angles across tests.
2. **Rotating coverage:** every remaining explicitly listed syllabus family. A recent zero or low count does not justify removal, and larger broad units should not crowd out small but assessable topics.
3. **Scope hold:** historical or ambiguous content, pending an explicit current syllabus listing. Recheck the official 2027 notification before claiming 2027 compliance.

No numerical forecast is calibrated here. A defensible forecast model would need more clean yearly papers, independent tagging, a declared rule fixed before holdout testing, and back-testing on unseen years. The present output supports balanced preparation rather than a claim to know what will appear.

## Pilot decision and official pattern basis

The user explicitly instructed on 29 October 2026 to complete analysis and proceed with Test 1 plus a review PDF. That authorises this **provisional pilot** without another approval pause. It does not approve the pilot for students or authorise bulk Tests 2–25 before its standard is reviewed.

Official 2026 references: [IAT examination page](https://www.iiseradmission.in/pages/admission/iat.html) and [2026 Information Brochure](https://app.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf). The verified 2026 pattern is 60 single-correct questions, 15 per science, 180 minutes, +4/-1/0 and maximum 240. The brochure permits an on-screen non-programmable scientific calculator; personal calculators are not allowed. A 2027 brochure has not been verified. This corrects the old repository assumption that there is no calculator.

The pilot is original authored content, not selected or number-swapped PYQs. Fixed question and option order preserves image links. The companion [blueprint](iat.md) records its coverage, the remaining series plan and release conditions. The PDF separates questions, key and worked solutions for manual review.
