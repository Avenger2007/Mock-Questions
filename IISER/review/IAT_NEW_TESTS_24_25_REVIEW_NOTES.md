# IAT New Tests 24–25: final authoring batch and review checkpoint

Prepared 6 November 2026 on `iat-tests-24-25`, based on `a46c8f180273d2bc44f7be27eb125873d97a2807`. Tests 1–25 are now authored review drafts: 1,500 questions, equally divided among the four subjects. This completes draft authoring, not academic approval or a certified exhaustive syllabus audit. All papers remain `pending_revision` until independent hidden-key subject review and timed attempts are complete.

The official 2026 exam and syllabus pages were rechecked on 6 November. No target-year 2027 notification was verified. The stored official 2026 syllabus and 60-question, 180-minute, +4/−1/0 pattern remain the provisional preparation basis. Sources: https://www.iiseradmission.in/pages/admission/iat.html and https://www.iiseradmission.in/pages/admission/syllabus.html . Historical PYQs do not authorise deleted scope.

## New papers and verification

| Test | Biology figures | Chemistry figures | Physics figures | PDF pages | Strict HTML math expressions |
|---|---:|---:|---:|---:|---:|
| 24 | 3 | 3 | 3 | 43 | 112 |
| 25 | 2 | 3 | 4 | 44 | 110 |

Each paper has 60 items, 15 per subject, 240 marks and the editorial 9 easy / 42 medium / 9 hard split. The rotating subject quotas are preserved. Each answer letter occurs 15 times per paper and three or four times per subject. No four consecutive identical letters or whole-paper short cycle is present. These difficulty labels and planned minutes are editorial judgements, not observed student performance.

Canonical files are `IISER/IAT NEW TEST 24.json` and `IISER/IAT NEW TEST 25.json`. Review JSON is byte-identical. Each PDF contains the question paper, answer key and all 60 worked explanations; HTML embeds figures and fonts. Every Mathematics/Physics solution includes givens, principles, numbered steps, displayed derivation, causal WHY and individually labelled distractor analysis. Numerical Chemistry and Biology include the necessary intermediate accounting, even when their format is a graph or diagram. No answer is certified merely by the presence of these headings.

All 25 papers pass structural validation. The previous 23 canonical JSONs / 1,380 questions are byte-unchanged from the base. All 127 author-entered calculation and enumeration probes pass. These include symbolic derivatives, integrals and composition identities; exhaustive dice, commuting-map, stopping-rule and committee counts; and electrical, thermal, mechanical and stoichiometric balances. The probes check selected content and bind their report to source hashes; they are not a complete scientific proof of every factual claim.

Both PDFs pass the renderer's zero-overflow, missing-glyph and empty-body-page checks. All page thumbnails and selected full-size mathematical pages were inspected; changed final solution pages were inspected again after rebuilding. Figures were checked for geometry, connectivity, labels, polarity and scope. A long chemical name caused one overfull line during drafting and was replaced with an equivalent readable name. The final PDFs have no observed clipping, collisions or orphan subject headings. Strict KaTeX/mhchem parsing passed for both HTML files; browser layout was not tested.

`tests24_25/final_manifest.json`, `calculation_checks.json`, render/HTML records, `visual_review.json` and `plan_consistency.json` bind the checks to the final sources. `authoring/tests24_25_checkpoint.json` freezes the eight historical TSVs and two canonical JSON hashes. The assembler's nonmutating refusal after freeze was tested. Subsequent corrections must begin with canonical JSON and regenerate affected views.

## PYQ demand and originality

All 30 Mathematics items have explicit acquired 2024–2026 PYQ year/question/PDF-page comparisons in `tests24_25/math_pyq_calibration.json`. The comparisons identify relevant task demand and explain how the new object or constraint differs; they do not copy stems or claim measured attempt times. Examples include translated-conic reconstruction, exceptional parameter limits, finite symmetry quotients, a signed GP branch, a one-point integral redefinition, a matrix nilpotent component and a finite commuting-map constraint.

The entire earlier bank's subject focus records were read, with direct stem/solution comparisons for high-risk matches and fresh three-candidate retrieval records for all 120 new items. The final full-bank text screen reports 23 older-only candidates, no new-batch threshold candidates and no exact or number-masked identical stems. Its hashes are retained in `tests24_25/series_overlap.json`. Text screening does not detect every shared reasoning task, and the older-only flags have not been independently re-audited during this batch. The new author comparison is not an independent semantic-originality certificate.

Original reservations were changed where they risked duplication or did not fit exact scope:

