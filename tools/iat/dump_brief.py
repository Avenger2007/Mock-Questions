"""Read-only review dump. usage: dump_brief.py N start end [full]
Conceptual items: stem, options, key, and only the 'Why not' line. Numerical items (and all with 'full'): complete."""
import json,sys,re,glob
n,a,b=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]); full=len(sys.argv)>4
f=[p for p in glob.glob('IISER/IAT*TEST*.json') if re.search(rf'TEST {n}\.json$',p)][0]
for q in json.load(open(f))['questions'][a-1:b]:
    print('##',q['id'][-3:],q['topic'],'|',q['sub_topic'],'|',q['difficulty'],q['format'],q.get('image_reference',''))
    print(q['question']); print(' ; '.join(q['options']),'| KEY',q['correct_option'])
    e=q['explanation']
    if full: print(e)
    else:
        e=re.sub(r'\nWhy:.*?(?=\nWhy not the others:)','',e,flags=re.S)
        e=re.sub(r'\nKey point:.*','',e,flags=re.S)
        print(e)
    print()
