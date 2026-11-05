"""Synchronise plan metadata from canonical items and literal future briefs; never author questions."""
import csv,hashlib,json,re,math
from collections import Counter,defaultdict
from pathlib import Path
R=Path(__file__).resolve().parents[2];D=R/'docs/blueprints';T=R/'tmp/iat_plan';T.mkdir(exist_ok=True)
check_path=D/'iat_coverage_plan_check.json'
if check_path.exists():
 prior=json.loads(check_path.read_text());csv_path=D/'iat_25_test_plan.csv'
 if prior.get('plan_csv_sha256') and csv_path.exists() and hashlib.sha256(csv_path.read_bytes()).hexdigest()!=prior['plan_csv_sha256']:
  raise SystemExit('Plan CSV has manual edits: reconcile them with the slot register and literal future briefs before rebuilding. No files changed.')
slots=list(csv.DictReader((D/'iat_25_test_slots.tsv').open(),delimiter='\t'));fields=list(slots[0]);lookup={(int(r['test']),int(r['question'])):r for r in slots}
briefs=list(csv.DictReader((D/'iat_tests20_25_angle_briefs.tsv').open(),delimiter='\t'))
assert len(briefs)==24
for row in briefs:
 angles=row['ordered_angle_briefs'].split('|');assert len(angles)==15,(row['test'],row['subject'],len(angles))
 start='BCMP'.index(row['subject'])*15+1
 for n,angle in enumerate(angles,start):lookup[int(row['test']),n].update(focus=angle,angle_seed='Reserved original task: '+angle,state='concrete reservation; syllabus and semantic review required before authorship')
actual={}
for test in range(1,20):
 p=R/'IISER'/('IAT TEST 1.json' if test==1 else f'IAT NEW TEST {test}.json')
 for q in json.loads(p.read_text())['questions']:
  n=int(q['id'][-2:]);actual[test,n]=(q,str(p.relative_to(R)))
  r=lookup[test,n];r.update(focus=q['sub_topic'],dominant_style_target=q['format'],difficulty_target=q['difficulty'],state='authored review draft; independent academic and timed review pending')
