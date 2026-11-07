# IAT New Tests 16–17: authoring and review checkpoint

Finalised 5 November 2026 on branch iat-tests-16-17, based on the corrected Tests 1–15 checkpoint 1de7c68. These are original **review drafts**, with independent hidden-key subject review and timed attempts pending. The user's 4 November instruction authorised continued draft authoring after the milestone repairs; it did not turn the pending academic review into an approval.

## Delivered papers

Each paper has 60 single-correct questions, 15 per subject, 180 minutes, +4/-1/0 and 240 marks. Each retains the editorial 9 easy / 42 medium / 9 hard split and 15 selected answers per letter. Fixed IDs, final option order and image filenames must remain stable. The subject splits are:

| Paper | Biology E/M/H | Chemistry E/M/H | Mathematics E/M/H | Physics E/M/H | Purposeful images B/C/P |
|---|---|---|---|---|---|
| 16 | 2/10/3 | 2/11/2 | 2/11/2 | 3/10/2 | 2/4/4 |
| 17 | 3/10/2 | 2/10/3 | 2/11/2 | 2/11/2 | 2/3/4 |

Canonical JSON files are IISER/IAT NEW TEST 16.json and 17.json. Their byte-identical delivery copies, offline HTML, printable PDFs and hash checks use IAT_NEW_TEST_16 and IAT_NEW_TEST_17 stems in this directory. Both PDFs contain the question paper followed by 60 worked solutions. Exact final page counts, source hashes, image hashes and strict-expression counts are in tests16_17/final_manifest.json.

## How the milestone findings shaped these tests

All 120 items have explicit syllabus anchors and actual focus descriptions. Mathematical and physical calculations show governing equations, substitution, intermediate results and the final answer. WHY explains the model or evidence, and all three alternatives have separately labelled rebuttals. Numerical Chemistry uses displayed mole, electron or energy accounting. Conceptual Biology includes controls, event order and causal interpretation rather than only answer restatements.

Several reserved seeds were retired before authorship:

- Repeated exposed-ovule classification became pollen-mediated fertilisation without external water. Repeated competitive-inhibition curves became dynamic equilibrium demonstrated by isotopic exchange.
- Repeated chromosome/DNA questions became a comparison of replication with nuclear fusion at equal DNA mass. Repeated spindle arrest became reversible quiescence. Repeated disrupted antibiotic markers became physical linkage of an origin versus transient cell-level resistance.
- The circular forbidden-neighbour template became interacting separation and neighbour constraints. The line-pencil fixed-point task became a circle through two common intersection points and an extra point. Pooled variance became correction of a single observation with both raw moments changing.
- Telescoping and weighted arithmetic-geometric seeds became finite AP block reconstruction and a three-term AP-to-GP transformation. General-series convergence is not required.
- The entropy seed became a monatomic-gas P-V heat/work cycle, and the thin-film seed became successive polarisation projections. These replacements use explicitly listed syllabus families.
- Single-loop scaling became centre-field cancellation with a nonzero magnetic moment. End-pivot rod emf became two off-centre arm potentials. A repeated lens-mirror arrangement became a contact-lens doublet.
- Terminal-speed ratios became drag-direction reversal after an imposed upward velocity. A simple bridge temperature became coefficient inference plus actual source loading. Basic Lenz direction became nonzero open-circuit emf without sustained conduction.
- Repeated rectifier averages became a loaded two-reference diode clipper. Interference contrast ratios became interference recovered by common polarisation projection.

The chapter-family reservations remain intact; actual focus and task-style fields for all 120 slots were updated. Tests 18–25 retain 480 reserved items. Family counts are preparation choices and do not establish equal coverage of every subtopic.

## PYQ standard and scope

All 30 Mathematics items have individual comparisons to specific 2023–2026 ledger entries, with source PDF/page, actual deductions and estimated time. See tests16_17/math_pyq_calibration.json and the authored calibration TSV. Examples include absolute-value differentiability, constrained matrix entries, nearest points of spatial lines, finite binomial identities and transformed initial-value equations. These are task-demand comparisons, not copied stems or measured difficulty equivalence.

