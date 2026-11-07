# IAT New Tests 22–23: restored workspace and author-review checkpoint

Prepared 6 November 2026 on `iat-tests-22-23`, based on completed local checkpoint `ba94103947ecbe2eca9fa681cb13ee8eb255e1f2`. All 75 saved partial draft rows were restored; the batch now contains 120 individually authored questions. Both papers remain `pending_revision`. Independent hidden-key subject review and timed attempts are required before student release. No official 2027 notice has been verified: the stored official 2026 syllabus and 60-question/180-minute/+4,-1,0 pattern remain provisional preparation references.

## Deliverables and checks

Each paper contains 15 questions in each subject, 240 maximum marks, an editorial 9 easy / 42 medium / 9 hard split and 15 correct answers per letter. Subject difficulty counts follow their rotating reservations. No four consecutive keys or whole-paper short cycle is present. Difficulty and attempt times are editorial estimates, not measured performance.

| Test | Biology images | Chemistry images | Physics images | PDF pages |
|---|---:|---:|---:|---:|
| 22 | 2 | 2 | 4 | 39 |
| 23 | 2 | 3 | 4 | 42 |

Canonical JSON is `IISER/IAT NEW TEST 22.json` and `IISER/IAT NEW TEST 23.json`. Review JSON is byte-identical; offline HTML embeds figures and fonts. Both HTML files pass strict mathematical parsing. PDFs contain all 60 questions and 60 solutions. Renderer checks reject overfull lines, missing glyphs and pages containing only headers/footers. All page thumbnails, selected full-size derivations and changed scientific figures were inspected; the final two replacement pages were checked again after rebuilding. No clipping or orphan subject heading was observed. HTML browser layout was not checked.

Every explanation includes a causal WHY and labelled rebuttals of all three actual alternatives. Mathematics and Physics show givens, principles, numbered steps, worked equations and interpretation. Numerical Biology/Chemistry also include intermediate accounting. The 105 source-bound calculation probes include exact arithmetic, symbolic integration/differentiation, exhaustive relation/digit counting and literal correct-content checks. They are an author-check aid, not independent academic certification.

All 23 canonical papers pass structural validation: 1,380 questions. The previous 21 papers / 1,260 canonical questions are byte-unchanged from the base. `tests22_23/final_manifest.json`, calculation records, render checks and plan consistency records bind evidence to the final sources. Historical authoring TSVs and current canonical JSON hashes are frozen in `authoring/tests22_23_checkpoint.json`; the assembler refuses to overwrite later canonical corrections.

## PYQ calibration and repetition review

All 30 Mathematics questions have individual acquired 2024–2026 PYQ year/question/PDF-page comparisons in `tests22_23/math_pyq_calibration.json`. They compare task demand rather than copying source questions. Estimated minutes are not timed student results.

The final full-bank text screen compares 23 papers and reports 23 candidate pairs, with no exact or number-masked identical stems. Seven candidates involve this batch, all concerning short definite-integral syntax. T22 Q33 uses translation followed by two integration-by-parts terms; T23 Q35 identifies both minimum-function crossings and absolute-value zeros. Flagged earlier integrals use polynomial division, reflection, squared-sine substitution or half-angle rationalisation. These methods and requested deductions differ despite similar notation. Older-only flags remain outside this batch; this result is not a clean semantic-originality certificate for the entire series.

`nearest_wording_candidates.json` retains three earlier stems and explanations per new item, with source hashes. Raw term-frequency retrieval is an aid and can miss conceptual repeats. Direct author comparison rejected these drafts before freeze; fixed IDs, quotas and correct-content letters were preserved:

