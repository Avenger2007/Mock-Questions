# IAT series: restart and repetition checks

The Git repository is the durable source of truth. Continue from the latest remote IAT branch, rather than a prior session's scratch path or download link. Tests 1–15 are authored review drafts. The correction checkpoint is on `fix-iat-milestone-15`, which includes Test 14–15 and the milestone audit; fetch that branch before continuing. Read `IISER/review/milestone15_fixes/CORRECTION_REPORT.md` and resolve remaining academic/timed review before starting Test 16–17. Integrate any newer work on `main` without overwriting unrelated changes. Named test branches preserve earlier commits unless explicitly deleted or force-pushed; new work belongs on a new branch.

| Material | Versioned location | Use |
|---|---|---|
| Authoring standards | `docs/instructions/IAT_Instructions.md` | Pattern, detailed WHY, figure minimum, review gate |
| PYQ source inventory | `PYQ/IAT/manifest.json`, `PYQ/IAT/README.md`, `PYQ/IAT/md/`, `PYQ/IAT/pdf/` | Verify year, provenance and original task style |
| Tagged PYQ evidence | `docs/blueprints/iat_pyq_ledger.json`, `iat_pyq_analysis.md`, `iat_pyq_chapter_counts.md` | Chapter and reasoning-demand calibration |
| 25-test reservation | `docs/blueprints/iat_25_test_plan.md`, `iat_25_test_slots.tsv` | 1,500 IDs, chapter families, distinct angle seeds and authored status |
| Authored questions | `IISER/IAT TEST 1.json`, `IISER/IAT NEW TEST 2.json` through `IAT NEW TEST 15.json`, then subsequent papers | Compare actual stems, methods, traps, figures and solutions |
| Figures and review | `IISER/images/`, `IISER/IAT_images.md`, `IISER/review/` | Check image purpose and PDF output |

For each next paper: fetch the latest remote state; inspect the relevant 60 reservations against the entire authored corpus and PYQ ledger; write a distinct task and solution for every slot; update the slot's authored status and angle when it changes. Run `python validate_iat.py <new-paper.json>` and `python tools/iat/check_series_overlap.py` before a full editorial semantic comparison. The overlap screen flags exact, number-swapped and similar stems across papers, but does not catch reworded methods or identical traps reliably. A reviewer must compare *reasoning angle, data representation, conclusion and distractor mechanism* as well as wording. Same syllabus theme may recur; the question task should not.

Record replaced angles and item-level mathematics PYQ calibration in the paper's review notes. Render and inspect the PDF. Commit JSON, images, PDF, slot updates and notes together, push a named branch, and verify that its remote commit matches the local HEAD before ending each session. Do not mark a draft academically approved solely because structural checks or a push passed. If remote authentication fails, supply a downloadable backup and state clearly that the branch is not safely stored remotely.
