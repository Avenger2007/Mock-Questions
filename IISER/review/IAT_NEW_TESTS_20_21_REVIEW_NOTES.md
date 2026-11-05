# IAT New Tests 20–21: author checks and delivery checkpoint

Prepared 5 November 2026 on local branch `iat-tests-20-21`, based on remotely verified commit `30d1c8fef0cba8641c38a27765254c15994484c2`. Both papers remain `pending_revision`: independent hidden-key academic review and timed student attempts are required before release. No verified 2027 brochure is claimed; the stored official 2026 syllabus and exam pattern remain the provisional basis.

## Contents and checks

Each paper has 60 questions, 15 per subject, 180 minutes, +4/-1/0 and 240 marks. Each has the editorial 9 easy / 42 medium / 9 hard split and 15 correct answers per letter, with no whole-paper short key cycle. These are design choices, not official difficulty quotas or measured difficulty.

| Paper | Biology figures | Chemistry figures | Physics figures | PDF pages |
|---|---:|---:|---:|---:|
| 20 | 2 | 2 | 4 | 41 |
| 21 | 2 | 3 | 2 | 38 |

Canonical sources are `IISER/IAT NEW TEST 20.json` and `IISER/IAT NEW TEST 21.json`; review JSON is byte-identical. Offline HTML embeds all figures and fonts and passes strict KaTeX/mhchem parsing. The PDFs contain all 60 questions and 60 worked solutions; the renderer rejects overfull boxes, missing glyphs and header/footer-only pages. All page thumbnails and selected full-size mathematical solutions were inspected. An orphan subject heading was found during review and fixed by reserving space before solution-section headings. HTML browser layout has not been checked.

Every explanation gives causal WHY and individually labelled rebuttals for the three actual wrong alternatives. Mathematics and Physics use stated givens, principles, numbered steps and displayed working, rather than English instructions to apply a formula. Numerical Chemistry and Biology also show intermediate accounting. The 86 source-bound calculation probes include exact rational arithmetic, symbolic integrals/derivatives, exhaustive arrangement enumeration and literal selected-content checks. Their scope is narrower than independent academic approval.

All 21 canonical papers pass structural validation (1,260 items). Tests 1–19, including their corrections, are byte-unchanged from the base commit. Hash-bound manifests cover new JSON, HTML, PDFs, figures and numerical evidence. All source files and fixed IDs are retained; final authoring snapshots are guarded against overwriting later canonical corrections.

## Originality and PYQ comparison

All 30 new Mathematics items have an individual year/question/PDF-page comparison in `tests20_21/math_pyq_calibration.json`. Comparisons concern reasoning demand and task type; estimated minutes are not measured attempt times. The acquired PYQs inform the level without supplying copied stems.

The full-bank text screen finds no exact or number-masked identical stems. Its three high-similarity pairs involving these papers concern T21 Q34 against earlier integral questions (T17 Q34, T18 Q34 and T01 Q35). The new half-angle rationalisation, earlier rational division, squared-sine substitution and reflection-weighted integral are distinct solution tasks. Common integral wording explains much of the similarity. A green text screen does not prove semantic originality.

The author inspected retrieved earlier stems and solutions and explicitly replaced high-risk drafts:

- T20 Q37 originally resembled T11 Q32 after swapping tangent direction and changing a coefficient. It now distinguishes a regular vertical point from a two-preimage self-intersection with perpendicular tangents.
- T20 Q43 originally reused the fixed quadratic in T14 Q42. It now combines coefficient-exchanged distinct polynomials with repeated-root structure.
- T20 Q44 originally inverted the midpoint-chord reconstruction used in T18 Q32. It now enumerates hyperbola-circle intersection pairs, excludes axis-parallel lines and measures the remaining diameters.
- T21 Q38 replaces a latent-common-cause proposal too close to T17 Q38 with a selection-table parameter that preserves conditional independence.
- T20 Q39 now asks a parameter difference: the limit value is necessary, whereas the original sum was already fixed by finiteness.

Retained recurring themes change the task: T20 Q27 contrasts buffer exhaustion with a surviving buffer, T20 Q29 combines free-ion activity with scaling an electrochemical reaction, T21 Q26 tracks two link-specific partial sugar hydrolyses, T21 Q54 changes charge-sharing subsystems in sequence, and T21 Q57 maximises capacitor voltage rather than current. The future T23 rod-impulse brief was retired because T21 Q48 now uses off-centre impulse energy partition. Its replacement concerns coupled rolling dynamics with an axle torque.

