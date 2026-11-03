# usage: fixopts.py q.json fixes.json ; fixes = {"idx": {"opts":[4 texts] (optional), "move":"B" (optional)}}
import json,sys,re
p=sys.argv[1]; d=json.load(open(p,encoding='utf-8')); F=json.load(open(sys.argv[2],encoding='utf-8'))
for k,f in F.items():
    q=d['q'][int(k)-1]
    if 'opts' in f: q['options']=[f'{L}) {t}' for L,t in zip('ABCD',f['opts'])]
    if 'move' in f and f['move']!=q['correct_option']:
        a,b=q['correct_option'],f['move']; o={x[0]:x[3:] for x in q['options']}; o[a],o[b]=o[b],o[a]
        q['options']=[f'{L}) {o[L]}' for L in 'ABCD']; q['correct_option']=b
        q['explanation']=re.sub(r'\(([AB'+'CD])\)',lambda m:'('+({a:b,b:a}.get(m.group(1),m.group(1)))+')',q['explanation'])
    c=q['correct_option']; t=[x for x in q['options'] if x.startswith(c+')')][0][3:]
    q['explanation']=f'Answer: ({c}) {t}\n'+q['explanation'].split('\n',1)[1]
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('fixed',len(F))
