# tools/cuet_phy — CUET Physics (322) authoring tools

Run everything from the repo root.

| Step | Command |
|---|---|
| Convert a draft | `python3 tools/cuet_phy/phy_conv.py tools/cuet_phy/drafts/phyNN.txt tools/cuet_phy/drafts/phyNN.json` |
| Check it | `python3 tools/cuet_phy/phy_check.py tools/cuet_phy/drafts/phyNN.json` |
| Ship it (build, shuffle, validate, mark ledger, commit, push) | `tools/cuet_phy/phy_ship.sh N "commit summary"` |
| Fix one shipped item | `python3 tools/cuet_phy/patch_item.py N 'sub_topic' patches.json` |
| Replace one shipped item | rewrite its draft block, then `python3 tools/cuet_phy/replace_item.py N 'old sub_topic'` |
| List earlier items per unit | `python3 tools/cuet_phy/phy_index.py [P1 P6 …]` |
| Refresh the series index | `python3 tools/cuet_phy/reindex_series.py "CUET/Physics"` |

**Draft format:** `@@ UNIT|sub_topic|e/m/h|fmt|ANS|keys`. UNIT is `P1`–`P9` (see `units.py`). fmt is `n` numerical, `d` direct, `m` match-list, `s` statements or `q` sequence. Options are written `A) …`; a line `=` starts the explanation, whose `Answer:` line is generated. Mathematics is KaTeX (`\( … \)`). Do not put `|` inside a sub-topic.

**Checker flags:** COUNT, DIFF (8/32/10), KEY (13/12/13/12 odd, 12/13/12/13 even), FMT (6 match, 6 statements, 3 sequence), FEW-NUMERICAL (< 20), QUOTA (exact unit counts), MATCH-SAME-UNIT, MATCH-PATTERN-REPEAT, STMT-POLARITY-NOT-ALTERNATING, SEQ-ABCD, DUPOPT, LONGEST (direct items), NO-STEPS, KATEX-UNBALANCED, REPEAT-TARGET (a skill key already used twice, see `docs/blueprints/physics_coverage.md` §C), OVERLAP (sub-topic or stem > 0.85 similar to an earlier revised test).