Explicit draft option exchanges were limited to named items and remapped all rebuttal labels. A local Biology ABCD drafting cycle was broken; no random shuffle or question renumbering occurred. Draft arithmetic alternatives were corrected to agree with solved results before freezing. The edit log records substantive replacements and placement corrections. Independent originality review remains pending.

## Scope decisions

The [IIT Kanpur SATHEE NCERT reproduction](https://sathee.iitk.ac.in/ncert-books/jee-ncert-books/jee-nb-che-12/chem-12-unit-8-the-d-and-f-block-elements/) explicitly places the detailed molecular-orbital explanation of permanganate colour beyond the chapter's scope. Therefore T21 Q18 was replaced with oxidation-state, d-electron and spin-only magnetic counting; the colour observation is only a counterexample to an invalid inference, not a charge-transfer mechanism question.

T21 Q60 uses atomic-to-nuclear electron-mass bookkeeping for positron-emission energetics, not an electron-capture requirement. T21 Q59 uses superposition and the field ratio of individual plane electromagnetic waves, not recall of the Poynting-vector formula. Explicitly supplied idealisations control the rod plastic plateau, cavity grounding sequence, glycosidic cleavage selectivity, fixed-pH solubility and ideal diode behaviour. General series convergence, Doppler extensions, detailed deleted p-block chemistry, Zener regulation and logic gates are absent.

## Plan and syllabus register

The CSV and TSV retain all 1,500 fixed slots. Tests 1–21 have actual item focuses and source-question hashes; Tests 22–25 retain 240 concrete reservations. The 640 printed syllabus phrases/sentences are not 640 disjoint facts. The register now records 143 explicit material-aspect evidence mappings, including the prior T19 displacement-current item; the other 497 phrases retain future coverage backstops. A material aspect does not certify that every fact under a broad official phrase is exhausted.

Unsupported former T20–21 assignments were moved to future owners rather than promoted to coverage. Examples include protist classification incorrectly owning algae/pteridophytes, respiratory volumes owning urine formation, and blastocyst defects owning angiosperm double fertilisation. The remaining 281 wording-alignment flags require semantic decisions; they are not 281 proven gaps. Electromagnetic-spectrum coverage now has an explicit future photoelectric-band brief at T25 Q58. No printed phrase is unallocated, but assignment alone does not prove complete coverage. Linear Programming remains on hold because it is a heading without specified subtopics in the stored syllabus.

The source-bound material ledger states the exact assessed aspect and preserves unresolved breadth. Remaining owners must be checked before each subsequent paper. CSV exports use exact workbook-cell round trips and LF line endings. The rebuild guard rejects silent overwrite of a manually edited plan CSV.

## Persistence and recovery

The authoring checkpoint is local commit `f43d33f`. GitHub rejected the previously supplied token with an invalid-credentials response. The token was used only through an echo-disabled transient environment and a temporary askpass helper outside the repository; it was not put in files, committed content or the remote URL. No successful remote checkpoint or final push is claimed. Main and earlier branches were not force-pushed, deleted or overwritten.

A downloadable package includes both papers, figures, plan, instructions, review evidence and an incremental Git recovery bundle. Clone the repository's `iat-tests-18-19` base, then fetch the included bundle's `iat-tests-20-21` branch and check it out to recover the local commits. Pushing the recovered branch requires working GitHub credentials with repository write access. Do not paste credentials into a remote URL or commit them.

## Reproduction

Run `python tools/iat/check_tests_20_21.py`, `python validate_iat.py 'IISER/IAT NEW TEST 20.json' 'IISER/IAT NEW TEST 21.json'`, and `python tools/iat/verify_tests_20_21.py`. SymPy is needed for the symbolic probes; NumPy/Matplotlib/Pillow produce the exact diagrams. The existing XeLaTeX exporter needs mhchem/chemgreek. HTML uses KaTeX/mhchem with `IAT_HTML_ONLY=1`; this does not assert browser-layout verification. Update plan metadata using `python tools/iat/update_series_plan.py`, then run `tools/iat/export_series_plan_csv.mjs` from a temporary folder linked to the primary runtime's artifact-tool dependencies with `IAT_REPO_ROOT` set. Do not rerun a frozen assembler over corrected canonical files.
