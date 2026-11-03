# CUET English authoring tools

Run everything from the repo root.

1. Write `tools/cuet_english/drafts/engNN.txt` in the compact format (see `drafts/eng01.txt`, the approved pilot):
   - `%P R1` / `%P R2` / `%P R3` start the factual, narrative and literary passages (≤ 300 words each).
   - `@@ SEC|sub_topic|e/m/h|fmt|ANS|targets` starts a question. SEC: R1–R3, V1–V6. fmt: `d` direct, `p` passage, `q` sequence, `m` match-list, `s` statements. targets: `C1:word,word;C2:idiom;C3:phrasal;C4:confusable` (the coverage ledgers).
   - Option lines `A) …`; a line `=` starts the explanation (the `Answer:` line is generated).
2. `python3 tools/cuet_english/eng_conv.py tools/cuet_english/drafts/engNN.txt tools/cuet_english/drafts/engNN.json`
3. `python3 tools/cuet_english/eng_check.py tools/cuet_english/drafts/engNN.json` — counts, key, passage word counts, LONGEST (correct option clearly longest), SEQ-ABCD, DUPOPT, REPEAT-TARGET (ledger), OVERLAP (with earlier revised tests). Fix everything it reports.
4. `tools/cuet_english/eng_ship.sh N "feat(english): revise Test N to CUET 2027 standard (themes)"`

`txtedit.py` has helpers (load/find/opts/hdr/stem/save) for editing a draft by sub_topic; `fixopts.py` rewrites options or moves an answer letter in the JSON.
