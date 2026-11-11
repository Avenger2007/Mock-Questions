# usage: phy_conv.py phyNN.txt phyNN.json  (compact authoring format -> build input)
# '@@ UNIT|sub_topic|e/m/h|fmt|ANS|keys' starts a question. UNIT is P1-P9.
# fmt: n numerical, d direct/concept, m match-list, s statements, q sequence. keys: comma-separated skill keys for the ledger.
# option lines 'A) ..'; a line '=' starts the explanation (the Answer line is generated). Lines starting '#' are comments.
import json,sys,re
F={'d':'direct','n':'numerical','m':'match-list','s':'statements','q':'sequence'}
D={'e':'easy','m':'medium','h':'hard'}
out={'q':[]}; cur=None; mode=None
def close():
    if cur is None: return
    q=cur; q['question']='\n'.join(q.pop('_q')).strip(); ex='\n'.join(q.pop('_e')).strip()
    assert len(q['options'])==4,(q['sub_topic'],q['options']); t=q['options']['ABCD'.index(q['correct_option'])][3:]
    q['explanation']=f"Answer: ({q['correct_option']}) {t}\n"+ex; out['q'].append(q)
for ln in open(sys.argv[1],encoding='utf-8').read().split('\n'):
    if ln.startswith('#'): continue
    if ln.startswith('@@ '):
        close(); f=[x.strip() for x in ln[3:].split('|')]+['']
        u,st,df,fm,ans,tg=f[:6]
        cur={'unit':u,'sub_topic':st,'difficulty':D[df],'format':F[fm],'_q':[],'options':[],'correct_option':ans,'_e':[],'targets':(u+':'+tg) if tg else ''}; mode='q'; continue
    if cur is None: continue
    if mode=='q' and re.match(r'^[A-D]\) ',ln): cur['options'].append(ln.rstrip()); continue
    if ln.strip()=='=': mode='e'; continue
    if mode=='e': cur['_e'].append(ln)
    elif not cur['options']: cur['_q'].append(ln)
close()
json.dump(out,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('converted',len(out['q']))
