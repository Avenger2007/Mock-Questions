# usage: build_math.py N mathNN.json -> CUET/Mathematics/CUET MATHEMATICS TEST N.json
import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from units import topic
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
meta={"test_id":f"CUET27_MATHEMATICS_TEST_{n:02d}","series_id":"CUET27_MATHEMATICS","exam":"CUET (UG) 2027","title":f"CUET Mathematics Test {n}",
 "subject":"Mathematics / Applied Mathematics (Code: 319)","subject_code":"319","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/Mathematics - 319.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: NTA CUET (UG) 319 papers 2024, 2025 and 2026, analysed for format and level (no questions copied)",
 "textbooks":["NCERT Mathematics, Class XII, Parts I and II","CBSE Applied Mathematics, Class XII curriculum (Section B2)"],
 "duration_minutes":60,"total_questions":85,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["Attempt all 15 questions of Section A (common to Mathematics and Applied Mathematics).",
  "Then attempt all 35 questions of EITHER Section B1 (Mathematics) OR Section B2 (Applied Mathematics) — 50 questions in total.",
  "Each correct answer earns 5 marks; each incorrect answer deducts 1 mark; unattempted questions earn 0."],
 "sections":[{"id":"A","title":"Section A — common to Mathematics and Applied Mathematics (compulsory)","question_range":"1-15","questions":15,"attempt":15},
  {"id":"B1","title":"Section B1 — Mathematics","question_range":"16-50","questions":35,"attempt":"35 if chosen"},
  {"id":"B2","title":"Section B2 — Applied Mathematics","question_range":"51-85","questions":35,"attempt":"35 if chosen"}],
 "common_sections":["A"],"optional_sections":["B1","B2"]}
order={'A':0,'B1':1,'B2':2}; qs=[]
for i,q in enumerate(sorted(src['q'],key=lambda q:order[q['section']]),1):
    o={'id':f'CUET27-MAT-T{n:02d}-Q{i:02d}','section':q['section'],'topic':topic(q['unit'])}
    if q['format'] in ('statements','match-list') and 'Choose the correct' not in q['question']: q['question']+='\nChoose the correct answer from the options given below:'
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==85, len(qs)
meta['questions']=qs
p=f'CUET/Mathematics/CUET MATHEMATICS TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
