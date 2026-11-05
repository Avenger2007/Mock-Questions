"""Mechanical assembly of individually authored, solved rows; no question generation."""
import csv,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[2]
plan_path=R/'docs/blueprints/iat_25_test_slots.tsv'
with plan_path.open() as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;slots=list(reader)
lookup={(int(r['test']),int(r['question'])):r for r in slots}
specs=json.loads((R/'IISER/authoring/tests16_17_images.json').read_text())
images={(r['test'],r['question']):r for r in specs}
base=json.loads((R/'IISER/IAT NEW TEST 15.json').read_text())
for t in [16,17]:
 data={k:v for k,v in base.items() if k!='questions'}
 data.update(test_id=f'IAT27_TEST_{t:02}',test_number=t,title=f'IAT New Test {t}',
             revision_date='2026-11-04',content_revision='tests16_17_authored_v1',
             review_status='author checks applied; independent academic and timed review pending',
             authoring_source=f'Individually authored IISER/authoring/test{t}_b,c,m,p.tsv; no templated question generation')
 questions=[]
 for sec in 'bcmp':
  rows=list(csv.reader((R/f'IISER/authoring/test{t}_{sec}.tsv').open(),delimiter='\t'))
  assert len(rows)==15
  for row in rows:
   assert len(row)==11,(t,sec,row[0],len(row))
   n=int(row[0]);slot=lookup[t,n]
   assert slot['subject']==sec.upper()
   exp=re.sub(r'\\n(?=(?:Given:|Formula/Principle:|Step \d+:|Worked derivation:|Why:|Why not the others:|Key point:))','\n',row[8])
   assert exp.startswith(f'Answer: ({row[7]})'),(t,n)
   q=dict(id=slot['id'],section=sec.upper(),subject={'b':'Biology','c':'Chemistry','m':'Mathematics','p':'Physics'}[sec],
          topic=slot['chapter'],sub_topic=row[9],class_level=slot['class_level'],
          syllabus_anchor=row[10],difficulty=slot['difficulty_target'],format=row[1],
          question=row[2],options=[f'{a}) {v}' for a,v in zip('ABCD',row[3:7])],
          correct_option=row[7],explanation=exp)
   if (t,n) in images:
    q.update(image_reference=f'IAT_T{t:02}_Q{n:02}.png',image_alt=images[t,n]['alt'])
   questions.append(q)
   slot.update(focus=row[9],angle_seed='Authored: '+row[9],
               dominant_style_target=row[1],state='authored review draft; academic and timed review pending')
  assert [int(q['id'][-2:]) for q in questions if q['section']==sec.upper()]==list(range(15*'bcmp'.index(sec)+1,15*'bcmp'.index(sec)+16))
 data['questions']=questions
 (R/f'IISER/IAT NEW TEST {t}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with plan_path.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(slots)
registry=R/'IISER/IAT_images.md';text=registry.read_text()
text=re.split(r'\n## Test 16 — Q',text,maxsplit=1)[0].rstrip()
for r in specs:
 t,n=r['test'],r['question']
 text+=f"""

## Test {t} — Q{n} (IAT27-T{t:02}-Q{n:02}) — {r['subject']}
- **File name:** IAT_T{t:02}_Q{n:02}.png
- **Purpose:** {r['purpose']}
- **Aspect ratio / size:** 4:3, 1200 × 900 px.
- **Style:** Exact black textbook lines on white; no decorative shading or photorealism.
- **Must show:** {r['must_show']}
- **Axes (graphs):** Quantities, units and ticks explicitly specified above where applicable; other drawings are schematics, not to scale.
- **Text in image:** Only the stated labels, units and identifying captions. Sans-serif text at least 24 px in the original image.
- **Must NOT show:** {r['prohibited']}
- **Alt text:** {r['alt']}
"""
registry.write_text(text.rstrip()+'\n')
print('Assembled 120 authored records; fixed IDs, source order and',len(specs),'image specifications')
