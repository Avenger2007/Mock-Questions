# COMEDK Tests 24 and 25 review

Each mock contains 180 single-answer questions in Physics, Chemistry and Mathematics, with 60 questions per section and a 180-minute mock clock. Each section uses 20 Class XI and 40 Class XII reservations from the [25-test plan](../../docs/blueprints/comedk_25_test_slots.csv) and the [official COMEDK UGET 2026 syllabus baseline](../SOURCES.md). Correct answers earn one mark. Incorrect and unattempted questions earn zero.

| Delivery check | Test 24 | Test 25 |
|---|---:|---:|
| Question paper pages | 35 | 35 |
| Worked solution pages | 37 | 36 |
| Original figures | 8 | 7 |
| Options compared with canonical JSON | 720 | 720 |
| Calculation and reasoning spot checks | 84 | 98 |

Screened the last 360 stems against Tests 1–23 and each other. Review of closest pairs led to revisions to the equilibrium of a beam, the time required for electrolysis, and integration when two endpoints move. The final scan found zero exact matches under punctuation and number normalisation for this batch. See the [scope and similarity ledger](test24_25_scope_and_similarity.csv) and the [angle register](../../docs/blueprints/comedk_angle_register.csv) for item-level records.

The [COMEDK past-paper analysis](../../docs/blueprints/comedk_pyq_analysis.md) uses sampled 2025 shifts and 2026 recalls for qualitative calibration. Test 24 Q024 uses a common scaling in a long solenoid. Test 25 Q026 combines the size and orientation of a plotted cycle, and Q136 checks a tied graphical optimum. The planned per-subject split of 9 easy, 39 medium and 12 hard remains an editorial target pending timed student attempts.

The four PDFs were compared with the canonical JSON for full question wording, answer order and worked explanations. All 15 figures were inspected in the question PDFs. The [series index](../series_index.json) contains the source, delivery and figure hashes.

The completed branch contains 25 papers and 4,500 canonical questions. Every question ID maps to its scheduled anchor, and the authored files collectively contain references to all 494 plan anchors. This verifies the mapping and file inventory across the series. The batch checks above apply to Tests 24 and 25.
