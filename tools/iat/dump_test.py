"""Read-only: print a slice of a test for review. usage: dump_test.py N start end"""
import json,sys,re,glob
n,a,b=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
f=[p for p in glob.glob('IISER/IAT*TEST*.json') if re.search(rf'TEST {n}\.json$',p)][0]
for q in json.load(open(f))['questions'][a-1:b]:
    print('##',q['id'][-3:],q['topic'],'|',q['sub_topic'],'|',q['difficulty'],q['format'],q.get('image_reference',''))
    print(q['question']); print(' ; '.join(q['options']),'| KEY',q['correct_option']); print(q['explanation']); print()
