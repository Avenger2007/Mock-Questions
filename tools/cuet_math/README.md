# tools/cuet_math — CUET Mathematics (319) authoring tools

Run everything from the repo root.

| Step | Command |
|---|---|
| Convert a draft | `python3 tools/cuet_math/math_conv.py tools/cuet_math/drafts/mathNN.txt tools/cuet_math/drafts/mathNN.json` |
| Check it | `python3 tools/cuet_math/math_check.py tools/cuet_math/drafts/mathNN.json` |
| Ship it (build, shuffle, validate, mark ledger, commit, push) | `tools/cuet_math/math_ship.sh N "commit summary"` |
| Fix one shipped item | `python3 tools/cuet_math/patch_item.py N 'sub_topic' patches.json` |
| Refresh the series index | `python3 tools/cuet_math/reindex_series.py "CUET/Mathematics"` |

**Draft format:** `@@ UNIT|sub_topic|e/m/h|fmt|ANS|keys`. UNIT decides the section: `C1–C6` → A, `M1–M13` → B1, `AM1–AM8` → B2. fmt is `n` numerical, `d` direct, `m` match-list or `s` statements. Options are written `A) …`; a line `=` starts the explanation, whose `Answer:` line is generated. Mathematics is KaTeX (`\( … \)`). Do not put `|` inside a sub-topic.

**Checker flags:** COUNT, DIFF, KEY and FMT (per section); QUOTA (a unit is off by more than ±1); MATCH-SAME-UNIT; MATCH-PATTERN-REPEAT; DUPOPT; LONGEST (text options only); NO-STEPS (a numerical item without `Step 1`); REPEAT-TARGET (a skill key already used 3 times, see `docs/blueprints/mathematics_coverage.md` §C); OVERLAP (sub-topic > 0.85 or stem > 0.85 similar to an earlier revised test).
