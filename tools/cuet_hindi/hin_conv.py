# usage: hin_conv.py hinNN.txt hinNN.json  (compact authoring format -> build_hin input)
# '%P R1' starts a passage (R1 factual, R2 narrative, R3 literary);
# '@@ SEC|sub_topic|e/m/h|fmt|ANS|targets' starts a question (fmt: d direct, p passage, q sequence, m match-list, s statements;
# targets: 'C1:word,word;C2:idiom' for the coverage ledgers, may be empty);
# option lines 'A) ..'; a line '=' starts the explanation (Answer line is generated).
import json,sys,re
F={'d':'direct','p':'passage','m':'match-list','s':'statements','q':'sequence'}
D={'e':'easy','m':'medium','h':'hard'}
lines=open(sys.argv[1],encoding='utf-8').read().split('\n'); out={'q':[],'passages':{}}; cur=None; mode=None; pas=None
def close():
    if cur is None: return
    q=cur; q['question']='\n'.join(q.pop('_q')).strip(); ex='\n'.join(q.pop('_e')).strip()
    assert len(q['options'])==4,(q['sub_topic'],q['options']); t=q['options']['ABCD'.index(q['correct_option'])][3:]
    q['explanation']=f"उत्तर: ({q['correct_option']}) {t}\n"+ex; out['q'].append(q)
for ln in lines:
    if ln.startswith('%P '):
        close(); cur=None; f=ln[3:].split(); pas=f[0]; out['passages'][pas]=''
        if 'verse' in f[1:]: out.setdefault('verse',{})[pas]=True
        continue
    if ln.startswith('@@ '):
        close(); pas=None; f=[x.strip() for x in ln[3:].split('|')]+['']
        t,st,df,fm,ans,tg=f[:6]
        cur={'topic':t,'sub_topic':st,'difficulty':D[df],'format':F[fm],'_q':[],'options':[],'correct_option':ans,'_e':[],'targets':tg}; mode='q'
        if fm=='p': cur['case']=t
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
