# IAT series: restart and repetition checks

The Git repository is the durable source of truth. Continue from the latest remote IAT branch, rather than an earlier scratch path or download link. Tests 1–17 are authored review drafts. The current branch is iat-tests-16-17, based on fix-iat-milestone-15; it includes all corrected earlier tests and the audit. The user authorised continuing draft authoring on 4 November while independent academic/timed review remains pending; that review is required before student release. Read the milestone correction report and IISER/review/IAT_NEW_TESTS_16_17_REVIEW_NOTES.md before preparing Test 18. Integrate newer main work without overwriting unrelated changes. Named branches preserve earlier commits unless explicitly deleted or force-pushed.

| Material | Versioned location | Use |
|---|---|---|
| Authoring standards | `docs/instructions/IAT_Instructions.md` | Pattern, detailed WHY, figure minimum, review gate |
| PYQ source inventory | `PYQ/IAT/manifest.json`, `PYQ/IAT/README.md`, `PYQ/IAT/md/`, `PYQ/IAT/pdf/` | Verify year, provenance and original task style |
| Tagged PYQ evidence | `docs/blueprints/iat_pyq_ledger.json`, `iat_pyq_analysis.md`, `iat_pyq_chapter_counts.md` | Chapter and reasoning-demand calibration |
| 25-test reservation | `docs/blueprints/iat_25_test_plan.md`, `iat_25_test_slots.tsv` | 1,500 IDs, chapter families, distinct angle seeds and authored status |
| Authored questions | `IISER/IAT TEST 1.json`, `IISER/IAT NEW TEST 2.json` through `IAT NEW TEST 17.json`, then subsequent papers | Compare actual stems, methods, traps, figures and solutions |
| Figures and review | `IISER/images/`, `IISER/IAT_images.md`, `IISER/review/` | Check image purpose and PDF output |

For each next paper: fetch the latest remote state; inspect the relevant 60 reservations against the entire authored corpus and PYQ ledger; write a distinct task and solution for every slot; update the slot's authored status and angle when it changes. Run `python validate_iat.py <new-paper.json>` and `python tools/iat/check_series_overlap.py` before a full editorial semantic comparison. The overlap screen flags exact, number-swapped and similar stems across papers, but does not catch reworded methods or identical traps reliably. A reviewer must compare *reasoning angle, data representation, conclusion and distractor mechanism* as well as wording. Same syllabus theme may recur; the question task should not.

Record replaced angles and item-level mathematics PYQ calibration in the paper's review notes. Render and inspect the PDF. Commit JSON, images, PDF, slot updates and notes together, push a named branch, and verify that its remote commit matches the local HEAD before ending each session. Do not mark a draft academically approved solely because structural checks or a push passed. If remote authentication fails, supply a downloadable backup and state clearly that the branch is not safely stored remotely.
