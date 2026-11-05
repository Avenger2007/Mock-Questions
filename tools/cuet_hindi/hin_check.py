import json,sys,glob,difflib,re,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import hin_ledger
d=json.load(open(sys.argv[1],encoding='utf-8')); src=d['q']; C=collections.Counter
print(len(src),'diff',dict(C(q['difficulty'] for q in src)),'key',sorted(C(q['correct_option'] for q in src).items()))
print('fmt',dict(C(q['format'] for q in src)))
u=C(q['topic'] for q in src); print('sections',dict(sorted(u.items())))
for k,v in d['passages'].items(): print('passage',k,len(v.split()),'words',' OVER300' if len(v.split())>300 else '')
led=hin_ledger.read(); seen=collections.Counter()
for i,q in enumerate(src,1):
    if not q['explanation'].startswith('उत्तर: ('+q['correct_option']+')'): print('ANSWERLINE',i)
    if q['format']=='sequence' and re.search(r'\(?A\)?, \(?B\)?, \(?C\)?, \(?D\)?$',q['options']['ABCD'.index(q['correct_option'])]): print('SEQ-ABCD',i)
    if len(set(o[3:].strip().lower() for o in q['options']))<4: print('DUPOPT',i)
    if q['format'] in('direct','passage'):
        ls=[len(o) for o in q['options']];k='ABCD'.index(q['correct_option'])
        if ls[k]==max(ls) and ls.count(max(ls))==1 and max(ls)>1.3*sorted(ls)[-2] and max(ls)>12: print('LONGEST',i,q['sub_topic'])
    for sec,ws in hin_ledger.parse_targets(q.get('targets')).items():
        for w in ws:
            seen[(sec,w)]+=1
            if w in led.get(sec,{}): print('REPEAT-TARGET',i,sec,w,'T%d'%led[sec][w])
for k,v in seen.items():
    if v>1: print('DUP-TARGET-IN-TEST',k)
print('targets',sum(seen.values()))
def norm(s): return re.sub(r'[\s.,;:!?\'"()\-–—।|‘’“”=]+',' ',s.lower())
old=[]
for f in glob.glob('CUET/Hindi/CUET HINDI TEST *.json'):
    o=json.load(open(f,encoding='utf-8'))
    if o.get('status')=='revised':
        for q in o['questions']: old.append((o['test_number'],q['sub_topic'],norm(q['question'].split('प्रश्न: ')[-1])[:200]))
for i,q in enumerate(src,1):
    b=norm(q['question'])[:200]
    for o in old:
        r1=difflib.SequenceMatcher(None,q['sub_topic'].lower(),o[1].lower()).ratio(); r2=difflib.SequenceMatcher(None,b,o[2]).ratio()
        if r1>0.85 or r2>0.8: print(f'OVERLAP Q{i} st{r1:.2f} q{r2:.2f} ~T{o[0]} [{o[1][:60]}]')
