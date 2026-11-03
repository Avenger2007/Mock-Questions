# CUET General Test authoring tools

Same workflow as `tools/cuet_english` (run everything from the repo root).

1. Write `tools/cuet_gt/drafts/gtNN.txt` (see `drafts/gt01.txt`, the pilot):
   - `%P D` starts the data-interpretation table (5 linked questions, section `D`, format `p`).
   - `@@ SEC|sub_topic|e/m/h|fmt|ANS|targets` starts a question. SEC: Q quant, D DI, M mental ability, L logical reasoning, G static GK, S science and environment, C current affairs. fmt: `d` direct, `n` numerical, `p` DI set, `a` assertion–reason, `q` sequence, `m` match-list, `s` statements. targets: `F1:fact;F2:fact;F3:event` (fact ledgers in `docs/blueprints/general_test_coverage.md`).
   - Option lines `A) …`; a line `=` starts the explanation (the `Answer:` line is generated).
2. `python3 tools/cuet_gt/gt_conv.py tools/cuet_gt/drafts/gtNN.txt tools/cuet_gt/drafts/gtNN.json`
3. `python3 tools/cuet_gt/gt_check.py tools/cuet_gt/drafts/gtNN.json` — counts, key, assertion–reason keys, LONGEST, SEQ-ABCD, DUPOPT, REPEAT-TARGET, OVERLAP.
4. `tools/cuet_gt/gt_ship.sh N "feat(general-test): revise Test N to CUET 2027 standard (DI theme)"`

Current affairs: January 2025 – October 2026 only, each item checked against a news or official source when written, with its date in the explanation.
