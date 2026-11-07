"""Reconcile the completed 25-test metadata and limited scope evidence; never author questions."""
import csv,json,hashlib
from pathlib import Path
from collections import defaultdict,Counter
R=Path(__file__).resolve().parents[2];D=R/'docs/blueprints';O=R/'IISER/review/tests24_25';T=R/'tmp/iat_plan';T.mkdir(exist_ok=True,parents=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prior=json.loads((D/'iat_coverage_plan_check.json').read_text())
if prior.get('plan_csv_sha256') and sha(D/'iat_25_test_plan.csv')!=prior['plan_csv_sha256']:raise SystemExit('Manual plan CSV edits require reconciliation before rebuilding.')
slots=list(csv.DictReader((D/'iat_25_test_slots.tsv').open(),delimiter='\t'));fields=list(slots[0]);lookup={r['id']:r for r in slots};actual={}
for t in range(1,26):
 p=R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json')
 for q in json.loads(p.read_text())['questions']:
  actual[q['id']]=(q,p);r=lookup[q['id']];r.update(focus=q['sub_topic'],dominant_style_target=q['format'],difficulty_target=q['difficulty'],state='authored review draft; independent academic and timed review pending')
with (D/'iat_25_test_slots.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(slots)
with (D/'iat_syllabus_coverage.csv').open(encoding='utf-8-sig') as f:catalog=list(csv.DictReader(f))
assert len(catalog)==640 and len({r['topic_id'] for r in catalog})==640
ledger=json.loads((R/'IISER/review/tests22_23/syllabus_material_evidence.json').read_text())
for e in ledger:assert sha(R/e['source_json'])==e['source_json_sha256']
# Explicit mappings concern the material aspect assessed, not every detail in a broad phrase.
mappings={
(24,1):'B-011',(24,2):'B-022',(24,3):'B-038',(24,4):'B-057 B-058',(24,5):'B-089',(24,6):'B-109 B-110 B-112',(24,7):'B-117',(24,8):'B-140',(24,9):'B-151 B-152',(24,10):'B-156',(24,11):'B-114 B-115',(24,12):'B-116',(24,13):'B-070',(24,14):'B-026',(24,15):'B-161',
(25,1):'B-002 B-005',(25,2):'B-012',(25,3):'B-026 B-028',(25,4):'B-055',(25,5):'B-091 B-092',(25,6):'B-104',(25,7):'B-122',(25,8):'B-140',(25,9):'B-152',(25,10):'B-163',(25,11):'B-114 B-115',(25,12):'B-083',(25,13):'B-081',(25,14):'B-039 B-040',(25,15):'B-108',
(24,16):'C-034 C-035',(24,17):'C-045 C-050',(24,18):'C-040 C-076',(24,19):'C-023 C-024 C-027',(24,20):'C-018',(24,21):'C-008 C-013',(24,22):'C-104',(24,23):'C-103 C-110',(24,24):'C-121',(24,25):'C-125 C-131 C-136',(24,26):'C-153 C-149',(24,27):'C-070 C-071',(24,28):'C-080',(24,29):'C-089',(24,30):'C-057 C-058',
(25,16):'C-032',(25,17):'C-045 C-047',(25,18):'C-029 C-054 C-057',(25,19):'C-016 C-017',(25,20):'C-106',(25,21):'C-129',(25,22):'C-146 C-147',(25,23):'C-152',(25,24):'C-096 C-097',(25,25):'C-060',(25,26):'C-074 C-075',(25,27):'C-057 C-058',(25,28):'C-079',(25,29):'C-110 C-112',(25,30):'C-119 C-120',
(24,31):'M-059 M-062 M-065',(24,32):'M-064 M-092 M-095',(24,33):'M-093 M-094 M-095',(24,34):'M-101',(24,35):'M-014 M-015 M-016',(24,36):'M-051 M-052 M-055',(24,37):'M-112 M-114',(24,38):'M-023',(24,39):'M-076 M-078',(24,40):'M-082 M-084 M-086',(24,41):'M-067 M-074',(24,42):'M-020',(24,43):'M-027 M-029',(24,44):'M-104 M-106',(24,45):'M-037',
(25,31):'M-064',(25,32):'M-095',(25,33):'M-095',(25,34):'M-097 M-101 M-102',(25,35):'M-012 M-013 M-014',(25,36):'M-044 M-048',(25,37):'M-050 M-021',(25,38):'M-114',(25,39):'M-019',(25,40):'M-021 M-077',(25,41):'M-076 M-079 M-032',(25,42):'M-032 M-027 M-029',(25,43):'M-110',(25,44):'M-106',(25,45):'M-014 M-085 M-086 M-088',
(24,46):'P-028 P-034',(24,47):'P-003 P-004 P-005',(24,48):'P-064 P-065',(24,49):'P-040 P-043 P-044 P-045 P-046',(24,50):'P-077 P-078 P-079 P-081',(24,51):'P-095',(24,52):'P-100 P-101 P-102',(24,53):'P-112 P-119',(24,54):'P-137 P-138',(24,55):'P-201',(24,56):'P-158 P-159 P-160',(24,57):'P-174 P-176',(24,58):'P-163 P-164 P-166 P-168',(24,59):'P-203 P-204',(24,60):'P-183',
(25,46):'P-020 P-024',(25,47):'P-028 P-034',(25,48):'P-048 P-052',(25,49):'P-058 P-060',(25,50):'P-069',(25,51):'P-085 P-087 P-090',(25,52):'P-094 P-096',(25,53):'P-126 P-127 P-130',(25,54):'P-154 P-155',(25,55):'P-108 P-109 P-114',(25,56):'P-138 P-139',(25,57):'P-178',(25,58):'P-172 P-185 P-186 P-187 P-189 P-190',(25,59):'P-193 P-194 P-195',(25,60):'P-150 P-158 P-159 P-162'}
cat={c['topic_id']:c for c in catalog};pairs={(e['topic_id'],e['question_id']) for e in ledger}
for (t,n),ids in mappings.items():
 q,p=actual[f'IAT27-T{t:02}-Q{n:02}']
 for tid in ids.split():
  assert tid in cat and tid[0]==q['section']
  if (tid,q['id']) in pairs:continue
  ledger.append(dict(topic_id=tid,official_topic=cat[tid]['official_topic'],question_id=q['id'],material_aspect=q['sub_topic'],source_json=str(p.relative_to(R)),source_json_sha256=sha(p),scope='Author mapping of the assessed aspect only; not exhaustive phrase coverage or independent approval.'));pairs.add((tid,q['id']))
bytopic=defaultdict(list);byq=defaultdict(list)
for e in ledger:bytopic[e['topic_id']].append(e);byq[e['question_id']].append(e['topic_id'])
residual=[]
for c in catalog:
 c.setdefault('prior_reserved_owner',c['planned_owner'])
 if bytopic[c['topic_id']]:
  es=bytopic[c['topic_id']];q,p=actual[es[0]['question_id']]
  c.update(planned_owner=q['id'],planned_angle=q['sub_topic'],scope_status='material aspect evidenced; residual breadth and academic approval pending',candidate_authored_evidence=';'.join(e['question_id'] for e in es),evidence_status='explicit aspect mappings with source hashes; not comprehensive coverage',required_action='Review remaining breadth of the full phrase and verify the mapped item independently.')
 else:
  c.update(planned_owner='',planned_angle='',scope_status='evidence mapping unresolved after 25 authored drafts; not a proven content gap',evidence_status='Earlier phrase candidates or reservations do not establish actual coverage',required_action='Review actual Tests1–25 for explicit evidence; if absent, revise an existing fixed-ID question and its deliveries. No future test reservation remains.')
  residual.append(c.copy())
plan=[]
for r in slots:
 q,p=actual[r['id']];v=dict(r);scope_ids=sorted(set(byq[q['id']]))
 v.update(syllabus_scope_ids=';'.join(scope_ids),syllabus_targets='; '.join(cat[i]['official_topic'] for i in scope_ids),syllabus_anchor=q.get('syllabus_anchor','Legacy item: verify exact scope anchor'),source_json=str(p.relative_to(R)),source_question_sha256=hashlib.sha256(q['question'].encode()).hexdigest(),semantic_review_status='author comparison recorded; independent semantic review pending' if int(r['test'])>=24 else 'earlier review evidence retained; not re-certified',required_before_authoring='',plan_updated='2026-11-06');plan.append(v)
assert len(plan)==1500 and len({p['id'] for p in plan})==1500
(T/'plan_data.json').write_text(json.dumps({'plan':[list(plan[0])]+[list(r.values()) for r in plan],'coverage':[list(catalog[0])]+[list(r.values()) for r in catalog]},ensure_ascii=False))
(O/'syllabus_material_evidence.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
(O/'scope_evidence_unresolved.json').write_text(json.dumps(dict(entries=residual,note='Unmapped means incomplete evidence accounting, not proof a topic is absent. Broad printed phrases may still have untested details even when mapped.'),ensure_ascii=False,indent=2)+'\n')
summary=dict(official_named_scope_entries=640,by_subject=dict(Counter(c['subject'] for c in catalog)),authored_tests=25,authored_questions=1500,remaining_tests=0,remaining_questions=0,future_slots=0,explicit_material_evidence_entries=len({e['topic_id'] for e in ledger}),material_evidence_links=len(ledger),unresolved_evidence_entries=len(residual),unallocated=len(residual),syllabus_sha256=sha(R/'IISER/IISER_Aptitude_Test_Syllabus_2026.md'),scope='All25 review drafts authored. Evidence mapping is incomplete; blank owners identify unresolved mapping, not certified missing content. Mapped aspects do not certify exhaustive coverage. Independent review and target-year notification verification remain pending.')
(D/'iat_coverage_plan_check.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
