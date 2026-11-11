# usage: phy_check.py drafts/phyNN.json  — quotas, key, difficulty, formats, ledger repeats, overlap with earlier tests
import json,sys,glob,difflib,re,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import phy_ledger; from units import U,N,DIFF,FMT,KEY,MIN_NUMERICAL
p=sys.argv[1]; n=int(re.search(r'(\d+)',os.path.basename(p)).group(1))
src=json.load(open(p,encoding='utf-8'))['q']; C=collections.Counter
dc=C(q['difficulty'] for q in src); kc=C(q['correct_option'] for q in src); fc=C(q['format'] for q in src)
print(len(src),dict(dc),'key',dict(sorted(kc.items())),'fmt',dict(fc))
if len(src)!=N: print('COUNT',len(src),N)
if {k:dc.get(k,0) for k in DIFF}!=DIFF: print('DIFF',dict(dc),DIFF)
if {k:kc.get(k,0) for k in 'ABCD'}!=KEY(n): print('KEY',dict(kc),KEY(n))
for f,v in FMT.items():
    if fc.get(f,0)!=v: print('FMT',f,fc.get(f,0),v)
if fc.get('numerical',0)<MIN_NUMERICAL: print('FEW-NUMERICAL',fc.get('numerical',0))
u=C(q['unit'] for q in src); print('  units',' '.join(f'{k}:{u[k]}/{U[k][1]}' for k in U))
for k in U:
    if u[k]!=U[k][1]: print('QUOTA',k,u[k],U[k][1])
mu=[q['unit'] for q in src if q['format']=='match-list']
if len(set(mu))<len(mu): print('MATCH-SAME-UNIT',mu)
st=[q for q in src if q['format']=='statements']
pol=['NOT' in q['question'] for q in st]
for a,b in zip(pol,pol[1:]):
    if a==b: print('STMT-POLARITY-NOT-ALTERNATING',pol); break
fs=[next((L for L in 'ABCD' if re.search(r'\('+L+r'\) is false|Only \('+L+r'\) is false',q['explanation'])),None) for q in st]
def plain(o): return re.sub(r'\\[a-zA-Z]+|[{}\\^_$]|\\\(|\\\)','',o[3:]).strip()
led=phy_ledger.read(); seen=C(); pats=[]
for i,q in enumerate(src,1):
    if not q['explanation'].startswith('Answer: ('+q['correct_option']+')'): print('ANSWERLINE',i)
    if len(set(o[3:].lower().replace(' ','') for o in q['options']))<4: print('DUPOPT',i,q['sub_topic'])
    if q['format']=='match-list':
        pats.append(q['options']['ABCD'.index(q['correct_option'])][3:].strip())
        for k in ['List-I','List-II','(I)','(IV)']:
            if k not in q['question']: print('MATCH-FORM',i,k)
    if q['format'] in ('statements','sequence') and '(D)' not in q['question']: print('STMT-FORM',i)
    if q['format']=='sequence' and re.search(r'\(A\),\s*\(B\),\s*\(C\),\s*\(D\)\s*$',q['options']['ABCD'.index(q['correct_option'])]): print('SEQ-ABCD',i)
    if q['format']=='direct':
        ls=[len(plain(o)) for o in q['options']]; k='ABCD'.index(q['correct_option'])
        if min(ls)>=12 and ls[k]==max(ls) and ls.count(max(ls))==1 and max(ls)>1.15*sorted(ls)[-2]: print('LONGEST',i,q['sub_topic'])
    if q['format']=='numerical' and not re.search(r'Step 1',q['explanation']): print('NO-STEPS',i,q['sub_topic'])
    if not re.search(r'Common mistake:|Why not the others:',q['explanation']): print('NO-DISTRACTOR-NOTE',i)
    if not q.get('targets'): print('NO-TARGET',i,q['sub_topic'])
    for fld in [q['question'],q['explanation']]+q['options']:
        if fld.count('\\(')!=fld.count('\\)'): print('KATEX-UNBALANCED',i); break
    for sec,ws in phy_ledger.parse_targets(q.get('targets')).items():
        for w in ws:
            seen[(sec,w)]+=1
            if len(led.get(sec,{}).get(w,[]))>=2: print('REPEAT-TARGET',i,sec,w,led[sec][w])
if len(set(pats))<len(pats): print('MATCH-PATTERN-REPEAT',pats)
for k,v in seen.items():
    if v>1: print('DUP-TARGET-IN-TEST',k)
print('targets',sum(seen.values()))
def norm(s): return re.sub(r'\s+',' ',re.sub(r'[^a-z0-9 ]',' ',s.lower()))
old=[]
for f in glob.glob('CUET/Physics/CUET PHYSICS TEST *.json'):
    o=json.load(open(f,encoding='utf-8'))
    if o.get('status')=='revised' and o['test_number']!=n:
        for q in o['questions']: old.append((o['test_number'],q['sub_topic'],norm(q['question'])[:220]))
for i,q in enumerate(src,1):
    b=norm(q['question'])[:220]
    for o in old:
        r1=difflib.SequenceMatcher(None,q['sub_topic'].lower(),o[1].lower()).ratio(); r2=difflib.SequenceMatcher(None,b,o[2]).ratio()
        if r1>0.85 or r2>0.85: print(f'OVERLAP Q{i} st{r1:.2f} q{r2:.2f} ~T{o[0]} [{o[1][:60]}]')
