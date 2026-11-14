"""Print questions compactly: python3 tools/iat/show.py N [start end]  |  python3 tools/iat/show.py T:Q T:Q ..."""
import json,sys,glob
def load(t):
    f='IISER/IAT TEST 1.json' if int(t)==1 else f'IISER/IAT NEW TEST {int(t)}.json'
    d=json.load(open(f)); return d['questions'] if isinstance(d,dict) else d
a=sys.argv[1:]
if ':' in a[0]:
    for x in a:
        t,n=x.split(':'); q=load(t)[int(n)-1]
        print(f"T{t} Q{n} [{q['correct_option']}] {q.get('image_reference') or ''}: {q['question']}\n   {' ; '.join(q['options'])}")
else:
    qs=load(a[0]); s,e=(int(a[1]),int(a[2])) if len(a)>2 else (1,60)
    for i,q in enumerate(qs,1):
        if s<=i<=e:
            print(f"\n## Q{i} | {q.get('sub_topic')} | {q.get('difficulty')} {q.get('format')} {q.get('image_reference') or ''} | KEY {q['correct_option']}")
            print(q['question']); print(' ; '.join(q['options']))