- T24 B2 and T25 B2 replace recent tissue-comparison angles with stomatal specialisation and three root-modification origins respectively.
- T24 C16 replaces another molecular-ion removal comparison with the C2 MO distinction between total bond order and occupied 2p sigma character.
- T24 C17 replaces another linkage-isomer question with EDTA denticity, charge and the limits of colour evidence.
- T24 C24 uses chloroform oxidation/storage chemistry; T24 C25 contrasts Reimer–Tiemann formylation with Kolbe carboxylation instead of repeating Williamson reagent reversal.
- T24 C26 now assesses chemical hormone classes; T24 C27 uses an amphiprotic ion instead of repeating the Test 22 weak-acid/weak-base salt calculation.
- T25 C19 contrasts a quantised photon absorption with an electron-impact energy transfer. C24 separates Arrhenius slope from prefactor; C25 uses tracer exchange at dynamic equilibrium; C28 uses conserved masses and non-additive measured volume; C30 separates physical branching effects from reaction rate.
- T25 M39's reserved “exactly two matches” task was rejected because T1 Q40 already uses that problem. The final committee counts one complete and two partial couples.
- T24 P51 uses buoyant restoring stiffness and finite immersion boundaries instead of another force-removal oscillator. T25 P60 uses the torque-sign product of an AC generator instead of repeating a translating-rod heating calculation.
- T24 P47's statistical measurement-error draft was rejected at strict scope review: the printed Units syllabus explicitly lists SI, significant figures and dimensions, but not that error-propagation subtopic. The replacement tests dimensionless arguments, additive power dimensions and the limits of dimensional inference.
- T25 B3 and B8 were strengthened during hard-tier review: protein-tag access uses an intact-versus-detergent control, while antibody removal and add-back separate specific serum blockade from broad phagocyte ingestion.

Retained recurring themes have different targets: T24 B13 aligns ECG with mechanical pressure crossings rather than asking valve state alone; C28 compares simultaneous temperature, composition and partial-pressure changes; M35 checks a three-cycle rather than reconstructing an involution; P58 adds parallel current phasors rather than a series voltage polygon; T25 P56 compares two constrained equal-load-power branches instead of maximising output power. A same-theme match remains a subject-review obligation.

The full original-to-authored angle reconciliation is recorded for all 120 slots. Five explicit pre-freeze option exchanges preserve solved contents and remap their answer and rebuttal labels. No random shuffle or question renumbering was used.

## Completed plan and honest scope accounting

The CSV and TSV agree on all 1,500 core rows, and each authored stem hash matches its canonical JSON. IDs, subject totals and broad chapter-family allocations are preserved. The series index now lists all 25 papers rather than only the original pilot. There are no future test slots. The older literal angle register is retained as pre-authoring history and is no longer used to overwrite authored focuses.

The scope checklist has the same 640 printed entries: B163/C153/M116/P208. Broad, overlapping and repeated phrases are retained, not relabelled as 640 independent facts. The cumulative explicit ledger has 544 source-bound links covering material aspects of 412 entries. **228 entries still lack explicit material-evidence mapping.** This is incomplete evidence accounting, not proof that 228 topics are absent from the existing questions. Some earlier papers may already assess them; that must be demonstrated from their actual tasks. Conversely, an aspect mapping does not prove every detail of a broad phrase has been tested.

The former blanket future assignments were not promoted to “covered” merely because the last tests were written. Unresolved entries now have blank active owners, retain their prior reserved owner for traceability, and specify an actual whole-bank evidence review or a fixed-ID revision if a real gap is found. `scope_evidence_unresolved.json` makes those obligations inspectable. Examples requiring explicit reconciliation include inflorescences, micturition, selected gastrointestinal hormones, some named applications and physical properties, and some detailed mathematical/physical scope phrases. These are review examples, not newly certified content gaps.

Do not advertise complete corner-by-corner syllabus coverage or student release based on the 25/25 authoring milestone. Review unresolved entries against all actual Tests 1–25, assess residual breadth in mapped phrases, audit semantic overlap, and obtain independent academic/timed evidence. General power-series convergence, Doppler extensions, detailed deleted p-block content, Zener regulation and logic gates remain excluded; the heading-only Linear Programming ambiguity remains on hold.

## Persistence

**Update, 7 November 2026:** The ordinary push succeeded and GitHub matched content checkpoint `ba97e4b5abad20e6ad5e8539ce3be8608d6c880c` on `iat-tests-24-25`. All previously local Tests 20–25 history is now stored on this branch. See `tests24_25/remote_preservation.json`. The failures below describe the earlier 6 November checkpoint, not the current remote status. Academic release and scope-evidence limitations above are unchanged.

Draft checkpoints and final deliverables are committed on `iat-tests-24-25`; main and earlier branches are not overwritten, deleted or force-pushed. A clean-URL noninteractive push was attempted and failed because no working GitHub authentication was available (`could not read Username; terminal prompts disabled`). The previously supplied token had already been rejected in the preceding batch. No credential was written into repository files or a remote URL.

At that earlier checkpoint the new branch was local only. The recovery bundle includes unpublished Tests 20–25 history since remotely verified base `30d1c8fef0cba8641c38a27765254c15994484c2`. Preserve the downloadable review package and bundle until an authenticated push is verified. A local commit or successful bundle check is not a successful GitHub push.
