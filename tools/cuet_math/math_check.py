# usage: math_check.py drafts/mathNN.json  — quotas, keys, formats, ledger repeats, overlap with earlier tests
import json,sys,glob,difflib,re,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import math_ledger; from units import U,SEC,DIFF,FMT,KEY
p=sys.argv[1]; n=int(re.search(r'(\d+)',os.path.basename(p)).group(1))
src=json.load(open(p,encoding='utf-8'))['q']; C=collections.Counter
for s in SEC:
    qs=[q for q in src if q['section']==s]; dc=C(q['difficulty'] for q in qs); kc=C(q['correct_option'] for q in qs); fc=C(q['format'] for q in qs)
    print(s,len(qs),dict(dc),'key',dict(sorted(kc.items())),'fmt',dict(fc))
    if len(qs)!=SEC[s]: print('COUNT',s,len(qs),SEC[s])
    if dict(dc)!={k:v for k,v in DIFF[s].items()}: print('DIFF',s,dict(dc),DIFF[s])
    if {k:kc.get(k,0) for k in 'ABCD'}!=KEY(n,s): print('KEY',s,dict(kc),KEY(n,s))
    for f,v in FMT[s].items():
        if fc.get(f,0)!=v: print('FMT',s,f,fc.get(f,0),v)
    u=C(q['unit'] for q in qs)
    print('  units',' '.join(f'{k}:{u[k]}/{U[k][2]}' for k in U if U[k][0]==s))
    for k in U:
        if U[k][0]==s and abs(u[k]-U[k][2])>1: print('QUOTA',k,u[k],U[k][2])
    mu=[q['unit'] for q in qs if q['format']=='match-list']
    if len(set(mu))<len(mu): print('MATCH-SAME-UNIT',s,mu)
def plain(o): return re.sub(r'\\[a-zA-Z]+|[{}\\^_$]|\\\(|\\\)','',o[3:]).strip()
led=math_ledger.read(); seen=C(); pats=[]
for i,q in enumerate(src,1):
    if not q['explanation'].startswith('Answer: ('+q['correct_option']+')'): print('ANSWERLINE',i)
    if len(set(o[3:].lower().replace(' ','') for o in q['options']))<4: print('DUPOPT',i,q['sub_topic'])
    if q['format']=='match-list':
        pats.append(q['options']['ABCD'.index(q['correct_option'])][3:].strip())
        for k in ['List-I','List-II','(I)','(IV)']:
            if k not in q['question']: print('MATCH-FORM',i,k)
    if q['format']=='statements' and '(D)' not in q['question']: print('STMT-FORM',i)
    if q['format']=='direct':
        ls=[len(plain(o)) for o in q['options']]; k='ABCD'.index(q['correct_option'])
        if min(ls)>=12 and ls[k]==max(ls) and ls.count(max(ls))==1 and max(ls)>1.15*sorted(ls)[-2]: print('LONGEST',i,q['sub_topic'])
    if q['format']=='numerical' and not re.search(r'Step 1',q['explanation']): print('NO-STEPS',i,q['sub_topic'])
    if not re.search(r'Common mistake:|Why not the others:',q['explanation']): print('NO-DISTRACTOR-NOTE',i)
    if not q.get('targets'): print('NO-TARGET',i,q['sub_topic'])
    if q['question'].count('\\(')!=q['question'].count('\\)'): print('KATEX-UNBALANCED',i)
    for sec,ws in math_ledger.parse_targets(q.get('targets')).items():
        for w in ws:
            seen[(sec,w)]+=1
            if len(led.get(sec,{}).get(w,[]))>=3: print('REPEAT-TARGET',i,sec,w,led[sec][w])
if len(set(pats))<len(pats): print('MATCH-PATTERN-REPEAT',pats)
for k,v in seen.items():
    if v>1: print('DUP-TARGET-IN-TEST',k)
print('targets',sum(seen.values()))
def norm(s): return re.sub(r'\s+',' ',re.sub(r'[^a-z0-9 ]',' ',s.lower()))
old=[]
for f in glob.glob('CUET/Mathematics/CUET MATHEMATICS TEST *.json'):
    o=json.load(open(f,encoding='utf-8'))
    if o.get('status')=='revised' and o['test_number']!=n:
        for q in o['questions']: old.append((o['test_number'],q['sub_topic'],norm(q['question'])[:220]))
for i,q in enumerate(src,1):
    b=norm(q['question'])[:220]
    for o in old:
        r1=difflib.SequenceMatcher(None,q['sub_topic'].lower(),o[1].lower()).ratio(); r2=difflib.SequenceMatcher(None,b,o[2]).ratio()
        if r1>0.85 or r2>0.85: print(f'OVERLAP Q{i} st{r1:.2f} q{r2:.2f} ~T{o[0]} [{o[1][:60]}]')
