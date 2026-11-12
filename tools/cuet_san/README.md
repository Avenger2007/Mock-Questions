# CUET Sanskrit authoring tools

These follow the same workflow as `tools/cuet_pol`. Run everything from the repo root.

1. Write `tools/cuet_san/drafts/sanNN.txt`. The pilot, `drafts/san01.txt`, shows the format.
   - `%P P` starts the unseen passage, an original Sanskrit prose passage. Its 5 questions use format `p` and are tagged with the unit they test (S7 ×2, S1, S5, and S3 or S4).
   - `@@ UNIT|sub_topic|e/m/h|fmt|ANS|targets` starts a question.
     - **UNIT** is S1–S10, the ten syllabus units. See `units.py` and the blueprint `docs/blueprints/sanskrit.md`.
     - **fmt** is `d` direct (this includes fill-in-the-blank), `p` passage, `q` order, `m` match-list or `s` multi-select / statements.
     - **targets** are comma-separated Latin answer-fact keys for the unit's ledger in `docs/blueprints/sanskrit_coverage.md`. Never use `;` or `:` inside a key.
   - Questions are in Sanskrit; explanations are in Hindi. Option lines are written `A) …`. A line containing only `=` starts the explanation, which runs क्यों → अन्य विकल्प क्यों नहीं → मुख्य बिंदु. The `उत्तर:` line is generated.
2. `python3 tools/cuet_san/san_conv.py tools/cuet_san/drafts/sanNN.txt tools/cuet_san/drafts/sanNN.json`
3. `python3 tools/cuet_san/san_check.py tools/cuet_san/drafts/sanNN.json` reports:
   - counts, the answer key and unit quotas (QUOTA if a unit is more than 1 off)
   - LONGEST: the correct option is clearly the longest
   - SEQ-ABCD: an order answer in A, B, C, D order
   - DUPOPT: duplicate options
   - NO-TARGET: an item with no answer-fact key
   - REPEAT-TARGET: a fact already used twice in the series
   - OVERLAP: the sub-topic or stem is too close to an earlier revised test
4. `python3 tools/cuet_san/relabel_match.py drafts/sanNN.txt 'sub_topic' II,IV,I,III` renames the सूची-II numerals of one match item. Use it so that no two match items in a test share an answer pattern.
5. `tools/cuet_san/san_ship.sh N "feat(sanskrit): revise Test N to CUET 2027 standard"` builds, shuffles, validates, marks the ledgers, commits and pushes.

`patch_item.py` fixes one item in both the draft and the shipped test. `reindex_series.py CUET/Sanskrit` refreshes `series_index.json`.
