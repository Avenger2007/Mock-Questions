"""Print Maths/Physics questions with current solutions: python3 tools/iat/dump_mp.py N [start end]"""
import json,sys
t=int(sys.argv[1]); s,e=(int(sys.argv[2]),int(sys.argv[3])) if len(sys.argv)>3 else (31,60)
d=json.load(open(f'IISER/IAT NEW TEST {t}.json')); qs=d['questions'] if isinstance(d,dict) else d
for i,q in enumerate(qs,1):
    if s<=i<=e:
        if q.get('image_reference'): print(f"\n## Q{i} FIGURE - skipped"); continue
        print(f"\n## Q{i} {q['difficulty']} {q['format']} KEY {q['correct_option']}\n{q['question']}\n"+' ; '.join(q['options']))
        ex=q['explanation'].split('\n')
        print('\n'.join(l for l in ex if not l.startswith(('Answer:','Key point:'))))
