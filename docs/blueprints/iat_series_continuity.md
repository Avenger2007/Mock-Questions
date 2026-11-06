# IAT series: restart and repetition checks

The Git repository is the project source of truth. **Remote preservation remains blocked:** GitHub rejected the previously supplied credential during this batch. The remotely verified base is `30d1c8fef0cba8641c38a27765254c15994484c2` on `iat-tests-18-19`; Tests 20–23 have local commits and must be recovered from the download bundle or pushed with working credentials. Do not assume that a local commit is on GitHub.

Tests 1–23 are authored review drafts. The current branch is `iat-tests-22-23`, based on the completed local Tests 20–21 checkpoint `ba94103947ecbe2eca9fa681cb13ee8eb255e1f2`. It preserves all 1,260 earlier canonical questions byte-for-byte. The next papers are Tests 24 and 25. Read `IISER/review/IAT_NEW_TESTS_22_23_REVIEW_NOTES.md`, the updated CSV/TSV plan, assigned syllabus entries and future-angle register before drafting. Independent academic and timed review remain required before student release. The recovery bundle includes unpublished Tests 20–23 history. No branch was deleted or force-pushed; main and earlier named branches remain intact.

| Material | Versioned location | Use |
|---|---|---|
| Authoring standards | `docs/instructions/IAT_Instructions.md` | Pattern, detailed WHY, figure minimum, review gate |
| PYQ source inventory | `PYQ/IAT/manifest.json`, `PYQ/IAT/README.md`, `PYQ/IAT/md/`, `PYQ/IAT/pdf/` | Verify year, provenance and original task style |
| Tagged PYQ evidence | `docs/blueprints/iat_pyq_ledger.json`, `iat_pyq_analysis.md`, `iat_pyq_chapter_counts.md` | Chapter and reasoning-demand calibration |
| 25-test reservation | `docs/blueprints/iat_25_test_plan.md`, `iat_25_test_slots.tsv` | 1,500 IDs, chapter families, distinct angle seeds and authored status |
| Authored questions | `IISER/IAT TEST 1.json`, `IISER/IAT NEW TEST 2.json` through `IAT NEW TEST 23.json`, then subsequent papers | Compare actual stems, methods, traps, figures and solutions |
| Figures and review | `IISER/images/`, `IISER/IAT_images.md`, `IISER/review/` | Check image purpose and PDF output |

For each next paper: fetch the latest remote state; inspect the relevant 60 reservations against the entire authored corpus and PYQ ledger; write a distinct task and solution for every slot; update the slot's authored status and angle when it changes. Run `python validate_iat.py <new-paper.json>` and `python tools/iat/check_series_overlap.py` before a full editorial semantic comparison. The overlap screen flags exact, number-swapped and similar stems across papers, but does not catch reworded methods or identical traps reliably. A reviewer must compare *reasoning angle, data representation, conclusion and distractor mechanism* as well as wording. Same syllabus theme may recur; the question task should not.

Record replaced angles and item-level mathematics PYQ calibration in the paper's review notes. Render and inspect the PDF. Commit JSON, images, PDF, slot updates and notes together, push a named branch, and verify that its remote commit matches the local HEAD before ending each session. Do not mark a draft academically approved solely because structural checks or a push passed. If remote authentication fails, supply a downloadable backup and state clearly that the branch is not safely stored remotely.

The new public plan views are docs/blueprints/iat_25_test_plan.csv and iat_syllabus_coverage.csv. Core rows mirror the TSV; review manual CSV edits before rebuilding. Future coverage backstops must be closed with actual question evidence or a revised brief, never an automatic status promotion.
