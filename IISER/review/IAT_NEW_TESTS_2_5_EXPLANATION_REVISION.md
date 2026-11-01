# Explanation revision: IAT New Tests 2–5 (1 November 2026)

Status: `pending_revision`. These four authored papers remain drafts for independent subject and timed-student review.

## Finding and changes

The prior audit confirmed the reader's concern: 115 of 120 Mathematics/Physics explanations had at most two labelled steps, 101 of 120 had a `Why` shorter than 20 words, and the four review PDFs reported no parsed math expressions. The explanations often gave a result in prose without a reproducible typeset calculation.

- Revised the `Why` and/or worked reasoning for all 240 items. Biology and Chemistry now trace the relevant observation or condition through the mechanism to the conclusion. Mathematics and Physics now have an explicit displayed `Worked derivation:` for every item, including items stored as conceptual, graph or diagram questions. Existing option-specific rebuttals remain.
- Strengthened `docs/instructions/IAT_Instructions.md` with an authoring gate and a release checklist. `validate_iat.py` now rejects new Mathematics/Physics items missing a worked display derivation. Word count alone is not a pass criterion.
- Regenerated the canonical delivery JSON, HTML, PDF and render-check files from the four source JSONs after the last explanation edit.

| Test | Questions/solutions | M/P derivations | `Why` words, min/median | PDF pages | Parsed math | Figures | Render overflow |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | 60/60 | 30/30 | 30 / 45.5 | 53 | 41 | 6 | 0 |
| 3 | 60/60 | 30/30 | 32 / 53.5 | 52 | 38 | 6 | 0 |
| 4 | 60/60 | 30/30 | 26 / 45.5 | 52 | 44 | 6 | 0 |
| 5 | 60/60 | 30/30 | 29 / 47 | 54 | 39 | 8 | 0 |

All four PDFs had no empty pages in text extraction; sampled solution pages from each rendered PDF showed legible display equations and no clipping. The validator passed the structural, key, figure and derivation checks. The series overlap screen is a text similarity diagnostic, not a semantic originality proof.

## Remaining academic review

The revised calculations and causal explanations need a second solver with the stored key hidden. Review each image against its stem, verify single-answer uniqueness and assumptions, and try the full paper under time before changing `pending_revision`. Mechanical checks and a sampled visual inspection do not certify every mathematical or scientific claim.
