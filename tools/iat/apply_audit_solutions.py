"""Mechanical only: replace explanation fields from IISER/audit/solutions/testNN.txt.
usage: python3 tools/iat/apply_audit_solutions.py N
Blocks start with '@@ Qnn'. Never touches question text, options or keys."""
import json,sys,re,glob
n=int(sys.argv[1])
f=[p for p in glob.glob('IISER/IAT*TEST*.json') if re.search(rf'TEST {n}\.json$',p)][0]
src=open(f'IISER/audit/solutions/test{n:02}.txt',encoding='utf-8').read()
blocks=dict((m.group(1),m.group(2).strip()) for m in re.finditer(r'@@ Q(\d\d)\n(.*?)(?=\n@@ Q\d\d\n|\Z)',src,flags=re.S))
t=json.load(open(f,encoding='utf-8')); ch=0
for q in t['questions']:
    k=q['id'][-2:]
    if k in blocks:
        e=blocks[k]
        assert e.startswith(f"Answer: ({q['correct_option']})"),(k,'key mismatch')
        if q['explanation']!=e: q['explanation']=e; ch+=1
json.dump(t,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2); open(f,'a').write('\n')
print(f,'blocks',len(blocks),'changed',ch)
