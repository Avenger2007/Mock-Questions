# CUET Geography authoring tools

Same workflow as `tools/cuet_gt` (run everything from the repo root).

1. Write `tools/cuet_geo/drafts/geoNN.txt` (see `drafts/geo01.txt`, the pilot):
   - `%P UNIT` starts the case passage or table (5 linked questions in that unit, format `p`).
   - `@@ UNIT|sub_topic|e/m/h|fmt|ANS|targets` starts a question. UNIT: A1–A8 (*Fundamentals of Human Geography*), B1–B9 (*India: People and Economy*) — see `units.py` and the blueprint. fmt: `d` direct, `n` numerical, `p` case set, `a` assertion–reason, `q` sequence, `m` match-list, `s` statements. targets: comma-separated answer-fact keys for the unit's ledger in `docs/blueprints/geography_coverage.md` (`B5:x;B4:y` for another unit).
   - Option lines `A) …`; a line `=` starts the explanation (the `Answer:` line is generated).
2. `python3 tools/cuet_geo/geo_conv.py tools/cuet_geo/drafts/geoNN.txt tools/cuet_geo/drafts/geoNN.json`
3. `python3 tools/cuet_geo/geo_check.py tools/cuet_geo/drafts/geoNN.json` — counts, key, unit quotas, assertion–reason keys, LONGEST, SEQ-ABCD, DUPOPT, NO-TARGET, REPEAT-TARGET (a fact already used twice), OVERLAP.
4. `tools/cuet_geo/geo_ship.sh N "feat(geography): revise Test N to CUET 2027 standard (case theme)"`
