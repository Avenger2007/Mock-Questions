# usage: build_his.py N hisNN.json -> CUET/History/CUET HISTORY TEST N.json
import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from units import topic
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
meta={"test_id":f"CUET27_HISTORY_TEST_{n:02d}","series_id":"CUET27_HISTORY","exam":"CUET (UG) 2027","title":f"CUET History Test {n}",
 "subject":"History (Code: 314)","subject_code":"314","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/History - 314.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: NTA CUET (UG) History papers 2022, 2024 and 2026, analysed for format only (no questions copied)",
 "textbooks":["NCERT Class 12 Themes in Indian History Part I (rationalised)","NCERT Class 12 Themes in Indian History Part II (rationalised)","NCERT Class 12 Themes in Indian History Part III (rationalised)"],
 "duration_minutes":60,"total_questions":50,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["All 50 questions are compulsory.","Each correct answer earns 5 marks; each incorrect answer deducts 1 mark; unattempted questions earn 0.","One set of 5 questions is based on a source passage; the set stays together."]}
qs=[]
for i,q in enumerate(src['q'],1):
    o={'id':f'CUET27-HIS-T{n:02d}-Q{i:02d}'}
    if q.get('case'):
        o['case_id']=f'CUET27-HIS-T{n:02d}-CASE'
        pas=src['passages'][q['case']]
        lead='Read the following source passage and answer the question that follows.'
        q['question']=lead+'\n\n'+pas+'\n\nQuestion: '+q['question']
    if q['format'] in ('statements','match-list','sequence','assertion-reason') and 'Choose the correct' not in q['question']: q['question']+='\nChoose the correct answer from the options given below:'
    o['topic']=topic(q['topic'])
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==50, len(qs)
meta['questions']=qs
p=f'CUET/History/CUET HISTORY TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
