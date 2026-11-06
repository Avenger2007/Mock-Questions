#!/bin/bash
# usage (from repo root): tools/cuet_his/his_ship.sh N 'commit summary'
# Builds the draft into CUET/History, shuffles, validates, marks the ledgers, commits and pushes.
set -e
T=tools/cuet_his; N=$1; NN=$(printf %02d $N); F="CUET/History/CUET HISTORY TEST $N.json"
python3 $T/build_his.py $N $T/drafts/his$NN.json
python3 shuffle_test.py "$F"
python3 - "$F" <<'PY'
import json,re,sys
d=json.load(open(sys.argv[1]))
ks=''.join(q['correct_option'] for q in d['questions'])
r=max(len(m.group()) for m in re.finditer(r'(.)\1*',ks)); print(ks,r); assert r<=3,'run'
PY
OUT=$(python3 validate_papers.py CUET --subject "History" 2>&1)
echo "$OUT" | grep -E "TEST $N\.json" && { echo "VALIDATION ISSUE"; exit 1; } || true
echo "$OUT" | grep -E "JSON Parse Errors|Cross-Paper|Within-Paper|Difficulty Dev|Missing Inline"
python3 $T/mark_his.py $N $T/drafts/his$NN.json
git add "$F" docs/blueprints/history_coverage.md $T/drafts/his$NN.txt
git commit -q -m "$2

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git pull -q --rebase origin main && git push -q origin main && git log --oneline -1
