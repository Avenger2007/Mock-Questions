# usage: build_eng.py N engNN.json -> CUET/English/CUET ENGLISH TEST N.json
import json,sys
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
T={'R1':'Reading Comprehension: Factual Passage','R2':'Reading Comprehension: Narrative Passage','R3':'Reading Comprehension: Literary Passage',
'V1':'Verbal Ability: Rearranging the Parts','V2':'Verbal Ability: Match the Following','V3':'Verbal Ability: Choosing the Correct Word',
'V4':'Verbal Ability: Synonyms and Antonyms','V5':'Verbal Ability: One-Word Substitution','V6':'Verbal Ability: Sentence Transformation and Correctness'}
meta={"test_id":f"CUET27_ENGLISH_TEST_{n:02d}","series_id":"CUET27_ENGLISH","exam":"CUET (UG) 2027","title":f"CUET English Test {n}",
 "subject":"English (Code: 101)","subject_code":"101","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/English - 101.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: CUET (UG) 2026 English paper formats (no questions or passages copied)",
 "duration_minutes":60,"total_questions":50,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["All 50 questions are compulsory.","Each correct answer earns 5 marks; each incorrect answer deducts 1 mark; unattempted questions earn 0.","The last 15 questions are three passage sets (factual, narrative, literary) of 5 questions each; each set stays together."]}
P={'R1':1,'R2':2,'R3':3}; qs=[]
for i,q in enumerate(src['q'],1):
    o={'id':f'CUET27-ENG-T{n:02d}-Q{i:02d}'}
    if q.get('case'):
        o['case_id']=f'CUET27-ENG-T{n:02d}-P{P[q["case"]]}'
        q['question']='Read the following passage and answer the question that follows.\n\n'+src['passages'][q['case']]+'\n\nQuestion: '+q['question']
    if q['format'] in ('statements','match-list','sequence') and 'Choose the correct' not in q['question']: q['question']+='\nChoose the correct answer from the options given below:'
    o['topic']=T[q['topic']]
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==50, len(qs)
meta['questions']=qs
p=f'CUET/English/CUET ENGLISH TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