with (D/'iat_25_test_slots.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(slots)
# Catalogue every explicitly printed topic phrase or sentence from the official stored syllabus.
syll=R/'IISER/IISER_Aptitude_Test_Syllabus_2026.md';text=syll.read_text();tax=json.loads((D/'iat_taxonomy.json').read_text())
def norm(s):return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
heads={sec:{norm(v[0]):code for code,v in units.items() if not code.startswith('X')} for sec,units in tax.items()}
heads['P'].update({norm('Motion in a Straight Line'):'KIN',norm('Motion in a Plane'):'KIN',norm('Electric Charges and Fields'):'ELECTRO',norm('Electrostatic Potential and Capacitance'):'CAP',norm('Moving Charges and Magnetism'):'MAG',norm('Magnetism and Matter'):'MAG',norm('Semiconductor Electronics: Materials, Devices and Simple Circuits'):'SEMI'})
mathheads={'Sets and Logic':'SET','Basic counting techniques':'COUNT','Complex numbers, linear and quadratic equations':'QUAD','Complex Numbers':'COMPLEX','Quadratic Equations':'QUAD','Linear Inequalities':'QUAD','Trigonometric functions':'TRIG','Vectors':'VECTOR','Matrices & determinants':'MATRIX','Coordinate geometry':'COORD','Three-dimensional geometry':'3D','Sequences & series':'SEQ','Limit & continuity':'LIMIT','Differentiation':'DIFF','Integration':'INT','Differential equations':'DE','Statistics, Probability & Linear Programming':'STAT','Statistics':'STAT','Probability':'PROB'}
heads['M'].update({norm(k):v for k,v in mathheads.items()})
sec=None;code=None;catalog=[];unit='';serial=Counter()
def split_commas(s):
 out=[];buf='';depth=0
 for ch in s:
  if ch=='(':depth+=1
  elif ch==')':depth=max(0,depth-1)
  if ch==',' and depth==0:
   if buf.strip():out.append(buf.strip())
   buf=''
  else:buf+=ch
 if buf.strip():out.append(buf.strip())
 return out
for para in re.split(r'\n\s*\n',text):
 s=' '.join(para.split()).strip()
 if s in ['BIOLOGY','CHEMISTRY','MATHEMATICS','PHYSICS']:sec={'BIOLOGY':'B','CHEMISTRY':'C','MATHEMATICS':'M','PHYSICS':'P'}[s];code=None;continue
 if not sec or s.startswith(('#','>')):continue
 # Find the longest recognised heading at the start, accommodating headings followed by a colon.
 matches=[(len(k),k,v) for k,v in heads[sec].items() if norm(s)==k or norm(s).startswith(k+' ')]
 if matches:
  _,key,code=max(matches);unit=tax[sec].get(code,[key])[0]
  if norm(s)==key:continue
  # Original heading text ends at the first colon, except the semiconductor heading with internal colon.
  if ':' in s:
   if sec=='P' and s.startswith('Semiconductor Electronics:'):body=s.split('Circuits:',1)[-1] if 'Circuits:' in s else s.split(':',2)[-1]
   else:body=s.split(':',1)[1]
  elif norm(s)==key:continue
  else:body=s
 else:body=s
 if not code:raise ValueError(('Unmapped official block',sec,s))
 # Retain the original subchapter label alongside each subtopic rather than dropping introductory content.
 parent=''
 if sec=='B' and ':' in body:parent,body=body.split(':',1)
 if sec=='M':pieces=[z.strip(' .') for z in re.split(r'(?<=[.])\s+|;',body) if z.strip(' .')]
 elif sec=='P':pieces=[z.strip(' .') for z in body.split(';') if z.strip(' .')]
 else:pieces=[z.strip(' .') for z in split_commas(body) if z.strip(' .')]
 for leaf in pieces:
  serial[sec]+=1;catalog.append(dict(topic_id=f'{sec}-{serial[sec]:03}',subject=sec,chapter_code=code,chapter=unit,official_parent=parent.strip(),official_topic=leaf,syllabus_source=str(syll.relative_to(R))))
# Each named scope item has a prospective owner. These are reservations, not automatic claims of tested mastery.
stop=set('the a an and or of in on to for with as by its is are from different general some introduction concept simple various properties applications types their it at be which into between same'.split())
def tokens(s):return {w[:-1] if w.endswith('s') and len(w)>4 else w for w in norm(s).split() if w not in stop and len(w)>2}
future=[r for r in slots if int(r['test'])>=20];loads=Counter();owners=defaultdict(list)
for leaf in catalog:
 candidates=[r for r in future if r['subject']==leaf['subject'] and r['chapter_code']==leaf['chapter_code']]
 assert candidates,leaf
 words=tokens(leaf['official_topic']+' '+leaf['official_parent'])
 def score(r):return len(words&tokens(r['focus']))/(max(1,len(words))**.5)-.10*loads[r['id']]
 overrides={'B-138':(21,12),'B-036':(23,14),'B-072':(24,13),'B-070':(24,13),'B-071':(24,13),'P-203':(22,60),'P-204':(22,60),'P-205':(22,60)}
 forced=overrides.get(leaf['topic_id'])
 chosen=lookup[forced] if forced else max(candidates,key=score);hits=words&tokens(chosen['focus']);loads[chosen['id']]+=1;owners[chosen['id']].append(leaf['topic_id'])
 # A text-evidence candidate is disclosed as such, never marked academically covered by a word match.
 evidence=[]
 phrase=norm(leaf['official_topic'])
 for (test,n),(q,path) in actual.items():
  if q['section']!=leaf['subject']:continue
  hay=norm(q['question']+' '+q['explanation']+' '+q.get('syllabus_anchor',''))
  if len(phrase)>8 and phrase in hay:evidence.append(q['id'])
 leaf.update(planned_owner=chosen['id'],planned_angle=chosen['focus'],scope_status='scheduled; authored coverage must be explicitly verified',alignment_status='related words in brief' if hits else 'manual alignment needed; no shared words in the brief',candidate_authored_evidence=';'.join(evidence[:20]),evidence_status='literal phrase candidates only; not verified coverage',required_action='Verify this named topic is materially tested in an authored stem, solution or labelled distractor; reassign if the brief cannot address it.')
extra=['syllabus_scope_ids','syllabus_targets','syllabus_anchor','source_json','source_question_sha256','semantic_review_status','required_before_authoring','plan_updated']
plan=[]
for r in slots:
 out=dict(r);key=int(r['test']),int(r['question']);q,path=actual.get(key,({},''))
 out.update(syllabus_scope_ids=';'.join(owners[r['id']]),syllabus_targets='; '.join(v['official_topic'] for v in catalog if v['planned_owner']==r['id']),syllabus_anchor=q.get('syllabus_anchor','Legacy authored item; explicit fine-grained syllabus anchor must be verified') if q else 'Assigned official scope IDs; primary/contrast alignment must be checked before drafting',source_json=path,source_question_sha256=hashlib.sha256(q['question'].encode()).hexdigest() if q else'',semantic_review_status='full-bank screen and authored comparison recorded; independent review pending' if key[0] in (18,19) else 'earlier review evidence retained' if q else 'not authored; compare object, constraints, method, conclusion and distractors against entire current bank',required_before_authoring='' if q else'Validate every assigned scope ID; sharpen or replace brief; solve independently; compare PYQ demand; reject cosmetic reuse and unlisted extensions',plan_updated='2026-11-05')
 plan.append(out)
assert len(plan)==1500 and len({r['id'] for r in plan})==1500
assert all(sum(int(r['test'])==t for r in plan)==60 for t in range(1,26))
assert len({norm(r['focus']) for r in future})==360
(T/'plan_data.json').write_text(json.dumps({'plan':[list(plan[0])]+[list(r.values()) for r in plan],'coverage':[list(catalog[0])]+[list(r.values()) for r in catalog]},ensure_ascii=False))
summary={'official_named_scope_entries':len(catalog),'by_subject':dict(Counter(r['subject'] for r in catalog)),'unallocated':sum(not r['planned_owner'] for r in catalog),'future_slots':360,'wording_alignment_review_entries':sum(r['alignment_status'].startswith('manual alignment') for r in catalog),'max_scope_entries_per_future_slot':max(loads.values()),'authored_tests':19,'authored_questions':1140,'remaining_tests':6,'remaining_questions':360,'syllabus_sha256':hashlib.sha256(syll.read_bytes()).hexdigest(),'scope':'All extracted official topic phrases/sentences have a future owner. Scheduling is not proof of existing or final comprehensive question coverage; wording-only alignment flags require manual review and, where necessary, brief revision. Linear Programming is a heading-only ambiguity with no listed subtopics and remains on hold.'}
(D/'iat_coverage_plan_check.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
