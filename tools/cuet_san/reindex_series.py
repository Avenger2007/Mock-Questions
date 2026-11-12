# usage: reindex.py "CUET/<Subject>" — refresh series_index.json from the test files
import json,sys,os,collections
D=sys.argv[1]; p=os.path.join(D,'series_index.json'); idx=json.load(open(p,encoding='utf-8'))
for pp in idx['papers']:
    t=json.load(open(os.path.join(D,pp['filename']),encoding='utf-8'))
    qs=t['questions'] if 'questions' in t else [q for s in t['sections'] for q in s['questions']]
    n=len(qs); dc=collections.Counter(q['difficulty'] for q in qs)
    pp['difficulty_distribution']={k:f"{dc[k]} ({round(100*dc[k]/n)}%)" for k in ('easy','medium','hard')}
    pp['key_distribution']=dict(sorted(collections.Counter(q['correct_option'] for q in qs).items()))
    pp['total_questions']=n; pp['status']=t.get('status',pp.get('status'))
    pp['topics_covered']=sorted({q['topic'] for q in qs})
idx['total_papers']=len(idx['papers']); idx['total_questions_series']=sum(pp['total_questions'] for pp in idx['papers'])
json.dump(idx,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2); open(p,'a').write('\n')
print(idx['total_papers'],idx['total_questions_series'],[pp['status'] for pp in idx['papers']][:3],idx['papers'][0]['difficulty_distribution'])
