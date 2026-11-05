# IAT Test 1 manual-review package

**Latest authored checkpoint, 5 November 2026:** New Tests 18 and 19 add 120 review-draft items, 21 linked figures, detailed worked solutions and 85 source-bound calculation checks. Final delivery hashes and the complete 19-paper validation are in tests18_19/. See [review notes](IAT_NEW_TESTS_18_19_REVIEW_NOTES.md). The updated 25-test CSV and 640-entry syllabus checklist distinguish actual evidence from future coverage obligations. Independent academic and timed review remain pending.


**Current checkpoint, 3 November 2026:** The documented milestone fixes have been applied to canonical Tests 1–15 and all delivery JSON/HTML/PDF files regenerated. See [correction report](milestone15_fixes/CORRECTION_REPORT.md) and its final hash manifest. The audit below is historical evidence for the repair; the bank still awaits independent academic and timed review. Earlier notes, page counts and check files describe their dated snapshots unless replaced by current source-bound records.

**Milestone audit, 3 November 2026: HOLD FOR REVISION.** The Tests 1–15 audit at `../audit/milestone_15/AUDIT_REPORT.md` records 15 repeated-task clusters, scientific/model and syllabus issues, and difficulty/explanation gaps despite all papers passing structural checks. Consult that report and its evidence before further authoring or student release. No test content was changed by the audit.

## Fresh authored papers

`IISER/IAT NEW TEST 2.json` through `IISER/IAT NEW TEST 5.json` distinguish freshly authored papers from the uncommitted earlier drafts lost during a workspace reset. Their generated review files use `IAT_NEW_TEST_<N>` stems. Each remains `pending_revision` for independent academic and timed review. The new standard requires two purpose-built figures each in Biology, Chemistry and Physics and full explanations of all alternatives. Commits preserve drafts between sessions; a commit is not approval for student publication. See `IAT_NEW_TESTS_4_5_REVIEW_NOTES.md` for the item-level mathematics comparison and figure inventory, and `IAT_NEW_TESTS_2_5_EXPLANATION_REVISION.md` for the later detailed-solution revision and verification limits.

New Tests 6 through 9 are complete authored review drafts under the same provisional 2026 pattern. Their canonical source JSON, linked figures, delivery HTML/JSON/PDF and render checks are versioned together. See `IAT_NEW_TESTS_6_7_REVIEW_NOTES.md` and `IAT_NEW_TESTS_8_9_REVIEW_NOTES.md` for mathematics calibration, figure purpose, checks and remaining independent review.

Revised 30 October 2026. Status: `pending_revision`. This is an original 2027-preparation pilot using the verified 2026 pattern and stored syllabus; it is not an official paper or a claim of verified 2027 compliance.

The historical 19-page audit applies to `baseline/IAT_TEST_1_before_revision.json`, not this revision. See `IAT_TEST_1_Revision_Notes.md` for all 21 changed records, figure checks and remaining review requirements.

## Files

- `../IAT TEST 1.json`: canonical authored test. Never edit generated copies instead of this file.
- `IAT_TEST_1.json`: byte-identical delivery copy, generated with the PDF for convenient download.
- `IAT_TEST_1.pdf`: 55-page review paper: questions on pages 2–26, answer key on page 27, worked solutions on pages 28–55. Cover is page 1.
- `IAT_TEST_1.html`: self-contained HTML, with embedded diagrams and KaTeX fonts, generated from the canonical JSON.
- `IAT_TEST_1_render_check.json`: source/delivery/PDF/HTML/diagram SHA-256 checksums, math parsing and image/layout checks.
- `IAT_TEST_1_arithmetic_checks.json`: 68 arithmetic/enumeration probes with transcribed stem inputs. These are supporting checks, not independent academic certification.
- `IAT_TEST_1_validation.json`: structural validator results for this snapshot.
- `IAT_TEST_1_review_notes.md`: verification record, limits and questions for the human reviewer.

