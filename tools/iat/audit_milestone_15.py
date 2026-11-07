"""Read-only corpus audit; diagnostics are not academic certification."""
import csv, hashlib, importlib.util, itertools, json, re, statistics, unicodedata
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'IISER/audit/milestone_15'
OUT.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('validator',ROOT/'validate_iat.py')
validator=importlib.util.module_from_spec(spec);spec.loader.exec_module(validator)
papers=[];rows=[];checks=[];render=[]
for t in range(1,16):
    path=ROOT/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json')
    data=json.loads(path.read_text());papers.append(data)
    checks.append(validator.validate(path))
    for q in data['questions']:
        exp=q['explanation'];why=exp.split('Why:',1)[1].split('Why not the others:',1)[0] if 'Why:' in exp else ''
        wrong=exp.split('Why not the others:',1)[1].split('Key point:',1)[0] if 'Why not the others:' in exp else (exp.split('Common mistake:',1)[1] if 'Common mistake:' in exp else '')
        opts=[x[3:] for x in q['options']];correct=opts['ABCD'.index(q['correct_option'])]
        rows.append(dict(test=t,id=q['id'],subject=q['section'],tier=q['difficulty'],topic=q['topic'],format=q['format'],
            image=q.get('image_reference',''),why_words=len(why.split()),missing_why_heading='Why:' not in exp,missing_wrong_heading='Why not the others:' not in exp,
            why_sentences=len(re.findall(r'[.!?](?:\s|$)',why)),
            missing_wrong_letters=''.join(a for a in 'ABCD' if a!=q['correct_option'] and f'({a})' not in wrong),
            displayed_derivation='\\[' in exp and '\\]' in exp,
            steps=len(re.findall(r'Step \d+:',exp)),
            inline_math='\\(' in exp,chem_tex='\\ce{' in exp,
            correct_is_unique_longest=len(correct)>max(len(x) for x in opts if x!=correct),
            correct_length_ratio=round(len(correct)/max(1,statistics.mean(len(x) for x in opts if x!=correct)),2),
            stem=q['question'],correct_option=q['correct_option'],selected_answer=correct,
            source_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    stem='IAT_TEST_1' if t==1 else f'IAT_NEW_TEST_{t}'
    cp=ROOT/f'IISER/review/{stem}_render_check.json'
    if cp.exists():
        c=json.loads(cp.read_text());drift=[]
        for key,target in [('source_json_sha256',path),('delivery_json_sha256',ROOT/f'IISER/review/{stem}.json'),('pdf_sha256',ROOT/f'IISER/review/{stem}.pdf')]:
            if key in c and (not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest()!=c[key]):drift.append(key)
        image_checks=c.get('image_sha256',{})
        if isinstance(image_checks,dict):
            for name,h in image_checks.items():
                ip=ROOT/data['image_base_path']/name
                if not ip.exists() or hashlib.sha256(ip.read_bytes()).hexdigest()!=h:drift.append('image:'+name)
        render.append(dict(test=t,record_exists=True,hash_drift=drift,record=c))
    else:render.append(dict(test=t,record_exists=False))

with (OUT/'question_diagnostics.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
summaries=[]
for t in range(1,16):
    rr=[r for r in rows if r['test']==t]
    summaries.append(dict(test=t,questions=len(rr),image_counts=dict(Counter(r['subject'] for r in rr if r['image'])),
        missing_MP_display=sum(not r['displayed_derivation'] and r['subject'] in 'MP' for r in rr),
        why_under_2_sentences=sum(r['why_sentences']<2 for r in rr),
        missing_individual_distractors=sum(bool(r['missing_wrong_letters']) for r in rr),
        hard_at_most_one_numbered_step=sum(r['tier']=='hard' and r['steps']<=1 for r in rr),
        C_display=sum(r['displayed_derivation'] and r['subject']=='C' for r in rr),
        inline_math=sum(r['inline_math'] for r in rr),chem_tex=sum(r['chem_tex'] for r in rr),
        correct_unique_longest=sum(r['correct_is_unique_longest'] for r in rr)))

def normal(s,masked=False):
    s=unicodedata.normalize('NFKC',s).lower().replace('−','-')
    s=re.sub(r'\\[()\[\]]','',s);s=s.replace('^{','').replace('^{-','-').replace('^','')
    s=s.replace('\\frac','frac').replace('\\sqrt','sqrt')
    if masked:s=re.sub(r'\d+(?:\.\d+)?','#',s)
    return re.sub(r'[^\w#]+','',s)
duplicates=[]
for a,b in itertools.combinations(rows,2):
    if a['subject']!=b['subject']:continue
    if normal(a['stem'])==normal(b['stem']):kind='normalised_exact'
    elif normal(a['stem'],True)==normal(b['stem'],True):kind='number_masked_exact'
    else:continue
    duplicates.append(dict(left=a['id'],right=b['id'],kind=kind,left_stem=a['stem'],right_stem=b['stem']))
result=dict(scope='900-item mechanical scan; diagnostic thresholds are not content verdicts',
    source_commit='56dd1acca318ce747a5f5c527951d7f12a38b8e0',questions=len(rows),
    structural=checks,per_test=summaries,render_records=render,normalised_duplicates=duplicates)
(OUT/'corpus_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(questions=len(rows),structural_errors=sum(len(x['errors']) for x in checks),
    per_test=summaries,normalised_duplicates=duplicates,render_drift=[{k:v for k,v in x.items() if k!='record'} for x in render if x.get('hash_drift') or not x['record_exists']]),ensure_ascii=False,indent=2))
