"""usage: replace_item.py N 'old sub_topic' — after the draft block has been rewritten, reconvert the draft
and swap the shipped item (matched by old sub_topic) for the new draft item, keeping its id and position."""
import json,subprocess,sys
N=int(sys.argv[1]); old=sys.argv[2]; T='tools/cuet_math'; d=f'{T}/drafts/math{N:02d}'
subprocess.run(['python3',f'{T}/math_conv.py',d+'.txt',d+'.json'],check=True)
f=f'CUET/Mathematics/CUET MATHEMATICS TEST {N}.json'; o=json.load(open(f,encoding='utf-8'))
have={q['sub_topic'] for q in o['questions']}
new=[q for q in json.load(open(d+'.json'))['q'] if q['sub_topic'] not in have]
assert len(new)==1,[q['sub_topic'] for q in new]; n=new[0]
hit=[q for q in o['questions'] if q['sub_topic']==old]; assert len(hit)==1; q=hit[0]
assert q['correct_option']==n['correct_option'] and q['section']==n['section'] and q['difficulty']==n['difficulty']
for k in ('sub_topic','format','question','options','explanation'): q[k]=n[k]
json.dump(o,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2); print('replaced',q['id'],'->',n['sub_topic'],'key',n['targets'])
