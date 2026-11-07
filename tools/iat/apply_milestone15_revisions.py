"""Mechanically apply individually authored correction rows without shuffling."""
import csv,json,re,hashlib,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'IISER/revisions'
records={}
for name in ('milestone15_math.tsv','milestone15_sciences.tsv','milestone15_additional.tsv','milestone15_extra.tsv','milestone15_inverse_followup.tsv','milestone15_hard_followup.tsv','milestone15_relation_followup.tsv','milestone15_inductor_followup.tsv'):
    for row in csv.reader((source/name).open(),delimiter='\t'):
        assert len(row)==8,(name,len(row),row[0])
        ident,stem,a,b,c,d,fmt,exp=row
        assert ident not in records or name.endswith('_followup.tsv'),ident
        records[ident]=dict(question=stem,options=[f'{l}) {v}' for l,v in zip('ABCD',(a,b,c,d))],
                            format=fmt,explanation=re.sub(r'\\n(?=(?:Given:|Formula/Principle:|Step \d+:|Worked derivation:|Why:|Why not the others:|Key point:))','\n',exp))
changes=[]
for t in range(1,16):
    p=ROOT/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json')
    data=json.loads(p.read_text())
    baseline=subprocess.check_output(['git','show','f06d700:'+str(p.relative_to(ROOT))],cwd=ROOT)
    old=hashlib.sha256(baseline).hexdigest()
    changed=[]
    for q in data['questions']:
        if q['id'] not in records:continue
        new=records[q['id']]
        assert new['explanation'].startswith(f"Answer: ({q['correct_option']})"),q['id']
        q.update(new);changed.append(q['id'])
    if changed:
        data['review_status']='milestone audit corrections applied; independent academic and timed review pending'
        data['revision_date']='2026-11-03'
        p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        changes.append(dict(test=t,question_ids=changed,before_sha256=old,after_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
out=ROOT/'IISER/review/milestone15_fixes';out.mkdir(exist_ok=True)
(out/'replacement_application.json').write_text(json.dumps(changes,indent=2)+'\n')
assert sum(len(x['question_ids']) for x in changes)==len(records)
print('Applied',len(records),'manually authored replacements/corrections across',len(changes),'papers')
