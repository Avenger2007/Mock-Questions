# IAT Tests 1–15: milestone quality audit

**3 November 2026 · Source commit `56dd1acca318ce747a5f5c527951d7f12a38b8e0` · Decision: HOLD FOR REVISION**

The series meets its basic paper structure, but does **not yet meet the complete authoring standard**. Correct-looking keys, balanced letters and successful exports have concealed repeated questions, inflated difficulty labels, a syllabus breach, scientific-model problems and explanation defects. The earlier completion reports described structural success too broadly. Those reports should not be read as academic certification.

This audit changes no test, key, figure or PDF. It supplies evidence and a repair order. “Completed 15/25” currently means **900 authored draft items**, not 900 approved items.

## 1. What was actually audited

| Layer | Coverage in this audit | What it establishes |
|---|---|---|
| Structure, metadata, keys, images, explanation markers | All 900 items / 15 canonical JSON files | Compliance with the existing validator and additional diagnostics |
| Render provenance | All 15 existing render records; canonical/delivery/PDF hashes where recorded | No detected hash drift; not a fresh visual review of every PDF page |
| Mathematics editorial reading | All 225 stems, options and stored keys | Method, repeated task, obvious branch/option and difficulty screening; not a complete independent line-by-line verification of every solution |
| Hard-question editorial reading | All 135 hard-labelled stems/options across four subjects | Review of claimed demand against the written rubric |
| Answer re-solve | Seeded 10% sample: six items per paper, 90 total; seed 20261103 | Author-side derivation with separate resolution anchors; 88 agree with stored keys and two are held for model/ambiguity problems |
| Figures | 18 selected raster figures visually inspected | Specific scientific/teaching and presentation findings, not approval of all 118 figures |
| PYQs | Stored analysis and 539-entry ledger, 20 selected 2023–2026 Mathematics excerpts; original 2024 M2 and 2026 M1 pages inspected | Task-demand comparison with explicit examples; not a new certification of all PYQ keys |

The 90-item sample is reproducible in `random_sample_ids.json` and `sample_resolutions.tsv`. This is a review by the same assistant, not an independent subject expert. **88 agreements do not imply a 97.8% accuracy rate for the entire bank.** The two holds are not two simple wrong-letter findings. Unsampled answers remain uncertified.

## 2. What passes, and what the passes miss

All 15 papers pass `validate_iat.py`: 60 questions; 15 per subject; 180 minutes; +4/−1/0; 240 marks; declared 9 easy / 42 medium / 9 hard; 15 keys per letter; required fixed IDs and file links. There are 118 linked figures. Every paper meets the **file-count** minimum of two Biology, Chemistry and Physics images. No recorded source/delivery/PDF hash drift was found.

The official IAT 2026 page reconfirms those exam conditions. The 15/70/15 split and exact answer-letter balance are our editorial policies, not official exam quotas. No 2027 compliance is claimed.

The validator checks declared labels, literal option strings and heading presence. It cannot prove conceptual depth, scientific validity, mathematical equivalence of differently written options, meaningful image use, or originality. Its legacy Test 1 path also omits gates applied to NEW TEST files. All 30 Test 1 Mathematics/Physics explanations lack the later `Worked derivation` display block, although many already contain inline mathematics and substantive working. This is a migration gap, not evidence that all 30 answers are wrong.

## 3. Priority findings

