#!/bin/bash
# usage (from repo root): tools/cuet_math/math_ship.sh N 'commit summary'
# Builds the draft into CUET/Mathematics, shuffles, validates, marks the ledgers, commits and pushes.
set -e
T=tools/cuet_math; N=$1; NN=$(printf %02d $N); F="CUET/Mathematics/CUET MATHEMATICS TEST $N.json"
python3 $T/build_math.py $N $T/drafts/math$NN.json
python3 shuffle_test.py "$F"
python3 - "$F" <<'PY'
import json,re,sys
d=json.load(open(sys.argv[1])); q=d['questions']
for path in (['A','B1'],['A','B2']):
    ks=''.join(x['correct_option'] for x in q if x['section'] in path)
    r=max(len(m.group()) for m in re.finditer(r'(.)\1*',ks)); print(path,ks,r); assert r<=3,'run'
PY
OUT=$(python3 validate_papers.py CUET --subject "Mathematics" 2>&1)
echo "$OUT" | grep -E "TEST $N\.json" && { echo "VALIDATION ISSUE"; exit 1; } || true
echo "$OUT" | grep -E "JSON Parse Errors|Cross-Paper|Within-Paper|Difficulty Dev|Wrong Question"
python3 $T/mark_math.py $N $T/drafts/math$NN.json
git add "$F" docs/blueprints/mathematics_coverage.md $T/drafts/math$NN.txt; git add -f $T/drafts/math$NN.json
git commit -q -m "$2

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git pull -q --rebase origin main && git push -q origin main && git log --oneline -1
