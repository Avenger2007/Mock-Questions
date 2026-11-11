import json,sys,glob,difflib,re,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import pol_ledger; from units import U,PART
d=json.load(open(sys.argv[1],encoding='utf-8')); src=d['q']; C=collections.Counter
print(len(src),'diff',dict(C(q['difficulty'] for q in src)),'key',sorted(C(q['correct_option'] for q in src).items()))
print('fmt',dict(C(q['format'] for q in src)))
u=C(q['topic'] for q in src); print('units',' '.join(f'{k}:{u[k]}/{U[k][2]}' for k in U)); print('parts',' '.join(f'{p}:{sum(u[k] for k in ks)}' for p,ks in PART.items()))
cu={q['topic'] for q in src if q.get('case')}
for k in U:
    if abs(u[k]-U[k][2])>1 and not (k in cu and 0<u[k]-U[k][2]<=2): print('QUOTA',k,u[k],U[k][2])
for k,v in d['passages'].items(): print('passage',k,len(v.split()),'words')
long=sum(1 for q in src if len(q['question'])>=150 or q.get('case')); print('stems>=150 or case',long)
led=pol_ledger.read(); seen=collections.Counter()
for i,q in enumerate(src,1):
    if not q['explanation'].startswith('Answer: ('+q['correct_option']+')'): print('ANSWERLINE',i)
    if q['format']=='sequence' and re.search(r'\(?A\)?,\s*\(?B\)?,\s*\(?C\)?,\s*\(?D\)?\s*$',q['options']['ABCD'.index(q['correct_option'])]): print('SEQ-ABCD',i)
    if len(set(o[3:].strip().lower() for o in q['options']))<4: print('DUPOPT',i)
    if q['format'] in('direct','case-based'):
        ls=[len(o) for o in q['options']];k='ABCD'.index(q['correct_option'])
        if ls[k]==max(ls) and ls.count(max(ls))==1 and max(ls)>1.15*sorted(ls)[-2]: print('LONGEST',i,q['sub_topic'])
    if not q.get('targets'): print('NO-TARGET',i,q['sub_topic'])
    for sec,ws in pol_ledger.parse_targets(q.get('targets')).items():
        for w in ws:
            seen[(sec,w)]+=1
            if len(led.get(sec,{}).get(w,[]))>=2: print('REPEAT-TARGET',i,sec,w,led[sec][w])
for k,v in seen.items():
    if v>1: print('DUP-TARGET-IN-TEST',k)
print('targets',sum(seen.values()))
def norm(s): return re.sub(r'[^a-z0-9 ]',' ',s.lower())
old=[]
for f in glob.glob('CUET/Political Science/CUET POLITICAL SCIENCE TEST *.json'):
    o=json.load(open(f,encoding='utf-8'))
    if o.get('status')=='revised' and o['test_number']!=int(re.search(r'(\d+)',os.path.basename(sys.argv[1])).group(1)):
        for q in o['questions']: old.append((o['test_number'],q['sub_topic'],norm(q['question'].split('Question: ')[-1])[:200]))
for i,q in enumerate(src,1):
    b=norm(q['question'])[:200]
    for o in old:
        r1=difflib.SequenceMatcher(None,q['sub_topic'].lower(),o[1].lower()).ratio(); r2=difflib.SequenceMatcher(None,b,o[2]).ratio()
        if r1>0.85 or r2>0.8: print(f'OVERLAP Q{i} st{r1:.2f} q{r2:.2f} ~T{o[0]} [{o[1][:60]}]')