| Priority / category | Exact evidence | Required action |
|---|---|---|
| P1 Scientific error | **T05 Q02** says pulmonary veins return oxygenated blood “from lungs and skin” to the left atrium. Pulmonary veins return lung blood; cutaneous return reaches the systemic venous/sinus-venosus route. The selected alternative and explanation conflate pathways. | Correct the alternative and explanation to lung return, and check every frog-circulation item. |
| P1 Invalid chemistry model | **T05 Q21** has 10 mmol carbonate in the aliquot and only 15 mmol HCl. Its forced single net equation produces the stored 0.33 g, but ordinary staged aqueous neutralisation first uses 10 mmol acid to make bicarbonate, then the remaining 5 mmol gives about **0.22 g CO2**, absent from the choices. | Rewrite the experiment/acid amount or supply the two-stage chemistry; do not simply change the key letter. Conditions such as addition and gas removal must be explicit. |
| P1 Ambiguous physical direction | **T11 Q14** says an “outward Na+ gradient” drives inward glucose through co-transport. It does not state inside/outside activities or membrane potential. Inward Na/glucose symport needs favourable inward sodium electrochemical flow. | State which side has high Na+, control voltage, and name symport/antiport consistently. Hold the present item rather than treating C as fully verified. |
| P1 Syllabus breach | **T14 Q41** needs convergence of a non-geometric power series and alternating-versus-harmonic endpoint tests. The stored syllabus lists finite/infinite geometric sums and finite special sums, not general power-series convergence or the alternating-series test. | Replace with a genuinely listed sequence/series task; preserve its ID and intended demand. |
| P1 Wrong distractor explanation | **T09 Q15** correctly selects D=2, but its “Why not” rebuts D, omits A, and maps the exponents incorrectly: square-root scaling gives 4 (A), three-quarter scaling gives 8 (B), direct scaling gives 16 (C). | Repair all three labelled rebuttals and scan the remaining explanations for this failure. |
| P2 Equivalent alternatives | **T04 Q38** lists A=3/8 and D=6/16. They are the same distractor. B=2/5 remains the correct conditional probability. | Replace one distractor; add numerical-equivalence checks. This is not a two-correct-answer case. |
| P2 Coverage metadata | **T14 Q37** tests bijectivity of x³+x but is tagged “Matrices & determinants”. | Retag to functions and restore the displaced matrix allocation elsewhere; recompute actual chapter coverage. |
| P2 Inconsistent source guidance | `iat_pyq_analysis.md` still calls 9/39/12 the OurMocks target, while current instructions and all authored papers use 9/42/9. | Version the obsolete target as historical and publish one current policy. |

