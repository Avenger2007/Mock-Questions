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
 if int(row['test'])<=23:continue
 angles=row['ordered_angle_briefs'].split('|');assert len(angles)==15,(row['test'],row['subject'],len(angles))
 start='BCMP'.index(row['subject'])*15+1
 for n,angle in enumerate(angles,start):lookup[int(row['test']),n].update(focus=angle,angle_seed='Reserved original task: '+angle,state='concrete reservation; syllabus and semantic review required before authorship')
actual={}
for test in range(1,24):
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
material={'B-001': [20, 1], 'B-012': [21, 2], 'B-013': [21, 2], 'B-017': [20, 2], 'B-018': [21, 15], 'B-026': [20, 14], 'B-030': [20, 14], 'B-040': [20, 14], 'B-034': [21, 14], 'B-035': [21, 14], 'B-054': [20, 4], 'B-058': [21, 4], 'B-059': [21, 4], 'B-061': [21, 4], 'B-084': [21, 13], 'B-085': [21, 13], 'B-086': [21, 13], 'B-066': [21, 5], 'B-087': [21, 5], 'B-088': [21, 5], 'B-090': [21, 5], 'B-068': [20, 5], 'B-106': [20, 15], 'B-102': [20, 6], 'B-110': [20, 6], 'B-129': [20, 7], 'B-133': [20, 11], 'B-119': [21, 11], 'B-138': [21, 12], 'B-139': [20, 8], 'B-145': [21, 8], 'B-150': [20, 9], 'B-152': [20, 9], 'B-153': [21, 9], 'C-009': [20, 21], 'C-013': [20, 21], 'C-010': [21, 21], 'C-015': [21, 19], 'C-017': [21, 19], 'C-021': [21, 20], 'C-022': [21, 20], 'C-028': [21, 16], 'C-034': [20, 16], 'C-038': [21, 18], 'C-039': [21, 18], 'C-040': [21, 18], 'C-054': [20, 30], 'C-055': [20, 30], 'C-061': [21, 30], 'C-064': [21, 30], 'C-068': [21, 30], 'C-073': [21, 30], 'C-062': [20, 27], 'C-069': [20, 27], 'C-072': [20, 27], 'C-082': [21, 27], 'C-085': [21, 28], 'C-091': [21, 28], 'C-087': [20, 29], 'C-111': [20, 23], 'C-122': [20, 25], 'C-125': [20, 25], 'C-123': [21, 24], 'C-149': [20, 26], 'C-148': [21, 26], 'C-150': [21, 26], 'M-010': [20, 33], 'M-017': [20, 32], 'M-028': [21, 42], 'M-026': [20, 34], 'M-031': [20, 43], 'M-035': [21, 39], 'M-036': [21, 39], 'M-039': [20, 45], 'M-044': [20, 45], 'M-049': [20, 45], 'M-040': [21, 41], 'M-045': [21, 41], 'M-050': [21, 37], 'M-053': [20, 31], 'M-058': [21, 31], 'M-063': [21, 31], 'M-065': [21, 32], 'M-066': [20, 36], 'M-068': [20, 36], 'M-069': [20, 36], 'M-075': [21, 40], 'M-082': [20, 39], 'M-087': [20, 37], 'M-096': [20, 35], 'M-097': [21, 34], 'M-100': [21, 33], 'M-109': [20, 38], 'M-111': [20, 40], 'P-004': [20, 46], 'P-005': [20, 46], 'P-007': [21, 46], 'P-009': [21, 46], 'P-012': [21, 46], 'P-016': [21, 46], 'P-023': [20, 47], 'P-026': [21, 47], 'P-029': [21, 47], 'P-032': [21, 47], 'P-036': [21, 48], 'P-039': [21, 48], 'P-043': [21, 48], 'P-056': [20, 48], 'P-059': [20, 48], 'P-061': [21, 49], 'P-066': [20, 49], 'P-074': [20, 49], 'P-078': [21, 50], 'P-081': [21, 50], 'P-084': [21, 50], 'P-087': [20, 50], 'P-088': [20, 50], 'P-095': [20, 51], 'P-100': [20, 52], 'P-101': [21, 51], 'P-105': [20, 53], 'P-107': [21, 53], 'P-117': [21, 54], 'P-133': [20, 54], 'P-139': [21, 55], 'P-140': [21, 55], 'P-143': [21, 56], 'P-161': [20, 55], 'P-163': [20, 56], 'P-167': [20, 56], 'P-164': [21, 57], 'P-166': [21, 57], 'P-170': [19, 59], 'P-171': [21, 59], 'P-174': [20, 57], 'P-176': [20, 57], 'P-182': [20, 58], 'P-197': [21, 60], 'P-199': [21, 60], 'P-207': [20, 60], 'C-025': [21, 20], 'C-131': [21, 23], 'C-143': [21, 25]}
batch_material={'B-011': [22, 1], 'B-024': [22, 2], 'B-025': [22, 2], 'B-029': [22, 3], 'B-041': [22, 4], 'B-042': [22, 4], 'B-044': [22, 4], 'B-078': [22, 5], 'B-093': [22, 5], 'B-099': [22, 6], 'B-100': [22, 6], 'B-121': [22, 7], 'B-148': [22, 8], 'B-149': [22, 8], 'B-127': [22, 9], 'B-153': [22, 9], 'B-160': [22, 10], 'B-124': [22, 11], 'B-128': [22, 12], 'B-065': [22, 13], 'B-037': [22, 14], 'B-053': [22, 15], 'B-056': [22, 15], 'B-022': [23, 2], 'B-040': [23, 3], 'B-048': [23, 4], 'B-092': [23, 5], 'B-113': [23, 6], 'B-125': [23, 7], 'B-126': [23, 7], 'B-143': [23, 8], 'B-154': [23, 9], 'B-155': [23, 9], 'B-163': [23, 10], 'B-136': [23, 11], 'B-130': [23, 12], 'B-063': [23, 13], 'B-036': [23, 14], 'B-120': [23, 14], 'B-152': [23, 15], 'C-036': [22, 16], 'C-049': [22, 17], 'C-052': [22, 18], 'C-053': [22, 18], 'C-131': [23, 23], 'C-092': [22, 20], 'C-141': [22, 21], 'C-143': [22, 21], 'C-076': [22, 22], 'C-093': [22, 23], 'C-102': [22, 25], 'C-103': [22, 25], 'C-081': [23, 25], 'C-083': [22, 26], 'C-011': [22, 27], 'C-013': [22, 27], 'C-020': [22, 28], 'C-021': [22, 28], 'C-151': [22, 29], 'C-071': [22, 30], 'C-033': [23, 16], 'C-047': [23, 17], 'C-019': [23, 18], 'C-104': [23, 19], 'C-112': [23, 20], 'C-127': [23, 22], 'C-144': [23, 24], 'C-146': [23, 24], 'C-147': [23, 24], 'C-086': [23, 26], 'C-094': [23, 27], 'C-095': [23, 27], 'C-063': [23, 29], 'C-066': [23, 29], 'C-041': [23, 30], 'C-042': [23, 30], 'M-064': [22, 31], 'M-103': [22, 31], 'M-091': [22, 32], 'M-098': [22, 33], 'M-009': [22, 34], 'M-010': [22, 34], 'M-051': [22, 35], 'M-114': [22, 36], 'M-019': [22, 37], 'M-021': [22, 38], 'M-078': [22, 39], 'M-081': [22, 39], 'M-083': [22, 40], 'M-087': [22, 40], 'M-088': [22, 40], 'M-106': [22, 41], 'M-070': [23, 36], 'M-074': [22, 42], 'M-048': [23, 45], 'M-109': [23, 38], 'M-037': [22, 45], 'M-054': [23, 31], 'M-018': [23, 32], 'M-012': [23, 33], 'M-029': [23, 34], 'M-099': [23, 35], 'M-069': [23, 36], 'M-092': [23, 37], 'M-082': [23, 39], 'M-084': [23, 39], 'M-115': [23, 40], 'M-116': [23, 40], 'M-038': [23, 41], 'M-108': [23, 42], 'M-031': [23, 43], 'M-057': [23, 44], 'M-060': [23, 44], 'M-041': [23, 45], 'M-075': [23, 45], 'P-002': [22, 46], 'P-020': [22, 47], 'P-024': [22, 47], 'P-025': [23, 47], 'P-057': [22, 48], 'P-059': [22, 48], 'P-073': [22, 49], 'P-087': [22, 50], 'P-088': [22, 50], 'P-091': [22, 51], 'P-092': [22, 51], 'P-098': [22, 52], 'P-100': [22, 52], 'P-102': [22, 52], 'P-111': [22, 53], 'P-115': [22, 53], 'P-139': [22, 54], 'P-161': [22, 55], 'P-168': [22, 56], 'P-169': [22, 56], 'P-178': [22, 57], 'P-182': [22, 58], 'P-183': [22, 58], 'P-191': [22, 59], 'P-205': [22, 60], 'P-006': [23, 46], 'P-032': [23, 47], 'P-027': [23, 48], 'P-030': [23, 48], 'P-037': [23, 49], 'P-041': [23, 49], 'P-052': [23, 50], 'P-053': [23, 50], 'P-055': [23, 50], 'P-065': [23, 51], 'P-078': [23, 52], 'P-079': [23, 52], 'P-080': [23, 52], 'P-109': [23, 53], 'P-116': [23, 53], 'P-121': [23, 53], 'P-125': [23, 54], 'P-128': [23, 54], 'P-130': [23, 54], 'P-144': [23, 55], 'P-157': [23, 56], 'P-160': [23, 56], 'P-174': [23, 57], 'P-175': [23, 57], 'P-177': [23, 57], 'P-181': [23, 58], 'P-194': [23, 59], 'P-196': [23, 59], 'P-201': [23, 60], 'C-056': [23, 28], 'C-136': [22, 24], 'C-120': [23, 21], 'P-043': [23, 49]}
for topic_id,coords in batch_material.items():material.setdefault(topic_id,coords)
future=[r for r in slots if int(r['test'])>=24];loads=Counter();owners=defaultdict(list)
for leaf in catalog:
 candidates=[r for r in future if r['subject']==leaf['subject'] and r['chapter_code']==leaf['chapter_code']]
 words=tokens(leaf['official_topic']+' '+leaf['official_parent'])
 def score(r):return len(words&tokens(r['focus']))/(max(1,len(words))**.5)-.10*loads[r['id']]
 overrides={'B-036':(23,14),'B-072':(24,13),'B-070':(24,13),'B-071':(24,13),'P-172':(25,58)}
 forced=material.get(leaf['topic_id'],overrides.get(leaf['topic_id']))
 chosen=lookup[tuple(forced)] if forced else max(candidates,key=score);hits=words&tokens(chosen['focus']);loads[chosen['id']]+=1;owners[chosen['id']].append(leaf['topic_id'])
 # A text-evidence candidate is disclosed as such, never marked academically covered by a word match.
 evidence=[]
 phrase=norm(leaf['official_topic'])
 for (test,n),(q,path) in actual.items():
  if q['section']!=leaf['subject']:continue
  hay=norm(q['question']+' '+q['explanation']+' '+q.get('syllabus_anchor',''))
  if len(phrase)>8 and phrase in hay:evidence.append(q['id'])
 leaf.update(planned_owner=chosen['id'],planned_angle=chosen['focus'],scope_status='scheduled; authored coverage must be explicitly verified',alignment_status='related words in brief' if hits else 'manual alignment needed; no shared words in the brief',candidate_authored_evidence=';'.join(evidence[:20]),evidence_status='literal phrase candidates only; not verified coverage',required_action='Verify this named topic is materially tested in an authored stem, solution or labelled distractor; reassign if the brief cannot address it.')
