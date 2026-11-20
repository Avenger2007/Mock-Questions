# COMEDK Test 1 pilot review

Status: ready for pilot review. The baseline is COMEDK UGET 2026. The 180-minute clock, English PCM sections, one point per correct answer and no penalty follow the documented foundation. The class split and difficulty targets are editorial. Difficulty labels await independent timed calibration.

| Check | Result |
|---|---|
| Composition | 180 original authoring rows, 60 per subject. Each subject has 20 Class XI, 40 Class XII and 9 easy, 39 medium, 12 hard reservations. |
| Options and answer order | Four choices per item, 15 of each correct letter in each subject and no sequence longer than three. Every PDF answer letter matches canonical JSON. |
| Explanations | Each answer gives the reasoning or calculation and separately addresses the three distractors. Equations are rendered as Unicode/plain mathematical text. |
| Diagrams | Four data-bearing visuals. The figure pages were inspected after correcting an image scaling issue. |
| Scope and overlap | 180 source-page mappings. Normalised stems within the paper and high-similarity matches against 2,445 indexed IAT, NEST and CUET PCM items were screened. Several same-task matches were replaced, including drift-speed ratio, isothermal mixture pressure arithmetic, ozone formal charges and a repeated monotonicity form. This records the historical pilot check. Subsequent COMEDK comparison uses the COMEDK mock series and COMEDK PYQs. |
| Delivery | The two PDFs preserve every item in sequence. The questions PDF contains 720 options. Delivery JSON is byte-identical to canonical JSON. The series index records hashes for the canonical file, delivery files and visuals. |

The [comparison ledger](test01_scope_and_similarity.csv) links each question to its assigned syllabus anchor, source page, final item hash and nearest indexed wording match. Nearest wording is a review lead. Overlap in shared concepts is expected. The two separate reaction-rate and relation tables retain the information needed to solve their items. The reserved series plan stays available as its initial baseline.

## Calibration for Tests 2 and 3

A desk spot check found uneven demands among questions labelled hard. Q075 in Chemistry needs carbon counting and functional-group recognition and is likely easy for a prepared candidate. Q144 in Mathematics can be settled by one inverse-matrix argument and is likely medium. Q093 in Chemistry requires both a sign decision and stoichiometric scaling, a stronger candidate for the hard tier. These are provisional judgments based on the shortest valid solutions. Use them to tighten the selection of hard slots in Tests 2 and 3.

Draft Tests 2 and 3 as one batch with a checkpoint after Test 2. Estimated effort can guide this batch while a fresh, independent student attempt is pending. Report only candidate observations as measured timing. See the [series blueprint](../../docs/blueprints/comedk.md) for the review procedure.
