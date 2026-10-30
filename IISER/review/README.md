# IAT Test 1 manual-review package

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
