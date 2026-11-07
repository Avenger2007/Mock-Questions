"""Synchronise manually reviewed focus/wording and existing fixed-slot metadata."""
import csv,json
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/'IISER/revisions'
focus={r[0]:(r[1],r[2]) for r in csv.reader((S/'milestone15_focus.tsv').open(),delimiter='\t')}
focus.update({r[0]:(r[1],r[2]) for r in csv.reader((S/'milestone15_focus_followup.tsv').open(),delimiter='\t')})
wording=dict(csv.reader((S/'milestone15_wording.tsv').open(),delimiter='\t'))
allq={}
for t in range(1,16):
 p=R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json');d=json.loads(p.read_text())
 for q in d['questions']:
  if q['id'] in focus:
   q['sub_topic'],q['syllabus_anchor']=focus[q['id']]
  if q['id'] in wording:q['question']=wording[q['id']]
  if q['id']=='IAT27-T05-Q02':q['difficulty']='medium'
  if q['id']=='IAT27-T05-Q12':q['difficulty']='hard'
  if q['id']=='IAT27-T09-Q31':q['difficulty']='medium'
  if q['id']=='IAT27-T09-Q42':q['difficulty']='hard'
  # Escape-only repair: a bracket immediately after an aligned row break is parsed as a length.
  q['explanation']=q['explanation'].replace(r'\\[\ce{OH-}]',r'\\ \left[\ce{OH-}\right]')
  allq[q['id']]=q
 d['review_status']='milestone corrections applied; independent academic and timed review pending'
 d['content_revision']='milestone15_fix_v1'
 d['revision_date']='2026-11-03'
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=S/'milestone15_chemistry_derivations.tsv'
p.write_text(p.read_text().replace(r'\\[\ce{OH-}]',r'\\ \left[\ce{OH-}\right]'))
p=R/'docs/blueprints/iat_25_test_slots.tsv'
with p.open() as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['id'] not in focus:continue
 q=allq[row['id']];row['focus']=focus[row['id']][0]
 row['angle_seed']='Milestone revision: '+focus[row['id']][0]
 row['dominant_style_target']=q['format'];row['difficulty_target']=q['difficulty']
 row['state']='milestone revision applied; academic and timed review pending'
# The frog correction changes level; paired kidney work restores the original section total.
for row in rows:
 if row['id']=='IAT27-T05-Q02':row['difficulty_target']='medium'
 if row['id']=='IAT27-T05-Q12':row['difficulty_target']='hard'
 if row['id']=='IAT27-T09-Q31':row['difficulty_target']='medium'
 if row['id']=='IAT27-T09-Q42':row['difficulty_target']='hard'
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Synchronized',len(focus),'reviewed focuses; IDs, order and keys retained')
