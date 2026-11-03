"""Mechanically assemble hand-authored TSV records and existing slot metadata."""
import csv,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2]
base=json.loads((root/'IISER/IAT NEW TEST 9.json').read_text())
plan={(int(r['test']),int(r['question'])):r for r in csv.DictReader((root/'docs/blueprints/iat_25_test_slots.tsv').open(),delimiter='\t')}
images={10:{2:'Frog heart chambers and labelled return vessels',3:'G1 and replicated chromosome DNA patterns',9:'Induced target-protein band and controls',18:'Water and metal calorimeter observations',23:'Two reaction-energy profiles with common endpoints',52:'Two circular orbit radii about a planet',53:'Opposite charges and marked x positions',58:'Concave mirror and object inside focal point'},11:{1:'Fruit wall enclosing seed and embryo',2:'Root radial vascular arrangement',8:'Microbial fermentation products',9:'Complementary vector and insert overhangs',17:'Ionisation isomers and sulfate wet-test observations',22:'Carbonyl addition arrow and cyanide pair',28:'Freezing point difference and solvent constant',49:'Elastic and plastic stress-strain slopes',52:'Pendulum length and lift acceleration',57:'Three layers and incident ray',58:'Photoelectric stopping-voltage plot',59:'Hydrogen energy levels and two transitions'}}
for t in (10,11):
 d={k:v for k,v in base.items() if k!='questions'}
 d.update(test_id=f'IAT27_TEST_{t:02}',title=f'IAT New Test {t}',test_number=t,revision_date='2026-11-03')
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
