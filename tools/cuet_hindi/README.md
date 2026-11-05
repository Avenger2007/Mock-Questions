# CUET Hindi authoring tools

Run everything from the repo root.

1. Write `tools/cuet_hindi/drafts/hinNN.txt` in the compact format (see `drafts/hin01.txt`, the approved pilot):
   - `%P R1` / `%P R2` / `%P R3` start the factual, narrative and literary passages (≤ 300 words each); add `verse` (`%P R3 verse`) when the literary passage is a पद्यांश.
   - `@@ SEC|sub_topic|e/m/h|fmt|ANS|targets` starts a question. SEC: R1–R3, V1–V6 (see docs/blueprints/hindi.md §3). fmt: `d` direct, `p` passage, `q` sequence, `m` match-list, `s` statements. targets: `C1:शब्द;C2:मुहावरा;C3:संधि/समास/उपसर्ग/प्रत्यय/लिंग words;C4:काव्यांग examples and रचनाएँ` (the ledgers in docs/blueprints/hindi_coverage.md).
   - Option lines `A) …`; a line `=` starts the explanation (`क्यों:` / `अन्य विकल्प क्यों नहीं:` / `मुख्य बिंदु:`; the `उत्तर:` line is generated).
2. `python3 tools/cuet_hindi/hin_conv.py tools/cuet_hindi/drafts/hinNN.txt tools/cuet_hindi/drafts/hinNN.json`
3. `python3 tools/cuet_hindi/hin_check.py tools/cuet_hindi/drafts/hinNN.json` — counts, key, passage word counts, LONGEST (correct option clearly longest), SEQ-ABCD, DUPOPT, REPEAT-TARGET (ledger), OVERLAP (with earlier revised tests). Fix everything it reports.
4. `tools/cuet_hindi/hin_ship.sh N "feat(hindi): revise Test N to CUET 2027 standard (themes)"`

`txtedit.py` has helpers (load/find/opts/hdr/stem/save) for editing a draft by sub_topic; `fixopts.py` rewrites options or moves an answer letter in the JSON.
