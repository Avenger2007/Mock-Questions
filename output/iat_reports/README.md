# IAT analysis and audit reports

Prepared 29 October 2026.

- `../pdf/IAT_PYQ_Analysis_Student_Guide.pdf`: 14-page guide for Class 12 students. Includes ten quantitative charts: corpus coverage, five subject/chapter charts, recurrence heatmap, task mix, difficulty and approximate class split. Historical/current-scope denominators and forecast limits are explicit.
- `../pdf/IAT_Test_1_Full_Audit.pdf`: 19-page self-audit against the PYQ evidence, official 2026 structure and OurMocks rules. Includes seven comparison/distribution charts, reproductions and checks of all six scientific figures, and individual findings for all 60 questions.
- `IAT_Test_1_Audit_Data.json`: all item comments, comparable manual task recoding, proposed difficulty tiers and audited-file SHA-256 values.
- `verification.json`: page counts, output hashes, text-margin and count checks. All 33 pages were rendered and visually inspected; full-size checks covered the dense charts, diagram pages and item tables.
- `assets/`: reproducible chart images embedded in the reports.

Rebuild from the repository root with `python tools/iat/build_analysis_reports.py`. Dependencies: NumPy, Matplotlib, ReportLab, Pillow and DejaVu fonts. PyMuPDF was used for PDF verification. If working under the PDF skill, run its required authoring marker before the first creation/edit command for a new operation; this report operation used expected output count two.

The canonical Test 1 JSON, original review PDF and six diagram PNGs were not changed by this audit. Proposed tier changes and content improvements are recommendations, not silently applied revisions. The overall conclusion is to revise before final student release. The reports do not claim independent academic certification, calibrated difficulty, target-year notification compliance or next-paper probabilities.
