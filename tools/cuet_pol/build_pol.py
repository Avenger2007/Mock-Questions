# usage: build_pol.py N polNN.json -> CUET/Political Science/CUET POLITICAL SCIENCE TEST N.json
import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from units import topic
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
meta={"test_id":f"CUET27_POLITICAL_SCIENCE_TEST_{n:02d}","series_id":"CUET27_POLITICAL_SCIENCE","exam":"CUET (UG) 2027","title":f"CUET Political Science Test {n}",
 "subject":"Political Science (Code: 323)","subject_code":"323","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/Political Science - 323.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: NTA CUET (UG) Political Science papers 2024 and 2026, analysed for format only (no questions copied)",
 "textbooks":["NCERT Class 12 Politics in India since Independence","NCERT Class 12 Contemporary World Politics"],
 "duration_minutes":60,"total_questions":50,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["All 50 questions are compulsory.","Each correct answer earns 5 marks; each incorrect answer deducts 1 mark; unattempted questions earn 0.","One set of 5 questions is based on a passage; the set stays together."]}
qs=[]
for i,q in enumerate(src['q'],1):
    o={'id':f'CUET27-POL-T{n:02d}-Q{i:02d}'}
    if q.get('case'):
        o['case_id']=f'CUET27-POL-T{n:02d}-CASE'
        pas=src['passages'][q['case']]
        lead='Read the following passage and answer the question that follows.'
        q['question']=lead+'\n\n'+pas+'\n\nQuestion: '+q['question']
    if q['format'] in ('statements','match-list','sequence','assertion-reason') and 'Choose the correct' not in q['question']: q['question']+='\nChoose the correct answer from the options given below:'
    o['topic']=topic(q['topic'])
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==50, len(qs)
meta['questions']=qs
p=f'CUET/Political Science/CUET POLITICAL SCIENCE TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
