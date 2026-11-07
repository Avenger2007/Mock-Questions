"""Organise individually authored teaching amendments; never generate questions."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'IISER/revisions'
p=ROOT/'IISER/IAT TEST 1.json';data=json.loads(p.read_text())
for row in csv.reader((S/'milestone15_test1_teaching.tsv').open(),delimiter='\t'):
    assert len(row)==4,row
    number,why,keypoint,tex=row;q=data['questions'][int(number)-1];old=q['explanation']
    if 'Common mistake:' in old:
        before,wrong=old.split('\nCommon mistake: ',1)
        assert 'Why:' not in before
        q['explanation']=before+'\nWorked derivation: '+tex+'\nWhy: '+why+'\nWhy not the others: '+wrong+'\nKey point: '+keypoint
    elif 'Worked derivation:' not in old:
        before,after=old.split('\nWhy:',1)
        q['explanation']=before+'\nWorked derivation: '+tex+'\nWhy:'+after
for number,exp in csv.reader((S/'milestone15_test1_structured.tsv').open(),delimiter='\t'):
    data['questions'][int(number)-1]['explanation']=exp.replace('\\n','\n')
data['review_status']='current explanation standard migrated; milestone corrections applied; academic and timed review pending'
data['revision_date']='2026-11-03'
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
equations=dict(csv.reader((S/'milestone15_chemistry_derivations.tsv').open(),delimiter='\t'))
steps=dict(csv.reader((S/'milestone15_explicit_steps.tsv').open(),delimiter='\t'))
count=0
for t in range(2,16):
    p=ROOT/f'IISER/IAT NEW TEST {t}.json';d=json.loads(p.read_text());changed=False
    for q in d['questions']:
        if q['id'] in steps:
            import re
            q['explanation']=re.sub(r'\\n(?=(?:Given:|Formula/Principle:|Step \d+:|Worked derivation:|Why:|Why not the others:|Key point:))','\n',steps[q['id']])
            changed=True
        if q['id'] not in equations or 'Worked derivation:' in q['explanation']:continue
        before,after=q['explanation'].split('\nWhy:',1)
        q['explanation']=before+'\nWorked derivation: '+equations[q['id']]+'\nWhy:'+after
        changed=True;count+=1
    if changed:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Migrated Test 1 teaching sections and added',count,'authored Chemistry derivations')
