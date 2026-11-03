"""Mechanically assemble individually authored TSV rows into IAT review schema."""
import csv,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2]
base=json.loads((root/'IISER/IAT NEW TEST 11.json').read_text())
plan={(int(r['test']),int(r['question'])):r for r in csv.DictReader((root/'docs/blueprints/iat_25_test_slots.tsv').open(),delimiter='\t')}
images={12:{1:'Taxonomic ranks relating species to genus and family',2:'Upper palisade and lower spongy mesophyll under incident light',4:'Thylakoid proton gradient and ATP synthase orientation',9:'Two resistance markers and the plasmid insertion site',16:'Nitrile carbon bonds and geometry',17:'Adjacent and opposite ligand arrangements on a square plane',21:'Carbonyl structures of ethanal and propanone',28:'Ideal mixture pure-component vapour pressures and composition',46:'Signed piecewise acceleration against time',53:'Piecewise electric field versus position',58:'Prism ray and surface normal angles'},13:{1:'Chloroplast pigments and starch storage evidence',2:'Superior ovary and whorl attachment points',9:'Inward-facing DNA primers on antiparallel strands',15:'900-bp and 600/300-bp restriction-fragment lanes',16:'Nitrogen lone-pair and bond-pair geometries',30:'Reaction quotient pressure values for the two gases',53:'Closed surface and inside/outside charge positions',54:'Resistor network and labelled nodes',55:'Increasing inward flux through the loop',60:'Forward and reverse diode current-voltage plot'}}
for t in (12,13):
 d={k:v for k,v in base.items() if k!='questions'}
 d.update(test_id=f'IAT27_TEST_{t:02}',title=f'IAT New Test {t}',test_number=t,revision_date='2026-11-03')
 amendments={}
 with (root/f'IISER/authoring/test{t}_explanation_amendments.tsv').open() as f:
  for n,why_extra,wrong_replacement in csv.reader(f,delimiter='|'):
   n=int(n);assert n not in amendments
   amendments[n]=(why_extra.strip(),wrong_replacement.strip())
 qs=[]
 for sec in 'bcmp':
  with (root/f'IISER/authoring/test{t}_{sec}.tsv').open() as f:
   for r in csv.reader(f,delimiter='\t'):
    assert len(r)==9,(t,sec,len(r))
    n=int(r[0]);p=plan[t,n];assert p['subject'].lower()==sec
    exp=re.sub(r'\\n(?=(?:Given:|Formula/Principle:|Step \d+:|Worked derivation:|Why:|Why not the others:|Key point:))','\n',r[8])
    if n in amendments:
     extra,wrong=amendments[n]
     before,rest=exp.split('\nWhy not the others: ',1)
     current,after=rest.split('\nKey point: ',1)
     assert 'Why: ' in before
     if extra:before+=' '+extra
     exp=before+'\nWhy not the others: '+(wrong or current)+'\nKey point: '+after
    q=dict(id=p['id'],section=sec.upper(),subject={'b':'Biology','c':'Chemistry','m':'Mathematics','p':'Physics'}[sec],topic=p['chapter'],sub_topic=p['focus'],class_level=p['class_level'],difficulty=p['difficulty_target'],format=r[1],question=r[2],options=[f'{a}) {v}' for a,v in zip('ABCD',r[3:7])],correct_option=r[7],explanation=exp)
    if n in images[t]:q.update(image_reference=f'IAT_T{t:02}_Q{n:02}.png',image_alt=images[t][n])
    qs.append(q)
 d['questions']=qs
 (root/f'IISER/IAT NEW TEST {t}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
