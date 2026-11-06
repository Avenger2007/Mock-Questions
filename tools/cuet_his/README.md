# CUET History authoring tools

These follow the same workflow as `tools/cuet_geo`. Run everything from the repo root.

1. Write `tools/cuet_his/drafts/hisNN.txt`. The pilot, `drafts/his01.txt`, shows the format.
   - `%P THEME` starts the source passage: an original summary of an NCERT source, with 5 linked questions in format `p`.
   - `@@ THEME|sub_topic|e/m/h|fmt|ANS|targets` starts a question.
     - **THEME** is H1–H12, the twelve syllabus themes. See `units.py` and the blueprint `docs/blueprints/history.md`.
     - **fmt** is `d` direct (this includes fill-in-the-blank and "identify the incorrect pair"), `p` source set, `q` sequence, `m` match-list or `s` statements.
     - **targets** are comma-separated answer-fact keys for the theme's ledger in `docs/blueprints/history_coverage.md`. Use `H9:x,y` to file a key under another theme. Never use `;` or `:` inside a key.
   - Option lines are written `A) …`. A line containing only `=` starts the explanation, which runs Why → Why not the others → Key point. The `Answer:` line is generated.
2. `python3 tools/cuet_his/his_conv.py tools/cuet_his/drafts/hisNN.txt tools/cuet_his/drafts/hisNN.json`
3. `python3 tools/cuet_his/his_check.py tools/cuet_his/drafts/hisNN.json` reports:
   - counts, the answer key and theme quotas (QUOTA if a theme is more than 1 off), and part totals
   - LONGEST: the correct option is clearly the longest
   - SEQ-ABCD: a sequence answer in A, B, C, D order
   - DUPOPT: duplicate options
   - NO-TARGET: an item with no answer-fact key
   - REPEAT-TARGET: a fact already used twice in the series
   - OVERLAP: the sub-topic or stem is too close to an earlier test
4. `python3 tools/cuet_his/relabel_match.py drafts/hisNN.txt 'sub_topic' II,IV,I,III` renames the List-II numerals of one match item (in the list, the options and the explanation). Use it so that no two match items in a test share an answer pattern.
5. `tools/cuet_his/his_ship.sh N "feat(history): revise Test N to CUET 2027 standard (source theme)"` builds, shuffles, validates, marks the ledgers, commits and pushes.

`patch_item.py` fixes one item in both the draft and the shipped test. `reindex_series.py CUET/History` refreshes `series_index.json`.
