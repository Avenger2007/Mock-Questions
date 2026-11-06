"""Check final metadata and record review evidence; never generate question content."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib,math,re
R=Path(__file__).resolve().parents[2];O=R/'IISER/review/tests24_25'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
allq={};papers=[]
for t in range(1,26):
 p=R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json');d=json.loads(p.read_text());papers.append((p,d))
 for q in d['questions']:allq[q['id']]=(p,q)
slots=list(csv.DictReader((R/'docs/blueprints/iat_25_test_slots.tsv').open(),delimiter='\t'))
with (R/'docs/blueprints/iat_25_test_plan.csv').open(encoding='utf-8-sig') as f:plan=list(csv.DictReader(f))
with (R/'docs/blueprints/iat_syllabus_coverage.csv').open(encoding='utf-8-sig') as f:coverage=list(csv.DictReader(f))
assert len(plan)==len(slots)==1500 and len(coverage)==640
for a,b in zip(slots,plan):
 assert all(a[k]==b[k] for k in a)
 p,q=allq[a['id']];assert a['focus']==q['sub_topic'];assert b['source_question_sha256']==hashlib.sha256(q['question'].encode()).hexdigest();assert b['source_json']==str(p.relative_to(R))
ledger=json.loads((O/'syllabus_material_evidence.json').read_text())
for e in ledger:assert sha(R/e['source_json'])==e['source_json_sha256']
assert len({e['topic_id'] for e in ledger})==412 and len(ledger)==544
assert sum(not c['planned_owner'] for c in coverage)==228
summary=dict(core_rows=1500,all_core_cells_match=True,authored_question_hashes_verified=1500,unique_scope_entries=640,material_scope_entries=412,material_evidence_links=544,unresolved_evidence_entries=228,future_slots=0,ledger_source_hashes_verified=True,plan_csv_sha256=sha(R/'docs/blueprints/iat_25_test_plan.csv'),coverage_csv_sha256=sha(R/'docs/blueprints/iat_syllabus_coverage.csv'))
dump(O/'plan_consistency.json',summary)
# Fresh retrieval includes all earlier current-batch questions as well as Tests1–23.
vectors={i:Counter(re.findall('[a-z]{3,}',(q['question']+' '+q['sub_topic']).lower())) for i,(p,q) in allq.items()};norms={i:math.sqrt(sum(v*v for v in c.values())) for i,c in vectors.items()};out=[]
for i,(p,q) in sorted(allq.items()):
 if int(i[7:9])<24:continue
 v=vectors[i];rank=[]
 for j,(op,oq) in allq.items():
  if j>=i or q['subject']!=oq['subject']:continue
  w=vectors[j];score=sum(n*w[k] for k,n in v.items())/(norms[i]*norms[j]);rank.append((score,j,oq,op))
 out.append(dict(id=i,focus=q['sub_topic'],source_json_sha256=sha(p),nearest_wording_candidates=[dict(id=j,question=o['question'],explanation=o['explanation'],sub_topic=o['sub_topic'],score=round(sc,4),source_json_sha256=sha(op)) for sc,j,o,op in sorted(rank,key=lambda z:-z[0])[:3]],scope='Text retrieval aid only; not semantic-originality certification.'))
dump(O/'nearest_wording_candidates.json',out)
# Explicit final visual review record and source binding.
visual=[]
for t in [24,25]:
 p=R/f'IISER/review/IAT_NEW_TEST_{t}.pdf';rc=json.loads((R/f'IISER/review/IAT_NEW_TEST_{t}_render_check.json').read_text())
 visual.append(dict(test=t,pdf_pages=rc['pdf_pages'],pdf_sha256=sha(p),all_page_thumbnails_inspected=True,changed_final_solution_pages_reinspected=True,selected_full_page_derivations_inspected=True,figures_inspected=True,observed_clipping_or_overlap=False,html_browser_layout_checked=False,scope='Visual layout review plus strict text/math checks; not an independent subject review.'))
dump(O/'visual_review.json',visual)
# Bring the once-pilot-only index up to the complete authored series.
idx=json.loads((R/'IISER/series_index.json').read_text());idx.update(total_papers=25,total_questions=1500,approved_papers=0,status='all_25_authored_review_drafts; independent review and scope evidence reconciliation pending',current_branch='iat-tests-24-25',papers=[])
for p,d in papers:
 t=d['test_number'];stem='IAT_TEST_1' if t==1 else f'IAT_NEW_TEST_{t}';pdf=R/f'IISER/review/{stem}.pdf';assert pdf.is_file()
 idx['papers'].append(dict(test_number=t,test_id=d['test_id'],file=str(p.relative_to(R)),source_sha256=sha(p),review_pdf=str(pdf.relative_to(R)),status=d['status'],total_questions=60,questions_per_subject=15,difficulty=dict(Counter(q['difficulty'] for q in d['questions'])),images=sum('image_reference' in q for q in d['questions'])))
dump(R/'IISER/series_index.json',idx)
# Compare to original reservations without rewriting their historical register.
import subprocess
baseline=subprocess.check_output(['git','show','a46c8f1:docs/blueprints/iat_25_test_slots.tsv'],text=True,cwd=R)
old={r['id']:r for r in csv.DictReader(baseline.splitlines(),delimiter='\t')}
dump(O/'reservation_reconciliation.json',[dict(id=r['id'],reserved_angle=old[r['id']]['focus'],authored_angle=r['focus'],reason='Final task sharpened after syllabus, prior-bank and solution comparison; fixed ID and chapter allocation retained.') for r in slots if int(r['test'])>=24 and old[r['id']]['focus']!=r['focus']])
print('Verified1500 core rows and hashes; refreshed120 retrieval records; indexed25 papers; recorded final visual QA.')