| ID | Retired angle | Final task |
|---|---|---|
| T22 Q16 | Dimer association particle balance, close to T14 Q26 | Dilution, donor masking and geometrical evidence distinguish intramolecular H bonding from a liquid network |
| T22 Q19 | Ethanal/ketone Tollens and iodoform inference, repeated from T12 Q21 | Choose ketone-to-methylene conditions compatible with a separate acid-sensitive acetal |
| T22 Q21 | Staged amine recovery | Track labelled amide carbon through Hofmann versus hydride reduction before deamination |
| T22 Q23 | Optical-background correction, close to T17 Q29 | Distinguish species disappearance from stoichiometrically normalised rate and product rise |
| T22 Q34 | Equivalence closure, close to T8 Q34 | Count symmetric/transitive nonreflexive relations using inactive elements and vacuous cases |
| T22 Q45 | Algebraically equivalent inverse-trig fold, close to T16 Q45 | Resolve two signed principal-value branches before summing inverse angles |
| T23 Q18 | Excited nitrogen occupancy, close to T19 Q18 | Infer 2s from an interior radial node and distinguish radial probability from nuclear density |
| T23 Q57 | Prism minimum deviation, close to T8 Q57 | Change surrounding index to remove total internal reflection with unchanged internal geometry |
| T23 Q60, first revision | Alpha/beta endpoint inversion, close to T1 Q55 | Rejected in favour of a mixture draft |
| T23 Q60, final revision | Two-isotope mixture, too close to T3 Q60/T12 Q60 | Condition exponential survival on an already surviving individual; distinguish half-life from a scheduled lifetime |

The edit log records these decisions and three explicit pre-freeze option exchanges with remapped rebuttals; no random shuffle or renumbering was used. Other recurring themes have different requested conclusions: mixed-substrate oxidation uses two balances; isotope combustion includes impure oxidant and leftover oxygen; telescope eyepiece translation changes angular magnification; a partial dielectric requires a fixed-charge energy derivative; a singular ODE requires the maximal initial-value interval as well as its minimum. Independent semantic review remains pending.

## Syllabus and remaining plan

The CSV and canonical TSV agree on all 1,500 core rows. All 1,380 authored question hashes match canonical stems, and all material-ledger source hashes match the final JSON. Tests 24–25 retain 120 future slots. No authored question has been promoted to independent scope approval.

The checklist contains 640 printed scope phrases: B163/C153/M116/P208. They include broad, overlapping and repeated wording and are not 640 independent facts. There are 291 entries with limited material-aspect evidence, supported by 316 question links; 349 retain future backstops. Zero entries are unallocated. The 376 wording-alignment flags require semantic review and are not 376 proven gaps. The largest future ownership load is 11 scope phrases; the author must resolve residual breadth before drafting rather than attaching disconnected facts to one item.

Mapping corrections distinguish d-block from s-block, aldehyde reactions from carboxylic-acid reactions and amine chemical behaviour from physical properties. Neutralisation enthalpy is mapped to reaction enthalpies rather than spontaneity. An ODE is not automatically evidence for logarithmic differentiation; a supplied magnetic force is not a Biot–Savart derivation; rolling is not automatically fixed-axis dynamics. RAAS is not claimed as every kidney/GI hormone. Donor doping alone is not evidence for intrinsic semiconductor classification. Test 24 P59 was revised to temperature-dependent carrier/band classification and intrinsic electron-hole equality versus mobility. These corrections update the cumulative plan without rewriting historical review reports or previous canonical tests.

Unlisted general power-series convergence, Doppler extensions, detailed deleted p-block material, Zener regulation and logic gates remain excluded. The heading-only Linear Programming ambiguity stays on hold. Full-syllabus completion is not certified by these ownership records.

## Persistence and next work

Commits are on `iat-tests-22-23`; main and earlier branches were not overwritten or deleted. GitHub rejected the old credential during this batch, so **the new branch has not been successfully pushed**. The remotely verified base remains `30d1c8fef0cba8641c38a27765254c15994484c2` on `iat-tests-18-19`. The downloadable recovery bundle preserves unpublished Tests 20–23 history and the review package includes the new deliverables. The credential was handled transiently outside the repository and was not stored in a remote URL.

Restore from the bundle or push this branch using working authentication before relying on remote recovery. Read this report, the current continuity file, instructions, actual earlier questions and the assigned scope phrases before starting Tests 24–25. Independent academic and timed review are still required for student release.
