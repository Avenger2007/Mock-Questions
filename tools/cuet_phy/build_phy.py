# usage: build_phy.py N phyNN.json -> CUET/Physics/CUET PHYSICS TEST N.json
import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from units import topic
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
meta={"test_id":f"CUET27_PHYSICS_TEST_{n:02d}","series_id":"CUET27_PHYSICS","exam":"CUET (UG) 2027","title":f"CUET Physics Test {n}",
 "subject":"Physics (Code: 322)","subject_code":"322","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/Physics - 322.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: NTA CUET (UG) Physics papers 2024, 2025 and 2026, analysed for format and level (no questions copied)",
 "textbooks":["NCERT Physics, Class XII, Parts I and II (rationalised edition)"],
 "duration_minutes":60,"total_questions":50,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["All 50 questions are compulsory.","Each correct answer earns 5 marks; each incorrect answer deducts 1 mark; unattempted questions earn 0.","Calculators are not allowed; numbers are chosen so the working can be done by hand."]}
qs=[]
for i,q in enumerate(src['q'],1):
    o={'id':f'CUET27-PHY-T{n:02d}-Q{i:02d}','topic':topic(q['unit'])}
    if q['format'] in ('statements','match-list','sequence') and 'Choose the correct' not in q['question']: q['question']+='\nChoose the correct answer from the options given below:'
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==50, len(qs)
meta['questions']=qs
p=f'CUET/Physics/CUET PHYSICS TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