# Explicit author mappings evidence only the aspect actually tested, not every fact in a broad printed phrase.
material_ledger=[]
for leaf in catalog:
 if leaf['topic_id'] not in material:continue
 coords=[material[leaf['topic_id']]]
 if leaf['topic_id'] in batch_material and batch_material[leaf['topic_id']] not in coords:coords.append(batch_material[leaf['topic_id']])
 evidence_ids=[]
 for test,n in coords:
  q,path=actual[test,n];evidence_ids.append(q['id'])
  material_ledger.append(dict(topic_id=leaf['topic_id'],official_topic=leaf['official_topic'],question_id=q['id'],material_aspect=q['sub_topic'],source_json=path,source_json_sha256=hashlib.sha256((R/path).read_bytes()).hexdigest(),scope='Material evidence for this aspect only; broad printed phrases can retain untested details.'))
 leaf.update(scope_status='material aspect evidenced; comprehensive breadth not certified',candidate_authored_evidence=';'.join(evidence_ids),evidence_status='explicit author mappings to actual items; independent scope review pending',required_action='Check recorded aspects and residual breadth of the full printed phrase before final series coverage approval.')
(R/'IISER/review/tests22_23/syllabus_material_evidence.json').write_text(json.dumps(material_ledger,ensure_ascii=False,indent=2)+'\n')
extra=['syllabus_scope_ids','syllabus_targets','syllabus_anchor','source_json','source_question_sha256','semantic_review_status','required_before_authoring','plan_updated']
plan=[]
for r in slots:
 out=dict(r);key=int(r['test']),int(r['question']);q,path=actual.get(key,({},''))
 out.update(syllabus_scope_ids=';'.join(owners[r['id']]),syllabus_targets='; '.join(v['official_topic'] for v in catalog if v['planned_owner']==r['id']),syllabus_anchor=q.get('syllabus_anchor','Legacy authored item; explicit fine-grained syllabus anchor must be verified') if q else 'Assigned official scope IDs; primary/contrast alignment must be checked before drafting',source_json=path,source_question_sha256=hashlib.sha256(q['question'].encode()).hexdigest() if q else'',semantic_review_status='full-bank screen and authored comparison recorded; independent review pending' if key[0] in (18,19,20,21,22,23) else 'earlier review evidence retained' if q else 'not authored; compare object, constraints, method, conclusion and distractors against entire current bank',required_before_authoring='' if q else'Validate every assigned scope ID; sharpen or replace brief; solve independently; compare PYQ demand; reject cosmetic reuse and unlisted extensions',plan_updated='2026-11-06')
 plan.append(out)