The paper has 60 questions, 15 in each of Biology, Chemistry, Mathematics and Physics; 180 minutes; +4/-1/0; 240 marks. Difficulty is editorial: 9 easy, 42 medium, 9 hard. Figures are linked to fixed IDs Q9, Q11, Q21, Q25, Q46, Q53, Q54 and Q57. No question or option shuffling is permitted. The 2026 brochure permits an on-screen scientific calculator, not a personal calculator.

The optional review ZIP includes this pilot, diagrams, analysis, blueprint, checks and reproduction scripts. It includes PYQ provenance metadata, but not the full source-PDF/page-image collection; those remain in the repository's separate `PYQ/IAT/` archive.

## Reproduce

Run from the repository root. Python dependencies: NumPy, Matplotlib and Pillow; PyMuPDF is useful for PDF visual inspection. Node dependencies: KaTeX and Playwright, plus a working Chromium installation. `IAT_NODE_MODULES` may point at an external directory containing those Node packages, avoiding changes to this repository's dependency setup.

```bash
python tools/iat/analyse_pyq.py
python tools/iat/draw_figures.py
python tools/iat/draw_revision_figures.py
python validate_iat.py
python tools/iat/check_pilot_arithmetic.py
IAT_NODE_MODULES=/path/to/node_modules IAT_BROWSER=/path/to/chromium node export_iat_review.mjs
```

Export does not author or shuffle questions. It parses every delimited expression with KaTeX/mhchem in strict error mode, loads all figures, checks for horizontal overflow and oversized question/solution blocks, then prints the review PDF and records checksums. Reinspect the rendered PDF after any content or layout change. If editing a skill-governed PDF artifact, follow that environment's PDF authoring-marker requirements separately.

## Manual review

Review all 60 keys and explanations, single-answer uniqueness, syllabus scope, distractor plausibility, diagram fidelity and a timed attempt. Difficulty labels and slot-time estimates have not been empirically calibrated after revision. Record corrections by stable question ID. Approve the pilot standard before authoring Tests 2–25. The blueprint reserves chapter slots for 25 tests; it does not claim that 1,500 exact question angles have already been planned.

New Tests 10 and 11 are authored review drafts. Their canonical JSON, figure sources and linked PNGs, delivery JSON/PDF and render checks are versioned together. The PDF review copies use `tools/iat/export_iat_review_tex.py` (XeLaTeX) because the earlier browser-render dependencies were not present in this restored workspace; see `IAT_NEW_TESTS_10_11_REVIEW_NOTES.md` for quality checks and remaining academic review.

IAT New Tests 12 and 13 are authored review drafts on `iat-tests-12-13`, with canonical JSON, linked figures, delivery JSON and PDF, and source-bound render checks. Each has 60 questions and detailed solutions; the figure minimum is exceeded in all three required subjects. See `IAT_NEW_TESTS_12_13_REVIEW_NOTES.md` for overlap decisions, item-level Mathematics checks, figure purpose and pending independent review.

IAT New Tests 14 and 15 are authored review drafts on `iat-tests-14-15`. Canonical JSON, original figure sources and PNGs, delivery JSON/PDF and render checks travel together. See `IAT_NEW_TESTS_14_15_REVIEW_NOTES.md` for repeated-angle replacements, item-level Mathematics checks, quantitative validation and the remaining academic/timed review.

## Tests 20–21, 5 November 2026

Canonical JSON and byte-identical review JSON, offline HTML and printable PDFs are available as `IAT_NEW_TEST_20` and `IAT_NEW_TEST_21`. See `IAT_NEW_TESTS_20_21_REVIEW_NOTES.md` and `tests20_21/final_manifest.json`. The authoring branch is local `iat-tests-20-21`; the supplied token was rejected by GitHub, so no successful remote checkpoint is claimed. Independent academic and timed review remain pending.
