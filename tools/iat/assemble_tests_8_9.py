"""Mechanical assembly of authored TSV against approved slot metadata."""
import csv,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2]
# Historical TSV snapshots must never overwrite a reviewed canonical revision.
for existing in (root / 'IISER').glob('IAT*TEST*.json'):
    if json.loads(existing.read_text()).get('content_revision') == 'milestone15_fix_v1':
        raise SystemExit('Historical assembly disabled: edit the corrected canonical JSON; see IISER/revisions/README.md.')

base=json.loads((root/'IISER/IAT NEW TEST 7.json').read_text())
plan={(int(r['test']),int(r['question'])):r for r in csv.DictReader((root/'docs/blueprints/iat_25_test_slots.tsv').open(),delimiter='\t')}
images={8:{2:'Read ovary-whorl attachment',15:'Compare restriction band fragments',17:'Read octahedral splitting and occupancy',28:'Read observed and pure vapour pressures',53:'Read signed electric-field intervals',58:'Read resistor and reactive voltage phasors'},9:{3:'Read Km and Vmax from two rate curves',4:'Identify bundle sheath and mesophyll organisation',17:'Count donor positions and coordination charge',27:'Read pure and observed vapour pressures',46:'Read applied force below static threshold',51:'Read molecule-wall momentum transfer',53:'Read disconnected dielectric insertion',59:'Read hydrogen transition gaps'}}
for t in (8,9):
 d={k:v for k,v in base.items() if k!='questions'}
 d.update(test_id=f'IAT27_TEST_{t:02}',title=f'IAT New Test {t}',test_number=t,revision_date='2026-11-01')
 qs=[]
 for sec in 'bcmp':
  with (root/f'IISER/authoring/test{t}_{sec}.tsv').open() as f:
   for r in csv.reader(f,delimiter='\t'):
    assert len(r)==9,(t,sec,len(r))
    n=int(r[0]);p=plan[t,n];assert p['subject'].lower()==sec
    exp=re.sub(r'\\n(?=(?:Given:|Formula/Principle:|Step \d+:|Worked derivation:|Why:|Why not the others:|Key point:))','\n',r[8])
    q=dict(id=p['id'],section=sec.upper(),subject={'b':'Biology','c':'Chemistry','m':'Mathematics','p':'Physics'}[sec],topic=p['chapter'],sub_topic=p['focus'],class_level=p['class_level'],difficulty=p['difficulty_target'],format=r[1],question=r[2],options=[f'{a}) {v}' for a,v in zip('ABCD',r[3:7])],correct_option=r[7],explanation=exp)
    if n in images[t]:q.update(image_reference=f'IAT_T{t:02}_Q{n:02}.png',image_alt=images[t][n])
    qs.append(q)
 d['questions']=qs
 (root/f'IISER/IAT NEW TEST {t}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