The [official examination page](https://www.iiseradmission.in/pages/admission/iat.html) and [2026 brochure](https://web.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf) were checked on 4 November. The stored 2026 syllabus remains the preparation basis; a 2027 brochure has not been verified. The papers therefore retain the provisional-year qualification. The acquired 2026 key is provisional, and its first-option convention is not used to infer official answer-letter distributions.

Quantitative models state the assumptions that affect their answers. The C3/C4 resource comparison in T17 Q04 is explicitly a simplified ATP/NADPH/carbon-loss model, not a complete physiological energy account. T16 Q07 corrects measured progeny for stated survival bias. T16 Q14 specifies whether initiation at the inhibitor's boundary time occurs. T17 Q09 excludes integration and molecular joining; T17 Q59 specifies ideal diodes and references able to source or absorb current.

## Repetition and option review

The whole-bank lexical screen covers all 17 papers. It finds no exact or number-masked identical stems. Three candidates involve a new paper:

| Pair | Editorial decision |
|---|---|
| T17 Q32 and T06 Q33 | Retain: rational versus cubic optimisation, with different derivative structure, feasible critical point and endpoint results. |
| T17 Q34 and T01 Q35 | Retain: polynomial division/logarithmic remainder versus a trigonometric symmetry integral. |
| T16 Q34 and T17 Q34 | Retain: complementary logarithmic reflection versus rational polynomial division. Similar evaluation wording does not imply the same object or method. |

The other candidates belong to the earlier bank and remain visible in the complete screen. A text threshold is supporting evidence, not proof of semantic originality. All 120 new task signatures preserve the full constraints, requested result, governing method and distractor mechanisms for later comparison.

Draft review also found an overly regular Test 16 answer pattern. Sixteen explicitly authored option corrections broke that cycle before finalisation, preserving every correct answer's content and every question/figure ID. Selected-content checks and labelled rebuttals were updated together. No random question or option shuffle was used. A T17 Q23 rebuttal was corrected to describe the actual alcohol-position/alkene error rather than incorrectly claiming loss of a carbon.

## Verification

- All 17 papers, 1,020 questions, pass the strengthened structural/design validator. The previous 900 canonical question records are byte-for-byte unchanged from the milestone-fix checkpoint.
- All 84 author-side calculation probes pass and bind to final source hashes and selected option contents. They include exact fractions, symbolic substitution, direct enumeration, numerical integration and representative branch/boundary cases. Boundary samples supplement the complete written proofs; they do not certify intervals by sampling alone.
- Both offline HTML files pass strict KaTeX/mhchem parsing. Browser layout was not tested; the browser dependency was unavailable.
- Both PDFs were rebuilt with XeLaTeX, with all 60 questions and 60 solutions detected, no empty pages, overfull-box warnings or missing-character warnings. Figure size was increased for readable labels. Final-exercise spacing keeps the last solution together.
- All 19 scientific rasters were inspected during authoring. All PDF pages were inspected as contact-sheet layout overviews, with detailed inspection of selected multi-stage solutions and the revised final pages. This is distinct from a fresh subject-expert reading of every rendered line.
- Final JSON, HTML, PDF and image checksums are recorded together. Delivery JSON is byte-identical to canonical JSON. The frozen authoring checkpoint prevents its assembler from overwriting later canonical corrections.

These checks do not establish empirical timing, item discrimination or independent scientific approval. The papers remain pending a separate subject reviewer solving with keys hidden and timed student attempts before student release. Errors found in that stage should be corrected at their existing IDs and re-exported, with evidence rebound to the new source hashes.

## Reproduction and continuation

Use canonical JSON for edits. The authoring TSVs are frozen evidence; the historical assembler is intentionally blocked by the checkpoint file. Run the structural validator and the calculation checker after a relevant change. Export from canonical JSON with the existing TeX exporter and offline HTML exporter, then run tools/iat/verify_tests_16_17.py. Python dependencies include SymPy, NumPy, Pillow and PyMuPDF; PDF export needs XeLaTeX with mhchem/chemgreek, while HTML uses KaTeX/mhchem and the configured Node dependencies.

The checkpoint and final commit are pushed to the named branch; main and earlier test branches are preserved. Continue from this branch and its continuity guide for Test 18. Save remote checkpoints before expensive rendering or review so an environment interruption cannot strand a full session's authorship.
