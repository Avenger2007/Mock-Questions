"""Bind final deliveries and review evidence; never generate question content."""
import csv,hashlib,json,re,subprocess,sys
from collections import Counter
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R))
from validate_iat import validate
O=R/'IISER/review/tests24_25';O.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
sources=[R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json') for t in range(1,26)]
results=[validate(p) for p in sources];assert all(not r['errors'] for r in results)
save('series_structural_validation.json',results)
old=[]
for p in sources[:23]:
 digest=hashlib.sha256(subprocess.check_output(['git','show','a46c8f1:'+str(p.relative_to(R))],cwd=R)).hexdigest()
 assert sha(p)==digest,p
 old.append(dict(source=str(p.relative_to(R)),sha256=digest,unchanged=True))
save('previous_tests_unchanged.json',old)
specs=json.loads((R/'IISER/authoring/tests24_25_images.json').read_text())
slots={r['id']:r for r in csv.DictReader((R/'docs/blueprints/iat_25_test_slots.tsv').open(),delimiter='\t')}
cal=list(csv.DictReader((R/'IISER/authoring/tests24_25_math_calibration.tsv').open(),delimiter='\t'))
refs={(q['year'],q['question_number']):q for q in json.loads((R/'docs/blueprints/iat_pyq_ledger.json').read_text()) if q['subject']=='M'}
assert len(cal)==30 and len({(r['test'],r['question']) for r in cal})==30
for r in cal:
 q=refs[int(r['pyq_year']),int(r['pyq_math_question'])]
 r.update(source_pdf=q['source_pdf'],pdf_page=q['pdf_page'],scope='Editorial comparison; timing estimates are not measured.')
save('math_pyq_calibration.json',cal)
checks=json.loads((O/'calculation_checks.json').read_text());assert checks['passed']==checks['total']==127
for p,digest in checks['source_sha256'].items():assert sha(R/p)==digest
manifest=[];signatures=[];coverage=[]
for t in [24,25]:
 p=R/f'IISER/IAT NEW TEST {t}.json';d=json.loads(p.read_text());stem=f'IAT_NEW_TEST_{t}'
 rc=json.loads((R/'IISER/review'/f'{stem}_render_check.json').read_text())
 hc=json.loads((R/'IISER/review'/f'{stem}_html_check.json').read_text())
 assert rc['source_json_sha256']==hc['source_json_sha256']==sha(p)
 assert rc['questions']==rc['solutions']==60 and rc['layout_warnings']==rc['empty_pages']==0
 delivery={k:R/'IISER/review'/f'{stem}.{k}' for k in ['json','pdf','html']}
 assert delivery['json'].read_bytes()==p.read_bytes()
 assert rc['pdf_sha256']==sha(delivery['pdf']) and hc['html_sha256']==sha(delivery['html'])
 assert hc['strict_math_parse'] and not hc['browser_layout_checked']
 for name,digest in rc['image_sha256'].items():
  ip=R/d['image_base_path']/name;assert sha(ip)==digest
  with Image.open(ip) as im:assert im.size==(1200,900)
 keys=''.join(q['correct_option'] for q in d['questions'])
 assert not any(keys==''.join(keys[i%n] for i in range(60)) for n in [1,2,3,4]),'Cyclic answer pattern'
 for q in d['questions']:
  slot=slots[q['id']];assert q['topic']==slot['chapter'] and q['difficulty']==slot['difficulty_target']
  assert q['sub_topic']==slot['focus'] and q['syllabus_anchor']
  exp=q['explanation'];method=exp.split('Formula/Principle:',1)[1].split('\nStep ',1)[0].strip() if 'Formula/Principle:' in exp else exp.split('Why:',1)[1].split('\nWhy not',1)[0].strip()
  signatures.append(dict(id=q['id'],source_question_sha256=hashlib.sha256(q['question'].encode()).hexdigest(),
   syllabus_anchor=q['syllabus_anchor'],reasoning_focus=q['sub_topic'],object_constraints_and_requested_result=q['question'],
   governing_method_or_causal_mechanism=method,distractor_mechanisms=exp.split('Why not the others:',1)[1].split('\nKey point:',1)[0].strip()))
 for sec in 'BCMP':
  qs=[q for q in d['questions'] if q['section']==sec]
  coverage.append(dict(test=t,subject=sec,chapter_counts=dict(Counter(q['topic'] for q in qs)),images=sum('image_reference' in q for q in qs),tiers=dict(Counter(q['difficulty'] for q in qs))))
 manifest.append(dict(test=t,source=str(p.relative_to(R)),source_sha256=sha(p),delivery_sha256={k:sha(v) for k,v in delivery.items()},
  image_sha256=rc['image_sha256'],pdf_pages=rc['pdf_pages'],strict_math_expressions=hc['math_expressions'],browser_layout_checked=False))
save('method_signatures.json',signatures);save('chapter_style_coverage.json',coverage)
save('final_manifest.json',dict(baseline='a46c8f180273d2bc44f7be27eb125873d97a2807',papers=manifest,previous_1380_unchanged=True,
 structural_questions=1500,calculation_checks=127,math_calibration_rows=30,images=len(specs),
 branch='iat-tests-24-25',remote_push_status=('Verified content checkpoint '+json.loads((O/'remote_preservation.json').read_text())['verified_content_commit']+' on iat-tests-24-25; verify later pushes separately' if (O/'remote_preservation.json').exists() else 'Remote preservation not independently verified'),release_status='Authored review drafts; independent hidden-key academic and timed review pending.'))
print('Verified 25 papers / 1500 questions; 120 new deliveries; 127 calculation checks; 18 images; previous 1380 unchanged.')
