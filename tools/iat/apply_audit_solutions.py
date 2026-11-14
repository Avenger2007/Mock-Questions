"""Mechanical only: apply audited text from IISER/audit/solutions/testNN.txt to a test JSON.
usage: python3 tools/iat/apply_audit_solutions.py N
'@@ Qnn'  block  -> replaces that question's explanation.
'@@Q Qnn' block  -> replaces the question itself: optional 'sub_topic:', 'difficulty:', 'format:' lines,
                    then 'question:' (may span lines), four option lines 'A) ..' to 'D) ..', and 'key: X'.
The key of a replaced question must equal the existing key (keeps the 15/15/15/15 balance); IDs never change."""
import json,sys,re,glob
n=int(sys.argv[1])
f=[p for p in glob.glob('IISER/IAT*TEST*.json') if re.search(rf'TEST {n}\.json$',p)][0]
src=open(f'IISER/audit/solutions/test{n:02}.txt',encoding='utf-8').read()
parts=re.split(r'^(@@Q? Q\d\d)\n',src,flags=re.M)
sol={}; qs={}
for head,body in zip(parts[1::2],parts[2::2]):
    (qs if head.startswith('@@Q') else sol)[head[-2:]]=body.strip()
t=json.load(open(f,encoding='utf-8')); ch=cq=0
for q in t['questions']:
    k=q['id'][-2:]
    if k in qs:
        b=qs[k]; m=re.search(r'question:\s*(.*?)\nA\) (.*)\nB\) (.*)\nC\) (.*)\nD\) (.*)\nkey: ([ABCD])\s*$',b,flags=re.S)
        assert m,(k,'bad question block')
        assert m.group(6)==q['correct_option'],(k,'replacement must keep the key letter')
        for fld in ('sub_topic','difficulty','format'):
            mm=re.search(rf'^{fld}:\s*(.+)$',b[:m.start()],flags=re.M)
            if mm: q[fld]=mm.group(1).strip()
        q['question']=m.group(1).strip(); q['options']=[f'{L}) {m.group(i).strip()}' for i,L in zip(range(2,6),'ABCD')]
        assert k in sol,(k,'replaced question needs a new solution'); cq+=1
    if k in sol:
        e=sol[k]
        assert e.startswith(f"Answer: ({q['correct_option']})"),(k,'key mismatch')
        if q['explanation']!=e: q['explanation']=e; ch+=1
json.dump(t,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2); open(f,'a').write('\n')
print(f,'solutions',len(sol),'changed',ch,'questions replaced',cq)
