# CUET Political Science authoring tools

These follow the same workflow as `tools/cuet_his`. Run everything from the repo root.

1. Write `tools/cuet_pol/drafts/polNN.txt`. The pilot, `drafts/pol01.txt`, shows the format.
   - `%P THEME` starts the passage: an original summary of an NCERT theme, with 5 linked questions in format `p`.
   - `@@ THEME|sub_topic|e/m/h|fmt|ANS|targets` starts a question.
     - **THEME** is I1–I9 and W1–W7, the sixteen syllabus units. See `units.py` and the blueprint `docs/blueprints/political_science.md`.
     - **fmt** is `d` direct (this includes fill-in-the-blank and "identify the incorrect pair"), `p` source set, `q` sequence, `m` match-list or `s` statements.
     - **targets** are comma-separated answer-fact keys for the theme's ledger in `docs/blueprints/political_science_coverage.md`. Use `W3:x,y` to file a key under another theme. Never use `;` or `:` inside a key.
   - Option lines are written `A) …`. A line containing only `=` starts the explanation, which runs Why → Why not the others → Key point. The `Answer:` line is generated.
2. `python3 tools/cuet_pol/pol_conv.py tools/cuet_pol/drafts/polNN.txt tools/cuet_pol/drafts/polNN.json`
3. `python3 tools/cuet_pol/pol_check.py tools/cuet_pol/drafts/polNN.json` reports:
   - counts, the answer key and theme quotas (QUOTA if a theme is more than 1 off), and part totals
   - LONGEST: the correct option is clearly the longest
   - SEQ-ABCD: a sequence answer in A, B, C, D order
   - DUPOPT: duplicate options
   - NO-TARGET: an item with no answer-fact key
   - REPEAT-TARGET: a fact already used twice in the series
   - OVERLAP: the sub-topic or stem is too close to an earlier test
4. `python3 tools/cuet_pol/relabel_match.py drafts/polNN.txt 'sub_topic' II,IV,I,III` renames the List-II numerals of one match item (in the list, the options and the explanation). Use it so that no two match items in a test share an answer pattern.
5. `tools/cuet_pol/pol_ship.sh N "feat(political-science): revise Test N to CUET 2027 standard "` builds, shuffles, validates, marks the ledgers, commits and pushes.

`patch_item.py` fixes one item in both the draft and the shipped test. `reindex_series.py CUET/Political Science` refreshes `series_index.json`.
