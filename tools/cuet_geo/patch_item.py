# usage: patch_item.py N 'sub_topic' patches.json — applies [old,new] text pairs to one item in the draft and in the shipped test
import json,sys
N=int(sys.argv[1]); st=sys.argv[2]; P=json.load(open(sys.argv[3]))
d=f'tools/cuet_geo/drafts/geo{N:02d}.txt'; s=open(d,encoding='utf-8').read()
i=s.index('@@ '); i=s.index('|'+st+'|'); i=s.rindex('@@ ',0,i); j=s.find('\n@@ ',i+3); j=len(s) if j<0 else j+1
blk=s[i:j]
for a,b in P: assert blk.count(a)==1,(st,a); blk=blk.replace(a,b)
open(d,'w',encoding='utf-8').write(s[:i]+blk+s[j:])
f=f'CUET/Geography/CUET GEOGRAPHY TEST {N}.json'; o=json.load(open(f,encoding='utf-8')); n=0
for q in o['questions']:
    if q['sub_topic']==st:
        n+=1
        for a,b in P:
            if a in q['explanation']: q['explanation']=q['explanation'].replace(a,b)
            elif a in q['options']: q['options'][q['options'].index(a)]=b
            else: raise SystemExit(f'not found in json: {a}')
assert n==1; json.dump(o,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2); print('patched',N,st)
