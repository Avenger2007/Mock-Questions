# Milestone 15 correction checkpoint — 3 November 2026

The canonical files `IISER/IAT TEST 1.json` and `IISER/IAT NEW TEST 2.json` through `15.json` contain the current corrected drafts. The TSVs here preserve individually written corrections, teaching blocks and syllabus anchors. They are authored text, mechanically applied without generating questions or shuffling answers. Historical `IISER/authoring/` rows predate these fixes.

Apply a correction from its canonical JSON first. Keep the corresponding row here consistent if using these scripts to reproduce the checkpoint. A rerun replaces the fields specified by those rows, so review the diff before retaining it.

```bash
python tools/iat/apply_milestone15_revisions.py
python tools/iat/apply_milestone15_teaching.py
python tools/iat/render_milestone15_figures.py
python tools/iat/sync_milestone15_metadata.py
python tools/iat/apply_milestone15_layout.py
```

The order matters: later follow-up rows resolve earlier drafts, teaching amendments extend worked solutions, and layout amendments are last. `replacement_application.json` records the authored replacement IDs; its application-time hashes are intermediate. The final hash manifest in `IISER/review/milestone15_fixes/` is authoritative for delivered files.

Re-run the structural validator, arithmetic probes and exporters after any content change. Historical assembly and slot-generation scripts now stop before overwriting corrected canonical content or revised planning records. Historical figure generators can also recreate old images: use the revised figure generator above for the 15 redrawn images and retain the other existing images.

These corrections resolve documented audit findings; they do not mark the bank academically approved. Independent hidden-key subject review and timed attempts remain pending. The original audit is retained unchanged under `IISER/audit/milestone_15/`.
