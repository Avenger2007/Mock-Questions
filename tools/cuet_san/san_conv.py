# usage: san_conv.py sanNN.txt sanNN.json  (compact authoring format -> build_san input)
# '%P P' starts the unseen passage (one per test; its questions use fmt p and are tagged with the unit they test);
# '@@ UNIT|sub_topic|e/m/h|fmt|ANS|targets' starts a question (fmt: d direct, n numerical, p case-based, a assertion-reason, q sequence, m match-list, s statements;
# targets: 'F1:fact,fact;F3:event' for the coverage ledgers, may be empty);
# option lines 'A) ..'; a line '=' starts the explanation (Answer line is generated).
import json,sys,re
F={'d':'direct','n':'numerical','p':'passage','a':'assertion-reason','m':'match-list','s':'statements','q':'sequence'}
D={'e':'easy','m':'medium','h':'hard'}
lines=open(sys.argv[1],encoding='utf-8').read().split('\n'); out={'q':[],'passages':{}}; cur=None; mode=None; pas=None
def close():
    if cur is None: return
    q=cur; q['question']='\n'.join(q.pop('_q')).strip(); ex='\n'.join(q.pop('_e')).strip()
    assert len(q['options'])==4,(q['sub_topic'],q['options']); t=q['options']['ABCD'.index(q['correct_option'])][3:]
    q['explanation']=f"उत्तर: ({q['correct_option']}) {t}\n"+ex; out['q'].append(q)
for ln in lines:
    if ln.startswith('%P '):
        close(); cur=None; pas=ln[3:].strip(); out['passages'][pas]=''; continue
    if ln.startswith('@@ '):
        close(); pas=None; f=[x.strip() for x in ln[3:].split('|')]+['']
        t,st,df,fm,ans,tg=f[:6]
        if tg and ':' not in tg: tg=t+':'+tg
        cur={'topic':t,'sub_topic':st,'difficulty':D[df],'format':F[fm],'_q':[],'options':[],'correct_option':ans,'_e':[],'targets':tg}; mode='q'
        if fm=='p': cur['case']='P'
        continue
    if pas is not None and cur is None: out['passages'][pas]+=('\n' if out['passages'][pas] else '')+ln; continue
    if cur is None: continue
    if mode=='q' and re.match(r'^[A-D]\) ',ln): cur['options'].append(ln.rstrip()); continue
    if ln.strip()=='=': mode='e'; continue
    if mode=='e': cur['_e'].append(ln)
    elif not cur['options']: cur['_q'].append(ln)
close()
out['passages']={k:v.strip() for k,v in out['passages'].items()}
json.dump(out,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('converted',len(out['q']))
