"""Bring the slot plan, plan CSV and evidence ledger back in line with the audited test JSONs.
Mechanical only: copies sub_topic/format/difficulty from the tests, applies the listed chapter moves,
refreshes hashes, and marks ledger rows whose question text changed. Run from the repo root."""
import csv,json,hashlib,glob
from pathlib import Path
from collections import Counter,defaultdict
R=Path('.');D=R/'docs/blueprints'
sha=lambda b:hashlib.sha256(b).hexdigest()
MOVES={'IAT27-T10-Q19':'STO','IAT27-T11-Q43':'3D','IAT27-T12-Q08':'GEN','IAT27-T12-Q59':'EMW','IAT27-T13-Q41':'COORD','IAT27-T17-Q47':'UNITS'}
act={};src={}
for t in range(1,26):
    p=R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json')
    for q in json.loads(p.read_text())['questions']: act[q['id']]=q;src[q['id']]=p
plan=list(csv.DictReader(open(D/'iat_25_test_plan.csv',encoding='utf-8-sig')));pf=list(plan[0])
names={}
for r in plan: names[(r['subject'],r['chapter_code'])]=r['chapter']
changed=set();n=Counter()
for r in plan:
    q=act[r['id']];h=sha(q['question'].encode())
    if h!=r['source_question_sha256']: changed.add(r['id']);r['source_question_sha256']=h;r['plan_updated']='2026-11-15';r['semantic_review_status']='question revised in the November 2026 audit; see IAT_AUDIT_REPORT.md'
    for k,v in (('focus',q['sub_topic']),('dominant_style_target',q['format']),('difficulty_target',q['difficulty'])):
        if r[k]!=v: r[k]=v;n[k]+=1
    if r['id'] in MOVES and r['chapter_code']!=MOVES[r['id']]:
        r['chapter_code']=MOVES[r['id']];r['chapter']=names[(r['subject'],MOVES[r['id']])];n['chapter']+=1
with open(D/'iat_25_test_plan.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,pf);w.writeheader();w.writerows(plan)
byid={r['id']:r for r in plan}
slots=list(csv.DictReader((D/'iat_25_test_slots.tsv').open(),delimiter='\t'));sf=list(slots[0])
for r in slots:
    for k in sf:
        if k in byid[r['id']] and k!='state': r[k]=byid[r['id']][k]
with (D/'iat_25_test_slots.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,sf,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(slots)
led=0
for lp in glob.glob('IISER/review/tests*/syllabus_material_evidence.json'):
    L=json.loads(Path(lp).read_text())
    for e in L:
        e['source_json_sha256']=sha((R/e['source_json']).read_bytes())
        if e['question_id'] in changed and 'revised' not in e['scope']:
            e['material_aspect']=act[e['question_id']]['sub_topic'];e['scope']='Question revised in the November 2026 audit; this topic mapping must be re-verified. '+e['scope'];led+=1
    Path(lp).write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
chk=json.loads((D/'iat_coverage_plan_check.json').read_text());chk['plan_csv_sha256']=sha((D/'iat_25_test_plan.csv').read_bytes());chk['reconciled']='2026-11-15: slot plan and plan CSV synchronised with audited tests'
(D/'iat_coverage_plan_check.json').write_text(json.dumps(chk,indent=2)+'\n')
bad=sum(1 for r in slots if (r['focus'],r['dominant_style_target'],r['difficulty_target'])!=(act[r['id']]['sub_topic'],act[r['id']]['format'],act[r['id']]['difficulty']))
print('updated',dict(n),'| questions revised',len(changed),'| ledger rows marked',led,'| remaining slot mismatches',bad)
cnt=defaultdict(Counter)
for r in plan: cnt[r['subject']][r['chapter_code']]+=1
for s in cnt: print(s,' '.join(f'{k}:{v}' for k,v in sorted(cnt[s].items(),key=lambda x:x[1])))
