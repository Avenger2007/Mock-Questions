# usage: build_gt.py N gtNN.json -> CUET/General Test/CUET GENERAL TEST TEST N.json
import json,sys
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
T={'Q':'Numerical Ability and Quantitative Reasoning','D':'Numerical Ability: Data Interpretation','M':'General Mental Ability',
'L':'Logical and Analytical Reasoning','G':'General Knowledge','S':'General Science and Environment Literacy','C':'Current Affairs'}
meta={"test_id":f"CUET27_GENERAL_TEST_TEST_{n:02d}","series_id":"CUET27_GENERAL_TEST","exam":"CUET (UG) 2027","title":f"CUET General Test Test {n}",
 "subject":"General Test (Code: 501)","subject_code":"501","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/General Test - 501.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: CUET (UG) 2025 and 2026 General Test shift analyses (no questions copied)",
 "current_affairs_window":"January 2025 to October 2026 (refresh before the 2027 exam)",
 "duration_minutes":60,"total_questions":50,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["All 50 questions are compulsory.","Each correct answer earns 5 marks; each incorrect answer deducts 1 mark; unattempted questions earn 0.","Calculators are not allowed.","The last 5 questions are a data-interpretation set based on one table; the set stays together."]}
qs=[]
for i,q in enumerate(src['q'],1):
    o={'id':f'CUET27-GT-T{n:02d}-Q{i:02d}'}
    if q.get('case'):
        o['case_id']=f'CUET27-GT-T{n:02d}-DI'
        q['question']='Study the following table and answer the question that follows.\n\n'+src['passages'][q['case']]+'\n\nQuestion: '+q['question']
    if q['format'] in ('statements','match-list','sequence','assertion-reason') and 'Choose the correct' not in q['question']: q['question']+='\nChoose the correct answer from the options given below:'
    o['topic']=T[q['topic']]
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==50, len(qs)
meta['questions']=qs
p=f'CUET/General Test/CUET GENERAL TEST TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