assert len(plan)==1500 and len({r['id'] for r in plan})==1500
assert all(sum(int(r['test'])==t for r in plan)==60 for t in range(1,26))
assert len({norm(r['focus']) for r in future})==120
(T/'plan_data.json').write_text(json.dumps({'plan':[list(plan[0])]+[list(r.values()) for r in plan],'coverage':[list(catalog[0])]+[list(r.values()) for r in catalog]},ensure_ascii=False))
summary={'official_named_scope_entries':len(catalog),'by_subject':dict(Counter(r['subject'] for r in catalog)),'unallocated':sum(not r['planned_owner'] for r in catalog),'future_slots':120,'wording_alignment_review_entries':sum(r['alignment_status'].startswith('manual alignment') for r in catalog),'max_scope_entries_per_future_slot':max(loads.values()),'authored_tests':23,'authored_questions':1380,'remaining_tests':2,'remaining_questions':120,'explicit_material_evidence_entries':len({r['topic_id'] for r in material_ledger}),'material_evidence_links':len(material_ledger),'syllabus_sha256':hashlib.sha256(syll.read_bytes()).hexdigest(),'scope':'Each extracted official phrase has either explicit material-aspect evidence or a future owner. Material evidence does not certify exhaustive breadth. Scheduling is not proof of existing or final comprehensive question coverage; wording-only alignment flags require manual review and, where necessary, brief revision. Linear Programming is a heading-only ambiguity with no listed subtopics and remains on hold.'}
(D/'iat_coverage_plan_check.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