Scientific references: [official IAT pattern](https://www.iiseradmission.in/pages/admission/iat.html); [IGNOU Chemistry Lab I, carbonate titration](https://egyankosh.ac.in/bitstream/123456789/53158/1/BCHCL-132%20E.pdf); [NCERT chemistry laboratory manual](https://www.ncert.nic.in/pdf/publication/sciencelaboratorymanuals/classXI/chemistry/kelm206.pdf); [primary anatomical study, frog cardiorespiratory system](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780167/). The carbonate value is the audit's stoichiometric inference from the two-stage model, not a quoted answer from a source. The frog correction concerns the item as written; it does not require adding advanced anatomy to the test.

## 4. Confirmed repetition: a series-level failure

The following are **15 manually identified repeated-task clusters involving 33 distinct items**. They are a lower bound, not the total number of repeats. Some preserve the exact calculation; others change only constants, names, output representation or one short follow-up. A shared chapter alone was not used to classify a repeat.

| Cluster | Question IDs | Why it breaches the distinct-angle rule |
|---|---|---|
| R01 | T04 Q35; T11 Q32 | Same implicit curve x²+xy+y²=7, same point (1,2), same requested tangent slope −4/5. |
| R02 | T04 Q34; T07 Q34 | Same area between y=x² and y=2x on the same intersections; answer 4/3. |
| R03 | T09 Q35; T13 Q34 | Same integral from 0 to pi of x sin x; adding an instruction to use symmetry does not create a new task. |
| R04 | T05 Q42; T15 Q40 | Same vector (1,2,2), same xy-plane and same sine of line-plane angle 2/3. |
| R05 | T02 Q35; T10 Q35 | Restricted inverse of a shifted square, domain x≥2, solve a squared displacement of 9; both return 5. |
| R06 | T03 Q41; T06 Q41 | Same telescoping summand 1/[k(k+2)]; only upper bound changes. |
| R07 | T04 Q43; T12 Q43 | Same monic quadratic with positive constant square; distinct positive roots reduce to positive coefficient above twice its square root. |
| R08 | T04 Q32; T09 Q44; T13 Q32 | Same linear pencil of lines; separate parameter and constant coefficients to find the fixed point. |
| R09 | T05 Q39; T10 Q39; T15 Q45 | Explicit quadratic partial sums; recover a selected term by S_n−S_(n−1), with numbers changed. |
| R10 | T01 Q38; T03 Q43; T09 Q38 | Same equal-group pooled variance task, changing means/variances. |
| R11 | T02 Q37; T13 Q37 | Same two-factory single-defective-item Bayes calculation with different priors/rates. |
| R12 | T03 Q17; T08 Q17 | Same high/low-spin octahedral d6 comparison and unpaired counts 4/0. |
| R13 | T07 Q08; T13 Q08 | Same booster/primary response comparison and memory-lymphocyte conclusion. |
| R14 | T08 Q22; T13 Q25 | Same cold diazonium coupling versus warm aqueous hydrolysis, same reason for different products. |
| R15 | T10 Q17; T15 Q17 | Same six monodentate versus three bidentate en-ligand comparison, asking the chelate-effect reason. |

Keep the strongest instance in each cluster and **review at least 18 later/other instances for replacement**; do not delete questions, shuffle options or renumber IDs. Choose replacements against the remaining ten-test plan so coverage is maintained. R07–R11 and R15 are editorial semantic judgements under our especially strict no-template rule; they are not claims of verbatim plagiarism.

The existing 0.78 overlap screen returned only seven candidate pairs and no exact or number-masked hits. It missed even R01–R04 because whole-sentence similarity is not mathematical equivalence. The additional conservative normalisation screen also found no exact full-stem matches. **A green text screen has demonstrably failed to establish originality.** Store method signatures: mathematical object, constraints, governing method, requested result and distractor mechanism. Use them to support human comparison.

## 5. Difficulty and PYQ calibration

The 135 hard labels were screened against the instruction's demand for several linked deductions, cases or a nonroutine model. The following 16 clear examples should be reclassified or substantively strengthened; this is an editorial judgement, not measured student difficulty:

| Subject | Current hard examples | Actual demand |
|---|---|---|
| Biology | T04 Q12; T07 Q08; T07 Q13; T12 Q11; T14 Q15; T15 Q07 | Standard conditional carrier fraction; memory recall; two cardiac products and a ratio; recombinant-frequency percentage; one power-law ratio; independence makes conditioning irrelevant. |
| Chemistry | T09 Q24; T12 Q18; T12 Q30; T13 Q25; T14 Q17 | Standard substituent acidity; octet count; directly stipulated SN2 inversion; familiar diazonium condition comparison; donor count and charge balance. |
| Physics | T04 Q55; T09 Q55; T12 Q49; T12 Q54; T15 Q55 | Inductor scaling; enclosed-charge sum; radius-squared Stokes scaling; constant-voltage capacitance scaling; three half-lives and subtraction. |

Other hard labels need judgement rather than automatic downgrade. For example, Test 1 Q44 really links focal-chord intersections, tangent intersection and triangle geometry; Test 9 Q43 needs discriminant and strict root-location conditions. Those are useful demand anchors.

Some medium Mathematics questions are also too routine for our rubric: T10 Q32 is a 3–4–5 chord triangle; T11 Q38 is one binomial coefficient; T14 Q35 is the elementary nonnegative square inverse; T15 Q42 is a single perpendicular-bisector locus. A fixed distribution of labels does not prove a fixed distribution of difficulty. Do not restore counts by changing another label without examining the actual task.

**Direct PYQ contrast:** the inspected 2024 Mathematics Q2 (PDF page 35) chains a perpendicular-bisector locus to a second point-versus-locus distance condition. T15 Q42 stops after the first locus while calling itself medium. The inspected 2026 Mathematics Q1 (PDF page 33) is itself a short quadratic-coefficient question. Therefore direct questions belong in an IAT paper; the finding is miscalibration and excessive routine demand, not a rule that every question must be difficult. Use the stored recent ledger to benchmark each revised item to a specific year/question and actual deduction count, not merely a chapter name.

No total revised easy/medium/hard distribution is asserted here. That requires retagging all 900 using one rubric, then timed student attempts. Current labels cannot support claims that Tests 9–15 are reliably deeper than Tests 1–8.

## 6. Explanations and typesetting

- The numerical solutions in newer papers are substantially better than bare answer statements. The sample's ordinary calculations mostly reproduce the selected results; a wholesale “all answers are wrong” verdict would be unsupported.
- **37 Test 1 explanations lack the current named Why and Why-not headings.** Many contain substantive Given/Principle/Step and Common mistake sections. Migrate them without discarding sound existing working.
- T09 Q14 and T10 Q39 have a single Why sentence. Review the reasoning quality, rather than padding word counts. T09 Q15 has the more serious incorrect option-label rebuttals described above.
- **69 Chemistry items are labelled numerical; 39 of those explanations have neither inline nor displayed delimited mathematics.** Only one Chemistry explanation in the whole corpus has a display block. Required structured calculations therefore remain inconsistently typeset, despite the Mathematics/Physics display gate passing for Tests 2–15.
- **85 of 135 hard-labelled items have at most one numbered Step.** This is a triage diagnostic, not 85 proven defective solutions: conceptual items need not have numbered steps, and a displayed derivation can contain several deductions. Inspect actual working before issuing item-level failures.
- The carbonate and frog examples show why a lengthy explanation can reinforce a wrong model. Two sentences and individual letter labels are necessary mechanical checks but insufficient teaching checks.

The stored JSON/PDF hashes match, which is good provenance. It does not certify teaching depth, valid chemistry, visual correctness, or adherence to every KaTeX/mhchem instruction. This audit did not rerender and inspect all pages of all 15 PDFs.

## 7. Figures and distractor quality

The 18 inspected figures include clear, usable examples: T03 Q07 preserves antiparallel DNA direction; T02 Q04 clearly compares CO2/light responses; T11 Q28 carries numerical freezing-point data; T11 Q49 gives an elastic endpoint for a modulus calculation.

Specific repair candidates:

- **T15 Q48:** the picture already draws the higher-left equilibrium water surface while the question asks which side rises. It supplies the intended conclusion and bypasses the effective-gravity reasoning. Show acceleration and an unspecified surface instead.
- **T05 Q28:** arbitrary “discharge preference” bars tell the student which species wins. They replace electrode-chemistry reasoning with reading the taller bar. Use real concentrations/conditions or an experimentally defensible observation, rather than invented preference units.
- **T09 Q03:** the inspected enzyme graph lacks conventional quantitative axes/scale labels while providing Km/Vmax in text and legend. It is interpretable, but does not meet the full graph specification.
- **T14 Q02:** the explanation claims whorl insertion points lie below the ovary; the planar diagram shows no longitudinal insertion geometry. The caption states “superior” instead. Add a genuine section and use distinct sepal/stamen symbols; both currently use S.
- **T14 Q27 and T15 Q24:** these are largely text in reaction-flow boxes, not molecular-structure drawings. Do not rely on them alone as evidence of visual scientific reasoning. Reassess meaningful-image counts after removing decorative or answer-supplying visuals.
- Tests 14–15 use abbreviated table entries in the image register, rather than the complete per-image specifications required by the instructions. Complete the size, axes, permitted labels and prohibited content for each.

The correct alternative is uniquely longest in 216/900 items. That count alone does **not** establish a length bias: it is close to one quarter, and ties/subject differences matter. Qualitative cue problems are clearer in T13 Q27 (the only scientifically detailed alternative against implausible distractors) and T15 Q24 (the detailed protection rationale against “destroy aromaticity”, “replace Br with Cl”, and “create a nitro group”). Replace implausible errors with mistakes a prepared student might actually make; do not merely equalise lengths.

## 8. Coverage, priorities and release decision

Broad chapter reservations are useful, but the authored metadata cannot yet prove balanced actual syllabus coverage. T14 Q37 already attributes functions to matrices. Retag from the actual solved content, then compare primary-topic counts with the current-scope PYQ ledger; retain the original planned code as a separate audit field. Broad chapter inclusion does not demonstrate subtopic coverage, and repeated methods consume nominal coverage slots without adding equal practice value.

Recommended repair order:

1. Hold release and pause new Test 16–17 authoring while the existing standard is repaired. Correct scientific validity, ambiguous premises, the syllabus breach and the wrong distractor explanations first.
2. Resolve the 15 documented repeat clusters, preserving one strong example each and replacing other instances at the same IDs. Extend semantic comparison to Biology, Chemistry and Physics beyond the examples found here.
3. Retag difficulty from actual reasoning, strengthen weak medium/hard items, and remap actual chapter/subtopic coverage. Keep exactly 9/42/9 only after content justifies it.
4. Finish Test 1's current-standard migration, Chemistry numerical typesetting, meaningful figures and full image-register specifications.
5. Rebuild affected PDFs; bind checks to final hashes; run scientific, equivalent-option, semantic-repeat and label-rebuttal review alongside schema checks.
6. Have independent subject reviewers solve the final 900 with keys hidden, then obtain timed attempts. Record approval at item level; do not replace it with a single blanket “passed” statement.

**Outcome:** preserve all 15 drafts and the good working already present, but do not advertise the bank as fully audited or official-standard approved. This report establishes concrete repair evidence, not a full 900-answer accuracy certificate. The remaining 10 tests should inherit the repaired process.

## Reproduction and evidence

Run `python tools/iat/audit_milestone_15.py` from the repository root. It performs read-only content checks and writes audit diagnostics; it does not author or modify questions. Run `python tools/iat/check_series_overlap.py --threshold 0.78` for the original lexical screen. Read `sample_resolutions.tsv` alongside the frozen source JSON for the 90 re-solves. `equivalent_numeric_options.json` records the conservative exact-rational duplicate check. Do not interpret diagnostic thresholds as academic verdicts.
