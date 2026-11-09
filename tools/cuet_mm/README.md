# CUET Mass Media authoring tools

These follow the same workflow as `tools/cuet_geo`. Run everything from the repo root.

1. Write `tools/cuet_mm/drafts/mmNN.txt`. The pilot, `drafts/mm01.txt`, shows the format.
   - `%P UNIT` starts the case: an original case scenario, with 5 linked questions in format `p`.
   - `@@ UNIT|sub_topic|e/m/h|fmt|ANS|targets` starts a question.
     - **UNIT** is M1–M8, the eight syllabus units. See `units.py` and the blueprint `docs/blueprints/mass_media.md`.
     - **fmt** is `d` direct (this includes fill-in-the-blank and "identify the incorrect pair"), `p` case set, `q` sequence, `m` match-list or `s` statements.
     - **targets** are comma-separated answer-fact keys for the unit's ledger in `docs/blueprints/mass_media_coverage.md`. Use `M2:x,y` to file a key under another unit. Never use `;` or `:` inside a key.
   - Option lines are written `A) …`. A line containing only `=` starts the explanation, which runs Why → Why not the others → Key point. The `Answer:` line is generated.
2. `python3 tools/cuet_mm/mm_conv.py tools/cuet_mm/drafts/mmNN.txt tools/cuet_mm/drafts/mmNN.json`
3. `python3 tools/cuet_mm/mm_check.py tools/cuet_mm/drafts/mmNN.json` reports:
   - counts, the answer key and unit quotas (QUOTA if a unit is more than 1 off)
   - LONGEST: the correct option is clearly the longest
   - SEQ-ABCD: a sequence answer in A, B, C, D order
   - DUPOPT: duplicate options
   - NO-TARGET: an item with no answer-fact key
   - REPEAT-TARGET: a fact already used twice in the series
   - OVERLAP: the sub-topic or stem is too close to an earlier test
4. `python3 tools/cuet_mm/relabel_match.py drafts/mmNN.txt 'sub_topic' II,IV,I,III` renames the List-II numerals of one match item (in the list, the options and the explanation). Use it so that no two match items in a test share an answer pattern.
5. `tools/cuet_mm/mm_ship.sh N "feat(mass-media): revise Test N to CUET 2027 standard (case theme)"` builds, shuffles, validates, marks the ledgers, commits and pushes.

`patch_item.py` fixes one item in both the draft and the shipped test. `reindex_series.py "CUET/Mass Media"` refreshes `series_index.json`.
