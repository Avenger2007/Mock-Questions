"""Bind correction evidence and delivery hashes to the current canonical sources."""
import csv,hashlib,json,subprocess
from collections import Counter
from pathlib import Path
import sys
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R))
from validate_iat import validate
O=R/'IISER/review/milestone15_fixes';O.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,d):(O/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
slots=list(csv.DictReader((R/'docs/blueprints/iat_25_test_slots.tsv').open(),delimiter='\t'))
slot_by_id={r['id']:r for r in slots};ledger=[];manifest=[];validation=[];coverage=[];aliases=[]
# Explicit legacy names, including old combined headings, are reported rather than
# silently treated as an independently reviewed primary-topic classification.
legacy={
 'Basic counting techniques':{'Permutations and Combinations'},
 'Sets and Logic':{'Relations & functions'},
 'Sets, Relations and Functions':{'Relations & functions'},
 'Complex numbers, linear and quadratic equations':{'Complex Numbers','Quadratic Equations'},
 'Statistics, Probability & Linear Programming':{'Statistics','Probability'},
 'Differential Calculus':{'Differentiation'},'Integral Calculus':{'Integration'},
 'Matrices and Determinants':{'Matrices & determinants'},
 'Sequences and Series':{'Sequences & series'},'Limits and Continuity':{'Limit & continuity'},
 'Relations and Functions':{'Relations & functions'},'Vector Algebra':{'Vectors'},
 'Electric Charges and Fields':{'Electric Charges and Fields / Electrostatic Potential'},
 'Moving Charges and Magnetism':{'Moving Charges and Magnetism / Magnetism and Matter'},
 'Motion in a Straight Line':{'Motion in a Straight Line / Motion in a Plane'},
 'Motion in a Plane':{'Motion in a Straight Line / Motion in a Plane'},
 'Structure of Atom':{'Structure of the Atom'},
 'Alcohols, Phenols and Ethers':{'Alcohols, phenols, and ethers'},
 'The d- and f-Block Elements':{'The d- & f-block elements'},
 'Aldehydes, Ketones and Carboxylic Acids':{'Aldehydes, ketones, and carboxylic acids'},
 'Semiconductor Electronics: Materials, Devices and Simple Circuits':{'Semiconductor Electronics'},
 'Classification of Elements and Periodicity':{'Classification of Elements and Periodicity in Properties'},
 'Atoms and Nuclei':{'Nuclei'},
}
def family(q):
 planned=slot_by_id[q['id']]['chapter'];old=q['topic']
 assert old.casefold()==planned.casefold() or planned in legacy.get(old,set()),(q['id'],old,planned)
 return planned
for t in range(1,16):
 p=R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json')
 d=json.loads(p.read_text());before=json.loads(subprocess.check_output(['git','show','f06d700:'+str(p.relative_to(R))],cwd=R))
 stem='IAT_TEST_1' if t==1 else f'IAT_NEW_TEST_{t}';v=validate(p);assert not v['errors'],v;validation.append(v)
 assert [(q['id'],q['correct_option']) for q in d['questions']]==[(q['id'],q['correct_option']) for q in before['questions']]
 for q,b in zip(d['questions'],before['questions']):
  fields=[k for k in sorted(set(q)|set(b)) if q.get(k)!=b.get(k)]
  if fields:ledger.append(dict(id=q['id'],changed_fields=fields,syllabus_anchor=q.get('syllabus_anchor',q['sub_topic']),difficulty=q['difficulty'],correct_option=q['correct_option']))
  family(q)
  if q['topic']!=slot_by_id[q['id']]['chapter']:
   aliases.append(dict(id=q['id'],canonical_label=q['topic'],reserved_family=family(q)))
  assert q['difficulty']==slot_by_id[q['id']]['difficulty_target'],q['id']
 paths={ext:R/'IISER/review'/f'{stem}.{ext}' for ext in ['json','pdf','html']}
 assert p.read_bytes()==paths['json'].read_bytes()
 render=json.loads((R/'IISER/review'/f'{stem}_render_check.json').read_text())
 html=json.loads((R/'IISER/review'/f'{stem}_html_check.json').read_text())
 assert render['source_json_sha256']==html['source_json_sha256']==sha(p)
 assert render['pdf_sha256']==sha(paths['pdf']) and html['html_sha256']==sha(paths['html'])
 assert render['questions']==render['solutions']==60 and render['layout_warnings']==render['empty_pages']==0
 assert html['strict_math_parse'] and not html['browser_layout_checked']
 images={name:sha(R/d['image_base_path']/name) for name in render['image_sha256']}
 assert images==render['image_sha256']
 manifest.append(dict(test=t,source=str(p.relative_to(R)),source_sha256=sha(p),delivery_sha256={k:sha(v) for k,v in paths.items()},image_sha256=images,pdf_pages=render['pdf_pages'],questions=60,solutions=60,strict_math_parse=True,browser_layout_checked=False))
 for sec in 'BCMP':
  raw=Counter(q['topic'] for q in d['questions'] if q['section']==sec)
  actual=Counter(family(q) for q in d['questions'] if q['section']==sec)
  planned=Counter(r['chapter'] for r in slots if int(r['test'])==t and r['subject']==sec)
  assert actual==planned
  coverage.append(dict(test=t,subject=sec,canonical_raw_topic_counts=dict(raw),canonical_family_counts_after_legacy_name_mapping=dict(actual),reserved_primary_topic_counts=dict(planned),match=True))
save('item_change_ledger.json',ledger)
save('structural_validation.json',validation)
save('chapter_coverage.json',dict(scope='Canonical topic metadata versus reserved families after explicit legacy-name mapping, not independent retagging of all 900 solved tasks. Broad combined legacy headings use their existing ID-specific reservation; no linear-programming question is inferred from that old heading.',legacy_label_mappings=aliases,comparisons=coverage))
save('final_manifest.json',dict(source_baseline_commit='f06d700f1c38516efc7187dc2a5758550afc1e9c',papers=manifest))
save('math_parse.json',dict(expressions=sum(json.loads((R/'IISER/review'/('IAT_TEST_1_html_check.json' if t==1 else f'IAT_NEW_TEST_{t}_html_check.json')).read_text())['math_expressions'] for t in range(1,16)),errors=[],papers=15,strict_math_parse=True,browser_layout_checked=False))
summary=dict(changed_items=len(ledger),field_changes=dict(Counter(k for r in ledger for k in r['changed_fields'])),papers=15,questions=900,pdf_pages=sum(r['pdf_pages'] for r in manifest),linked_images=sum(len(r['image_sha256']) for r in manifest),ids_order_keys_preserved=True)
save('change_summary.json',summary)
(R/'IISER/review/IAT_TEST_1_validation.json').write_text(json.dumps([validation[0]],indent=2)+'\n')
print(json.dumps(summary,indent=2))
